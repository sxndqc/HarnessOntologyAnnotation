// The text of a gold file as the review tools read it: the file, with the text repairs of
// data/gold_text_repairs.json applied (places where the gold file itself does not parse, e.g. a missing
// bracket; an edit op cannot express those). A repair replaces one whole line; it is applied only if the line
// still has the expected text.
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');
let R = {};
try { R = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'gold_text_repairs.json'), 'utf8')); } catch (e) {}
exports.read = function (entry) {
  const lines = fs.readFileSync(path.join(ROOT, 'data', 'gold', entry.gold + '.umr'), 'utf8').split('\n');
  for (const r of R[entry.doc] || []) {
    if (lines[r.line - 1] === r.from) lines[r.line - 1] = r.to;
    else console.log(`${entry.doc}: text repair of line ${r.line} not applied, the line is not as expected`);
  }
  return lines.filter(l => l !== null).join('\n');
};
