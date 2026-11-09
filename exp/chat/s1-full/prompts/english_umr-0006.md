# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph and alignment, then all the document-level relations (temporal, modal, coreference) of the
document. Follow the guidelines below. The document is under **Input** at the end, one sentence per line.

## Guidelines

The full UMR guidelines (umr4nlp/umr-guidelines `guidelines.md`, about 366,000 characters) are
attached to this message as `umr_guidelines.md`. Read them before you annotate. They often write the older
short names (AUTH, DCT, FullAff, :modstr); your answer uses the release names listed under Output format.


## Output format

Write plain text only (no JSON, no commentary). For every sentence, in order:

    # ::snt 1
    # sentence level graph:
    (s1t / taste-01
        :ARG0 (s1p / person
            :name (s1n / name :op1 "Edmund" :op2 "Pope"))
        :ARG1 (s1f / free-04
            :ARG1 s1p
            :aspect state)
        :temporal (s1t2 / today)
        :aspect performance)
    # alignment:
    s1t: 3-3
    s1p: 1-2
    s1n: 0-0
    s1f: 4-4
    s1t2: 5-5

then, once, after the last sentence, every document-level relation of the whole document in one graph:

    # document level relations:
    (d / document
        :temporal ((document-creation-time :depends-on s1t2)
                   (s1t2 :contained s1t)
                   (s1t :before s2c))
        :modal ((root :modal author)
                (author :full-affirmative s1t)
                (author :full-affirmative s2c))
        :coref ((s1p :same-entity s2p)))

- `# ::snt N` uses the sentence number of the input line. Every sentence gets a graph, even a short one.
- Variables of sentence N start with `s` + N and a letter (`s3p`, `s3x2`), all different. A node that
  fills two roles in one sentence is written once and then named by its variable.
- Alignment: one line per variable, `variable: first-last` with the word positions of the input line
  (counted from 1); `0-0` for a node with no word.
- Document level: `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`;
  each end is a variable of a sentence graph or a constant (`author`, `root`, `document-creation-time`,
  `past-reference`, `present-reference`, `future-reference`, `null-conceiver`).
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, `partial-affirmative`, `neutral-affirmative`, `neutral-negative`,
  `partial-negative`, `full-negative`, `unspecified` (not FullAff, ...), `:modal-strength` (not
  :modstr), `:refer-person` / `:refer-number` with lower-case values (`3rd`, `singular`), and lower-case
  aspect values (`performance`, `state`, ...).
- Write the whole document: do not stop early, do not summarise, do not skip sentences.

## Input

Language: en
Document: english_umr-0006 (28 sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

1	200 dead , 1,500 feared missing in Philippines landslide .
2	TACLOBAN , Philippines , Feb 17 , 2006 .
3	About 200 people were believed killed and 1,500 others were missing in the central Philippines on Friday when a landslide buried an entire village , the Red Cross said .
4	Eyewitnesses said only a few houses were left standing after the landslide hit the village of Guinsaugon in the south of the Philippine island of Leyte .
5	" There are about 1,500 missing , 200 dead , " Richard Gordon , the head of the Philippine Red Cross , said in a radio interview .
6	The first footage from the devastated village showed a sea of mud covering what had been lush green valley farmland .
7	Only a few sheets of tin roofing and the occasional coconut tree could be seen .
8	Tiny groups of mud - spattered survivors were also shown , walking through the muck , apparently stunned by the scope of the destruction .
9	In a televised address to the nation , President Gloria Arroyo said rescue teams were rushing to the area from " air , land and sea " to cope with the catastrophe .
10	" I have ordered the Coast Guard and our entire naval force in the ( central Philippines ) region to the area , " she said .
11	" Naval ships will be used as floating hospitals and command centres for relief and rescue . "
12	Leyte Governor Rosette Lerias said the latest census indicated there were 375 houses with 3,000 people living in Guinsaugon before the landslide .
13	She described the village as totally flattened .
14	" It was like mud running down the mountain and it covered the village in seconds , " she said , quoting survivors .
15	Experts blamed deforestation for the tragedy , which came after days of rainfall that was five times higher than usual .
16	Lerias said that many Guinsaugon residents had been evacuated after landslides earlier in the week had killed more than 20 people on Leyte , but that many had returned Friday because the rains had stopped and the sun had come out.
17	A mild 2.6 - magnitude earthquake which struck before the landslide may also have helped set off the wall of mud that crashed down on the village , said Rene Solidum , head of the government vulcanology office.
18	" The area could have really been ready for a landslide because of the amount of rainfall and if there was a minor earthquake , it might have hastened it , " Solidum said .
19	Army Colonel Nestor Sadirin , head of a rescue task force , said 16 dead bodies had been recovered so far and 100 people rescued .
20	Leyte Congressman Roger Mercado said in a radio interview that the village had a population of 3,000 to 4,000 and expressed fears that as many as 2,000 people had been buried .
21	Lerias called for more rescuers to come to the site to help look for bodies as heavy earth moving equipment could not work in the mud , which officials said was more than six metres (yards) deep in many areas.
22	Volunteer rescue teams from the country's mining companies , skilled in digging through the earth to rescue people , were also going to the area , said President Arroyo said.
23	Gordon said the Red Cross said was trying to dispatch sniffer dogs to hunt for survivors .
24	Military helicopters were able to reach the area despite heavy clouds but the flights ceased after nightfall because the aircraft did not have night - flying capabilities.
25	Lerias said a smaller landslide later in the afternoon caused no damage but left many of the rescuers worried about a possible new disaster .
26	Relief groups called for drinking water , food , blankets and body bags to be brought to the scene .
27	Provincial board member Eva Dumol said in a radio interview that heavy equipment that was already in the area to clear up earlier landslides was being sent to the Guinasaugon area .
28	More than 5,000 people were killed in a combined flood and mudslide on Leyte in November 1991.
