#!/usr/bin/env node
// usage: node validate.js <doc-id> [--show <proposal-id>] [--quiet]
//   doc-id: zh-0001 ... (data/docs.json); reads review/proposals/<doc-id>.json and data/gold/<gold name>.umr
//   Every proposal must apply cleanly to the gold on its own, and all of them together (in order) too.
const fs = require('fs'), path = require('path'), E = require('./engine.js');
const DOCS = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'docs.json'), 'utf8')).docs;
const doc = process.argv[2], show = process.argv.indexOf('--show') > 0 ? process.argv[process.argv.indexOf('--show') + 1] : null;
const entry = DOCS.find(d => d.doc === doc);
if (!entry) { console.log('usage: node review/validate.js <doc-id> [--show <proposal-id>] [--quiet]'); process.exit(2); }
const gold = E.splitDoc(require('./goldtext.js').read(entry));
const fileArg = process.argv.indexOf('--file') > 0 ? process.argv[process.argv.indexOf('--file') + 1] : null;   // another proposals file than review/proposals/<doc>.json
const P = JSON.parse(fs.readFileSync(fileArg || path.join(__dirname, 'proposals', doc + '.json'), 'utf8'));
let bad = 0, total = 0; const ids = new Set();
const OPS = ['add_node', 'del_node', 'rename', 'add_rel', 'del_rel', 'mod_rel', 'set_attr', 'del_attr', 'doc_add', 'doc_del', 'doc_mod', 'align', 'del_align', 'set_root'];
for (const b of gold.blocks) {
  let base; const list = P[String(b.n)] || [];
  try { base = E.loadState(b); } catch (e) { if (list.length) { bad += list.length; console.log(`[snt${b.n}] the gold graph of this sentence cannot be read (${e.message}): no fix can be written for it; ${list.length} fix(es) given`); } continue; }
  const baseErr = new Set(E.validate(base, b.n));
  let merged = E.clone(base); const seenExcl = new Set();
  for (const p of list) {
    total++; const tag = `[snt${b.n}] ${p.id}`;
    for (const f of ['id', 'title', 'why', 'refs', 'conf', 'ops']) if (p[f] === undefined) { console.log(tag, 'MISSING FIELD', f); bad++; }
    if (ids.has(p.id)) { console.log(tag, 'DUPLICATE ID'); bad++; } ids.add(p.id);
    if (!['high', 'mid', 'low'].includes(p.conf)) { console.log(tag, 'conf must be high|mid|low'); bad++; }
    for (const o of p.ops || []) if (!OPS.includes(o.op)) { console.log(tag, 'UNKNOWN OP', o.op); bad++; }
    const r = E.applyOps(base, p.ops || []);
    const errs = E.validate(r.state, b.n).filter(e => !baseErr.has(e));
    const noops = r.log.filter(l => l.status === 'noop');
    if (r.failed || errs.length || noops.length) {
      bad++; console.log(tag, r.failed ? 'FAILED' : 'PROBLEM');
      r.log.forEach((l, i) => { if (l.status !== 'ok') console.log('   op#' + i, l.status, JSON.stringify(p.ops[i]), '→', l.text); });
      errs.forEach(e => console.log('   new validation error:', e));
    }
    if (show === p.id) {
      console.log('=== ' + p.id + ' : ' + p.title); r.log.forEach(l => console.log('  [' + l.kind + '] ' + l.label + ': ' + l.text));
      const a = E.serState(base), z = E.serState(r.state);
      for (const k of ['graph', 'al', 'doc']) E.diffLines(a[k], z[k]).forEach(([t, s], i, arr) => { if (t !== ' ' || (arr[i - 1] && arr[i - 1][0] !== ' ') || (arr[i + 1] && arr[i + 1][0] !== ' ')) console.log(t + ' ' + s); });
    }
    if (p.excl) { if (seenExcl.has(p.excl)) continue; seenExcl.add(p.excl); }
    const m = E.applyOps(merged, p.ops || []);
    if (m.failed) { bad++; console.log(tag, 'CONFLICT when merged after earlier proposals:', m.log.filter(l => l.status === 'fail').map(l => l.text).join('; ')); }
    merged = m.state;
  }
  const mErr = E.validate(merged, b.n).filter(e => !baseErr.has(e));
  if (mErr.length) { console.log(`[snt${b.n}] merged-all validation errors:`); mErr.forEach(e => console.log('   ', e)); }
  try { E.parseGraph(E.serGraph(merged.g)); E.parseDoc(E.serDoc(merged.doc)); } catch (e) { console.log(`[snt${b.n}] merged output does not re-parse:`, e.message); bad++; }
  if (!process.argv.includes('--quiet')) console.log(`snt${b.n}: ${list.length} proposals; gold baseline warnings: ${baseErr.size}`);
}
if (process.argv.includes('--quiet')) {} 
for (const k of Object.keys(P)) if (!gold.blocks.some(b => String(b.n) === k)) { console.log('unknown sentence key', k); bad++; }
console.log(bad ? `\n${bad} problem(s) in ${total} proposals` : `\nOK: ${total} proposals all apply cleanly`);
process.exit(bad ? 1 : 0);
