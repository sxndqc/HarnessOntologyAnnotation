# PropBank entries for the words of english_umr-0007

From ai-native-annotator.github.io data/skillparse/resources/propbank/en.json: every roleset of every word of the document that PropBank has.

## United (found as unite)

### unite-01 (make into one)

- ARG0: uniter, agent
- ARG1: (first) thing(s) being unified
- ARG2: other things, if separate from arg1
- ARG3: unified whole

Example 1 (all args): This unification was to be brought about through policies and institutions that *trace* would unite workers and employers with government in a fully integrated and ``harmonic'' society.
- ARGM-SLC: that -> policies and institutions
- ARG0: *trace* (= that)
- ARGM-MOD: would
- ARG1: workers and employers
- ARG2: with government
- ARG3: in a fully integrated and ``harmonic'' society
- rel: unite

Example 2 (passive): [The oil and auto industries]-1, united *trace*-1 in their dislike of President Bush's proposal for cars that run on alternative fuels, announced a joint research program that could turn up a cleaner-burning gasoline.
- ARG1: *trace*
- ARGM-LOC: in their dislike of President Bush's proposal for cars that run on alternative fuels
- rel: united

Example 3 (ergative!): Most political analysts say that if Mr. Gandhi's opposition unites to field single candidates in most precincts, the Congress (I) will lose big.
- ARG1: Mr. Gandhi 's opposition
- ARGM-PRP: to field single candidates in most precincts
- rel: unites

## States (found as state)

### state-01 (state, say, state or say)

- ARG0: announcer
- ARG1: utterance
- ARG2: hearer
- ARG3: attributive

Example 1 (transitive): The Japanese government, Mr. Godown said, has stated that it wants 10% to 11% of its gross national product to come from biotechnology products.
- ARG0: The Japanese government
- ARG1: that it wants 10% to 11% of its gross national product to come from biotechnology products
- rel: stated

Example 2 (Example with args 0 and 2): China 's statements to its own people
- ARG0: China 's
- ARG2: to its own people
- rel: statements

Example 3 (Example with arg 3): a registration statement filed with the Securities and Exchange Commission
- ARG3: registration
- rel: statement

Example 4 (MNR): in a written statement
- ARGM-MNR: written
- rel: statement

Example 5 (Args 0, 1, and 2): I'm puzzled by his statement to the media that my proposal seeks to place 10000 horses on the Spruce Ranch
- ARG0: his
- ARG2: to the media
- ARG1: that my proposal seeks to place 10000 horses on the Spruce Ranch
- rel: statement

Example 6 (Example with args 0 and 3): Its statement on expanding and improving its health insurance program
- ARG0: Its
- ARG3: on expanding and improving its health insurance program
- rel: statement

## hoping (found as hop)

### hop-01 (manner of motion, jumping)

- ARG0: hopper
- ARG3: Source
- ARG4: Destination

Example 1: *PRO* Hop onto a trolley with over a century of history.
- ARG0: *PRO*
- ARG4: onto a trolley with over a century of history
- rel: Hop

Example 2 (Jump): The women said they had seen him waive an exhausted fairwell; but he may have been shooing away the fleas that-1 *T*-1 hopped from his yellow dog on to him.
- ARGM-SLC: that-1 -> the fleas
- ARG0: *-1 (=that)
- ARG3: from his yellow dog
- ARG4: on to him
- rel: hopped

Example 3 (arg3 source and destination): I got an email from Christina that stressed me out& she 's been ignoring my q about how many credits I have . I 'm looking forward to museum hopping on Sat !
- ARG3: museum
- rel: hopping

### hop-02 (catch a ride)

- ARG0: entity catching a ride
- ARG1: the ride

Example 1 (hopping a ride): Ludie hopped rides on freight cars , and was chased by Mr. Yankton , the railroad guard .
- ARG0: Ludie
- ARG1: rides on freight cars
- rel: hopped

Example 2 (ride = vehicle): He thought he'd hopped a train to Philadelphia, and now he was in a bit of a pickle.
- ARG0: he
- ARGM-MOD: 'd
- ARG1: a train to Philadelphia
- rel: hopped

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

## follow

### follow-01 (be subsequent, temporally or spatially)

- ARG0: causal agent
- ARG1: thing following, coming after
- ARG2: thing followed, coming before

Example 1 (intransitive): Champagne and dessert followed.
- ARG1: Champagne and desert
- rel: followed

Example 2 (transitive): The strong growth followed year-to-year increases of 21% in August.
- ARG1: The strong growth
- ARG2: year-to-year increases of 21% in August
- rel: followed

Example 3 (passivized): [California]-1 led the nation, followed *trace*-1 by Texas, Iowa, and Florida
- ARG2: *trace*-1
- ARG1: by Texas, Iowa, and Florida
- rel: followed

Example 4 (as temporal): *trace* Following the acquisition of RP Scherer, the maker of gelcaps decided to ...
- ARG1: *trace*
- ARG2: the acquisition of RP Scherer
- rel: Following

Example 5 (with causal agent): Mr. Simmons has followed friendly offers with a hostile tender offer.
- ARG0: Mr. Simmons
- ARG2: friendly offers
- ARG1: with a hostile tender offer
- rel: has followed

Example 6 (obnoxious intervening idiom chunk): Now Republican leaders are concentrating on attaching a capital-gains amendment to some other bill, perhaps a measure raising the federal borrowing limit or a second tax bill that-1 [*T*-1] would follow on the heels of the deficit-reduction legislation.
- ARG1: [*T*-1] (= that)
- ARGM-SLC: that -> a second tax bill
- ARGM-MOD: would
- ARGM-MNR: on the heels
- ARG2: of the deficit-reduction legislation
- rel: follow

### follow-02 (adhere to, accept, understand, pursue)

- ARG0: acceptor, pursuer
- ARG1: thing followed
- ARG2: benefactive

Example 1 (another transitive): Many investors follow a strategy of buying and holding a mix of stocks.
- ARG0: Many investors
- ARG1: a strategy of buying and holding a mix of stocks
- rel: follow

Example 2 (with manner): John avidly follows Major League baseball for his father, who can only receive Italian soccer on his TV.
- ARG0: John
- ARGM-MNR: avidly
- ARG1: Major League baseball
- ARG2: for his father, who can only receive Italian soccer on his TV.
- rel: follows

Example 3 (arg 1 first): its loyal following among buyers of equipment
- ARG1: its
- ARGM-MNR: loyal
- ARG0: among buyers of equipment
- rel: following

Example 4 (arg 0 only): Baker had a large gay following later in her career when she was an overdressed singer rather than underdressed dancer
- ARGM-ADJ: large
- ARG0: gay
- rel: following

Example 5 (Arg 1 only): bling following of fads
- ARGM-MNR: blind
- ARG1: of fads
- rel: following

### follow-04 (list function)

- ARG1: described

Example 1 (with arg): The following individuals were fined as indicated and barred from association with NASD members, or, where noted, suspended.
- ARG1: individuals
- rel: following

Example 2 (ICH): The following [*ICH*-2] were neither barred nor suspended: [Stephanie Veselich Enright, Rolling Hills, Calif., fined $2,500 and ordered to disgorge $11,762; Stuart Lane Russel, Glendale, Calif., fined $2,500 and ordered to disgorge $14,821; Devon Nilson Dahl, Fountain Valley, Calif., fined $82,389]-2.
- ARG1: [*ICH*-2]
- rel: following

### follow-05 (logical conclusion)

- ARG1: conclusion
- ARG2: thesis

Example 1 (with manner): ...``Robert Bork's America'' -- the parade of imaginary horribles that-2 [*T*-2]would follow logically, he claimed, from the positions Mr. Bork had taken over the space of two decades.
- ARG1: [*T*-2](=that)
- ARGM-SLC: that -> the parade of imaginary horribles
- ARGM-MOD: would
- ARGM-MNR: logically
- ARG2: from the positions Mr. Bork had taken over the space of two decades
- rel: follow

## special

### special-02 (unique)

- ARG1: thing that is unique, possibly cherished
- ARG2: entity cherishing, holding arg1 as unique

Example 1 (that special kind of special): Our best friend 's sister 's wedding was uhm , special .
- ARG1: Our best friend's sister's
- ARGM-DIS: uhm
- rel: special

Example 2 (both args): Now you know why-1 July is special to me [*-1].
- ARG1: July
- ARG2: to me
- ARGM-CAU: [*-1]
- rel: special

## commission

### commission-01 (to grant a commission, authorize, hiring by commission)

- ARG0: granter, agent
- ARG1: task
- ARG2: recepient

Example 1 (transitive): [*-1] To find out why , the group recently commissioned a study of the past 20 years of bowling-related research .
- ARG0: the group
- ARGM-TMP: recently
- ARG1: a study of the past 20 years of bowling-related research
- rel: commissioned

Example 2 (all arguments): And she further stunned her listeners by [*-2] revealing her secret garden design method : [*]Commissioning a friend to spend `` five or six thousand dollars ... on books that I ultimately cut up [*T*-1] . ''
- ARG0: [*]
- ARG2: a friend
- ARG1: to spend `` five or six thousand dollars ... on books that I ultimately cut up [*T*-1]
- rel: Commissioning

Example 3 (no args): Special occasions such as keel laying , ship christening , and commissioning ceremonies deal with shipbuilding , no ceremonies for scrapping .
- rel: commissioning

Example 4 (All args): The search for a theatrical home took up most of the company's energy, through the Blackfriars financial fiasco, in the bitter battles with Giles Allen over their lease (which resulted in pulling down the Theatre), and through their commissioning of Peter Street to build a new theater in Southwark, the Globe.
- ARG0: their
- ARG2: of Peter Street
- ARG1: to build a new theater in Southwark, the Globe
- rel: commissioning

## pardon

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

## American (found as american)

### american-02 (or origin in america)

- ARG1: American entity

Example 1: Violence is as American as cherry pie
- ARG1: Violence
- ARGM-CXN: as ...as cherry pie
- rel: American

## serving (found as serve)

### serve-01 (act, work, performance of a service)

- ARG0: worker, entity performing a service/acting in some capacity
- ARG1: job, project, service performed
- ARG2: employer/recipient/beneficiary of service

Example 1 (just employer): Each new trading roadblock is likely to be beaten by institutions-1 seeking better ways *trace*-1 to serve their high-volume clients, here or overseas.
- ARG0: *trace*-1
- ARG2: their high-volume clients
- ARGM-LOC: here or overseas
- rel: serve

Example 2 (just job): Mr. Reupke was one of three executives on Reuters's eight-person executive committee who-1 *trace*-1 didn't also serve on the company's board of directors.
- ARG0: *trace*-1 (= who)
- ARGM-SLC: who -> three executives
- ARGM-NEG: n't
- ARGM-ADV: also
- ARG1: on the company's board of directors
- rel: serve

Example 3 (job and employer): He has never met Lynn Williams, the president of the United Steelworkers union, and isn't active in the industry's main trade group, the American Iron and Steel Institute, which-1 Mr. Roderick served *trace*-1 as chairman.
- ARG2: *trace*-1 (= which)
- ARGM-SLC: which -> the American Iron and Steel Institute
- ARG1: as chairman
- rel: served

Example 4 (job as pro-controlled S): In a statement, Arnold B. McKinnon, chairman and chief executive officer, noted that the new repurchase program ``should serve to enhance shareholder value.''
- ARG0: the new repurchase program
- ARGM-MOD: should
- ARG1: to enhance shareholder value
- rel: serve

Example 5 (nominal rel: serving): His serving as CTO for many years had given him great insight into the dynamics of small companies.
- ARG0: his
- ARG1: as CTO
- ARGM-TMP: for many years
- rel: serving

Example 6 (nominal rel: service): The service of security
- ARG1: of security
- rel: service

Example 7 (nominal rel: service): His exemplary service as Secretary of Commerce
- ARG0: his
- ARGM-ADV: exemplary
- ARG1: as Secretary of Commerce
- rel: service

Example 8 (nominal rel: service): a company that provides disaster recovery services forcomputer-dependent businesses
- ARG1: disaster recovery
- ARG2: for computer-dependent businesses
- rel: services

Example 9 (nominal rel: service): Mike raised $35000 for Help For Heroes, a charity that is close to his heart following his ten year service in the British Army.
- ARG0: his
- ARGM-TMP: ten year
- ARG2: in the British Army
- rel: service

Example 10 (nominal rel: service): Community service
- ARG2: community
- rel: service

### serve-02 (cater (to someone or something), delivery of something concrete)

- ARG0: server
- ARG1: thing served/delivered
- ARG2: served/delivered to

Example 1 (breakfast in bed): John served runny eggs and burnt toast to Mary.
- ARG0: John
- ARG1: runny eggs and burnt toast
- ARG2: to Mary
- rel: served

Example 2 (nominal rel: serving): Her serving popcorn all day caused her to go home smelling like butter substitute.
- ARG0: Her
- ARG1: popcorn
- ARGM-TMP: all day
- rel: serving

Example 3 (nominal rel: service): For that reason, the service of legal documents on the premises of the trade show has been prohibited.
- ARG1: of legal documents
- ARGM-LOC: on the premises of the trade show
- rel: service

Example 4 (nominal rel: service): Proof of service of divorce papers to someone in jail in florida
- ARG1: of divorce papers
- ARG2: to someone in jail in Florida
- rel: service

Example 5 (nominal rel: service): A part of the Hotel-Villa BB is Adria tavern where we offer service of breakfast to our guests
- ARG1: of breakfast
- ARG2: to our guests
- rel: service

### serve-04 (serve a sentence)

- ARG0: entity doing time
- ARG1: sentence served (maybe given as a period of time)
- ARG2: crime, reason for sentence

Example 1 (args 0, 1): ...no one...wanted her to serve prison time more than myself.
- ARG0: her
- ARG1: prison time
- rel: serve

## sentence

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

## charged (found as charge)

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

## secrets (found as secrete)

### secrete-01 (generate and releases substance, release substance)

- ARG0: secreting entity
- ARG1: secretion

Example 1 (active): It secretes the largest quantity of venom of any Taiwanese snake.
- ARG0: It
- ARG1: the largest quantity of venom of any Taiwanese snake
- rel: secretes

Example 2 (Both args): The liver's importance to the digestive system is its secretion of bile salts.
- ARG0: its
- ARG1: of bile salts
- rel: secretion

## relating (found as relate)

### relate-01 (be related to, involved, connected)

- ARG0: agent, entity drawing comparison
- ARG1: thing under consideration
- ARG2: what it's related to

Example 1 (progressive): ...information relating to fees from clients should be confidential.
- ARG1: information
- ARG2: to fees from clients
- rel: relating

Example 2 (past): ...a series of initiatives related both to global warming and the plight of the African elephant
- ARG1: a series of initiatives
- ARGM-DIS: both
- ARG2: to global warming and the plight of the African elephant
- rel: related

Example 3 (active): John related the performance of the Dow Jones to sunspot activity.
- ARG0: John
- ARG1: the performance of the Dow Jones
- ARG2: to sunspot activity
- rel: related

Example 4 (Very common 'in relation to'): low prices in relation to the company 's earnings per share
- ARG2: to the company 's earnings per share
- rel: relation

Example 5 (Family relation): Ed Turner, no relation to Ted Turner -RRB-
- ARG1: Ed Turner,
- ARGM-NEG: no
- ARG2: to Ted Turner
- rel: relation

Example 6 (What to do when the things being compared are in the same node): The relation between physical education and the economy
- ARG1: between physical education and the economy
- rel: relation

Example 7 (both constituents in arg1): He 's a bit aggressive , raves and rants a lot , and mixes up a lot of different political stances into one bundle when-1 many are in no way related [*-1], but beyond that ....
- ARG1: many
- ARGM-MNR: in no way
- ARGM-TMP: [*-1]
- rel: related

Example 8 (args 1, 2): Even if people show up who you agree with on some political issue , ask yourselves if that issue is actually related to what the protest is about .
- ARG1: that issue
- ARGM-ADV: really
- ARG2: to what the protest is about
- rel: related

Example 9 (nominal usage): ambassadorial relations
- ARG1: ambassadorial
- rel: relations

### relate-02 (say)

- ARG0: Sayer
- ARG1: Utterance
- ARG2: Hearer
- ARG3: Attributive

Example 1 (relate as verb of saying): John related a funny story about his grandmother.
- ARG0: John
- ARG1: a funny story about his grandmother
- rel: related

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

## speed

### speed-01 ((cause to) go fast)

- ARG0: causer of fast motion
- ARG1: entity in motion

Example 1 (lawbreaker): John always speeds in his Chevette.
- ARG1: John
- ARGM-TMP: always
- ARGM-LOC: in his Chevette
- rel: speeds

Example 2 (with agent): The Los Alamos laboratory is one of three U.S. Department of Energy national laboratories designed as pilot centers to foster joint industry-government programs [0]-1 [*T*-1]to speed the transfer of new superconductors to the marketplace.
- ARG0: [*T*-1] (= [0])
- ARGM-SLC: [0] -> joint industry-government programs
- ARG1: the transfer of new superconductors to the marketplace
- rel: speed

Example 3 (with redundant directional): The market's wild week may speed along the market-reform legislation that has been pending for months in the aftermath of the 1987 crash.
- ARG0: The market's wild week
- ARGM-MOD: may
- ARGM-DIR: along
- ARG1: the market-reform legislation that has been pending for months in the aftermath of the 1987 crash
- rel: speed

Example 4 (arg1): According to Kyle Evans, he says he stopped a man and inquired about the reason for his speeding.
- ARG1: his
- rel: speeding

Example 5 (both args): The doctor had a thrilling experience on his homeward trip, which necessitated his speeding his car,
- ARG0: his
- ARG1: his car
- rel: speeding

## torpedo

### torpedo-01 (to destroy decisively, wreck)

- ARG0: destroyer, firer of torpedo, agent
- ARG1: entity torpedoed

Example 1 (transitive): Such an offer could torpedo a plan [*ICH*-1] by Lion Nathan Ltd. of New Zealand [*]to acquire half the brewing interests .
- ARG0: Such an offer
- ARGM-MOD: could
- ARG1: a plan [*ICH*-1] by Lion Nathan Ltd. of New Zealand [*]to acquire half the brewing interests
- rel: torpedo

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

## backed (found as back)

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

## up

### up-01 (make higher)

- ARG0: causer
- ARG1: ante

Example 1 (up-v: up yours!): Then the two camps upped the ante: Reports that Chosen Soren had donated directly to JSP members were rapidly countered by statements that the South Korean residents' organization had long been donating directly to LDP members.
- ARGM-TMP: Then
- ARG0: the two camps
- ARG1: the ante
- rel: upped

### up-02 ((be) at an increase)

- ARG1: increased entity
- ARG2: EXT
- ARG3: start point
- ARG4: end point
- ARG5: specific aspect of/domain in which arg1 is increased

Example 1 (up-j: args 1, 5): She is still volume up , and I suspect part of her respiratory difficulties are secondary to fluid overload .
- ARG1: She
- ARGM-TMP: still
- ARG5: volume
- rel: up

Example 2 (up-j: complex arg 1): She is still volume up , and I suspect part of her respiratory difficulties are secondary to fluid overload .
- ARG1: [She] [volume]
- ARGM-TMP: still
- rel: up

### up-03 (spatially up high, or at the upper end of something)

- ARG1: entity that is up high
- ARG2: high place, upper end of what spatial body

Example 1 (up-j): One our our cats is up in a tree.
- ARG1: One our our cats
- ARG2: in a tree
- rel: up

Example 2 (up-j: up a creek- metaphorical): Dee Paterson is up a creek without a paddle or a boat after gaining her first call-up to the Great Biritain Freestyle Canoeing team.
- ARG1: Dee Paterson
- ARG2: a creek
- ARGM-MNR: without a paddle or a boat
- ARGM-TMP: after gaining her first call-up to the Great Biritain Freestyle Canoeing team
- rel: up

### up-04 (awake and perhaps out of bed/mobile)

- ARG1: awake and mobile entity
- ARG2: former state/location of repose

Example 1 (up-j: arg1): Mrs. Kent has continued to recover from surgery and is currently up sitting in bed during consultation today .
- ARG1: Mrs. Kent
- ARGM-TMP: currently
- ARGM-ADV: sitting in bed
- ARGM-TMP: during consultation today
- rel: up

Example 2 (up-j: both args): My dad is up from bed, resting on the sofa.
- ARG1: my dad
- ARG2: from bed
- rel: up

## based (found as base)

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

## news (found as new)

### new-01 (be newly created; recently come into being)

- ARG1: new object

Example 1 (Portlandia, all args (example 1)): The company has a new product
- ARG1: product
- rel: new

Example 2 (all args (example 2)): We will discuss new developments in the economic crisis
- ARG1: developments
- rel: new

Example 3 (use this sense for new positions): Having a new leader every 4 years doesn't make a country unstable
- ARG1: leader
- rel: new

Example 4 (AMR-only adverbial use): Newly married people can have trouble adjusting
- ARG1: married
- rel: newly

Example 5 (AMR-only adverbial use): I just bought a new car
- ARG1: car
- rel: new

### new-02 (new to; novel; have an existing idea, state or circumstance apply to new targets)

- ARG1: entity that seems new
- ARG2: person/place for whom arg1 is new; experiencer of newness

Example 1 (locational arg2): We've been encountering this species in new areas
- ARG2: areas
- rel: new

Example 2 (all args (example 2)): He is new to the idea of waking up at 5am.
- ARG2: He
- ARG1: to the idea of waking up at 5am
- rel: new

Example 3 (no arg2 in Propbank scope): I like meeting new people
- ARG1: people
- rel: new

## give

### give-01 (transfer)

- ARG0: giver
- ARG1: thing given
- ARG2: entity given to

Example 1 (double object): The executives gave the chefs a standing ovation.
- ARG0: The executives
- ARG2: the chefs
- ARG1: a standing ovation
- rel: gave

Example 2 (ditransitive): She had given the answers to two low-ability geography classes.
- ARG0: She
- ARG1: the answers
- ARG2: to two low ability geography classes
- rel: given

Example 3 (give way): The Beatles give way to baseball in the Nipponese version.
- ARG0: The Beatles
- ARG1: way
- ARG2: to baseball
- rel: give

Example 4 (Odd discourse-level usage): This is very odd, *trace* given uncertainties about the auction.
- ARG2: *trace*
- ARG1: uncertainties about the auction
- rel: given

Example 5 (another discourse-level usage): Given the weakness in both the junk bond market and the stock market, traders fear that these transactions may be revised yetagain.
- ARG1: the weakness in both the junk bond market and the stock market
- ARG2: traders
- rel: given

Example 6 (nominal rel: giving): Gift - giving is also a technical job
- ARG1: Gift
- rel: giving

### give-14 (to be likely to, given to)

- ARG1: Person entity likely to do/be a certain way
- ARG2: Thing which arg1 is likely to do/be

Example 1 (All arguments): As the pyramids were already about 2500 years old when Diodorus wrote his World History , one is given to wonder what his authority might have been for such a vivid description .
- ARG1: one
- ARG2: to wonder what his authority might have been for such a vivid description.
- rel: given

### give-16 (idiomatic: to care (give a crap, etc))

- ARG0: giver/carer
- ARG1: crap/shit/poopoo, ect
- ARG2: about what

Example 1 (give a shit): I 've been threatened physically twice .... like I give a shit ....
- ARG0: I
- ARG1: a shit
- rel: give

Example 2 (all args): I mean you do n't really think that any of these guys really give a shit about their party or their nation , do ya ?
- ARG0: any of these guys
- ARGM-ADV: really
- ARG1: a shit
- ARG2: about their party of their nation
- rel: give

Example 3 (any synonym for excrement will do...): Plus , you have to find 250 students who-1 *PRO*-1 even pay attention to the student council , and give enough of a poo poo todo something about it .
- ARG0: *PRO*-1
- ARGM-SLC: who -> [250 students]
- ARGM-ADV: even
- ARG1: enough of a poo poo to do something about it
- rel: give

### give-17 (yield when pressure is applied)

- ARG1: thing yielding
- ARG2: to what

Example 1 (both args): He is hoping your arm is going to drop off and you-1 are going *-1 to give to the pressure of his pulling
- ARG1: *-1
- ARG2: to the pressure of his pulling
- rel: give

Example 2 (Standard): People just have to accept that something must give .
- ARG1: something
- ARGM-MOD: must
- rel: give

### give-LV (light verb)

- (no roles)

## reason

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

## sure

### sure-02 (believing absolutely)

- ARG0: believer
- ARG1: belief

Example 1 (both args): Peter Anthony , who runs an employment agency in New York , decries program trading as `` limiting the game to a few , '' but he also is n't sure it should be more strictly regulated .
- ARG0: he
- ARGM-ADV: also
- ARGM-NEG: n't
- ARG1: it should be more strictly regulated
- rel: sure

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

## interviewed (found as interview)

### interview-01 (speak with)

- ARG0: interviewer
- ARG1: interviewee
- ARG2: purpose or subject matter of interview

Example 1 (passive): ([Both men]-1 declined *trace*-1 to be interviewed *trace*-1 for this article.)
- ARG1: *trace*-1 (= Both men)
- ARG2: for this article
- rel: interviewed

Example 2 (job interview): Mary interviewed John for a job with BigHugeCo.
- ARG0: Mary
- ARG1: John
- ARG2: for a job with BigHugeCo
- rel: interviewed

Example 3 (inverted args): John interviewed with BigHugeCo for a job.
- ARG1: John
- ARG0: with BigHugeCo
- ARG2: for a job
- rel: interviewed

Example 4 (autogen1): their -LCB- job -RCB- interview suit
- ARG2: job
- rel: interview

Example 5 (autogen2): his Rolling Stone interview in 1980
- ARG1: his
- ARG0: Rolling Stone
- ARGM-TMP: in 1980
- rel: interview

Example 6 (with LOC): a recent radio interview
- ARGM-TMP: recent
- ARGM-LOC: radio
- rel: interview

Example 7 (these tend to be arg1): the interview with Bob Shapiro
- ARG1: with Bob Shapiro
- rel: interview

Example 8 (same form, with arg0): my interview with general John Abizaid
- ARG0: my
- ARG1: with John Abizaid
- rel: interview

Example 9 (with arg2): an exclusive interview with Iraqi Prime Minister Ibrahim al - Jaafari about his visit with President Bush and the huge challenges still facing his country
- ARGM-MNR: exclusive
- ARG1: with Iraqi Prime Minister Ibrahim al - Jaafari
- ARG2: about his visit with President Bush and the huge challenges still facing his country
- rel: interview

Example 10 (eh-- I knew it-- same form, but "with" arg 0. Call these arg1 unless you're sure though.): In an interview with CNN , Borislav Milosevic accused Western nations
- ARG0: with CNN
- rel: interview

Example 11 (with COM): In his joint interview with his wife, Denise
- ARG1: his
- ARGM-MNR: joint
- ARGM-COM: with his wife, Denise
- rel: interview

## say

### say-01 (say)

- ARG0: Sayer
- ARG1: Utterance
- ARG2: Hearer
- ARG3: Attributive

Example 1 (Transitive): A Lorillard spokeswoman said "This is an old story."
- ARG0: A Lorillard spokeswoman
- ARG1: "This is an old story"
- rel: said

Example 2 (Fronted): [Kent cigarettes were sold]-1, the company said *trace*-1
- ARG0: the company
- ARG1: *trace*-1
- rel: said

Example 3 (Inverted): [What matters is what advertisers will pay]-1, said *trace*-1 Newsweek's chairman
- ARG1: *trace*-1
- ARG0: Newsweek's chairman
- rel: said

Example 4 (Split): S-["What you have to understand," said John [*?*], "is that Philly literally stinks."]
- ARGM-DSP: [*?*] (tag the leaf node of the *?* itself, and '*' link to the S node containing the ENTIRE utterance
- ARG1: [*?*] (tag the parent node)
- ARG0: John
- rel: said

Example 5 (with listener): John said to Mary: "you're an idiot."
- ARG0: John
- ARG2: to Mary
- ARG1: "you're an idiot"
- rel: said

Example 6 (Weird, attributive usage:): "Well that's odd," said John of the disappearance of his nose.
- ARG1: "Well that's odd"
- ARG0: John
- ARG3: of the disappearance of his nose
- rel: said

Example 7 (split utterance): John-1 is said *trace*-1 to be an idiot.
- ARG1: *trace*-1 to be an idiot
- rel: said

### say-02 (discourse function)

- (no roles)

Example 1 (TAKES NO ARGS): Do you think 0 this war is going *-1 to end up...much less popular say a year from now...?
- rel: say

## spy

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

## rising (found as rise)

### rise-01 (go up)

- ARG0: causer of inception/rising of arg1, likely to occur with light verb
- ARG1: Logical subject, patient, thing rising
- ARG2: EXT, amount risen
- ARG3: start point
- ARG4: end point
- ARGM: medium

Example 1 (all args): Sales rose 4% to $3.28 billion from $3.16 billion.
- ARG1: Sales
- ARG2: 4%
- ARG4: to $3.28 billion
- ARG3: from $3.16 billion
- rel: rose

Example 2 (arg2 as manner): The index rose modestly as well.
- ARG1: The index
- ARG2: modestly
- ARGM-DIS: as well
- rel: rose

Example 3 (with locative): Stock prices rose fractionally in moderate trading.
- ARG1: Stock prices
- ARG2: fractionally
- ARGM-LOC: in moderate trading
- rel: rose

Example 4 (with temporal): Georgia Gulf stock rose $1.75 a share yesterday
- ARG1: Georgia Gult stock
- ARG2: $1.75 a share
- ARGM-TMP: yesterday
- rel: rose

Example 5 (non-financial usage): Mr. Hahn rose swiftly through the ranks
- ARG1: Mr Hahn
- ARGM-MNR: swiftly
- ARGM-LOC: through the ranks
- rel: rose

Example 6 (and again): The sun rises in the west.
- ARG1: The sun
- ARGM-LOC: in the west
- rel: rises

Example 7 (Example with args 2, 3, and 4): a monthly rise of 0.2 % in September from August
- ARGM-TMP: monthly
- ARG2: of 0.2 %
- ARG4: in September
- ARG3: from August
- rel: rise

Example 8 (Example with most args): a 6 % rise in revenue to $ 323.2 million from $ 305.7 million
- ARG2: 6 %
- ARG1: in revenue
- ARG4: to $ 323.2 million
- ARG3: from $ 305.7 million
- rel: rise

Example 9 (None numeric rise): Slobodan Milosevic's rise to power
- ARG1: Slobodan Milosevic's
- ARG4: to power
- rel: rise

## really

### really (:degree very)

- (no roles)

Example 1 (very): This issue is really important.

## suspicious

### suspicious-02 (being prone to suspect; distrustful)

- ARG0: suspecter
- ARG1: thing or event viewed suspiciously
- ARG2: act expressing suspicion, often a glance

Example 1 (adjectival rel: suspicious): It would have to be explained in great predictive detail for me to consider it , and even then I would be highly suspicious .
- ARGM-TMP: even then
- ARG0: I
- ARGM-MOD: would
- ARGM-EXT: highly
- rel: suspicious

Example 2 (adjectival rel: suspicious): Many people are suspicious of lobbyists
- ARG0: Many people
- ARG1: of lobbyists
- rel: suspicious

### suspicious-03 (acting in a manner that evokes suspicion; shady)

- ARG1: thing or event acting in ways that evoke suspicion

Example 1 (adjectival rel: suspicious): The security guards look out for any suspicious activity
- ARG1: activity
- rel: suspicious

Example 2 (AMR only adverbial functions): Timmy was suspiciously silent about the missing cookies
- ARG1: silent
- rel: suspiciously

Example 3 (adjectival rel: suspicious; arg2 as subject): I'll be honest, though: overly perfect-looking food is suspicious to me.
- ARG1: overly perfect-looking food
- ARGM-ADV: to me
- rel: suspicious

## term

### term-01 (assign a label)

- ARG0: caller
- ARG1: item being labelled
- ARG3: attribute

Example 1 (passivized): Reuters Holdings PLC said Michael Reupke resigned as general manager to pursue unspecified interests, a move [0]-1 the news organization termed *trace*-1 an ``amicable separation.''
- ARG0: the news organization
- ARG1: *trace*-1 (= [0])
- ARGM-SLC: [0] -> a move
- ARG3: an `` amicable separation
- rel: termed

Example 2 (all args): They immediately termed the proposal-1 *trace*-1 inadequate .
- ARG0: They
- ARGM-TMP: immediately
- ARG1: the proposal-1
- ARG3: *trace*-1 inadequate
- rel: termed

## even

### even-02 (equalize, make uniform, equal, without variation)

- ARG1: first equal/unvaried thing
- ARG2: second equal thing, even in comparison to what
- ARG3: domain of evenness

Example 1 (arg1): Good urine , balance even ,
- ARG1: balance
- rel: even

Example 2 (al args): Zeno the Epicurean, who has been mentioned before. k Timocrates, according to Diogenes Laertius, was even with him inhis abuses.
- ARG1: Zeno the Epicurean, who has been mentioned before. k Timocrates, according to Diogenes Laertius
- ARG2: with him
- ARG3: in his abuses
- rel: even

Example 3 (Both args): Pearl's evening of the amount of batter in each cupcake liner resulted in perfectly even cupcakes.
- ARG1: Pearl's
- ARG2: of the amount of batter in each cupcake liner
- rel: evening

### even-03 (divisible by 2)

- ARG1: number divisible by 2

Example 1 (arg1): The crossing number is even if and only if the point is outside the polygon.
- ARG1: The crossing number
- ARGM-ADV: if and only if the point is outside the polygon
- rel: even

## according (found as accord)

### accord-01 (to give)

- ARG0: giver
- ARG1: gift
- ARG2: given-to

Example 1 (passive): The drug will be given treatment investigational new drugstatus, [a label]-1 accorded [*trace*-1]to drugs believed effective but lackingformal approval.
- ARG1: *trace*-1 (= a label)
- ARG2: to drugs believed effective but lacking formal approval.
- rel: accorded

Example 2 (active): Several of the city's black leaders, including Democratic mayoralnominee David Dinkins, have spoken out for racial gerrymandering [*0][*T*-1]to accord blacks and Hispanics ``the fullest opportunity forrepresentation.''
- ARG0: [*T*-1] (= [*0])
- ARGM-SLC: [*0] -> racial gerrymandering
- ARG2: blacks and Hispanics
- ARG1: ``the fullest opportunity for representation.''
- rel: accord

Example 3 (Args 1 & 2): No nation disputed the accordance to Canada of rights of access.
- ARG2: to Canada
- ARG1: of rights of access
- rel: accordance

Example 4 (Args 1 & 2 again): The accordance of a fair trial to each citizen is a principle of the Constitution.
- ARG1: of a fair trial
- ARG2: to each citizen
- rel: accordance

Example 5 (All arguments): He wanted to challenge their accordance of legitimacy to the political system.
- ARG0: their
- ARG1: of legitimacy
- ARG2: to the political system
- rel: accordance

### accord-02 (conform to regulations, procedures, expectations; 'in accordance with')

- ARG0: follower of procedure
- ARG1: action done
- ARG2: regulations, procedure, or expectations accorded with

Example 1 (Likely most typical usage): This product must be disposed of in accordance with federal regulation.
- ARG2: with federal regulation
- rel: accordance

Example 2 (in accordance with): This product must be disposed of in accordance with federal regulation.
- ARG1: This product must be disposed of
- ARG2: federal regulation
- rel: in accordance with

Example 3 (accords): His shift accords with the transformation of the colony's status, and was one of the details that helped me to recognize the model of dual chieftaincy in the Powhatans.
- ARG1: His shift
- ARG2: with the transformation of the colony's status
- rel: accords

### accord-03 (agreement (e.g. 'peace accord'))

- ARG0: first party in agreement, both parties when mentioned together
- ARG1: subject of agreement
- ARG2: second party in agreement

Example 1 (nominal with treaty subject): Japan will help monitor weapons and soldiers under the peace accord that ended Nepal's decade-long Maoist insurgency.
- ARG1: peace
- ARGM-ADJ: that ended Nepal's decade-long Maoist insurgency.
- rel: accord

Example 2 (args 0 and 1): The European post-Cold War security accord
- ARG0: European
- ARGM-TMP: post-Cold War
- ARG1: security
- rel: accord

Example 3 (Args 0 & 2): One can see, that satisfactory accordance of calculation results with experiments is observed.
- ARGM-MNR: satisfactory
- ARG0: of calculation results
- ARG2: with experiments
- rel: accordance

Example 4 (All arguments, invented example): Mary's accordance with John on the subject of finance was quite surprising to all.
- ARG0: Mary's
- ARG2: with John
- ARG1: on the subject of finance
- rel: accordance

## evidence

### evidence-01 (provide proof for, proven/proving)

- ARG0: proof
- ARG1: thing proved

Example 1 (as evidenced): The use of [the abominable construction practices in the Soviet Union]-1 -- as *trace*-1 evidenced *trace*-1 by the collapse of sand apartment blocks during the Armenian earthquake -- as a metaphor for the U.S. economic system was a sublime example of Mr. Cockburn's satirical muse.
- ARG1: *trace*
- ARG0: by the collapse of sand apartment blocks during the Armenian earthquake
- rel: evidenced

Example 2 (untraceable): And it has remained there, as *trace*-1 evidenced *trace*-1 by its reappearance in a 1972 CBS sitcom called ``Bridget Loves Bernie,'' whose sole distinction was that it led to the real-life marriage of Meredith Baxter and David Birney.
- ARG1: *trace*
- ARG0: by its reappearance in a 1972 CBS sitcom called ``Bridget Loves Bernie,'' whose sole distinction was that it led to the real-life marriage of Meredith Baxter and David Birney
- rel: evidenced

Example 3 (more obviously verbal): [Sluggish demand]-1 was also evidenced *trace*-1 by the weak 2.41-to-1 bid-to-cover ratio, which was lower than the average 2.79-to-1 ratio at the last 12 similar auctions.
- ARGM-DIS: also
- ARG1: *trace*
- ARG0: by the weak 2.41-to-1 bid-to-cover ratio, which was lower than the average 2.79-to-1 ratio at the last 12 similar auctions
- rel: evidenced

Example 4 (Adjective usage: evident): This was evident from his confusion and embarrassment in reading the minutes.
- ARG1: This
- ARG0: from his confusion and embarrassment in reading the minutes.
- rel: evident

## presented (found as present)

### present-01 (give)

- ARG0: giver
- ARG1: thing given
- ARG2: given to
- ARG3: secondary attribute of thing given

Example 1 (just transitive): But such a combination also presents great risks.
- ARGM-DIS: But
- ARG0: such a combination
- ARGM-DIS: also
- ARG1: great risks
- rel: presents

Example 2 (with attribute): But I think we are losing credibility because when the market does this, it doesn't present itself as a rational investment.
- ARG0: it
- ARGM-NEG: n't
- ARG1-REC: itself
- ARG3: as a rational investment
- rel: present

Example 3 (with recipient): John presented Mary with a bouquet of wilted dandelions.
- ARG0: John
- ARG2: Mary
- ARG1: with a bouquet of wilted dandelions
- rel: presented

Example 4 (Args 0, 1, 2): Jakob's presentation of the gift to the foundation was surprisingly generous.
- ARG0: Jakob's
- ARG1: of the gift
- ARG2: to the foundation
- rel: presentation

### present-101 (to emerge during birth)

- ARG1: infant
- ARG2: body part initially emerging
- ARG3: orientation of infant: breech, vertex, transversely, etc

Example 1 (Infant as subject): It is normal for the fetus to present breech in the second trimester and spontaneously invert sometime in the third trimester.
- ARG1: the fetus
- ARG3-MNR: breech
- ARGM-TMP: in the second trimester
- rel: present

Example 2 (Body part as subject): A variation is when-1 one or both feet present first *T*-1, called a "footling breech".
- ARG2: one or both feet
- ARGM-MNR: first
- ARGM-TMP: *T*-1
- rel: present

Example 3 (all arguments): Baby John presented transversely, right shoulder first.
- ARG1: Baby John
- ARG3-MNR: transversely
- ARG2: right shoulder
- ARGM-MNR: first
- rel: presented

Example 4 (Arg1, 3): The baby's breech presentation required intervention from the obstetrician.
- ARG1: The baby's
- ARG3: breech
- rel: presentation

### present-102 (to appear in a clinical setting)

- ARG0: Patient presenting
- ARG1: Disorder presenting
- ARG2: Manner of presentation (symptoms, illness)

Example 1 (Disorder as Arg1): Can diabetic neuropathy present as flank radicular pain ?
- ARG1: diabetic neuropathy
- ARG2-MNR: as flank radicular pain
- rel: present

Example 2 (Patient as Arg0): Elderly patient presented in clinic this morning with lower back pain
- ARG0: Elderly patient
- ARGM-LOC: in clinic
- ARGM-TMP: this morning
- ARG2-MNR: with lower back pain
- rel: presented

Example 3 (Arg0, 2): The patient's presentation with severe chest pains caused the doctors to immediately administer and ECG test.
- ARG0: The patient's
- ARG2: with severe chest pains
- rel: presentation

Example 4 (Arg1, 2): Diabetic neuropathy's inital presentation as flank radicular pain can throw off less experienced diagnosticians.
- ARG1: Diabetic neuropathy's
- ARGM-TMP: initial
- ARG2: as flank radicular pain
- rel: presentation

### present-02 (in attendance)

- ARG1: entity present
- ARG2: where

Example 1 (both args): I am not for a law that prevents people from keeping a gun in their home although I am for safety regulations especially where-1 children are present *T*-1.
- ARG1: children
- ARG2: *T*-1
- rel: present

Example 2 (with TMP): Mother of newborn trapped in sewer was present for rescue
- ARG1: Mother of newborn trapped in sewer
- ARGM-TMP: for the rescue
- rel: present

## court

### court-01 (pursue (romantically))

- ARG0: suitor
- ARG1: courted

Example 1 (romantically?): All foreign markets are aggressively courting U.S. business.
- ARG0: All foreign markets
- ARGM-MNR: aggressively
- ARG1: U.S. business
- rel: courting

Example 2 (semi-idiomatic: courting disaster): The danger that [Ms. Bogart]-1 seems *trace*-1 to be courting *trace* here is one of obfuscation rather than rejuvenation, a vision so at odds with the playwright's that the two points of view nullify, rather than illuminate, each other.
- ARG0: *trace*
- ARG1: *trace*
- ARGM-RCL: that -> The danger
- ARGM-LOC: here
- rel: courting

## due

### due-01 (owed, required)

- ARG0: ower
- ARG1: recipient, entity owed/expecting arg2
- ARG2: thing expected, owed

Example 1 (long awaited): Her husband is due for a hip replacement in June.
- ARG1: Her husband
- ARG2: for a hip replacement in June.
- rel: due

Example 2 (all args): I am due him a debt of gratitude for. his valuable information, both verbal and clinical.
- ARG0: I
- ARG1: him
- ARG2: a debt of gratitude
- ARGM-CAU: for his valuable information, both verbal and clinical
- rel: due

### due-02 (caused by, attributable to)

- ARG0: cause, stimulus
- ARG1: thing caused, experiencer

Example 1 (Arg 1 will often appear in the sentence before arg 0): The Blackhawks' Stanley Cup victory was due to their superior speed and coaching.
- ARG1: The Blackhawk's Stanley Cup victory
- ARG0: to their superior speed and coaching.
- rel: due

### due-03 (be scheduled for, planned for a time)

- ARG1: thing that is scheduled
- ARG2: what arg1 is scheduled to do

Example 1 (All args): Samples are due to arrive this week.
- ARG1: Samples
- ARG2: to arrive
- ARGM-TMP: this week
- rel: due

## listened (found as listen)

### listen-01 (attend to a sound)

- ARG0: listener
- ARG1: sound or speaker

Example 1 (transitive): ``We watch the same indicators and listen to the same prognosticators.''
- ARG0: We
- ARG1: to the same prognosticators
- rel: listen

Example 2 (intransitive): Willliam Greaney said that the influence of the appeals court in New York ``will make insurers sit up and listen.''
- ARG0: insurers
- rel: listen

Example 3 (Arg0,1): His listening to loud music all night drove me crazy.
- ARG0: His
- ARG1: to loud music
- ARGM-TMP: all night
- rel: listening

## less

### less-02 (not as much as)

- ARG1: thing that is less
- ARG2: thing that is more
- ARG3: less of what

Example 1 (args 1,2): I go to therapy -LRB- for other reasons also -RRB- and they have encouraged me to pick a number of times to check , obviously that-1 [*-1] is less than 20 , and to stick to it and cut down that way .
- ARG1: [*-1]
- ARG2: [than] [20]
- rel: less

Example 2 (args 1, 3): Although it is less of a problem during the day it does not feel normal during the day .
- ARG1: it
- ARG3: of a problem
- ARGM-TMP: during the day
- rel: less

### less-03 (akin to "not": i'm less than impressed!)

- ARG1: Topic
- ARG2: Comment that is NOT quite true of Arg1

Example 1 (All args): Now , with the various " Occupy " movements , it is -LRB- or ought to be -RRB- obvious that a great many people are less than enchanted with capitalism and its expression in the idustrial democracies , as well as in the countries into which capitalists from the industrial democracies go to invest .
- ARG1: a great many people
- ARG2: than enchanted with capitalism and its expression in the idustrial democracies , as well as in the countries into which capitalists from the industrial democracies go to invest .
- rel: less

## sounds (found as sound)

### sound-01 (seem, appear, to the ear)

- ARG1: thing seeming
- ARG2: attribute of arg1
- ARG3: viewer

Example 1 (just arg1): How does a nice new tax, say 5%, on any financial transaction sound?
- ARG1: a nice new tax, say 5%, on any financial transaction
- rel: sound

Example 2 (with arg2): ``Credibility sounds intangible.
- ARG1: Credibility
- ARG2: intangible
- rel: sounds

Example 3 (all args): John sounds to me like a real idiot.
- ARG1: John
- ARG3: to me
- ARG2: like a real idiot
- rel: sounds

### sound-02 (make a sound, production of noise)

- ARG0: agent who activates arg1
- ARG1: noise-maker
- ARG2: the sound itself (the name of the sound/song, etc., not just a characteristic)
- ARG3: characteristic of the sound

Example 1 (alarm): John sounded the alarm: "The British are coming, the British are coming!"
- ARG0: John
- ARG1: the alarm: "The British are coming, the British are coming!"
- rel: sounded

Example 2 (just arg2): Our citizens were massacred to the sound of that anthem
- ARG2: of that anthem
- rel: sound

Example 3 (just arg1): Moments later , another shot and the sound of someone in pain .
- ARG1: of someone in pain
- rel: sound

Example 4 (arg3): They hollow out the bat and stick the cork in there to mask the hollow sound .
- ARG3: hollow
- rel: sound

Example 5 (noisy secret- args 1 and 3): Despite its clunking sound it was one of Hitler 's secret weapons .
- ARG1: its
- ARG3: clunking
- rel: sound

Example 6 (arg1): listen to the sound of the waves the wind makes in the rice paddies to discover if the rice is ripe ;
- ARG1: of the waves the wind makes in the rice paddies
- rel: sound

Example 7 (sunken junk- arg3): It is said that , late at night , the sunken junks make moaning sounds .
- ARG3: moaning
- rel: sounds

### sound-04 (do an ultrasound)

- ARG0: agent; doctor; technician
- ARG1: subject

Example 1 (with arg 1): Fetal ultrasound
- ARG1: fetal
- rel: ultrasound

## like

### like-01 (have affection towards, be fond of, enjoy (habitually))

- ARG0: liker
- ARG1: object of affection

Example 1 (like-v: fond of): Mary likes John.
- ARG0: Mary
- ARG1: John
- rel: likes

Example 2 (like-v: prefer): John likes dill pickles on his grilled cheese sandwiches.
- ARG0: John
- ARG1: dill pickles on his grilled cheese sandwiches
- rel: likes

Example 3 (like-v: enjoy to do something): John likes to play tennis.
- ARG0: John
- ARG1: to play tennis
- rel: likes

Example 4 (like-v: enjoy doing something): Mary likes watching movies.
- ARG0: Mary
- ARG1: watching movies
- rel: likes

Example 5 (liking-n: just arg0): It 's the only team that has the capacity to send me into the depths of despair -LRB- all too often for my liking -RRB- , or run around screaming and shouting with joy .
- ARG0: my
- rel: liking

Example 6 (liking-n: True story. Both args): 30% of my liking the decemberists is their obsession with boats
- ARG0: my
- ARG1: the decemberists
- rel: liking

Example 7 (liking-n: Harsh. both args): The Emperor has demonstrated his liking to inflict pain on people just as people born under the sign Aries often do.
- ARG0: his
- ARG1: to inflick pain on people
- ARGM-MNR: just as people born under the sign Aries often do
- rel: liking

Example 8 (hypothetical, with 'would like'): I loved the movie, but I'm not sure whether you would like it.
- ARG0: you
- ARG1: it
- rel: like

### like-02 (would like, wish, want (polite))

- ARG0: wanter
- ARG1: thing wanted

Example 1 (like-v: would like to): I would like to find a flight that goes from Boston to Orlando.
- ARG0: I
- ARG1: to find a flight that goes from Boston to Orlando
- rel: would like

Example 2 (like-v: 'd like something): I'd like a flight on American from Newark to Nashville.
- ARG0: I
- ARG1: a flight on American from Newark to Nashville
- rel: 'd like

Example 3 (like-v: with 'if' but without 'would' (rare)): We can leave now, if you like.
- ARG0: you
- ARG1: [We] [leave now]
- rel: like

Example 4 (like-v: with 'whenever' but without 'would' (rare)): You can come whenever you like.
- ARG0: you
- ARG1: [You] [come]
- rel: like

### like-04 (similar)

- ARG1: first item in comparison
- ARG2: second item in comparison

Example 1 (like-j: both args): He had a colonoscopy performed today with a decent amount of stool that did note an hepatic flexure mass , which-1 [*-1] was flat and broad and plaque - like .
- ARG1: [*-1]
- ARG2: plaque
- rel: like

## criticism

### criticism-04 (judge carefully, but not necessarily negatively, esp art/literature)

- ARG0: judge, critic
- ARG1: work judged, critiqued

Example 1 (criticism-n): First, his political work remains more prominent than his literary criticism.
- ARG0: his
- ARGM-ADJ: literary
- rel: criticism

Example 2 (criticism-n: both args): In his literary criticism of radical writers, he is very sharp and not entirely inaccurate in describing both them and himself ata certain stage as a "snob"
- ARG0: his
- ARGM-ADJ: literary
- ARG1: of radical writers
- rel: criticism

## number

### number-01 (have a certain quantity)

- ARG1: thing being counted
- ARG2: count, number, quantity

Example 1 (ergative): Items listed as being in short supply numbered only about a dozen, but they included one newcomer: milk and milk powder.
- ARG1: Items listed as being in short supply
- ARG2: only about a dozen
- rel: numbered

Example 2 (passive): It is a certainty that [Mr. Barre's days]-1 are numbered *trace*-1.
- ARG1: *trace*
- rel: numbered

## show

### show-01 (cause to see)

- ARG0: shower
- ARG1: thing seen/shown
- ARG2: seer

Example 1 (seer as NP): Can you show me evening flights from Nashville to Houston that serve dinner?
- ARGM-MOD: Can
- ARG0: you
- ARG2: me
- ARG1: evening flights from Nashville to Houston that serve dinner
- rel: show

Example 2 (with WH-clause): The case showed how testing was being overused.
- ARG0: The case
- ARG1: how testing was being overused
- rel: showed

Example 3 (Example with arg 1 (but not arg 0, because of 'snaps')): "We 're not running that ad campaign any more," Mr.Straszheim snaps in a rare show of irritation .
- ARGM-TMP: rare
- ARG1: of irritation
- rel: show

Example 4 (Example with both args): John's show of strength was more than impressive
- ARG0: John's
- ARG1: of strength
- rel: show

Example 5 (within LVC): According to department policy , prosecutors must make a strong showing that lawyers ' fees came from assets tainted by illegal profits before any attempts at seizure are made .
- ARGM-ADV: According to department policy
- ARG0: prosecutors
- ARGM-MOD: must
- ARGM-LVB: make
- ARGM-MNR: strong
- ARG1: that lawyers ' fees came from assets tainted by illegal profits
- ARGM-TMP: before any attempts at seizure are made .
- rel: showing

### show-04 (show/production)

- ARG0: Show creator
- ARG1: Type of show, title, or message
- ARG2: Audience
- ARG3: Source (TV/channel/venue to watch at)

Example 1 (Example of arg 0 as a country of creation): Europe 's TV shows
- ARG0: Europe 's
- ARG3: TV
- rel: shows

Example 2 (Example with arg 1 and 3): TV's hottest reality shows
- ARG3: TV's
- ARG1: reality
- rel: shows

Example 3 (Arg 3 when its not TV): Broadway's new Andrew Lloyd Webber show
- ARG3: Broadway's
- ARG0: Andrew Lloyd Webber
- rel: show

Example 4 (Arg 3 as a channel): A new show for FX
- ARG3: for FX
- rel: show

Example 5 (Arg 1 as a title): The TV show Mike and Buffy
- ARG3: TV
- ARG1: Mike and Buffy
- rel: show

Example 6 (Example with arg 2): Everyone's favorite show
- ARG2: Everyone's
- rel: show

## support

### support-01 (lend aid, credence to)

- ARG0: helper
- ARG1: person, thing or project being supported

Example 1 (benefactive): The finding probably will support those who argue that the US should regulate the class of asbestos including crocidolite more closely.
- ARG0: The finding
- ARGM-ADV: probably
- ARGM-MOD: will
- ARG1: those who argue that the US should regulate the class of asbestos including crocidolite more closely.
- rel: support

Example 2 (adjectival rel: supportive): Credit growth was supportive of continued recovery in Q1.
- ARG0: Credit growth
- ARG1: of continued recovery
- ARGM-TMP: in Q1
- rel: supportive

Example 3 (Example with both args): his support for the Constitution
- ARG0: his
- ARG1: for the Constitution
- rel: support

Example 4 (Slightly different arg 1 (thing being supported)): side support
- ARG1: side
- rel: support

Example 5 (Another example with both args): Republican support for Alito
- ARG0: Republican
- ARG1: for Alito
- rel: support

Example 6 (awkward sentence): The party's base support, liberal woman's groups, civil rights groups, environmental groups, the foot that raises money knock on doors and vote come rain or shine, want to fight over Alito.
- ARG1: The party's
- ARG0: base
- rel: support

## including (found as include)

### include-01 (include)

- ARG0: agent, entity causing some grouping
- ARG1: theme, thing being included in some group
- ARG2: group

Example 1 (include-v: group as PP): John includes Mary in the list of people he admires.
- ARG0: John
- ARG1: Mary
- ARG2: in the list of people he admires
- rel: includes

Example 2 (include-v: group as subject): The project did not include Seymour Cray.
- ARG2: The project
- ARGM-NEG: not
- ARG1: Seymour Cray
- rel: include

Example 3 (include-v: no group mentioned): The government includes money spent on residential renovation.
- ARG0: The government
- ARG1: money spent on residential renovation
- rel: includes

Example 4 (include-v: passive, no group): [Several important divisions]-1 weren't included *trace*-1
- ARGM-NEG: n't
- ARG1: *trace*
- rel: included

Example 5 (include-v: passive, with group as PP): [Losses from the earthquake in California]-1 would be included *trace*-1 in 4th QTR results.
- ARG1: *trace*
- ARGM-MOD: would
- ARG2: in 4th QTR results
- rel: included

Example 6 (include-v: PP-group in subject position): ...included *trace*-1 on the list are [John and Mary]-1
- ARG2: on the list
- ARG1: *trace*
- rel: included

Example 7 (inclusive-j): Maybe they-1 wanted *PRO*-1 to be inclusive because they want to sell you a car and your race does n't matter one way or the other .
- ARG0: *PRO*-1
- ARGM-CAU: because they want to sell you a car and your race doesn't matter one way or the other
- rel: inclusive

Example 8 (inclusion-n: Arg0,1,2): Many attribute China's rise to their inclusion of capitalism into their society.
- ARG0: their
- ARG1: of capitalism
- ARG2: into their society
- rel: inclusion

### include-91 (subset)

- ARG1: subset (or member)
- ARG2: superset
- ARG3: relative size of subset compared to superset

Example 1 (percentage): 10% of smokers die of lung cancer.
- ARG1: people who die of lung cancer
- ARG2: smokers
- ARG3: 10%
- rel: of

Example 2 (190 of 200): 190 of 200 British newspapers owned by Murdoch.
- ARG1: 190 newspapers owned by Murdoch
- ARG2: 200 British newspapers
- rel: of

Example 3 (including): The company employs several translators, including five from China.
- ARG1: 5 people from China
- ARG2: several translators employed by company
- rel: including

## police

### police-01 (monitor, watch, serve as   police for, enforcing the law)

- ARG0: police
- ARG1: thing or place being monitored

Example 1 (pretty simple, really): ``We can't police the many organizations that have sprung up in the last few years using part of our name.
- ARG0: We
- ARGM-NEG: n't
- ARG1: the many organizations that have sprung up in the last few years using part of our name
- rel: police

Example 2 (intransitive): Governments must compel private companies to aid them in their policing, the cost of which is unknown...
- ARG0: their
- ARGM-ADJ: the cost of which is unknown
- rel: policing

## respond

### respond-01 (give an answer, reply)

- ARG0: replier
- ARG1: in response to
- ARG2: answer

Example 1 (respond-v: intransitive): [The board]-1 has 10 business days *trace*-1 to respond.
- ARG0: *trace*
- rel: respond

Example 2 (respond-v): People familiar with Nekoosa said [its board]-1 isn't likely to meet before the week after next *trace*-1 to respond to the bid.
- ARG0: *trace*
- ARG1: to the bid
- rel: respond

Example 3 (respond-v: quotative response): A Boeing spokesman responded: ``All along the company has said there was no grounds for criminal prosecution.''
- ARG0: A Boeing spokesman
- ARG2: All along the company has said there was no grounds for criminal prosecution
- rel: responded

Example 4 (respond-v: by an action response): Nashua immediately responded by strengthening a poison-pill plan and saying it will buy back up to one million of its shares, or 10.4% of the 9.6 million outstanding.
- ARG0: Nashua
- ARGM-TMP: immediately
- ARG2: by strengthening a poison-pill plan and saying it will buy back up to one million of its shares, or 10.4% of the 9.6 million outstanding
- rel: responded

Example 5 (respond-v: with an action response): Poquet, trying to avoid the ``gadget'' label, responded with the tag line, ``The Poquet PC -- a Very Big Computer.''
- ARG0: Poquet
- ARGM-ADV: trying to avoid the `` gadget '' label
- ARG2: with the tag line , `` The Poquet PC -- a Very Big Computer
- rel: responded

Example 6 (respond-v: Medical: Arg0 as patient): In this patient, who-2 *T*-2 is not responding to nonsteroidal anti-inflammatory drugs for superficial thrombophlebitis, what is round two?
- ARG0: *T*-2
- ARGM-NEG: not
- ARG1: to nonsteroidal anti-inflammatory drugs for superficial thrombophlebitis
- rel: responding

Example 7 (respond-v: Medical: Arg0 as illness/condition): History of at least 2 urinary tract infections which-1 *T*-1 have responded to treatment.
- ARG0: *T*-1
- ARG1: to treament
- rel: responded

Example 8 (responding-n: Arg0,1): But there was a delay of about one year in his responding to the call.
- ARG0: his
- ARG1: to the call
- rel: responding

Example 9 (response-n: Tricky example): prices dropped in response to gains in the stock market and losses in Treasury securities
- ARG0: prices
- ARG2: dropped
- ARG1: to gains in the stock market and losses in Treasury securities
- rel: response

Example 10 (response-n: Example with arg 1 and 2): the computer-guided selling in response to those developments
- ARG2: the computer-guided selling
- ARG1: to those developments
- rel: response

Example 11 (response-n: Example with arg 1): In response to what Karl Rove said
- ARG1: to what Karl Rove said
- rel: response

Example 12 (response-n: Arg 0): A response from Lucy Dalglish
- ARG0: from Lucy Dalglish
- rel: response

Example 13 (response-n: Arg 0 and 1): Your response to it
- ARG0: Your
- ARG1: to it
- rel: response

Example 14 (response-n: Somewhat rare arg 2 as a literal answer rather than an action/reaction): His two-word, 'no ambition' responce
- ARG0: His
- ARG2: 'no-ambition'
- rel: response

## think

### think-01 (think, believing, imagining)

- ARG0: Thinker
- ARG1: Thought
- ARG2: Attributive (please look at the examples-- this is tricky)

Example 1 (transitive): A Lorillard spokeswoman thought "This is an old story."
- ARG0: A Lorillard spokeswoman
- ARG1: "This is an old story"
- rel: thought

Example 2 (intransitive, with subject of thinking): People weren't thinking about targeting 10 years ago.
- ARG0: People
- ARGM-NEG: n't
- ARG2: about targeting
- ARGM-TMP: 10 years ago
- rel: thinking

Example 3 (transitive, with subject of thinking): People weren't thinking anything about targeting 10 years ago.
- ARG0: People
- ARGM-NEG: n't
- ARG1: anything
- ARG2: about targeting
- ARGM-TMP: 10 years ago
- rel: thinking

Example 4 (fronted): [Kent cigarettes were sold]-1, the company thought *Trace*-1
- ARG0: the company
- ARG1: *trace*
- rel: thought

Example 5 (inverted): [What matters is what advertisers will pay,]-1 thought *Trace*-1 Newsweek's chairman
- ARG1: *trace*
- ARG0: Newsweek's chairman
- rel: thought

Example 6 (split): "What you have to understand," thought [*?*] John, "is that Philly literally stinks."
- ARG1: [*?*]
- ARGM-DSP: [*?*] -> "What you have to understand," thought John [*?*] "is that Philly literally stinks"
- ARG0: John
- rel: thought

Example 7 (attributive): They think of us as a good partner.
- ARG0: They
- ARG1: of us
- ARG2: as a good partner
- rel: think

Example 8 (split utterance): [John]-1 is thought *trace*-1 to be an idiot.
- ARG1: [John][*trace* to be an idiot]
- rel: thought

Example 9 (have a new idea): ``I can't think of any reason to join Lloyd's now,'' says Keith Whitten, a British businessman and a Lloyd's member since 1979.
- ARG0: I
- ARGM-MOD: ca
- ARGM-NEG: n't
- ARG1: of any reason [0] [*]to join Lloyd 's now [*T*-2]
- rel: think

Example 10 (Within LVC): I once had the thought that , relying on Japan 's technology and economic strength she would be able to build a road to the summit or simply put up a cable car.
- ARG0: I
- ARGM-TMP: once
- ARGM-LVB: had
- ARG1: that , relying on Japan 's technology and economic strength she would be able to build a road to the summit or simply put up a cable car.
- rel: thought

Example 11 (no mention of actual thought): She writes of her thoughts of her own possible death as she approaches the birth of one of her children.
- ARG0: her
- ARG2: of her own possible death
- ARGM-TMP: as she approaches the birth of one of her children.
- rel: thoughts

Example 12 (Args 0 & 2): Kim Hyung Jun discusses his thoughts about going solo.
- ARG0: his
- ARG2: about going solo
- rel: thoughts

Example 13 (With thought itself): The thought that we could just do what needs to be done to make it happen never passes their lips.
- ARG1: that we could just do what needs to be done to make it happen
- rel: thought

Example 14 (0,1,2): This would explain people's thinking nothing of advertising 40 years ago.
- ARG0: people's
- ARG1: nothing
- ARG2: of advertising
- rel: thinking

## knows (found as know)

### know-01 (be cognizant of, realize)

- ARG0: knower
- ARG1: fact that is known
- ARG2: entity that arg1 is known ABOUT

Example 1 (know-v: just transitive): I-1 need *trace*-1 to know the aircraft and flight number.
- ARG0: *trace*-1
- ARG1: the aircraft and flight number
- rel: know

Example 2 (know-v: sentential thing known): The other side knows that Giuliani has always been prochoice.
- ARG0: The other side
- ARG1: that Guiliani has always been prochoice
- rel: knows

Example 3 (know-v: attributive): He didn't know (anything) about most of the cases until Wednesday.
- ARG0: He
- ARGM-NEG: n't
- ARG1: anything about most of the cases
- ARGM-TMP: until Wednesday
- rel: know

Example 4 (knowledgeable-j: args 0, 1): I 'm fairly knowledgeable about how the culture works in that part of the world , as is many of the experts .
- ARG0: I
- ARG1: fairly about how the culture works in that part of the world
- ARGM-ADV: as is many of the experts
- rel: knowledgeable

Example 5 (idk-v: both args): *PRO* Idk what I 'm going to do without you
- ARG0: *PRO*
- ARG1: what I'm going to do without you
- rel: Idk

Example 6 (know vs. know about, compare with .02 examples): I know a lot about London. (I have read much about it.)
- ARG0: I
- ARG1: a lot about London
- rel: know

Example 7 (Know TO BE, rephrasable as We know that your words are true.): We know [your words]-1 *-1 to be true.
- ARG0: We
- ARG1: your words to be true
- rel: know

Example 8 (Know TO BE, more weird syntax for PB): They know [the Cherokee Nation]-1 *-1 to be a sovereign state.
- ARG0: They
- ARG1: the Cherokee Nation to be a sovereign state
- rel: know

### know-02 (kennen; be familiar with, have experienced)

- ARG0: knower, person familiar with something
- ARG1: what arg0 is familiar with
- ARG2: what arg1 is known AS
- ARG3: what arg1 is known FOR

Example 1 (know-v: just transitive): I do not know him.
- ARG0: I
- ARGM-NEG: not
- ARG1: him
- rel: know

Example 2 (know vs. know about, compare with .01 examples): I know London well. (I've been there many times.)
- ARG0: I
- ARG1: London
- ARGM-MNR: well
- rel: know

Example 3 (know vs. know about, somewhat ambiguous): I knew a planet that was inhabited by a lazy man.
- ARG0: I
- ARG1: a planet that was inhabited by a lazy man
- rel: knew

Example 4 (known-j): Defendant is known to me and provided his name when I asked.
- ARG1: Defendant
- ARG0: to me
- rel: known

Example 5 (experience): I have known hunger.
- ARG0: I
- ARG1: hunger
- rel: know

Example 6 (known-as): Samuel Langhorne Clemens was known as Mark Twain.
- ARG1: Samuel Langhorne Clemens
- ARG2: as Mark Twain
- rel: known

Example 7 (known-for): Mark Twain was known for the Adventures of Huckleberry Finn.
- ARG1: Mark Twain
- ARG3: for the Adventures of Huckleberry Finn
- rel: known

Example 8 (poetic usage): Her love knew no bounds.
- ARG0: Her love
- ARG1: no bounds
- rel: knew

Example 9 (know-v: attribute): [These nations]-1 are known *trace*-1 as "little tigers"
- ARG1: *trace*-1
- ARG2: as "little tigers"
- rel: known

Example 10 (know-v: infinitival attribute, contrast with sense 01): I have never known a lady to faint in the belfry.
- ARG0: I
- ARGM-NEG: never
- ARG1: a lady to faint in the belfry.
- rel: known

Example 11 (know-v: marginal usage, don't let the FOR syntax confuse you!): Mary knows John for an idiot.
- ARG0: Mary
- ARG1: John
- ARG2: for an idiot
- rel: knows

Example 12 (known-j): . China and India are both ancient countries with ancient cultures , and both have long histories and cultures ; the people of both nations are well known for being hard working , intelligent,and having a good natureed civilization , and have both been humiliated and invaded by foreign races .
- ARG1: the people of both nations
- ARGM-EXT: well
- ARG3: for being hard working , intelligent , and having a good natureed civilizatio
- rel: known

Example 13 (knowledgeable-j: all args): Within those two incidents of which one is not aware, we become knowledgeable of them as primary forces in life.
- ARGM-LOC: within those two incidents of which one is not aware
- ARG0: we
- ARG1: of them
- ARG2: as primary forces in life
- rel: knowledgeable

### know-03 (have an ability, skill, or know-how)

- ARG0: knower, person with an ability/skill
- ARG1: ability or skill

Example 1 (skill as NP object): I know Latin.
- ARG0: I
- ARG1: Latin
- rel: know

Example 2 (skill as how complement): I know how to speak Latin.
- ARG0: I
- ARG1: how to speak Latin
- rel: know

Example 3 (with dances): I know (how to dance the) Macarena.
- ARG0: I
- ARG1: (how to dance) the Macarena
- rel: know

### know-04 (recognize, differentiate)

- ARG0: knower, entity with ability to recognize/differentiate
- ARG1: thing recognized, first thing differentiated
- ARG2: differentiated-from, when separate mention

Example 1 (with Manner): The dog knew his master by his voice.
- ARG0: The dog
- ARG1: his master
- ARGM-MNR: by his voice
- rel: knew

Example 2 (with others): The dog knew his master's call from all the other voices.
- ARG0: The dog
- ARG1: his master's call
- ARG2: from all the other voices.
- rel: knew

Example 3 (with differentiated-from): She doesn't know one end of the car from the other.
- ARG0: She
- ARGM-NEG: n't
- ARG1: one end of the car
- ARG2: from the other
- rel: know

Example 4 (recognize): They know a tasty meal when they eat one.
- ARG0: They
- ARG1: a tasty meal
- ARGM-TMP: when they eat one.
- rel: know

### know-05 (Biblical sense, to have sex with)

- ARG0: Knower, first sexual partner
- ARG1: Known, second sexual partner

Example 1 (A special kind of familiarity): Adam knew Eve.
- ARG0: Adam
- ARG1: Eve
- rel: knew

### know-06 (discourse usage)

- ARG0: you, addressee

Example 1 (Always arg0 only for PB, drop for AMR): John, you know, is an alcoholic.
- ARG0: you
- rel: know

Example 2 (President Bush quote): I just can't envision myself, you know, with a big straw hat and Hawaiian shirt, sitting on some beach.
- ARG0: you
- rel: know

## sends (found as send)

### send-01 (give)

- ARG0: sender
- ARG1: sent
- ARG2: sent-to

Example 1 (ditransitive): They-1 have begun *trace*-1 sending letters explain the program to about five million card holders.
- ARG0: *trace*
- ARG1: letters explain the program
- ARG2: to about five million card holders.
- rel: sending

Example 2 (double object): He sent merchants around the country a form asking them to check one of three answers.
- ARG0: He
- ARG2: merchants around the country
- ARG1: a form asking them to check one of three answers.
- rel: sent

### send-02 (cause to action)

- ARG0: sender
- ARG1: sent, impelled agent
- ARG2: project, impelled action, attribute of arg1

Example 1 (attribute): Lightning-fast trades of huge baskets of stocks and futures can send stock prices reeling in minutes.
- ARG0: Lightning-fast trades of huge baskets of stocks and futures
- ARGM-MOD: can
- ARG1: stock prices
- ARG2: reeling
- ARGM-TMP: in minutes
- rel: send

Example 2 (NP project): Mary sent John on a wild goose chase.
- ARG0: Mary
- ARG1: John
- ARG2: on a wild goose chase
- rel: sent

### send-03 (cause motion)

- ARG0: causer of motion
- ARG1: entity in motion
- ARG2: EXT
- ARG3: start point
- ARG4: end point, attribute of arg1
- ARG5: direction

Example 1 (stupid stock reports): News of the restructuring plan sent Sea Containers' shares up $1 to $62 in New York Stock Exchange composite trading.
- ARG0: News of restructuring plan
- ARG1: Sea Containers' shares
- ARG5: up
- ARG2: $1
- ARG4: to $62
- ARGM-LOC: in New York Stock Exchange composite trading
- rel: sent

## endorse

### endorse-01 (support for a position)

- ARG0: supporter
- ARG1: thing/person supported
- ARG2: for what

Example 1 (passive): [That offer]-1 was endorsed *trace*-1 by the shareholders committee .
- ARG1: *trace*
- ARG0: by the shareholders committee
- rel: endorsed

Example 2 (active): The state has endorsed the New England Electric plan, which promises to limit rate increases to 4.8% annually for seven years.
- ARG0: The state
- ARG1: the New England Electric plan , which promises to limit rate increases to 4.8 % annually for seven years
- rel: endorsed

Example 3 (all args): John endorsed Richard Nixon for president.
- ARG0: John
- ARG1: Richard Nixon
- ARG2: for president
- rel: endorsed

Example 4 (Args 0 and 1): your strong endorsement to repeal this Depression-era fossil
- ARG0: your
- ARGM-MNR: strong
- ARG1: to repeal this Depression-era fossil
- rel: endorsement

Example 5 (Another arg 0 and 1): their formal endorsement of a merger with Daimler-Benz AG
- ARG0: their
- ARGM-MNR: formal
- ARG1: of a merger with Daimler-Benz AG
- rel: endorsement

Example 6 (Arg 0 only): The Russian President's endorsement
- ARG0: The Russian President's
- rel: endorsement

Example 7 (Slightly different form of arg 1): formal endorsement to Russia's white, red, and blue flag
- ARGM-MNR: formal
- ARG1: to Russia's white, red, and blue flag
- rel: endorsement

Example 8 (The rare arg 2): Ehud Barak won the endorsement of his Labor Party as its candidate for Prime Minister
- ARG1: of his Labor Party
- ARG2: as its candidate for Prime Minister
- rel: endorsement

### endorse-02 (sign on the backside)

- ARG0: signer
- ARG1: thing signed

Example 1 (typical): John endorsed his paycheck before depositing it.
- ARG0: John
- ARG1: his paycheck
- ARGM-TMP: before depositing it
- rel: endorsed

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

## question

### question-01 (ask a question (of a listener))

- ARG0: asker
- ARG1: question
- ARG2: entity asked, hearer

Example 1 (question-v: with hearer): Mary questioned John about his whereabouts last night.
- ARG0: Mary
- ARG2: John
- ARG1: about his whereabouts last night
- rel: questioned

Example 2 (question-n: Example with arg 2): I have a question for Mr. Laband
- ARG2: for Mr. Laband
- rel: question

Example 3 (question-n: arg 0 and 1): an attorney 's question about whether we would go after attorney's fees, and that is different from actually doing it ,althoughwe reserve that right
- ARG0: an attorney 's
- ARG1: about whether we would go after attorney 's fees , and that is different from actually doing it , although we reservethat right
- rel: question

Example 4 (question-n: arg 0 and 2): Your questions to some experts
- ARG0: Your
- ARG2: to some experts
- rel: questions

Example 5 (question-n: Lots of arg ms): Our web question of the week
- ARG0: Our
- ARGM-LOC: web
- ARGM-TMP: of the week
- rel: question

Example 6 (question-n: args 0 and 1): Your question about the New York Times
- ARG0: Your
- ARG1: about the New York Times
- rel: question

Example 7 (questioning-n: Arg0,2): Due in large part to Patrick's thoroughness, and his questioning of the plaintiff's doctors, the plaintiff was awardeddamages of only $3000.
- ARG0: his
- ARG2: of the plaintiff's doctors
- rel: questioning

Example 8 (rare meaning of questionable: can be questioned): The prisoner was finally questionable once the truth serum took effect.
- ARG2: The prisoner
- ARGM-TMP: finally
- ARGM-TMP: once the truth serum took effect
- rel: questionable

### question-02 (out-of-the-question)

- ARG1: thing that is out of the question
- ARG2: for whom/what

Example 1 (arg1): Sometimes repairs are out of the question .
- ARGM-TMP: Sometimes
- ARG1: repairs
- rel: are out of the question

Example 2 (arg1 and arg2): renewing military aid had been considered out of the question for civilians,
- ARG1: renewing military aid
- ARG2: for civilians
- rel: out of the question

### question-03 (have doubts, be dubious)

- ARG0: entity having doubts
- ARG1: dubious thing

Example 1 (question-v: transitive): Many analysts question management's credibility.
- ARG0: Many analysts
- ARG1: management's credibility
- rel: question

Example 2 (questionable-j: arg1): Prosecutors in Port St. Lucie, Fla., said the victim's identification of McIntyre as the suspect was questionable.
- ARG1: the victim's identification of McIntyre as the suspect
- rel: questionable

Example 3 (questionable-j: args0, 1): If the right was questionable by the legislature, the right of the legislature to question it could not be disputed;
- ARG1: the right
- ARG0: by the legistlature
- rel: questionable

## balance

### balance-01 (establish a balance)

- ARG0: balancer, agent
- ARG1: thing balanced
- ARG2: in comparison to

Example 1 (simple transitive): And even those who say some selective selling may be in order stress that [individuals]-3 need to be in the stock market *trace* to achieve their long-term investment objectives and to help *trace*-3 balance their other assets.
- ARG0: *trace*-3
- ARG1: their other assets
- rel: balance

Example 2 (ergative): To make the books balance, as is required by law, somebody invented a new budget line item that simply subtracted $45 billion.
- ARG1: the books
- ARGM-ADV: as is required by law
- rel: balance

Example 3 (ergative with comparator): [Stock-market investments]-1 also help *trace*-1 balance the other assets an individual owns, says John Blankenship Jr., president of the Institute of Certified Financial Planners.
- ARG1: *trace*-1
- ARG2: the other assets an individual owns
- rel: balance

Example 4 (passive with comparator): 2 . In seeking approval of a TRO, the prosecutor must articulate [any anticipated impact that forfeiture and the TRO would have on innocent third parties]-2, balanced *trace*-2 against the government's need to preserve the assets.
- ARG1: *trace*-2
- ARG2: against the government's need to preserve the assets
- rel: balanced

Example 5 (agent and thing balanced merged): John balanced on the peak of the roof.
- ARG0: John
- ARGM-LOC: on the peak of the roof
- rel: balanced

## mentioned (found as mention)

### mention-01 (say in passing)

- ARG0: speaker
- ARG1: utterance, entity being mentioned
- ARG2: hearer
- ARG3: secondary attribute of arg1

Example 1 (as phrase requires passive?): Among companies-1 mentioned *trace*-1 by analysts as possible counterbidders for Nekoosa are International Paper, Weyerhaeuser, Canadian Pacific Ltd. and MacMillan Bloedel Ltd.
- ARG1: *trace*
- ARG0: by analysts
- ARG3: as possible counterbidders for Nekoosa
- rel: mentioned

Example 2 (discourse function: not to mention): For a while, it looked like the deal -- *trace* not to mention the courtroom itself -- was on the verge of collapse.
- ARG0: *trace*
- ARGM-NEG: not
- ARG1: the courtroom itself
- rel: mention

Example 3 (same function, different parse): It is Mr. Paul's art venture, however, that has drawn the most attention from investors and regulators, *trace* not to mention galleries throughout the world.
- ARG0: *trace*
- ARGM-NEG: not
- ARG1: galleries throughout the world
- rel: mention

Example 4 (transitive): But the ad also mentions Sears's sales -- a topic that the retailer has avoided since switching to everyday pricing.
- ARGM-DIS: But
- ARG0: the ad
- ARGM-DIS: also
- ARG1: Sears's sales -- a topic that the retailer has avoided since switching to everyday pricing
- rel: mentions

Example 5 (with hearer and more traditional utterance): John mentioned to Mary that he was thinking of joining the Navy Seals--despite the fact that he can't swim.
- ARG0: John
- ARG2: to Mary
- ARG1: that he was thinking of joining the Navy Seals
- ARGM-ADV: despite the fact that he can't swim
- rel: mentioned

Example 6 (Arg 1): Host Ted Koppel introduced him as `` the media master of the Reagan Administration , '' with nary a mention of Mr. Deaver 'sconviction in 1987 on perjury charges .
- ARGM-NEG: nary
- ARG1: of Mr. Deaver 's conviction in 1987 on perjury charges
- rel: mention

Example 7 (args 0 and 1): His mention of the election was made in passing.
- ARG0: His
- ARG1: of the election
- rel: mention

## need

### need-01 (need, required, necessary)

- ARG0: needer
- ARG1: thing needed

Example 1 (need an NP): I need a flight to Seattle leaving from Baltimore making a stop inMinneapolis.
- ARG0: I
- ARG1: a flight to Seattle leaving from Baltimore making a stop in Minneapolis
- rel: need

Example 2 (need an infinitive): I-1 need *trace*-1 to have dinner served *trace*
- ARG0: I
- ARG1: *trace* to have dinner served *trace*
- rel: need

Example 3 (need both an NP and an S): Prosecutors-1 need court permission *trace*-1 to obtain the tax returns of an individual or a business.
- ARG0: Prosecutors
- ARG1: court permission
- ARGM-PRP: *trace* to obtain the tax returns of an individual or a business.
- rel: need

Example 4 (need an S): I need you to pay attention to the frames files!
- ARG0: I
- ARG1: you to pay attention to the frames files
- rel: need

Example 5 (autogen1): its production needs
- ARG0: its
- ARG1: production
- rel: needs

Example 6 (autogen2): the need to avoid those cuts
- ARG1: to avoid those cuts
- rel: need

Example 7 (physical object theme): the need for antibiotics
- ARG1: for antibiotics
- rel: need

Example 8 (with MNR): an urgent need to find a way to prevent pollution of their coastal waters
- ARGM-MNR: urgent
- ARG1: to find a way to prevent pollution of their coastal waters
- rel: need

Example 9 (CAU: because nobody needs an earthquake): Not everyone is convinced the state must raise new revenue to meet its earthquake needs
- ARG0: its
- ARGM-CAU: earthquake
- rel: needs

Example 10 (patient + proposition = arg1): his need for them to play better
- ARG0: his
- ARG1: for them to play better
- rel: need

Example 11 (arg1): Thus , it is just and needed for the US to impose such sanctions on Iran .
- ARGM-DIS: Thus
- ARG1: for the US to impose such sanctions on Iran
- rel: needed

## keep

### keep-01 (maintain possession)

- ARG0: Keeper
- ARG1: thing kept

Example 1 (plain old transitive): The Herald kept its old-time Hearst readership.
- ARG0: The Herald
- ARG1: its old-time Hearst readership
- rel: kept

Example 2 (nominal): The keeping of animals
- ARG1: of animals
- rel: kept

### keep-02 (aspectual)

- ARG0: causer of continued action
- ARG1: continued entity
- ARG2: continued state or action

Example 1 (subject control): John kept *trace* annotating.
- ARG0: John
- ARG2: *trace* annotating
- rel: kept

Example 2 (object control with sentential attribute): Ringers keep the bells sounding in the many belfries of East Anglia.
- ARG0: Ringers
- ARG1: the bells
- ARG2: sounding in the many belfries of East Anglia
- rel: keep

Example 3 (object control with Adj attribute): The captain kept the crew loyal.
- ARG0: The captain
- ARG1: the crew
- ARG2: loyal
- rel: kept

Example 4 (nominal use may be rare or ackward): The maintenance, the keeping going of the body
- ARG2: going of the body
- rel: keeping

Example 5 (subject control): John kept *trace* annotating.
- ARG0: John
- ARG1: *trace* annotating
- rel: kept

Example 6 (object control with sentential attribute): Ringers keep the bells sounding in the many belfries of East Anglia.
- ARG0: Ringers
- ARG1: the bells sounding in the many belfries of East Anglia
- rel: keep

Example 7 (object control with Adj attribute): The captain kept the crew loyal.
- ARG0: The captain
- ARG1: the crew loyal
- rel: kept

Example 8 (nominal use may be rare or ackward): The maintenance, the keeping going of the body
- ARG1: going of the body
- rel: keeping

### keep-03 (light verb (eventually to become replaced by real semantic frames - AMR))

- ARG0: agenty thing
- ARG1: noun
- ARG2: prepositional object

Example 1 (keep_pace): Newsweek keeps pace with its rival Time.
- ARG0: Newsweek
- ARG1: pace
- ARG2: with its rival Time
- rel: keeps

Example 2 (keep_track): The state keeps track of the achievement-test preparation booklets.
- ARG0: The state
- ARG1: track
- ARG2: of the achievement-test preparation booklets
- rel: keeps

### keep-04 (maintain some prepositional relationship)

- ARG0: causer of separation
- ARG1: one noun
- ARG2: other noun

Example 1 (be careful with 'from'!): Growers can't always keep the worm from the apple.
- ARG0: Growers
- ARGM-MOD: ca
- ARGM-NEG: n't
- ARGM-TMP: always
- ARG1: the worm
- ARG2: from the apple
- rel: keep

Example 2 (keep from: quasi-aspectual): Japanese demand has kept the U.S. currency from *trace* plunging.
- ARG0: Japanese demand
- ARG1: the U.S. currency
- ARG2: from *trace* plunging
- rel: kept

Example 3 (keep out): Britain kept light tanks out of the talks.
- ARG0: Britain
- ARG1: light tanks
- ARG2: out of the talks
- rel: kept

Example 4 (keep off): Keep your Foster Savings Institution off the federal budget deficit.
- ARG0: *trace*
- ARG1: your Foster Savings Institution
- ARG2: off the federal budget deficit
- rel: Keep

Example 5 (with attributive): The Fed kept inflation-fighting as its top priority.
- ARG0: The Fed
- ARG1: inflation-fighting
- ARG2: as its top priority
- rel: kept

### keep-06 (prepositional, comforming (only annotated by amr), prepositional (keeping with))

- ARG1: thing conforming
- ARG2: conformed-to

Example 1 (keep with): ... in *trace=nothing* keeping with the reputation of the company.
- ARG1: *trace*
- ARG2: with the reputation of the company.
- rel: keeping

Example 2 (Both args): There will be no flowers at the funeral, in keeping with the family's wishes.
- ARG1: There will be no flowers at the funeral
- ARG2: with the family's wishes.
- rel: keeping

### keep-LV (light verb)

- (no roles)

## free

### free-01 ((cause to be) available)

- ARG0: entity providing freedom, agent
- ARG1: entity made free
- ARG2: freed from
- ARG3: beneficiary/purpose

Example 1 (prepositional Arg3): But [the Oct. 17 temblor]-1 put a halt to much nonessential building , and heavy rains last week slowed the rest , [*]-1 freeing construction workers for earthquake repairs .
- ARG0: [*]
- ARG1: construction workers
- ARG3: for earthquake repairs
- rel: freeing

Example 2 (Arg3 as a VP): The New York Times Co. said [0] it reached a settlement with independent home delivery dealers in the metropolitan New York area that [*T*-1]will free the newspaper to expand home delivery circulation .
- ARG0: [*T*-1]
- ARGM-RCL: that -> a settlement
- ARGM-MOD: will
- ARG1: the newspaper
- ARG3: to expand home delivery circulation
- rel: free

Example 3 (with Arg2): Despite fears [0] the mine may be partially nationalized [*-2]by the new Namibian government following next month 's elections freeing the country from South African control , De Beers engineers are working [*-1] to extend the mine 's productive life for another 25 years , from the current estimate of 10 .
- ARG0: next month 's elections
- ARG1: the country
- ARG2: from South African control
- rel: freeing

### free-03 (costing nothing)

- ARG1: thing that costs nothing
- ARG2: "of charge" or similar

Example 1 (both args): The popcorn is free of charge when you purchase a ticket
- ARG1: The popcorn
- ARG2: of charge
- ARGM-TMP: when you purchase a ticket
- rel: free

### free-04 (unconstrained, unrestricted)

- ARG1: free entity
- ARG2: free from (former chains/burden)
- ARG3: resulting freedom (to do what)

Example 1 (args 1, 2): He is free from worry.
- ARG1: He
- ARG2: from worry
- rel: free

Example 2 (args 1, 3): She is free to read whatever she likes.
- ARG1: She
- ARG3: to read whatever she likes
- rel: free

## case

### case-01 (to put or enclose in a case)

- ARG0: packer
- ARG1: thing packed
- ARG2: case, location

Example 1 (storage): Mary cased the wine for easier storage.
- ARG0: Mary
- ARG1: the wine
- ARGM-PRP: for easier storage
- rel: cased

### case-02 (case the joint, observe covertly)

- ARG0: Thief or spy
- ARG1: Place being observed

Example 1 (Planting bugs): I put a small electric amplifier against the wall on the side *0*-2 I-1 wanted*PRO*-1 to case *T*-2.
- ARG0: *PRO*-1
- ARG1: *T*-2
- ARGM-RCL: *0*-2 -- the side
- rel: case

### case-03 (a formal argument/petition/big deal)

- ARG0: authority making a case
- ARG1: the argument
- ARG2: against whom

Example 1: In *PRO* making cases , the authorities frequently zero in on alleged misrepresentations made by the charities ' fund raisers .
- ARG0: *PRO*
- ARGM-LVB: making
- rel: cases

### case-04 (instance)

- ARG1: instance of, thing happenening or occuring, example

Example 1 (an instance of): a case of pot luck
- ARG1: of pot luck
- rel: case

Example 2 (One more): This is clearly a case of bad judgement.
- ARG1: of bad judgement
- rel: case

## likely

### likely-01 (probable)

- ARG1: likely event (may require concatenation

Example 1 (the arg): The banks that took care of their own loans wound up, long term, in a situation that-1 *PRO*-1 was likely to be better;
- ARG1: [*PRO*-1][to be better]
- rel: likely

Example 2 (with CXN): In our office we are more likely to eat store bought goodies then homemade unless we really know the patient . There is only 1 patient that I will accept homemade goodies from . -LRB- He and his wife make fudge and it s amazing -RRB-
- ARGM-LOC: In our office
- ARG1: [we][to eat store bough goodies]
- ARGM-CXN: [more][then homemade]
- rel: likely

## strain

### strain-01 (injure, put stress on, violent exertion)

- ARG0: agent, entity causing damage
- ARG1: patient, entity experiencing hurt/damage

Example 1 (physical hurt): The harder he tried to push them into large piles, the closer he-1 came to *trace*-1 breaking the rake and straining his back.
- ARG0: *trace*
- ARG1: his back
- rel: straining

Example 2 (metaphysical hurt): [The fight]-1 is putting a tight squeeze on profits of many, *trace*-1 threatening to drive the smallest ones out of business and straining relations between the national fast-food chains and their franchisees.
- ARG0: *trace*
- ARG1: relations between the national fast-food chains and their franchisees
- rel: straining

Example 3 (Defecation causes the straining, 'he' would be the experiencer): He developed difficulties with constipation and it was described as a significant amount of straining with defecation.
- ARG0: with defecation
- rel: straining

### strain-02 (separate solids from liquid)

- ARG0: separator, filter, agent
- ARG1: solids, thing removed
- ARG2: liquid, source, removed-from

Example 1 (solids and liquids still mixed): The idea behind the Egg King is pretty simple: *trace* put the eggs into a cylinder that contains perforated baskets, spin them at a high speed to break the shells and strain the edible part through the baskets.
- ARG0: *trace*
- ARG1: the edible part
- ARGM-DIR: through the baskets
- rel: strain

Example 2 (separated args): John strained the chunks out of his glass of expired milk before drinking it.
- ARG0: John
- ARG1: the chunks
- ARG2: out of his glass of expired milk
- ARGM-TMP: before drinking it
- rel: strained

### strain-03 (try hard)

- ARG0: Agent/Entity Trying
- ARG1: thing tried

Example 1 (work it, baby!): And, since the public has always been fascinated by gossip and voyeurism, reporters and editors will strain for creative angles to justify the inclusion of collateral facts about private lives including sexual activities and domestic relationships, activities of family members, and all matters about mental and physical health.
- ARGM-DIS: And
- ARGM-CAU: since the public has always been fascinated by gossip and voyeurism
- ARG0: reporters and editors
- ARGM-MOD: will
- ARG1: for creative angles
- ARGM-PRP: to justify the inclusion of collateral facts about private lives including sexual activities and domestic relationships, activities of family members, and all matters about mental and physical health
- rel: strain

### strain-04 (adjectival: hurting)

- ARG1: thing hurting
- ARG2: for what

Example 1 (one arg): Judge Kozinski found [the derivation]-1 entirely strained *trace*-1 and writes that ``for an academic to refer to himself as an intellectual gigolo is ... a devastating admission of professional dishonesty.''
- ARGM-ADV: entirely
- ARG1: *trace*
- rel: strained

Example 2 (both args): Intel makes semiconductors and Campeau-1 operates department-store chains and is strained *trace*-1 for cash.
- ARG1: *trace*-1
- ARG2: for cash
- rel: strained

## relations (found as relation)

### relation-03 (to know an entity, know/friendship)

- ARG0: first party (or all parties, if together)
- ARG1: type of relationship/ reason to know
- ARG2: second party/ relations with/ beneficiary

Example 1 (Example with arg 1 and 2): South Korea established diplomatic relations with Hungary in February 1989
- ARG1: diplomatic
- ARG2: with Hungary
- rel: relations

Example 2 (Example with arg 0 and 2): our relations with Japan
- ARG0: our
- ARG2: with Japan
- rel: relations

Example 3 (Example with all args): our excellent working relationship with the Drug Enforcement Administration and the Metropolitan Police Department
- ARG0: our
- ARGM-MNR: excellent
- ARG1: working
- ARG2: with the Drug Enforcement Administration and the Metropolitan Police Department
- rel: relationship

Example 4 (Example with args 1 and 2): a military relationship with Moscow
- ARG1: military
- ARG2: with Moscow
- rel: relationship

Example 5 (Example with args 0 and 2): His long and tortured relationship with Deep Throat
- ARG0: His
- ARGM-ADJ: long and tortured
- ARG2: with Deep Throat
- rel: relationship

Example 6 (All args): It jeopardized her professional relationship with her boss
- ARG0: Her
- ARG1: professional
- ARG2: with her boss
- rel: relationship

## policy

### policy-01 ((have/abide by) a predetermined course of action for governing, conduct)

- ARG0: entity holding the policy
- ARG1: the policy
- ARG2: policy regarding

Example 1 (policy-v): He found they policied 'black' areas of the city with more aggression and suspicision than 'white areas'
- ARG0: they
- ARG2: 'black' areas of the city
- ARGM-MNR: with more aggression and suspicision than 'white areas'
- rel: policied

Example 2 (policy-n): I think his foreign policy has been great
- ARG0: his
- ARG2: foreign
- rel: policy

Example 3 (have_policy-l): One company learned the hard way that it is not okay *PRO* to have a policy of firing people simply because they turn 62.
- ARG0: *PRO*
- ARGM-LVB: have
- ARG1: of firing people simply because they turn 62
- rel: policy

## fallen (found as fall)

### fall-01 (move downward)

- ARG1: Logical subject, patient, thing falling
- ARG2: EXT, amount fallen
- ARG3: start point
- ARG4: end point, end state of arg1
- ARGM: medium

Example 1 (all args): Profits fell 10% to $118 million from $130.6 million
- ARG1: Profits
- ARG2: 10%
- ARG4: to $118 million
- ARG3: from $130.6 million
- rel: fell

Example 2 (arg2 as manner): British government bonds fell sharply initially.
- ARG1: British government bonds
- ARG2: sharply
- ARGM-TMP: initialy
- rel: fell

Example 3 (temporal, with EXT): The average junk bond fell by 4.2% in October
- ARG1: The average junk bond
- ARG2: by 4.2%
- ARGM-TMP: in October
- rel: fell

Example 4 (non financial, fall into): They fell into oblivion after the 1929 crash.
- ARG1: They
- ARG4: into oblivion
- ARGM-TMP: after the 1929 crash
- rel: fell

Example 5 (Args 1, 2, 3): The Dow's falling 52 points to 12628 was an indication that the nation was moving closer to the possibility of a credit downgrade.
- ARG1: The Dow's
- ARG2: 52 points
- ARG3: to 12628
- rel: falling

Example 6 (autogen1): the stock market lurched into a 190-point free fall on Oct. 13
- ARG2: 190-point
- ARGM-MNR: free
- rel: fall

Example 7 (autogen2): the estimated 2 % fall in imports
- ARG2: 2 %
- ARG1: in imports
- rel: fall

Example 8 (motion arg1): These tree branches cushioned her fall
- ARG1: her
- rel: fall

Example 9 (non-numeric arg2): The dramatic rise and fall of US software stocks
- ARG2: dramatic
- ARG1: of US software stocks
- rel: fall

Example 10 (Watch out for .LVs!!!): In the '70s , the market took falls nine times in a row on Friday the you - know - what .
- ARGM: argM-PRX: falls (tag the NP parent node, sister to rel!)
- ARGM: argM-PRR: falls (tag the word itself)
- rel: took

### fall-04 (occur)

- ARG1: thing occurring
- ARG2: when/where

Example 1 (where they fall): The increase reflects spending on the S& L rescue as well as payroll and Social Security checks normally issued in October that were issued in September this year because Oct. 1 fell on a Sunday.
- ARG1: Oct. 1
- ARG2: on a Sunday
- rel: fell

Example 2 (Arg1, 2): The Fourth of July's falling on a Monday did not seem to dampen our neighbors' enthusiasm for illegal fireworks.
- ARG1: The Fourth of July's
- ARG2: on a Monday
- rel: falling

### fall-05 (be defeated)

- ARG1: loser
- ARG2: winner or instrument of destruction

Example 1 (pithy): The pithiest testimony to their domination of the just-concluded tournament came from Giants' manager Roger Craig after his team had fallen in Game Three to a five-home-run barrage that tied a 61-year-old Series record.
- ARG1: his team
- ARGM-LOC: in Game Three
- ARG2: to a five-home-run barrage that tied a 61-year-old Series record
- rel: fallen

Example 2 (Arg1,2): The Spartans' falling to the army of Xerxes is depicted in the film 300.
- ARG1: The Spartans'
- ARG2: to the army of Xerxes
- rel: falling

Example 3 (both args-- defeat): their fall to the Babylonians in 587 BC
- ARG1: their
- ARG2: to the Babylonians
- ARGM-TMP: in 587 BC
- rel: fall

Example 4 (both args-- sort of conversion/defeat): his fall to the dark side
- ARG1: his
- ARG2: to the dark side
- rel: fall

Example 5 (just loser): People in Baghdad celebrate the fall of a leader whose fate is unknown tonight
- ARG1: of a leader whose fate is unknown tonight
- rel: fall

### fall-07 (become)

- ARG1: Person undergoing change
- ARG2: End state

Example 1 (ah, romance!): When, however, Claudio's sister, Isabella, a novitiate in a convent, goes to Angelo to plead her brother's case, the obdurate ruler immediately falls in love with her and, in a supreme act of hypocrisy, demands that Isabella yield up her virtue to him in exchange for her brother's life.
- ARGM-TMP: When, however, Claudio's sister, Isabella, a novitiate in a convent, goes to Angelo to plead her brother's case
- ARG1: the obdurate ruler
- ARGM-TMP: immediately
- ARG2: in love
- ARGM-MNR: with her
- rel: falls

Example 2 (Falling Ill): For [a middle-aged person]-1, * losing one's job is just as traumatic as a car accident, *-1 falling ill, the death of a spouse, or a child running away from home.
- ARG1: *-1 --> a middle aged person
- ARG2: ill
- rel: falling

Example 3 (Become a delinquent): We were worried * that they might fall in with the wrong crowd after they got into junior high.
- ARG1: they
- ARGM-MOD: might
- ARG2: in
- ARGM-MNR: with the wrong crowd
- ARGM-TMP: after they got into junior high
- rel: fall

Example 4 (Arg1, 2): Steve's falling ill coincided with the release party for the third Harry Potter book.
- ARG1: Steve's
- ARG2: ill
- rel: falling

Example 5 (both args): their fall into a state of pauperism
- ARG1: their
- ARG2: into a state of pauperism
- rel: fall

Example 6 (another): their fall into silence
- ARG1: their
- ARG2: into silence
- rel: fall

### fall-10 (fall for a trick: be fooled by)

- ARG1: the fool
- ARG2: the trick

Example 1 (both args): Many people keep falling for this CON - GAME that lower taxes on the rich benefits everyone .
- ARG1: Many people
- ARG2: for this CON-GAME that lower taxes on the rich benefits everyone
- rel: falling

Example 2 (Both args): And many will fall for it and vote McCain , because he 's the great war hero and he will protect them .
- ARGM-DIS: And
- ARG1: many
- ARGM-MOD: will
- ARG2: for it
- ARGM-CAU: because he's the great war hero and he will protect them
- rel: fall

## line

### line-01 (provide a lining, accompany in line-like fashion)

- ARG0: agent only!
- ARG1: thing lined
- ARG2: instrument, lining proper

Example 1 (unstated lining): How many government programs and policies exist because they line the pockets of political insiders?
- ARG0: they
- ARG1: the pockets of political insiders
- rel: line

Example 2 (Enron stocks?): [Wall Street]-1 is just about ready *trace*-1 to line the bird cage with paper stocks.
- ARG0: *trace*
- ARG1: the bird cage
- ARG2: with paper stocks
- rel: line

Example 3 (stand in lines): Telephone poles lined the road .
- ARG2: Telephone poles
- ARG1: the road
- rel: lined

Example 4 (All args): Bert's lining of the basement's walls with lead was meant to convert it into a fallout shelter.
- ARG0: Bert's
- ARG1: of the basement's walls
- ARG2: with lead
- rel: lining

### line-03 (puts lines on)

- ARG0: putter of lines
- ARG1: thing with lines

Example 1 (adjectival): He looked at the lined face with vague interest ; ; he felt [0] he was noting it , as if it were something [0]he might think about [*T*-1] when he grew stronger [*T*-2] .
- ARG1: face
- rel: lined

## demonstrate

### demonstrate-01 (show (off))

- ARG0: demonstrator
- ARG1: thing demonstrated
- ARG2: watcher

Example 1 (transitive): The bank added that it believes the review will ``demonstrate that First Union is in compliance with the requirements of the Community Reinvestment Act.''
- ARG0: the review
- ARGM-MOD: will
- ARG1: that First Union is in compliance with the requirements of the Community Reinvestment Act
- rel: demonstrate

Example 2 (nonviolent political action): John demonstrated in front of City Hall.
- ARG0: John
- ARGM-LOC: in front of City Hall
- rel: demonstrated

## force

### force-01 (impelled action)

- ARG0: forcer
- ARG1: impelled agent
- ARG2: impelled action

Example 1 (sentential predicate): Commonwealth Edison said the ruling could force it to slash its 1989 earnings by $1.55 a share.
- ARG0: the ruling
- ARGM-MOD: could
- ARG1: it
- ARG2: to slash its 1989 earnings by $1.55 a share.
- rel: force

Example 2 (prepositional predicate): Low test scores force entire districts into wrenching, state-supervised interventions that can mean firings.
- ARG0: Low test scores
- ARG1: entire districts
- ARG2: into wrenching, state-supervised interventions that can mean firings.
- rel: force

Example 3 (preposition and passive): [Insurance agents]-1 have been forced *trace*-1 by their companies into *trace* becoming registered reps.
- ARG1: *trace*
- ARG0: by their companies
- ARG2: into *trace* becoming registered reps
- rel: forced

Example 4 (weird tertiary predication): [R. Gordon McGovern]-1 was forced *trace*-1 out as Campbell Soup's president and CEO.
- ARG1: *trace*
- ARG2: out
- ARGM-PRD: as Campbell Soup's president and CEO.
- rel: forced

Example 5 (and again): Arm troubles forced him back to the minors the next year.
- ARG0: Arm troubles
- ARG1: him
- ARG2: back
- ARGM-DIR: to the minors
- ARGM-TMP: the next year
- rel: forced

### force-02 (force a thing)

- ARG0: forcer
- ARG1: thing forced
- ARG2: benefactive, forced-on

Example 1 (typical): The new pact will force huge debt on the new firm.
- ARG0: The new pact
- ARGM-MOD: will
- ARG1: huge debt
- ARG2: on the new firm
- rel: force

Example 2 (nominal predicate): The scandal forced John's resignation.
- ARG0: The scandal
- ARG1: John's resignation
- rel: forced

### force-03 (put)

- ARG0: put-er, not putter
- ARG1: thing put
- ARG2: where put

Example 1 (abstract): So in terms of emotional ties we don't want *-1 to force each other into categories.
- ARG0: [ *-1] [ We]
- ARG1: each other
- ARG2: into categories
- rel: force

### force-04 (impinging with power upon)

- ARG0: forceful thing
- ARG1: entity impinged upon
- ARG2: type of force

Example 1: the Sun's gravitational force on the Earth is much stronger than the Moon's gravitational force on the Earth.

## wants (found as want)

### want-01 (want, desire)

- ARG0: Wanter
- ARG1: thing wanted
- ARG2: beneficiary
- ARG3: in-exchange-for
- ARG4: from

Example 1 (transitive): I want a flight from Ontario to Chicago
- ARG0: I
- ARG1: a flight from Ontario to Chicago
- rel: want

Example 2 (arg1 as infinitive): I actually want *trace* to go from Ontario to Chicago
- ARG0: I
- ARGM-ADV: actually
- ARG1: *trace* to go from Ontario to Chicago
- rel: want

Example 3 (arg1 as infinitival sentence): Czechoslovakia still wants the dam to be built.
- ARG0: Czechoslovakia
- ARGM-TMP: still
- ARG1: the dam to be built
- rel: wants

Example 4 (passive with extraction): he-1 was wanted *trace*-1 as a suspect in a double murder
- ARG1: *trace*-1 as a suspect in a double murder
- rel: wanted

## put

### put-01 (location)

- ARG0: putter
- ARG1: thing put
- ARG2: where put

Example 1 (heheh, he said 'onus'): Wilder has put the onus on Cole.
- ARG0: Wilder
- ARG1: the onus
- ARG2: on Cole
- rel: has put

Example 2 (put your money where your mouth is): Japanese companies often put their money behind odd projects.
- ARG0: Japanese companies
- ARGM-TMP: often
- ARG1: their money
- ARG2: behind odd projects
- rel: put

Example 3 (genie in the bottle): It's too late *trace* to put the genie back in the bottle.
- ARG0: *trace*
- ARG1: the genie
- ARGM-DIR: back
- ARG2: in the bottle
- rel: to put

### put-02 (say)

- ARG0: speaker
- ARG1: thing said

Example 1 (no utterance?): As Dorothy Arighi puts it, blah blah blah
- ARG0: Dorothy Arighi
- ARG1: it
- rel: puts

Example 2 (manner, not attribute): Let's put it bluntly.
- ARG0: us ('s)
- ARG1: it
- ARGM-MNR: bluntly
- rel: put

### put-03 (result, attributive)

- ARG0: putter
- ARG1: thing put
- ARG2: attribute of arg1

Example 1 (state to be): The pilots put the amount as high as $100 million.
- ARG0: The pilots
- ARG1: the amount
- ARG2: as high as $100 million
- rel: put

Example 2 (putting it all together): [That fund]-1 was put *trace*-1 together by Blackstone Group.
- ARG1: *trace*-1
- ARG2: together
- ARG0: by Blackstone Group
- rel: put

Example 3 (another example): Increasing labor costs , Mr. Tyszkiewicz argued , would only put the countries at a further disadvantage in competing in the barrier - free EC market planned for after 1992 .
- ARG0: Increasing labor costs
- ARGM-MOD: would
- ARGM-ADV: only
- ARG1: the countries
- ARG2: at a further disadvantage in competing in the barrier - free EC market planned for after 1992
- rel: put

## end

### end-01 (come to a close, cause to stop)

- ARG0: Agent/cause of ending
- ARG1: Thing ending
- ARG2: Subevent or thing that Arg1 ends with
- ARGM: point at which something ends

Example 1 (nominal arg1): [The courts]-1 want *trace*-1 to end rigid affirmative action programs.
- ARG0: *trace*
- ARG1: rigid affirmative action programs
- rel: to end

Example 2 (accusative, arg1 NP): Such a countermove could end Jaguar's hopes for independence.
- ARG0: Such a countermove
- ARG1: Jaguar's hopes for independence
- rel: end

Example 3 (ergative): The huge bronze bells...end, surprisingly, in the inverted position.
- ARG1: [The huge bronze bells...][in the inverted position]
- ARGM-DIS: surprisingly
- rel: end

Example 4 (with instrumental): The movie ends with sound.
- ARG1: The movie
- ARG2: with sound
- rel: ends

Example 5 (different kind of instrument): The first two GAF trials ended in mistrials earlier this year.
- ARG1: The first two GAF trials
- ARG2: in mistrials
- ARGM-TMP: earlier this year
- rel: ended

Example 6 (a weird usage): ...in the week ended Tuesday.
- ARG1: ...in the week
- ARGM-TMP: Tuesday
- rel: ended

Example 7 (autogen1): By Richterian standards , the show that the Oakland Athletics puton Friday and Saturday nights , in putting a mercifully swift endto the game 's Longest Short Series , rated somewhere between a10 and an 11 .
- ARGM-MNR: swift
- ARG1: to the game 's Longest Short Series
- rel: end

Example 8 (autogen2): he awaits his end in a prison cell
- ARG1: his
- rel: end

Example 9 (temporal end): the end of the year
- ARG1: of the year
- rel: end

Example 10 (all args): What I favor about Crichton's style is his ending the novel with a bibliography and a chapter with some ideas on correcting the issues he presented in the book.
- ARG0: his
- ARG1: the novel
- ARG2: with a bibliography and a chapter with some ideas on correcting the issues he presented in the book
- rel: ending

### end-02 (valuation at the end of a trading period, especially stocks)

- ARG1: thing closing
- ARG2: EXT, amount-changed-by
- ARG3: start point
- ARG4: end point

Example 1 (damn stock reports): Gilts ended about 3/8 point lower.
- ARG1: Gilts
- ARG2: about 3/8 point lower
- rel: ended

Example 2 (with manner): ...trading in Frankfurt ended higher.
- ARG1: ...trading in Frankfurt
- ARGM-MNR: higher
- rel: ended

Example 3 (two senses at once?): Japan's No. 111 4.6% bond due 1998 ended the day on brokers' screens at 95.11 [*-1] to yield 5.43%.
- ARG1: Japan's No. 111 4.6% bond due 1998
- ARGM-TMP: the day
- ARGM-LOC: on brokers' screens
- ARG4: at 95.11
- ARGM-ADV: [*-1] to yield 5.43%
- rel: ended

## regarded (found as regard)

### regard-01 (assign a label or attribute, careful thought or attention to something)

- ARG0: describer
- ARG1: thing described
- ARG2: secondary attribute, described-as

Example 1 (passivized): Until the collapse of this bid, [Mr. Wolf]-1 was regarded *trace*-1 as one of the nation's savviest airline executives after engineering turnarounds of Tiger International Inc. and Republic Airlines.
- ARGM-TMP: Until the collapse of this bid
- ARG1: *trace*
- ARG2: as one of the nation 's savviest airline executives
- ARGM-TMP: after engineering turnarounds of Tiger International Inc. and Republic Airlines
- rel: regarded

Example 2 (Args 0 & 1, within LVC): They did not take regard for countries' sovereignty.
- ARG0: They
- ARGM-NEG: not
- ARGM-LVB: take
- ARG1: for countries' sovereignty.
- rel: regard

Example 3 (Nominal, all args): Aristotle was explicit in his regard of phronesis as the most important of the three intellectual virtues.
- ARG0: his
- ARG1: of phronesis
- ARG2: as the most important of the three intellectual virtues.
- rel: regard

## attempts (found as attempt)

### attempt-01 (try)

- ARG0: Agent/Entity Trying
- ARG1: thing tried

Example 1 (sentential attempt): Mr. Nichol said he was ``extremely disappointed in the continuing deterioration of the company's operations while it attempted to conclude the reorganization during the past four months.''
- ARG0: it
- ARG1: to conclude the reorganization during the past four months
- rel: attempted

Example 2 (nominal attempt): Investment bankers following UAL agree that the strongest impetus for an eventual deal is that the pilots have been attempting a buy-out for more than two years, and aren't likely to stop, having come so close to success.
- ARG0: the pilots
- ARG1: a buy-out
- ARGM-TMP: for more than two years
- rel: attempting

Example 3 (both args): a management buy-out attempt
- ARG0: management
- ARG1: buy-out
- rel: attempt

Example 4 (autogen2): an attempt to speed deficit-reduction through Congress
- ARG1: to speed deficit-reduction through Congress
- rel: attempt

Example 5 (One more with both args): Congress' attempt to deny the president the funding necessary to execute certain of his duties and prerogatives specified in Article II of the Constitution.
- ARG0: Congress'
- ARG1: to deny the president the funding necessary to execute certain of his duties and prerogatives specified in Article II of the Constitution.
- rel: attempt

## be

### be-01 (copula)

- ARG1: topic
- ARG2: comment

Example 1 (poor John): John is an idiot.
- ARG1: John
- ARG2: an idiot
- rel: is

Example 2 (Arg1, 2): George's being a brat ruined the field trip for everybody.
- ARG1: George's
- ARG2: a brat
- rel: being

### be-02 (existential, existing)

- ARG1: thing that is

Example 1 (what it is, what it was, what it shall be): John doesn't think, therefore he isn't.
- ARG1: he
- ARGM-NEG: n't
- rel: is

Example 2 (with support): There's a foul odor in the air whenever John's around.
- ARG1: a foul odor in the air
- ARGM-TMP: whenever John's around
- rel: 's

Example 3 (Arg1, with adjectival): The existence of the hideous theatre, its very being, offended him so badly as to cause him nausea each day he passed the decrepit building.
- ARG1: its
- ARGM-ADJ: very
- rel: being

### be-03 (auxiliary)

- (no roles)

Example 1 (one of many): John is eating.

## source

### source-01 (obtain or use from a specific source)

- ARG0: obtainer
- ARG1: thing obtained
- ARG2: source

Example 1 (infinitive): ... they-2 continued *-2 to source raw materials and semi-finished goods from Taiwan.
- ARG0: *-1
- ARG1: raw materials and semi-finished goods
- ARG2: from Taiwan
- rel: source

Example 2 (adjectival): foreign-sourced news
- ARG2: foreign
- ARG1: news
- rel: sourced

### source-02 (provide, be a source of)

- ARG0: provider
- ARG1: thing provided
- ARG2: entity provided for (benefactive)

Example 1 (straight transitive): The company sources virtually of the necessary raw materials and parts on the mainland.
- ARG0: The company
- ARG1: virtually all of the necessary raw materials and parts
- ARG2-LOC: on the mainland
- rel: sources

## minor

### minor-01 (lesser)

- ARG1: lesser entity
- ARG2: greater entit

Example 1 (arg1): This is minor and is not causing her significant symptoms .
- ARG1: this
- rel: minor

### minor-02 (not of legal age)

- ARG1: minor

Example 1 (arg1): Colvii craved to be reponed to other defences, seeing he was minor at that time, and abroad.
- ARG1: he
- ARGM-TMP: at the time
- rel: minor

## troubles (found as trouble)

### trouble-01 (upset slightly)

- ARG0: cause of trouble
- ARG1: experiencer, one upset
- ARG2: instrument or manner (if arg0 also present)

Example 1 (trouble-v: just transitive): The volatility inherent in program trading troubled other traders, too.
- ARG0: The volatility inherent in program trading
- ARG1: other traders
- ARGM-DIS: too
- rel: troubled

Example 2 (troubled-j: with CXN): I 'm not sure she is as troubled by U.S. actions around the world as I am , but I think so .
- ARG1: she
- ARGM-CXN: [as] [as I am]
- ARG0: by U.S. actions around the world
- rel: troubled

### trouble-05 (exertion of effort)

- ARG0: agent, entity forcing the effort (rare)
- ARG1: entity trying, exherting
- ARG2: thing tried

Example 1 (saving the trouble): Save yourself the trouble of cooking tomorrow night!
- ARG1: yourself
- ARG2: of cooking
- ARGM-TMP: tomorrow night
- rel: trouble

Example 2 (mwe form): You must have had a pretty big reason to go to the trouble of tracking me down
- ARG1: You
- ARG1: of tracking me down
- rel: [go],[to],[trouble]

Example 3 (mwe form): like all the other laws the police do not take the trouble to enforce, it is a dead letter.
- ARG1: the police
- ARGM-NEG: not
- ARGM-LVB: take
- ARG2: to enforce
- rel: trouble

Example 4 (rare verbal form): Can I trouble you to pass me the sugar?
- ARGM-MOD: Can
- ARG0: I
- ARG1: I
- ARG2: to pass me the sugar?
- rel: trouble

## can

### can-01 (put into tins)

- ARG0: canner, agent
- ARG1: substance

Example 1 (passive): The agency won't allow mushrooms that [*T*-2] were canned [*-3]or packed in brine at any Chinese plant to enter the U.S. until ``satisfactory sanitation-control measures are implemented in China to prevent'' bacterial contamination.
- ARGM-RCL: that -> mushrooms
- ARG1: [*T*-2]
- ARGM-LOC: at any Chinese plant
- rel: canned

Example 2 (almost agentive): The outbreaks were traced to staphylococcus aureus, a type of bacteria that produces a toxin capable of surviving the high temperatures used in [*] canning vegetables.
- ARG0: [*]
- ARG1: vegetables
- rel: canning

### can-02 (fire (metphorical extension of 'throw away'))

- ARG0: employer
- ARG1: ex-employee (thing thrown away)
- ARG2: job

Example 1 (you get the picture): [John]-1 was canned *trace*-1 from his job at the weenie factory after making one too many sexual innuendoes.
- ARG1: *trace*-1
- ARG2: from his job at the weenie factory
- ARGM-TMP: after making one too many sexual innuendoes
- rel: canned

Example 2 (throw away): The American market is what matters -LRB- afterall , they took the american title of the book , not the original title -RRB- , so [all plans for a sequel]-1 were canned *-1.
- ARGM-ADV: so
- ARG1: *-1
- rel: canned

## scare

### scare-01 ((cause to) become afraid, afraid)

- ARG0: scary entity
- ARG1: scared entity
- ARG2: instrument (if separate from arg0)
- ARG3: intensifier, extent

Example 1 (scare-v: transitive): Such disclosures of big holdings often are used by raiders-1 [*trace*-1]-2 to try *trace*-2 to scare a company's managers.
- ARG0: *trace*-2
- ARG1: a company 's managers
- rel: scare

Example 2 (scare-v: with instrument): Mary scared John with her blood-red fingernails.
- ARG0: Mary
- ARG1: John
- ARG2: with her blood-red fingernails
- rel: scared

Example 3 (scare-v: instrumental subject): Mary's blood-red nails scared John.
- ARG0: Mary's blood-red nails
- ARG1: John
- rel: scared

Example 4 (scare-v: with intensifier): It won't take [much more]-1 *trace*-1 to ``scare the hell out of retail investors,'' he says.
- ARG0: *trace*-1
- ARG3: the hell
- ARG1: out of retail investors
- rel: scare

Example 5 (scare-v: another intensifier example): ``Small investors are absolutely dismayed that Wall Street is stacking the deck against them, and these wide swings are scaring them to death.
- ARG0: these wide swings
- ARG1: them
- ARG3: to death
- rel: scaring

Example 6 (scared-j): I am scared to die.
- ARG1: I
- ARG0: to die
- rel: scared

Example 7 (scare-n: just arg2): The scare over Alar , a growth regulator that makes apples redder and crunchier but may be carcinogenic , made consumers shy away from the Delicious , though they were less affected than the McIntosh .
- ARG2: over Alar, a growth regulator that makes apples redder and crunchier but may be carcinogenic
- rel: scare

Example 8 (scare-n: both args): Bud Noetzel is recovering from his scare of fluid in his lungs.
- ARG1: his
- ARG2: of fluid in his lungs
- rel: scare

Example 9 (scare-n: another with both args): Between her pregnancy scare and alleged breakup with Miles Austin, Kim could have a difficult transition when she returns home this week.
- ARG1: her
- ARG2: pregnancy
- rel: scare

### scare-02 (scare and make go away, or into motion)

- ARG0: intentional agent of scaring
- ARG1: scared entity
- ARG2: instrument
- ARG3: direction or resulting action

Example 1 (scare-v: scare off): [Their opposition]-1 helped *trace*-1 scare off some Japanese banks .
- ARG0: *trace*
- ARG3: off
- ARG1: some Japanese banks
- rel: scare

Example 2 (scare-v: scare away): Mr. DaPuzzo also complained that the sharp swings in stock prices lately is scaring away retail and foreign investors.
- ARG0: the sharp swings in stock prices
- ARGM-TMP: lately
- ARG3: away
- ARG1: retail and foreign investors
- rel: scaring

Example 3 (scare-v: with resulting action): Mr. Brady also agreed with senators' concerns about recent stock-market volatility, and said he realizes that the gyrations are scaring investors from investing in stocks.
- ARG0: the gyrations
- ARG1: investors
- ARG3: from investing in stocks
- rel: scaring

## just

### just-02 (ethically/morally fair)

- ARG0: agent of fair actions
- ARG1: fair actions
- ARG2: target of fair behavior, beneficiary

Example 1 (args 0, 2): He was just to them because he was just.
- ARG0: he
- ARG2: to them
- ARGM-CAU: because he was just
- rel: just

Example 2 (arg1, empty it): Thus , it is just and needed for the US to impose such sanctions on Iran .
- ARGM-DIS: Thus
- ARG1: for the US to impose such sanctions on Iran
- rel: just

## flying (found as fly)

### fly-01 (fly through the air, travel via air, fly in a flock)

- ARG0: pilot, agentive entity capable of flight (like a bird)
- ARG1: passenger, cargo
- ARG2: aircraft flown, flight number, steed, non-agentive thing in motion
- ARG3: type of flight plan, mission, cognate object (like 'a flight' or 'sorties')
- ARG4: airline

Example 1 (fly-v: unaccusative, traveller as subject): And some investors fault Mr. Spiegel's life style; he earns millions of dollars a year and flies around in Columbia's jet planes.
- ARG1: he
- ARGM-DIR: around
- ARG2: in Columbia's jet planes
- rel: flies

Example 2 (fly-v: transitive, pilot as subject): As a ``good-will measure,'' [the pilots]-1 had been working four extra hours a month and had agreed *trace*-1 to fly UAL's two new Boeing 747-400 aircraft.
- ARG0: *trace*-1
- ARG2: UAL's two new Boeing 747-400 aircraft
- rel: fly

Example 3 (fly-v: with destination): He will fly to San Francisco on the afternoon of the 20th to participate in another round of speeches .
- ARG1: He
- ARGM-MOD: will
- ARGM-GOL: to San Francisco
- ARGM-TMP: on the afternoon of the 20th
- ARGM-PRP: to participate in another round of talks
- rel: fly

Example 4 (fly-v: with recipient): John flew the paper airplane to Mary.
- ARG0: John
- ARG2: the paper airplane
- ARGM-GOL: to Mary
- rel: flew

Example 5 (fly-v: with employing airline, arg4): [All of the first group of pilots who went abroad to receive training for new fighter aircraft]-1 have left the military *trace*-1 to fly for civilian airlines
- ARG0: *trace*-1
- ARG4: for civilian airlines
- rel: to fly

Example 6 (fly-v: with arg3): Since this war began, something like 23,000 coalition sorties have been flown.
- ARGM-TMP: Since this war began
- ARG3: something like 23,000 coalition sorties
- rel: flown

Example 7 (flight-n: Within LVC): Just last week , for example , Trans World Airlines and Pan Am Corp. 's Pan American World Airways went so far as to offer cash rebates or gift checks of $ 200 to $ 1,000 to certain frequent-flier members making trans-Atlantic flights in business class or first class .
- ARG1: certain frequent-flier members
- ARGM-LVB: making
- ARGM-DIR: trans-Atlantic
- ARGM-MNR: in business class or first class.
- rel: flights

Example 8 (flight-n: pilot as subject, source and destination): This month we celebrate and remember Amelia Earhart's flight from Hawaii to California.
- ARG0: Amelia Earhart's
- ARGM-DIR: from Hawaii
- ARGM-GOL: to California
- rel: flight

Example 9 (flight-v: With DIR): The maximum count of birds flighting in at dusk was a remarkable 183.
- ARG0: birds
- ARGM-DIR: in
- ARGM-TMP: at dusk
- rel: flighting

Example 10 (fly-v): I never fly Frontier anymore.
- ARG1: I
- ARGM-NEG: never
- ARG4: Frontier
- ARGM-TMP: anymore
- rel: fly

Example 11 (fly-v): He flew on flight 664 to Albuquerque.
- ARG1: He
- ARG2: on flight 664
- ARGM-GOL: to Albuquerque
- rel: flew

Example 12 (For first/business/economy class, use :manner.): When I fly intercontental, I always fly first class.
- ARG1: I
- ARGM-TMP: always
- ARGM-MNR: first class
- rel: fly

### fly-02 (fly in the face of: flout)

- ARG0: flouter
- ARG1: "in the face of __"

Example 1 (ULA example): There I believe we would decidedly fly in the face of established case law .
- ARG0: we
- ARGM-MOD: would
- ARGM-ADV: decidedly
- ARG1: in the face of established case law
- rel: fly

### fly-03 (hit a fly ball, has strange past participle)

- ARG0: hitter
- ARG1: bases
- ARG2: where player moves to after hitting fly ball

Example 1 (Args 0 & 2): Kemp came closest to a home run in the fourth inning when he flied to very deep right field.
- ARG0: he
- ARG2: to very deep right field
- rel: flied

### fly-06 ((cause to) hold a spatial configuration in the air)

- ARG0: causal agent
- ARG1: thing suspended in the air

Example 1 (fly-v): He flew a flag above his house
- ARG0: He
- ARG1: a flag
- ARGM-LOC: above his house
- rel: flew

### fly-yy (insect (and other non-predicative senses))

- (no roles)

Example 1 (fruit fly): A large number of fruit flies hovered over the rotting bananas.

## over

### over-01 (finished, completed, no longer occuring)

- ARG1: thing that is no longer occurring

Example 1 (over-j: arg1): Angie I have the money and unsold tickets for Alex . Will you be at the games before it s over ?
- ARG1: it
- rel: over

Example 2 (over_with-m): Just get it over with.
- ARG1: it
- rel: [over][with]

### over-02 (be done dealing with a trauma, have come to terms with)

- ARG1: entity done dealing with a trauma
- ARG2: the trauma

Example 1 (over-j): It seems Bieber, 21, is still not over his first love.
- ARG1: Bieber, 21,
- ARGM-TMP: still
- ARGM-NEG: not
- ARG2: his first love
- rel: over

### over-03 (too much of something (overly))

- ARG1: too much of what?

Example 1 (overly): He is overly anxious.
- ARG1: anxious
- rel: overly

## planes (found as plan)

### plan-01 (expect)

- ARG0: planner
- ARG1: thing planned
- ARG2: grounds for planning
- ARG3: beneficiary

Example 1 (just transitive): They initially planned a transaction that included about $250m in equity
- ARG0: They
- ARGM-TMP: initially
- ARG1: a transaction that included about $250m in equity
- rel: planned

Example 2 (thing planned as infinitive): The group plans *trace=group* to put in even more money in equity
- ARG0: The group
- ARG1: to put in even more money in equity
- rel: plans

Example 3 (grounds as ON phrase): John plans his travels on the advice of gypsy fortune tellers.
- ARG0: John
- ARG1: his travels
- ARG2: on the advice of gypsy fortune tellers
- rel: plans

Example 4 (plan on): John is planning on *trace* going to the beach this summer.
- ARG0: John
- ARG1: on *trace* going to the beach this summer
- rel: is planning

Example 5 (plan for): John plans for every contingency.
- ARG0: John
- ARG1: for every contingency
- rel: plans

Example 6 (discourse usage): John graduated only fifteen years after entering graduate school, as *trace*-1 planned *trace*-1.
- ARG1: *trace*
- rel: planned

Example 7 (with beneficiary): Isn't it true that you were so worked up that framing Mr. Laff for this crime was [the least]-4 that you planned [*T*-4]for him?''
- ARG0: you
- ARG1: [*T*-4]
- ARG3: for him
- rel: planned

Example 8 (Within LVC): The market rebound Monday followed weekend assurances from Mr. Darman that the administration has other plans to win the cut , which is alive and well .
- ARG0: the administration
- ARGM-LVB: has
- ARGM-ADJ: other
- ARG1: to win the cut , which is alive and well .
- rel: plans

Example 9 (With beneficiary): We also rest peacefully on the fact that she is also His, and His plan for her is perfect
- ARG0: His
- ARG3: for her
- rel: plan

Example 10 (Args 0, 1, 2): The City Council Democrats unveiled their plan to redistrict the municipality based on 2010 U.S. Census numbers.
- ARG0: their
- ARG1: to redistrict the municipality
- ARG2: based on 2010 U.S. Census numbers.
- rel: plan

Example 11 (Within LVC): So %uh anyway we-1 're really doing our utmost PRO-1 to do some creative planning to reverse that trend for next year
- ARG0: PRO-1
- ARGM-LVB: do
- ARGM-MNR: creative
- ARGM-PRP: to reverse that trend for next year.
- rel: planning

Example 12 (Args 0 & 1): He has a flair for design and is exacting in his planning of our installations.
- ARG0: his
- ARG1: of our installations
- rel: planning

## Hawk (found as hawk)

### hawk-01 (try to attract buyers)

- ARG0: seller, salesperson
- ARG1: goods
- ARG2: (potential) buyer

Example 1 (one example): But Mr. Steidtmann predicts that healthy stores hawking mostly apparel could ring up gains of as much as 25% to 30%.
- ARG0: healthy stores
- ARG1: mostly apparel
- rel: hawking

### hawk-02 (clear one's throat)

- ARG0: hawker
- ARG1: mucus

Example 1 (ladylike behaviour): Mary hawked and spat.
- ARG0: Mary
- rel: hawked

Example 2 (Both args): Barney the Dinosaur hawked a loogie onto the city of Prague.
- ARG0: Barney the Dinosaur
- ARG1: a loogie
- ARGM-LOC: onto the city of Prague.
- rel: hawked

## erupted (found as erupt)

### erupt-01 ((cause to) spew forth, spewing forth)

- ARG1: thing erupting
- ARG2: substance spewing forth

Example 1 (straight unaccusative): On so-called Manic Monday, Oct. 16, stock prices plunged across Europe and trading problems erupted.
- ARGM-TMP: On so-called Manic Monday, Oct. 16,
- ARG1: trading problems
- rel: erupted

Example 2 (misplaced modifier): A bitter conflict with global implications has erupted between Nomura Securities Co. and Industrial Bank of Japan, two of the world's most powerful financial companies.
- ARG1: A bitter conflict with global implications
- ARGM-LOC: between Nomura Securities Co. and Industrial Bank of Japan, two of the world's most powerful financial companies
- rel: erupted

Example 3 (with substance): The Senate's public gallery was packed with Judge Hastings' supporters, who *trace* erupted into applause after he finished his argument.
- ARG1: *trace*
- ARGM-RCL: who -> Judge Hastings' supporters
- ARG2: into applause
- ARGM-TMP: after he finished his argument
- rel: erupted

Example 4 (Arg0): The eruption of Krakatoa began in May 1883 and culminated with the destruction of Krakatoa on 27 August 1883.
- ARG1: of Krakatoa
- rel: eruption

### erupt-02 (mode of speaking)

- ARG0: speaker
- ARG1: utterance
- ARG2: hearer

Example 1 (blow your top): And Mancuso himself is investigating at the top of his lungs: [``How the hell can you live with yourself?'']-1 he erupts *trace*-1 at a politician.
- ARG0: he
- ARG1: *trace*
- ARG2: at a politician
- rel: erupts

## sell

### sell-01 (commerce: seller, giving in exchange for money)

- ARG0: Seller
- ARG1: Thing Sold
- ARG2: Buyer
- ARG3: Price Paid
- ARG4: Benefactive

Example 1 (sell-v: intransitive): They-1 have *trace*-1 to sell when things look like they're falling.
- ARG0: *trace*-1
- ARGM-TMP: when things look like they're falling
- rel: sell

Example 2 (sell-v: Ergative): A painting by August Strindberg sold at auction in Stockholm.
- ARG1: A painting by August Strindberg
- ARGM-LOC: at auction
- ARGM-LOC: in Stockholm
- rel: sold

Example 3 (sell-v: basic transitive): Dead-eyed men selling four-year-old copies of Cosmopolitan
- ARG0: Dead-eyed men
- ARG1: four-year-old copies of Cosmopolitan
- rel: selling

Example 4 (sell-v: strange sellers): A more recent novel has sold more than 4 million copies.
- ARG1: A more recent novel
- ARGM-EXT: more than 4 million copies
- rel: sold

Example 5 (sell-v: ergative with price): Individual copies sell for $3.95
- ARG1: Individual copies
- ARG3: for $3.95
- rel: sell

Example 6 (sell-v: agentive with price): Al Brownstein sold it for $60 a bottle.
- ARG0: Al Brownstein
- ARG1: it
- ARG3: for $60 a bottle
- rel: sold

Example 7 (sell-v: semi-idiomatic): Day traders sell the company' stock short.
- ARG0: Day traders
- ARG1: the company's stock
- ARG3: short
- rel: sell

Example 8 (sell-v: with buyer): It will sell the ad time to its clients at a discount
- ARG0: It
- ARG1: the ad time
- ARG2: to its clients
- ARG3: at a discount
- rel: sell

Example 9 (sell-v: with benefactive): John sold his mother's house for her.
- ARG0: John
- ARG1: his mother's house
- ARG4: for her
- rel: sold

Example 10 (sale-n: Example with args 1, 2, and 3, but not 0 because of the interviening verb): it completed the sale of Phenix-Transmission Co. to BishopPipeline Co. , for $ 17 million in cash and notes
- ARG1: of Phenix-Transmission Co.
- ARG2: to Bishop Pipeline Co.
- ARG3: for $ 17 million in cash and notes
- rel: sale

Example 11 (sale-n: Example with args 0, 1, and 2): a Whitbread sale of brewing operations to Scottish& Newcastle
- ARG0: Whitbread
- ARG1: of brewing operations
- ARG2: to Scottish& Newcastle
- rel: sale

Example 12 (sale-n: Example with args 1 and 2): The measure allows the sale of food and medicine to Cuba.
- ARG1: of food and medicine
- ARG2: to Cuba
- rel: sale

Example 13 (sale-n: Example with args 0, 1, and tmp): Her sale of the stock the day before the price collapsed.
- ARG0: Her
- ARG1: of the stock
- ARGM-TMP: the day before the price collapsed
- rel: sale

Example 14 (selling-n: just arg1): The most volatile form of program trading is index arbitrage -- the rapid - fire , computer - guided buying and selling of stocks
- ARGM-MNR: rapid-fire
- ARGM-MNR: computer-guided
- ARG1: of stocks
- rel: selling

Example 15 (selling-n: arg0 and more argMs): Tokyo stocks closed easier , posting their first loss in six trading days , partly because of programmed index - linked selling by trust investment funds in the afternoon session .
- ARGM-PRD: programmed
- ARGM-MNR: index-linked
- ARG0: by trust investment funds
- ARGM-TMP: in the afternoon session
- rel: selling

Example 16 (selling-n: args 1 and 3): A "put option" allows the selling of the stock for a set price at a future date.
- ARG1: of the stock
- ARG3: for a set price
- ARGM-TMP: at a future date
- rel: selling

Example 17 (selling-n: arg2): Locals in that area are against selling of the house to a minority community family
- ARG1: of the house
- ARG2: to a minority community family
- rel: selling

Example 18 (selling-n: arg4): Thank you for all you did with the selling of the house for me.
- ARG1: of the house
- ARG4: for me
- rel: selling

### sell-06 (to convince somebody of something)

- ARG0: Convincer
- ARG1: Person being convinced or persuaded
- ARG2: Convinced of what

Example 1 (sold): The savviest investors are not yet sold on the rally.
- ARG1: The savviest investors
- ARG2: the rally
- rel: sold

## contrary

### contrary-01 (contrary)

- ARG1: contradictor, contrary thing
- ARG2: contradicted thing, contrary to what?

Example 1 (all args): Studying chemistry is contrary to reason.
- ARG1: Studying chemistry
- ARG2: to reason
- rel: contrary

## combined (found as combine)

### combine-01 (combine, mix, cause to combine, combine or mix together)

- ARG0: agent, mixer
- ARG1: ingredient one
- ARG2: ingredient two
- ARG3: end product

Example 1 (separate ingredients, and agent): The plan still calls for LIN to combine its cellular telephone properties with BellSouth's and to spin off its broadcasting operations.
- ARG0: LIN
- ARG1: its cellular telephone properties
- ARG2: with BellSouth's
- rel: combine

Example 2 (separate ingredients, passivized): [GMAC profits]-1 are combined *trace*-1 with earnings from the rest of GM's operations and attributed to the company's traditional common stock.
- ARG1: *trace*
- ARG2: with earnings from the rest of GM's operations
- rel: combined

Example 3 (ergative, one ingredient): Mr. Bryant and other analysts hope all those moves will combine to help Tandy's results improve in the important Christmas quarter.
- ARG1: all those moves
- ARGM-MOD: will
- ARGM-PNC: to help Tandy's results improve in the important Christmas quarter
- rel: combine

Example 4 (ergative, two ingredients): Sterling's firm tone, combined with a steady opening on Wall Street, also tempted some investors to come back to the market, dealers said.
- ARG1: Sterling 's firm tone
- ARG2: with a steady opening on Wall Street
- rel: combined

Example 5 (with end product): Further, he said, an internal reorganization *trace* *trace* to combine several divisions into the Information Technology Group is expected to affect fourth-quarter results by an undisclosed amount.
- ARG0: *trace*
- ARGM-RCL: *trace* -> an internal reorganization
- ARG1: several divisions
- ARG3: into the Information Technology Group
- rel: combine

Example 6: a conglomeration of regional lymph node metasteses
- ARG1: of regional lymph node metasteses
- rel: conglomeration

Example 7 (amass into power): His conglomeration of power
- ARG0: his
- ARG3: power
- rel: conglomeration

Example 8 (What to do if both ingredients are lumped together): The combination of traditional Taiwanese and contemporary factors
- ARG1: of traditional Taiwanese and contemporary factors
- rel: combination

Example 9 (Two ingredients treed in seperate PPs): The combination of solid loan growth with tight expense control
- ARG1: of solid loan growth
- ARG2: with tight expense control
- rel: combination

Example 10 (Three ingredients; one PP): some combination of drug, alcohol, and mental problems.
- ARG1: of drug, alcohol, and mental problems.
- rel: combination

Example 11 (Arg 0): the network's inabliity to match a Time-Warner combination
- ARG0: Time-Warner
- rel: combination

## profits (found as profit)

### profit-01 (make money from, wages)

- ARG0: entity making money
- ARG1: source
- ARG2: the profit itself, amount

Example 1 (profit-v: transitive, typical): ...protects against stocks being relentlessly beaten downward by those-1 seeking *trace*-1 to profit from lower prices.
- ARG0: *trace*
- ARG1: from lower prices
- rel: profit

Example 2 (profit-n: NP only): group net profit of $ 2.5 billion on revenue of $ 125.1 billion
- ARG0: group
- ARG2: of $ 2.5 billion
- ARG3: on revenue of $ 125.1 billion
- rel: profit

Example 3 (profit-n: With manner only): These investors are looking for a quick profit.
- ARGM-MNR: quick
- rel: profit

Example 4 (profit-n: preposition for source argument): George only made a twenty dollar profit each year on his crafts.
- ARG2: twenty dollar
- ARGM-TMP: each year
- ARG1: on his crafts
- rel: profit

Example 5 (profit-n: preposition for source argument): George only made a twenty dollar profit each year on his crafts.
- ARG0: George
- ARG2: [twenty dollar] [each year]
- ARG1: on his crafts
- rel: [made a] [profit]

Example 6 (profit-n: Metaphorical profit, with source only): I hope there is some profit in your seeing this play.
- ARG2: some
- ARG1: in your seeing this play
- rel: profit

Example 7 (profit-n: Source with "of" preposition): What's the profit of visiting the doctor if you won't take his advice.
- ARG1: of visiting the doctor
- rel: profit

## thank

### thank-01 (thank)

- ARG0: thanker
- ARG1: thanked
- ARG2: for what?

Example 1 (thank-v: nice easy transitive): ``We will support it, we will thank him, and we will augment it where appropriate,'' said Rep. Vic Fazio D., Calif.
- ARG0: we
- ARGM-MOD: will
- ARG1: him
- rel: thank

Example 2 (thank-v: with arg2): In 1986, Stamford officials thanked Mr. Hoelzer for taking care of the mural -- and demanded he return it as soon as possible.
- ARGM-TMP: In 1986
- ARG0: Stamford officials
- ARG1: Mr. Hoelzer
- ARG2: for taking care of the mural
- rel: thanked

Example 3 (thank-v: sentential arg2): ``*trace* Thank God we have some deal on the table,'' said Stewart Gilchrist, a director at Scottish Amicable Investment Managers, which intends to vote its roughly 1% stake in favor of the restructuring.
- ARG0: *trace*
- ARG1: God
- ARG2: we have some deal on the table
- rel: Thank

Example 4 (thank-v: Be VERY CAREFUL! Most args that seem like arg 1 are in VOC nodes. These MUST be discourse!): Thanks for spending time with us tonight doctor.
- ARG2: for spending time with us tonight
- ARGM-DIS: doctor.
- rel: Thanks

Example 5 (thank-v: Dis and and 2): Dr. Sanjay Gupto thanks for the update
- ARGM-DIS: Dr. Sanjay Gupto
- ARG2: for the update
- rel: thanks

## speaking (found as speak)

### speak-01 (speak, lecturing, talking)

- ARG0: talker
- ARG1: subject
- ARG2: hearer
- ARG3: language

Example 1 (speak-v: just hearer): He added that he had spoken with Mr. Laidig, whom he referred to as a friend, by telephone Monday evening.
- ARG0: he
- ARG2: with Mr. Laidig, whom he referred to as a friend,
- ARGM-MNR: by telephone
- ARGM-TMP: Monday evening
- rel: spoken

Example 2 (speak-v: subject and hearer): Mary spoke to John about his atrocious breath.
- ARG0: Mary
- ARG2: to John
- ARG1: about his atrocious breath
- rel: spoke

Example 3 (speak-v: just subject): John spoke at length about the dangers of breathing paint fumes.
- ARG0: John
- ARGM-TMP: at length
- ARG1: about the dangers of breathing paint fumes
- rel: spoke

Example 4 (speak-v: arg3): John speaks 15 languages.
- ARG0: John
- ARG3: 15 languages
- rel: speaks

Example 5 (speaking-n: args 0, 2): We need to stay in the presence of God until He has finished His speaking to us.
- ARG0: His
- ARG2: to us
- rel: speaking

Example 6 (speaking-n: args 0, 3): I was surprised by HIS SPEAKING German so fluently.
- ARG0: his
- ARG3: German
- ARGM-MNR: so fluently
- rel: speaking

Example 7 (speech-n: Example with args 0 and 1): his first major arms-control speech
- ARG0: his
- ARG1: arms-control
- rel: speech

Example 8 (speech-n: Example with speaker and group spoken to): Mr. Kemp's speech to the Mortgage Bankers Association
- ARG0: Mr. Kemp's
- ARG2: to the Mortgage Bankers Association
- rel: speech

Example 9 (speech-n: Arg 2 can seem like the name of a speech when it really is the audience): The Des Moines speech
- ARG2: Des Moines
- rel: speech

Example 10 (speech-n: All Args present. If you have a real speech name, then it is arg 1): The President's axis of evil speech before congress
- ARG0: The President's
- ARG1: axis of evil
- ARG2: before congress
- rel: speech
