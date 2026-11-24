"""analysis/breakdown.html: heatmaps of the change of every breakdown F1 against a reference setting.

    python3 pipeline/breakdown_chart.py      (after pipeline/breakdown.py)

A cell is the F1 of a setting (mean of its two runs) minus the F1 of the reference setting (mean of its two
runs): s1-full for the 31 Chinese documents (the baseline did not run on the non-test ones), the one-sentence
baseline s0 for the test set.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

NAMES = {"s0": "s0 baseline", "s1f": "full", "s3": "+三个工具", "a2": "a2"}
B = json.load(open(os.path.join(C.ANALYSIS, "breakdown.json"), encoding="utf-8"))
panels = []
for G in B["groups"]:
    conds = list(dict.fromkeys(k.split("/")[0] for k in G["systems"]))
    ref = conds[0]
    rows = []
    for key, name in B["rows"]:
        runs = {c: [G["systems"][k][key] for k in G["systems"] if k.split("/")[0] == c] for c in conds}
        if any(v is None for vs in runs.values() for v in vs):
            continue
        mean = {c: sum(v) / len(v) for c, v in runs.items()}
        rows.append({"name": name, "n": G["systems"][ref + "/r1"].get(key + "_n"), "ref": round(mean[ref], 1),
                     "cells": [{"d": round(mean[c] - mean[ref], 1), "v": round(mean[c], 1), "runs": runs[c]} for c in conds[1:]]})
    panels.append({"id": G["id"], "title": G["title"], "ref": NAMES[ref], "cols": [NAMES[c] for c in conds[1:]], "rows": rows, "ndocs": len(G["docs"])})
HTML = r"""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>GPT-6.1 Sol：分项 F1 在各设定下的变化</title>
<style>
body{font:14px/1.5 -apple-system,"PingFang SC","Helvetica Neue",sans-serif;color:#1f1f1c;background:#faf9f6;margin:24px}
h1{font-size:20px;margin:0 0 6px} p.note{color:#55534d;max-width:980px;margin:4px 0 14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(470px,1fr));gap:16px}
.card{background:#fff;border:1px solid #e3e1da;border-radius:12px;padding:16px 18px}
.card.wide{grid-column:1/-1;max-width:760px}
.card h2{font-size:15px;margin:0 0 2px} .card .sub{color:#77756e;font-size:12px;margin-bottom:10px}
table{border-collapse:separate;border-spacing:4px;width:100%}
th{font-weight:400;color:#77756e;font-size:12.5px;padding:2px 4px;text-align:center}
td.l{text-align:right;color:#3d3c38;white-space:nowrap;padding-right:8px;font-size:13px}
td.r{text-align:right;color:#77756e;font-variant-numeric:tabular-nums;font-size:12.5px;padding-right:6px}
td.c{height:26px;border-radius:5px;text-align:center;font-variant-numeric:tabular-nums;font-size:12.5px;min-width:64px}
.legend{display:flex;align-items:center;gap:4px;color:#77756e;font-size:12.5px;margin:14px 0 4px}
.legend i{width:30px;height:14px;border-radius:3px;display:inline-block}
</style>
<h1>GPT-6.1 Sol：分项 F1 相对基准设定的变化（分）</h1>
<p class="note">每格是该设定两次运行的平均 F1 减去基准设定两次运行的平均 F1；格里的数字是差值，鼠标停在格上可以看两次运行各自的 F1。"基准 F1"一列是基准设定的绝对分数。
中文 31 篇的基准是 full（s1-full，完整 guideline、无工具），因为 baseline 没有跑非测试文档；测试集的基准是 s0 baseline（一句话 guideline、无工具）。这一轮没有跑 abridged 无工具、+search、+PropBank、+gold、a1 这几个设定，所以没有这些列。
分项是这次新写的脚本算的（节点按对齐的词对应），和你那张图的打分器不是同一个，绝对数值不能直接对比。</p>
<div class="legend">−20 更低 __LEGEND__ +20 更高</div>
<div class="grid" id="g"></div>
<script>
const P=__DATA__;
const RAMP=["#d6604d","#e07f72","#e8a097","#edbcb5","#f0d8d3","#efeeea","#d3dbe9","#b3c4e3","#8eaadb","#6a90d4","#4376cc"];
function col(d){const i=Math.max(0,Math.min(10,Math.round(d/4)+5));return RAMP[i]}
function ink(d){return Math.abs(d)>=14?"#fff":"#2b2a27"}
document.getElementById("g").innerHTML=P.map((p,k)=>'<div class="card'+(k<2?' wide':'')+'"><h2>'+p.title+'</h2><div class="sub">基准：'+p.ref+'　'+p.ndocs+' 篇</div><table><tr><th></th><th>基准 F1</th>'+p.cols.map(c=>'<th>'+c+'</th>').join('')+'</tr>'+
 p.rows.map(r=>'<tr><td class="l">'+r.name+'</td><td class="r">'+r.ref.toFixed(1)+'</td>'+r.cells.map(c=>'<td class="c" style="background:'+col(c.d)+';color:'+ink(c.d)+'" title="F1 '+c.v.toFixed(1)+'（两次运行：'+c.runs.join('、')+'）'+(r.n!=null?'；gold 里 '+r.n+' 个':'')+'">'+(c.d>0?'+':c.d<0?'−':'')+Math.abs(c.d).toFixed(1)+'</td>').join('')+'</tr>').join('')+'</table></div>').join('');
</script></html>"""
ramp = ["#d6604d", "#e07f72", "#e8a097", "#edbcb5", "#f0d8d3", "#efeeea", "#d3dbe9", "#b3c4e3", "#8eaadb", "#6a90d4", "#4376cc"]
html = HTML.replace("__DATA__", json.dumps(panels, ensure_ascii=False)).replace("__LEGEND__", "".join('<i style="background:%s"></i>' % c for c in ramp))
out = os.path.join(C.ANALYSIS, "breakdown.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", out, len(panels), "panels")
