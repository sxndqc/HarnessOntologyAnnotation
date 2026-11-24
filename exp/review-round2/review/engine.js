/* UMR graph engine: parse / edit ops / serialize / diff. Shared by the HTML page and the node validator. */
(function (root) {
  const E = {};
  const tokenize = s => s.match(/\(|\)|"(?:[^"\\]|\\.)*"|\/(?=\s)|[^\s()]+?(?=\/\s|[\s()]|$)/g) || [];

  /* ---------- sentence graph ---------- */
  E.parseGraph = function (text) {
    const tk = tokenize(text); let i = 0;
    const g = { root: null, nodes: {}, edges: [] };
    const vars = new Set();
    for (let k = 0; k < tk.length - 2; k++) if (tk[k] === '(' && tk[k + 2] === '/') vars.add(tk[k + 1]);
    function node() {
      i++; const v = tk[i++];
      if (tk[i] !== '/') throw new Error('expected / after ' + v); i++;
      g.nodes[v] = tk[i++];
      while (tk[i] !== ')') {
        const r = tk[i++];
        if (r === undefined || r[0] !== ':') throw new Error('expected role, got ' + r);
        if (tk[i] === '(') { const e = { s: v, r, t: null, v: true, def: true }; g.edges.push(e); e.t = node(); }
        else { const a = tk[i++]; g.edges.push({ s: v, r, t: a, v: vars.has(a), def: false }); }
      }
      i++; return v;
    }
    g.root = node();
    return g;
  };
  E.reachable = function (g) {
    const seen = new Set([g.root]); const st = [g.root];
    while (st.length) { const v = st.pop(); for (const e of g.edges) if (e.s === v && e.v && e.t in g.nodes && !seen.has(e.t)) { seen.add(e.t); st.push(e.t); } }
    return seen;
  };
  E.serGraph = function (g) {
    function run(useDef) {
      const seen = new Set();
      function rec(v, ind) {
        seen.add(v);
        let s = '(' + v + ' / ' + g.nodes[v];
        const mine = g.edges.filter(e => e.s === v), isOp = e => /^:op\d+$/.test(e.r);
        const ops = mine.filter(isOp).sort((x, y) => +x.r.slice(3) - +y.r.slice(3)); let oi = 0;
        for (const e0 of mine) {
          const e = isOp(e0) ? ops[oi++] : e0;
          s += '\n' + ' '.repeat(ind + 4) + e.r + ' ';
          if (!e.v || !(e.t in g.nodes) || seen.has(e.t)) s += e.t;
          else if (useDef && !e.def && g.edges.some(x => x !== e && x.def && x.v && x.t === e.t && x.s in g.nodes)) s += e.t;
          else s += rec(e.t, ind + 4);
        }
        return s + ')';
      }
      return { text: rec(g.root, 0), n: seen.size };
    }
    const a = run(true);
    if (a.n >= E.reachable(g).size) return a.text;
    return run(false).text;
  };

  /* ---------- document-level annotation ---------- */
  const KINDS = ['temporal', 'modal', 'coref'];
  E.parseDoc = function (text) {
    const tk = tokenize(text); const d = { head: null, lists: {}, present: [] };
    if (!tk.length) return d;
    let i = 1; d.head = tk[i]; i += 3;
    while (tk[i] && tk[i] !== ')') {
      const kind = tk[i++].slice(1); d.present.push(kind); d.lists[kind] = [];
      if (tk[i] !== '(') throw new Error('doc: expected ( after :' + kind); i++;
      while (tk[i] === '(') { d.lists[kind].push([tk[i + 1], tk[i + 2], tk[i + 3]]); if (tk[i + 4] !== ')') throw new Error('doc: bad triple near ' + tk[i + 1]); i += 5; }
      if (tk[i] !== ')') throw new Error('doc: expected ) closing :' + kind); i++;
    }
    return d;
  };
  E.serDoc = function (d) {
    let s = '(' + d.head + ' / sentence';
    for (const k of d.present.concat(KINDS.filter(k => !d.present.includes(k)), Object.keys(d.lists).filter(k => !KINDS.includes(k) && !d.present.includes(k)))) {
      const L = d.lists[k]; if (!L) continue;
      if (!L.length && !d.present.includes(k)) continue;
      const pad = '\n' + ' '.repeat(4 + k.length + 3);
      s += '\n    :' + k + ' (' + L.map(t => '(' + t.join(' ') + ')').join(pad) + ')';
    }
    return s + ')';
  };

  /* ---------- alignment ---------- */
  E.parseAl = text => text.split('\n').map(l => l.trim()).filter(Boolean).map(l => { const k = l.indexOf(':'); return [l.slice(0, k).trim(), l.slice(k + 1).trim()]; });
  E.serAl = al => al.map(a => a[0] + ': ' + a[1]).join('\n');

  /* ---------- gold file splitting ---------- */
  const H_G = '# sentence level graph:', H_A = '# alignment:', H_D = '# document level annotation:';
  E.splitDoc = function (text) {
    const parts = text.split(/(?=^#{20,}\s*$)/m); const out = { prefix: '', blocks: [] };
    for (const raw of parts) {
      const m = raw.match(/# :: snt(\d+)/);
      if (!m || raw.indexOf(H_G) < 0) { if (!out.blocks.length) out.prefix += raw; else out.blocks[out.blocks.length - 1].raw += raw; continue; }
      const iG = raw.indexOf(H_G), iA = raw.indexOf(H_A), iD = raw.indexOf(H_D);
      const docPart = raw.slice(iD + H_D.length);
      const words = (raw.match(/^Words:\s*(.*)$/m) || [, ''])[1].trim().split(/\s+/);
      out.blocks.push({
        n: +m[1], raw, pre: raw.slice(0, iG + H_G.length) + '\n', words,
        graphText: raw.slice(iG + H_G.length, iA).trim(), alText: raw.slice(iA + H_A.length, iD).trim(),
        docText: docPart.trim(), tail: docPart.slice(docPart.trimEnd().length)
      });
    }
    return out;
  };
  E.loadState = b => ({ g: E.parseGraph(b.graphText), doc: E.parseDoc(b.docText), al: E.parseAl(b.alText) });
  E.clone = st => JSON.parse(JSON.stringify(st));
  E.serBlock = (b, st) => b.pre + E.serGraph(st.g) + '\n\n' + H_A + '\n' + E.serAl(st.al) + '\n\n' + H_D + '\n' + E.serDoc(st.doc) + (b.tail || '\n');
  E.serState = st => ({ graph: E.serGraph(st.g), al: E.serAl(st.al), doc: E.serDoc(st.doc) });

  /* ---------- edit operations ----------
     add_node {parent, role, var, concept, attrs?, align?}   del_node {var, subtree?}   rename {var, concept}
     add_rel {s, r, t}   del_rel {s, r, t}   mod_rel {s, r, t, r2}
     set_attr {var, attr, value}   del_attr {var, attr}
     doc_add {kind, triple}   doc_del {kind, triple}   doc_mod {kind, triple, to}
     align {var, span}   del_align {var}   set_root {var}                                            */
  const nm = (g, v) => v in g.nodes ? v + ' / ' + g.nodes[v] : v;
  const role = r => r[0] === ':' ? r : ':' + r;
  const eqT = (a, b) => a[0] === b[0] && a[1] === b[1] && a[2] === b[2];
  function findEdge(g, s, r, t) { return g.edges.findIndex(e => e.s === s && e.r === r && (t === undefined || e.t === String(t))); }
  const T3 = t => [String(t[0]), role(String(t[1])), String(t[2])];
  E.applyOp = function (st, op) {
    if (op.triple) op = Object.assign({}, op, { triple: T3(op.triple) }, op.to ? { to: T3(op.to) } : {});
    const g = st.g, R = (status, kind, label, text) => ({ status, kind, label, text });
    const need = v => { if (!(v in g.nodes)) throw new Error('节点 ' + v + ' 不存在'); };
    try {
      switch (op.op) {
        case 'add_node': {
          need(op.parent); const r = role(op.role);
          if (op.var in g.nodes) { if (g.nodes[op.var] === op.concept) return R('noop', 'add', '新增 node', op.var + ' 已存在'); throw new Error('变量 ' + op.var + ' 已被占用'); }
          g.nodes[op.var] = op.concept; g.edges.push({ s: op.parent, r, t: op.var, v: true, def: true });
          let txt = nm(g, op.parent) + '  ' + r + '  (' + op.var + ' / ' + op.concept;
          for (const k in (op.attrs || {})) { g.edges.push({ s: op.var, r: role(k), t: String(op.attrs[k]), v: String(op.attrs[k]) in g.nodes, def: false }); txt += ' ' + role(k) + ' ' + op.attrs[k]; }
          st.al.push([op.var, op.align || '0-0']);
          return R('ok', 'add', '新增 node', txt + ')' + '   对齐 ' + (op.align || '0-0'));
        }
        case 'del_node': {
          if (!(op.var in g.nodes)) return R('noop', 'del', '删除 node', op.var + ' 已不存在');
          if (op.var === g.root) throw new Error('不能删除根节点');
          const txt = nm(g, op.var); let gone = [op.var];
          delete g.nodes[op.var]; g.edges = g.edges.filter(e => e.s !== op.var && !(e.v && e.t === op.var));
          if (op.subtree) { const keep = E.reachable(g); for (const v of Object.keys(g.nodes)) if (!keep.has(v)) { gone.push(v); delete g.nodes[v]; } g.edges = g.edges.filter(e => e.s in g.nodes && (!e.v || e.t in g.nodes)); }
          const G = new Set(gone);
          st.al = st.al.filter(a => !G.has(a[0]));
          for (const k in st.doc.lists) st.doc.lists[k] = st.doc.lists[k].filter(t => !G.has(t[0]) && !G.has(t[2]));
          return R('ok', 'del', '删除 node', txt + (gone.length > 1 ? '  （连同子节点 ' + gone.slice(1).join(', ') + '）' : '') + '，及其对齐、文档级三元组');
        }
        case 'rename': {
          need(op.var); const old = g.nodes[op.var];
          if (old === op.concept) return R('noop', 'mod', '修改 node 名', op.var + ' 已是 ' + op.concept);
          g.nodes[op.var] = op.concept; return R('ok', 'mod', '修改 node 名', op.var + ' / ' + old + '  →  ' + op.concept);
        }
        case 'add_rel': {
          need(op.s); const r = role(op.r), t = String(op.t), isV = t in g.nodes;
          if (findEdge(g, op.s, r, t) >= 0) return R('noop', 'add', '新增 relation', '已存在');
          g.edges.push({ s: op.s, r, t, v: isV, def: false });
          return R('ok', 'add', isV ? '新增 relation' : '添加 attribute', nm(g, op.s) + '  ' + r + '  ' + nm(g, t));
        }
        case 'del_rel': {
          const r = role(op.r), i = findEdge(g, op.s, r, op.t);
          if (i < 0) { if (!(op.s in g.nodes)) return R('noop', 'del', '删除 relation', '源节点已不存在'); throw new Error('找不到 relation ' + op.s + ' ' + r + ' ' + op.t); }
          const e = g.edges[i]; const txt = nm(g, e.s) + '  ' + r + '  ' + nm(g, e.t); g.edges.splice(i, 1);
          return R('ok', 'del', '删除 relation', txt);
        }
        case 'mod_rel': {
          const r = role(op.r), r2 = role(op.r2), i = findEdge(g, op.s, r, op.t);
          if (i < 0) { if (findEdge(g, op.s, r2, op.t) >= 0) return R('noop', 'mod', '修改 relation', '已是 ' + r2); throw new Error('找不到 relation ' + op.s + ' ' + r + ' ' + op.t); }
          g.edges[i].r = r2; return R('ok', 'mod', '修改 relation', nm(g, op.s) + '  ' + r + ' → ' + r2 + '  ' + nm(g, g.edges[i].t));
        }
        case 'set_attr': {
          need(op.var); const r = role(op.attr), v = String(op.value), i = g.edges.findIndex(e => e.s === op.var && e.r === r && !e.v);
          if (i < 0) { g.edges.push({ s: op.var, r, t: v, v: false, def: false }); return R('ok', 'add', '添加 attribute', nm(g, op.var) + '  ' + r + ' ' + v); }
          const old = g.edges[i].t; if (old === v) return R('noop', 'mod', '修改 attribute', '已是 ' + v);
          g.edges[i].t = v; return R('ok', 'mod', '修改 attribute', nm(g, op.var) + '  ' + r + ' ' + old + '  →  ' + v);
        }
        case 'del_attr': {
          const r = role(op.attr), i = g.edges.findIndex(e => e.s === op.var && e.r === r && !e.v);
          if (i < 0) return R('noop', 'del', '删除 attribute', op.var + ' 没有 ' + r);
          const txt = nm(g, op.var) + '  ' + r + ' ' + g.edges[i].t; g.edges.splice(i, 1); return R('ok', 'del', '删除 attribute', txt);
        }
        case 'set_root': { need(op.var); const old = g.root; g.root = op.var; return R('ok', 'mod', '修改根节点', old + ' → ' + nm(g, op.var)); }
        case 'doc_add': {
          const L = st.doc.lists[op.kind] || (st.doc.lists[op.kind] = []);
          if (L.some(t => eqT(t, op.triple))) return R('noop', 'add', '新增 ' + op.kind, '已存在');
          L.push(op.triple.slice()); return R('ok', 'add', '新增 ' + op.kind, '(' + op.triple.join(' ') + ')');
        }
        case 'doc_del': {
          const L = st.doc.lists[op.kind] || [], i = L.findIndex(t => eqT(t, op.triple));
          if (i < 0) return R('noop', 'del', '删除 ' + op.kind, '(' + op.triple.join(' ') + ') 已不存在');
          L.splice(i, 1); return R('ok', 'del', '删除 ' + op.kind, '(' + op.triple.join(' ') + ')');
        }
        case 'doc_mod': {
          const L = st.doc.lists[op.kind] || [], i = L.findIndex(t => eqT(t, op.triple));
          if (i < 0) { if (L.some(t => eqT(t, op.to))) return R('noop', 'mod', '修改 ' + op.kind, '已是目标值'); throw new Error('找不到 ' + op.kind + ' 三元组 (' + op.triple.join(' ') + ')'); }
          L[i] = op.to.slice(); return R('ok', 'mod', '修改 ' + op.kind, '(' + op.triple.join(' ') + ')  →  (' + op.to.join(' ') + ')');
        }
        case 'align': {
          const i = st.al.findIndex(a => a[0] === op.var);
          if (i < 0) { st.al.push([op.var, op.span]); return R('ok', 'add', '新增对齐', op.var + ': ' + op.span); }
          const old = st.al[i][1]; if (old === op.span) return R('noop', 'mod', '修改对齐', '已是 ' + op.span);
          st.al[i][1] = op.span; return R('ok', 'mod', '修改对齐', nm(g, op.var) + ': ' + old + '  →  ' + op.span);
        }
        case 'del_align': {
          const i = st.al.findIndex(a => a[0] === op.var);
          if (i < 0) return R('noop', 'del', '删除对齐', op.var + ' 无对齐行');
          const txt = op.var + ': ' + st.al[i][1]; st.al.splice(i, 1); return R('ok', 'del', '删除对齐', txt);
        }
        default: throw new Error('未知操作 ' + op.op);
      }
    } catch (err) { return R('fail', 'mod', op.op, err.message); }
  };
  /* apply a whole proposal atomically: on any failure the state is left untouched */
  E.applyOps = function (st, ops) {
    const work = E.clone(st), log = ops.map(op => E.applyOp(work, op));
    const failed = log.some(l => l.status === 'fail');
    return { state: failed ? st : work, log, failed };
  };
  E.validate = function (st, n) {
    const g = st.g, errs = [], pre = new RegExp('^s' + n + '[a-z]'), reach = E.reachable(g);
    for (const v in g.nodes) if (!reach.has(v)) errs.push('节点 ' + v + ' / ' + g.nodes[v] + ' 从根不可达（悬空）');
    for (const e of g.edges) if (!e.v && pre.test(e.t) && !/^s\d+s0$/.test(e.t)) errs.push('relation ' + e.s + ' ' + e.r + ' 指向不存在的变量 ' + e.t);
    for (const k in st.doc.lists) for (const t of st.doc.lists[k]) for (const x of [t[0], t[2]]) if (pre.test(x) && !(x in g.nodes)) errs.push(k + ' 三元组 (' + t.join(' ') + ') 引用了图中不存在的 ' + x);
    const alv = new Set(st.al.map(a => a[0]));
    for (const a of st.al) if (!(a[0] in g.nodes)) errs.push('对齐行 ' + a[0] + ' 在图中不存在');
    for (const v in g.nodes) if (!alv.has(v)) errs.push('节点 ' + v + ' 没有对齐行');
    return errs;
  };

  /* ---------- line diff (LCS) ---------- */
  E.diffLines = function (a, b) {
    const A = a.split('\n'), B = b.split('\n'), n = A.length, m = B.length;
    const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
    for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) dp[i][j] = A[i] === B[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    const out = []; let i = 0, j = 0;
    while (i < n && j < m) { if (A[i] === B[j]) { out.push([' ', A[i]]); i++; j++; } else if (dp[i + 1][j] >= dp[i][j + 1]) out.push(['-', A[i++]]); else out.push(['+', B[j++]]); }
    while (i < n) out.push(['-', A[i++]]); while (j < m) out.push(['+', B[j++]]);
    return out;
  };
  E.KINDS = KINDS;
  if (typeof module !== 'undefined' && module.exports) module.exports = E; else root.UMR = E;
})(typeof window !== 'undefined' ? window : globalThis);
