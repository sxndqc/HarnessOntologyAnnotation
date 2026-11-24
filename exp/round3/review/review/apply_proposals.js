#!/usr/bin/env node
// usage: node review/apply_proposals.js <doc-id> [<doc-id> ...] | --all   [--decisions <umr-gold-review-decisions.json>]
//   Writes data/gold_revised/<doc-id>.umr: the gold with the proposals of review/proposals/<doc-id>.json applied.
//   Without --decisions: every proposal that is not conf "low" (of proposals sharing an "excl" group, the first).
//   With --decisions (the file the review page exports): only the proposals the reviewer accepted.
//   A sentence with nothing applied is copied as it is. A proposal that fails to apply is reported and skipped.
const fs = require('fs'), path = require('path'), E = require('./engine.js');
const ROOT = path.join(__dirname, '..');
const DOCS = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'docs.json'), 'utf8')).docs;
const args = process.argv.slice(2);
let accepted = null;
const di = args.indexOf('--decisions');
if (di >= 0) {
  const dec = JSON.parse(fs.readFileSync(args[di + 1], 'utf8'));
  accepted = new Set(Object.entries(dec.decisions || dec.dec || {}).filter(([, v]) => v === 'accept').map(([k]) => k));
  args.splice(di, 2);
}
const ids = args.includes('--all') ? DOCS.map(d => d.doc).filter(d => fs.existsSync(path.join(__dirname, 'proposals', d + '.json'))) : args;
if (!ids.length) { console.log('usage: node review/apply_proposals.js <doc-id> ... | --all [--decisions file.json]'); process.exit(2); }
fs.mkdirSync(path.join(ROOT, 'data', 'gold_revised'), { recursive: true });
let failed = 0;
for (const id of ids) {
  const entry = DOCS.find(d => d.doc === id);
  if (!entry) { console.log(id, 'is not in data/docs.json'); failed++; continue; }
  const gold = E.splitDoc(require('./goldtext.js').read(entry));
  const P = JSON.parse(fs.readFileSync(path.join(__dirname, 'proposals', id + '.json'), 'utf8'));
  let out = gold.prefix, applied = 0, skipped = 0;
  for (const b of gold.blocks) {
    let st, n = 0; const excl = new Set();
    try { st = E.loadState(b); } catch (e) { out += b.raw; continue; }
    for (const p of P[String(b.n)] || []) {
      if (accepted ? !accepted.has(p.id) : p.conf === 'low') continue;
      if (p.excl) { if (excl.has(p.excl)) continue; excl.add(p.excl); }
      const r = E.applyOps(st, p.ops || []);
      if (r.failed) { console.log(`${id} snt${b.n} ${p.id}: does not apply, skipped:`, r.log.filter(l => l.status === 'fail').map(l => l.text).join('; ')); skipped++; failed++; continue; }
      st = r.state; n++;
    }
    out += n ? E.serBlock(b, st) : b.raw; applied += n;
  }
  fs.writeFileSync(path.join(ROOT, 'data', 'gold_revised', id + '.umr'), out);
  console.log(`${id}: ${applied} proposals applied${skipped ? ', ' + skipped + ' skipped' : ''} -> data/gold_revised/${id}.umr`);
}
process.exit(failed ? 1 : 0);
