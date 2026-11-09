# PropBank entries for the words of english_umr-0008

From ai-native-annotator.github.io data/skillparse/resources/propbank/en.json: every roleset of every word of the document that PropBank has.

## tasted (found as taste)

### taste-01 (use one's tastebuds, active perception of flavor)

- ARG0: taster
- ARG1: food

Example 1 (nasty trace chains): ``Parties are rather a state of mind, '' [she]-3 said, [*-3]-4 pausing only [*-4] to taste [*RNR*-1] and pass judgment on [the Georgian shashlik]-1 (``a little well done, but very good'').
- ARGM-DIS: only
- ARG0: [*-4]
- ARG1: [*RNR*-1]
- rel: taste

Example 2 (just arg1): Ms. Morgan is really insulting all the troops who 've been there to assume that by going for ten days and taking a few casual leisurely trips outside the Green Zone that she got a full taste of combat
- ARGM-EXT: full
- ARG1: of combat
- rel: taste

Example 3 (both args): Diminutive Vanderkitten Road Sprinter Starla Teddergreen pinned on the numbers for her first taste of mud racing
- ARG0: her
- ARGM-TMP: first
- ARG1: of mud racing
- rel: taste

Example 4 (LVC): Oh man , that is creepy . Farmers mkt sounds good ! They 're doing a tomato tasting ! What time are you thinking ?
- ARG0: they
- ARGM-LVB: doing
- ARG1: tomato
- rel: tasting

### taste-02 (possess a flavor)

- ARG1: thing with flavor
- ARG2: description of flavor

Example 1 (beautiful metaphor): They still buy apples mainly for big, red good looks -- that's why so many taste like woodchucks' punching bags.
- ARG1: so many
- ARG2: like woodchucks ' punching bags
- rel: taste

## time

### time-01 (measure the time it takes to do an action, measuring time it takes)

- ARG0: measurer
- ARG1: action
- ARG2: time required

Example 1 (time-v: passive-- just like John): [John]-2 ran the Boston Marathon last week, and [*trace*-2]-1 was timed *trace*-1 at one week, three days, four hours, sixteen minutes and 27 seconds, his best performance yet.
- ARG1: *trace*-1
- ARG2: at one week, three days, four hours, sixteen minutes and 27 seconds
- rel: timed

### time-02 (synchronize)

- ARG0: agent
- ARG1: first thing synchronized
- ARG2: second thing, if separate

Example 1 (time-v: merged things): Totally absorbed, [the ringers]-2 stare straight ahead, using peripheral vision (they call it ``rope-sight'') to watch the other ropes and thus *trace*-2 time their pulls.
- ARG0: *trace*-2
- ARG1: their pulls
- rel: time

Example 2 (time-v: second thing, sorta): Renaissance declined to confirm the move, but [its stock purchases]-1 were thought to have begun Tuesday, timed *trace*-1 to coincide with the maturity this week of Treasury bills owned by the firm.
- ARG1: *trace*
- ARG2: to coincide with the maturity this week of Treasury bills owned by the firm
- rel: timed

Example 3 (time-v: clearer arg2): John timed his snoring with Mary's breathing.
- ARG0: John
- ARG1: his snoring
- ARG2: with Mary's breathing
- rel: timed

## American (found as american)

### american-02 (or origin in america)

- ARG1: American entity

Example 1: Violence is as American as cherry pie
- ARG1: Violence
- ARGM-CXN: as ...as cherry pie
- rel: American

## convicted (found as convict)

### convict-01 (to find or prove guilty of an offense or crime, finding guilty of a crime)

- ARG0: judge, jury, agent
- ARG1: person convicted
- ARG2: convicted of

Example 1 (all arguments): Despite the strong evidence against Mrs. Yeargin , popular sentiment [*ICH*-1] was so strong [*ICH*-3]in her favor , Mrs. Ward says [0] [*T*-2] , that `` I 'm afraid [0] a jury would n't have convicted her .
- ARG0: a jury
- ARGM-MOD: would
- ARGM-NEG: n't
- ARG1: her
- rel: convicted

Example 2 (passive): He-1 was convicted [*-1] of [*-2]charging interest rates much higher than what the law permitted [*T*-3] , and attempting [*-4] to evade income taxes by [*-5] using a double accounting system .
- ARG1: [*-1]
- ARG2: of [*-2] charging interest rates much higher than what the law permitted [*T*-3], and attempting [*-4] to evade income taxes by [*-5] using a double accounting system
- rel: convicted

Example 3 (All args): Supreme Court upheld their conviction of him for graft.
- ARG0: their
- ARG1: of him
- ARG2: for graft
- rel: conviction

## last

### last-01 (extend for some period of time; duration)

- ARG1: thing that lasts
- ARG2: period of time

Example 1 (prepositional period): The turmoil in junk bonds may last for years, investors and traders say.
- ARG1: The turmoil in junk bonds
- ARGM-MOD: may
- ARG2: for years
- rel: last

Example 2 (not prepositional): Some traders said the popularity of issues that gained yesterday won't last long, as investors will rotate their buying choices over the short term.
- ARG1: the popularity of issues that gained yesterday
- ARGM-MOD: wo
- ARGM-NEG: n't
- ARG2: long
- ARGM-CAU: as investors will rotate their buying choices over the short term
- rel: last

### last-02 (later than/behind all other entities)

- ARG1: last one (may require concatenation)

Example 1: Malaysia Airlines MH370: Co-pilot was last to communicate from cockpit.

### last-03 (of supplies or resources: be sufficient for a period of time)

- ARG1: supplies, resources
- ARG2: how long the supplies/resources will last
- ARG3: consumers of supplies/resources
- ARG4: consumption rate

Example 1 (food): This food will last us for at least three months.
- ARG1: This food
- ARG3: us
- ARG2: for at least three months
- rel: will last

Example 2 (oil reserves): BP eestimates that global oil reserves will last 53.3 years at the current production rates.
- ARG1: Global oil reserves
- ARG2: 53.3 years
- ARG4: at the current production rates
- rel: will last

### last-04 (of products or people: function, survive for a period of time)

- ARG1: product, person
- ARG2: how long the product/person will function/survive
- ARG3: attribute of product/person that has a duration
- ARG4: beneficiary

Example 1 (car, with arg4): This well-built car will last you for a very long time.
- ARG1: This well-built car
- ARG4: you
- ARG2: for a very long time
- rel: will last

Example 2 (coach): The new coach won't last a full season.
- ARG1: The new coach
- ARGM-NEG: n't
- ARG2: a full season
- rel: will last

Example 3 (diet, with arg3): I only lasted 2 days on my diet.
- ARG1: I
- ARG2: 2 days
- ARG3: on my diet
- rel: lasted

## on

### on-01 (functioning, active)

- ARG1: functioning thing

Example 1 (on-j): Is this thing on?
- ARG1: this thing
- rel: on

## spying (found as spy)

### spy-01 (to investigate intensively  or discover by close observation, clandestine observation)

- ARG0: secret agent
- ARG1: entity spied/seen

Example 1 (transitive): Mr. Boren even spies a silver lining .
- ARG0: Mr. Boren
- ARGM-ADV: even
- ARG1: a silver lining
- rel: spies

Example 2 (argM-LOC and arg1): Domestic spying on Americans is an e-hoarding epidemic
- ARGM-LOC: domestic
- ARG1: on Americans
- rel: spying

Example 3 (Just argM-LOC): A party that already was waning in respect due to corruption and its willingness to take some fundamental social justice concepts too far is now supported by a majority of the public , and the beloved party of small government and individual liberties is now a hulking rusty heap of corruption , scandal , incompetence , special interests , big government , and domestic spying .
- ARGM-LOC: domestic
- rel: spying

Example 4 (both args): "This report contradicts the president's claim that his spying on Americans was legal," said Sen. Frank Lautenberg (D-N.J.)
- ARG0: his
- ARG1: on Americans
- rel: spying

## charges (found as charge)

### charge-01 (asking price)

- ARG0: seller
- ARG1: asking price
- ARG2: buyer
- ARG3: commodity

Example 1 (charge-v: price and buyer): [Traditional stock managers]-1 like *trace*-1 to charge higher fees for smaller investors.
- ARG0: *trace*-1
- ARG1: higher fees
- ARG2: for smaller investors
- rel: charge

Example 2 (charge-v: all args): The Penn Bookstore charged John $100 for a mechanical pencil.
- ARG0: The Penn Bookstore
- ARG2: John
- ARG1: $100
- ARG3: for a mechanical pencil
- rel: charged

Example 3 (charge-n: NP only, Args 0, 2 & 3): The charge on loans to depository institutions by the New YorkFederal Reserve Bank
- ARG3: on loans
- ARG2: to depository institutions
- ARG0: by the New York Federal Reserve Bank
- rel: charge

Example 4 (charge-n: Args 0 & 2): They submitted their charges to customers at the end of each month.
- ARG0: their
- ARG2: to customers
- rel: charges

Example 5 (charge-n: Arg 3 only): Admission charges at movie theaters have been going up recently.
- ARG3: Admission
- rel: charges

Example 6 (charge-n: Args 0, 1, 3): Their charge of ?14 (?13,95) for breakfast is extortionate.
- ARG0: Their
- ARG1: of ?14 (?13,95)
- ARG3: for breakfast
- rel: charge

### charge-02 (walk quickly)

- ARG0: entity in motion
- ARG1: path
- ARG2: deep agent (if different from arg0)

Example 1 (charge-v: intransitive): John recklessly charged down the crowded street.
- ARG0: John
- ARGM-MNR: recklessly
- ARG1: down the crowded street
- rel: charged

Example 2 (charge-v: with arg0): Rupert charged his horse across and into Ireton.
- ARG2: Rupert
- ARG0: his horse
- ARG1: across and into Ireton
- rel: charged

Example 3 (charge-v: transitive, with argM-GOL): The soldiers charged the enemy (line).
- ARG0: The soldiers
- ARGM-GOL: the enemy (line)
- rel: charged

Example 4 (charge-n: Arg 0 only): The wrestler's charge carried him past his adversary.
- ARG0: The wrestler's
- rel: charge

Example 5 (charge-n: All arguments): The offensive charge of the field gained their football team 22 yards in the last play.
- ARG0: offensive
- ARG1: of the field
- rel: charge

### charge-03 (supply, as with electricity)

- ARG0: supplier
- ARG1: battery, usually
- ARG2: instrument (defaults to electricity)

Example 1 (charge-v: literal batteries): John charged his Walkman batteries.
- ARG0: John
- ARG1: his Walkman batteries
- rel: charged

Example 2 (charge-v: metaphorical batteries): John charged his batteries with a quadruple shot of espresso.
- ARG0: John
- ARG1: his batteries
- ARG2: with a quadruple shot of espresso
- rel: charged

### charge-04 (buy on credit)

- ARG0: buyer
- ARG1: thing charged (amount, item)
- ARG2: credit

Example 1 (charge-v: all args): During the third quarter, the company charged about $46 million against earnings in reducing goodwill.
- ARGM-TMP: During the third quarter
- ARG0: the company
- ARG1: about $ 46 million
- ARG2: against earnings
- ARGM-ADV: in reducing goodwill
- rel: charged

Example 2 (charge-n: All arguments): Mary's charge of the dress on her old credit card would not go through.
- ARG0: Mary's
- ARG1: of the dress
- ARG2: on her old credit card
- rel: charge

Example 3 (charge-n: Args 1 & 2): The charge of $900 dollars of merchandise to his father's credit card got John into big trouble.
- ARG1: of $900 dollars of merchandise
- ARG2: to his father's credit card
- rel: charge

### charge-05 (assign a role (including criminal charges), assign an allegation or criminal charge against someone)

- ARG0: assigner
- ARG1: assigned
- ARG2: role or crime

Example 1 (charge-v: usually as crime): Royal Business Group Inc. said [it]-1 filed suit in federal court here *trace*-1 charging Realist Inc. and its directors with violating federal securities laws ``by engaging in a scheme to prevent'' Royal from acquiring Realist.
- ARG0: *trace*-1
- ARG1: Realist Inc. and its directors
- ARG2: with violating federal securities laws ``by engaging in a scheme to prevent'' Royal from acquiring Realist
- rel: charging

Example 2 (charge-v: passivized crime): [Mr. Antar]-2 was charged *trace*-2 last month in a civil suit filed in federal court in Newark by the Securities and Exchange Commission.
- ARG1: *trace*-2
- ARGM-TMP: last month
- ARGM-LOC: in a civil suit filed in federal court in Newark by the Securities and Exchange Commission
- rel: charged

Example 3 (charge-v: not a crime): Instead, [an appropriate institution]*-4 should be charged [*-4]with the job of preventing chaos in the market: the Federal Reserve.
- ARGM-MOD: should
- ARG1: [*-4]
- ARG2: with the job of preventing chaos in the market
- rel: charged

Example 4 (charge-n: Fragment, Args 0 & 2): its largely successful defense of antitrust charges by the UnitedStates Football League
- ARG2: antitrust
- ARG0: by the United States Football League
- rel: charges

Example 5 (charge-n: Charged with a crime): Prosecuters around Taiwan dealt with more than 2,000 cases concerning black - gold offenses, and brought charges against 30 elected officials and representatives.
- ARG1: against 30 elected officials and representatives
- rel: charges

Example 6 (charge-n: Arg 2 only): The newspaper published charges that the attorney had tried to bribe members of the jury.
- ARG2: that the attorney had tried to bribe members of the jury.
- rel: charges

Example 7 (charge-n: Args 0 and 2): House Speaker Nancy Pelosi said Friday she won't talk any more about her charge that the CIA lied in 2002 about using waterboarding.
- ARG0: her
- ARG2: that the CIA lied in 2002 about using waterboarding.
- rel: charge

### charge-06 (allege (an utterance or complement clause))

- ARG0: speaker
- ARG1: utterance

Example 1 (charge-v: transitive): Pharmacia, based in Upsala, Sweden, had charged in a lawsuit against MedChem that MedChem's AMVISC product line infringes on the Pharmacia patent.
- ARG0: Pharmacia, based in Upsala, Sweden,
- ARGM-LOC: in a lawsuit against MedChem
- ARG1: that MedChem's AMVISC product line infringes on the Pharmacia patent
- rel: charged

### charge-08 (to be in charge of something, have a responsibility or role)

- ARG0: Person assigning responsibility (rare)
- ARG1: Person that the responsibility is assigned to
- ARG2: responsibility itself, role

Example 1 (charge-n: Args 0 & 1): The judge's charge to the jury was to ignore the preceding statement of the witness.
- ARG0: The judge's
- ARG1: to the jury
- rel: charge

Example 2 (charge-n: Args 1 & 2): The spy fulfilled his charge of smuggling fissile materials into the country.
- ARG1: his
- ARG2: of smuggling fissile materials into the country
- rel: charge

Example 3 (charge-n: Arg 2 only (very common)): Malcolm S. Todt was named vice president and senior officer in charge of equipment leasing to municipalities , a new effort of this bond insurer .
- ARG2: of equipment leasing to municipalities, a new effort of this bond insurer.
- rel: charge

## sentenced (found as sentence)

### sentence-01 (assign criminal punishment)

- ARG0: judge/jury
- ARG1: criminal
- ARG2: punishment
- ARG3: crime
- ARG4: duration of punishment

Example 1 (all args): [Dallas District Judge Jack Hampton]-1 had sparked calls for a judicial inquiry with his remarks to the press last December, two weeks after *trace*-1 sentencing an 18-year-old defendant to 30 years in state prison for killing two homosexual men in a city park.
- ARG0: *trace*
- ARG1: an 18-year-old defendant
- ARG2: to 30 years in state prison
- ARG3: for killing two homosexual men in a city park
- rel: sentencing

Example 2 (passive, without crime): He-1 was sentenced *trace*-1 to 500 hours of community service and restitution to the museum of $45,000.
- ARG1: *trace*
- ARG2: to 500 hours of community service and restitution to the museum of $45,000
- rel: sentenced

Example 3 (Example with all but arg 0): his prison sentence for income-tax evasion
- ARG1: his
- ARG2: prison
- ARG3: for income-tax evasion
- rel: sentence

Example 4 (Arg 0 as a court body): many people would receive federal death sentences
- ARG0: federal
- ARG2: death
- rel: sentences

Example 5 (Example with arg 1 and 4): His 18-year sentence
- ARG1: His
- ARG4: 18-year
- rel: sentence

Example 6 (Example with args 2 and 4): A prison sentence of less than three years
- ARG2: prison
- ARG4: of less than three years
- rel: sentence

Example 7 (Example with args 3 and 4): A 30-year sentence for the self-confessed 1992 killing of his wife in Clinton Maryland
- ARG4: 30-year
- ARG3: for the self-confessed 1992 killing of his wife in Clinton Maryland
- rel: sentence

Example 8 (Traditional punishment): A sentence of 100 lashes
- ARG2: of 100 lashes
- rel: sentence

Example 9 (args 0, 1, 2): Their sentencing him to solitary confinement, what a joke.
- ARG0: Their
- ARG1: him
- ARG2: to solitary confinement
- rel: sentencing

### sentence-02 (what your english teacher made you write correctly and completely)

- ARG0: writer
- ARG1: theme (topic/thing written)

Example 1 (Example with both args): His next sentence about a radio interview,
- ARG0: His
- ARGM-TMP: next
- ARG1: about a radio interview,
- rel: sentence

Example 2 (Example of the type of sentence to use this sense for): the first to use silences and sentence fragments and menacingstares, almost to the exclusion of what we previously understoodto be theatrical dialogue
- rel: sentence

## denied (found as deny)

### deny-01 (turn down, reject)

- ARG0: denier
- ARG1: thing denied
- ARG2: anti-benefactive: entity being denied arg1

Example 1 (transitive, no benefactive): Earlier this year, the Fed denied an application by Continental Bank Corp. to purchase Grand Canyon State Bank in Scottsdale, Ariz., on grounds that Continental hadn't fully complied with the Community Reinvestment Act.
- ARGM-TMP: Earlier this year
- ARG0: the Fed
- ARG1: an application by Continental Bank Corp. to purchase Grand Canyon State Bank in Scottsdale, Ariz.
- ARGM-CAU: on grounds that Continental hadn't fully complied with the Community Reinvestment Act
- rel: denied

Example 2 (deny an S): In affidavits filed yesterday in the Los Angeles court, Mr. Ross, Warner Bros. Chairman Robert Daly and President Semel deny that such an oral agreement was ever made.
- ARGM-LOC: in affidavits filed yesterday in the Los Angeles court
- ARG0: Mr. Ross , Warner Bros. Chairman Robert Daly and President Semel
- ARG1: that such an oral agreement was ever made
- rel: deny

Example 3 (with benefactive): Mary denied John a kiss.
- ARG0: Mary
- ARG2: John
- ARG1: a kiss
- rel: denied

## pardoned (found as pardon)

### pardon-01 (legally relieve of guilt)

- ARG0: pardoner
- ARG1: guilty party
- ARG2: for what

Example 1 (transitive): Under the guise of ``healing the wounds of the nation,'' President Carter pardoned thousands of draft evaders, thus giving dignity to their allegations of the war's ``immorality.''
- ARGM-LOC: Under the guise of ``healing the wounds of the nation
- ARG0: President Carter
- ARG1: thousands of draft evaders
- ARGM-ADV: thus giving dignity to their allegations of the war's ``immorality
- rel: pardoned

### pardon-02 (give forgiveness, usually for a minor social misstep)

- ARG0: person forgiving the faux pas
- ARG1: guilty party, misstepper
- ARG2: crime, sin or faux pas

Example 1 (lacking social mores): "Pardon me," John said after emitting a thunderclap-like belch at the dinner table.
- ARG1: me
- rel: pardon

Example 2 (pardon my french sense): " All of which, pardon me for saying this, could be put down to employee screwups."
- ARG1: me
- ARG2: for saying this
- rel: pardon

Example 3 (beg your pardon): "Beg your pardon, Sir, but Cornwall is dead! "
- ARG0: your
- rel: pardon

## reasons (found as reason)

### reason-01 (think logically)

- ARG0: thinker
- ARG1: thought
- ARG2: with whom?

Example 1 (reason-v: fronted): [That is another small encouragement for the Federal Reserve tolower interest rates in coming weeks]-1, they reasoned *trace*-1.
- ARG0: they
- ARG1: *trace*-1
- rel: reasoned

Example 2 (reason-v): John reasoned with Mary about the reality of Santa Clause.
- ARG0: John
- ARG2: with Mary
- ARG1: about the reality of Santa Clause
- rel: reasoned

Example 3 (reasoning-n: most args): My reasoning to go out and buy a new car was based mainly on fuel economy.
- ARG0: My
- ARG1: to go out and buy a new car
- rel: reasoning

Example 4 (reasoning-n: Arg-m only, probably most common): Discussed reasoning behind the EUS procedure
- ARGM-ADJ: behind the EUS procedure
- rel: reasoning

## base

### base-01 (be located in)

- ARG0: agent basing something somewhere
- ARG1: institution
- ARGM: M-LOC location, where arg1 is based

Example 1 (base-v (according to the tree): showing physical location): [Hearst]-2, based *trace*-2 in New York, ....
- ARG1: *trace*-2
- ARGM-LOC: in New York
- rel: based

Example 2 (base-v: With agent): When referring to the achievements made in recent years by greatly investing in national infrastructure , Xiang Wang , concurrently a member of the national CPPCC , a member of the Standing Committee of the Jiangxi Province CPPCC , president of the Group , etc. said frankly to the reporters that " *PRO* basing ourselves in the inland and ' building bridges and paving roads ' for the development of the local economy was a wise choice on my part . "
- ARG0: *PRO*
- ARG1: ourselves
- ARGM: in the inland
- rel: basing

Example 3 (base-v: All arguments): They based the company in Southern California but maintained a Boulder operation.
- ARG0: They
- ARG1: the company
- ARGM-LOC: in Southern California
- rel: based

Example 4 (based-j): Using the city where-1 I am based [*-1] as an example , nearly all the medium and small - sized state - owned enterprises have closed down
- ARG1: I
- ARGM-LOC: [*-1]
- rel: based

### base-02 (justified by, made up of)

- ARG0: justifier, agent (rarely seen)
- ARG1: decision, whole
- ARG2: justification, parts/ arg1 is made up of what?

Example 1 (base-v: justify): ...a [market structure]-1 based *trace*-1 on such variables
- ARG1: *trace*-1
- ARG2: on such variables
- rel: based

Example 2 (base-v: transitive, agentive): John based his decision on gut instinct
- ARG0: John
- ARG1: his decision
- ARG2: on gut instinct
- rel: based

Example 3 (adverbial, with trace): Milton Roy will pay an initial $ 4 million *trace*-*U* for the operations and [additional payments during the next four years]-1 based *trace*-1 on the earnings performance of the businesses.
- ARG1: *trace*-1
- ARG2: on the earnings performance of the businesses
- rel: based

Example 4 (adverbial): [The exact amount of the refund -16] will be determined *trace-16* next year based on actual collections made *trace*-* until Dec. 31 of this year.
- ARG1: *trace-16*
- ARG2: on actual collections made *trace*-* until Dec. 31 of this year
- rel: based

## will

### will-01 (give in a will, bequeath)

- ARG0: bequeather, giver
- ARG1: inheritance, gift
- ARG2: beneficiary

Example 1 (all args): Until recently, [a farmer with no heir]-1 had [*-1]to will the state his land [*-1] to collect his pension.
- ARG0: [*-1]
- ARG2: the state
- ARG1: his land
- rel: will

### will-02 (desire some state/action, desiring, agreeing to)

- ARG0: desirer
- ARG1: state/action desired

Example 1 (both args): ...the Lord willed it to be of pneumonia ...
- ARG0: the Lord
- ARG1: it to be of pneumonia
- rel: willed

Example 2 (adjectival rel: willing): and and it 's very specific about what the United States is willing *PRO*-1 to do *T*-2 uh *PRO*-1 to take a step forward towards them should they dismantle all their nuclear programs and their weapons of mass destruction.
- ARG0: the United States
- ARG1: *PRO*-1 to do *T*-2
- ARGM-DIS: uh
- ARGM-PRP: *PRO*-1 to take a step forward towards them
- ARGM-ADV: should they dismantle all their nuclear programs and their weapons of mass destruction
- rel: willing

## spend

### spend-01 (use money, paying money/time)

- ARG0: spender, buyer
- ARG1: thing bought, commodity
- ARG2: seller
- ARG3: price paid, money
- ARG4: benefactive

Example 1 (demonstrating commodity and price): The NIH currently spends about $8 million annually on fetal-tissue research.
- ARG0: The NIH
- ARGM-TMP: currently
- ARG3: about $8 million
- ARGM-TMP: annually
- ARG1: on fetal-tissue research.
- rel: spends

Example 2 (with TMP): They spent $325,000 in 1989.
- ARG0: They
- ARG3: $325,000
- ARGM-TMP: in 1989
- rel: spent

Example 3 (arg0): Government spending is actually increasing .
- ARG0: Government
- rel: spending

Example 4 (arg 0, 1 and 3): The question is whether his spending $7.7 million on food, drink, hotels and parties is excessive.
- ARG0: his
- ARG3: $7.7 million
- ARG1: on food, drink, hotels and parties
- rel: spending

### spend-02 (bide time)

- ARG0: bider, waiter
- ARG1: unit of time
- ARG2: activity

Example 1 (spend time): He spends his days *trace-1* sketching passers-by or *trace-2* trying to.
- ARG0: He
- ARG1: his days
- ARG2: *trace-1* sketching passers-by or *trace-2* trying to.
- rel: spends

Example 2 (simpler example): Mr. Bernstein has spent much of his time in recent years on human rights issues.
- ARG0: Mr. Bernstein
- ARG1: much of his time
- ARGM-TMP: in recent years
- ARG2: on human rights issues.
- rel: spent

### spend-04 (be used up)

- ARG1: thing used up
- ARG2: cause

Example 1 (arg 1 only - most common): the spent fuel rod
- ARG1: fuel rod
- rel: spent

Example 2 (with arg 2): Man! I am completely spent from that basketball game!
- ARGM-DIS: Man!
- ARG1: I
- ARGM-EXT: completely
- ARG2: from that basketball game
- rel: spent

Example 3 (adjectival): The shampoo and conditioner are completely spent.
- ARG1: The shampoo and conditioner
- ARGM-EXT: completely
- rel: spent.

## center

### center-01 (focus (on))

- ARG0: agent, focuser
- ARG1: thing focused
- ARG2: focused-on

Example 1 (center-v: normal usage): Speculation on his successor centers on a number of division heads at the house.
- ARG1: Speculation on his successor
- ARG2: on a number of division heads at the house
- rel: centers

Example 2 (center-v: around variant): Japan's objections to the U.S. plan center around its desire to stay self-sufficient in rice, a staple food, even though foreign producers are far more efficient.
- ARG1: Japan's objections to the U.S. plan
- ARG2: around its desire to stay self-sufficient in rice, a staple food, even though foreign producers are far more efficient
- rel: center

Example 3 (center-v: in variant): The size of the cuts isn't known, but [they]-1'll be centered *trace*-1 in the exploration and production division, which is responsible for locating oil reserves, drilling wells and pumping crude oil and natural gas.
- ARG1: *trace*-1
- ARGM-MOD: 'll
- ARG2: in the exploration and production division, which is responsible for locating oil reserves, drilling wells and pumping crude oil and natural gas
- rel: centered

Example 4 (center-v: agentive): In *trace*-2 centering on the disruption of a few proud local customs such as the historic homes tour and the damage to the antiquities, [your reporter]-2 served to only perpetuate an outdated and stereotypically provincial view of this otherwise thriving port city.
- ARG0: *trace*-2
- ARG2: on the disruption of a few proud local customs such as the historic homes tour and the damage to the antiquities
- rel: centering

Example 5 (center-v: arg2 as location): The larger parallel after [the earthquake]-1 centered *trace*-1 south of San Francisco is surely with the state of the U.S. economy.
- ARG1: *trace*-1
- ARG2-LOC: south of San Francisco
- rel: centered

Example 6 (center-v: all args): John centered his gaze on Mary's knees.
- ARG0: John
- ARG1: his gaze
- ARG2: on Mary's knees
- rel: centered

Example 7 (centered-j): Of course , undeniably , some enforcement departments , which-1 [*-1] are public security bureau - centered , face the fact that they have insufficient personnel and they have to recruit some " temporary workers . "
- ARG1: [*-1]
- ARG2: public security bureau
- rel: centered

### center-02 (politically/socially moderate)

- ARG1: politically/socially centrist entity
- ARG2: domain or topic of centrism

Example 1 (Both args): he's accused of being too centerist
- ARG1: he
- ARGM-EXT: too
- rel: centerist

## returns (found as return)

### return-01 (come back)

- ARG1: entity in motion
- ARG2: (extent -- rare)
- ARG3: start point
- ARG4: end point
- ARGM: medium

Example 1 (typical): I-1 need *trace*-1 to return on Tuesday.
- ARG1: *trace*
- ARGM-TMP: on Tuesday
- rel: return

Example 2 (metaphorical): Parents are returning to the cloth diaper.
- ARG1: Parents
- ARG4: to the cloth diaper
- rel: returning

Example 3 (Example of end point as 'return to ..."): they expect a return to full operations by Saturday
- ARG4: to full operations
- ARGM-TMP: by Saturday
- rel: return

Example 4 (Example with arg 1 and 4): their return to black townships across the country
- ARG1: their
- ARG4: to black townships across the country
- rel: return

Example 5 (Example with args 0 and 4): their return to Earth
- ARG1: their
- ARG4: to Earth
- rel: return

Example 6 (Example with arg 1): The possible return of the verification team
- ARG1: of the verification team
- rel: return

Example 7 (revert to): a return to Soviet-era symbolism in Russia
- ARG4: to Soviet-era symbolism in Russia
- rel: return

### return-02 (give back)

- ARG0: giver
- ARG1: thing given
- ARG2: entity given to

Example 1 (Japanese baseball): Fans politely return foul balls to stadium ushers.
- ARG0: Fans
- ARGM-MNR: politely
- ARG1: foul balls
- ARG2: to stadium ushers
- rel: return

Example 2 (seeking comment): Charles LaBella didn't return phone calls seeking comment.
- ARG0: Charles LaBella
- ARGM-NEG: n't
- ARG1: phone calls seeking comment
- rel: return

Example 3 (Example with all args): his return toast to Mr. Nixon
- ARG0: his
- ARG1: toast
- ARG2: to Mr. Nixon
- rel: return

Example 4 (Example with args 1 and 2): the return of cheaper shares to the lender
- ARG1: of cheaper shares
- ARG2: to the lender
- rel: return

Example 5 (Example with all args): Their return of our refugees to their homes
- ARG0: Their
- ARG1: of our refugees
- ARG2: to their homes
- rel: return

Example 6 (Possibly confusing use): Jack's safe return
- ARG1: Jack's
- ARGM-MNR: safe
- rel: return

Example 7 (Args 1 and 2): The return of East Jerusalem to the Palestinians
- ARG1: of East Jerusalem
- ARG2: to the Palestinians
- rel: return

### return-03 (bring back)

- ARG0: entity bring something back
- ARG1: thing brought back
- ARG2: attribute of arg1, state arg1 is brought back to

Example 1 (transitive active): The company had returned the plant to routine inspection in August.
- ARG0: The company
- ARG1: the plant
- ARG2: to routine inspection
- ARGM-TMP: in August
- rel: returned

Example 2 (Example with arg 1): the best punt return , quarterback sack , etc
- ARG1: punt
- rel: return

Example 3 (Example with arg 0 and arg 1): The mechine's ball return was broken.
- ARG0: The mechine's
- ARG1: ball
- rel: return

### return-04 (send back)

- ARG0: sender
- ARG1: thing sent
- ARG2: sent-to

Example 1 (all args): Mr. Koskotas is fighting extradition proceedings that [*T*-2] would return him to Greece, where he is charged with embezzling more than $250 million from the Bank of Crete.
- ARG0: [*T*-2]
- ARGM-RCL: that -> extradition proceedings
- ARGM-MOD: would
- ARG1: him
- ARG2: to Greece, where he is charged with embezzling more than $250 million from the Bank of Crete
- rel: return

### return-05 (exchange, trade)

- ARG0: agent, entity trading
- ARG1: theme
- ARG2: other exchanger
- ARG3: secondary theme

Example 1 (Args 1,3): North Korea agreed to dismantle its nuclear program in return for economic aid.
- ARG1: for economic aid
- ARG3: North Korea agreed to dismantle its nuclear program
- rel: return

Example 2 (Example with args 1): in return for removing all our tariff barriers
- ARG1: for removing all our tariff barriers
- rel: return

Example 3 (Often in the form of 'in return for'): In return for services rendered
- ARG1: for services rendered
- rel: return

Example 4 (It is rare to find this with more than arg 1): In return for your patience
- ARG1: for your patience
- rel: return

### return-06 (give a dividend)

- ARG0: thing providing a dividend
- ARG1: dividend, earnings
- ARG2: recipient

Example 1 (Monitary example (usual use)): a 0.89 % return on assets for Security Pacific
- ARG1: 0.89 %
- ARG0: on assets
- ARG2: for Security Pacific
- rel: return

Example 2 (the return percentage can be 'earnings'): KKR racked up annual returns of 60 % in the three years it owned Storer .
- ARGM-TMP: annual
- ARG1: of 60 %
- rel: returns

Example 3 (Non-monitary example): Returns from just under a third of the polling stations
- ARG0: from just under a third of the polling stations
- rel: Returns

Example 4 (Arg 0 is often inanimate): A return of investments of 32%
- ARG0: on investments
- ARG1: of 32%
- rel: return

Example 5 (Animate arg 2): whose returns after tax have trailed tuition increases
- ARG2: whose
- ARGM-TMP: after tax
- rel: returns

## remission

### remission-02 (abate in intensity)

- ARG0: cause of remission
- ARG1: thing abating

Example 1 (remission-n: cancer): remission of breast cancer
- ARG1: of breast cancer
- rel: remission

Example 2 (remission-n: non-cancer and with the elusive arg 0!): effects of catecholamine depletion on antidepressant-induced remission of depression
- ARG0: antidepressant-induced
- ARG1: of depression
- rel: remission

## rare

### rare-02 (uncommon, infrequent)

- ARG1: uncommon thing

Example 1 (Single arg): Most cars with that mileage will be rare and possibly worth something.
- ARG1: Most cars with that mileage
- ARGM-MOD: will
- rel: rare

### rare-03 (cooked a short time, still red)

- ARG1: meat

Example 1 (With CXN, who's hungry?): The burger was so rare that the bits that fell out when I picked the burger up, they could be pressed and molded.
- ARG1: The burger
- ARGM-CXN: [so] [that the bits that fell out when I picked the burger up, they could be pressed and molded]
- rel: rare

## form

### form-01 (create, make)

- ARG0: creator
- ARG1: thing created
- ARG2: source
- ARG3: benefactive
- ARG4: attribute of arg1

Example 1 (just transitive): Peter Drake, biotechnology analyst for Vector Securities International, Chicago, thinks market uncertainty may encourage small companies to form more strategic alliances with big corporations.
- ARG0: small companies
- ARG1: more strategic alliances with big corporations
- rel: form

Example 2 (passive, with source): [NCNB Texas National]-1, formed *trace*-1 from the remnants of of the failed First RepublicBank Corp. of Dallas, contributed $76.9 million to NCNB's bottom line in the third quarter.
- ARG1: *trace*-1 (= NCNB Texas National)
- ARG2: from the remnants of of the failed First RepublicBank Corp. of Dallas
- rel: formed

Example 3 (nominal rel: forming): ---------------------- The forming of a market involves a process . This process may be very tortuous . At present , this market is in the process of forming .
- ARG1: of a market
- rel: forming

Example 4 (autogen1): Friday , 42 franchisees announced the formation of an association-- called A.P. Association Inc. -- to `` preserve the integrityof the Arby 's system . ''
- ARG1: of an association -- called A.P. Association Inc. -- to `` preserve the integrity of the Arby 's system
- rel: formation

Example 5 (autogen2): the formation of a holding company enabling the savings bank topursue nontraditional banking activities under a new federal law
- ARG1: of a holding company enabling the savings bank to pursue nontraditional banking activities under a new federal law
- rel: formation

Example 6 (With COM (probably not source in this case)): the formation of a national emergency unity government with Ariel Sharon 's opposition Likud Party
- ARG1: of a national emergency unity government
- ARGM-COM: with Ariel Sharon's opposition Likud Party
- rel: formation

Example 7 (args0 and 1): the formation of a new political party by James Soong
- ARG1: of a new political party
- ARG0: by James Soong
- rel: formation

Example 8 (with materials/source): Vortex formation out of two-dimensional orifices
- ARG1: Vortex
- ARG2: out of two-dimensional orifices
- rel: formation

Example 9 (swapped product/materials): Personal formation into the likeness of Christ
- ARG2: personal
- ARG1: into the likeness of Christ
- rel: formation

### form-02 (comprise)

- ARG0: components
- ARG1: whole

Example 1 (cf. 'make up'): Commission income from domestic stock and bond sales accounts form a large portion of Japanese securities companies' earnings.
- ARG0: Commission income from domestic stock and bond sales accounts
- ARG1: a large portion of Japanese securities companies' earnings
- rel: form

Example 2 (comprise again): The labels were breathy: ``Within its sheltering walls is a microcosm of a thousand years in garden design ... [a rose garden, herb garden, serpentine garden, flower fields, an apple orchard]-1 ... organized in a patchwork of 50-by-50-foot squares [*]-1 to form `rooms'...
- ARG0: [*]
- ARG1: rooms
- rel: form

## bone

### bone-01 (remove bones)

- ARG0: remover
- ARG1: thing which used to have bones

Example 1 (Eeeeewwww): John boned the fish.
- ARG0: John
- ARG1: the fish
- rel: boned

## arrested (found as arrest)

### arrest-01 (like a criminal)

- ARG0: police
- ARG1: criminal
- ARG2: crime

Example 1 (difficult syntax for crime): Since Mexican President Carlos Salinas de Gortari took office last December, special agents have arrested more than 6,000 federal employees on charges ranging from extortion to tax evasion.
- ARGM-TMP: Since Mexican President Carlos Salinas de Gortari took office last December
- ARG0: special agents
- ARG1: more than 6,000 federal employees
- ARG2: on charges ranging from extortion to tax evasion
- rel: arrested

Example 2 (NP only, all arguments): the arrest of opposition activists on the grounds of terrorism
- ARG1: of opposition activists
- ARG2: on the grounds of terrorism
- rel: arrest

Example 3 (NP only, Args 0 & 1): the arrest by West German authorities of five young West Germans, accused of stealing information from computers in the U.S. andEurope and selling it to the Soviet KGB
- ARG0: by West German authorities
- ARG1: of five young West Germans , accused of stealing information from computers in the U.S. and Europe and selling it to the Soviet KGB
- rel: arrest

Example 4 (All arguments): Information passed to Crimestoppers resulted in a milestone figure of the 100,000th arrest, following the arrest of a man by Durham Police for burglary.
- ARG1: of a man
- ARG0: by Durham Police
- ARG2: for burglary
- rel: arrest

### arrest-02 (stop)

- ARG0: causer of stopping
- ARG1: thing stopping

Example 1 (arrested development): China might stave off a crisis if it acts as forcefully as [it]*-1 did [*-1]to arrest the 1985 decline, when Beijing slammed the brakes on foreign-exchange spending and devalued the currency.
- ARG0: [*-1]
- ARG1: the 1985 decline
- ARGM-TMP: when Beijink slammed the brakes on foreign-exchange spending and devalued the currency
- rel: arrest

Example 2 (Arg 1 as "of" PP): The medication is very effective in the arrest of the disease's progress.
- ARG1: of the disease's progress
- rel: arrest

Example 3 (Arg 1 pre-relation): The patient was experiencing cardiac arrest.
- ARG1: cardiac
- rel: arrest

Example 4 (All arguments): Thus, the arrest of egg maturation by allatectomy might be due to the failure of the corpora allata to stimulate the mnc.
- ARG1: of egg maturation
- ARG0: by allectomy
- rel: arrest

## Doctors (found as doctor)

### doctor-01 (to falsify or alter)

- ARG0: causer of change, agent
- ARG1: entity doctored

Example 1 (transitive): Members find it [*EXP*-1] easy [*]to doctor legislation by [*] slipping in special provisions that [*T*-2] could never survive in the cold light of day .
- ARG0: [*]
- ARG1: legislation
- ARGM-MNR: by [*] slipping in special provisions that [*T*-2]could never survive in the cold light of day
- rel: doctor

## examine

### examine-01 (look at closely)

- ARG0: examiner
- ARG1: thing examined
- ARG2: in search of what

Example 1 (passivized): [Valley Federal]-1 is currently being examined *trace*-1 by regulators.
- ARGM-TMP: currently
- ARG1: *trace*
- ARG0: by regulators
- rel: examined

Example 2 (active): Mr. Paul says that he has feelers out over much of the globe and that potential buyers from as far away as Japan and Italy have examined the collection.
- ARG0: potential buyers from as far away as Japan and Italy
- ARG1: the collection
- rel: examined

Example 3 (Both args): his examination of Mr. Lorin
- ARG0: his
- ARG1: of Mr. Lorin
- rel: examination

Example 4 (arg 1 only): After hours of meticulous examination of each address book,
- ARGM-MNR: meticulous
- ARG1: of each address book,
- rel: examination

Example 5 (both args): international examination of one of the most troubling mysteries in US - Soviet relations
- ARG0: international
- ARG1: of one of the most troubling mysteries in US - Soviet relations
- rel: examination

Example 6 (with args 1 and 2): The applications for such technology include examination of the body for asymmetries
- ARG1: of the body
- ARG2: for asymmetries
- rel: examinations

## signs (found as sign)

### sign-01 (affix a signature)

- ARG0: signer
- ARG1: document
- ARG2: signature

Example 1 (sign-v: historical): John's great-uncle Fred signed the Declaration of Independence--unfortunately, in 1924.
- ARG0: John's great-uncle Fred
- ARG1: the Declaration of Independence
- ARGM-ADV: unfortunately, in 1924
- rel: signed

Example 2 (sign-v: with explicit signature): One writer signed his letter as "Red blooded, balanced male".
- ARG0: One writer
- ARG1: his letter
- ARG2: as "Red blooded, balanced male"
- rel: signed

### sign-02 (enter into an agreement)

- ARG0: signer, agreer
- ARG1: agreement
- ARG2: co-signer

Example 1 (sign-v: agreement): First Constitution has signed a merger agreement with WFRR LP and GHKM Corp.
- ARG0: First Constitution
- ARG1: a merger agreement
- ARG2: with WFRR LP and GHKM Corp.
- rel: signed

Example 2 (sign-v: no co-signer): An ultimatum: *trace* either sign new long-term commitments to buy future episodes, or don't.
- ARG0: *trace*
- ARG1: new long-term commitments to buy future episodes
- rel: sign

Example 3 (sign-v: sign to): John was signed to the Mudville Giants.
- ARG2: John
- ARG1: to the Mudville Giants
- rel: signed

Example 4 (signing-n): When Ma Ying - jeou resumed its " reign " four years ago , he worked actively to make up for the time squandered by the DPP , and the signing of the Economic Cooperation Framework Agreement -LRB- ECFA -RRB- was the biggest highlight .
- ARG1: of the Economic Cooperation Framework Agreement -LRB- ECFA -RRB-
- rel: signing

## have

### have-01 (auxiliary)

- (no roles)

Example 1 (auxiliary): John has annoyed Mary for the last time.

### have-02 (modal)

- (no roles)

Example 1 (modal): John has to apologize to Mary.
- rel: has

### have-03 (own, possess)

- ARG0: owner
- ARG1: possession

Example 1 (bummer): Four of the five surviving workers have asbestos-related diseases, including three with recently diagnosed cancer.
- ARG0: Four of the five surviving workers
- ARG1: asbestos-related diseases
- ARGM-ADV: including three with recently diagnosed cancer
- rel: have

### have-04 (caused action)

- ARG0: causer
- ARG1: action

Example 1 (clearer, but still gruesome): Mary had John killed.
- ARG0: Mary
- ARG1: John killed
- rel: had

### have-05 (birthing sense)

- ARG0: entity giving birth to something
- ARG1: entity birthed

Example 1 (Miracle of Life Sense): Some of them had children while they were out at sea.
- ARG0: Some of them
- ARG1: children
- ARGM-TMP: while they were out at sea
- rel: had

### have-06 (light verb)

- ARG0: true subject
- ARG1: true predicate

Example 1 (have a threesome): Have you ever had a threesome?
- ARG0: you
- ARG1: a threesome
- rel: had

### have-11 (have yet to)

- ARG0: subject, entity having not yet done arg2
- ARG1: fixed: 'yet'
- ARG2: have yet to what (infinitival S-node complement)

Example 1 (all args): [US News]-1 has yet *-1 to announce its 1990 ad rates.
- ARG0: [US News]-1
- ARG1: yet
- ARG2: *-1 to announce its 1990 ad rates
- rel: has

Example 2 (all args): We did experience some difficulties with the initial LBO terms and , as your article made clear , successfully restructured our debt earlier this year , something those other retailers have yet to accomplish .
- ARG0: those other retailers
- ARG1: yet
- ARG2: to accomplish
- rel: have

Example 3 (passive infinitival complement. same args.): [Some of the biggest service - industry exporters -- American financial - service companies , for example --]-1 have yet [*-1]-2 to be fully included *-2 in our export statistics .
- ARG0: Some of the biggest service - industry exporters -- American financial - service companies , for example --
- ARG1: yet
- ARG2: [*-1]-2 to be fully included *-2 in our export statistics .
- rel: have

### have-07 (semi-modal: had better/best)

- ARG0: entity that should
- ARG1: fixed: better/best
- ARG2: what arg0 had better/best do (main verb clause)

Example 1 (Had best. Also, good advice.): One-1 had best *-1 not dance on top of a coffin until the lid is sealed tightly shut . ''
- ARG0: One
- ARG1: best
- ARG2: *-1 not dance on top of a coffin until the lid is sealed tightly shut .
- rel: had

Example 2 (had better): He-1 had better *-1 do what he is told.
- ARG0: he
- ARG1: better
- ARG2: *-1 do what he is told.
- rel: had

### have-08 (have at you! (tackle))

- ARG0: agent, tackler
- ARG1: thing tackled ('at' what)

Example 1 (Standard usage): But , if you just got your arms and legs blown off by and IED , then by all means , have at it . -LRB- Err ... have someone do it for you . -RRB-
- ARGM-DIS: But
- ARGM-ADV: if you just got your arms and legs blown off by and IED
- ARGM-ADV: then
- ARGM-ADV: by all means
- ARG0: *PRO*
- ARG1: at it
- rel: have

### have-09 (have_one's_way_with: have sex with, possibly rape-ily)

- ARG0: agent, agressor
- ARG1: fixed: (arg0's) way
- ARG2: victim/patient

Example 1 (all args): It 's rather amusing to watch them shove Obama down people 's throats every night on the news , while completely *PRO* having their way with Hillary .
- ARGM-EXT: completely
- ARG0: *PRO*
- ARG1: their way
- ARG2: with Hillary
- rel: having

### have-10 (have a go at; attempt, try out)

- ARG0: agent
- ARG1: action attempted. "a go at __"

Example 1 (Both args): When I first looked last month I had a go at photographing the planet and managed to get four of the moons :
- ARGM-TMP: When I first looked last month
- ARG0: I
- ARG1: a go at photographing the planet
- rel: had

## come

### come-01 (motion)

- ARG1: entity in motion / 'comer'
- ARG2: extent -- rare
- ARG3: start point
- ARG4: end point

Example 1 (destination): Mrs. Yeargin came to work on weekends.
- ARG1: Mrs Yeargin
- ARG4: to work
- ARGM-TMP: on weekends
- rel: came

Example 2 (with purpose): Students, teachers, and parents came to testify on her behalf.
- ARG1: Students, teachers, and parents
- ARGM-PRP: to testify on her behalf
- rel: came

Example 3 (destination as by-phrase): You may come by the agency to read but not copy the books.
- ARG1: You
- ARGM-MOD: may
- ARG4: by the agency
- ARGM-PRP: to read but not copy the books
- rel: come

Example 4 (come back (not phrasal)): They aren't going to come back to the US.
- ARG1: They
- ARGM-DIR: back
- ARG4: to the US
- rel: to come

Example 5 (nice syntactic reversal): ``So crunch, crunch, crunch, bang, bang, bang -- here-4 come [*T*-4] the ringers from above, making a very obvious exit while the congregation is at prayer,'' he says.
- ARG4: [*T*-4]
- ARG1: the ringers
- ARG3: from above
- ARGM-ADV: making a very obvious exit while the congregation is at prayer
- rel: come

Example 6 (temporal coming): It is also the sovereign power that, come 1997, will take over this British colony.
- ARG1: 1997
- rel: come

Example 7 (coming on): Although Bausch remains the leader among the six majors, Johnson& Johnson, with its new disposables, is coming on fast.
- ARGM-ADV: Although Bausch remains the leader among the six majors
- ARG1: Johnson& Johnson, with its new disposables,
- ARGM-DIR: on
- ARGM-MNR: fast
- rel: coming

Example 8 (another with start point): But at the time when he stood to speak , I was in the restroom and sort of coming back from the restroom
- ARGM-TMP: at the time when he stood to speak
- ARG1: I
- ARGM-ADV: sort of
- ARG3: back from the restroom
- rel: coming

Example 9 (arg1): Haha , that s what I said in conversation with someone last night , she 's the second coming of Dan Quayle !
- ARGM-TMP: second
- ARG1: of Dan Quayle
- rel: coming

### come-12 (come to: speaking of)

- ARG1: topic

Example 1 (Zen-like blase): But as the French embody a Zen-like state of blase when-1 it comesto athletics [*T*-1] (try finding a Nautilus machine in Paris), myfellow conventioners were having none of it.
- ARG1: to athletics
- ARGM-TMP: [*T-1*]
- rel: comes

### come-02 (pursue (often with after), pursuing)

- ARG0: pursuer
- ARG1: goal

Example 1 (come after): Portfolio managers come after the highest rates.
- ARG0: Portfolio managers
- ARG1: after the highest rates
- rel: come

Example 2 (Both args): He runs the risk of their coming after him immediately
- ARG0: their
- ARG1: after him
- ARGM-TMP: immediately
- rel: coming

### come-03 (arise (from))

- ARG1: thing (often state) arising
- ARG2: source, basis on which arg1 comes to be  (not start point of motion!)

Example 1 (arise in): Part of the charm comes in recognizing one's self in the novel.
- ARG1: Part of the charm
- ARG2: in recognizing one's self in the novel
- rel: comes

Example 2 (arise of): Ringers are filled with the solemn intoxication that-1 *trace*-1 comes of intricate ritual faultlessly performed.
- ARGM-SLC: that -> the solemn intoxication
- ARG1: *trace*-1 (= that)
- ARG2: of intricate ritual faultlessly performed
- rel: comes

Example 3 (origin of being): Yes , I do recall Bill Buckingham making comments about , you know , the apes and monkeys - *PRO*-3 coming from apes and monkeys .
- ARG1: *PRO*-3
- ARG2: from apes and monkeys
- rel: coming

### come-04 (become, various near-idioms)

- ARG1: object
- ARG2: attribute on arg1

Example 1 (come true): Its forecasts didn't come true.
- ARG1: Its forecasts
- ARGM-NEG: didn't
- ARG2: true
- rel: come

Example 2 (come as): That may not come as a surprise to Americans who have watched the Japanese snap up properties in the U.S. from golf courses to a stake in Rockefeller Center.
- ARG1: That
- ARGM-MOD: may
- ARGM-NEG: not
- ARG2: as a surprise to Americans who have watched the Japanese snap up properties in the U.S. from golf courses to a stake in Rockefeller Center
- rel: come

Example 3 (result in): They do at least come around to [*] saying that the courts might want to end ``rigid affirmative action programs.''
- ARG1: They
- ARGM-ADV: at least
- ARGM-DIR: around
- ARG2: to [*] saying that the courts might want to end ``rigid affirmative action programs
- rel: come

Example 4 (come of age): The attack commercial has come of age in an off-election year.
- ARG1: The attack commercial
- ARG2: of age
- ARGM-TMP: in an off-election year
- rel: come

Example 5 (come under scrutiny): But the growing controversy comes as many practices historically accepted as normal here -- such as politicians accepting substantial gifts from businessmen or having extramarital affairs -- are coming under close ethical scrutiny.
- ARG1: many practices historically accepted as normal here -- such as politicians accepting substantial gifts from businessmen or having extramarital affairs --
- ARG2: under close ethical scrutiny
- rel: coming

Example 6 (come to a head): The ``one-yen'' controversy first came to a head last week when the city of Hiroshima announced that Fujitsu won a contract to design a computer system to map its waterworks.
- ARG1: The ``one-yen'' controversy
- ARGM-TMP: first
- ARG2: to a head
- ARGM-TMP: last week
- ARGM-TMP: when the city of Hiroshima announced that Fujitsu won a contract to design a computer system to map its waterworks
- rel: came

Example 7 (come to a halt): Despite the economic slowdown, there are few clear signs that growth is coming to a halt.
- ARG1: growth
- ARG2: to a halt
- rel: coming

Example 8 (come to an end): ``Actually, [the long deterioration in daily newspapers]-1 shows signs of [*]-1 coming to an end, and the industry looks pretty healthy.''
- ARG1: [*]
- ARG2: to an end
- rel: coming

### come-05 (pertaining to a purchase)

- ARG1: commodity
- ARG2: buyer
- ARG3: price

Example 1 (non-specific price): Chateau Yquem now comes dear.
- ARG1: Chateau Yquem
- ARGM-TMP: now
- ARG3: dear
- rel: comes

### come-to-terms-14 (acclimate to fate)

- ARG0: entity coming to terms
- ARG2: with who/what

Example 1 (come to terms): In the coming decade, analysts say, U.S.-Japanese relations will be tested as Tokyo comes to terms with its new status as the region's economic behemoth.
- ARG0: Tokyo
- ARG2: with its new status as the region's economic behemoth
- rel: comes to terms

### come-16 (amount to)

- ARG1: thing(s) being counted
- ARG2: sum, total, amount

Example 1 (so, it comes to this): Last year, the Cowboys' share of that pie came to $17.6 million.
- ARGM-TMP: Last year
- ARG1: the Cowboys' share of that pie
- ARG2: to $17.6 million
- rel: came

### come-28 (serial verb construction)

- ARG0: subject
- ARG1: subsequent action

Example 1 (both args): I 'm studying abroad for a year and [my boyfriend]-1 is going [*-1]-2 to come *PRO*-2 visit me a few times times .
- ARG0: [*-1]-2
- ARG1: *PRO*-2 visit me a few times times
- rel: come

Example 2: if you-1 want *-1 to come skiing/snowboarding this Saturday you can join the event here
- ARG0: *-1
- ARG1: skiing/snowboarding this Saturday
- rel: come

## back

### back-01 (support)

- ARG0: supporter
- ARG1: thing being supported

Example 1 (support): ...asking [him]-1 *trace*-1 to back a Palestinian bid to joing the committee.
- ARG0: *trace*-1
- ARG1: a Palestinian bid to joing the committee
- rel: back

Example 2 (cease support): The big brokerage firms back out of program trading for their own accounts or for clients.
- ARG0: The big brokerage firms
- ARG1: out of program trading
- ARGM-PNC: for their own accounts or for clients.
- rel: back

Example 3 (cease support, with NP): Eastern Airline's creditors committee backed off a move to come up with its own alternative proposals to the carrier's bankruptcy reorganization plans.
- ARG0: Eastern Airline's creditors committee
- ARG1: off a move to come up with its own alternative proposals to the carrier's bankruptcy reorganization plans.
- rel: backed

Example 4 (Both args): Russia's backing of Kostunica
- ARG0: Russia's
- ARG1: of Kostunica
- rel: backing

Example 5 (Arg 0 only): Congressional backing
- ARG0: Congressional
- rel: backing

### back-02 (move backwards)

- ARG0: causer of backwards motion
- ARG1: entity in motion

Example 1 (retreat): The Soviets might back away from the current conciliatory attitude
- ARG1: The Soviets
- ARGM-MOD: might
- ARGM-DIR: away from the current conciliatory attitude
- rel: back

### back-03 (face backwards)

- ARG0: looker, facer
- ARG1: looked at, faced

Example 1 (with PP): John's house backs onto the city dump.
- ARG0: John's house
- ARG1: onto the city dump
- rel: backs

## awaiting (found as await)

### await-01 (wait for)

- ARG1: wait-er (not waiter, that's a different sense)
- ARG2: thing waited for
- ARGM: period of time waited through

Example 1 (typical usage): Trading is expected to remain subdued as the market awaits tomorrow's release of the jobs data with the hope that it will point toward a decline in interest rates.
- ARG1: the market
- ARG2: tomorrow's release of the jobs data
- ARGM-MNR: with the hope that it will point toward a decline in interest rates
- rel: awaits

## trial

### trial-06 (medical trial, consumer trial, or similar)

- ARG0: doctor
- ARG1: patient, consumer
- ARG2: medication/ treatment, thing tested

Example 1: We will trial her on continuous face mask oxygen.
- ARG0: We
- ARGM-MOD: will
- ARG1: her
- ARG2: on continuous face mask oxygen.
- rel: trial

Example 2 (Another example with both args): a trial of its computers to consumers who qualify for its credit cards or leases .
- ARG2: of its computers
- ARG1: to consumers who qualify for its credit cards or leases
- rel: trial

Example 3 (arg0 and arg2): the company 's clinical trials of both its animal and human-based insulins
- ARG0: the company's
- ARGM-MNR: clinical
- ARG2: of both its animal and human-based insulins
- rel: trials

## suffering (found as suffer)

### suffer-01 (suffer, endure/undergo something painful)

- ARG0: entity suffering
- ARG1: malady

Example 1 (intransitive): The company's return on equity could suffer if it made a higher bid.
- ARG0: The company's return on equity
- ARGM-MOD: could
- ARGM-ADV: if it made a higher bid
- rel: suffer

Example 2 (with PP-malady): John suffers from delusions of grandeur.
- ARG0: John
- ARG1: from delusions of grandeur
- rel: suffers

Example 3 (with S-malady): Thou shalt not suffer a fool to live.
- ARG0: Thou
- ARGM-MOD: shalt
- ARGM-NEG: not
- ARG1: a fool to live
- rel: suffer

## high

### high-02 (in the upper ranges (altitude, pitch, etc))

- ARG1: entity in the upper ranges
- ARG2: the upper ranges of what (domain)

Example 1 (arg1): This manifests into the devastation we often see in neighborhoods , where-1 the poverty rate is high [*-1].
- ARG1: the poverty rate
- ARGM-LOC: [*-1]
- rel: high

Example 2 (wide range of arg2s): Orchid Beach penthouse is high in altitude, price and glamour
- ARG1: Orchid Beach penthouse
- ARG2: in altitude, price and glamour
- rel: high

Example 3 (argMs, lexicalized comparative alias): The reason specific ethnic groups are targeted for trying to reduce crime is because , for whatever reason , crime overall is often higher statistically in these groups .
- ARGM-CAU: for whatever reason
- ARG1: crime overall
- ARGM-TMP: often
- ARGM-ADV: statistically
- ARGM-LOC: in these groups
- rel: higher

### high-03 (elated, in good spirits)

- ARG0: cause of elation
- ARG1: elated entity

Example 1 (That's a little harsh, but both args.): Still *PRO* Feeling high from that Toy Story 3 trailer? Well, get ready to be disapointed.
- ARGM-TMP: Still
- ARG1: *PRO*
- ARG0: from that Toy Story 3 trailer
- rel: high

### high-04 (stoned, intoxicated)

- ARG0: intoxicant
- ARG1: stoner

Example 1 (both args): Man runs into Ross Campground Church, announces he's high on "bath salts"
- ARG1: he's
- ARG0: on "bath salts"
- rel: high

## blood

### blood-01 (bleed)

- ARG0: agent
- ARG1: theme, one bled

Example 1 (passive, arg1 only): The night after [*] reading her letter about her surgeon uncle -- it musthave been late in September -- I had a vision of myself returned in raggeduniform from The Front , nearly dying , my head bandaged and blooded , andJessica bending over me , the power of her love bringing me back to life .
- ARG1: my head
- rel: blooded

### blood-02 (possess/contain blood)

- ARG1: entity possessing blood
- ARG2: characteristic of the blood

Example 1: basically with all this fuss about Scottish Independence in the news I 'm wondering how this bears for people who are n't 100 % ' pure blooded Scot ' for 7 generations or something .
- ARGM-EXT: 100 %
- ARG2: pure
- ARG1: Scot
- rel: blooded

## pressure

### pressure-01 (apply pressure, pressure someone to do something)

- ARG0: presser
- ARG1: pressed (on)
- ARG2: goal, pressed-for

Example 1 (with goal): Big Board stock specialists, began to have them pressure the exchange to ban program trading.
- ARG0: them
- ARG1: the exchange
- ARG2: to ban program trading
- rel: pressure

Example 2 (without goal): Generally in the quarter, overproduction of gasoline and higher crude oil prices pressured profitability.
- ARGM-DIS: Generally
- ARGM-TMP: in the quarter
- ARG0: overproduction of gasoline and higher crude oil prices
- ARG1: profitability
- rel: pressured

### pressure-02 (move, cause motion by pressure)

- ARG0: mover
- ARG1: moved
- ARGM: ahead, usually

Example 1 (somewhat odd usage): [The Nikkei index]-1 was pressured *trace*-1 down by profit-taking triggered by sharp advances made through this week and fell 151.20 points to 35527.29.
- ARG1: *trace*
- ARGM-DIR: down
- ARG0: by profit-taking triggered by sharp advances made through this week
- rel: pressured
