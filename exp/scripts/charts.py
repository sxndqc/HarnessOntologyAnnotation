"""Inline SVG charts for report.html: grouped horizontal bars and a diverging heatmap, with a hover/focus
tooltip. Colors come from CSS custom properties (light and dark steps, see CSS below); the palette is the
dataviz skill's reference instance (categorical slots 1-3 validated in both modes; slot 3 is under 3:1
on the light surface, so every chart sits above a table with its numbers)."""
import html
import json

CSS = """
.viz{--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;
 --s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;background:var(--surface);border:1px solid rgba(11,11,11,.10);
 border-radius:8px;padding:12px 14px;margin:.8rem 0;display:inline-block;max-width:100%;overflow-x:auto;vertical-align:top}
.viz svg{display:block;font-family:system-ui,-apple-system,"Segoe UI","PingFang SC",sans-serif}
.viz .t{fill:var(--ink);font-size:13px;font-weight:600} .viz .lab{fill:var(--ink2);font-size:12px}
.viz .tick{fill:var(--muted);font-size:11px;font-variant-numeric:tabular-nums} .viz .val{fill:var(--ink2);font-size:11px}
.viz .grid{stroke:var(--grid);stroke-width:1} .viz .base{stroke:var(--axis);stroke-width:1}
.viz .ref{stroke:var(--muted);stroke-width:1}
.viz .b1{fill:var(--s1)} .viz .b2{fill:var(--s2)} .viz .b3{fill:var(--s3)}
.viz .hit{fill:transparent;cursor:default} .viz .mk{pointer-events:none} .viz .hit:hover+.mk,.viz .hit:focus+.mk{opacity:.75}
.viz .cell{fill:var(--cl)} .viz .hit:focus{outline:none}
.viz .ring,.viz .dia{stroke:var(--surface);stroke-width:2;pointer-events:none} .viz .rk{fill:none;stroke:var(--ink2);stroke-width:1.5}
.viz .ring.s1,.viz .dia.s1{fill:var(--s1);filter:brightness(.72)} .viz .ring.s2,.viz .dia.s2{fill:var(--s2);filter:brightness(.72)}
.viz .ring.s3,.viz .dia.s3{fill:var(--s3);filter:brightness(.72)}
.metricbar{display:flex;gap:6px;margin:.6rem 0} .metricbar button{font:inherit;font-size:.85rem;padding:3px 10px;border-radius:6px;
 border:1px solid rgba(11,11,11,.15);background:transparent;color:inherit;cursor:pointer}
.metricbar button[aria-pressed="true"]{background:#2a78d6;color:#fff;border-color:#2a78d6}
[data-metric-view][hidden]{display:none}
.vizrow{display:flex;flex-wrap:wrap;gap:12px}
#viztip{position:fixed;pointer-events:none;z-index:10;background:var(--surface,#fcfcfb);color:#0b0b0b;
 border:1px solid rgba(11,11,11,.12);border-radius:6px;padding:6px 8px;font-size:12px;display:none;
 box-shadow:0 2px 8px rgba(0,0,0,.08);font-family:system-ui,-apple-system,"Segoe UI","PingFang SC",sans-serif}
#viztip .h{color:#52514e;margin-bottom:3px} #viztip .r{display:flex;align-items:center;gap:6px}
#viztip .k{width:12px;height:2px} #viztip b{font-variant-numeric:tabular-nums}
@media (prefers-color-scheme: dark){
 .metricbar button{border-color:rgba(255,255,255,.2)} .metricbar button[aria-pressed="true"]{background:#3987e5;border-color:#3987e5}
 .viz .ring.s1,.viz .dia.s1,.viz .ring.s2,.viz .dia.s2,.viz .ring.s3,.viz .dia.s3{filter:brightness(1.35)}
 .viz{--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--s1:#3987e5;--s2:#d95926;--s3:#199e70;
  border-color:rgba(255,255,255,.10)} .viz .cell{fill:var(--cd)}
 #viztip{background:#1a1a19;color:#f0efec;border-color:rgba(255,255,255,.12)} #viztip .h{color:#c3c2b7}}
"""

JS = """
(function(){var tip=document.createElement('div');tip.id='viztip';document.body.appendChild(tip);
function show(el,x,y){var d=JSON.parse(el.getAttribute('data-tip'));tip.textContent='';
 var h=document.createElement('div');h.className='h';h.textContent=d.h;tip.appendChild(h);
 d.rows.forEach(function(r){var row=document.createElement('div');row.className='r';
  if(r.c){var k=document.createElement('span');k.className='k';k.style.background=getComputedStyle(el).getPropertyValue(r.c);row.appendChild(k);}
  var b=document.createElement('b');b.textContent=r.v;row.appendChild(b);
  var s=document.createElement('span');s.textContent=r.n;row.appendChild(s);tip.appendChild(row);});
 tip.style.display='block';var w=tip.offsetWidth,hh=tip.offsetHeight;
 tip.style.left=Math.min(x+14,innerWidth-w-8)+'px';tip.style.top=Math.max(8,y-hh-10)+'px';}
document.querySelectorAll('.metricbar').forEach(function(bar){
 var group=bar.getAttribute('data-group');
 bar.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){
  bar.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
  document.querySelectorAll('[data-metric-group="'+group+'"]').forEach(function(v){
   v.hidden=v.getAttribute('data-metric-view')!==b.getAttribute('data-metric');});});});});
document.querySelectorAll('.viz [data-tip]').forEach(function(el){
 el.addEventListener('pointermove',function(e){show(el,e.clientX,e.clientY);});
 el.addEventListener('pointerleave',function(){tip.style.display='none';});
 el.addEventListener('focus',function(){var r=el.getBoundingClientRect();show(el,r.right,r.top);});
 el.addEventListener('blur',function(){tip.style.display='none';});});})();
"""


def _e(s):
    return html.escape(str(s), quote=True)


def _bar(x0, y, w, h, cls):
    """A horizontal bar from x0 with a 4px rounded data-end, square at the baseline."""
    if w <= 0:
        return ""
    r = min(4, w, h / 2)
    return ('<path class="mk %s" d="M%.1f,%.1f h%.1f a%.1f,%.1f 0 0 1 %.1f,%.1f v%.1f a%.1f,%.1f 0 0 1 %.1f,%.1f '
            'h%.1f z"/>' % (cls, x0, y, w - r, r, r, r, r, h - 2 * r, r, r, -r, r, -(w - r)))


def grouped_hbar(title, cats, series, xmax, unit="", step=10, refs=(), label_w=210, width=640, fmt="%.1f",
                 note_best=True, marks=None):
    """cats: [category]; series: [(name, slot 1-3, [value or None per category])]; refs: [(label, value)]
    drawn as solid hairlines. The best value of each series is labelled at its bar tip; every value is in
    the tooltip and in the table below the chart. marks: per series [(recall, precision) or None per
    category], drawn on the bar's row as a ring (recall) and a diamond (precision) in the series color;
    the bar is then the F1."""
    bar, gap, pad = (13 if marks else 11), 2, 10
    band = len(series) * bar + (len(series) - 1) * gap + pad * 2
    top, legend_h = 26, (38 if marks and refs else 22)
    plot_w = width - label_w - 40
    h = top + legend_h + band * len(cats) + 26
    sx = lambda v: label_w + plot_w * v / xmax
    out = ['<svg width="%d" height="%d" role="img" aria-label="%s">' % (width, h, _e(title)),
           '<text class="t" x="0" y="16">%s</text>' % _e(title)]
    lx = 0
    for name, slot, _ in series:   # legend: rect swatches (the mark is a bar)
        out.append('<rect class="b%d" x="%d" y="%d" width="10" height="10" rx="2"/>' % (slot, lx, top + 2))
        out.append('<text class="lab" x="%d" y="%d">%s</text>' % (lx + 14, top + 11, _e(name)))
        lx += 24 + 7.5 * len(name) + (6 * sum(1 for ch in name if ord(ch) > 0x2e80))
    if marks:                      # legend of the two markers, in neutral ink: shape only
        out.append('<text class="lab" x="%d" y="%d">条 = F1</text>' % (lx, top + 11))
        lx += 56
        out.append('<circle class="rk" cx="%d" cy="%d" r="4"/>' % (lx + 4, top + 7))
        out.append('<text class="lab" x="%d" y="%d">召回 R</text>' % (lx + 12, top + 11))
        lx += 62
        out.append('<path class="rk" d="M%d,%d l4.5,4.5 l-4.5,4.5 l-4.5,-4.5 z"/>' % (lx + 4, top + 2.5))
        out.append('<text class="lab" x="%d" y="%d">精确 P</text>' % (lx + 12, top + 11))
    y0 = top + legend_h
    v = 0
    while v <= xmax + 1e-9:          # hairline grid + ticks
        x = sx(v)
        out.append('<line class="grid" x1="%.1f" x2="%.1f" y1="%d" y2="%d"/>' % (x, x, y0, y0 + band * len(cats)))
        out.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">%s%s</text>' % (
            x, y0 + band * len(cats) + 16, ("%g" % v), unit))
        v += step
    for lab, val in refs:
        x = sx(val)
        out.append('<line class="ref" x1="%.1f" x2="%.1f" y1="%d" y2="%d"/>' % (x, x, y0 - 4, y0 + band * len(cats)))
        out.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, y0 - 7, _e(lab)))
    best = {i: max((x for x in s[2] if x is not None), default=None) for i, s in enumerate(series)}
    for ci, cat in enumerate(cats):
        yb = y0 + ci * band
        out.append('<text class="lab" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>' % (
            label_w - 10, yb + band / 2, _e(cat)))
        for si, (name, slot, vals) in enumerate(series):
            val = vals[ci]
            y = yb + pad + si * (bar + gap)
            tipd = {"h": cat, "rows": [{"v": ("–" if vv[2][ci] is None else (fmt % vv[2][ci]) + unit), "n": vv[0]
                                        + (" F1" if marks else ""), "c": "--s%d" % vv[1]} for vv in series]}
            if marks:
                for k, vv in enumerate(series):
                    rp = marks[k][ci]
                    if rp:
                        tipd["rows"].append({"v": "R %s · P %s" % tuple("–" if x is None else fmt % x for x in rp),
                                             "n": vv[0], "c": "--s%d" % vv[1]})
            out.append('<rect class="hit" tabindex="0" x="%d" y="%.1f" width="%d" height="%d" data-tip="%s"/>' % (
                label_w, y - gap, plot_w + 30, bar + 2 * gap, _e(json.dumps(tipd, ensure_ascii=False))))
            if val is None:
                out.append('<g class="mk"></g>')
                continue
            out.append(_bar(label_w, y, sx(val) - label_w, bar, "b%d" % slot))
            rp = marks[si][ci] if marks else None
            ends = [sx(val)]
            if rp:
                cy = y + bar / 2
                if rp[0] is not None:
                    out.append('<circle class="ring s%d" cx="%.1f" cy="%.1f" r="4.5"/>' % (slot, sx(rp[0]), cy))
                    ends.append(sx(rp[0]) + 6)
                if rp[1] is not None:
                    x = sx(rp[1])
                    out.append('<path class="dia s%d" d="M%.1f,%.1f l5.5,5.5 l-5.5,5.5 l-5.5,-5.5 z"/>' % (slot, x, cy - 5.5))
                    ends.append(x + 7)
            if note_best and val == best[si]:
                out.append('<text class="val" x="%.1f" y="%.1f" dominant-baseline="middle">%s%s</text>' % (
                    max(ends) + 4, y + bar / 2, fmt % val, unit))
        out.append('<line class="base" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (label_w, label_w, yb, yb + band))
    out.append("</svg>")
    return '<div class="viz">%s</div>' % "".join(out)


def _oklab(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = lin(r), lin(g), lin(b)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s, 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def _hex(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    g = lambda c: 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    return "#" + "".join("%02x" % round(255 * min(1, max(0, g(c)))) for c in rgb)


def _mix(c1, c2, t):
    a, b = _oklab(c1), _oklab(c2)
    return _hex(tuple(x + (y - x) * t for x, y in zip(a, b)))


DIV = {"light": ("#e34948", "#f0efec", "#2a78d6"), "dark": ("#e66767", "#383835", "#3987e5")}


def heatmap(title, rows, cols, values, vmax=20, unit="", label_w=200, cell=(58, 22)):
    """values[r][c] (or None): a diverging heatmap, blue = higher than the baseline, red = lower, gray =
    no change; the color saturates at ±vmax. No numbers in the cells: the tooltip and the table below
    carry them."""
    cw, ch = cell
    top = 72
    w = label_w + cw * len(cols) + 10
    h = top + ch * len(rows) + 40
    out = ['<svg width="%d" height="%d" role="img" aria-label="%s">' % (w, h, _e(title)),
           '<text class="t" x="0" y="16">%s</text>' % _e(title)]
    for ci, c in enumerate(cols):     # column labels, two lines
        x = label_w + ci * cw + cw / 2
        parts = c.split("\n")
        for k, p in enumerate(parts):
            out.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, top - 26 + 12 * k, _e(p)))
    for ri, r in enumerate(rows):
        y = top + ri * ch
        out.append('<text class="lab" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>' % (
            label_w - 8, y + ch / 2, _e(r)))
        for ci, c in enumerate(cols):
            v = values[ri][ci]
            x = label_w + ci * cw
            if v is None:
                cl = cd = None
            else:
                t = max(-1, min(1, v / vmax))
                cl = _mix(DIV["light"][1], DIV["light"][2] if t > 0 else DIV["light"][0], abs(t))
                cd = _mix(DIV["dark"][1], DIV["dark"][2] if t > 0 else DIV["dark"][0], abs(t))
            tipd = {"h": "%s · %s" % (r, c.replace("\n", " ")), "rows": [{"v": "–" if v is None else "%+.1f%s" % (v, unit),
                                                                          "n": "相对 abridged"}]}
            out.append('<rect class="hit" tabindex="0" x="%d" y="%d" width="%d" height="%d" data-tip="%s"/>' % (
                x, y, cw, ch, _e(json.dumps(tipd, ensure_ascii=False))))
            if cl:
                out.append('<rect class="mk cell" style="--cl:%s;--cd:%s" x="%d" y="%d" width="%d" height="%d" rx="3"/>' % (
                    cl, cd, x + 1, y + 1, cw - 2, ch - 2))
            else:
                out.append('<g class="mk"></g>')
    # scale legend: red arm, gray midpoint, blue arm
    ly = top + ch * len(rows) + 14
    for k in range(11):
        t = (k - 5) / 5
        cl = _mix(DIV["light"][1], DIV["light"][2] if t > 0 else DIV["light"][0], abs(t))
        cd = _mix(DIV["dark"][1], DIV["dark"][2] if t > 0 else DIV["dark"][0], abs(t))
        out.append('<rect class="cell" style="--cl:%s;--cd:%s" x="%d" y="%d" width="18" height="10" rx="2"/>' % (
            cl, cd, label_w + 20 * k, ly))
    out.append('<text class="tick" x="%d" y="%d" text-anchor="end">−%d%s 更低</text>' % (label_w - 6, ly + 9, vmax, unit))
    out.append('<text class="tick" x="%d" y="%d">+%d%s 更高</text>' % (label_w + 20 * 11 + 4, ly + 9, vmax, unit))
    out.append("</svg>")
    return '<div class="viz">%s</div>' % "".join(out)


def facet_hbar(title, cats, facets, series, xmax=100, step=20, label_w=150, panel_w=200, gap=22, fmt="%.1f",
               refs=None):
    """One chart, several metrics side by side sharing the category rows (small multiples on one axis
    each, all 0..xmax so the panels compare). facets: [(metric name, {series index: [value per cat]},
    {series index: [(recall, precision) or None per cat]} or None)]; series: [(name, slot)]; refs:
    {facet index: [(label, value)]} drawn as hairlines. Bars are F1; a ring is recall, a diamond
    precision. Every value is in the tooltip and in the table below the chart."""
    bar, bgap, pad = 13, 2, 9
    band = len(series) * bar + (len(series) - 1) * bgap + pad * 2
    top = 26
    any_marks = any(f[2] for f in facets)
    legend_h, head_h = 22, (36 if refs else 22)
    y0 = top + legend_h + head_h
    width = label_w + len(facets) * (panel_w + gap)
    h = y0 + band * len(cats) + 24
    out = ['<svg width="%d" height="%d" role="img" aria-label="%s">' % (width, h, _e(title)),
           '<text class="t" x="0" y="16">%s</text>' % _e(title)]
    lx = 0
    for name, slot in series:
        out.append('<rect class="b%d" x="%d" y="%d" width="10" height="10" rx="2"/>' % (slot, lx, top + 2))
        out.append('<text class="lab" x="%d" y="%d">%s</text>' % (lx + 14, top + 11, _e(name)))
        lx += 24 + 7.5 * len(name) + (6 * sum(1 for ch in name if ord(ch) > 0x2e80))
    if any_marks:
        out.append('<text class="lab" x="%d" y="%d">条 = F1</text>' % (lx, top + 11))
        lx += 56
        out.append('<circle class="rk" cx="%d" cy="%d" r="4"/>' % (lx + 4, top + 7))
        out.append('<text class="lab" x="%d" y="%d">召回 R</text>' % (lx + 12, top + 11))
        lx += 62
        out.append('<path class="rk" d="M%d,%d l4.5,4.5 l-4.5,4.5 l-4.5,-4.5 z"/>' % (lx + 4, top + 2.5))
        out.append('<text class="lab" x="%d" y="%d">精确 P</text>' % (lx + 12, top + 11))
    for ci, cat in enumerate(cats):
        yb = y0 + ci * band
        out.append('<text class="lab" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>' % (
            label_w - 10, yb + band / 2, _e(cat)))
    for fi, (metric, vals, marks) in enumerate(facets):
        x0 = label_w + fi * (panel_w + gap)
        sx = lambda v, x0=x0: x0 + panel_w * v / xmax
        out.append('<text class="t" x="%d" y="%d" style="font-size:12px">%s</text>' % (x0, top + legend_h + 12, _e(metric)))
        v = 0
        while v <= xmax + 1e-9:
            x = sx(v)
            out.append('<line class="grid" x1="%.1f" x2="%.1f" y1="%d" y2="%d"/>' % (x, x, y0, y0 + band * len(cats)))
            out.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">%g</text>' % (x, y0 + band * len(cats) + 14, v))
            v += step
        for lab, val in (refs or {}).get(fi, []):
            x = sx(val)
            out.append('<line class="ref" x1="%.1f" x2="%.1f" y1="%d" y2="%d"/>' % (x, x, y0 - 4, y0 + band * len(cats)))
            out.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, y0 - 7, _e(lab)))
        for ci, cat in enumerate(cats):
            yb = y0 + ci * band
            rows = []
            for si, (name, slot) in enumerate(series):
                val = vals.get(si, [None] * len(cats))[ci]
                rp = (marks or {}).get(si, [None] * len(cats))[ci]
                txt = "–" if val is None else fmt % val
                if rp:
                    txt += "（R %s · P %s）" % tuple("–" if x is None else fmt % x for x in rp)
                rows.append({"v": txt, "n": name, "c": "--s%d" % slot})
            tipd = {"h": "%s · %s" % (cat, metric), "rows": rows}
            for si, (name, slot) in enumerate(series):
                val = vals.get(si, [None] * len(cats))[ci]
                y = yb + pad + si * (bar + bgap)
                out.append('<rect class="hit" tabindex="0" x="%d" y="%.1f" width="%d" height="%d" data-tip="%s"/>' % (
                    x0, y - bgap, panel_w, bar + 2 * bgap, _e(json.dumps(tipd, ensure_ascii=False))))
                if val is None:
                    out.append('<g class="mk"></g>')
                    continue
                out.append(_bar(x0, y, sx(val) - x0, bar, "b%d" % slot))
                rp = (marks or {}).get(si, [None] * len(cats))[ci]
                if rp:
                    cy = y + bar / 2
                    if rp[0] is not None:
                        out.append('<circle class="ring s%d" cx="%.1f" cy="%.1f" r="4.5"/>' % (slot, sx(rp[0]), cy))
                    if rp[1] is not None:
                        out.append('<path class="dia s%d" d="M%.1f,%.1f l5.5,5.5 l-5.5,5.5 l-5.5,-5.5 z"/>' % (
                            slot, sx(rp[1]), cy - 5.5))
            out.append('<line class="base" x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (x0, x0, yb, yb + band))
    out.append("</svg>")
    return '<div class="viz">%s</div>' % "".join(out)
