# Uniform Meaning Representation (UMR) guidelines, local revised version

## Conventions of this revised version

This file is a local revision of the UMR 0.9 specification (August 8, 2022). The spellings follow the UMR 2.2
release data, and the points below were decided for this project; where an older passage disagrees with
them, they hold.

* Names: `:possessor`, `:modal-strength` with the values `full-affirmative`, `partial-affirmative`,
  `neutral-affirmative`, `neutral-negative`, `partial-negative`, `full-negative`, `unspecified`;
  `:refer-person`, `:refer-number` and `:aspect` with lower-case values; `:quote`; the constants `author`,
  `root`, `document-creation-time`, `past-reference`, `present-reference`, `future-reference`; `umr-unknown`
  for a questioned element.
* Temporal containment is always written `:contained`: `(A :contained B)` says that B lies inside A.
  `:contains` and `:includes` are not used.
* Part and whole: with the part as the parent the relation is `:part-of`, `(s / string :part-of (g / guitar))`;
  with the whole as the parent it is `:part`, `(g / guitar :part (s / string))`.
* Organizational roles are `have-org-role-92` and kinship or other personal relations `have-rel-role-92`
  (not -91).
* A measure word or classifier is always kept as `:unit`.
* A place is `:place` (not `:location`). A time is `:temporal`; `:time` is only the clock time inside a
  `date-entity`.
* `:cause` is what brings an event about (its cause); `:reason` is the motive or justification given for it.
* `:degree` is an intensifier or downtoner of a property (`very`, `somewhat`); `:extent` is how far or how much
  an event or state reaches (a measure or amount).
* `:modpred` is not used. An event under the scope of a modal or other complement-taking event is linked to it
  in the document-level modal dependency: `(s1w :unspecified s1v)`, or with the strength the modal event gives.
* `:subset-of` is written member (or subset) first: `(s2p :subset-of s1p)` says that s2p is one of, or a part
  of, s1p.
* A person can be `person` or `individual-person`, and a place name can have an AMR type (`city`, `state`,
  `country`) or a UMR type (`human-settlement`, `country-partition`): both are accepted.
* The examples carry no `:wiki`.
* Variables are written `s1x`: `s` and the sentence number, then the variable's letter.

## Table of Contents

* Part 1. Introduction: What is UMR and what does UMR annotation look like?
* Part 2. From AMR to UMR
    * Part 2-1. Introduction
    * Part 2-2. Introduction for field linguists
        * Part 2-2-1. Predicate-argument relations
        * Part 2-2-2. Multi-word expressions
        * Part 2-2-3. Abstract concepts
        * Part 2-2-4. Non-participant role relations
        * Part 2-2-5. Attributes
* Part 3. Sentence-Level Representation
    * Part 3-1. UMR Concepts
        * Part 3-1-1. Eventive concepts
            * Part 3-1-1-1. Processes in predication
            * Part 3-1-1-2. Processes in modification and reference
            * Part 3-1-1-3. States and entities
            * Part 3-1-1-4. Implicit events
        * Part 3-1-2. Named entities
        * Part 3-1-3. Concept-word mismatches
            * Part 3-1-3-1. Predicate and argument as one word
            * Part 3-1-3-2. Valency-changing operations
            * Part 3-1-3-3. TAM categories
            * Part 3-1-3-4. Associated Motion
            * Part 3-1-3-5. Light verb constructions
            * Part 3-1-3-6. Non-verbal clauses
            * Part 3-1-3-7. Multi-word concepts
            * Part 3-1-3-8. Miscellaneous constructions
        * Part 3-1-4. Word senses
        * Part 3-1-5. Scope for Quantification and negation
        * Part 3-1-6. Discourse-relations
    * Part 3-2. UMR relations
        * Part 3-2-1. Participant roles
            * Part 3-2-1-1. Stage 0
                * Part 3-2-1-1-1. Non-verbal clauses
                * Part 3-2-1-1-2. Valency alternations
            * Part 3-2-1-2. Stage 1
                * Part 3-2-1-2-1. Valency alternations
            * Part 3-2-1-3. Inverse participant roles
            * Part 3-2-1-4. Table of verb meanings
        * Part 3-2-2. Non-participant role UMR relations
            * Part 3-2-2-1. Temporal relations
            * Part 3-2-2-2. Modifiers
            * Part 3-2-2-3. Circumstantial temporals and locatives
            * Part 3-2-2-4. Named entities
            * Part 3-2-2-5. Quantification
            * Part 3-2-2-6. Other relations
    * Part 3-3. UMR attributes
        * Part 3-3-1. Aspect
            * Part 3-3-1-1. Event Nominals
            * Part 3-3-1-2. Habitual
            * Part 3-3-1-3. State
            * Part 3-3-1-4. Activity
            * Part 3-3-1-5. Endeavor and Performance
        * Part 3-3-2. Mode
        * Part 3-3-3. Polarity
        * Part 3-3-4. Quant
        * Part 3-3-5. Ref
        * Part 3-3-6. Degree
* Part 4. Document-Level Representation
    * Part 4-1. Coreference
        * Part 4-1-1. Entity coreference
        * Part 4-1-2. Event coreference
    * Part 4-2. Temporal Dependency
        * Part 4-2-1. Nodes in the temporal dependency
            * Part 4-2-1-1. Pre-defined metanodes
            * Part 4-2-1-2. Time expressions
        * Part 4-2-2. Temporal relations
            * Part 4-2-2-1. Choosing the right temporal relation
                * Part 4-2-2-1-1. Special cases
            * Part 4-2-2-2. Contained or Overlap
            * Part 4-2-2-3. Causally-related events
    * Part 4-3. Modal Dependency
        * Part 4-3-1. Stage 0
            * Part 4-3-1-1. modstr values
                * Part 4-3-1-1-1. Non-future events
                * Part 4-3-1-1-2. Evidential justification
                * Part 4-3-1-1-3. Future events and deontic modality
            * Part 4-3-1-2. Events under the scope of a modal event
            * Part 4-3-1-3. quot relation
            * Part 4-3-1-4. purpose relation
            * Part 4-3-1-5. condition relation
            * Part 4-3-1-6. Modal dependency structure
        * Part 4-3-2. English modals
* Part 5. Annotation Cheat Sheet
* Part 6. Integrated examples
* Part 7. Alphabetical Index of UMR Annotation Categories

## Part 1. Introduction: What is UMR and what does UMR annotation look like?

The **Uniform Meaning Representation** (UMR) project aims to design a meaning representation that facilitates
the computational interpretation of a text. UMR combines a **sentence-level** representation that is adapted
from **Abstract Meaning Representation** (AMR), which focuses on **predicate-argument structures**, **word senses**, **named entities**, **multi-word expressions**, **aspect**, and **quantification**, and a document-level representation that focuses on **coreference**, **temporal** and **modal** relations. We illustrate this representation with a short English document as in (1) - (9), and then describe in more detail each component of UMR in the next few sections. UMR is intended to be a cross-lingual annotation framework with a shared set of **abstract** concepts and relations.

Operationally, for both sentence-level and document-level annotation, we assume an annotation procedure in which a document is processed sentence by sentence. The sentence-level representation is annotated first, so that the document-level annotation can make reference to the concepts in the sentence-level representation.

Example 1 (1)
```
Snt1: Edmund Pope tasted freedom today for the first time in more than eight months.

(s1t / taste-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Edmund"
            :op2 "Pope"))
    :ARG1 (s1f / free-04
        :ARG1 s1p)
    :temporal (s1t2 / today)
    :ord (s1o / ordinal-entity
        :value 1
        :range (s1m / more-than
            :op1 (s1t3 / temporal-quantity
                :quant 8
                :unit (s1m2 / month))))
    :aspect performance
    :modal-strength full-affirmative)

(s1s0 / sentence
    :temporal ((document-creation-time :depends-on s1t2)
            (s1t2 :contained s1t))
    :modal (author :full-affirmative s1t))
```
The document-level representation includes a list of **temporal and modal dependencies**, as well as a list of **coreference relations**. In this first sentence, the first temporal relation is between *document-creation-time*, a constant that refers to the time when the document is created, and *today*, a concept that can only be correctly interpreted if we know the document-creation-time of the document. In this sense, we say that *today* depends on document-creation-time, hence the relation between them is *:depends-on*. We will define the set of temporal relations used in UMR in Part 4-2-2.  The second temporal relation is between *today* and *taste-01*, and we say here *taste-01* happened sometime *today* and therefore is _:contained_ in *today*.

The document-level representation also includes a list of modal dependencies. There is only one modal relation in this sentence, and it is between *taste-01* and *author*. Like document-creation-time, author is also a constant - it refers to the author of this text as a *conceiver*, or in other words, as the *source* of the modal judgment of certainty about the *taste-01* event, which is indicated by the *:full-affirmative* label.

Example 1 (2)
```
Snt2: Pope is the American businessman who was convicted last week on spying charges and sentenced to 20 years in a Russian prison.

(s1i / identity-91
     :ARG1 (s1p / person
        :name (s1n / name "op1 "Pope))
     :ARG2 (s1b / businessman
    :mod (s1n2 / nationality
       :name (s1n3 / name :op1 "America")))
    :ARG1-of (s1c / convict-01
       :ARG2 (s1c2 / charge-05
          :ARG1 s1b
          :ARG2 (s1s / spy-02
             :ARG0 s1b))
       :temporal (s1w / week
          :mod (s1l / last))
       :aspect performance
       :modal-strength full-affirmative)
    :ARG1-of (s1s2 / sentence-01
       :ARG2 (s1p2 / prison
          :mod (s1c3 / country
             :name (s1n4 / name :op1 "Russia))
          :duration (s1t / temporal-quantity
             :quant 20
         :unit (s1y / year)))
       :ARG3 s1s
       :aspect performance
       :modal-strength full-affirmative)
     :aspect state
     :modal-strength full-affirmative)

(s2 / sentence
    :temporal((document-creation-time :depends-on s2w)
(s2w :contained s2c)
(s2w :contained s2s2)
          (s2c :before s2s))
    :modal((author :full-affirmative s2i)
(author :full-affirmative s2c)
(author :full-affirmative NULL_CHARGER)
(NULL_CHARGER :full-affirmative s2c)
(s2c :unspecified s2s)
    :coref(s1p :same-entity s2p))
```
<!-- should annotate coreference for nominals? if so we need to annotate "the american businessman" (the question is really whether it needs to be in the doc graph in addition to the identity-91 predicate in the sent graph)-->

For this sentence, the temporal relations represent the fact that the *conviction* event and the *sentence* event both
happened *last week*, which itself depends on the document-creation-time for its temporal interpretation, and that the *sentence* event happened after the *conviction*. The modal dependencies indicate that from the author's perspective, the *conviction* event and the
*sentence* event definitely happened, and that *Pope* is certainly *the American businessman*. It introduces a *NULL_CHARGER* conceiver to indicate that the authority that charged Pope (which is not explicit in the text) presents the *spying* event as a certainty. The coreference annotation specifies that *Pope* in sentence 2 and *Edmund Pope* in sentence 1 are the same entity.

Example 1 (3)
```
Snt3: He denied any wrongdoing.
(s3d / deny-01
    :ARG0 (s3p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s3t / thing
        :ARG1-of (s3d2 / do-02
            :ARG0 s3p
            :ARG1-of (s3w / wrong-02)))
    :aspect performance
    :modal-strength full-affirmative)

(s3s0 / sentence
    :temporal ((document-creation-time :before s3d)
            (s3d :before s3d2))
    :modal ((author :full-affirmative s3d)
            (author :full-affirmative s3p)
            (s3p :full-negative s3d2)
            (s3d :unspecified s3d2))
    :coref (s2p :same-entity s3p))
```

For this sentence, the coreference annotation indicates that *he* is the same person as *Pope* mentioned in (2). Because there is no strict event coreference or subevent relation between *wrongdoing* and, for example, *spying* in  (2), this relation is left unannotated.

The temporal annotation indicates that Pope's denial took place before document creation time, and that any *wrongdoing* would have happened before this denial. When annotating temporal relations, we always need to pick a *reference time* with respect to which the temporal relation between the reference time and the event can be determined. In this case, it is not clear whether the *deny* event happened before or after the *conviction* and *sentence* events, so the reference time is determined to be the document creation time.

The modal relations indicate that the *deny* event definitely happened according to the author. The author presents themselves as having certainty about Pope's mental state at the time of the denial (annotated as a :full-affirmative relation from author to *Pope*), and the :full-negative relation indicates that *wrongdoing* did not happen according to Edmund Pope, based on the author's account.

Example 1 (4)
```
Snt4: Russian President Vladimir Putin pardoned him for health reasons.
(s4p / pardon-01
    :ARG0 (s4p2 / person
        :name (s4n / name
            :op1 "Vladimir"
            :op2 "Putin")
        :ARG1-of (s4h / have-org-role-92
            :ARG2 (s4c / country
                :name (s4n2 / name
                    :op1 "Russia"))
            :ARG3 (s4p3 / president)))
    :ARG1 (s4p4 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1-of (s4c2 / cause-01
        :ARG0 (s4r / reason
            :mod (s4h2 / health)))
    :aspect performance
    :modal-strength full-affirmative)

(s4s0 / sentence
    :temporal (s2s2 :after s4p)
    :modal (author :full-affirmative s4p)
    :coref (s3p :same-entity s4p4))
```

In the document-level representation for this sentence, the person that is pardoned by Putin is marked as coreferential with *he* in sentence 3 (and therefore *Edmund Pope*). In the temporal annotation, the *sentence-01* event is designated as the reference time of *pardon-01* - the latter happens after the former. In the modal annotation, *pardon-01* is annotated as certain from the point of view of the author.

Example 1 (5)
```
Snt5: Pope was flown to the U.S. military base at Ramstein, Germany.

(s5f / fly-01
    :ARG1 (s5p / person
        :name (s5n / name
            :op1 "Pope"))
    :goal (s5b / base
        :mod (s5m / military
            :mod (s5c / country
                :name (s5n2 / name
                    :op1 "U.S.")))
        :place (s5c2 / city
            :name (s5n3 / name
                :op1 "Ramstein")
            :place (s5c3 / country
                :name (s5n4 / name
                    :op1 "Germany"))))
    :aspect performance
    :modal-strength full-affirmative)

(s5s0 / sentence
    :temporal (s4p :after s5f)
    :modal (author :full-affirmative s5f)
    :coref (s4p4 :same-entity s5p))
```
In the document-level annotation of this sentence, *pardon-01* from (4) is chosen as the
reference time of the *fly-01* event, and it happened before the *fly-01* event. The author is certain that the *fly-01*
event happened, and *Pope* in this sentence is the same person as *him* in the previous one.

Example 1 (6)
```
Snt6: He will spend the next several days at the medical center there before he returns home with his wife Sherry

(s1s / spend-02
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1t / temporal-quantity
        :quant (s1s2 / several)
        :unit (s1d / day
            :mod (s1n / next)))
    :temporal (s1b / before
        :op2 (s1r / return-01
            :ARG1 s1p
            :ARG4 (s1h / home)
            :companion (s1p2 / person
                :name (s1n2 / name
                    :op1 "Sherry")
                :ARG1-of (s1h2 / have-role-91
                    :ARG2 s1p
                    :ARG3 (s1w / wife)))
            :aspect performance
            :modal-strength full-affirmative))
    :place (s1c / center
        :mod (s1m / medical)
        :place (s1t2 / there))
    :aspect state
    :modal-strength full-affirmative)

(s6 / sentence
  :temporal((document-creation-time :after s6s)
            (s6s :after s6r))
  :modal((author :full-affirmative s6s)
         (author :full-affirmative s6r))
  :coref((s5p :same-entity s6p)
         (s5b :same-entity s6t2))
```
In the temporal annotation of this sentence, the document-creation-time is chosen as the reference time for *spend-02*, which is in turn the reference time for *return-01* - *spending time at the medical center* will happen after the document-creation-time, and *returning home* will happen later still. In the modality annotation, both *spend-02* and and *return-01* are presented by the author as certainly happening - or at least as certain as one can be about future events. In the coreference annotation, *he* is considered to be the same as the *person* whose name is Pope in (5), and *there* is the same location as the town of *Ramstein, Germany* in the preceding sentence.

Example 1 (7)
```
Snt7: Pope was in remission from a rare form of bone cancer when he was arrested in Russia.

(s7h / have-mod-91
    :ARG1 (s7p / person
        :name (s7n / name
            :op1 "Pope"))
    :ARG2 (s7r / remission-02
        :ARG1 (s7d / disease
            :name (s7n2 / name
                :op1 "bone"
                :op2 "cancer")
            :ARG1-of (s7r2 / rare-02))
        :temporal (s7a / arrest-01
            :ARG1 s7p
            :place (s7c / country
                :name (s7n3 / name
                    :op1 "Russia")))
        :aspect performance
        :modal-strength full-affirmative)
    :aspect state
    :modal-strength full-affirmative)

(s7s0 / sentence
    :temporal ((s2c :before s7a)
            (s7a :overlap s7h))
    :modal ((author :full-affirmative s7h)
            (author :full-affirmative s7a))
    :coref (s6p :same-entity s7p))
```
For (7), the state of being in *remission-02* held simultaneously with the *arrest-01* event, and the *arrest-01* event happended before the *convict-01* event from sentence 2. According to the author, both *arrest-01* and *be in remission* happened. Once again, *Pope* is the same entity as *he* in the previous sentence.

Example 1 (8)
```
Snt8: Doctors will examine him for signs that the cancer may have come back while he was awaiting trial in a Russian jail.

 (s8e / examine-01
       :ARG0 (s8d / doctor
          :refer-number plural)
       :ARG1 (s8p / person
          :refer-person 3rd
      :refer-number singular)
       :ARG2 (s8s / signal-07
          :ARG1 (s8c / come-01
         :ARG1 (s8d2 / disease
            :name (s8n / name :op1 "cancer))
         :direction (s8b / back)
         :temporal (s8a / await-01
            :ARG1 s8p
        :ARG2 (s8t / try-02
           :ARG1 s8p
           :aspect process)
        :place (s8j / jail
           :mod (s8c2 / country :wiki "Russia
              :name (s8n2 / name :op1 "Russia")))
        :aspect state
        :modal-strength full-affirmative)
         :aspect performance
         :modal-strength neutral-affirmative)
      :ARG2 s8d)
    :aspect endeavor
    :modal-strength full-affirmative)

(s8s0 / sentence
    :temporal ((document-creation-time :after s8e)
            (s2c :before s8a)
            (s8a :overlap s8c))
    :modal ((author :full-affirmative s8e)
            (author :neutral-affirmative s8c)
            (author :full-affirmative s8a))
    :coref (s7p :same-entity s8p))
```

The *examine-01* event will happen after the document-creation-time. The *await-01* event happened before the *conviction* event mentioned earlier in the text, and the potential return of the cancer temporally overlaps with this *await-01* event. According to the author, the *examine-01* event will certainly happen, and the *await-01* event certainly happened as well. The author is uncertain about whether the cancer has come back, indicated with a *neutral-affirmative* epistemic strength link. *He* is annotated as being the same person as Edmund Pope.

Example 1 (9)
```
Snt9:  A spokeswoman said that Pope was suffering from malnutrition and high blood pressure.
(s9s / say-01
    :ARG0 (s9p / person
        :ARG1-of (s9h / have-org-role-92
            :ARG3 (s9s2 / spokeswoman))
        :refer-number singular)
    :ARG1 (s9s3 / suffer-01
        :ARG0 (s9p2 / person
            :name (s9n / name
                :op1 "Pope"))
        :ARG1 (s9a / and
            :op1 (s9m / malnourished-01
                :ARG1 s9p2)
            :op2 (s9p3 / pressure-01
                :ARG1 (s9b / blood
                    :part-of s9p2)
                :ARG1-of (s9h2 / high-02)))
        :aspect state
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)

(s9s0 / sentence
    :temporal ((document-creation-time :before s9s)
            (s9s :overlap s9s3))
    :modal ((author :full-affirmative s9s)
            (author :full-affirmative s9p)
            (s9p :full-affirmative s9s3))
    :coref (s8p :same-entity s9p2))
```
The document-level representation indicates the *say-01* event happened before Document Creation Time, and that the *suffer-01* event overlaps temporally with the *say-01* event. The modality annotation indicates that from the author's perspective, the *say-01* event definitely happened, and the author indicates that the *suffer-01* event happened according to the spokesperson. Once again, coreference is indicated between different mentions of *Pope*.

## Part 2. From AMR to UMR

### Part 2-1. Introduction

UMR inherits the sentence-level representation of AMR, with modifications. Like AMR, the sentence-level representation of UMR is a single-rooted, directed, node- and edge-labeled graph, as in (1). The nodes of this graph are UMR concepts, while edges represent UMR relations.

Example 2 (1)
```
Snt1: Edmund Pope tasted freedom today for the first time in more than eight months.

(s1t / taste-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Edmund"
            :op2 "Pope"))
    :ARG1 (s1f / free-04
        :ARG1 s1p)
    :temporal (s1t2 / today)
    :ord (s1o / ordinal-entity
        :value 1
        :range (s1m / more-than
            :op1 (s1t3 / temporal-quantity
                :quant 8
                :unit (s1m2 / month))))
    :aspect performance
    :modal-strength full-affirmative)
```

**UMR concepts:** There are a number of ways that UMR concepts are created based on the input sentence:

* Lemmas: Some UMR concepts are simply lemmas. For example, `today` in the example above is a lemma, which happens to have the same form as the word token itself.
* Word senses: When definitions of word senses are available for a language in the form of a lexicon, a concept can also be a sense-disambiguated word. For instance, `taste-01` in the example above refers to the first sense of the word *taste* in the English PropBank.
* Concepts formed out of multi-word expressions: `more-than` is a concept that is formed by concatenating multiple words in a sentence. Exactly when
mulit-word concepts should be formed will be determined on a language-by-language basis.
* Named entity types. Named entities in a sentence are annotated with a named entity type concept (e.g., `person`) and a `name` concept. The actual names are annotated as a constant (`Edmund` and `Pope`).
* Abstract concepts. In some cases a concept can be inferred from the context. In this case, the concept does not correspond to any particular word in the sentence, hence it is an *abstract* concept (e.g. `ordinal-entity`).

**UMR relations:** There are also a number of ways relations between concepts are created:

* Participant roles: The participant roles characterize the role that a participant plays with respect to the predicate. They can be predicate-specific if a set of *frame files* are defined for a language, where a set of core participant roles are defined for each (sense of the) predicate. For example, `:ARG0` and `:ARG1` are participant roles defined for `taste-01`. For languages that do not have *frame files*, the participant roles are generic (e.g., `Actor`, `Experiencer`), and they are described in Part 3-2-1.
* Semantic relations: Other UMR relations include `:temporal`, `:ord`, `:range` etc. that are not normally characterized as participant roles. A complete list of such relations can be found in Part 3-2-2.

**UMR attributes:** UMR currently has seven attribute types:

* Aspect: Aspect is annotated for eventive concepts only (see
Part 3-1-1 on event identification). Possible Aspect values at the default level of granularity include `Activity`, `Habitual`, `State`, `Endeavor`, `Performance`. A complete list of aspect values with explanations and examples can be found in Part 3-3-1.
* Polarity: Polarity is only annotated for negative polarity as indicated by a negation marker or an affix indicating negation (see Part 3-3-3).
* Mode: The mode attribute is typically for the main predicate of a sentence. Its values include `imperative`, `expressive`, and `interrogative` (see Part 3-3-2).
* Quantity: The value of a `:quant` attribute is a numerical number (see Part 3-3-4).
* Value: The value of a `:value` attribute is a numerical number (see Part 3-2-2).
* Degree: The value of a `:degree` attribute is either `intensifier`, `downtoner`, or `equal` (see Part 3-3-6).
* Reference: The value of a `:refer-person` or `:refer-number` attribute is a either a person feature (e.g. `1st`, `2nd`, `3rd`) or a number feature (e.g. `Singular`, `Dual`, `Paucal`, `Plural`) used to represent reference. These features are used to represent pronouns, verbal cross-referencing, implicit arguments, and overt nominal number (see Part 3-3-5).

**UMR modal values:** UMR currently has three modal relations that are annotated at the sentence level, even though the final modal dependency structure functions at the document level:

* Modstr: Indicates the epistemic strength relation (degree of confidence/certainty) between a conceiver and an event or between a conceiver and an embedded conceiver.
* Modpred: Indicates the relation between a modal complement-taking predicate and its complement
* Quot: Indicates the relation between a speech predicate and its complement

**Differences between AMR and UMR**

UMR differs from AMR in a number of ways:

* UMR has a document-level representation that represents *coreference*, *temporal dependencies*, and *modal dependencies*.

* As a result, some sentence-level AMR concepts  are now represented at the document level. This applies to concepts for modality (e.g., `possible-01`, `obligate-01`) - see the AMR and the UMR for *The boy can go* in (2a) and (2b), respectively.

Example 2 (2a)

```
(s1p / possible-01
    :ARG0 (s1g / go-01
        :ARG0 (s1b / boy
            :refer-number singular)))
```
Example 2 (2b)
```
(s0g / go-01
    :ARG0 (s0b / boy
        :refer-number singular)
    :aspect state
    :modal-strength neutral-affirmative)

(s0s0 / sentence
    :modal (author :neutral-affirmative s0g))
```

* UMR adds a *scope* concept to represent the relative scope of quantifiers and negations. See Part-3-1-5 for details.
* UMR allows the use of non-predicate-specific participant roles for languages that do not have *frame files* with lexicalized argument structure information. See Part 3-2-1 for details. To further accomodate languages with less advanced grammatical description or resource availability, other annotation domains are structured as *lattices*.
* UMR adds *aspect* and *ref* attributes to the representation. See Part 3-3-1 and Part 3-3-5 for details.

### Part 2-2. Introduction for field linguists

The annotation scheme detailed in these guidelines, Uniform Meaning
Representation (UMR), intends to allow for annotation of temporal,
aspectual, modal, and quantification semantics, as well as semantic
argument structure, in a cross-linguistically motivated and portable
way. Some semantic domains, specifically coreference, temporal
relations, and modal relations, are annotated in a document-level
structure. Other domains, such as predicate-argument structure, aspect,
and quantification, are annotated in a sentence-level structure.

This UMR sentence-level structure builds on a sentence-level representation
that is adapted from the Abstract Meaning Representation (AMR)
annotation scheme, which was originally designed for the annotation of
English, and has since been extended to Chinese and Arabic, amongst
others. This means that, before getting to the cross-linguistically
motivated parts of UMR annotation, annotators for new languages need to
do some AMR-based annotation of their texts, specifically regarding
predicate-argument structure. This section of the guidelines discusses
which parts of AMR annotation are required before the UMR annotation
procedure detailed in the rest of these guidelines can be applied.

The core of AMR is that it represents natural language sentences as
single-rooted, directed, node-labelled and edge-labelled graphs.
Semantic concepts expressed in such natural language sentences are
represented in two ways. Some of them are represented as *concepts*,
which means that they function as nodes in the AMR graphs. This is the
case for predicates and (heads of) referring expressions, for instance.
Other meanings are represented as *relations* in AMR, which means that
they function as edges in the AMR graphs. This is the case for argument
roles and a range of different modification relations, amongst others.

#### Part 2-2-1. Predicate-argument relations

The annotation of predicate-argument structure is the main domain in
which AMR annotation conventions are inherited. First and foremost,
predicated events are represented in the graph as nodes, as are
predicated states, events that are being referred to or used as
modifiers, and various other kinds of "non-verbal predicates" (see
Part 3-1-1 on event identification). For annotation of English texts,
sense-disambiguated predicates from PropBank, such as the one presented below for English _taste_ are used to label predicate
nodes. Since for most languages, no equivalent of PropBank is available, the UMR annotation tool contains a lexicon-building functionality where annotators can either upload a lexicon created in FLEx to support them in their annotation effort, or they can start a lexicon with argument structure information from scratch and essentially build PropBank-style frame files on the fly.

```
Roleset id: taste.01, use one's tastebuds, active perception of flavor.
Roles:
    ARG0: taster
    ARG1: food

Roleset id: taste.02, possess a flavor.
Roles
    ARG1: thing with flavor
    ARG2: description of flavor
```

The semantic arguments of such predicate nodes are represented in the
graph as daughter nodes of the relevant predicate. The edge that connects parent and daughter
nodes in these structures carries a participant role label. For English,
these participant role labels are predicate-specific, numbered argument
roles drawn once again from PropBank. For languages without comparable
lexical databases, we use an inventory of general argument roles such as
`:actor`, `:undergoer`, and `:theme`. In the long run, annotations can be used to
create language-specific and predicate-specific frame files detailing
argument structure of individual predicates, and the predicate-specific
argument roles can be linked to predicate-general participant roles for
commensurability (see Part 3-2-1 on argument structure annotation).
This AMR-based predicate-argument annotation is shown in its most basic
form in (1) from Sanapaná (Enlhet-Enenlhet) below.

Example 2-2-1 (1)
```
ap-hle-am-ke'       nenhlet
2/3M-travel-TI-DECL person
'A man travelled.'

(s1e / enhleama-00
    :actor (s1n / nenhlet
        :refer-number singular)
    :aspect endeavor
    :modal-strength full-affirmative)
Glosses: enhleama-00 = 'travel'; nenhlet = 'person'
(s1t / travel-01
    :ARG0 (s1m / man
        :refer-number singular)
    :aspect endeavor
    :modal-strength full-affirmative)
```

The basic, AMR-inspired graph structures for simple sentences in
languages like English and Sanapaná then look very similar, as shown
above: they both have a predicate corresponding to the main event of the
sentence as the top of the graph - the English one has a reference to a
numbered PropBank frame file for the predicate *travel*, the Sanapaná
one just has the citation form of the *travel*-verb with a `-00` suffix.
In both cases, the semantic argument 'person/man' is a daughter of this
predicate, linked with a participant role edge. In English, this is a
numbered participant role taken from this same PropBank frame file,
while in Sanapaná it is a predicate-general participant role. In both languages, the participant has a :refer-number singular attribute.

AMR and UMR concepts are underspecified for morphosyntactic
representation: the same concept (for example, `travel-01`) can be used
to annotate a verb (as seen above), a noun (e.g. *his travels* in (2), or any other relevant part of speech conveying the same semantics. Part 3-1-1 discusses how AMR and UMR deal with the
information-packaging differences which are conveyed by packaging such
content in different parts of speech.

Example 2-2-1 (2)
```
I heard about his travels.
(s1h / hear-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1t / travel-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :aspect process
        :modal-strength full-affirmative)
    :aspect state
    :modal-strength full-affirmative)
```

#### Part 2-2-2. Multi-word expressions

UMR inherits annotation conventions from AMR in domains other than
predicate-argument structure. With regard to concepts, UMR treats
multi-word expressions in essentially the same way as AMR. Specifically,
it allows annotators to select multiple words in a sentence and annotate
them as a single concept. This is necessary, for example, to annotate
idiomatic expressions which cannot be semantically decomposed
felicitously. In (1) from Sanapaná, for instance,
*elvongkeskama tayep* is a multi-word expression which literally and
compositionally means 'cause (someone) to be just across', but its
idiomatic meaning is 'rescue'. The two words are therefore annotated
together as a multi-word expression with a single meaning. Some further
specifications are made in UMR with regards to the annotation of
multi-word expressions such as serial verb constructions and
periphrastic TAM constructions. More information about the annotation of
multi-word expressions is given throughout Part 3-1-3, and
specifically in section Part 3-1-3-6.

Example 2-2-2 (1)
```
apk-el-vongk-es-akp-e'      tayep   ayko<'o>k
2/3M-DSTR-be.just-CAUS-PAS-DECL across  child<PL>
'The children were rescued.'
(s1e / elvongkeskama-tayep-00
    :undergoer (s1a / ayko'ok 'child'
        :refer-number plural)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: elvongkeskama-tayep-00 = 'rescue'
```

#### Part 2-2-3. Abstract concepts

AMR conventions are also largely inherited with regards to the use of
abstract concepts. Abstract concepts are concepts that are identified
and annotated even though they do not (consistently) correspond to any
overt word in the sentence. There are typically two main reasons for
which AMR and UMR use abstract concepts. Firstly, there are concepts
where AMR and UMR use abstract concepts rather than language-specific
concepts corresponding to specific words with the goal of making
annotations cross-linguistically comparable. For example, even though
the Sanapaná thetic possession construction in (1) makes use of a verb
that literally means *exist*, an abstract concept predicate node
`have-91` is introduced rather than a language specific `enyetnema-00`
concept. This way, possessive constructions across the world's languages
can be annotated in consistent and comparable ways regardless of the
morphosyntactic strategies they use (see Part 3-1-3-6 for more
information on such "non-verbal clauses").

Example 2-2-3 (1)
```
an-yetn-eye'        ko'o    vakka-hak   ah-angkok
2/3F-exist-DECL     1SG:PRO cow-old     1SG-POS
'I have a book.' lit. 'My book exists.'
(s1h / have-91
    :ARG1 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG2 (s1v / vakkahak)
    :aspect state
    :modal-strength full-affirmative)
Glosses: vakkahak = 'book'
```

Secondly, abstract concept conventions are inherited from AMR in a
variety of domains where information expressed in natural language text
needs to be standardized for computational tractability. This applies
to, for example, the annotation of different types of quantities (which
use abstract concepts such as `distance-quantity`,
`temporal-quantity` and `monetary-quantity`, as
illustrated in (2a)-(2b), and the annotation of dates and times (which use abstract concepts such as `date-entity`, as illustrated in (2c), all from Sanapaná). More information on abstract concepts can be found throughout this document in the sections dedicated to the specific semantic phenomena for which they are needed.

Example 2-2-3 (2)

Example 2-2-3 (2a)
```
cinco,  seis    meses   apk-ehl-ta'mehl-kes-kam-a
five    six months  2/3M-DSTR-be.good-CAUS-TI-NOM
'They would preserve it for five or six months.'
(s1e / enta'mehlkeskama-00 'preserve'
    :actor (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :undergoer (s1t / thing)
    :duration (s1o / or
        :op1 (s1t2 / temporal-quantity
            :quant 5
            :unit (s1m / mes))
        :op2 (s1t3 / temporal-quantity
            :quant 6
            :unit (s1m / mes)))
    :aspect habitual
    :modal-strength full-affirmative)
Glosses: mes = 'month'
```
Example 2-2-3 (2b)
```
escuela agrícola    seis    millón  cada    año on-yanmong-kes-ek
school  agricultural    six million each    year    1PL.IRR-exchange-CAUS-FUT
'For the agricultural school, we would pay six million (guaranies) per year.'
(s1e / enyanmongkeskama-00
    :actor (s1p / person
        :refer-person 1st
        :refer-number plural)
    :recipient (s1e2 / escuela
        :mod (s1a / agrícola))
    :theme (s1m / monetary-quantity
        :quant 6,000,000
        :unit (s1g / guaraní
            :mod (s1c / country

                :name (s1n / name :op1 "Paraguay"))))
    :frequency (s1r / rate-entity
        :ARG1 1
        :ARG2 (s1t / temporal-quantity
            :quant 1
            :unit (s1a2 / año 'year)))
    :aspect habitual
    :modal-strength full-affirmative)
Glosses: enyanmongkeskama-00 = 'pay'; escuela = 'school'; agrícola = 'agricultural'
```
Example 2-2-3 (2c)
```
apk-el-v-ayk-akh-a'     Venancio    el-eyv-om-akha'     mil     novecientos sesenta y   seis=anehla
2/3M-DSTR-arrive-TI-DUPL-NOM    Venancio    1PL-live-TI-NOM.LOC thousand    nine-hundred    sixty   and six=DUB
'Venancio and his companions arrived where we lived in ninteen sixty-six, maybe.'
(s1e / elvay'a-00 'arrive'
    :actor (s1p / person
        :name (s1n / name :op1 "Venancio")
    :companion (s1p2 / person))
    :goal (s1p3 / place
        :Place-of (s1e2 / eleyvoma-00
            :actor (s1p4 / person
                :refer-person 1st
                :refer-number plural)))
    :temporal (s1d / date-entity
        :year 1966)
    :aspect performance
    :modal-strength neutral-affirmative)
Glosses: eleyvoma-00 = 'live'
```

#### Part 2-2-4. Non-participant role relations

Another domain in which AMR conventions are inherited by UMR is the
annotation of non-participant role relations. Such relations are used to
annotate a wide range of meanings. Many of them, such as `:medium`,
`:topic`, and `:mod` (the latter of which is illustrated in (2-2-3 2b) are used to
annotate modifiers of referring expressions. Other relations are used
with specific abstract concepts: whenever a `date-entity`
concept is present, one of the temporal relations `:month`, `:year`, `:day`
etc. will be used, for example. The use of these relations is treated
more in detail in Part 3-2-2 of this document.

Even though many of these relations are straightforwardly inherited by
UMR, some changes are made to their use for the sake of cross-linguistic
comparability. Firstly, UMR adjusts the use of the `:mod` relation to
cover all *typifying* modifiers - i.e. modifiers which subcategorize the
reference of a referring expression rather than narrowing it down to a
specific entity (e.g. *women* in *women's magazine*). In AMR, this
semantic domain was shared between the `:mod` relation and a number of
other relations such as `:medium`, `:topic`, and `:group`. In UMR, these
other relations still exist, but they are treated as more fine-grained
values on a lattice underneath the more general `:mod` relation. Whereas
AMR used the `:frequency` and `:duration` relations as the main ways of
annotating aspect, UMR does this through a dedicated `:aspect` attribute.
However, UMR maintains the `:duration` and `:frequency` relations so that
annotators can use them to indicate more fine-grained aspectual
information beyond the aspect categories offered in the corresponding
attribute, as in (2-2-3 2b). UMR also adds a new non-participant role relation: the `:other-role` relation, which annotators can use when encountering meanings that UMR currently does not provide a straightforward annotation procedure for.

#### Part 2-2-5. Attributes

The last area in which AMR conventions are inherited by UMR is that of
*attribute* annotations. Attributes are relations which attach one of a
closed, pre-defined list of values to a concept node: for example, the
`:aspect` attribute allows annotators to hang a `State`, `Habitual`,
`Activity`, `Endeavor`, or `Performance` value off
of a predicate node.

Attributes inherited from AMR are `:polarity`, `:mode`,
`:quant`, and `:value` (Part 3-2-2, Part 3-3). The use
of the `:quant` relation was changed in that a more fine-grained
annotation scheme for quantification is now available (see Part 3-1-5, Part 3-3-4). The `:quant` relation is mainly what annotators with
less training or for languages with less available linguistic analysis
will use to flag concepts that are of interest with regards to
quantification. More confident annotators
and annotators for well-documented languages will apply the full
fine-grained quantification and scope scheme. One
specific change is that, whereas in mensural constructions (e.g. *three
cups of milk*), AMR varies between having the substance or the mensural
term as the head depending on morphosyntactic expression, UMR always
annotates the substance as the head for greater cross-linguistic
comparability. This means that even less conventionalized measure terms,
like English *cup* or *bag*, are annotated as modifiers, even though
they look like morphosyntactic heads. This is illustrated in (1). The use of the `:polarity` value is constrained to the sentence level.
Propositional negation is annotated in the modal section of the document
level annotation and through `:modal-strength` relations. The `:polarity` value is used to indicate any overt
morphosyntactic exponents of negation at the sentence level, flagging
such concepts as interesting for the modal or scope negation. This
includes e.g. morphologically negated adjectives like _unhappy_, even though in the
document-level modal annotation, these will not be annotated as negated.

Example 2-2-5 (1)
```
Three bottles of water
(s1w / water
    :quant 3
    :unit (s1b / bottle))
```

UMR introduces four new attributes: `:aspect` (see Part 3-3-1), `:degree` (see Part 3-3-6), and
`:refer-person` and `:refer-number` (see Part 3-3-5).

## Part 3. Sentence-Level Representation

### Part 3-1. UMR Concepts

#### Part 3-1-1. Eventive concepts

Identification of eventive concepts is important to participant role annotation as well as aspect and modality annotation.
The criteria used to identify events in UMR are largely based on the
criteria used in TimeML (Pustejovsky et al. 2005). Event identification is not based on parts of speech or word classes, since these vary greatly across languages. Instead, event identification is based on a combination of semantic type and information packaging (Croft 2001). Semantic type refers to the difference between entities (or, objects), states (or, properties), and processes; this can be thought of as a categorization of things in the real world.
Information packaging (also called discourse function or information
structure), on the other hand, characterizes how a particular linguistic
expression “packages” the semantic content. There are three fundamental
information packaging functions: reference, modification, and
predication. Croft (2022)  defines them as:

**reference**: what the speaker is talking about
**modification**: additional information provided about the referent
**predication**: what the speaker is asserting about the referents in a particular utterance

The three semantic types can occur with any of the three fundamental
information packaging functions, as shown in Table
1 from Croft (2022).

|  | Reference | Modification | Predication |
|---|---|---|---|
| Entities | the sharp **thorns** | the **bush’s** thorns | It **is a thorn.** |
| States | **sharpness** | the **sharp** thorns | Those thorns **are sharp.** |
| Processes | I said \[**that** the thorns **scratched** me\]. / the \[**scratching** of the thorns\] | the thorns **that** \[**scratched** me\] / the thorns \[**scratching** me\] | The sharp thorns **scratched** me. |

Table 1: Semantic types expressed in different information packaging constructions

Cross-linguistically, certain types of morphosyntactic constructions
tend to express specific combinations of semantic type and information
packaging; these are shown in Table 2,
modified from Croft (2001). Prototypical combinations of semantic type and
information packaging are indicated with caps. These correspond to
well-known part-of-speech classes across languages: entities in
reference correspond to nouns, states in modification to adjectives, and
processes in predication to verbs.

|  | Reference | Modification | **Predication** |
|---|---|---|---|
| Entities | UNMARKED NOUNS | relative clauses, PPs on nouns | **predicate nominals,** **complements** |
| States | deadjectival nouns | UNMARKED ADJECTIVES | **predicate adjectives,** **complements** |
| **Processes** | **event nominals, complements,** **infinitives, gerunds** | **participles, relative clauses** | **UNMARKED VERBS** |

Table 2: Constructions identified as events

The most prototypical expression for an event is a process in
predication, therefore we identify a word/phrase as an event if it has
either the semantic type of the prototype (process) or the prototypical
information packaging (predication). The categories which are identified
as events in UMR are shown in bold in Table 2.

##### Part 3-1-1-1. Processes in predication

Predicated processes are the most prototypical subcategory of events,
corresponding cross-linguistically to unmarked verbs. They will
therefore always be identified as events. This is shown in
(1) below. (Throughout this section, words
that are identified as events will be shown in bold; the relevant
phenomenon under discussion will be italicized.)

Example 3-1-1-1 (1)

(1a) She
**_repaired_** her bike.
(1b) Before
she **_went_** to school, she **repaired** my bike.

Regardless of whether they are in an independent clause, like *repaired*
in (1a), or a dependent clause, like *went* in
(1b), predicated processes are always
identified as events.

##### Part 3-1-1-2. Processes in modification and reference

Processes packaged as modifiers or referents should also be identified
as events. Cross-linguistically, these may take a variety of
morphosyntactic forms, such as event nominals (as in
(1a)), non-finite complements (as in
(1b)), participles (as in
(1c)), or relative clauses (as in
(1d)).

Example 3-1-1-2 (1)

Example 3-1-1-2 (1a) The
**_storm_ damaged** the roads.

Example 3-1-1-2 (1b) She
**wanted _to go_** to school.

Example 3-1-1-2 (1c) The
student **_playing_** the violin **likes** Bach.

Example 3-1-1-2 (1d) The student,
who is **_playing_** the violin, **likes** Bach.

The combination of semantic type and information packaging determines
whether or not a particular word in a particular context is identified
as an event. The morphological structure of a word (i.e., whether or not
it derives from a verb) doesn’t factor into whether or not it is
identified as an event. For example, not all event nominals are derived
from verbs, as in (2a); and, not all words
derived from verbs actually refer to processes, as in
(2b).

Example 3-1-1-2 (2)

Example 3-1-1-2 (2a) He is
**planning** a **_ceremony_** for Saturday.

Example 3-1-1-2 (2b)
The bus _driver_ **turned** the corner too sharply.

Even the same lexical item may or may not refer to a process, depending
on context as in (3) below.

Example 3-1-1-2 (3)

Example 3-1-1-2 (3a)

The **_final exam_** began at 8:00.

Example 3-1-1-2 (3b)

One student **threw** their _final exam_ in the trash.

In (3a), *final exam* refers to a process and therefore
is identified as an event. In (3b), however,
*final exam* refers to a physical object and therefore is not identified
as an event.

Participles (or other non-finite verb forms) are identified as events,
unless they are part of a compound. For example, *floating* in *floating
hospitals* is identified as an event, but *firing* in *firing squad* is
not, since it is part of a compound. One way to check for this
distinction is to see if the event described by the participle must be
ongoing at the reference time. For example, one can say *I saw the
firing squad* without having seen an actual firing event, whereas *I saw
the floating hospitals* implies that the seer witnessed the floating
event as well.

##### Part 3-1-1-3. States and entities

As mentioned above, anything that is predicated is identified as an
event, even if it is not a process. Two-place statives, such as *love*
in (1), are annotated in the same way as predicated
processes, i.e. an event is identified and labelled with the predicate
in the language.

Example 3-1-1-3 (1)

My cat **_loves_** wet food.

Other types of predicated states and entities require different
solutions based on their function and the strategy used to express them
in a language; we call these “non-verbal clauses”. The different
functional types of non-verbal clauses are shown below in Table 3.

| **Semantics** | **Information-packaging** | **Example** |
|---|---|---|
| possession | thetic/presentational | The teacher has a dog. |
| possession | predicational | The dog is the teacher's. |
| location | thetic/presentational | On the rock was a symbol. |
| location | predicational | The symbol was on the rock. |
| property | predicational | The cat is black. |
| object | predicational | Panda is a cat. |
| object | equational | Panda is my cat. |

Table 3: Non-verbal clause types

There are four semantic types of non-verbal clauses: possession,
location, property, and object. All of these occur with predicational
information-packaging: the possessive relationship, location, property,
or object category are predicated of the possession or theme. Possession and location are, in addition, used in a context in which the entire information is presented as ‘thetic’ or ‘all-new’ in the terms of
Lambrecht’s theory of information structure (Lambrecht 1994; cf. the contrast between
‘have’ possession \[thetic\] and ‘belong’ possession \[predicational\]
in Heine 1997). One common thetic function is presentational, as in the examples
in Table 3 above. For objects, it can be
difficult to distinguish equational (corresponding to Lambrecht’s
identificational information structure) and predicational
information-packaging in context (see Stassen 1997:106-111). Object predication asserts that
the theme is part of a category of objects (i.e., *Panda* fits within
the category of *cat*), whereas equational sentences indicate that two
referents are the same (i.e., *Panda* is the same referent as *my cat*).

For these non-verbal clause categories, the event identified is labelled
with a special abstract UMR predicate that indicates the relevant combination of
semantics and information-packaging. These are shown below in Table 4. Note that some of these (e.g. `have-91`, `belong-91`) look very similar to existing English PropBank predicates (`have-03` and `belong-01`, respectively). However, they are cross-linguistic abstract concepts meant to annotate the crosslinguistically stable meanings of thetic possession and predicative possession, respectively. For the labelling of participants with these
non-verbal clause predicates, see Part 3-2-1-1-1.

| Clause type | UMR Predicate | If Phrasal |
|---|---|---|
| thetic/presentational possession | have-91 | :possessor |
| predicative possession | belong-91 | :possessor |
| thetic/presentational location | exist-91 | :place |
| predicative location | have-place-91 | :place |
| property predication | have-mod-91 | :mod |
| object predication | have-role-91 | have-role-91 |
| object predication | have-rel-role-92 | have-rel-role-92 |
| object predication | have-org-role-92 | have-org-role-92 |
| object equation | identity-91 | identity-91 |

Table 4: Non-verbal clause predicates

States in modification, as in (2a) and
(2b), and states in reference, as in
(2c), are not identified as events.

Example 3-1-1-3 (2)

Example 3-1-1-3 (2a) The
_tall_ man...

Example 3-1-1-3 (2b) The man,
_who is tall_...

Example 3-1-1-3 (2c) His
_happiness_...

Similarly, entities in modification, as in (3a),
and entities in reference, as in (3b), are not
identified as events.

Example 3-1-1-3 (3)

Example 3-1-1-3 (3a) The man,
_who is a doctor_...

Example 3-1-1-3 (3b) The
_doctor_

Causal relationships follow the same rules as states and entities. They
are identified as events when they are predicated, as in
(4a), but they are not identified as events
otherwise, like in (4b).

Example 3-1-1-3 (4)

Example 3-1-1-3 (4a) The
**explosion _caused_** the house **to collapse**.

Example 3-1-1-3 (4b) The house
**collapsed** _because_ of the **explosion**.

##### Part 3-1-1-4. Implicit events

Since UMR annotates meaning, and not form, there are situations where
events are identified in the absence of explicit linguistic material.
These correspond to events which are implicit, given the context, but
not overtly expressed. We encourage annotators to be conservative on
this front; when in doubt, don’t add an implicit event.

We’ve identified two types implicit events: those where the implicit
event corresponds to an event mentioned earlier in the text (as in
(1)), and those where it does not (as in
(2)).

Example 3-1-1-4 (1)

Example 3-1-1-4 (1a) John was **smoking** on
the corner of the street, but when he **saw** me, he stopped
**\[_smoking_\]**.

Example 3-1-1-4 (1b) They **told** me “a card
was **left** on Tuesday” (no it wasn’t **\[_left_\]** of
course)...

In (1a), there is an implicit second *smoking* event and
in (1b), there is an implicit second *leave* event. These
implicit events should be annotated as coreferential with the event
mentioned earlier in the text (see Part 4-1).

In (2), however, the implicit events don’t
have a relationship with an event previously mentioned in the text;
instead, they refer to generic events which can be filled in from
context.

Example 3-1-1-4 (2)

Example 3-1-1-4 (2a) **Phoned** Amtrak on
Wednesday, **\[_they said_\]** “We **need** a consignment
number”.

Example 3-1-1-4 (2b) “I have **ordered** the Coast
Guard and our entire naval force in the (Central Philippines) region
**\[_to go_\]** to the area,” she **said**.

In (2a), the quotation marks make it clear that there is an
implicit *say* event. In (2b), we can identify a very general
*go* event, since *ordered...to the area* implies a motion event. For
these types of implicit events, the most abstract, least specific event
should be identified. For example in (2b), we could make an
assumption based on context clues (e.g., *Coast Guard, naval force*),
that the type of motion event is *sail*. But, that assumption may not be
accurate (and may not be shared amongst annotators); therefore, the most
general event possible should be identified.

#### Part 3-1-2. Named entities

Following AMR, each named entity in a text is annotated with a type. However, the vocabuary of the named entity types are adapted from AMR so that they reflect the characterization of additional languages and thus made uniform across languages. Example (1) has a `nationality` entity and a `person` entity.

Example 3-1-2 (1) Edmond Pope is an American businessman.
```
(s1h / have-role-91
    :ARG1 (s1p / person
        :name (s1n / name
            :op1 "Edmund"
            :op2 "Pope"))
    :ARG3 (s1b / businessman
        :mod (s1n2 / nationality
            :name (s1n3 / name
                :op1 "America")))
    :aspect state
    :modal-strength full-affirmative)
```
The total set of entity types are hierarchically organized, as listed in Table 5 below.

<!--organization, company, government-organization, military, criminal-organization, political-party, market-sector, school, university, research-institute, team, league-->
<!--location, city, city-district, county, state, province, territory, country, local-region, country-region, world-region, continent; ocean, sea, lake, river, gulf, bay, strait, canal; peninsula, mountain, volcano, valley, canyon, island, desert, forest moon, planet, star, constellation, (landforms and water forms?)-->

| Class | Type | Subtype |
|---|---|---|
| animal |  |  |
| plant |  |  |
| language |  |  |
| nationality |  |  |
| person |  |  |
| social_group | family |  |
|  | ethnic-group |  |
|  | regional-group |  |
|  | religious-group |  |
|  | clan |  |
|  | organization | international_organization, business, company, government_organization, political_organization, criminal_organization, armed_organization, academic_organization, association, sports_organization, religious_organization |
| geographic_entity | ocean, sea, lake, river, gulf, bay, strait, peninsula, mountain, volcano, valley, canyon, island, desert, forest |  |
| celestial-body | moon, planet, star, constellation |  |
| region | local-region, country-region, world-region |  |
| geo-political-entity | city, city-district, county, state, province, territory, country |  |
| facility | airport, station, port, tunnel, bridge, road, railway-line, canal, building, theater, museum, palace, hotel, worship-place, market, sports-facility, park, zoo, amusement-park |  |
| vehicle | ship, aircraft, aircraft-type, spaceship, car-make |  |
| cultural-artifact | work-of-art |
|  | picture |
|  | music |
|  | literature |
|  | dance |
|  | show |
|  | broadcast-program |
|  | publication | book, newspaper, magazine, journal |
| cultural-activity |  |  |
| event | incident, natural-disaster, earthquake, war, conference, game, festival, ceremony |  |
| law | court-decision, treaty |  |
| award |  |  |
| food-dish |  |  |
| notational-system | writing-script, music-key, musical-note |
| variable |  |  |
| computer-program |  |  |
| biomedical-entity | molecular-physical-entity, small-molecule, protein, protein-family, protein-segment, amino-acid, macro-molecular-complex, enzyme, nucleic-acid, pathway, gene, dna-sequence, cell, cell-line, species, taxon, disease, medical-condition |  |

<!--

| Type | Subtype (AMR NE Type) |
|---|---|
| person | person, family, animal, language, nationality, ethnic-group, regional-group, religious-group, political-movement |
| *Organization* | commerical_org (company), political_org (political-party), government_org (government_organization), military_org (military), criminal_org (criminal-organization), academic_org (school, university, research-institute), sports_org (team, league), market-sector |
| *Geographic-entity* | ocean, sea, lake, river, gulf, bay, strait, canal, peninsula, mountain, volcano, valley, canyon, island, desert, forest |
| *Celestial-body* | moon, planet, star, constellation |
| *region* | local-region, country-region, world-region |
| *GPE* | city, city-district, county, state, province, territory, country |
| *facility* | airport, station, port, tunnel, bridge, road, railway-line, canal, building, theater, museum, palace, hotel, worship-place, market, sports-facility, park, zoo, amusement-park |
| *event* | incident, natural-disaster, earthquake, war, conference, game, festival |
| *product* | vehicle, ship, aircraft, aircraft-type, spaceship, car-make, work-of-art, picture, music, show, broadcast-program |
| *publication* | book, newspaper, magazine, journal |
| *Natural-object* |  |
| *Artifact* | award, law, court-decision, treaty, music-key, musical-note, food-dish, writing-script, variable, program |
| *Biomedical-entity* | molecular-physical-entity, small-molecule, protein, protein-family, protein-segment, amino-acid, macro-molecular-complex, enzyme, nucleic-acid, pathway, gene, dna-sequence, cell, cell-line, species, taxon, disease, medical-condition |

Table 5: Named entity types

-->

#### Part 3-1-3. Concept-word mismatches

Cross-linguistically, concepts are not always mapped onto words in the
same way. Many low-resource languages are morphologically more complex
than languages like English, and they often express in a single word
concepts for which English needs multiple words. For a number of
reasons, UMR does not require the decomposition of morphologically
complex words into morphemes that individually map to concepts, but
instead, such words can as a whole map to multiple concepts. How exactly
this mapping between single, (often) morphologically complex words and
multiple concepts is achieved depends on which semantic categories are
involved and how they behave across languages. This section provides
guidance on the annotation of predicates and arguments in five different
types of constructions where the mapping between words and concepts is
not straightforward.

##### Part 3-1-3-1. Predicate and argument as one word

In languages that make use of verbal argument indexation (i.e.
pronominal affixes on the verb to cross-reference semantic arguments) or
noun incorporation, predicates and their arguments can be expressed
together in a single word. Both issues are illustrated in
(1) from Arapaho. Here, what is
expressed as a multi-word sentence in the English translation takes the
form of a single Arapaho word. The pronominal suffix *-o'* indicates
that a first person argument acts on a third person argument. The
lexical item for 'head', *e'ei*, is incorporated in the verb, and the
classifier *-s* indicates that the instrument is a blade-like implement.
So, this single word expresses the predicate, and the actor, undergoer,
theme, and instrument arguments of this state of affairs.

Example 3-1-3-1 (1)
```
nih-teb-e'ei-s-o'
PST-break/remove.stick.like-head-by.blade.CAUS-1SG/3SG
'I cut his head off with a knife.'
(s1t / teb-e'ei-s ‘break/remove.stick.like’
    :actor (s1p / person
        :refer-person 1st
    :refer-number singular)
    :undergoer (s1p2 / person
        :refer-person 3rd
    :refer-number singular)
    :theme (s1t2 / thing
        :refer-person obviative)
    :aspect performance
    :modal-strength full-affirmative)
```

When languages use verbal affixes to index arguments, these arguments
then may or may not be expressed through independent NPs elsewhere in
the clause. UMR treats such indexed arguments in the same way as it does
free pronouns - they are identified as arguments of the verb. So, even
though there is no overt word in the sentence above referring to a first
person actor or a third person undergoer, these arguments are
nevertheless identified and annotated (using a named-entity concept, in
this case `person` or `thing`), as they are clearly identifiable to
native speakers of the language.

Noun incorporation constructions come in different types across
languages (Mithun 1984). Some constructions, such as the one illustrated by *-e'ei*
'head' above, are not very grammaticalized. Here, the incorporated noun
functions as an argument of the verb, meaning that no overt NP can be
present in the clause to fill this semantic role. So, while UMR treats
the whole stem *teb-e'ei-s* as the predicate, it also identifies a
separate concept for 'head', which has the `:theme` participant role as
seen in the UMR corresponding to example
(1).

On the other hand, in more grammaticalized noun incorporation
constructions, the incorporated noun does not "replace" one of the
verbal arguments. Instead, the incorporated noun only denotes a very
general class of objects, and an independent NP can be present in the
clause to specify the kind of object at hand. Such noun incorporation
constructions are often referred to as "verbal classifiers". For
example, the Arapaho instrumental suffix *-s* indicates that the
"remove"-event is done by means of a blade-like implement, but still an
independent NP can appear to specify the instrument. For such
grammaticalized noun incorporation constructions, no separate concept
corresponding to the incorporated noun is identified. A participant
with the `:instrument` role is only identified if it is expressed as an
overt NP in the clause.

This treatment of noun incorporation means that a certain amount of
linguistic analysis must be done prior to UMR annotation. If the
language at hand has one or more noun incorporation constructions,
annotators need to know for any individual construction whether or not
it allows the expression of the incorporated participant as an
independent overt NP. Of course, grammaticalization is a continuous
process, and therefore noun incorporation constructions are likely to be
found on a continuum between these two end points. However, we map this
continuum onto a discrete choice for annotators by taking the ability of
an incorporated noun to co-occur with an independent NP as criterial. This treatment of single words containing predicates and arguments is summarized in table 6 below.

| Construction type | Construction definition/diagnostic | UMR Treatment |  |  |  |
|---|---|---|---|---|---|
| Pronominal affixes | Verbal affixes expressing person/number values of arguments | If coreferential with overtly expressed nominal argument: don't annotate |  |  |  |
| Pronominal affixes | Verbal affixes expressing person/number values of arguments | If no overt nominal is present: annotate as argument with relevant named-entity concept | Incorporated nouns | No nominal expression coreferential with the incorporated noun can occur in the clause | Annotate separate concept for incorporated noun as argument |
| Verbal classifier | Nominal expression specifying type of object denoted by incorporated noun can occur in the clause | Do not annotate separate concept for incorporated noun |  |  |  |

Table 6: Treatment of pronominal affixes and noun incorporation

##### Part 3-1-3-2. Valency-changing operations

Secondly, constructions used to change the valency of verbs (causatives,
applicatives, reflexives etc.) can cross-linguistically either express
the two concepts at hand in separate words (e.g. English *I **made** him
**eat***), or combine the two concepts into a single word (e.g. Sanapaná
*as-**tav-kes**-ke'* 'I made her/him eat'). In order to assess whether
one or two concepts should be identified for UMR annotation, unity under
negation is chosen as a criterion.

In English Causatives, for instance, negation can apply to the causing
event and to the caused event separately as in
(1), indicating that the causing event and the
caused event are construed as independent predicates. Therefore, a
"cause"-event is identified in addition to the "drink"-event expressed
by the verb root.

Example 3-1-3-2 (1)

Example 3-1-3-2 (1a) Grandmother made the kid drink the water.
```
(s1d / drink
    :cause (s1m / make
        :actor (s1p / person
            :ARG1-of (s1h / have-rel-role-92
                :ARG3 (s1g / grandmother))
            :refer-number singular)
        :aspect performance
        :modal-strength full-affirmative)
    :actor (s1k2 / kid
        :refer-number singular)
    :undergoer (s1w / water)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-1-3-2 (1b) Grandmother did not make the kid drink the water.
```
(s1d / drink
    :cause (s1m / make
        :actor (s1p / person
            :ARG1-of (s1h / have-rel-role-92
                :ARG3 (s1g / grandmother))
            :refer-number singular)
        :aspect performance
        :modal-strength full-negative)
    :actor (s1k2 / kid
        :refer-number singular)
    :undergoer (s1w / water)
    :aspect performance
    :modal-strength neutral-affirmative)
```

Example 3-1-3-2 (1c) Grandmother made the kid not drink the water.
```
(s1d / drink
    :cause (s1m / make
        :actor (s1p / person
            :ARG1-of (s1h / have-rel-role-92
                :ARG3 (s1g / grandmother))
            :refer-number singular)
        :aspect performance
        :modal-strength full-affirmative)
    :actor (s1k2 / kid
        :refer-number singular)
    :undergoer (s1w / water)
    :aspect performance
    :modal-strength full-negative)
```

Kukama (Tupían), on the other hand, has a morphological causative, as in
(2). The caused event and causing event cannot be
negated independently: if
(2) is negated, negation necessarily scopes over
both, indicating that this form is construed in Kukama as denoting a
single event. Therefore, only a single predicate is identified
(corresponding to the whole verb stem *kuratata* 'make drink').

Example 3-1-3-2 (2)
```
nai     kurata-ta   churan=ui   uni-pu
grandmother drink-CAUS  kid=PST     water-INST
'Grandmother made the kid drink the water.'
(s1k / kuratata
    :causer (s1p / person
        :ARG1-of (s1h / have-rel-role-92
            :ARG3 (s1n / nai))
        :refer-number singular)
    :actor (s1c / churan)
    :undergoer (s1u / uni)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: kuratata = 'make drink'; nai = 'grandmother'; churan = 'kid'; uni = 'water'
```

This criterion will be used for all valency change concepts: if the
"lexical" concept expressed by the verb root and the valency change
concept can be negated independently, two events are identified, whereas
if they cannot be negated independently, only one event is identified
corresponding to the derived verb stem (see table 7). The semantics and valency of
such derived forms will be inferred from the participant role annotation
associated with the verb. Which valency changes lead to which argument
structures is detailed in Part 3-2-1-2-1.

| **IF** | **THEN** |
|---|---|
| Event and valency-changing category can be negated independently | Identify and annotate them as separate events |
| Event and valency-changing category cannot be negated independently | Identify a single event |

Table 7: Treatment of valency-changing categories

##### Part 3-1-3-3. TAM categories

Third, some semantic categories such as (phasal) aspect, temporal
relations, and modal relations, can be expressed cross-linguistically
either through bound morphology or through separate words (often called
"auxiliaries").

Phasal aspectual meanings such as inchoative, completive, and
continuative, firstly, are never identified as separate events, even if
they are expressed through independent words. Instead, they will simply
inform the aspect attribute label of the event they modify (Part 3-3-1). This principle is illustrated in example
(1). In
Manipuri, the inchoative concept and the "close"-meaning form part of
the same word, while in the English translation, they are expressed as
two different words (example from Bhat 1999). Nevertheless, in both the English and the Manipuri
UMR, only one event is identified (corresponding to concept of property
predication, in this case).

Example 3-1-3-3 (1)
```
ce  əsi mu-re
paper   this    black-change
'This paper has become black.'
(s1h / have-mod-91
    :ARG1 (s1c / ce)
    :mod (s1s / əsi)
    :ARG2 (s1m / mu)
    :aspect performance)
Glosses: ce = 'paper'; əsi = 'this'; mu = 'black'

Or:
(s1h / have-mod-91
    :ARG1 (s1p / paper)
    :mod (s1t / this)
    :ARG2 (s1b / black)
    :aspect performance)
```

Similarly, modal and temporal auxiliaries will not be identified
independently as events, but will instead inform the modal and temporal
dependency annotation: in English, for example, modal auxiliaries such
as *might* and *should* in *He **might/should** go to school* are not
identified as independent events, and neither are temporal auxiliaries
such as *have* and *be* in *She **has gone/is going** to school*. How
such meanings exactly inform the temporal and modal annotation is
detailed in Part 4-2 and Part 4-3.

For some semi-modal concepts, there may be language-internal semantic
evidence that they are construed as independent concepts. For instance,
in the English desiderative construction in
(2), the desire-event can be modalized
independently of the "go"-event, indicating that desires are construed
as independent events in English. The UMR therefore has predicates for
both *want* and *go*.

Example 3-1-3-3 (2)

Example 3-1-3-3 (2a) She wants to go to school.
```
(s1w / want-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1g / go-01
        :ARG1 s1p
        :ARG4 (s1s / school)
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-1-3-3 (2b) She may want to go to school.
```
(s1w / want-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1g / go-01
        :ARG1 s1p
        :ARG4 (s1s / school)
        :aspect performance)
    :aspect state
    :modal-strength neutral-affirmative)
```

However, if in a language the desire-event cannot be modalized
independently from the desired event, no separate event is identified
for the desire-semantics. Instead, the desiderative is taken into
account in the modal annotation, as detailed in Part 4-3. For three
other semi-modal concepts, the same guidelines as to concept-word
mismatches are used as for desideratives: this is the case for conatives
('try to'), optatives ('wish that'), and frustratives ('fail to').

##### Part 3-1-3-4. Associated Motion

Associated motion constructions are treated in a similar way to
semi-modals. If associated motion events can have their own argument
structure (i.e. if they can co-occur with NPs expressing start points or
end points of motion events), these motion events are identified as
separate predicates in the UMR. If they cannot take their own argument
structure, only one event is identified.

For instance, the Sanapaná associated motion construction in
(1) expresses that the sleeping-event takes place during a motion event
towards the deictic center: the suffix *-ant* essentially means that the
event expressed by the verb root happens "while coming here". As shown
in (1), this construction can co-occur with a spatial NP. However, such a spatial NP can only express the location of the sleeping-event rather
than the goal or the start point of the motion event. It is therefore
better analyzed as a circumstantial locative belonging to the
"sleep"-event expressed by the verb root than as an argument of the
motion event. The motion event itself therefore has no independent
argument structure, and only one event is identified for UMR annotation.

Example 3-1-3-4 (1)
```
en-na'-ten-ek-ant-a'
1PL-DSTR-sleep-TI-VNT-NOM   La  Esperanza
'We slept in La Esperanza while coming here'
(s1e / enna'tenekanta' 'sleep while coming'
    :undergoer (s1p / person
        :refer-person 1st
    :refer-number plural)
    :place (s1c / city
        :name (s1n / name
            :op1 "La"
            :op2 "Esperanza"))
    :aspect state
    :modal-strength full-affirmative)
                                                            :aspect activity
                                                            :modal-strength full-affirmative)
                                                            :aspect state
                                                        :modal-strength full-affirmative)

Or:
La  Esperanza
(s / sleep-01
:ARG0 (p / person
:refer-person 1st
:refer-number plural)
:place (c / city
:name (n / name
:op1 "La"
:op2 "Esperanza"))
:temporal (c2 / come-01
:ARG1 p
:ARG4 (h / here)
```

The English "venitive" construction in the translational equivalent of
(1), however, can co-occur with an NP which is clearly an argument of the "come"-event: one could say, for instance *We slept in La Esperanza
while coming here **from Puerto Casado***. Therefore, the motion event
and the "sleep"-event are construed in English as two independent
events, and are annotated in UMR as two separate predicates.

##### Part 3-1-3-5. Light verb constructions
A light verb construction takes the canonical form of a verb followed by an eventive noun, and the verb has little meaning while the nound
carries most of the semantic content. An example is in (1), where ``do'' is a light verb and most of the semantic content comes from
``interview''. In this case the UMR concept ``interview-01'' is created based on the eventive noun, while the verb is simply dropped. Note however
the verb may contribute to the aspectual attribute of the concept.

Example 3-1-3-5 (1)  Where do you get this information from that Obama uses tax payer money to do interviews and bus trips?

```
(s1g / get-01
    :aspect performance
    :ARG0 (s1p / person
        :refer-number singular
        :refer-person 2nd)
    :ARG1 (s1i / information
        :mod (s1t / this)
        :topic (s1u / use-01
            :aspect habitual
            :ARG0 (s1p2 / person
                :name (s1n / name
                    :op1 "Obama"))
            :ARG1 (s1m / money
                :source (s1p3 / person
                    :ARG0-of (s1p4 / pay-01
                        :aspect process
                        :ARG1 (s1t2 / tax-01))))
            :ARG2 (s1a2 / and
                :op1 (s1i2 / interview-01
                    :aspect habitual
                    :ARG1 s1p2)
                :op2 (s1t4 / trip-03
                    :aspect habitual
                    :ARG0 s1p2
                    :medium (s1b / bus)))))
    :ARG2 (s1a / umr-unknown))
```

##### Part 3-1-3-6. Non-verbal clauses

Many types of "non-verbal clauses", such as predicate nominals and
predication of properties, possession, and location (see Part 3-1-1-3 for the UMR predicates that are used to annotate these meanings), show different
mappings between concepts and words across languages. According to typological studies by Stassen (1997, 2009), Heine (1997), and Creissels (2019), there are three cross-linguistically common strategies for the expression of such meanings. English uses an
easily identifiable "verbal" predicate with argument NPs, as seen in the
English translational equivalents of the Kukama examples in
(1) and (2). In English, these constructions do not pose
serious problems to the predicate-argument structure of UMR - one could
simply identify the "have" or "be"-verb as a predicate, and the NPs in
the clause as its arguments.

In the Kukama object predication construction in
(1), however, the predicate does not map to
an overt word: object predication is expressed through juxtaposition of
two NPs, with the predicational meaning implicit but inherent in the
construction. In the Kukama thetic possession construction in (2), on the other hand, the possessum
and the relation of possession are expressed together as a single word
which functions as a predicate: something that is typically thought of
as an "argument" is predicativized. In languages that use the construction type exemplified in (2), there is only one of the participants that can act as the predicate cross-linguistically. For example, in languages that use a (2)-type strategy for object predication, it is always the object category participant and never the theme participant that morphosyntactically looks like a predicate. Both these structures pose problems
for the annotation of predicate-argument structure, since there is no
separate material that can be identified as a predicate.

Example 3-1-3-6 (1)
```
ajan    kunumi
this    young.man   shaman
'This young man is a shaman.'
(s1h / have-role-91
    :ARG1 (s1k / kunumi
        :mod (s1a / ajan)
        :refer-number singular)
    :ARG3 (s1t / tsumi)
    :aspect state
    :modal-strength full-affirmative)
Glosses: kunumi = 'young man'; ajan = 'this'; tsumi = 'shaman'

Or:
tsumi
(s1h / have-role-91
    :ARG1 (s1m / man
        :mod (s1y / young)
        :mod (s1t / this)
        :refer-number singular)
    :ARG3 (s1s / shaman)
    :aspect state
    :modal-strength full-affirmative)
```

Example 3-1-3-6 (2)
```
Mijiri-tin  ɨara-yara
Miguel-CER  canoe-owner
'Miguel does have a canoe.' lit. 'Miguel is a canoe-owner.'

(s1h / have-91
    :ARG1 (s1p / person
        :name (s1n / name
            :op1 "Mijiri")
        :refer-number singular)
    :ARG2 (s1a / ɨarayara)
    :aspect state
    :modal-strength full-affirmative)
Glosses: ɨarayara = 'canoe'

Or:
(s1h / have-91
    :ARG1 (s1p / person
        :name (s1n / name
            :op1 "Miguel")
        :refer-number singular)
    :ARG2 (s1c / canoe)
    :aspect state
    :modal-strength full-affirmative)
```

We propose a set of seven abstract concept predicates each corresponding
to a discrete "non-verbal clause" function, listed in the table below. When there is no overt predicate-word, as
in (1), we assume that annotators will be able
to recognize the type of non-verbal clause function they are dealing
with. They should use such an abstract predicate concept as predicative core of the graph, and use the appropriate numbered argument roles as specified in
the table (see also Part 3-2-1-1-1 for more in-depth treatment of the argument structure annotation with these predicates).

In constructions with predicativized arguments, such as
(2), once again annotators are expected to recognize the type of non-verbal clause function at hand and select the appropriate predicate. An argument concept will be identified and linked to the predicativized participant word in the sentence - the possessum *ɨara-yara* in the case of (2). As can be seen in the example UMRs
above, the resulting graphs have similar structures regardless of
whether a language uses an overt-predicate strategy, a zero-predicate
(juxtaposition) strategy, or a predicativized argument strategy for such
"non-verbal clause" meanings.

| Clause Type | Predicate | ARG1 | ARG2 | ARG3 | ARG4 | ARG5 |
|---|---|---|---|---|---|---|
| Thetic Possession | have-91 | possessor | possessum | --- | --- | --- |
| Predicative Possession | belong-91 | possessum | possessor | --- | --- | --- |
| Thetic Location | exist-91 | location | theme | --- | --- | --- |
| Predicative Location | have-place-91 | theme | location | --- | --- | --- |
| Property Predication | have-mod-91 | theme | property | --- | --- | --- |
| Object Predication | have-role-91 | theme | reference point | object category, arg1 | object category, arg2 | --- |
| Object Predication | have-org-role-92 | theme | organization | title of role | job description | --- |
| Object Predication | have-rel-role-92 | theme | relative | theme's role | relative's role | relationship basis |
| Equational | identity-91 | theme | equated referent | --- | --- | --- |

Table 8: Argument structure of non-verbal clause predicates

##### Part 3-1-3-7. Multi-word concepts

In languages with simpler morphology, the opposite situation, *multi-word concepts* may arise. Multi-word concepts can simply be handled by
concatenating the lemmatized words, as in (1). In (1a), *take-out-11* is a multi-word concept, meaning a UMR concept that maps to multiple words. In this case, the multi-word concept also has more than one sense, as indicated by the sense number *11*.

Example 3-1-3-7 (1)

Example 3-1-3-7 (1a) So I normally steep it in hot water , then take it out and stir - fry it.
```
(s1c / cause-01
    :ARG1 (s1a / and
        :op1 (s1s / steep-01
            :ARG0 (s1p / person
                :refer-person 1st
                :refer-number singular)
            :ARG1 (s1t / thing
                :refer-number singular)
            :ARG2 (s1w / water
                :ARG1-of (s1h / hot-05))
            :aspect habitual
            :modal-strength full-affirmative)
        :op2 (s1a2 / and
            :op1 (s1t2 / take-out-11
                :ARG0 s1p
                :ARG1 s1t
                :aspect habitual
                :modal-strength full-affirmative)
            :op2 (s1s2 / stir-01
                :ARG0 s1p
                :ARG1 s1t
                :aspect habitual
                :modal-strength full-affirmative)
            :op3 (s1f / fry-01
                :ARG0 s1p
                :ARG1 s1t
                :aspect habitual
                :modal-strength full-affirmative)
            :temporal (s1t3 / then)))
    :ARG1-of (s1n / normal-02))
```

Multi-word concepts are not limited phrasal verbs like ``take out''. They also include idiomatic expressions like ``jump on the bandwagon'', as in
(1b):

Example 3-1-3-7 (1b)  Pretty soon the far left loons will jump on his wagon.
```
(s1j / jump-on-bandwagon-09
      :aspect performance
      :ARG0 (s1l / loon
            :ARG1-of (s1l2 / left-19
                  :degree (s1f / far)))
      :ARG1 (s1p / person
               :refer-person 3rd
           :refer-number singular)
      :temporal (s1s / soon
            :mod (s1p / pretty)))
```
Note that these muli-word concepts are predicates and have their own arguments. Other multi-word concepts are not predicates and are simply concatenation of
single words, as in (1c), where the multi-word concept is *as-well*, which maps to two words.

Example 3-1-3-7 (1c) The moral aspects of the movement intrigued him as well
```
(s1i / intrigue-01
    :ARG0 (s1a / aspect
        :ARG1-of (s1m / moral-02)
        :possessor (s1m2 / movement-07)
        :refer-number plural)
    :ARG1 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :mod (s1a2 / as-well)
    :aspect state
    :modal-strength full-affirmative)
```

In languages like Chinese where there are no natural word boundaries in written text, sentences will have to go through a word segmentation process to facilitate the mapping of words into UMR concepts. Consecutive sequences of Chinese characters that form a single concept will always be segmented into a single word. This is the case for idioms such as 缘木求鱼, 刻舟求剑, which are segmented into single words, and  are mapped to single concepts in UMR annotation.  However, multi-word concepts are still relevant if the sequence of words that form a single concept are discontinuous, as 帮-忙-01 in (2a):

Example 3-1-3-7 (2a) 这 办法 帮 不 了 我 多 大 忙 ， 点灯人 说 。
```
(s1x0 / 说-01
    :ARG0 (s1x11 / 人
        :ARG0-of (s1x12 / 点-01
            :ARG1 (s1x13 / 灯)))
    :ARG1 (s1x14 / 帮-忙-01
        :degree (s1x20 / 大-01
            :polarity (s1x15 / -))
        :ARG0 (s1x16 / 办法
            :mod (s1x17 / 这))
        :ARG1 s1x11)
    :aspect performance
    :modal-strength full-affirmative)
```

Multi-word concepts are also relevant for idiomatic expressions that are segmented into multiple words but mapped single concepts.

Example 3-1-3-7 (2b) 我 把 锤子 、 螺钉 、 饥渴 、 死亡 ， 全都 抛在 脑 后 。
```
(s1x0 / 抛在脑后-01
    :ARG0 (s1x2 / individual-person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1x3 / and
        :op1 (s1x4 / 锤子)
        :op2 (s1x5 / 螺钉)
        :op3 (s1x6 / 饥渴)
        :op4 (s1x7 / 死亡))
    :manner (s1x11 / 全-01)
    :manner (s1x12 / 都)
    :aspect performance)
```

##### Part 3-1-3-8. Miscellaneous constructions
Other than multi-word concepts, languages often have regular or irregular constructions that involve mapping multipe words to single concepts. We adopt the general approach of AMR, which is to propose a set of abstract predicates each of which has their semantic roles to annotate such constructions. (1) is such an example, where the abstract concept ``correlate-91'' is proposed to annotate the ``the X-er, the Y-er`` construction.
<!--which concepts are languages-specific, and which are uniform? -->

Example 3-1-3-8 (1) The more I read your stuff, the more I am convinced that you have a black heart.

```
(s1c2 / correlate-91
    :aspect habitual
    :ARG1 (s1m / more
        :frequency-of (s1r / read-01
            :ARG0 (s1p / person
                :refer-person 1st
                :refer-number singular)
            :ARG1 (s1s2 / stuff
                :possessor (s1p2 / person
                    :refer-person 2nd
                    :refer-number singular))))
    :ARG2 (s1m2 / more
        :ARG3-of (s1h3 / have-degree-91
            :ARG1 0
            :ARG2 (s1c / convince-01
                :ARG1 s1p
                :ARG2 (s1h / have-03
                    :ARG0 s1p2
                    :ARG1 (s1h2 / heart
                        :ARG1-of (s1b / black-06)))))))
```

<!-- we need a list of such predicates-->

#### Part 3-1-4. Word senses

 UMR allows concepts to be word senses. In order to annotate word senses, it is necessary to first have a sense inventory for all words that need to be sense-disambiguated. For languages that do not have a sense inventory, concepts can simply be represented by lemmas. For predicate concepts which the annotator wants to flag for later inclusion in a lexicon, the suffix -00 can be added to such lemmas. It is also possible that a language only has a sense inventory for a subset of the words. This is the case with English (1) and Chinese (2), where word senses are defined for predicates together with their arguments in *frame files*.

Example 3-1-4 (1) The school has approximately 570 pupils.
```
(s1h / have-91
    :ARG1 (s1s / school)
    :ARG2 (s1p / pupil
        :quant (s1a / approximately
            :op1 570))
    :aspect state
    :modal-strength full-affirmative)
```

Example 3-1-4 (2)
```
 并且 还 有 很多 高层 的 人物 哦 ！
There will even be many VIPs!
(s1x / and
    :op2 (s1e / exist-91
        :mod (s1x2 / 还)
        :ARG2 (s1x3 / 人物
            :mod (s1x4 / 高层)
            :quant (s1x5 / 很多))
        :mode Expressive
        :aspect state
        :modal-strength full-affirmative))
```

 
#### Part 3-1-5. Scope for Quantification and negation

To facilitate the translation of UMR into first-order expressions to support logical inference,
we add a **scope** concept to represent the relative order of the predicate, quantified concept and negated concept.
In most cases, the order of these elements are interpreted in textual order, and do not need an over scope annotation.
The scope annotation is only needed when these elements are interpreted "out-of-order", as in (1).

Example 3-1-5 (1)
```
Someone didn't answer all the questions
(s1a / answer-01
    :ARG0 (s1p / person)
    :ARG1 (s1q / question
        :quant A
        :polarity -)
    :Pred-of (s1s / scope
        :ARG0 s1p
        :ARG1 s1q))
```

Related to scope is the issue of distributive vs. collective interpretations of events. Ambiguities in this realm may arise in a great number of different contexts. They may be triggered by, amongst others, explicit quantifiers or numerals, or events with plural arguments. For example, in (2) below, is there a single woman which every man loves, or does every man love a different woman? The latter interpretation is distributive, the former is usually interpreted as collective.

Example 3-1-5 (2)

Example 3-1-5 (2a) Each man loves a woman.

However, many cases that are technically ambiguous nevertheless have a strong default reading stemming from the lexical semantics of the predicate and its arguments. For example, in (3a), there is a strong default interpretation that every single student ran 5 kilometers rather than that they ran a total of 5 kilometers between them - _run_ is typically an individual activity, so its lexical semantics trigger a default distributive reading. However, in (3b), the equally strong default interpretation is that the students carried a single piano together and there was only a single carrying-event - our world knowledge specifies that things as heavy as a piano must typically be carried by multiple people, so the lexical semantics of the predicate-argument combination here trigger a default collective reading. In yet another set of cases, our "default" feeling is that it does not really matter in what configurations the participants participate in the denoted events. In (3c), all that typically matters is that 6 states were hit by at least one hurricane each, and that there was a total of 10 hurricanes. We can't really know how many hurricanes hit each state, and we don't really care - all we know is that 6 states and 10 hurricanes were involved. This kind of default interpretation is called a summation reading.

Example 3-1-5 (3)

Example 3-1-5 (3a) The linguistics students ran 5 kilometers to raise money for charity.

Example 3-1-5 (3b) The linguistics students carried a piano into the theater.

Example 3-1-5 (3c) Ten hurricanes hit six states over the weekend.

Scope will not be annotated for summation readings (as we cannot reliably know it from the text alone), nor is it annotated where a distributive or collective reading can be predictably derived from the lexical semantics. In other words, whenever _run_ is interpreted distributively or _carry a piano_ is interpreted collectively, no scope annotation is needed. The scope annotation only comes into play when some overt linguistic element forces an interpretation that diverges from the lexical default. For example, in (4a), _together_ forces a collective interpretation of _run_, in (4b), _each_ forces a distributive interpretation of _carry a piano_, and in (4c), _each_ similarly forces a distributive interpretation of _hit_. In all these cases, a (s / scope) predicate would appear to clarify the non-canonical scopal relations.

Example 3-1-5 (4)

Example 3-1-5 (4a) The linguistics students together ran 200 kilometers to raise money for charity.

Example 3-1-5 (4b) The bodybuilders each carried a piano into the theater.

Example 3-1-5 (4c) Ten hurricanes each hit six states over the weekend.

#### Part 3-1-6. Discourse-relations

When multiple events are expressed in a complex sentence, a variety of semantic relations can hold between them. UMR provides annotators with a lattice of category values to annotate such discourse-level event-event relations. This lattice is based partly on existing typological research (Malchukov 2004; Thompson & Longacre 1985), and partly on patterns of expression through adverbial subordination or coordination in English. This lattice covers event-event relations that are typically overtly and obligatorily expressed in languages through either (coordinating or subordinating) conjunctions or dedicated (“deranked”) verb forms. In other words, it does not cover relations typically expressed through optional “discourse adverbs”.

![Discourse Lattice_2022](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Discourse%20Lattice_May2022.png)

Annotators may choose annotation values from more fine-grained levels of the lattice when they are confident in doing so, or from more course-grained levels when they are in doubt. Generally, (adverbial) subordination constructions express overtly more fine-grained values. Many of these are already treated in other parts of UMR (particularly through participant roles), in which case cross-references will lead annotators to the relevant sections of this document. Coordination constructions tend to be more polysemous – they subsume various more fine-grained values and may be ambiguous between them, and they might therefore require the use of higher-level categories. This description already hints at the observation that many of the event-event relations on this lattice can be expressed through either coordination or subordination. We follow Talmy (1978), Reinhart (1984), and Wierzbicka (1980) in taking this difference not to be a semantic one, but rather an information-structural one between a “complex figure” construal (both events are equally “prominent”) and a “figure-ground” construal (one event is “foregrounded” and another is “backgrounded”). We therefore do not require annotators to annotate the same meaning differently when expressed through coordination as opposed to subordination (although, as mentioned before, subordination constructions may allow for the identification of more fine-grained meanings). In the examples below, both options are illustrated wherever possible.

Each discourse relation on the lattice is defined below, based on Croft (2022, ch. 15, ch. 17).

```Disjunctive```: Construes two (or more) events as being alternatives of each other in some way. Roughly corresponds to the range of meanings expressed by English _(either) or_. UMR expresses this meaning through an abstract concept ```or``` which takes numbered ```:opX``` arguments for the construed alternatives as in (1).

Example 3-1-6 (1)
```
I will go for a walk or play some soccer.
(s1o / or
    :op1 (s1w / walk-01
        :ARG0 (s1p / person
            :refer-person 1st
            :refer-number singular)
        :aspect process
        :modal-strength full-affirmative)
    :op2 (s1p2 / play-01
        :ARG0 s1p
        :ARG1 (s1s / soccer)
        :aspect process
        :modal-strength full-affirmative))
```

There are two more fine-grained subtypes of disjunctive relations:

```Inclusive Disjunctive```: also known as “non-exhaustive disjunction”. Indicates that either any of the construed alternatives can be “chosen” individually, or any combination of the construed alternatives. This is illustrated in (2a) from Hua (Haiman 1978:7-8). Here, _-ve_ indicates that bashing pandanus, husking and eating corn, and planting bananas are not mutually exclusive alternatives. Performing any or all of these actions equally violates a sexual taboo. UMR uses an abstract concept ```inclusive-disj``` to annotate this meaning, with numbered ```:opX``` roles for the construed alternatives.

```Exclusive Disjunctive```: also known as “exhaustive disjunction”. Indicates that the construed alternatives are presented as mutually exclusive options. This is illustrated in (2b) from Hua (Haiman 1980:271). Here, _ito_ indicates that his being here and his not being here are mutually exclusive alternatives. UMR uses an abstract concept ```exclusive-disj``` to annotate this meaning, with numbered ```:opX``` roles for the construed alternatives.

Example 3-1-6 (2)

Example 3-1-6 (2a)
```
mnu'bo      hatai-supi'ba-ve    kire'bo kro-de-supi'ba-ve   egemo   bre-supi'ba-ve      degi    kiko-pi'    rmi-supamo  a-ki'       a'-vo-g-une
pandanus    bash-PURP.1PL-NONEX corn    husk-eat-PURP.1PL-NONEX banana  plant-PURP.1PL-NONEX    crazy   place-in    go_down-if.1PL  woman-with  not-sleep-fut-1PL.IND
'If we go down to a 'crazy place' to bash pandanus, husk and eat corn, or plant bananas, we don't sleep with women.'
(h / have-condition-91
   :ARG1 (a / a'vogune-00 'sleep'
    :actor (p / person
        :refer-person 1st
        :refer-number plural)
    :companion (a2 / aki' 'woman')
    :aspect habitual
    :modal-strength full-negative)
   :ARG2 (r / rmisupamo-00
    :actor p
    :goal (k / kikopi' 'place'
        :mod (d / degi))
    :purpose (i / inclusive-disj
        :op1 (h2 / hataisupi'bave-00 'bash'
            :actor p
            :undergoer (m / mnu'bo 'pandanus')
            :aspect performance
            :modal-strength full-affirmative)
        :op2 (k2 / krodesupi'bave-00 'husk and eat'
            :actor p
            :undergoer (k3 / kire'bo 'corn')
            :aspect performance
            :modal-strength full-affirmative)
        :op3 (b / bresupi'bave-00 'plant'
            :actor p
            :undergoer (e / egemo)
            :aspect performance
            :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative
   :aspect state)
```

Example 3-1-6 (2b)
```
bai-ve      ito 'a'-bai-e
be.3SG-INTERR   EX  NEG-be.3SG-IND
'Is he here or isn't he?'
(s1e / exclusive-disj
    :op1 (s1h / have-place-91
        :ARG1 (s1p / person
            :refer-person 3rd
            :refer-number singular)
        :ARG2 (s1p2 / place)
        :aspect state
        :modal-strength neutral-affirmative
        :mode Interrogative)
    :op2 (s1h2 / have-place-91
        :ARG1 s1p
        :ARG2 s1p2
        :aspect state
        :modal-strength neutral-negative
        :polarity -
        :mode Interrogative))
```

The exclusive disjunction relation has one further, more specific subtype:

```Apprehensive```: expresses that two events are mutually exclusive alternatives, but more specifically, that one event is carried out with the intention of preventing the other event from happening. It is in a way a negated counterpart of the `purpose` relation discussed below. In (3), the implication is that if the addressee of the imperative grabs a stick, they will not be attacked - the grab-event and the attack-event are mutually exclusive alternatives. As illustrated in (3), English has a dedicated subordinator to express apprehensive relations, but may also draw on its polysemous disjunctive coordinator, which has apprehensive as one of its functions. In the latter case, annotators may either use the higher-level category (the ```or``` abstract concept) in the lattice, or if they are confident, the lower-level category (using the ```:apprehensive``` relation. The same holds for many of the other fine-grained meanings discussed below - illustrative annotations will not be provided for all of them.

Example 3-1-6 (3)

Example 3-1-6 (3a)
```
Grab a stick lest he attack you!
(s1g / grab-01
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1s / stick
        :refer-number singular)
    :apprehensive (s1a / attack-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 s1p
        :aspect performance
        :modal-strength full-affirmative)
    :mode Imperative
    :aspect performance
    :modal-strength partial-affirmative)
```

Example 3-1-6 (3b)
```
Grab a stick or he will he attack you!
(s1g / grab-01
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1s / stick
        :refer-number singular)
    :apprehensive (s1a / attack-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 s1p
        :aspect performance
        :modal-strength full-affirmative)
    :mode Imperative
    :aspect performance
    :modal-strength partial-affirmative)

Or:
(s1o / or
    :op1 (s1g / grab-01
        :ARG0 (s1p / person
            :refer-person 2nd
            :refer-number singular)
        :ARG1 (s1s / stick
            :refer-number singular)
        :mode Imperative
        :aspect performance
        :modal-strength partial-affirmative)
    :op2 (s1a / attack-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 s1p
        :aspect performance
        :modal-strength full-affirmative))
```

```Additive```: expresses the addition of one “figure” (foregrounded participant or event) to another one in order to form a complex figure. This is represented in UMR through an ```additive``` abstract concept with numbered ```:opX``` roles. The additive function has a number of more fine-grained subfunctions:

```Simultaneous```: expresses full or partial temporal overlap of the events that together form a complex figure. This is illustrated in (4a) - the reading-event and the listening-event take place, at least in part, at the same time. This function is annotated at the sentence level using the ```:temporal``` participant role relation (see Part 3-2-1-1), and at the document level through the :overlap temporal relation (see Part 4-2-2).

```(pure) Addition```: expresses no temporal specification of the sequencing of events, but rather that the two events that form a complex figure cannot occur separately from each other in the context of the utterance. In (4b), having either your hand stamped or showing your ticket stub alone is not sufficient to get into the concert - both are necessary. UMR uses a ```:pure-addition``` relation to connect two events semantically related in this way.

```Substitution```: expresses that one of the events that together form a complex figure is offered as an “alternative” or “replacement” for the other – this is typically expressed through the negation of one of the two coordinands, as in (4c). The acceptability of both _and_ and _but_ here illustrates that the substitutive function is intermediate between the conjunctive and adversative higher-level categories (see below). Substitutive meanings are annotated with the ```:substitute``` relation, which takes the event being replaced as its child and the replacement event as its parent. The rejected alternative is annotated as `:ARG2`, while the replacement is annotated as `:ARG1`.

Example 3-1-6 (4)

Example 3-1-6 (4a)
```
I read a book while I listened to music. / I read a book while listening to music. / I read a book and listened to music.
(s1r / read-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1b / book
        :refer-number singular)
    :temporal (listen-01 :ARG0 s1p
        :ARG1 (s1m / music)
        :aspect state
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)

Or:
(s1a / and
    :op1 (s1r / read-01
        :ARG0 (s1p / person
            :refer-person 1st
            :refer-number singular)
        :ARG1 (s1b / book
            :refer-number singular)
        :aspect performance
        :modal-strength full-affirmative)
    :op2 (s1l / listen-01
        :ARG0 s1p
        :ARG1 (s1m / music)
        :aspect state
        :modal-strength full-affirmative))
```

Example 3-1-6 (4b)
```
In addition to having your hand stamped, you have to show your ticket to get into the concert. / You have to have your hand stamped and show your ticket stub to get into the concert.
(a / and
   :op1 (h / have-04
    :ARG0 (p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s / stamp-01
        :ARG0 (p2 / person)
        :ARG1 (h2 / hand
            :part-of p)
        :aspect performance
        :modal-strength partial-affirmative)
    :aspect performance
    :modal-strength partial-affirmative)
   :op2 (s2 / show-01
    :ARG0 p
    :ARG1 (t / ticket
        :possessor p
        :refer-number singular)
    :ARG2 (p3 / person)
    :aspect performance
    :modal-strength partial-affirmative)
   :purpose (g / get-05
    :ARG0 p
    :ARG2 (c / concert
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)

Or:
(s1h / have-04
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1s / stamp-01
        :ARG0 (s1p2 / person)
        :ARG1 (s1h / hand
            :part-of s1p)
        :aspect performance
        :modal-strength partial-affirmative)
    :aspect performance
    :modal-strength partial-affirmative
    :pure-addition (s1s2 / show
        :ARG0 s1p
        :ARG1 (s1t / ticket
            :possessor s1p
            :refer-number singular)
        :ARG2 (s1p3 / person)
        :aspect performance
        :modal-strength partial-affirmative)
    :purpose (s1g / get-05
        :ARG0 s1p
        :ARG2 (s1c / concert
            :refer-number singular)
        :aspect performance
        :modal-strength full-affirmative))
```

Example 3-1-6 (4c)
```
Instead of going out to eat, we barbecued chicken at home. / We didn’t go out to eat and/but barbecued chicken at home.
(b / barbecue-01
   :ARG0 (p / person
    :refer-person 1st
    :refer-number plural)
   :ARG1 (c / chicken)
   :place (h / home)
   :substitute (g / go_out-17
    :ARG0 p
    :purpose (e / eat-01
        :ARG0 p
        :aspect endeavor
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-negative
   :aspect performance
   :modal-strength full-affirmative

Or:
(s1a / and
    :op1 (s1g / go_out-17
        :ARG0 (s1p / person
            :refer-person 1st
            :refer-number plural)
        :purpose (s1e / eat-01
            :ARG0 s1p
            :aspect endeavor
            :modal-strength full-affirmative)
        :aspect performance
        :modal-strength full-negative)
    :op2 (s1b / barbecue-01
        :ARG0 s1p
        :ARG1 (s1c / chicken)
        :place (s1h / home)
        :aspect performance
        :modal-strength full-affirmative))
```

```Consecutive```: expresses two or more events as a complex figure, with additional information on their temporal and/or logical sequencing. Just like the ```additive``` meaning, this is represented in UMR through a ```consecutive``` abstract concept with numbered ```:opX``` relations. The temporal relations holding between the events can then be further specified in the document-level temporal annotation. More fine-grained sub-functions of the consecutive function are the following:

```Purpose```: expresses the intention on the part of the agent of one event towards bringing about another event, as in (5a). This relation is annotated using the `:purpose` participant role relation (see Part 3-2-1-1).

```Means```: expresses a relation where one event accompanies another and characterizes more specifically what happened (or didn't happen) in another event, as in (5b). This relation has also been called “positive circumstantial”. This relation is annotated using the `:manner` participant role relation (see Part 3-2-1-1).

```Causal```: expresses a relation between a causing event and a resulting event, where the former explicitly brings about the latter, as in (5c). This relation is annotated using the `cause-01` predicate or the `:cause` participant role relation (see Part 3-2-1-1).

```Conditional```: expresses a relation where one event is contingent upon the occurrence of another event, as in (5d). This relation is annotated using the `have-condition-91` predicate or the `:condition` participant role relation (see Part 3-2-1-1, Part 4-3-1-5).

```Anterior```: expresses that one event takes place before another. This can either be expressed through an adverbial construction with the earlier event in the main clause and the later event in a subordinate clause, or through iconicity of tense in coordinated clauses with the earlier event in the sequentially prior clause, all exemplified in (5e). This relation is annotated at the sentence level, using the `:temporal` participant role relation (see Part 3-2-1-1), and at the document level (see Part 4-2-2).

```Posterior```: expresses that one event takes place following another. This can either be expressed through an adverbial construction with the later event in the main clause and the earlier event in a subordinate clause, or through iconicity of tense in coordinated clauses with the later event in the sequentially later clause, all exemplified in (5f). This relation is annotated at the sentence level, using the `:temporal` participant role relation (see Part 3-2-1-1), and at the document level (see Part 4-2-2).

Example 3-1-6 (5a)
```
I grabbed a stick in order to defend myself. / I grabbed a stick and defended myself.
(s1g / grab-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1s / stick
        :refer-number singular)
    :purpose (s1d / defend
        :ARG0 s1p
        :ARG1 s1p
        :aspect performance
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (5b)
```
He got into the army by lying about his age. / He lied about his age and got into the army.
(s1g / get-5
    :ARG1 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s1a / army)
    :manner (s1l / lie-01
        :ARG0 s1p
        :ARG1 (s1t / thing
            :ARG2-of (s1a2 / age-01
                :ARG1 s1p))
        :aspect performance
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (5c)
```
Sarah moved back to California because she couldn't find a job in Washington. / Sarah couldn't find a job in Washington and (so) she moved back to California.
(s1m / move-01
    :ARG0 (s1p / person
        :name (s1n / name :op1 "Sarah))
    :ARG2 (s1s / state
        :name (s1n2 / name :op1 "California))
    :mod (s1b / back)
    :cause (s1f / find-01
        :ARG0 s1p
        :ARG1 (s1j / job)
        :place (s1s / state
            :name (s1n3 / name :op1 "Washington"))
        :aspect performance
        :modal-strength full-negative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (5d)
```
If you touch it, it might explode. / Touch it, and it might explode.
(s1e / explode-01
    :ARG1 (s1t / thing
        :refer-number singular)
    :condition (s1t2 / touch-01
        :ARG0 (s1p / person)
        :ARG1 s1t
        :aspect performance
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength neutral-affirmative)
```

Example 3-1-6 (5e)
```
I fed my dog before going to the office. / I fed my dog and went to the office.

(f / feed-01
    :ARG0 (p / person
        :refer-person 1st
        :refer-number singular)
    :ARG2 (d / dog
        :possessor p
        :refer-number singular)
    :temporal (b / before
        :op1 (g / go-01
            :ARG1 p
            :ARG4 (o / office
                :refer-number singular)
            :aspect performance
            :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (5f)
```
I went home after paying the check. / I paid the check and went home.
(g / go-01
    :ARG1 (p / person
        :refer-person 1st
        :refer-number singular)
    :ARG4 (h / home)
    :temporal (a / after
        :op1 (p2 / pay-01
            :ARG0 p
            :ARG3 (c / check)
            :aspect performance
            :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Together, the additive and consecutive functions and all their subfunctions can be subsumed under the higher-level, more coarse-grained conjunctive function, marked in UMR with the ```and``` abstract concept and numbered ```:opX``` roles. That these functions are all semantically related and that their conjoining under the higher-level function is appropriate is illustrated by _and_ being the English coordinator used to express all these functions when a complex-figure construal is chosen.

```(pure) Contrast```: expresses a relation of contrast in some way between events, without an element of unexpectedness. In (6a), properties attributed to Peter are contrasted with properties attributed to Vanja. Unlike with the “unexpected co-occurrence” relation below, there is no expectation that whenever two people are discussed and one of them is diligent, the other must be lazy. This meaning is annotated using the ```contrast-91``` abstract predicate and its numbered argument roles.

```Unexpected co-occurrence```: expresses a relation of juxtaposition between two events where the second event is unexpected in case the first occurs. For example, in (6b) from Russian (Malchukov 2004:180), it is unexpected that Vanja went to school given that she had a cold - the sentence implies, in other words, that people who have a cold usually do not go to school. UMR uses a ```unexpected-co-occurrence-91``` abstract concept with ```:ARG1``` and ```:ARG2``` roles to represent this meaning.

Example 3-1-6 (6)

Example 3-1-6 (6a)
```
Petja   staratel'nyi,   a   Vanja   lenivyj
Peter   diligent    CONJ    Vanja   lazy
'Peter is diligent, but [contrast] Vanja is lazy.'
(s1c / contrast-91
   :ARG1 (s1h / have-mod-91
    :ARG1 (s1p / person
        :name (s1n / name :op1 "Peter"))
    :ARG2 (s1s / staratel'nyi 'diligent')
    :aspect state
    :modal-strength full-affirmative)
   :ARG2 (s1h2 / have-mod-91
    :ARG1 (s1p2 / person
        :name (s1n2 / name :op1 "Vanja"))
    :ARG2 (s1l / lenivyj)
    :aspect state
    :modal-strength full-affirmative))
Glosses: lenivyj = 'lazy'
```

Example 3-1-6 (6b)
```
Vanja   prostudilsja,   no  poshël  v   shkolu
Vanja   caught_cold CONJ    went    to  school
'Vanja caught a cold, but [unexpected] went to school.'
(s1u / unexpected-co-occurrence-91
   :ARG1 (s1p / prostudilsja-00
    :experiencer (s1p2 / person
        :name (s1n / name :op1 "Vanja"))
    :aspect performance
    :modal-strength full-affirmative)
   :ARG2 (s1p3 / poshël-00
    :actor s1p2
    :goal (s1s / shkolu 'school)
    :aspect performance
    :modal-strength full-affirmative))
Glosses: prostudilsja-00 = 'catch a cold'; poshël-00 = 'go'
```

There are three subtypes of unexpected co-occurrence relations that confident annotators, or annotators for languages which have overt grammatical mechanisms of disambiguating them, may distinguish:

```Negative circumstantial```: expresses that the lack of occurrence of one event is a specific characterization of the other event, in the same way that the `means` relation discussed above expresses that the occurrence of one event is a specific characterization of another event. This meaning is classified as a subtype of “unexpected cooccurrence” because typically, the “more specific”, “characterizing” event that did not happen is only expressed overtly if the general expectation is that it _would_ happen. Compare the difference in naturalness between (7a) and (7b): the former sounds natural because we assume that, when carrying a bowl of punch, spills are a fairly common occurrence. The latter is not ungrammatical, but it implies that Sarah usually does a somersault whenever she carries bowls of punch. This relation is annotated using the `:manner` participant role relation (see Part 3-2-1-1), and a negative polarity attribute (see Part 3-3-3).

```Concessive```: expresses a relation between two events towards which the speaker has a positive epistemic stance (i.e. the speaker believes they both occurred/will occur), but specifies that this co-occurrence is unexpected. Concessives have also been treated as negative causal relations (Comrie 1986). For instance, in (7c), the speaker asserts that both the state of being broke and the guitar-buying event occurred in the real world. The concessive _even though_ specifies that typically being broke causes one to not buy new guitars. This relation is annotated using the ```have-concession-91``` predicate or the shortcut ```:concession``` relation (see Part 3-2-1-1, Part 4-3).

```Concessive conditional```: expresses that the state of affairs described in the apodosis will be true under the entire range of conditions described in the protasis. Concessive conditionals are different from regular conditionals in that they imply an expectation that the event expressed in the protasis may not lead to the event expressed in the apodosis happening. For instance, in (7d), there is an expectation that a mere five minutes of tardiness is not likely to cause one to be fired, and the concessive conditional contradicts this expectation: in the entire range of possible tardiness events, the event in the apodosis (being fired) will take place. This relation is annotated using the ```concessive-condition``` relation.

Example 3-1-6 (7)

Example 3-1-6 (7a)
```
Sarah carried the bowl of punch into the living room without doing a somersault. / Sarah carried the bowl of punch into the living room and/but didn't do a somersault.
(s1c / carry-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Sarah"))
    :ARG1 (s1p2 / punch
        :unit (s1b / bowl))
    :goal (s1r / room
        :mod (s1l / living))
    :manner (s1s / somersault
        :ARG0 s1p
        :aspect performance
        :polarity -
        :modal-strength full-negative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (7b)
```
Sarah carried the bowl of punch into the living room without spilling a drop. / Sarah carried the bowl of punch into the living room and/but didn't spill a drop.
(s1c / carry-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Sarah"))
    :ARG1 (s1p2 / punch
        :unit (s1b / bowl))
    :goal (s1r / room
        :mod (s1l / living))
    :manner (s1s / spill
        :ARG0 s1p
        :ARG1 s1p2
        :unit (s1d / drop)
        :aspect performance
        :polarity -
        :modal-strength full-negative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (7c)
```
Even though he was broke, he bought a new guitar. / He was broke, but (still) bought a new guitar.
(s1b / buy-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1g / guitar
        :mod (s1n / new)
        :refer-number singular)
    :concession (s1h / have-mod-91
        :ARG1 s1p
        :ARG2 (s1b2 / broke)
        :aspect state
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-1-6 (7d)
```
Even if you arrive only five minutes late, you will be fired.
(s1f / fire-02
    :ARG1 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative
    :concessive-condition (s1a / arrive-01
        :ARG1 s1p
        :temporal (s1l / late
            :extent (s1t / temporal-quantity
                :quant 5
                :unit (s1m / minute)))
        :aspect performance
        :modal-strength full-affirmative))
```

Lastly, the “(pure) contrast” meaning has a more fine-grained “subtraction” value, where one event is
additionally characterized by the absence of a second event that is normally a part of
the first event (Croft, to appear). UMR handles this meaning through a ```:subtraction``` relation that takes the absent second event as its child (see (8).

Example 3-1-6 (8)
```
People don't own tigers, except for Joe Exotic.
(s1o / own-01
    :polarity -
    :ARG0 (s1p / person
        :refer-person plural)
    :ARG1 (s1t / tiger
        :refer-number plural)
    :subtraction (s1p2 / person
        :name (s1n / name
            :op1 "Joe"
            :op2 "Exotic"))
    :aspect state
    :modal-strength full-negative)
```

Some languages co-express the “(pure) contrast” and the “unexpected co-occurrence” meanings, using the same form to express both. These two meanings are therefore subsumed under the `adversative` category on the lattice, annotated in UMR using the ```but-91``` abstract concept and ```:ARG1``` and ```:ARG2``` argument roles. However, both the “(pure) contrast” and the “unexpected co-occurrence meaning” may also be co-expressed with conjunctive meanings. Therefore, these categories combine into a number of higher-level, more coarse-grained categories on the UMR lattice above:

```And + unexpected```: abstract concept that may be used if a language does not formally distinguish conjuctive relations from unexpected co-occurrence relations. The language may still have a distinct form to express pure contrast. This abstract concept takes numbered ```:opX``` roles.

```And + contrast```: abstract concept that may be used if a language does not formally distinguish conjunctive relations from pure contrast relations. The language may still have a distinct form for expressing unexpected cooccurrence. This abstract concept takes numbered ```:opX``` roles.

```And + but```: abstract concept that may be used if a language does not formally distinguish between conjunctive relations and adversative relations at all. This abstract concept takes numbered ```:opX``` roles.

### Part 3-2. UMR relations

#### Part 3-2-1. Participant roles

Every entity and event identified as a participant is related to an
event (the event that it is dependent on) and annotated with a
participant role label. The participant role annotation is organized as a road map with different stages. The factor which
determines where a language begins on the road map is whether there is
an existing PropBank-style lexicon (frame files) for the language which defines predicate-specific roles. An English PropBank
frame file is shown in (1).

Example 3-2-1 (1)
```
Predicate: give.01
    Roles:
    Arg0: giver
    Arg1: thing given
    Arg2: entity given to
```
Following AMR, UMR uses PropBank frame files to annotate lexicalized
participant roles. But, this only works for languages which have
PropBank-style frame files. This is considered the ‘Stage 1’ participant
role annotation (see Part 3-2-1-2). The 'Stage 0' annotation involves
using a set of general participant roles, while building a lexicon of
PropBank-style frame files in order to move towards Stage 1 annotation.

Some types of valency alternations (or, argument structure alternations)
are indicated in the participant role annotation; other types of
alternations are not annotated in UMR. Not all valency alternations have
the same relationship between the basic construction and the non-basic
construction. Givón (1994) distinguishes semantic and pragmatic valency
alternations. In semantic alternations, the basic and non-basic
constructions differ in terms of the semantic content that they express,
i.e., they don’t refer to the same “real-world” event. Reciprocals are
an example of a semantic alternation, seen below in
(2) from Torau (Parkinson 2018:53).

Example 3-2-1 (2)

Example 3-2-1 (2a)
```
ta-di=lo    daki-a      tioni   arimi       ta  besu
PFV-3PL.S=go    find-3SG.O  man feel.sorry  3SG.PFV be.hungry
‘When they found him, the poor many was hungry.’
```

Example 3-2-1 (2b)
```
ta-di=lama  ari     da-daki     uua=i
PFV-3PL.S-TAM   REC RDP-find    in.that.direction=LOC
‘They had found each other.’
```

The event described in (2a) is different than the
event described in (2b) - in the former, the finder and findee are different, while in the latter they are the same. This is in contrast to
valency alternations which reflect a pragmatic difference between the
basic and non-basic construction. With pragmatic alternations, both
constructions refer to the same “real-world” event, but they package
that information differently, often in terms of the topicality (or,
discourse salience) of participants. Passive constructions are an
example of a pragmatic valency alternation, as seen in
(3) from Balinese (Shibatani and Artawa 2013).

Example 3-2-1 (3)

Example 3-2-1 (3a)
```
anak=e      muani   cenik   ento    ngajeng buah=e      ento
person=DEF  male    small   that    eat fruit=DEF   that
‘The boy ate the fruit.’
```
Example 3-2-1 (3b)
```
buah=e      ento    ajeng=a     teken   anak=e      muani   cenik   ento
fruit=DEF   that    eat=PASS    by  person=DEF  male    small   that
‘The fruit was eaten by the boy.’
```
Here, (3a) and (3b) could
refer to the same event, with the main difference being the saliency or
topicality of *anak=e muani cenik* ‘the boy’.

Broadly, UMR indicates semantic valency alternations with the
participant role annotation, while pragmatic alternations are not
reflected in the UMR. This means that the participant role annotations
for (2a) and (2b) would be
different, where as the participant role annotation for
(3a) and (3b) would be the
same. The annotations for valency alternations also depend on the stage
of the road map, which will be detailed in Part 3-2-1-1-2 and Part 3-2-1-2-1.

##### Part 3-2-1-1. Stage 0

At Stage 0, a set of general (i.e., non-lexicalized) semantic roles are
used. These certainly will not map exactly to the grammatical marking of
argument phrases in any language, but this set of roles was selected
based on cross-linguistic patterns of argument marking. The set of
participant role labels, a brief description for each label, and
examples are shown below in Table 9.

| **UMR Annotation** | **Definition** | **Example** |
|---|---|---|
| `actor` | animate entity that initiates the action | **the doctor** laughed **the boy** ate a salad |
| `undergoer` | entity (animate or inanimate) that is affected by the action | **the papers** burned he burned **the onions** |
| `theme` | entity (animate or inanimate) that moves from one entity to another entity, either spatially or metaphorically | she put **the books** on the shelf she tore **a page** from the book he gave **a sandwich** to me she told him **a story** |
| `recipient` | animate entity that gains possession (or at least temporary control) of another entity | he gave a sandwich **to me** she told **him** a story |
| `force` | inanimate entity that initiates the action | **the wind** knocked down the tree |
| `causer` | animate entity that acts on another animate entity to initiate the action | **the mother** made her child eat the broccoli |
| `experiencer` | animate entity that cognitively or sensorily experiences a `stimulus` | **the dog** heard a sound |
| `stimulus` | entity (animate or inanimate) that is experienced by an `experiencer` | the dog heard **a sound** |
| `instrument` | inanimate entity that is manipulated by an external causer in order to initiate the action | she hit him with **a broom** |
| `companion` | animate entity that acts with the `actor` to initiate the action | he cooked dinner with **his wife** |
| `material` | entity (inanimate) that is transformed into a new entity | he made a roux with **flour and butter** |
| `source` | entity from which the `theme` detaches | he plucked a flower from the **the bush** |
| `place` | location at which the action takes place | he read a book in **the garden** |
| `start` | location at which a motion event begins | she biked from **her house** |
| `goal` | location at which the action ends, the end point at which the `theme` arrives | she put the books on **the shelf** |
| `affectee` | animate entity which the action has a positive or negative influence on, i.e. beneficiary or maleficiary | he made a cake for **the dog** she stole a watch from **the CEO** |
| `cause` | inanimate entity that causes the action to happen | he was late because of **the fire** |
| `manner` | manner in which the action takes place | she exercised by **lifting weights** |
| `reason` | motivation for the `actor` to initiate the action | they got married because **they are in love** |
| `purpose` | intended event that results from the action | they dropped water in order to **fight the fires** |
| `temporal` | event that has a temporal relation with the action | she left after **dinner** |
| `extent` | measurement phrase | he ran **seven miles** |
| `other-role` | this role can be used when an annotator is unsure of which role is appropriate |  |

Table 9: UMR non-lexicalized roles

These general semantic roles can be categorized based on the types of events with which they occur, shown in Table 10. Participant roles that characterize the central participant(s) in an event only occur with a specific semantic class of event. For example, ```:experiencer``` and ```:stimulus``` participants only occur with experiential events. The other general participant roles that characterize central event participants are shown in the middle column below along with their associated semantic event class. Other general participant roles (shown in the first and third columns below) occur with a wide variety of semantic event classes. Those in the first column characterize causes external to the central event. Those in the third column label various roles that characterize the external circumstances of the event. Note that UMR uses ```:temporal``` to annotate temporal circumstantials of events, while ```:time``` is only used as a daughter of date-entity concepts to annotate hours and minutes on the clock.

| External Cause | Central Event | Circumstantial |
|---|---|---|
| `actor` | (CHANGE OF) STATE: ; `material, undergoer` | `affectee` |
| `companion` | (CHANGE OF) STATE: ; `material, undergoer` | `place` |
| `instrument` | MOTION/LOCATION: ; `theme, goal, start, source, place` | `manner` |
| `force` | MOTION/LOCATION: ; `theme, goal, start, source, place` | `purpose` |
| `causer` | TRANSFER: ; `theme, recipient` | `reason` |
| `cause` | TRANSFER: ; `theme, recipient` | `temporal` |
|  | EXPERIENTIAL: ; `experiencer, stimulus` | `extent` |

Table 10: Categorization of UMR non-lexicalized roles

For the roles that characterize the central participant(s) in the event,
the best way to decide which participant role label a given participant
should receive is to consider the semantic class of the event as specified in the middle column of table 10. The
```:undergoer``` role only occurs with
change-of-state events, construed broadly to include creation and
contact events as well. The ```:undergoer```
role is used for the entity that undergoes the change-of-state, is the
endpoint of force in a contact event, or is created in a creation event,
as seen in (1). The ```:material```
role only occurs with creation events, as in
(1c)), and is used for the raw materials
that are transformed into the created object.

Example 3-2-1-1 (1)

Example 3-2-1-1 (1a)
```
The ice cube melted.
(s1m / melt-01
    :undergoer (s1c / cube
        :material (s1i / ice)
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (1b)
```
The enemy sank the ship.
(s1s / sink-01
    :actor (s1e / enemy)
    :undergoer (s1s2 / ship
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (1c)
```
She built a house out of wood.
(s1b / build-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :undergoer (s1h / house
        :refer-number singular)
    :material (s1w / wood)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (1d)
```
He hit the stick against the fence.
(s1h / hit-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :instrument (s1s / stick
        :refer-number singular)
    :undergoer (s1f / fence
        :refer-number singular)
    :aspect endeavor
    :modal-strength full-affirmative)
```
The `:experiencer` and
`:stimulus` roles always occur with
experiential events, as seen in (4). The
`:experiencer` role is used for the
mental-level entity which attends to, reacts to, or passively
experiences the `:stimulus` role.

Example 3-2-1-1 (4)

Example 3-2-1-1 (4a)
```
The audience listened to the concerto.
(s1l / listen-01
    :experiencer (s1a / audience)
    :stimulus (s1c / concerto
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (4b)
```
The cat startled me.
(s1s / startle-01
    :experiencer (s1p / person
        :refer-person 1st
        :refer-number singular)
    :stimulus (s1c / cat
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
The `:start, :goal`, and
`:source` roles only occur with motion
events; `:place` has two different uses, one
with Motion/Location events and one with other event classes.
`:start`,
`:goal`, and
`:place` are used for locations –
`:start` is the location from which motion
originates, as in (5a),
`:goal` is the location in which motion
ends, as in (5b) and (5c),
and `:place` is used for static locations,
as in (5d). The
`:source` role is in the removal subclass of
motion events; it is used for the entity from which the
`:theme` is removed, as in
(5e). With motion events, the
`:theme` role is used for the entity that
moves (unless the motion is volitional), as in
(5a).

Example 3-2-1-1 (5)

Example 3-2-1-1 (5a)
```
She walked home from the store.
(s1w / walk-01
    :actor (s1p / person
        :refer-person 3rd
        ref-number Singular)
    :goal (s1h / home)
    :start (s1s / store)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (5b)
```
The leaf fell to the ground.
(s1f / fall-01
    :theme (s1l / leaf
        :refer-number singular)
    :goal (s1g / ground)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (5c)
```
He put the books in a box.
(s1p / put-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1b / book
        :refer-number plural)
    :goal (s1b2 / box
        :refer-number singular)
    :aspect: Performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (5d)
```
She is sitting on the couch.
(s1s / sit-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :place (s1c / couch
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (5e)
```
He picked some berries from the bush.
(s1p / pick-01
    :actor (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1b / berry
        :refer-number paucal)
    :source (s1b2 / bush
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
The `:recipient` role only occurs with
transfer events, or metaphorical transfer events like communication.
With these events, the initiator of the transfer is an
`:actor`, the entity that is transferred is
the `:theme` and the entity that the
`:theme` is transferred to is labelled as
the `:recipient`. For transfer of possession
events that express the original possessor of the
`:theme`, the original possessor is
annotated as `:affectee`, as in
(6d).

Example 3-2-1-1 (6)

Example 3-2-1-1 (6a)
```
He gave the cat some wet food.
(s1g / give-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1f / food
        :mod (s1w / wet)
        :quant (s1s / some))
    :recipient (s1c / cat
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-2-1-1 (6b)
```
I showed the pictures to her.
(s1s / show-01
    :actor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :theme (s1p2 / picture
        :refer-number plural)
    :recipient (s1p3 / person
        :refer-person 3rd
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-2-1-1 (6c)
```
She told me that they they’re attending.
(s1t / tell-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1a / attend-01
        :actor (s1p2 / person
            :refer-person 3rd
            :refer-number plural)
        :aspect activity
        :quote s1t
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-2-1-1 (6d)
```
She stole the information from a competitor.
(s1s / steal-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1i / information)
    :source (s1c / competitor
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

The other participant roles can occur pretty much freely with any semantic class of event. The external cause roles are used to annotate entities that bring about the central event. The
`:actor` role is used for “active”
single-participant events, in which the single participant acts
volitionally to bring about the event, as in
(7a). This contrasts with “inactive”
single-participant events, in which the single participant undergoes a
change outside of its control, as in (1a)
above. See Appendix 8 for examples of single-participant
verbs and their participant role annotation. The
`:actor` role is also used for animate
entities that initiate an action, as in (1b)
above.

The `:companion` role is used for the entity
that helps the `:actor` bring about the
action, as in (7b). Note that this role is only annotated when the `:companion`
participant is expressed separately from the
`:actor`. Plural participants and conjoined
participants, as in (7c) and
(7d), are annotated with a single
`:actor` role. In some languages, a marker
may be ambiguous between a comitative marker and a conjunction. When the two participants are expressed separately in the clause, they should be treated as separate participants, annotated with `:actor` and `:companion`. When they are expressed
together, they are treated as a single
`:actor` participant.

The `:instrument` role is used for an entity
that is manipulated by one of the other external cause roles, often an `:actor`, in order to initiate the action.
The entity which manipulates the
`:instrument` may or may not be present in
the clause; see (7e) and
(7f).

The `:force` role is used for inanimate physical
entities which initiate an action, or cause another entity to undergo a
change, as in (7g). Finally, the
`:causer` role is used for the external
initiator in some causative constructions, see 4.1.2.

Example 3-2-1-1 (7)

Example 3-2-1-1 (7a)
```
He winked.
(s1w / wink-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (7b)
```
Jane wrote the paper with Chris.
(s1w / write-01
    :actor (s1p / person
        :name (s1n / name
            :op1 "Jane"))
    :companion (s1p2 / person
        :name (s1n2 / name
            :op2 "Chris"))
    :undergoer (s1p3 / paper
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-2-1-1 (7c)
```
They wrote the paper.
(s1w / write-01
    :actor (s1p / person
        :refer-number plural)
    :undergoer (s1p2 / paper
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (7d)
```
Jane and Chris wrote the paper.
(s1w / write-01
    :actor (s1a / and
        :op1 (s1p / person
            :name (s1n / name :op1 "Jane"))
        :op2 (s1p2 / person
            :name (s1n2 / name :op1 "Chris)))
    :undergoer (s1p3 / paper
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (7e)
```
She sliced the bread with a knife.
(s1s / slice-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :instrument (s1k / knife
        :refer-number singular)
    :undergoer (s1b / bread
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (7f)
```
The knife sliced through the bread.
(s1s / slice-01
    :instrument (s1k / knife
        :refer-number singular)
    :undergoer (s1b / bread
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1 (7g)
```
The storm damaged the power lines.
(s1d / damage-01
    :force (s1s / storm
        :refer-number singular)
    :undergoer (s1l / line
        :purpose (s1p / power)
        :refer-number plural)
    :aspect performance
    :modal-strength full-affirmative)
```
See Table 9 above for examples of the circumstantial
roles. In addition, there is an `:other-role`
placeholder role that can be used when annotators are unsure of which participant role annotation is accurate for a particular participant. Also see Appendix 8 for a list of verbs and how their microroles are annotated.

At Stage 0, participant roles that aren’t explicitly expressed in the clause do not have to be annotated, even if they are implied by the context. If the annotator is certain about them, however, they can be annotated. For example, in (8), the
`:goal` is left implicit on the left-hand side but annotated on the right-hand side; at Stage 0, this
role may be left out of the annotation.

Example 3-2-1-1 (8)
```
They loaded the boxes.
(s1l / load-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :theme (s1b / box
        :refer-number plural)
    :aspect performance
    :modal-strength full-affirmative)

Or:
(s1l / load-01
    :actor (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :theme (s1b / box
        :refer-number plural)
    :goal (s1t / thing)
    :aspect performance
    :modal-strength full-affirmative)
```

###### Part 3-2-1-1-1. Non-verbal clauses

There is a small set of predicates that use lexicalized roles at all stages of the road map; therefore, frame files for these predicates are created at Stage 0 annotation. These are the non-verbal clause predicates presented above in Table 8, repeated below (see also Part 3-1-1-3 and Part 3-1-3-6). Each non-verbal clause predicate has a set of numbered argument roles which map to the semantic roles as shown in Table 8.

| Clause Type | Predicate | ARG1 | ARG2 | ARG3 | ARG4 | ARG5 |
|---|---|---|---|---|---|---|
| Thetic Possession | have-91 | possessor | possessum | --- | --- | --- |
| Predicative Possession | belong-91 | possessum | possessor | --- | --- | --- |
| Thetic Location | exist-91 | location | theme | --- | --- | --- |
| Predicative Location | have-place-91 | theme | location | --- | --- | --- |
| Property Predication | have-mod-91 | theme | property | --- | --- | --- |
| Object Predication | have-role-91 | theme | reference point | object category, arg1 | object category, arg2 | --- |
| Object Predication | have-org-role-92 | theme | organization | title of role | job description | --- |
| Object Predication | have-rel-role-92 | theme | relative | theme's role | relative's role | relationship basis |
| Equational | identity-91 | theme | equated referent | --- | --- | --- |

Table 8: Argument structure of non-verbal clause predicates

The argument that can be predicativized in languages using the predicativized-argument strategy is always
the argument role with the highest number. The examples in (1) show how
non-verbal clauses are annotated with participant roles. Note that these
annotations will be the same at every stage of the road map.

Example 3-2-1-1-1 (1)

Example 3-2-1-1-1 (1a)
Thetic/presentational Possession - Kukama

```
Mijiri-tin  ɨara-yara
Miguel-CER  canoe-owner
‘Miguel does have a canoe.’ (Lit. ‘Miguel is a canoe-owner’)

(s1h / have-91
    :ARG1 (s1p / person
        :name (s1n / name
            :op1 "Mijiri"))
    :ARG2 (s1i / ɨarayara
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
Glosses: ɨarayara = 'canoe'
```
Example 3-2-1-1-1 (1b) Predicative
Possession - English
```
The dog is the teacher's.

(s1b / belong-91
    :ARG1 (s1d / dog
        :refer-number singular)
    :ARG2 (s1p / person
        :refer-number singular
        :ARG0-of (s1t / teach-01))
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-2-1-1-1 (1c) Thetic/presentational Location - English
```
On the rock was a symbol.

(s1e / exist-91
    :ARG1 (s1r / rock
        :refer-number singular)
    :ARG2 (s1s / symbol
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-2-1-1-1 (1d) Predicative
Location - Yabem (Dempwolff 1939)
```
àndu  kê-kô     malac
house 3SG-be.at village
‘The house is in the village.’
(s1h / have-place-91
    :ARG1 (s1a / àndu
        :refer-number singular)
    :ARG2 (s1m / malac
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
Glosses: àndu = 'house'; malac = 'village'
```
Example 3-2-1-1-1 (1e) Property
Predication - English
```
The cat is black.
(s1h / have-mod-91
    :ARG1 (s1c / cat
        :refer-number singular)
    :ARG2 (s1b / black)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-2-1-1-1 (1f) Object Predication - Kukama
```
ajan kunumi     tsumi
this young.man  shaman
‘This young man is a shaman.’
(s1h / have-role-91
    :ARG1 (s1k / kunumi
        :mod (s1a / ajan)
        :refer-number singular)
    :ARG3 (s1t / tsumi)
    :aspect state
    :modal-strength full-affirmative)
Glosses: kunumi = 'young man'; ajan = 'this'; tsumi = 'shaman'
```
Example 3-2-1-1-1 (1g) Object Equational - English
```
She is the winner.
(s1i / identity-91
    :ARG1 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s1p2 / person
        :ARG0-of (s1w / win-01))
    :aspect state
    :modal-strength full-affirmative)
```

###### Part 3-2-1-1-2. Valency alternations

Information-packaging alternations, such as passives, antipassives, or valency-rearranging applicatives, are not reflected in the annotation. That is, participants are annotated in the same way as in the basic construction in the language. If a participant is omitted, for example the agent in a passive construction as in (1) from Berber (Guerssel 1986:52), then it doesn't need to be annotated at Stage 0. This means that agentless passives and anticausatives may have the same participant role annotation at Stage 0. Annotators may choose to annotate omitted participants that are semantically present at Stage 0.

Example 3-2-1-1-2 (1)

Example 3-2-1-1-2 (1a)
```
Y-usy       wrba    tafirast.
3M.SG-pick.up   boy:CST pear
‘The boy picked up the pear.’
(s1u / yusy-00
    :actor (s1w / wrba
        :refer-number singular)
    :undergoer (s1t / tafirast
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: yusy-00 = 'pick up'; wrba = 'boy'; tafirast = 'pear'
```

Example 3-2-1-1-2 (1b)
```
T-ttw-asy       tfirast.
3F.SG-DETR-pick.up  pear
‘The pear was picked up.’
(s1t / tttwasy-00
    :undergoer (s1t2 / tafirast
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: tttwasy-00 = 'pick up'; tafirast = 'pear'
```

Certain types of semantic valency alternations are reflected in the participant role annotation. At Stage 0, these alternations influence the choice of general participant role labels.

**Causatives.** There are a few different types of causatives that
require different annotation solutions. For most causatives of
transitives, the causer is annotated as
`:causer`, the causee as
`:actor`, and the rest of the participants
receive the same annotation labels that they would in a a non-causative
construction. In (2) from Kukama, *nai*
‘grandmother’ is annotated as `:causer`,
the causee *churan* ‘kid’ is annotated as
`:actor`, and *uni* ‘water’ as `:undergoer`.

Example 3-2-1-1-2 (2)
```
nai         kurata-ta   churan=ui   uni=pu
grandmother     drink-CAUS  kid=PST     water=INS
‘Grandmother made the kid drink the water.’
(s1k / kuratata
    :causer (s1p / person
        :ARG1-of (s1h / have-rel-role-92
            :ARG3 (s1n / nai))
        :refer-number singular)
    :actor (s1c / churan)
    :undergoer (s1u / uni)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: kuratata = 'make drink'; nai = 'grandmother'; churan = 'kid'; uni = 'water'
```

There are certain causatives of transitives which do not use the `:causer` role. These are constructions which express transfer events, including mental/cognitive transfer. Some
languages express these types of events with monomorphemic verbs, like English, but other languages use causatives of transitive verbs.
Languages may differ in terms of which types of causative constructions are construed as transfer; in order to annotate the same semantic events in the same way across languages, the `:actor, :theme, :recipient` roles are used for transfer of possession (giving), sending, and mental transfer, which includes showing and communication. Bezhta in (3b) (Comrie, Khalilov, Khalilova 2015:560) uses the causative of *b-egā-yo* ‘see’ as equivalent to English *show*.

Example 3-2-1-1-2 (3)

Example 3-2-1-1-2 (3a)
```
hogco-l     raɬad       b-egā-yo
he.OBL-LAT  sea(iii)    iii-see-PST
‘He saw the sea.’
(s1b / begāyo-00
    :experiencer (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :stimulus (s1r / raɬad)
    :aspect state
    :modal-strength full-affirmative)
Glosses: begāyo-00 = 'see'; raɬad = 'sea'
```
Example 3-2-1-1-2 (3b)
```
hogco       kibba-l     raɬad       b-ega-l-lo
he.OBL(ERG)     girl.OBL-LAT    sea(iii)    iii-see-CAUS-PST
‘He showed the sea to the girl.’
(s1b / begallo-00
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :theme (s1r / raɬad)
    :recipient (s1k / kibba
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
Glosses: begallo-00 = 'show'; raɬad = 'sea'; kibba = 'girl'
```

For causatives of ditransitives, the causer receives the
`:causer` role, the causee the `:actor` role, and the other participants receive the same annotation as in a non-causative construction. This can be seen in (4) from Shipibo-Konibo
(Valenzuela 2003:612). If ‘the man’ was expressed in the clause, that participant would be annotated as `:recipient`.

Example 3-2-1-1-2 (4)
```
Ja-tian     ja  xontako         jawen   tita-n      xoi             meni-ma-\[a\]i  keen-yama-\[a\]i-bi...
that-TEMP   that    unmarried.girl:ABS  POS3    mother-ERG  roasted.meat/fish:ABS   give-CAUS-INC   want-NEG-SDS-EM
‘Then her mother makes the unmarried girl give roasted meat/fish (to the
man who had asked her in matrimony) even though she doesn’t want to...’
(s1m / menima-00
    :causer (s1p / person
        :ARG1-of (s1h / have-rel-role-92
            :ARG2 (s1x / xontako
                :mod (s1j / ja)
                :refer-number singular)
            :ARG3 (s1t / titan))
            :refer-number singular)
    :actor s1x
    :theme (s1x2 / xoi)
    :temporal (s1j2 / jatian)
    :concession (s1k2 / keenyamaaibi-00
        :experiencer s1x
        :stimulus (m)
        :aspect state
        :modal-strength full-negative)
    :aspect habitual
    :modal-strength full-affirmative)
Glosses: menima-00 = 'make give'; xontako = 'unmarried girl'; ja = 'that'; titan = 'mother'; xoi = 'roasted meat/fish'; jatian = 'that time'; keenyamaaibi-00 = 'want'
```

There are two types of causatives of intransitives, based on the two types of intransitives. For intransitives whose single participant corresponds to an `:undergoer` role, such as
change-of-state verbs in many languages, the causer is annotated as `:actor` and the single participant retains
its `:undergoer` label. This can be seen in
(5) from Falam Chin (King 2011:195) below.

Example 3-2-1-1-2 (5)

Example 3-2-1-1-2 (5a)
```
Ka  kedam   hri a   cat.
1SG     shoe    string  3SG.NOM broken.1
‘My shoelace is broken/broke.’
(s1c / cat-00
    :undergoer (s1h / hri
        :part-of (s1k / kedam)
        :possessor (s1p / person
            :refer-person 1st
            :refer-number singular)
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
Glosses: cat-00 = 'broken'; hri = 'string'; kedam = 'shoe'
```

Example 3-2-1-1-2 (5b)
```
Thangte in  ka  kedam   hri     a   cat-ter.
Thangte ERG     1SG     shoe    string  3SG.NOM broken.1-CAUS
‘Thangte broke my shoelace.’
(c / catter-00
    :actor (p / person
        :name (n / name :op1 "Thangte"))
    :undergoer (h / hri
        :part-of (k / kedam)
        :possessor (p2 / person
            :refer-person 1st
            :refer-number singular)
        :refer-number singular
    :aspect performance
    :modal-strength full-affirmative)
```

Regardless of whether the causative or anticausative verb is derived (or if neither is derived), the anticausative/intransitive meaning is annotated with a single `:undergoer` participant and the causative/transitive meaning is annotated with an
`:actor` and an `:undergoer` participant.

When the single participant of the intransitive corresponds to the
`:actor` role, then the causer receives the `:causer` annotation and the single participant retains its `:actor` label. This
can be seen in (6) from Falam Chin (King 2011:195) below.

Example 3-2-1-1-2 (6)

Example 3-2-1-1-2 (6a)
```
Cinte a     hni.
Cinte 3SG.NOM   laugh.1
‘Cinte laughed.’
(s1h / hni-00
    :actor (s1p / person
        :name (s1n / name
            :op1 "Cinte"))
    :aspect endeavor
    :modal-strength full-affirmative)
Glosses: hni-00 = 'laugh'
```
Example 3-2-1-1-2 (6a)
```
Parte   in  Cinte a     hni-ter.
Parte   ERG     Cinte 3SG.NOM   laugh.1-CAUS
‘Parte made Cinte laugh.’
(s1h / hniter-00
    :causer (s1p / person
        :name (s1n / name
            :op1 "Parte"))
    :actor (s1p2 / person
        :name (s1n2 / name
            :op1 "Cinte"))
    :aspect performance
    :modal-strength full-affirmative)
Glosses: hniter-00 = 'make laugh'
```

**Applicatives.**  Peterson (2007) distinguishes between “valency-increasing” applicatives and “valency-rearranging” applicatives. In valency-rearranging applicatives, a participant is expressed as an oblique in the basic construction and expressed as a core argument in the applicative construction; they are generally associated with the increased saliency or topicality of the oblique participant. Therefore, these fit into the category of pragmatic valency alternations, and both the basic and applicative construction receive the same participant role
annotation. This can be seen in
(7) from Falam Chin (King 2011:240).

\-2-1-1-2 (7)

Example 3-2-1-1-2 (7a)
```
Parte in    Thangte hrang=ah    hmeh    a   suang.
Parte ERG   Thangte for=LOC     curry   3SG.NOM cook.1
‘Parte cooked some curry for Thangte.’
(s1s / suang-00
    :actor (s1p / person
        :name (s1n / name
            :op1 "Parte"))
    :undergoer (s1h / hmeh)
    :affectee (s1p2 / person
        :name (s1n2 / name
            :op2 "Thangte"))
    :aspect performance
    :modal-strength full-affirmative)
Glosses: suang-00 = 'cook'; hmeh = 'curry'
```
Example 3-2-1-1-2 (7b)
```
Parte in    Thangte hmeh    a   suan-sak
Parte ERG   Thangte curry   3SG.NOM cook.2-BEN
‘Parte cooked Thangte some curry.’
(s1s / suangsak-00
    :actor (s1p / person
        :name (s1n / name
            :op1 "Parte"))
    :undergoer (s1h / hmeh)
    :affectee (s1p2 / person
        :name (s1n2 / name
            :op1 "Thangte"))
    :aspect performance
    :modal-strength full-affirmative)
Glosses: suangsak-00 = 'cook for'; hmeh = 'curry'
```
Example 3-2-1-1-2 (7c)
```
as-teny-aye'    pa'ang
1SG-buy-DECL    palm
‘I bought palm hearts.’
(s1t / entenyay'a-00
    :actor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :theme (s1p2 / pa'ang 'palm)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-1-2 (7d)
```
as-teny-as-ke'      pa'ang  ap-angkok   Eduardo
1SG-buy-APPL-DECL   palm    2/3M-POSS   Eduardo
‘I bought palm hearts from Eduardo.’
(s1t / entenyaskama-00
    :actor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :theme (s1p2 / pa'ang 'palm)
    :source (s1p3 / person
        :name (s1n / name :op1 "Eduardo"))
    :aspect performance
    :modal-strength full-affirmative)
```

Whether the beneficiary, *Thangte*, is expressed as an oblique or a core argument, it is annotated as `:affectee`. Valency-increasing applicatives involve the addition of a participant, compared to the basic construction. Here, the added participant is
simply annotated with the appropriate semantic role. This can be seen in (7c)-(7d) from Sanapaná.

**Reflexives & Reciprocals** For reflexive and reciprocal constructions, the single participant is annotated with both of the semantic role labels which it is fulfilling in the construction. This can be seen in (8a) and (8b) from Supyire (Carlson 1994:416-7).

Example 3-2-1-1-2 (8)

Example 3-2-1-1-2 (8a)
```
U   a   ù-yé    bánì
he  PERF    he-REFL wound
‘He has wounded himself.’
(s1b / bánì-00
    :actor (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :undergoer s1p
    :aspect performance
    :modal-strength full-affirmative)
Glosses: bánì-00 = 'wound'
```
Example 3-2-1-1-2 (8b)
```
Pi  a   pì-yé       kánù
they    PERF    they-REFL   love
‘They loved each other.’
(s1k / kánù-00
    :actor (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :undergoer s1p
    :aspect state
    :modal-strength full-affirmative)
Glosses: kánù-00 = 'love'
```

The annotation of participant roles for valency alternations in Step 1 of the road map is summarized in Table 11 below.

| **Valency Alternation** | **Which participants to annotate** | **Which participant roles** |
|---|---|---|
| Passives | Every overt participant | Same as in basic construction |
| Anticausatives | Every overt participant | Same as in basic construction |
| Valency-rearranging applicatives | Every overt participant | Same as in basic construction |
| Causatives of transitives | Every overt participant | `:causer`, `:actor`, other participants same as in basic construction |
| Transfer events expressed as causatives | Every overt participant | `:actor`, `:theme`, `:recipient` |
| Causatives of ditransitives | Every overt participant | `:causer`, `:actor`, `:theme`, `:recipient` |
| Causatives of inactive intransitives | Every overt participant | `:actor`, `:theme` |
| Causatives of active intransitives | Every overt participant | `:causer`, `:actor` |
| Valency-increasing applicatives | Every overt participant | Same as in basic construction, appropriate role for new participant |
| Reflexives | A single participant with two roles | Both roles the participant fulfills in the construction |
| Reciprocals | A single participant with two roles | Both roles the participant fulfills in the construction |

Table 11: Argument structure of valency alternations

##### Part 3-2-1-2. Stage 1

The Stage 1 participant role annotation requires access to
PropBank-style frame files in the language for a large number of
predicates. At this stage, each predicate identified as an event is linked
to its corresponding frame file. The participants dependent on that
event are annotated with the lexicalized roles, as determined by the
frame file. This can be seen in (1) below.

```
predicate: tease-02
    roles:
    ARG0: teaser
    ARG1: teased
    ARG2: about what
```

Example 3-2-1-2 (1)

```
He teased the boy about his hat.

(s1t / tease-02
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1b / boy
        :refer-number singular)
    :ARG2 (s1h / hat
        :possessor s1b)
    :aspect endeavor
    :modal-strength full-affirmative)
```

Since the non-verbal clause functions require the use of lexicalized predicates at Stage 0, these are annotated in the same way at Stage 1 (see Part 3-2-1-1-1). Unlike Stage 0, implicit participants are
annotated for their semantic role at Stage 1. This is shown in
(2).

Example 3-2-1-2 (2)
```
She parked the truck in the driveway. They loaded the boxes.

(s1p / park-01
    :ARG0 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1t / truck
        :refer-number singular)
    :ARG2 (s1d / driveway)
    :aspect performance
    :modal-strength full-affirmative)

(s2l / load-01
    :ARG0 (s2p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s2t / thing)
    :ARG2 (s2b / box
        :refer-number plural)
    :aspect performance
    :modal-strength full-affirmative)
(s2s0 / sentence
    :temporal (document-creation-time :before s2l)
    :modal (author :full-affirmative s2l)
    :coref (s1t :same-entity s2t))
```

The second sentence in (2) does not
include explicit mention of the truck, but it is understood from the
context that the truck is the goal participant of the loading event. Therefore, an implicit 'thing' participant is identified for the ```:ARG1``` role of the loading event at Stage 1. In the document-level annotation, this participant is then flagged as coreferential with the truck in the previous sentence.

###### Part 3-2-1-2-1. Valency alternations

The approach to valency alternations at Stage 1 is largely the same as
that detailed for Stage 0 in Part 3-2-1-1-2. However, at Stage 1,
predicates with valency-changing morphology should have their own frame
files with lexicalized arguments. Therefore, the annotation of
participant roles for valency alternations is the same as that for other
types of predicates. The predicate is matched with its frame files and
the participants are annotated accordingly with numbered argument roles rather than predicate-general ones.

##### Part 3-2-1-3. Inverse participant roles

AMR, the predecessor of UMR, makes use of **inverse** participant roles for a number of different purposes, such as the annotation of events that function as modifiers of referring expressions (typically relative clauses or participles, see Part 3-1-1-2), the annotation of embedded interrogatives, and the annotation of participant nominalizations. These three uses of inverse participant roles are illustrated in (1). The use of, for example, the `:ARG1-of` relation in (1a), which is the inverse of the numbered argument role `:ARG1`, allows us to maintain a single-rooted graph structure by embedding the *see*-event underneath the participant it modifies (*sweater*). Such event concept nodes which are linked to other concepts by means of inverse participant roles can then further take their own full argument structure annotation and attribute values for e.g. aspect. Such inverses of numbered argument roles also allow us to make use of PropBank framefiles as much as possible: by annotating *runner* in (1c) as `(p / person :ARG0-of r/ run-02)`, we can directly link this annotation to the existing lexicon rather than having to enter an ad-hoc object concept node `(r / runner)`.

Example 3-2-1-3 (1)

Example 3-2-1-3 (1a)
```
I bought the sweater that you saw.
(s1b / buy-0101
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1s / sweater
        :ARG1-of (s1s2 / see-01
            :ARG0 (s1p2 / person
                :refer-person 2nd
                :refer-number singular)
            :aspect state
            :modal-strength full-affirmative)
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

Example 3-2-1-3 (1b)
```
I didn't see whether he bought the sweater.
(s1s / see-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1t / truth-value
        :Polarity-of (s1b / buy-01
            :ARG0 (s1p2 / person
                :refer-person 3rd
                :refer-number singular)
            :ARG1 (s1s2 / sweater
                :refer-number singular)
            :aspect performance
            :modal-strength neutral-affirmative))
    :aspect state
    :Modstr full-negative)
```

Example 3-2-1-3 (1c)
```
The runner was wearing a sweater.
(s1w / wear-01
    :ARG0 (s1p / person
        :ARG0-of (s1r / run-02)
        :refer-number singular)
    :ARG1 (s1s / sweater
        :refer-number singular)
    :aspect state
    :modal-strength full-affirmative)
```

UMR expands upon this AMR system of inverse relations by adding inverses for the general (i.e. non-predicate-specific) participant roles to be used at stage 0 of the road map. So, in addition to having inverses of numbered participant roles, there are now also `:actor-of` and `:undergoer-of` roles, and analogues for each of the general participant roles described in table 9 in Part 3-2-1-1). Example (2) below illustrates the use of the inverse `:Stimulus-of` role to annotate the same relative clause as in (1a) above.

Example 3-2-1-3 (2)

```
I bought the sweater that you saw.
(s1b / buy-01
    :actor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :theme (s1s / sweater
        :Stimulus-of (s1s2 / see-01
            :experiencer (s1p2 / person
                :refer-person 2nd
                :refer-number singular)
            :aspect state
            :modal-strength full-affirmative)
        :refer-number singular)
    :aspect performance
    :modal-strength full-affirmative)
```

One more context in which inverse participant roles are used is in the annotation of certain relations that are mostly thought of (and mostly expressed in languages) as nominal modification - specifically, kinship relations and certain other relational nouns, e.g. those designating functions within organizations. For the annotation of noun phrases like *my father*, or *the President of the University of New Mexico*, UMR uses a `(p / person)` concept node as the top of the graph, connected with an inverse participant role to a non-verbal clause predicate (which can then take further argument roles to express other elements in the NP). The most general, coarse-grained non-verbal clause predicate to be used in such annotations is `have-role-91`, although more specific predicates (e.g. `have-rel-role-92, have-org-role-92`) for frequently encountered concrete relation types are also available. The rolesets used for their arguments are detailed in Part 3-1-3-5). The use of these predicates in such annotations is illustrated in (3).

Example 3-2-1-3 (3)

Example 3-2-1-3 (3a)
```
I met my father.
(s1m / meet-03
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1p2 / person
        :ARG1-of (s1h / have-rel-role-92
            :ARG2 s1p
            :ARG3 (s1f / father)))
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-1-3 (3a)
```
I met the President of the University of New Mexico.
(s1m / meet-03
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1p2 / person
        :ARG1-of (s1h / have-org-role-92
            :ARG2 (s1a / academic_organization
                :name (s1n / name
                    :op1 "University
                    :op2 "of"
                    :op3 "New"
                    :op4 "Mexico")
)
            :ARG2 (s1p3 / president)))
    :aspect performance
    :modal-strength full-affirmative)
```

##### Part 3-2-1-4. Table of verb meanings

Table 12 below contains the general participant role annotation for the microroles associated with 89 verb meanings. The verb meanings and microroles are from the Valency Patterns Leipzig project (ValPaL; Hartmann et al. 2013). For two verb meanings, WIPE and PEEL, the ValPaL data reflects distinct verb senses: a motion sense (ex: She wiped the crumbs from the table) and a change-of-state (COS) sense (ex: He wiped the table).

As mentioned in Part 3-2-1-1, the single participant in a monovalent event can either be annotated as `actor` or as `undergoer`. This distinction depends on the amount of control that the single participant has in carrying out the event. For events that are more controlled by the participant ("active" events), the participant is annotated as `actor`; for events that are less controlled by the participant ("inactive" events), the participant is annotated as `undergoer`. Languages that reflect this distinction in their morphosyntax (i.e., languages with active alignment) do not always draw the distinction between active events and inactive events in the same place. There is, however, a cross-linguistic organization in terms of how languages with active alignment code these events in their morphosyntax.

The following semantic event classes reflect an ordering from most active to most inactive (Croft 2012; 2022).

Controlled activities (ex: run)
Position events (ex: hang)
Inherent properties (ex: short)
Bodily actions (ex: cough)
Change of state (ex: become ill)
Transitory properties (ex: be ill)
Uncontrolled activities (ex: fall)

For the purposes of UMR, controlled activities, position events, inherent properties, and more controlled types of bodily actions (ex: laugh) are annotated with an `actor` participant. Less controlled types of bodily actions (ex: cry) and the remaining semantic event classes are annotated with an `undergoer` participant.

Annotators may use Table 12 as a reference point for annotating general participant roles for various semantic verb classes.

| Verb Meaning | Microrole | UMR annotation |
|---|---|---|
| Active (A-like) S | Active (A-like) S | Active (A-like) S |
| RUN | runner | `actor` |
| CLIMB | climber | `actor` |
| CLIMB | climbing goal | `undergoer` |
| JUMP | jumper | `actor` |
| GO | goer | `actor` |
| GO | going goal | `goal` |
| LEAVE | leaver | `actor` |
| LEAVE | left place/person | `source` |
| SIT DOWN | sit downer | `actor` |
| SIT DOWN | sitting-down place | `goal` |
| DIG | digger | `actor` |
| PLAY | player | `actor` |
| SING | singer | `actor` |
| SIT | sitter | `actor` |
| SIT | sitting place | `place` |
| LIVE | liver | `actor` |
| LIVE | living place | `place` |
| LAUGH | laugher | `actor` |
| BLINK | blinker | `actor` |
| COUGH | cougher | `actor` |
| Inactive (P-like) S | Inactive (P-like) S | Inactive (P-like) S |
| CRY | crier | `undergoer` |
| DIE | dieer | `undergoer` |
| SINK | sunken entity | `undergoer` |
| BURN | burnt thing | `undergoer` |
| BOIL | boiled thing | `undergoer` |
| BE SAD | sad person | `undergoer` |
| BE HUNGRY | hungry person | `undergoer` |
| BE DRY | dry thing | `undergoer` |
| BE ILL | sick person | `undergoer` |
| ROLL | rolling entity | `undergoer` |
| FALL | fallee | `undergoer` |
| RAIN | rain | `undergoer` |
| Inherent Reflexive/Reciprocal | Inherent Reflexive/Reciprocal | Inherent Reflexive/Reciprocal |
| DRESS | dresser | `actor` |
| DRESS | dressee | `undergoer` |
| SHAVE (a body part) | shaver (of body part) | `actor` |
| SHAVE (a body part) | shaved body part | `undergoer` |
| WASH | washer | `actor` |
| WASH | washed entity | `undergoer` |
| HELP | helper | `actor` |
| HELP | helpee | `undergoer` |
| FOLLOW | follower | `actor` |
| FOLLOW | followee | `undergoer` |
| MEET | meeter | `actor` |
| MEET | met person | `undergoer` |
| HUG | hugger | `actor` |
| HUG | huggee | `undergoer` |
| Change-of-State | Change-of-State | Change-of-State |
| BREAK | breaker | `actor` |
| BREAK | broken thing | `undergoer` |
| BREAK | breaking instrument | `instrument` |
| KILL | killer | `actor` |
| KILL | killee | `undergoer` |
| KILL | killing instrument | `instrument` |
| BEAT | beater | `actor` |
| BEAT | beatee | `undergoer` |
| BEAT | beating instrument | `instrument` |
| CUT | cutter | `actor` |
| CUT | cut thing | `undergoer` |
| CUT | cutting instrument | `instrument` |
| GRIND | grinder | `actor` |
| GRIND | ground thing | `undergoer` |
| COOK | cooker | `actor` |
| COOK | cooked food | `undergoer` |
| EAT | eater | `actor` |
| EAT | eaten food | `undergoer` |
| DRINK | drinking person | `actor` |
| DRINK | drunken thing | `undergoer` |
| COVER | coverer | `actor` |
| COVER | cover | `instrument` |
| COVER | covered thing | `undergoer` |
| FILL | filler | `actor` |
| FILL | filling material | `instrument` |
| FILL | filled container | `undergoer` |
| WIPE (cos) | wiper | `actor` |
| WIPE (cos) | wiped surface | `undergoer` |
| PEEL (cos) | peeler | `actor` |
| PEEL (cos) | peeled object | `undergoer` |
| Contact | Contact | Contact |
| HIT | hitter | `actor` |
| HIT | hittee | `undergoer` |
| HIT | hitting instrument | `instrument` |
| TOUCH | toucher | `actor` |
| TOUCH | touchee | `undergoer` |
| TOUCH | touching instrument | `instrument` |
| PUSH | pusher | `actor` |
| PUSH | pushee | `undergoer` |
| Experiential | Experiential | Experiential |
| LOOK AT | looker | `experiencer` |
| LOOK AT | looked at entity | `stimulus` |
| SEE | seeer | `experiencer` |
| SEE | seen entity | `stimulus` |
| APPEAR | appearer | `stimulus` |
| SMELL | smeller | `experiencer` |
| SMELL | smelled entity | `stimulus` |
| HEAR | hearer | `experiencer` |
| HEAR | heard sound | `stimulus` |
| FEAR | fearer | `experiencer` |
| FEAR | fear stimulus | `stimulus` |
| FRIGHTEN | frightenee | `experiencer` |
| FRIGHTEN | frightener | `stimulus` |
| LIKE | liker | `experiencer` |
| LIKE | liked entity | `stimulus` |
| KNOW | knower | `experiencer` |
| KNOW | known thing/person | `stimulus` |
| THINK | thinker | `experiencer` |
| THINK | thought content | `stimulus` |
| WANT | wanter | `experiencer` |
| WANT | wanted thing | `stimulus` |
| FEEL PAIN | pain-feeler | `experiencer` |
| FEEL PAIN | pain locus | `stimulus` |
| Partly-unrealized | Partly-unrealized | Partly-unrealized |
| SEARCH FOR | searcher | `actor` |
| SEARCH FOR | searched thing | `undergoer` |
| HUNT (FOR) | hunter | `actor` |
| HUNT (FOR) | hunted thing | `undergoer` |
| Application | Application | Application |
| PUT | putter | `actor` |
| PUT | put thing | `theme` |
| PUT | putting goal | `goal` |
| POUR | pourer | `actor` |
| POUR | poured substance | `theme` |
| POUR | pouring goal | `goal` |
| LOAD | loader | `actor` |
| LOAD | loaded thing | `theme` |
| LOAD | loading place | `goal` |
| TIE | tier | `actor` |
| TIE | tied thing | `theme` |
| TIE | tying goal | `goal` |
| Removal | Removal | Removal |
| TAKE | taker | `actor` |
| TAKE | taken thing | `theme` |
| TAKE | taking source | `source` |
| TEAR | tearer | `actor` |
| TEAR | torn thing | `theme` |
| TEAR | tearing source | `source` |
| WIPE (motion) | wiper | `actor` |
| WIPE (motion) | wiped material | `theme` |
| WIPE (motion) | wiped surface | `source` |
| PEEL (motion) | peeler | `actor` |
| PEEL (motion) | peel | `theme` |
| PEEL (motion) | peeled object | `source` |
| Creation | Creation | Creation |
| BUILD | builder | `actor` |
| BUILD | built thing | `undergoer` |
| BUILD | building material | `instrument` |
| MAKE | maker | `actor` |
| MAKE | made thing | `undergoer` |
| Transfer | Transfer | Transfer |
| GIVE | giver | `actor` |
| GIVE | gift | `theme` |
| GIVE | giving recipient | `recipient` |
| SEND | sender | `actor` |
| SEND | sent thing | `theme` |
| SEND | sending recipient | `recipient` |
| CARRY | carrier | `actor` |
| CARRY | carried thing | `theme` |
| CARRY | carrying goal | `goal` |
| THROW | thrower | `actor` |
| THROW | thrown thing | `theme` |
| THROW | throwing goal | `goal` |
| BRING | bringer | `actor` |
| BRING | brought thing | `theme` |
| BRING | bringing recipient | `recipient` |
| STEAL | stealer | `actor` |
| STEAL | stolen thing | `theme` |
| STEAL | stealing source | `affectee` |
| GET | receiver | `recipient` |
| GET | received thing | `theme` |
| Communication | Communication | Communication |
| TALK | talker | `actor` |
| TALK | talked about content | `theme` |
| TALK | talked to person | `recipient` |
| ASK FOR | asker | `actor` |
| ASK FOR | requested thing | `theme` |
| ASK FOR | askee | `recipient` |
| SHOUT AT | shouter | `actor` |
| SHOUT AT | shoutee | `recipient` |
| TELL | teller | `actor` |
| TELL | told content | `theme` |
| TELL | tellee | `recipient` |
| SHOW | shower | `actor` |
| SHOW | shown thing | `theme` |
| SHOW | showing addressee | `recipient` |
| HIDE | hider | `actor` |
| HIDE | hidden thing | `theme` |
| HIDE | hiding affectee | `affectee` |
| SCREAM | screamer | `actor` |
| TEACH | teacher | `actor` |
| TEACH | taught content | `theme` |
| TEACH | teachee | `recipient` |
| SAY | sayer | `actor` |
| SAY | said content | `theme` |
| SAY | saying addressee | `recipient` |
| NAME | namer | `actor` |
| NAME | name | `theme` |
| NAME | namee | `recipient` |

Table 12: Verb meanings and non-lexicalized role annotation

#### Part 3-2-2. Non-participant role UMR relations

Apart from predicate-specific and general participant roles, UMR also has a set of relations that are mainly used to mark NP-internal relations, to mark some types of modifiers of predicates, and to make the meanings of certain natural language expressions computationally tractable. Most of those relations are inherited from AMR, but for some of them, there are some changes in their use.

##### Part 3-2-2-1. Temporal relations

Some relations are used to describe entities in a standard, canonical form. This is the case for ```:calendar, :century, :day, :dayperiod, :decade, :era, :month, :quarter, :season, :time, :timezone, :weekday, :year,``` and ```:year2```. The use of these relations is exemplified in (1).

Example 3-2-2-1 (1)

Example 3-2-2-1 (1a)
```
March 23rd, 2021
(s1d / date-entity
    :year 2021
    :month 3
    :day 23)
```
Example 3-2-2-1 (1b)
```
Friday the 13th
(s1d / date-entity
    :weekday (s1f / Friday)
    :day 13)
```
Example 3-2-2-1 (1c)
```
3.30 pm Albuquerque time
(s1d / date-entity
    :time 15:30
    :timezone (s1z / MST))
```

##### Part 3-2-2-2. Modifiers

Other relations mostly function to modify object concepts - they are often expressed in languages as modifiers of some sort within an NP. Semantically, modification relations in referring expressions come in two kinds: anchoring and typifying (Croft, to appear). Anchoring modifiers "situate the intended referent of the referring expression via reference to another object", in other words, they provide referential grounding for a referent expression. Many anchoring modification relations are construed in languages as possessive relations: ownership (which situates a referent via reference to its owner), part-whole relations (which situate a referent via reference to a larger entity it is a part of), and kinship relations (which situate a referent via reference to another person that has a particular kind of relation to them). As described in Part 3-2-1-3, kinship relations are annotated through the `have-rel-role-92` predicate, even when they are not predicated. For ownership and part-whole relations, UMR uses `:possessor` and `:part-of` relations with the possessum or part as the parent and the possessor or whole as the daughter, as in (1). When the whole is the parent and the part the daughter, the relation is `:part`.

Example 3-2-2-2 (1)

Example 3-2-2-2 (1a)

```
John's car
(s1c / car
    :possessor (s1p / person
        :name (s1n / name
            :op1 "John"))
    :refer-number singular)
```
Example 3-2-2-2 (1b)
```
Guitar strings
(s1s / string
    :part-of (s1g / guitar)
    :refer-number plural)
```
Typifying modifiers, on the other hand, "enrich the referent description by subcategorizing it or selecting the quantity (cardinality, amount, proportion, piece) of the
category or type denoted by the head noun." For such modifiers, a high-level, coarse-grained relation `:mod` is available. For example, in (2a), the modifier *women* does not narrow down the reference of *magazine* to a specific identifiable instance, but rather to a subclass of magazines. It is therefore annotated with the `:mod` relation, as opposed to a phrase like *that woman's magazine*, where *woman* would be annotated with the `:possessor` relation. The `:mod` relation additionally inherits some uses from UMR. It is used to annotate demonstrative determiners, and it is used to annotate property concept modifiers that do not have their own frame files. Those uses are exemplified in (2b)-(2c) A number of more fine-grained subtypes of the `:mod` relation are also available - `:age`, for indicating the age of referents as in (2d); `:group`, for indicating the membership of groups (2e); `:topic`, for indicating what a referent is about as in (2f), and `:medium` for indicating channels of communication, such as languages as in (2g).

Example 3-2-2-2 (2)

Example 3-2-2-2 (2a)
```
a women's magazine
(s1m / magazine
    :mod (s1w / woman)
    :refer-number singular)
```
Example 3-2-2-2 (2b)
```
These shirts of mine
(s1s / shirt
    :possessor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :mod (s1t / these)
    :refer-number plural)
```
Example 3-2-2-2 (2c)
```
My quirky shirts
(s1s / shirt
    :possessor (s1p / person
        :refer-person 1st
        :refer-number singular)
    :mod (s1q / quirky)
    :refer-number plural)
```
Example 3-2-2-2 (2d)
```
The thirty year-old man
(s1m / man
    :age (s1t / temporal-quantity
        :quant 30
        :unit (s1y / year))
    :refer-number singular)
```
Example 3-2-2-2 (2e)

```
A swarm of bees
(s1s / swarm
    :group (s1b / bee
        :refer-number plural))
```
Example 3-2-2-2 (2f)

```
Information about the case
(s1i / information
    :topic (s1c / case))
```

Example 3-2-2-2 (2g)
```
a French song
(s1t / thing
    :ARG1-of (s1s / sing-01)
    :medium (s1l / language
        :name (s1n / name
            :op1 "French")))
```

##### Part 3-2-2-3. Circumstantial temporals and locatives

A number of relations serve to modify events rather than objects - they are used to annotate circumstantial locative and temporal information rather than participants. The `:direction` and `:path` relations are used to annotate cardinal directions and extended spatial paths, respectively, as in (1a) and (1b). The `:duration` and `:frequency` relations, illustrated in (1c)-(1e), are optionally used to annotate aspectual information that may be overtly present but that cannot be captured in the `:aspect` attribute - as clarified in Part 3-3-1, the latter abstracts away from duration and frequency information.

Example 3-2-2-3 (1)

Example 3-2-2-3 (1a)
```
He drove west.
(s1d / drive-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :direction (s1w / west)
    :aspect activity
    :modal-strength full-affirmative)
```
Example 3-2-2-3 (1b)
```
He drove through the tunnel.
(s1d / drive-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :path (s1t / tunnel)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-2-3 (1c)
```
I visited New York City for a week.
(s1v / visit-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "New"
            :op2 "York"
            :op3 "City"))
    :duration (s1t / temporal-quantity
        :quant 1
        :unit (s1w / week))
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 3-2-2-3 (1d)
```
I visited New York City twice.
(s1v / visit-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "New"
            :op2 "York"
            :op3 "City"))
    :frequency 2
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-2-3(1e)
```
I visit New York City every December.
(s1v / visit-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "New"
            :op2 "York"
            :op3 "City"))
    :frequency (s1r / rate-entity-91
        :ARG4 (s1d / date-entity
            :month 12))
    :aspect habitual
    :modal-strength full-affirmative)
```

##### Part 3-2-2-4. Named entities

The relations `:name`, `:wiki`, and `:opX` are mostly used in the treatment of named entities. Whenever an entity is explicitly mentioned by name in the text to be annotated, it receives a `:name` relation, whose daughter is an `(n / name)` node. This node then has as many numbered `:opX` relations as the number of words this name consists of, each of which takes one of these words as their daughter. In \[3-2-2-3 (1e)\] above, for example, the `(n / name)` concept corresponding to *New York City* takes an `:op1`, `:op1`, and `:op3` relation, one for each orthographic word. Named entities can also take a `:wiki` relation, whose daughter is the title of the Wikipedia page corresponding to the entity in question. Numbered `:opX` relations are also used as the daughters of various abstract concepts used for expressing relations between clauses or phrases (e.g. coordination), as in (1).

Example 3-2-2-4 (1)
```
I saw a spider and a snake.
(s1s / see-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1a / and
        :op1 (s1s2 / spider
            :refer-number singular)
        :op2 (s1s3 / snake
            :refer-number singular))
    :aspect state
    :modal-strength full-affirmative)
```

##### Part 3-2-2-5. Quantification

The `:ord`, `:quant`, `:range`, `:scale`, `:unit`, and `:value` relations are used to annotate semantics of quantification, as illustrated in (1). The `:ord` role is used to express ordinals. It always takes an `(o / ordinal-entity)` concept as its daughter, which in turn takes a `:value` relation to express the ordinal position, as in (1a). It may furthermore take a `:range` relation to indicate a specific time period in which the relevant ordinal position holds, as in (1b). The `:value` relation is, apart from ordinals, used for annotating percentages, phone numbers, e-mail addresses, and urls, as illustrated in (1c) and (1d). The `:quant` relation is used for annotating both exact and approximate cardinalities of sets of countable objects as in (1e) and (1f), as well as for the number of "units" of non-countable substances, as in (1g). This latter use includes temporal durations and spatial distances, as in \[3-2-2-3 (1c)\] above. The `:unit` relation is used for both standardized, well-established units such as dollars in \[3-3-2 (1a)\] below or weeks in \[3-2-2-3 (1c)\] above, and for ad-hoc mensural constructions, such as cups in (1g). Lastly, the `:scale` relation is used for quantities where a `:quant 0` value does not actually represent a 0-quantity, such as on the Richter or Decibel scale, as in (1h).

Example 3-2-2-5 (1)

Example 3-2-2-5 (1a)
```
I visited New York for the third time.
(s1v / visit-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "New"
            :op2 "York"))
    :ord (s1o / ordinal-entity
        :value 3)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-2-5 (1b)
```
I visited New York for the third time in six months.
(s1v / visit-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "New"
            :op2 "York"))
    :ord (s1o / ordinal-entity
        :value 3
        :range (s1t / temporal-quantity
            :quant 6
            :unit (s1m / month)))
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-2-2-5 (1c)
```
30 percent
(s1p / percentage-entity
    :value 30)
```
Example 3-2-2-5 (1d)
```
http://umr-tool.cs.brandeis.edu/display_post
(s1u / url-entity
    :value "http://umr-tool.cs.brandeis.edu/display_post")
```
Example 3-2-2-5 (1e)
```
Three houses
(s1h / house
    :quant 3)
```
Example 3-2-2-5 (1f)
```
More than three houses
(s1h / house
    :quant (s1m / more-than
        :op1 3))
```
Example 3-2-2-5 (1g)
```
Three cups of milk
(s1m / milk
    :quant 3
    :unit (s1c / cup))
```
Example 3-2-2-5 (1h)
```
6.5 on the Richter scale
(s1s / seismic-quantity
    :quant 6.5
    :scale (s1r / richter))
```

##### Part 3-2-2-6. Other relations

The `:example` relation, illustrated in (1a), is used to annotate illustrative examples of object categories. The `:polite` relation is used to indicate that an utterance (often a command) is marked for deference with respect to the interlocutor, as in (1b). The `:li` relation is used to mark entities as entries on a bulleted list, as in (1c).

Example 3-2-2-6 (1)

Example 3-2-2-6 (1a)
```
Countries like Germany and France
(s1c / country
    :example (s1a / and
        :op1 (s1c2 / country
            :name (s1n / name
                :op1 "Germany"))
        :op2 (s1c3 / country
            :name (s1n2 / name
                :op1 "France"))))
```
Example 3-2-2-6 (1b)
```
Could you close the window?
(s1c / close-01
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1w / window)
    :aspect performance
    :mode Imperative
    :polite +)
```

Example 3-2-2-6 (1c)
```
I will buy (a) rice, (b) beans, and (c) onions.
(b / buy-01
    :ARG0 (p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (and
        :op1 (r / rice
            :li "(a)")
        :op2 (b / bean
            :refer-number plural
            :li "(b)")
        :op3 (o / onion
            :refer-number plural
            :li "(c)")
    :aspect performance
    :modal-strength full-affirmative)
```

The `:condition` and `:concession` relations are alternative ways of annotating the `have-condition-91` and `have-concession-91` predicates - their use is detailed in Part 4-3.

Lastly, annotators have at their disposal an `:other-role` relation, as already mentioned in table 5 in Part 3-2-1-1. If they encounter any concept that they believe needs to be included in the UMR annotation, but UMR does currently not have a defined procedure of annotating it, they may simply add it to the graph using this `:other-role` relation, linking it to the concept node that seems appropriate.

### Part 3-3. UMR attributes

#### Part 3-3-1. Aspect

The aspect annotation consists of a single value that is annotated for
every event identified in Part 3-1-1. The aspect annotation doesn’t
have distinct annotation stages, unlike modality and participant roles.
Instead it relies on a typological lattice which ranges from very
coarse-grained to very fine-grained aspectual values. It’s expected that
languages at an earlier stage of semantic analysis or annotation will
tend to use more coarse-grained values, and languages at later stages of
annotation will tend to use more fine-grained values.

This is also heavily dependent on the aspectual distinctions that are
grammaticalized and/or obligatory in the language. For example, although
English has a long history of semantic analysis and many computational
resources, it has very little overt aspectual marking in its grammar and
therefore the most fine-grained aspect distinctions are very difficult
to judge in annotation. This aspect lattice is shown below.

![Aspect lattice](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Aspect%20Lattice_2022.png)

Below are the aspect values with a brief definition.

```habitual```: occurs/occurred usually or habitually
```imperfective```: ambiguous between state and atelic process
```process```: unspecified type of process
```atelic process```: process that does not reach a result state
```perfective```: process that comes to an end
```state```: unspecified type of state
```reversible state```: acquired state that is not permanent
```irreversible state```: acquired state that is permanent
```inherent state```: state that is not acquired and permanent
```point state```: state that is acquired and reversed at a single point in time
```activity```: process that does not end
```undirected activity```: process that does not end and does not progress linearly along a scale
```directed activity```: process that does not end and does progress linearly along a scale
```endeavor```: process that ends without reaching a result state
```semelfactive```: process that ends without reaching a result state and happens at a single point in time
```undirected endeavor```: process that ends without reaching a result state and does not progress linearly along a scale
```directed endeavor```: process that ends without reaching a result state and progresses linearly along a scale
```performance```: process that ends and  reaches a result state
```incremental accomplishment```: process that ends and reaches a result state, and progresses linearly along a scale
```nonincremental accomplishment```: process that ends and reaches a result state, and does not progress linearly along a scale
```directed achievement```: process that ends and reaches a result state within a single point in time, and progresses linearly along a scale
```reversible directed achievement```: process that ends and reaches a result state, which is not permanent, within a single point in time, and progresses linearly along a scale
```irreversible directed achievement```: process that ends and reaches a result state, which is permanent, within a single point in time, and progresses linearly along a scale

In order to select the appropriate annotation value for each event,
annotators proceed through a series of decisions.

##### Part 3-3-1-1. Event Nominals

The first decision concerns the morphosyntactic expression of the event. Events expressed as nominals often lack any grammatical clues as to their aspectual structure. This makes determining an aspectual
annotation value difficult. We do, however, know that these events are
processes, and not states, since nominals expressing states are not
identified as events. On the lattice,
```process``` is the aspectual value that includes all types of processes. Therefore, events expressed as event
nominals, as in (1), are annotated as
```process```.

Example 3-3-1 (1)

Example 3-3-1-1 (1a)
```
He presented his research at the meeting yesterday.
(s1p / present-01
    :ARG0 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1t / thing
        :ARG1-of (s1r / research-01
            :ARG0 s1p2))
    :place (s1m / meet-01
        :aspect process)
    :temporal (s1y / yesterday)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-3-1-1 (1b)
```
After the game, she went home.
(s1g / go-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG4 (s1h / home)
    :temporal (s1a / after
        :op1 (s1g2 / game
            :aspect process))
    :aspect performance
    :modal-strength full-affirmative)
```
Any event packaged in a referring expression is considered an event
nominal and annotated with `process`. This
includes underived nominals, nominalizations, and gerunds, as in (2).

Example 3-3-1-1 (2)

Example 3-3-1-1 (2a)
```
The second training was cancelled yesterday.
(s1c / cancel-01
    :ARG1 (s1t / train-01
        :ord (s1o / ordinal-entity
            :value 2)
        :aspect process)
    :temporal (s1y / yesterday)
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-3-1-1 (2b)
```
The dog interrupted the meeting with his barking.
(s1i / interrupt-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :ARG1 (s1m / meet-01
        :aspect process)
    :manner (s1b / bark-01
        :ARG0 s1d
        :aspect process)
    :aspect performance
    :modal-strength full-affirmative)
```

Note that *-ing* forms in English can occur in a variety of
constructions; they should only be treated as event nominals when they
are used in referring expressions (as in (2a) and
(2b) above). When they occur in other types of
constructions, as in (3), they should not
receive an aspect annotation at this point and annotators should
continue on to the next step.

Example 3-3-1-1 (3) The
dog stopped **barking** for a few seconds.

Event nominals that occur in predicate nominal constructions, as in
(4), are also not annotated at this point;
these are treated like other predicate nominal constructions.

Example 3-3-1-1 (4)

It was **an earthquake**.

##### Part 3-3-1-2. Habitual

The next step concerns the application of the
```habitual``` aspect value. This value should
be applied to all events that are presented as occurring usually or
habitually, as in (1).

Example 3-3-1-2 (1)

Example 3-3-1-2 (1a)
```
He bakes pies.
(s1b / bake-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1p2 / pie
        :refer-number plural)
    :aspect habitual
    :modal-strength full-affirmative)
```
Example 3-3-1-2 (1b)
```
She rides her bike to work.
(s1r / ride-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1b / bike
        :possessor s1p)
    :goal (s1w / work-01
        :ARG0 s1p
        :aspect process)
    :aspect habitual
    :modal-strength full-affirmative)
```
Example 3-3-1-2 (1c)
```
They vacation in Taos every winter.
(s1v / vacation-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG (s1c / city
        :name (s1n / name
            :op1 "Taos"))
    :frequency (s1r / rate-entity-91
        :ARG3 (s1t / temporal-quantity
            :quant 1
            :unit (s1y / year))
        :ARG4 (s1w / winter))
    :aspect habitual
    :modal-strength full-affirmative)
```
Example 3-3-1-2 (1d)
```
They used to vacation in Taos every winter.
(s1v / vacation-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s1c / city
        :name (s1n / name
            :op1 "Taos"))
    :frequency (s1r / rate-entity-91
        :ARG3 (s1t / temporal-quantity
            :quant 1
            :unit (s1y / year))
        :ARG4 (s1w / winter))
    :aspect habitual
    :modal-strength full-affirmative)
```

In English, present habitual events are signalled by the Simple Present
construction; past tense habitual events are expressed with the *used
to* construction. Note that the ```habitual```
annotation is not used for ability modals (e.g., *he can bake apple
pie*); see example 3-3-1-3 (3)) for handling ability modals.

##### Part 3-3-1-3. State

The next step assesses whether the event is a
```state```. The distinction between states and
processes is necessary for event identification (as states are only
identified as events when predicated, see Part 3-1-1). According to Vendler (1967), states are those events which are stative—that is, no change takes place over the course of the event. There are various ways to express states in predication, shown in (1); note that all of the non-verbal clause types identified in Part 3-1-1-3 and annotated with UMR predicates are annotated as ```state```.

Example 3-3-1-3 (1)

Example 3-3-1-3 (1a)
```
My cat loves tuna.
(s1l / love-01
    :ARG0 (s1c / cat
        :possessor (s1p / person
            :refer-person 1st
            :refer-number singular)
        :refer-number singular)
    :ARG1 (s1t / tuna)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (1b)
```
The doctor is tall.
(s1h / have-mod-91
    :ARG1 (s1d / doctor
        :refer-number singular)
    :ARG2 (s1t / tall)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (1c)
```
The book is on the table.
(s1h / have-place-91
    :ARG1 (s1b / book
        :refer-number singular)
    :ARG2 (s1t / table)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (1d)
```
She is an architect.
(s1h / have-role-91
    :ARG1 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG3 (s1a / architect)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (1e)
```
Your glass is in the kitchen.
(s1h / have-place-91
    :ARG1 (s1g / glass
        :possessor (s1p / person
            :refer-person 2nd
            :refer-number singular))
    :ARG2 (s1k / kitchen)
    :aspect state
    :modal-strength full-affirmative)
```

Modal verbs, as in (2), and events under the scope of
ability modals, as in (3), are also annotated as
```state```.

Example 3-3-1-3 (2)

Example 3-3-1-3 (2a)
```
He wants to travel to Albuquerque.
(s1w / want-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1t / travel-01
        :ARG0 s1p
        :ARG4 (s1c / city
            :name (s1n / name
                :op1 "Albuquerque"))
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (2b)
```
The cat needs to be fed.
(s1n / need-01
    :ARG0 (s1c / cat)
    :ARG1 (s1f / feed-01
        :ARG s1c
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (2c)
```
He’s dreading their decision.
(s1d / dread
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1d2 / decide-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-person plural)
        :aspect process)
    :aspect state
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (3)

Example 3-3-1-3 (3a)
```
She is able to sing that aria.
(s1s / sing-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1a / aria
        :mod (s1t / that)
        :refer-number singular)
    :aspect state
    :modal-strength neutral-affirmative)
```
Example 3-3-1-3 (3b)
```
This car can go up to 150 mph.
(s1g / go-01
    :ARG0 (s1c / car
        :mod (s1t / this)
        :refer-number singular)
    :manner (s1s / speed-quantity
        :quant 150
        :unit (s1m / miles-per-hour))
    :aspect state
    :modal-strength neutral-affirmative)
```
In this analysis, ability modals refer to a static state of affairs,
i.e. an entity possesses the relevant ability. For examples like
(3a), ability modals may look more like event
quantification. That is, there are probably multiple singing events that this example is generalizing over. Examples like (3b), however, show how ability modals are more like states. It is possible
that the car has never actually gone as fast as 150 mph; the car just
has the parts and (theoretical) ability to do so. Therefore, all types
of ability modals, both (3a) and (3b), are
analyzed as states and annotated as such.

There is a type of event, called “inactive actions” by Croft (2012), which is semantically intermediate between states and processes. In many languages, they can be construed either way. For example, English *lie* can occur in the Progressive (*Bill **is lying** on the bed*) or the Simple Present (*The Sandias **lie** to the east of Albuquerque*). And across languages there is variation as to the default construal of
inactive actions. The most frequent inactive actions are posture verbs
(*sit, stand, lie, hang*), perception verbs (*see/look at, watch,
hear/listen to, feel*), some sensation verbs (*ache*), mental activity
verbs (*think, understand*), and verbs of operation/function (*work* in
*This washing machine **works/is working***). For the UMR annotation,
inactive actions in all constructions are annotated as
```state```. If it is unclear whether an event
refers to a ```state``` or an
```atelic process```, then the
```imperfective``` annotation value is used.

There are different types of states, shown in
(4), which can optionally be distinguished in
the aspect annotation.

Example 3-3-1-3 (4)

Example 3-3-1-3 (4a)
```
My cat is black and white.
(h / have-mod-91
    :ARG1 (c / cat
        :possessor (p / person
            :refer-person 1st
            :refer-number singular)
        :refer-number singular)
    :ARG2 (a / and
        :op1 (b / black)
        :op2 (w / white)
    :aspect inherent State
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (4b)
```
My cat is hungry.
(s1h / hunger-01
    :ARG0 (s1c / cat
        :possessor (s1p / person
            :refer-person 1st
            :refer-number singular))
    :refer-number singular)
    :aspect reversible State
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (4c)
```
The wine glass is shattered.
(s1s / shatter-01
    :ARG1 (s1g / glass
        :purpose (s1w / wine)
        :refer-number singular)
    :aspect irreversible State
    :modal-strength full-affirmative)
```
Example 3-3-1-3 (4d)
```
It is 2:30pm.
(s1b / be-temporally-at-91
    :ARG1 (s1n / now)
    :ARG2 (s1d / date-entity
        :time 14:30)
    :aspect point State
    :modal-strength full-affirmative)
```

Events that are annotated as ```inherent
state```, as in (4a), refer to states that are
an inherent property of the entity, i.e. they did not ‘start’ at any
particular point in the entity’s history and are not changeable in the
future. Events annotated as ```reversible
state```, as in (4b), refer to properties of entities
that are not inherent, meaning they have come into existence at some
point during the entity’s history; these states are reversible, meaning
the entity likely will revert back to its base state in the future.
Events annotated as ```irreversible state```,
as in (4c), refer to properties of entities that are not
inherent, but cannot be reversed in the future; once acquired, these
states are permanent. Finally, events that are annotated as
```point state```, as in (4d),
refer to states that come into and out of existence over a single point
in time (what is considered a ‘point’ is open to construal); these
states necessarily do not persist into the future.

Events that are not annotated as a type of
```state``` move on to the next step.

##### Part 3-3-1-4. Activity

The ```activity``` label applies to processes
when there is no evidence that the event has come to an end, as in
(1).

Example 3-3-1-4 (1)

Example 3-3-1-4 (1a)
```
He is still writing his paper.
(s1w / write-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1p2 / paper
        :possessor s1p
        :refer-number singular)
    :mod (s1s / still)
    :aspect activity
    :modal-strength full-affirmative)
```
Example 3-3-1-4 (1b)
```
He was writing his paper yesterday.
(s1w / write-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s1p2 / paper
        :possessor s1p
        :refer-number singular)
    :temporal (s1y / yesterday)
    :aspect activity
    :modal-strength full-affirmative)
```

This covers cases where it is clear that the process is still ongoing at
document creation time, as in (1a), but also cases
where it is ambiguous whether or not the process continues, as in
(1b).

This step is largely dependent on context and real world knowledge,
however there are some grammatical cues that can help. Events in the
present tense, as in (2), are annotated as
```activity```.

Example 3-3-1-4 (2)
```
He is playing the violin.
(s1p / play-01
    :ARG0 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s1v / violin)
    :aspect activity
    :modal-strength full-affirmative)
```

Inceptive and continuative aspectual marking, as in (3),
also do not imply that an event has (necessarily) ended.

Example 3-3-1-4 (3)

Example 3-3-1-4 (3a)
```
He started playing the violin.
(s1p / play-01
    :ARG0 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s1v / violin)
    :aspect activity
    :modal-strength full-affirmative)
```
Example 3-3-1-4 (3b)
```
He kept on playing the violin.
(s1p / play-01
    :ARG0 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s1v / violin)
    :aspect activity
    :modal-strength full-affirmative)
```
If an annotator is unsure about whether the text indicates that an event has ended or not, the ```atelic process```
label can be used.

There are two finer-grained ```activity```
categories which can optionally be distinguished. Certain types of
activities describe directed change, as in
(4), whereas other activities describe
undirected change, as in (5);
these are annotated as ```directed activity```
and ```undirected activity``` respectively.

Example 3-3-1-4 (4)
```
The soup was cooling on the counter.
(s1c / cool
    :ARG1 (s1s / soup)
    :place (s1c2 / counter)
    :aspect directed Activity
    :modal-strength full-affirmative)
```

Example 3-3-1-4 (5)
```
The cat was meowing outside the door.
(s1m / meow-01
    :ARG0 (s1c / cat
        :refer-number singular)
    :place (s1o / outside
        :op1 (s1d / door))
    :aspect undirected Activity
    :modal-strength full-affirmative)
```

Events annotated as ```directed activity```
refer to change that occurs gradually along a qualitative scale. In
(4), the temperature of the soup
continues to decrease in a linear fashion. Events annotated as
```undirected activity``` refer to change that
does not progress incrementally along a scale; in
(5), there is no scale or gradual
change.

Events that have ended prior to document creation time and have not yet
received an annotation move on to the next step.

##### Part 3-3-1-5. Endeavor and Performance

At this point, only ```perfective``` events are
left: ```endeavor``` and
```performance```. Both the
```endeavor``` and
```performance``` aspectual types entail that
the process has come to an end; they are distinguished by the
boundedness of the event in terms of qualitative state. The
```performance``` value is used when the event
reaches a result state distinct from the base (start) state, that is, a specific “natural” endpoint. The ```endeavor```
value is used when the events ends, but does not reach a distinct result
state. The ```performance``` value can be seen
as the ‘default’ value for events at this step; the
```endeavor``` value is only annotated in the
presence of explicit marking, which may come in several forms detailed
below. If it’s not clear which category an event fits into, it can be
annotated as ```perfective```.

The explicit aspectual markings which suggest an
```endeavor``` annotation are terminative
aspect marking, durative adverbials, and non-result paths. These are
illustrated for English below.

Example 3-3-1-5 (1)

Example 3-3-1-5 (1a)
```
Mary stopped mowing the lawn.
(s1m / mow-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Mary"))
    :ARG1 (s1l / lawn)
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (1b)
```
Mary mowed the lawn for thirty minutes.
(s1m / mow-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Mary"))
    :ARG1 (s1l / lawn)
    :duration (s1t / temporal-quantity
        :unit (s1m2 / minute)
        :quant 30)
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (1c) \*Mary
finished **mowing** the lawn for thirty minutes.

Example 3-3-1-5 (1d)
```
They walked along the river.
(s1w / walk-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG2 (s1a / along
        :op1 (s1r / river))
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (1e)
```
They finished walking along the river.
(s1w / walk-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG2 (s1a / along
        :op1 (s1r / river))
    :aspect performance
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (1f)
```
They walked along the river in 3 hours.
(s1w / walk-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG2 (s1a / along
        :op1 (s1r / river))
    :duration (s1t / temporal-quantity
        :unit (s1h / hour)
        :quant 3)
    :aspect performance
    :modal-strength full-affirmative)
```

Terminative aspectual marking, such as *stop* in English, is the
strongest evidence that an event has ended without reaching a result
state and should therefore be annotated as
```endeavor```. Durative adverbials, such as in
(1b), are the second strongest evidence for an
```endeavor``` annotation: they indicate that
the event took place for a defined period of time and then ended, likely
without completion. At least in English, durative adverbials cannot
co-occur with completive aspectual marking; see
(1c). A non-result path is the weakest evidence
for an ```endeavor``` annotation; in the
absence of other aspectual indicators, a non-result path requires an
```endeavor``` annotation, as in
(1d). But, if there is a completive aspectual marker,
as in (1e), or a container adverbial, as in
(1f), both indicators that an event has reached
a distinct result state, then the event is annotated as
```performance```.

In the absence of any of the aspectual indicators listed above, events
that have made it to this point in the decision tree are annotated as
```performance```.

Both ```endeavor``` and
```performance``` have more fine-grained
aspectual distinctions which may optionally be annotated. Endeavors may
be specified with ```undirected endeavor```,
```directed endeavor```, and
```semelfactive```. The
```undirected endeavor``` and
```directed endeavor``` values correspond to
```undirected activity``` and
```directed activity```; they differ in that
the event has come to an end. Semelfactives refer to punctual events
that happen once before reverting back to the base state (these are
similar to ```point state```, but refer to a
process), as in (2c).

Example 3-3-1-5 (2)

Example 3-3-1-5 (2a)
```
The cat meowed for two hours until I woke up.
(s1m / meow-01
    :ARG0 (s1c / cat)
    :duration (s1t / temporal-quantity
        :unit (s1h / hour)
        :quant 2)
    :temporal (s1u / until
        :op1 (s1w / wake-01
            :ARG1 (s1p / person
                :refer-person 1st
                :refer-number singular)
            :aspect performance
            :modal-strength full-affirmative))
    :aspect undirected Endeavor
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (2b)
```
The soup cooled for an hour before we ate it.
(s1c / cool-01
    :ARG1 (s1s / soup)
    :duration (s1t / temporal-quantity
        :unit (s1h / hour)
        :quant 1)
    :temporal (s1b / before
        :op1 (s1e / eat-01
            :ARG0 (s1p / person
                :refer-person 1st
                :refer-number plural)
            :ARG1 s1s
            :aspect performance
            :modal-strength full-affirmative))
    :aspect directed Endeavor
    :modal-strength full-affirmative)
```

Example 3-3-1-5 (2c)
```
The cat meowed (once).
(s1m / meow-01
    :ARG0 (s1c / cat
        :refer-number singular)
    :aspect semelfactive
    :modal-strength full-affirmative)
```

The finer-grained annotations for
```performance``` distinguish between punctual
events (```directed achievement```) and durative
events (```incremental accomplishment```,
```nonincremental accomplishment```), with even
finer-grained categories based on the type of change.

Achievements are punctual events, meaning that they are conceptualized as
occurring at a single point in time (like ```point
state``` and ```semelfactive```). Unlike
```point state``` and
```semelfactive```, achievements don’t revert
back to the base state, which is why they’re considered a finer-grained
type of ```performance```. The
```directed achievement``` annotation can be
further specified based on whether the change is reversible or
irreversible. In (3a), the change that the door
undergoes can be reversed in that the door can be closed; therefore this
is annotated as ```reversible directed
achievement```. In (3b), the change that the
window undergoes cannot be reversed; therefore this is annotated as
```irreversible directed achievement```.

Accomplishments are durative events that can be categorized based on
whether the change occurs incrementally or nonincrementally; this is
similar to the difference between directed and undirected activities and
endeavors. With ```incremental
accomplishment```, the change occurs incrementally along the
qualitative dimension; in (3c), the pancake
is eaten piece-by-piece and each subsequent bite brings the event closer
to completion. With ```nonincremental
accomplishment```, the change ends up at a distinct result state (as
with all types of Performances), but it may not get there in a
linear/incremental fashion. In (3d),
the computer does not necessarily get progressively more repaired with
each action. Harry may try one tactic unsuccessfully to fix the
computer; he may even make the problem worse at some point, but
eventually succeeds in repairing the computer.

Example 3-3-1-5 (3)

Example 3-3-1-5 (3a)
```
The door opened.
(s1o / open-01
    :ARG1 (s1d / door
        :refer-number singular)
    :aspect reversible Directed Achievement
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (3b)
```
The window shattered.
(s1s / shatter-01
    :ARG1 (s1w / window
        :refer-number singular)
    :aspect irreversible Directed Achievement
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (3c)
```
I ate an apple pancake.
(s1e / eat-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1p2 / pancake
        :mod (s1a / apple)
        :refer-number singular)
    :aspect incremental Accomplishment
    :modal-strength full-affirmative)
```
Example 3-3-1-5 (3d)
```
Harry repaired the computer.
(s1r / repair-01
    :ARG0 (s1p / person
        :name (s1n / name :op1 "Harry"))
    :ARG1 (s1c / computer
        :refer-number singular)
    :aspect nonincremental Accomplishment
    :modal-strength full-affirmative)
```

#### Part 3-3-2. Mode

UMR adopts the `:mode` attribute from AMR. The values for the `:mode` attribute include:

```expressive```: used for exclamational words such as _hmm_, _wow_, _yup_ etc., which express emotion but don't clearly refer to events, objects or properties, as in (1a). This value is not used for mere emphasis, or for exclamation marks.

```imperative```: used for commands, as in (1b).

```interrogative```: used for both polar questions and content questions, as in (1c).

Example 3-3-2 (1)

Example 3-3-2 (1a)
```
Yup , a couple of hundred dollars is going to save the day !
(s1s / save-02
      :ARG0 (s1c / couple
            :op1 (s1m / monetary-quantity
            :quant 100
                :unit (s1d / dollar)))
      :ARG1 (s1d / day
            :refer-number singular)
      :aspect performance
      :modal-strength full-affirmative
      :mode expressive)
```
Example 3-3-2 (1b)
```
Chalk another good one up to the wife .
(s1c / chalk-up-02
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1a / another
        :ARG1-of (s1g / good-02)
        :quant 1)
    :ARG2 (s1w / wife)
    :aspect performance
    :modal-strength partial-affirmative
    :mode imperative)
```

Example 3-3-2 (1c)
```
Did you see that?
(s1s / see-01
    :ARG0 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG1 (s1t / that)
    :aspect state
    :modal-strength neutral-affirmative
    :mode interrogative
    :polarity umr-unknown)
```

#### Part 3-3-3. Polarity
UMR mainly treats propositional negation at the document-level in the modal dependency annotation. However, the AMR attribute `:polarity` is also maintained in the UMR sentence-level annotation. It is used to flag any morphosyntactic indicators of negation that are present in the clause, as in (1). These do not necessarily signal semantic negation. This is the case, for example, for some instances of derivational negation of adjectives in English.

Example 3-3-3 (1)

Example 3-3-3 (1a)
```
Unhealthy food.

(s1t / thing
    :ARG1-of (s1e / eat-01)
    :mod (s1h / healthy
        :polarity -))
```

#### Part 3-3-4. Quant

Example 3-3-4 (1)

```
As of now , five million tickets have been sold on the StubHub website .
(s1s / sell-01
    :ARG1 (s1t / ticket
        :quant 5000000)
    :place (s1w / website
        :mod (s1c / company
            :name (s1n / name
                :op1 "StubHub")))
    :temporal (s1a / as-of
        :op1 (s1n2 / now))
    :aspect performance)
```

#### Part 3-3-5. Ref
As opposed to AMR, which uses an English-based lexical treatment of pronominal reference, UMR approaches pronominal reference and person/number marking in a cross-linguistically motivated way. It annotates person and number through two attributes - `:refer-person` for grammatical person information, and `:refer-number` for grammatical number marking. These attributes can apply to any entity concept. If an explicit nominal is marked for plural or dual number, for instance, the node for this entity concept can take the relevant attribute value label, as in (1).

Example 3-3-5 (1)

Example 3-3-5 (1a)
```
Bill saw rare birds today.
(s1s / see-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Bill"))
    :ARG1 (s1b / bird
        :mod (s1r / rare)
        :refer-number plural)
    :aspect state
    :modal-strength full-affirmative)
```

Example 3-3-5 (1b)
```
áine    ŋara-di-a-ru.
woman   that-3PL-EP-DU
'Those two women'

(s1a / áine
    :mod (ŋ / ŋara)
    :refer-number dual)
Glosses: áine = 'woman'; ŋara = 'that'
```

For arguments expressed only through verbal cross-referencing, or arguments that are implicit, both `:refer-person` and `:refer-number` can be used to represent their pronominal features. In such cases where there is no overt nominal expression to attach those values to, UMR "hallucinates" a concept (typically a named-entity category, e.g. `person`, `thing`) to attach the attribute labels to in order to facilitate cross-lingual compatibility, as in (2). In the context preceding this one-word sentence, the speaker talks about how upon first contact between the Sanapaná and Latinoparaguayans, the Paraguayans gifted the Sanapaná food and clothes. Here, the Sanapaná speaker describes the reaction of his ancestors to these gifts. From the prefixal indexation on the verb (2nd/3rd person masculine + distributive) and the preceding context (talking about the Sanapaná ancestors), we know that the `:actor` argument of the *eat*-verb is third person plural. Therefore, we annotate this argument with a `(p / person)` concept, which in turn takes `:refer-person` and `:refer-number` attributes with the values `3rd` and `Plural`. The `:undergoer` of this predicate is not explicitly expressed at all, but from previous context we know it is the food that they were offered by the Paraguayans. We therefore annotate it with a `(t / thing)` concept that will later in the document-level annotation be marked as coreferential with a mention of 'food' in the previous context.

Example 3-3-5 (2)
```
m-e-hl-t-om-o=hlta
NEG-2/3M.IRR-DSTR-eat-TI-IPFV=PHOD
'They did not eat it.'

(s1e / entoma-00
    :actor (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :undergoer (s1t / thing)
    :aspect performance
    :modal-strength full-negative)
Glosses: entoma-00 = 'eat'
```

The possible values for the `:refer-person` attribute are based on Cysouw's (2003) cross-linguistic study of person-marking systems in the languages of the world. They are organized in a lattice as seen below. The default level of categories contains the well-known and familiar `1st`, `2nd`, and `3rd` person values. Some languages have more fine-grained person systems, distinguishing a first person `exclusive` from a first person `inclusive` value in non-singular numbers (depending on whether the interlocutor is included in the group that is being referred to). Other languages have more coarse-grained systems, making no distinction between first and second person, or between second and third person (like Sanapaná above).

![Person lattice](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Person%20Lattice_2022.png)

The possible number values for the `:refer-number` attribute are based on Corbett (2000). The default level here consists simply of `singular` vs. `non-singular`. Languages with more fine-grained categories in their system may have more fine-grained `dual`, `trial`, `paucal`, and `greater plural` categories, which fit together as shown in the figure below.

![Number lattice](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Number%20Lattice.jpg)

#### Part 3-3-6. Degree
In AMR, markers of degree such as English _very_ (high degree of a scalar quality, as in _very cold_) and _somewhat_ (low degree of a scalar quality, as in _somewhat dirty_) are treated lexically - a `:degree` relation is added to the property concept that is admodified. However, in many languages, such degree expressions are morphological rather than periphrastic - they form a single word with the property concept word. Such a lexical treatment is hard for these languages. UMR therefore allows annotators to treat `:degree` as an attribute, with three possible values: `intensifier`, `downtoner`, and `equal`. These values can in this way be attached directly to the whole property concept word without the need for morphological decomposition, as shown in (1). For languages with periphrastic degree expressions like English, the lexical entry for words such as _very_ and _somewhat_ can be constructed to include reference to which of the three degree values listed above it expresses. In that way, English annotations would be comparable to annotations in a language like Sanapaná.

Example 3-3-6 (1)
```
ak-yav-ay'-a=ngkoye     yamet
2/3F-be.large-TI-PFV.NMLZ=INTNS tree
'The tree is very large.'
(s1h / have-mod-91
    :ARG1 (s1y / yamet)
    :ARG2 (s1e / enyavay'a-00 'large'
        :degree Intensifier)
    :aspect state
    :modal-strength full-affirmative)
Glosses: yamet = 'tree'

(s1h / have-mod-91
    :ARG1 (s1t / tree)
    :ARG2 (s1l / large
        :degree (s1v / very))
    :aspect state
    :modal-strength full-affirmative)
Lexicon: Very - Intensifier
```

## Part 4. Document-Level Representation
### Part 4-1. Coreference

Anaphoric expressions such as pronouns cannot be properly interpreted without identifying their referents. This is generally done by linking an anaphoric expression to a named entity, a process generally known as *coreference* in the field of NLP. Coreference is an established NLP task, and the goal here is to identify the most relevant types of coreference in the UMR framework.

#### Part 4-1-1. Entity coreference

For the UMR corereference annotation, we first need to answer two questions. The first is what counts as an anaphorical expression. For UMR annotation, we focus on pronouns. The second question is what types of coreference relations we are considering. The most common type of coreference relations are *identity* relations, and we label such relations as *same*. Identity relations means two expressions have the same referent. In (1), *he* refers to the same person as the person whose name is "Edmond Pope", and it is therefore annotated in the document-level representation with a `:same-entity` relation to the `s2p` node.

Example 4-1-1 (1)

```
Snt2: Pope is the American businessman who was convicted last week on spying charges and sentenced to 20 years in a Russian prison.
(s3i / identity-91
     :ARG1 (s3p / person
        :name (s3n / name "op1 "Pope))
     :ARG2 (s3b / businessman
    :mod (s3n2 / nationality
       :name (s3n3 / name :op1 "America")))
    :ARG1-of (s3c / convict-01
       :ARG2 (s3c2 / charge-05
          :ARG1 s3b
          :ARG2 (s3s / spy-02
             :ARG0 s3b))
       :temporal (s3w / week
          :mod (s3l / last))
       :aspect performance
       :modal-strength full-affirmative)
    :ARG1-of (s3s2 / sentence-01
       :ARG2 (s3p2 / prison
          :mod (s3c3 / country
             :name (s3n4 / name :op1 "Russia))
          :duration (s3t / temporal-quantity
             :quant 20
         :unit (s3y / year)))
       :ARG3 s3s
       :aspect performance
       :modal-strength full-affirmative)
     :aspect state
     :modal-strength full-affirmative)

Snt3: He denied any wrongdoing.
(s3d / deny-01
    :ARG0 (s3p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s3t / thing
        :ARG1-of (s3d2 / do-02
            :ARG0 s3p
            :ARG1-of (s3w / wrong-02)))
    :aspect performance
    :modal-strength full-affirmative)

(s3s0 / sentence
    :temporal ((document-creation-time :before s3d)
            (s3d :before s3d2))
    :modal ((author :full-affirmative s3p))
            (s3p :full-affirmative s3d)
            (s3d :unspecified s3d2))
  :coref(s2p :same-entity s3p))
```

The example in (2) shows how the `:subset-of` relation is used to relate mentions of sets of entities to mentions of entities belonging to such a set. For example, _we_ (`p3`) includes reference to two entities - the author/speaker of the sentence, and the person who is described as *possessive and controlling*. The pronoun _he_, given the constant `p2`, refers to one of these two entities. Therefore, in the document-level annotation, `p2` is annotated with a `:subset-of` relation to the `p3` node.

Example 4-1-1 (2)
```
He is very possessive and controlling but he has no right to be as we are not together.
(s1c / contrast-01
      :ARG1 (s1a / and
            :op1 (s1p / possessive-03
                  :ARG0 (s1p / person
            :refer-person 3rd
            :refer-number singular)
                  :degree (s1v / very)
          :aspect state
          :modal-strength full-affirmative)
            :op2 (s1h / have-mod-91
                  :ARG1 s1p
          :ARG2 (s1c2 / controlling)
                  :degree (s1v / very)
          :aspect state
          :modal-strength full-affirmative))
      :ARG2 (s1r / right-05
            :ARG1 s1p
            :ARG2 s1a
            :ARG1-of (s1c3 / cause-01
                  :ARG0 (s1h2 / have-mod-91
            :ARG1 (s1p2 / person
                :refer-person 1st
                :refer-number plural)
            :ARG2 (s1t / together)
            :aspect state
            :modal-strength full-negative))
            :aspect state
        :modal-strength full-negative))
(s / sentence
    :temporal ((document-creation-time :overlap s1p)
            (s1p :overlap s1h)
            (s1h :overlap s1r)
            (s1r :overlap s1h2))
    :modal ((author :full-affirmative s1p)
            (author :full-affirmative s1h)
            (author :full-negative s1r)
            (author :full-negative s1h2))
    :coref (p :subset-of p2))
```

#### Part 4-1-2. Event coreference

UMR uses the `:same-event` relation to represent cases where two event mentions refer to  the same event, as in \[4-1-1 (1)\].

 Example 4-1-2 (1)

 Example 4-1-2 (1a)
```
El-Shater and Malek's property was confiscated and is believed to be worth millions of dollars.
(s1a / and
    :op1 (s1c / confiscate-01
        :ARG1 (s1a2 / and
            :op1 (s1p / property
                :possessor (s1p2 / person
                    :name (s1n / name
                        :op1 "El-Shater")))
            :op2 (s1p3 / property
                :possessor (s1p4 / person
                    :name (s1n2 / name
                        :op1 "Malek"))))
        :aspect performance
        :modal-strength full-affirmative)
    :op2 (s1b / believe-01
        :ARG1 (s1w / worth-01
            :ARG1 s1a2
            :ARG2 (s1m / multiple
                :op1 (s1m2 / monetary-quantity
                    :quant 1000000
                    :unit (s1d / dollar)))
            :aspect state)
        :aspect state
        :modal-strength full-affirmative))

(s1s0 / sentence
    :temporal ((past-reference :contained s1c)
            (document-creation-time :overlap s1b)
            (s1b :overlap s1w))
    :modal ((author :full-affirmative s1c)
            (author :full-affirmative NULL_BELIEVER)
            (NULL_BELIEVER :full-affirmative s1b)
            (s1b :unspecified s1w)))
```
 Example 4-1-2 (1b)
```
Abdel-Maksoud stated the confiscation will affect the Brotherhood's financial bases.
(s2s / state-01
    :ARG0 (s2p / person
        :name (s2n / name
            :op1 "Abdel-Maksoud"))
    :ARG1 (s2a / affect-01
        :ARG0 (s2c / confiscate-01)
        :ARG1 (s2b / base
            :possessor (s2o / organization
                :name (s2n2 / name
                    :op1 "Brotherhood"))
            :mod (s2f / finance))
        :aspect performance
        :quote s2s
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)

(s2s0 / sentence
    :temporal ((s1c :after s2s)
            (s2s :after s2a))
    :modal ((author :full-affirmative s2s)
            (author :full-affirmative s2p)
            (s2p :full-affirmative s2c)
            (s2p :full-affirmative s2a))
    :coref (s1c :same-event s2c))
```
Event identity also includes cases where the same underlying event is referred to with two very different linguistic expressions. This is the case for *introduced* and *provide* in (2).

Example 4-1-2 (2)

Example 4-1-2 (2a)
```
The Three Gorges project on the Yangtze River has recently **introduced*** the first foreign capital.
(s1i / introduce-01
    :ARG0 (s1p / project
        :name (s1n / name
            :op1 "The"
            :op2 "Three"
            :op3 "Gorges")
        :place (s1r / river
            :name (s1n2 / name
                :op1 "Yangtze"
                :op2 "River")))
    :ARG1 (s1c / capital
        :mod (s1f / foreign)
        :ord (s1o / ordinal-entity
            :value 1))
    :temporal (s1r2 / recent)
    :aspect performance
    :modal-strength full-affirmative)

(s1s0 / sentence
    :temporal ((past-reference :contained s1r2)
            (s1r2 :contained s1i))
    :modal (author :full-affirmative s1i))
```
Example 4-1-2 (2b)
```
The loan, a sum of 12.5 million US dollars, is an export credit **provided** to the Three Gorges project by the Canadian government, which will be used mainly for the management system of the Three Gorges project.
(s2i / identity-91
    :ARG1 (s2t / thing
        :ARG1-of (s2l / loan)
        :ARG0-of (s2i2 / identity-91
            :ARG1 (s2m / monetary-quantity
                :quant 12500000
                :unit (s2d / dollar
                    :mod (s2c / country

                        :name (s2n / name :op1 "US"))))))
    :ARG2 (s2c2 / credit
        :mod (s2e / export-01)
        :ARG1-of (s2p / provide
            :ARG0 (s2g / government-organization
                :ARG0-of (s2g / govern-01
                    :mod (s2c3 / country

                        :name (s2n2 / name :op1 "Canada"))))
            :ARG2 (s2p2 / project

                :name (s2n3 / name
                    :op1 "Three"
                    :op2 "Gorges"))
            :aspect performance
            :modal-strength full-affirmative)
        :ARG1-of (s2u / use-01
            :ARG2 (s2s / system
                :possessor s2p2
                :mod (s2m2 / manage-01))
            :mod (s2m3 / main)
            :aspect activity
            :modal-strength full-affirmative))
    :aspect state
    :modal-strength full-affirmative)

(s2s0 / sentence
    :temporal ((document-creation-time :overlap s2i)
            (future-reference :contained s2u))
    :modal ((author :full-affirmative s2i)
            (author :full-affirmative s2p)
            (author :full-affirmative s2u))
    :coref (s1i :same-event s2p))
```
The `:subset-of` relation is also used to annotate the subset relations between two event mentions, with one referring to a subset of another, as is the case in (3). Both the _arrest_ made in Germany and the one made in the Netherlands are subevents of the _arrests_ that were ordered by judge Fragnoli. Therefore, both the `s1a2` node and the `s1a3` node are annotated with a `:subset-of` relation to `s2a`.

Example 4-1-2 (3)

Example 4-1-2 (3a)
```
1 arrest took place in the Netherlands and another in Germany.
(s1a / and
    :op1 (s1a2 / arrest-01
        :quant 1
        :place (s1c / country
            :name (s1n / name
                :op1 "Netherlands"))
        :aspect performance
        :modal-strength full-affirmative)
    :op2 (s1a3 / arrest-01
        :place (s1c2 / country
            :name (s1n2 / name
                :op1 "Germany"))
        :mod (s1a4 / another)
        :aspect performance)
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((document-creation-time :before a2)
            (document-creation-time :before a3))
    :modal ((author :full-affirmative a2)
            (author :full-affirmative a3)))
```
Example 4-1-2 (3b)
```
The arrests were ordered by anti-terrorism judge fragnoli.
(s2o / order-01
    :ARG0 (s2p / person
        :name (s2n / name
            :op1 "Fragnoli")
        :ARG0-of (s2o2 / oppose-01
            :ARG1 (s2t / terrorism))
        :ARG1-of (s2h / have-role-91
            :ARG3 (s2j / judge-01)))
    :ARG2 (s2a / arrest-01
        :aspect process
        :quote s2o)
    :aspect performance
    :modal-strength full-affirmative)

(s2s0 / sentence
    :temporal (s2a :before s2o)
    :modal ((author :full-affirmative s2o)
            (author :full-affirmative s2p)
            (s2p :partial-affirmative s2a))
    :coref ((s1a2 :subset-of s2a)
            (s1a3 :subset-of s2a)))
```

<!---
- Script / subevent?

For now UMR does not annotate cases where one event is a subevent of another event, or when an event is part of a "script". These will be annotated under temporal relations.

```
 Reports suggest that the group of nine were having a picnic on Friday when they were abducted in the Saada province of Yemen. A spokesman for the Yemeni Embassy said "The foreigners ventured outside the city of Saada without the required police escorts due to the heightened security situation in the area.
```
 --->

### Part 4-2. Temporal Dependency

The temporal annotation in UMR is done at both the sentence level and the document level. For instance, a time expression that serves as the modifier of a predicate is annotated at the sentence level. In (1), the time expression
*April 1998* is annotated as a temporal modifier of the predicate *sign*. Likewise, the temporal relation between an event and its document creation time (document-creation-time) is also annotated at the sentence level. In (1), the temporal relation between *sign* and the document-creation-time is annotated as `:temporal (b2 /before :op (n / now))`. The temporal relation between an event and a time expression is annotated when a time expression is present in the sentence. The temporal relation between an event and the document-creation-time is annotated when this temporal relation is defined in that context. For example, while the relation between *signed* and the document-creation-time is clearly defined, the temporal relation between *fight* and the document-creation-time is not.

Example 4-2 (1)
```
In April 1998 Arab countries signed an anti-terrorism agreement that binds the signatories to coordinate to fight terrorism.
(s / sign-02
      :ARG0 (c / country
            :mod (e / ethnic-group
                  :name (n / name :op1 "Arab")))
      :ARG1 (a / agree-01
            :topic (c2 / counter-01
                  :ARG1 (t / terrorism))
            :ARG0-of (b / bind-01
                  :ARG1 c
                  :ARG2 (c3 / coordinate-01
                        :ARG1 c
                        :purpose (f / fight-01
                              :ARG0 c
                              :ARG1 t
                  :aspect activity
                  :modal-strength full-affirmative)
            :aspect activity)
          :aspect activity
          :modal-strength full-affirmative))
      :temporal (d / date-entity :year 1998 :month 4)
      :temporal (b2 / before :op (n / now))
      :aspect performance))
```

In addition to temporal relations at the sentence level, we also annotate temporal relations at the document level.
The document-level temporal relations focus on event-event and time-time relations. Time-time relations are annotated when
a relative time depends on another time expression for its interpretation.

Event-event relations are annotated only when the temporal relations are clearly supported by morpho-syntactic clues or when there is a clear temporal sequence can be inferred.

The temporal dependency is divided into two passes: the first pass involves setting up the temporal
superstructure – the top levels of the dependency structure - and the second
pass involves adding events to the temporal dependency structure. The temporal superstructure contains the temporal expressions (timexs) in the text and pre-defined metanodes and their temporal relations to each other; the rest of the temporal dependency contains the events and their temporal relations to timexs and other events.

#### Part 4-2-1. Nodes in the temporal dependency

There are three types of nodes in the temporal dependency structure: pre-defined metanodes, time expressions, and events. Pre-defined metanodes and time expressions make up the top levels of the dependency structure, called the temporal superstructure. `:depends-on` is the relation that is used to link all nodes in the temporal superstructure.

##### Part 4-2-1-1. Pre-defined metanodes

Pre-defined metanodes are nodes that are present at the top of every temporal dependency structure, connected directly to the `root` node. There are four pre-defined metanodes: `past-reference`, `present-reference`, `future-reference`, and `document-creation-time` (document creation time). Unlike time expressions, the pre-defined metanodes don’t correspond to linguistic material in the text.  As mentioned
above, there is a generic `:depends-on` relation between all nodes
in the temporal superstructure.

##### Part 4-2-1-2. Time expressions

The other type of node in the temporal superstructure are time
expressions. Annotators should identify all time expressions in a document and add them to the temporal superstructure before annotating events.

Time expressions are broken down into a taxonomy that
determines their representation in the temporal superstructure (see
Table 1 in Zhang & Xue (2018), reproduced here in Table 13.

| Taxonomy | Taxonomy | Taxonomy | Taxonomy | Examples | Possible Reference Times |
|---|---|---|---|---|---|
| Time Expressions |  |  |  |  |  |
| Time Expressions | Locatable Time Expressions | Concrete | Absolute | May 2015 | root |
| Time Expressions | Locatable Time Expressions | Concrete | Relative | today, two days later | document-creation-time, another Concrete |
| Time Expressions | Locatable Time Expressions | Vague | Vague | nowadays | Present/Past/future-reference |
| Time Expressions | Unlocatable Time Expressions | Unlocatable Time Expressions | Unlocatable Time Expressions | every month | -- |

First, time expressions are distinguished based on whether they are
locatable on a timeline or not. Unlocatable time expressions are time
expressions which refer to the duration (*for three hours*) or
quantification (*every day*) of an event. Unlocatable time expressions
are not represented in the temporal dependency structure at any level. They do influence the aspect annotation, however (see Part 3-3-1).

<!-- (they do influence the aspect annotation; see §3) -->

All locatable time expressions are represented in the temporal
superstructure. Locatable time expressions are divided between concrete
and vague time expressions. Vague time expressions (e.g. *nowadays, in
the old days*) are represented as the children of `present-reference`,
`past-reference`, or `future-reference`. Concrete time expressions
are divided into relative and absolute time expressions. Relative
concrete time expressions (*yesterday, the week before*) are represented
as the children of either `document-creation-time` (as in *yesterday*) or
another concrete time expression on which they depend for their
interpretation (as in *the week before*). Finally, absolute concrete
time expressions (*in 2019*) are represented as children of
`root`.

#### Part 4-2-2. Temporal relations

##### Part 4-2-2-1. Choosing the right temporal relation

Once time expressions have been identified and annotated in the temporal dependency, annotators select temporal relations for the events in a text (see Part 3-1-1 for event ID guidelines). Each event is annotated as the child of either a time
expression in the superstructure or another event (or both). The set of
temporal relations are shown below. Note that the labels characterize
the relation from child to parent.

`:contained`: child is entirely contained within the parent; parent begins before child and parent ends after child (Note: this is called ‘Includes’ in Zhang & Xue 2018).

`:after`: child is after parent.

`:before`: child is before parent.

`:overlap`: child and parent overlap (either partially or fully).

The goal of this temporal annotation scheme is to give each event the
most precise temporal location possible. We also want to avoid adding
annotations which do not give any additional information (i.e., the
relation falls out logically from the other annotations). Follow the steps below to determine the most accurate and precise reference time for each event (but see Part 4-2-2-1-1 below for exceptions) . All events need to receive at least one temporal annotation, but may receive two in cases where an event needs to be linked to both a time expression and another event.

1. If there is a time expression in the same line as the event, link the event to it with the proper relation (although see exception below). If the event does not receive an annotation at this step, proceed to step 2. If an event does receive an annotation at this step, proceed to step 4.

     - **Exception:** The only scenario in which an event which has a clear temporal
        relation with a time expression doesn’t need to have this relation
        annotated is when the relation logically falls out from other
        annotations. This is the case when an event is `:contained` in another event, which itself is
    `:contained` in a time expression. That is, if
        event A is `:contained` within event B (i.e., a
        subevent) and event B is `:contained` within a time expression,
        then logically, event A must also be `:contained`
        within the time expression and therefore this relation doesn’t need to be
        annotated.

2. At this point, consider time expressions in other lines in the text. If the event has a `:contained` relation to     any time expression in the text, annotate that relation. Note that the same exception applies here as in 1. If an event doesn't receive an annotation at this step, proceed to step 3. If an event does receive an annotation at this step, proceed to step 4.

3. If an event is not linked to a time expression, then the next best reference time is another event in the text.  Good reference time events (i.e., parents in the temporal dependency) meet all of the criteria listed below. Often, the most appropriate parent is the event in the immediately preceding line or clause. Starting with the immediately preceding event in the text and working back through the events in the preceding lines, find an event that is a good parent. If there isn't a good parent event in the text, proceed to step 5. Otherwise, the temporal annotation for the event is complete.

    a. The parent event is a Process (or finer-grained subtype) in the Aspect annotation

    b. The parent event has a compatible modal annotation:
        the parent event and child event have the same parent and the same edge value in the modal dependency OR
        the parent event has a `:full-affirmative` relation to the `author` node in the modal dependency

    c. There is a clear temporal relation between the parent event and the child event

4. If an event does get a relation to a time expression, a second annotation that specifies its relationship with another event may also be added. This is the case when a set of events are all `:contained` within the same time expression. The first event in the set of events only needs to be linked to the time expression. Subsequent events can receive two temporal annotations: one that relates it to the time expression and one that relates it to another event in the set.

5. Finally, if the event cannot be linked to either a time expression nor another event, then link it to the appropriate tense metanode.

An example is shown below in (1), an excerpt from a description of the Pear Story film.

Example 4-2-2-1 (1)

```
snt15   A-nd u-h and then he gets down out of the tree,
(s15g / get-05
    :ARG1 (s15p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s15d / down)
    :source (s15t / tree
        :refer-number singular)
    :aspect performance
    :temporal (s15t2 / then)
    :modal-strength full-affirmative)

(s15s0 / sentence
    :modal ((root :modal author)
            (author :full-affirmative s15g))
    :temporal ((past-reference :contained s15g)))

snt16   and he dumps all his pears into the basket
(s16d / dump-01
    :ARG0 (s16p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s16p2 / pear
        :quant (s16a / all)
        :possessor s16p)
    :aspect performance
    :goal (s16b / basket
        :refer-number singular)
    :modal-strength full-affirmative)

(s16s0 / sentence
    :modal ((root :modal author)
            (author :full-affirmative s16d))
    :temporal ((s15g :after s16d)))

snt17   and the basket's full,
(s17h / have-mod-91
    :ARG1 (s17b / basket
        :refer-number singular)
    :ARG2 (s17f / full)
    :aspect state
    :modal-strength full-affirmative)

(s17s0 / sentence
    :modal ((root :modal author)
            (author :full-affirmative s17h))
    :temporal ((s16d :overlap s17h)))

snt18   and one of the pears drops down to the floor,
(s18d / drop-01
    :ARG1 (s18p / pear
        :quant 1
        :ARG2-of (s18i2 / include-91
            :ARG1 (s18p2 / pear
                :refer-number plural)))
    :ARG4 (s18f / floor
        :refer-number singular)
    :direction (s18d2 / down)
    :aspect performance
    :modal-strength full-affirmative)

(s18s0 / sentence
    :modal ((root :modal author)
            (author :full-affirmative s18d))
    :temporal ((s16d :after s18d)))
```

The first event in this excerpt (`s15g`) is linked to a tense metanode, as there are no time expressions in the clause and there are no previous events in the excerpt. The next event (`s16d`) is linked to the immediately preceding event in the text (`s15g`) because it fits all of the criteria for a good reference time: its aspect annotation is a type of Process, it has a full-affirmative relation to the `author` node, and there is a clear temporal relation between the two events. In a similar way, `s17h` is linked to `s16d`. For the final event in the excerpt (`s18d`), the previous event in the text does not make a good reference time. Since `s17h` is a State (not a Process), it does not fit the criteria for a good reference time. Therefore, `s18d` is linked to the next event back in the text `s16d`.

###### Part 4-2-2-1-1. Special cases

There are certain types of modal constructions that require special treatment in the temporal annotation. Events that are related in the modal dependency are generally related in the temporal dependency as well. The rest of this section covers event-event relations; when time expressions are present in the text, those temporal relations should be annotated in addition to the ones described below.

**Complement-taking predicates**

Events that are linked to a complement-taking predicate in the modal dependency should also be linked in the temporal dependency. The complement-taking predicate acts as the reference time for its complement. That is, the complement is the child of the complement-taking predicate in the temporal dependency. There can be various types of temporal relations between complement-taking predicates and their complements, shown in (1)-(3).

Example 4-2-2-1-1 (1)

```
I saw him knock on the door.

(s1s / see-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1k / knock-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s1d / door
            :refer-number singular))
    :aspect performance)
    :aspect state
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :overlap s1k)))
```

Example 4-2-2-1-1 (2)

```
I want to cook dinner.
(s1w / want-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1c / cook-01
        :ARG0 s1p
        :ARG1 (s1d / dinner)
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((present-reference :contained s1W)
            (s1w :after s1c)))
```

Example 4-2-2-1-1 (3)

```
I wish she had read the book.
(s1w / wish-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1r / read-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s1b / book
            :refer-number singular)
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((present-reference :contained s1W)
            (s1w :before s1c)))
```

In cases where there are multiple complements of the same predicate, the annotator must consider whether the complements are ordered with respect to each other. When they are ordered, only one complement is annotated as the child of the main predicate in the temporal dependency. The remaining complement(s) are then linked to other complements in whichever way most fully specifies their temporal ordering. The complement which is closest in time to the main predicate is the one that is linked to the main predicate.

Example 4-2-2-1-1 (4)

```
I want to go to the city and visit a museum.
(s1w / want-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1g / go-01
        :ARG1 s1p
        :ARG4 (s1c / city
            :refer-number singular)
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((present-reference :contained s1W)
            (s1w :after s1c)))
```

The complement-taking predicate itself follows the same process as other events (see Part 4-2-2-1) in order to select its reference time (i.e., its parent in the temporal dependency).

**Reporting events**

Reporting events are treated similarly to complement-taking predicates. Generally, reported events are linked to the reporting predicate with the appropriate temporal relation. When there are multiple reported events, annotators consider if they are ordered with respect to each other. In all cases, at least one of the reported events must be linked to the reporting predicate. Other reported events may be linked to each other or to the reporting predicate.

In (5), both the arriving event and the eating event occur before the saying event. Since there is a clear ordering of the arriving event before the eating event, only one of these events is linked to the saying event. The eating event is closer in time to the saying event, and therefore the eating event is linked to the saying event in the temporal dependency. The arriving event is then linked to the eating event. (The fact that the arriving event also occurred before the saying event logically falls out from the annotations.) Finally, since the meeting event occurs after the saying event, the meeting event is also linked to the saying event.

Example 4-2-2-1-1 (5)

```
Magdalena said she arrived home, ate dinner, and will meet us at the theater.
(s1s / say-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Magdalena"))
    :ARG1 (s1a / and
        :op1 (s1a2 / arrive-01
            :ARG1 s1p
            :ARG4 (s1h / home)
            :aspect performance
            :modal-strength full-affirmative
            :QUOT s1s)
        :op2 (s1e / eat-01
            :ARG0 s1p
            :ARG1 (s1d / dinner)
            :aspect performance
            :modal-strength full-affirmative
            :QUOT s1s)
        :op3 (s1m / meet-03
            :ARG0 s1p
            :ARG1 (s1p2 / person
                :refer-person 1st
                :refer-number plural)
            :place (s1t / theater
                :refer-number singular)
            :aspect performance
            :modal-strength full-affirmative
            :QUOT s1s))
    :aspect performance
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1e)
            (s1e :before s1a)
            (s1s :after s1m)))
```

**Purpose clauses**

Events in purpose clauses (i.e., annotated with a `:purpose` relation at the sentence level) are linked to the event in the main clause in the temporal dependency. The temporal relation between the event in the purpose clause and the main clause event is always `:after`.

Example 4-2-2-1-1 (6)

```
He went home (in order) to wash the dishes.
(s1g / go-01
    :ARG1 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG4 (s1h / home)
    :purpose (s1w / wash-01
        :ARG0 s1p
        :ARG1 (s1d / dish
            :refer-number plural)
        :aspect performance
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)

(s / sentence
    :temporal ((past-reference :contained s1g)
            (s1g :after s1w)))
```

##### Part 4-2-2-2. Contained or Overlap

Following the definition of the `:contained` and the
`:overlap` relations, `:overlap` must be used rather
than `:contained` for events that are perfectly simultaneous
(beginning and ending at the exact same time point). The
`:contained` relation will instead be used for all relations
where both the beginning and ending of one event are included within the
temporal duration of a second event - this includes subevent structure
and also events which have a purely temporal (and not causal or
conceptual) relation between them.

##### Part 4-2-2-3. Causally-related events

Causal relations between events are always annotated as
`:after` relations. This means that in examples such as *the
crops grew well because it rained enough*, `(rain :after grow)`
is annotated even though the causing event (raining) and the caused
event (growing) partly overlap. If the causal relationship is explicitly
predicated, it is identified as a separate event. It is then annotated
as `:after` the causing event, and the caused event is
annotated as following it. Therefore, *the opening of the food can
prompted my cat to meow* is annotated as `(open :after prompt)`
and `(prompt :after meow)`.

<!-- 1.  The term “event” is used throughout these guidelines as a
    superordinate category subsuming processes and states, as is
    customary in the cognitive linguistic tradition. The more specific
    category of telic processes (which is also often called “event” in
    the formal semantics literature), we will refer to as “performance”
    (see §3). 2.  We are considering using the NA value for non-real
    events as well, but for now, these types of events should receive
    one of the other aspect values. -->

### Part 4-3. Modal Dependency

UMR represents modal strength and polarity as a dependency structure.
The nodes are either events or conceivers (i.e., a source, an entity
whose perspective on an event is modelled in the text). The edges in the dependency structure correspond to modal strength and polarity values (i.e., how certain a specific conceiver is about the occurrence of the event in the real world). Annotators do not have to construct the dependency structure directly, but it can be built up “behind the
scenes” by annotating some modal/polarity information and leveraging
the participant role annotation.

The modal annotation captures the modal strength of events, but not the modal type of the event (i.e., epistemic/evidential, deontic,
permissive, etc.). These modal strengths are annotated based on a
lattice of annotation values that differ in terms of granularity. An
example of the UMR annotation and the underlying modal dependency
structure is shown below in (1).

Example 4-3 (1)

![Modal dependency structure](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Modal%20Dep_2022.jpg)

```
Martin said that the package has probably already arrived.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Martin")
    :ARG1 (a / arrive-01
        :ARG1 (p / package
            :refer-number singular)
        quot: s
        :modal-strength partial-affirmative)
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1a))
    :modal ((author :full-affirmative s1p)
            (author :full-affirmative s1s)
            (s1p :partial-affirmative s1a)))
```

The *say*-event and the *arrive*-event each get a modal strength value (`:modal-strength`), which can then be represented
in the dependency as an edge between the event and the relevant conceiver/source. The
`:quote` value indicates than an event is
being reported, and the participant role annotation can be used to
automatically select the conceiver for the reported event(s), here,
*Martin*.

This simplified, mostly sentence-level, annotation process is step 0 of the road map for modal annotation. Step 1 builds on this step to end up at a fully specified modal dependency structure. This means that Stage 1 annotation involves first doing the Stage 0 modality annotations. (This contrasts with participant roles, where annotators can largely ignore Stage 0 if the annotation language has existing frame files.)

#### Part 4-3-1. Stage 0

There are two types of modal annotations at Stage 0: a
`:modal-strength` annotation that consists of a
single epistemic strength/polarity value, and a dependency annotation
that indicates a relation between two events. The link between a modal event and the event(s) that it modalizes is written in the document-level modal
dependency; `:quote` marks the link between a reporting
event and the event(s) that it reports. Additionally, events in purpose clauses and events in conditional constructions must be taken up in the modal dependency tree. The right structure of the modal dependency graph for these events will be extrapolated from the sentence-level annotation: events in purpose clauses are daughters of events in the main clause they depend on, and are connected to them with the `:purpose` participant role. This can be leveraged to embed the purpose-event underneath the correct parent in the modal dependency graph as well. For conditionals, similarly, the protasis event will be embedded under the apodosis event with a `:condition` relation, or the protasis and apodosis events will both be ```:ARG1``` and ```:ARG2``` of a `have-condition-91` node. Again, this information will be taken up in the eventual modal dependency graph without annotators needing to indicate it a second time in the document-level modal annotation workflow.
The `:modal-strength` annotation applies to all events, except for those under the scope of a modal identified as its own event (i.e., events with `:mod` relations). This
is summarized below.

| **Event type** | **UMR Treatment** |
|---|---|
| Events under the scope of modals | child of the modal event (CPT) in the document-level modal dependency |
| Events under the scope of reporting events | `:modal-strength` annotation, `:quote` relation to reporting event |
| All other events | `:modal-strength` annotation |

Table 14: Modal relations at Stage 0

##### Part 4-3-1-1. modstr values

The modal strength values correspond to epistemic strength, i.e. the
author or conceiver’s certainty about the occurrence of the event in the real world, or certainty about another conceiver’s mental content. Based on Boye (2012), a typological study of modal systems across languages, and following FactBank (Pustejovsky et al. 2005), the UMR annotation is based around three levels of modal strength: `Full`, `Partial`, and `Neutral`, illustrated in (1).

Example 4-3-1-1 (1)

Example 4-3-1-1 (1a) Full:
The cat already **ate** breakfast.

Example 4-3-1-1 (1b)
Partial:
The cat probably already **ate** breakfast.

Example 4-3-1-1 (1c)
Neutral:
The cat might have already **eaten** breakfast.

The `Full` modal strength value, as in (1a), corresponds to complete certainty; that is, the conceiver is 100% certain that the event occurs in the real world. The `Neutral` modal strength value, shown in (1c), indicates the possibility of the event; essentially, this corresponds to 50/50 certainty that the event occurs in the real world. The `Partial` modal strength value, as in (1b), falls between the `Full` and `Neutral` values; the conceiver believes that more likely than not, the event occurs in the real world.

But, `Full`, `Partial`, and `Neutral` aren’t the only possible modal strength annotation values. Languages differ in the modal strength distinctions that are conventionalized in their grammar. In order to accommodate these differences, we use a typological lattice of annotation values, constructed based on the structure of the annotation category across languages (Van Gysel et al. 2019).

One level of granularity in the lattice is designated as the “base
level”: annotators are encouraged to use categories from this level as
the default. These values are selected as the base level because these
distinctions occur the most frequently across languages. The higher and lower levels, respectively, contain equally typologically-motivated coarser-grained and finer-grained categories, which can be used when a language conventionalizes these distinctions in its grammar. Such lattices capture the idea that many semantic categories are structured as hierarchical scales, where the middle values can group together with either end, but the extremes of the scale are highly unlikely to be categorized together in any language. For example, no language has a grammatical form that is used for both `Full` and `Neutral` epistemic strength, but not `Partial`. The typological lattice for epistemic strength is shown below.

![Modal strength lattice](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Affirmative%20Modal%20Strength%20Lattice_2022.png)

![Modal strength lattice](https://github.com/umr4nlp/umr-guidelines/blob/master/Guidelines_figures/Negative%20Modal%20Strength%20Lattice_2022.png)

This lattice is based around the base level of `Full` vs. `Partial` vs.
`Neutral`, but also allows for the annotation of more coarse-grained
values that lump together the distinctions in the base level, and more
fine-grained annotation values. For contexts where it is unclear if the modal strength is `Full` or `Partial`, the `Non-neutral` value can be used; if it is unclear whether the modal strength is `Partial` or `Neutral`, then the `Non-full` value can be used. The most fine-grained modal strength values are generally used with languages that have grammatical forms that encode the relevant distinction.

Also following FactBank (Pustejovsky et al. 2006), the `:modal-strength`
annotation combines the epistemic strength values with a binary polarity distinction (`Affirmative`, `Negative`). This results in six modal strength/polarity values for the default level, shown below. Both the affirmative values and the negative values have their own set of related coarse-grained and fine-grained values.

| **Label** | **Value** |
|---|---|
| ```full-affirmative``` | full strength, affirmative polarity |
| ```partial-affirmative``` | partial strength, affirmative polarity |
| ```NeutAFf``` | neutral strength, affirmative polarity |
| ```neutral-negative``` | neutral strength, negative polarity |
| ```partial-negative``` | partial strength, negative polarity |
| ```full-negative``` | full strength, negative polarity |

These values and their interpretation are shown below; the corresponding FactBank values are in parentheses.

```full-affirmative```: full affirmative support; complete certainty that the event occurs (CT+)
```partial-affirmative```: partial affirmative support; there is strong, but not definitive certainty that the event occurs (PR+)
```neutral-affirmative```: affirmative neutral support; there is neutral certainty that the event occurs/doesn’t occur; event is expressed positively (PS+)
```neutral-negative```: negative neutral support; there is neutral certainty that the event occurs/doesn’t occur; negation of event is expressed (PS-)
```partial-negative```: partial negative support; there is strong but not definitive certainty that the event does not occur (PR-)
```full-negative```: full negative support; complete certainty that the event does not occur (CT-)

Degree of certainty corresponds most straightforwardly to the degree of confidence of a conceiver (often, the author) in the occurrence of an episodic event, i.e. the epistemic continuum from certainty to
possibility. We use these same values for the evidential continuum from direct evidence to second-hand (reported or inferred) evidence; see Part 4-3-1-1-2 below). And these values are
interpreted into the domain of future-oriented or deontic modality, as
explained in Part 4-3-1-1-3. The interpretation of
the value - as epistemic, evidential or deontic - is not reflected in
the modal strength annotation.

###### Part 4-3-1-1-1. Non-future events

For non-future (non-deontic) events, the `modstr` values correspond to the author’s level of certainty towards the occurrence of the event in the real world. Events presented as fact are annotated with
`full-affirmative`, while events for which the author categorically denies their occurrence are annotated `full-negative`. When the author doesn’t present the
event as fact, but has a higher level of certainty towards the event
either being true or not true, this is annotated as
`partial-affirmative` or, when the polarity is negative, `partial-negative`. When the author doesn’t lean either direction towards the event being true in the real world or not, the event is annotated as `neutral-affirmative` or
`neutral-negative`, depending on the polarity of the
linguistic expression. These strength values are exemplified in
(1).

Example 4-3-1-1-1 (1)

Example 4-3-1-1-1 (1a)
```
The dog barked last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength full-affirmative)
```
Example 4-3-1-1-1 (1b)
```
The dog probably barked last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength partial-affirmative)
```
Example 4-3-1-1-1 (1c)
```
The dog may have barked last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength neutral-affirmative)
```
Example 4-3-1-1-1 (1d)
```
The dog may not have barked last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength neutral-negative)
```
Example 4-3-1-1-1 (1e)
```
The dog probably didn't bark last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength partial-negative)
```
Example 4-3-1-1-1 (1f)
```
The dog didn't bark last night.
(s1b / bark-01
    :ARG0 (s1d / dog
        :refer-number singular)
    :temporal (s1n / night
        :mod (s1l / last))
    :aspect endeavor
    :modal-strength full-negative)
```

###### Part 4-3-1-1-2. Evidential justification

Following Boye (2012) and Saurí and Pustejovsky (2009), we conflate evidential justification with epistemic support. Boye (2012) finds that there is cross-linguistic evidence for lumping epistemic support and evidential justification together into the same relations. Languages may encode direct evidential justification (sensory perception) with the same forms as full epistemic support; indirect justification (hearsay, inferential) may be encoded by the same forms as partial epistemic support.

Example (1) shows how direct and indirect justification correspond to epistemic support.

Example 4-3-1-1-2 (1)

Example 4-3-1-1-2 (1a)
```
(I saw) Mary feed the cat.
(s1s / see-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1f / feed-01
        :ARG0 (s1p2 / person
            :name (s1n / name :op1 "Mary"))
        :ARG2 (s1c / cat
            :refer-number singular)
        :aspect performance
        **:modal-strength full-affirmative**)
    :aspect state
    :modal-strength full-affirmative)
```
Example 4-3-1-1-2 (1b)
```
Mary must have fed the cat.
(s1f / feed-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Mary"))
    :ARG2 (s1c / cat
        :refer-number singular)
    :aspect performance
    :modal-strength partial-affirmative)
```

In (1a), the author has direct knowledge of the feeding event, by way of witnessing it. Therefore, *feed* is annotated with `Aff` modal strength. In (1b), however, *must* signals that the author is inferring that the feeding event occurred without direct, perceptual knowledge. Therefore, *fed* in (1b) is annotated with `Prt` modal strength.

###### Part 4-3-1-1-3. Future events and deontic modality

For events presented as (potentially) happening in the future,
`:modal-strength` refers to the predictability of
the occurrence of the event in the future, as presented by the author.
Predictive future has full strength (`full-affirmative`
or `full-negative`); intentions and commands
correspond to partial strength (`partial-affirmative` or
`partial-negative`); and desire and permission
correspond to neutral (`neutral-affirmative` or
`neutral-negative`) strength. Keep in mind that events under the scope of modals identified as their own event don't receive any `:modal-strength` value at all. This section refers to deontic meanings indicated by grammaticalized modals that don't fit the criteria to be identified as events.

This is illustrated in (1).

Example 4-3-1-1-3 (1)

Example 4-3-1-1-3 (1a)
```
I will go to Santa Fe.
(s1g / go-01
    :ARG1 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG4 (s1c / city
        :name (s1n / name
            :op1 "Santa"
            :op2 "Fe"))
    :aspect performance
    :modal-strength full-affirmative)
```
Example 4-3-1-1-3 (1b)
```
You must go to Santa Fe.
(s1g / go-01
    :ARG1 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG4 (s1c / city
        :name (s1n / name
            :op1 "Santa"
            :op2 "Fe"))
    :aspect performance
    :modal-strength partial-affirmative
    :mode Imperative)
```

Example 4-3-1-1-3 (1c)
```
You can go to Santa Fe.
(s1g / go-01
    :ARG1 (s1p / person
        :refer-person 2nd
        :refer-number singular)
    :ARG4 (s1c / city
        :name (s1n / name
            :op1 "Santa"
            :op2 "Fe"))
    :aspect performance
    :modal-strength neutral-affirmative)
```
The predictive future, as in (1a), is annotated with
full modal strength because it presents the future event as a certainty
(i.e., it is as certain as is possible for future events). Commands, as
in (1b), are annotated with partial modal strength
because they present the future event as less likely than the predictive
future, but more likely to happen than the neutral strength deontics.
Finally, permission, as in (1c), is annotated as
neutral strength, since even if someone has permission to do something, there is no guarantee they will.

##### Part 4-3-1-2. Events under the scope of a modal event

Events under the scope of a modal identified as its own event get no `:modal-strength` of their own in the
sentence-level graph. They are linked to the relevant modal event in the document-level modal dependency,
`(modal event :strength event)`, as shown below in (1). (Earlier versions wrote a sentence-level `:modpred`
relation for this; it is no longer used.)

Example 4-3-1-2 (1)

Example 4-3-1-2 (1a)
```
Mary wants to visit France.
(w / want-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (v / visit-01
        :ARG0 p
        :ARG1 (c / country
            :name (n / name :op1 "France"))
        :aspect performance
    :aspect state
    :modal-strength full-affirmative

(s / sentence
    :temporal ((document-creation-time :overlap s1w)
           (s1w :after s1v))
    :modal ((author :full-affirmative s1p)
(s1p :full-affirmative s1w)
        (s1w :unspecified s1v))
```
Example 4-3-1-2 (1b)
```
Rob thinks the dog escaped through the fence.
(s1t / think-01
    :ARG0 (s1p / person
        :name (s1n / name
            :op1 "Rob"))
    :ARG1 (s1e / escape-01
        :ARG0 (s1d / dog
            :refer-number singular)
        :path (s1f / fence)
        :aspect performance)
    :aspect state
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((document-creation-time :overlap s1t)
            (s1t :before s1e))
    :modal ((author :full-affirmative s1p)
            (s1p :full-affirmative s1t)
            (s1t :unspecified s1e)))
```
Example 4-3-1-2 (1c)
```
They probably decided to leave on Monday.
(s1d / decide-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s1l / leave-01
        :ARG0 s1p
        :temporal (s1d / date-entity
            :weekday (s1m / Monday))
        :aspect performance)
    :aspect performance
    :modal-strength partial-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1d)
            (s1m :contained s1l))
    :modal ((author :partial-affirmative s1p)
            (s1p :full-affirmative s1d)
            (s1d :unspecified s1l)))
```
Example 4-3-1-2 (1d)
```
His parents forbid him from smoking.
(s1f / forbid-01
    :ARG0 (s1p / person
        :ARG0-of (s1k / kinship)
        :ARG1 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG2 (s1p3 / parent)
        :refer-number plural)
    :ARG1 (s1s / smoke-01
        :ARG0 s1p2
        :aspect process)
    :ARG2 s1p2
    :aspect state
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((document-creation-time :overlap s1f)
            (s1f :overlap s1s))
    :modal ((author :full-affirmative s1p)
            (s1p :full-affirmative s1f)
            (s1f :unspecified s1s)))
```

Note that the modal itself is annotated with a
`:modal-strength` value (if it is not under the
scope of another modal). The actual modal value imparted by the modal
event is not annotated at Stage 0. It will be taken up in the lexical entries of modal complement-taking predicates and space-builders as the lexicon is being built, and will then automatically replace the unspecified link between the modal event and the modalized event in the document-level structure.

##### Part 4-3-1-3. quot relation

Events under the scope of a reporting predicate or a speech predicate
are annotated with a `:quote` relation to the
reporting or speech predicate. Unlike events under the scope of modals,
these events are also annotated with a
`:modal-strength` value.

Example 4-3-1-3 (1)

Example 4-3-1-3 (1)
```
Mary said that she went to Santa Fe.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (g / go-01
        :ARG1 p
        :ARG4 (c / city
            :name (n2 / name
                :op1 "Santa"
                :op2 "Fe))
        :aspect performance
        :modal-strength full-affirmative
        :quote s
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1g))
    :modal ((author :full-affirmative s1s)
            (author :full-affirmative s1p)
            (s1p :full-affirmative s1g)))
```
Example 4-3-1-3 (1a)
```
The New York Times reported that Congress voted on the bill this afternoon.
(s1r / report-01
    :ARG0 (s1n / newspaper
        :name (s1n2 / name
            :op1 "The"
            :op2 "New"
            :op3 "York"
            :op4 "Times"))
    :ARG1 (s1v / vote-01
        :ARG0 (s1g / government-organization
            :name (s1n3 / name
                :op1 "Congress"))
        :ARG1 (s1b / bill
            :refer-number singular)
        :temporal (s1a / afternoon
            :mod (s1t / this))
        :aspect performance
        :modal-strength full-affirmative
        :quote s1r)
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1r)
            (s1a :contained s1v))
    :modal ((author :full-affirmative s1r)
            (author :full-affirmative s1n)
            (s1n :full-affirmative s1v)))
```
Example 4-3-1-3 (1b)
```
Mary might have said that she went to Santa Fe.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (g / go-01
        :ARG1 p
        :ARG4 (c / city
            :name (n2 / name
                :op1 "Santa"
                :op2 "Fe))
        :aspect performance
        :modal-strength full-affirmative
        :quote s
    :aspect performance
    :modal-strength neutral-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1g))
    :modal ((author :neutral-affirmative s1s)
            (author :neutral-affirmative s1p)
            (s1p :full-affirmative s1g)))
```
Example 4-3-1-3 (1c)
```
Mary didn’t say that she went to Santa Fe.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (g / go-01
        :ARG1 p
        :ARG4 (c / city
            :name (n2 / name
                :op1 "Santa"
                :op2 "Fe))
        :aspect performance
        :modal-strength full-affirmative
        :quote s
    :aspect performance
    :modal-strength full-negative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1g))
    :modal ((author :full-negative s1s)
            (author :full-negative s1p)
            (s1p :full-affirmative s1g)))
```
Example 4-3-1-3 (1d)
```
Mary said that John might have gone to Santa Fe.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (g / go-01
        :ARG1 (p2 / person
            :name (n2 / name :op1 "John"))
        :ARG4 (c / city
            :name (n3 / name
                :op1 "Santa"
                :op2 "Fe))
        :aspect performance
        :modal-strength neutral-affirmative
        :quote s
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1g))
    :modal ((author :full-negative s1s)
            (author :neutral-affirmative s1p)
            (s1p :neutral-affirmative s1g)))
```
Example 4-3-1-3 (1e)
```
Mary said that John probably didn’t go to Santa Fe.
(s / say-01
    :ARG0 (p / person
        :name (n / name :op1 "Mary"))
    :ARG1 (g / go-01
        :ARG1 (p2 / person
            :name (n2 / name :op1 "John"))
        :ARG4 (c / city
            :name (n3 / name
                :op1 "Santa"
                :op2 "Fe))
        :aspect performance
        :modal-strength partial-negative
        :quote s
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1s)
            (s1s :before s1g))
    :modal ((author :full-negative s1s)
            (author :partial-negative s1p)
            (s1p :partial-negative s1g)))
```
As can be seen above, both the reporting predicate and the reported
events are annotated with a `:modal-strength` value.
The `:modal-strength` value of the reporting
predicate corresponds to the author’s certainty that the reporting event
happened. The `:modal-strength` value associated
with the reported events corresponds to the certainty with which the
sayer/reporter reports the events. For example, in
(1d), the author is certain about the saying event,
so it is annotated with `Aff`; but Mary is
unsure about the reality of the going event, and therefore it is
annotated with `Neut` modal strength.

##### Part 4-3-1-4. purpose relation

Events in purpose clauses are annotated with both a
`:modal-strength` value in the document-level annotation, and with the `:purpose` participant role relation to the main clause event in the sentence-level annotation.

Example 4-3-1-4 (1)
```
They dropped water in order to fight the fire.
(s1d / drop-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s1w / water)
    :purpose (s1f / fight-01
        :ARG0 s1p
        :ARG1 (s1f / fire)
        :aspect activity
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1d)
            (s1d :after :s1f))
    :modal ((author :full-affirmative s1d)
            (author :full-affirmative s1p)
            (s1p :partial-affirmative purpose)
            (purpose :full-affirmative s1f)))
```
Example 4-3-1-4 (2)
```
He walked quickly in order to not arrive late.
(s1w / walk-01
    :ARG0 (s1p / person
        :refer-person 3rd
        :refer-number singular)
    :manner (s1q / quickly)
    :purpose (s1a / arrive-01
        :ARG1 s1p
        :temporal (s1l / late)
        :aspect performance
        :modal-strength full-negative)
    :aspect activity
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((past-reference :contained s1w)
            (s1w :after s1a))
    :modal ((author :full-affirmative s1w)
            (author :full-affirmative s1p)
            (s1p :partial-affirmative purpose)
            (purpose :full-negative s1a)))
```

The `:modal-strength` value represents any modals or
negation that are present within the purpose clause. That is, this value
doesn’t capture the fact that the purpose clause itself imparts a
non-full epistemic stance on its events; that is captured by the
`:purpose` relation.

##### Part 4-3-1-5. condition relation

The `:condition` relation in the sentence-level annotation indicates the relationship between events in conditional constructions. These events
also receive a `:modal-strength` annotation. As can
be seen in (1), the event in the protasis is annotated with a `:condition` relation to the event in the
apodosis.

Example 4-3-1-5 (1)

Example 4-3-1-5 (1a)
```
If she’s hungry, I’ll feed her dinner.
(s1f / feed-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1d / dinner)
    :ARG2 (s1p2 / person
        :refer-person 3rd
        :refer-number singular)
    :condition (s1h / hunger-01
        :ARG0 s1p2
        :aspect state
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((document-creation-time :overlap s1h)
            (document-creation-time :after s1f))
    :modal ((author :neutral-affirmative have-condition)
            (have-condition :full-affirmative s1h)
            (have-condition :full-affirmative s1f)))
```
Example 4-3-1-5 (1b)
```
If she’s hungry, maybe I’ll cook pasta.
(s1c / cook-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number singular)
    :ARG1 (s1p2 / pasta)
    :condition (s1h / hunger-01
        :ARG0 (s1p3 / person
            :refer-person 3rd
            :refer-number singular)
        :aspect state
        :modal-strength full-affirmative)
    :aspect performance
    :modal-strength neutral-affirmative)
(s / sentence
    :temporal ((document-creation-time :overlap s1h)
            (document-creation-time :after s1c))
    :modal ((author :neutral-affirmative have-condition)
            (have-condition :full-affirmative s1h)
            (have-condition :neutral-affirmative s1c)))
```
Example 4-3-1-5 (1c)
```
If she isn’t hungry, we’ll just watch a movie.
(s1w / watch-01
    :ARG0 (s1p / person
        :refer-person 1st
        :refer-number plural)
    :ARG1 (s1m / movie)
    :mod (s1j / just)
    :condition (s1h / hunger-01
        :ARG0 (s1p2 / person
            :refer-person 3rd
            :refer-number singular)
        :aspect state
        :modal-strength full-negative)
    :aspect performance
    :modal-strength full-affirmative)
(s / sentence
    :temporal ((document-creation-time :overlap s1h)
            (document-creation-time :after s1w))
    :modal ((author :neutral-affirmative have-condition)
            (have-condition :full-negative s1h)
            (have-condition :full-affirmative s1c)))
```
As with purpose clauses, the `:modal-strength` value
doesn’t capture the uncertainty imparted by the conditional construction
itself; it corresponds to any negation or modals which are expressed
inside of the conditional construction. The modal value of the
conditional construction is captured by the
`:condition` value.

##### Part 4-3-1-6. Modal dependency structure

At Stage 0, there are some pieces of the modal dependency structure that
are unspecified. The modal strength that a modal verb imparts on its
complement is one of these pieces. As the modal annotation progresses,
this information is added to the frame files for modal verbs. For
example, the complements of English *want* have a
`:modal-strength neutral-affirmative` value; this will be indicated
in the frame file as shown below.

```
Predicate: want.01
    Roles:
    Arg0: wanter
    Arg1: thing wanted
    Arg2: beneficiary
    Arg3: in-exchange-for
    Arg4: from

:modal-strength of complement: neutral-affirmative
```

For the complements of modals, the `:modal-strength`
values work largely the same way that they do for other events; however,
they reflect the beliefs of the
`:experiencer` participant of the modal
event, who is often not the author. For example, in
(1), Mary believes that the visit event may take
place in the future (`neutral-affirmative` strength), but
the author disagrees.

\[4-3-1-6 (1)\] Mary wants
to visit France next month, but I don’t think that’s possible.

The value associated with the modal event in its frame file corresponds
to Mary’s beliefs, as the `:experiencer` of
the wanting event.

Some predicates impart full, positive
(`full-affirmative`) strength on their complements,
often called factive predicates (e.g., *manage to*). Strong epistemic
modals (e.g., *expect that, deduce*) and strong deontic modals,
including intention modals (e.g., *plan to, decide to*) and obligation
modals (e.g., *need, demand*), impart `partial-affirmative`
strength on their complements. Weak deontic modals, including desire
(e.g., *want*) and permission (e.g., *allow*), impart
`neutral-affirmative` strength on their complements.
Certain modals may also lexicalize negation, such as *doubt*, *forbid*,
or *wish*. These are annotated with the
`neutral-negative`,
`partial-negative`, and
`full-negative` values, respectively.

#### Part 4-3-2. English modals

This list gives the modal strength value associated with common English
modal constructions (this is certaintly not an exhaustive list). For
modal predicates that are identified as their own event (e.g.,
deontic predicates), the modal strength value characterizes the dependency link between the modal predicate node and its child event. For example, *want* is in the `neutral-affirmative` list, which indicates that there
is a `neutral-affirmative` link between the `want` node and its
complement event node in the full dependency structure.

`full-affirmative` (full affirmative)

  - Simple assertions: declarative sentences

  - Certainty: *certainly, be sure, definitely, necessarily*

  - Predictive future: *will,* non-intentional *be going to*

  - Factual predicates: *manage to, finished*

`partial-affirmative` (partial affirmative)

  - Strong epistemic modals: *must/must have, have to, expect that,
    deduce*

  - Strong epistemic adverbs/adjectives: *probably/be probable that,
    likely/be likely that*

  - Strong deontic modals:

      - Intention: *intend, plan,* intentional *be going to, decide, be
        slated to*

      - Obligation: imperative, deontic *must, have to, should, ought
        to, be required to, need; order to, tell to, demand*

      - Purpose clauses/purposive event nominals: *(in order) to* VERB,
        *for* EVENT.NOM

`neutral-affirmative` (neutral affirmative)

  - Weak epistemic modals: *may, might/might have, could have*

  - Weak epistemic adverbs/adjectives: *maybe, possibly/be possible
    that*

  - Conditionals (done automatically in the conversion from sentence-level to document-level structure)

  - Hope/Fear: *hope, fear, worry, dread*

  - Weak deontic modals

      - Desire: *want, prefer, would like to*

      - Permission: *let, permit, allow*

`neutral-negative` (neutral negative)

  - Doubt: *doubt, call into question, be dubious that, be skeptical
    that*

  - Combination of (some) neutral-affirmative lexical items with negation

`partial-negative` (partial negative)

  - Strong negative deontics: *forbid, ban, disallow*

  - Negative imperatives

  - Combination of (some) partial-affirmative lexical items with negation

`full-negative` (full negative)

  - Negation: *not, never, no* + noun phrase

  - Negative complement taking predicates that entail that the event
    didn’t happen: *deny, prevent, prohibit, block, cease, it is
    impossible that, avoid*

  - Counterfactuals

  - Wishes: *wish*

## Part 5. Annotation Cheat Sheet

 * Sentence-level Annotation
    * Choose the **top node** of the graph for the sentence you are annotating.
        * If the sentence contains **one main event** (typically a lexical verb in a main clause), **annotate it** as the **top of the graph** (see Part 3-1-1 and Part 3-1-3 on how to decide what counts as one event).
            * Highlight the word token that corresponds to the event.
            * If a citation form of it is in the lexicon already, click the "Lexicalized Concept" button and select this lemma.
            * If it is not in the lexicon yet, click the "add to Lexicon" button and create a lexical entry for it first.
        * If the sentence contains a **"non-verbal clause"** concept as its main event, choose the relevant **non-verbal clause predicate** as the top node (see Part 3-1-1-3, Part 3-1-3-5).
        * If the sentence contains **multiple events** expressed in multiple clauses, decide what the top node is **based on the logical relation** between the events:
            * If one event is an argument of another event, choose the **main event** as the top node.
            * If one event is a **circumstantial participant** or **adverbial participant** in another event, choose the **main event** as the top node.
            * If two events are **coordinated** but a fine-grained meaning on the lowest level of the lattice in Part 3-1-6 can be identified, choose the **main event** as the top node following the guidelines in the aforementioned section.
            * If two events are **coordinated** but a fine-grained meaning on the lowest level of the lattice in Part 3-1-6 can not be identified, choose the **relevant coordinator concept** as the top node (see Part 3-1-6).

    * Annotate the **participants** of the top node - these can be both entities and events.
        * For each participant, select the correct **role/relation** from the "roles" drop-down menu:
            * If the top node is an **abstract concept predicate**, use the appropriate **numbered argument roles** or **:opX** roles (see Part 3-2-1-1-1 for non-verbal clause predicates, Part 3-1-6 for discourse relations).
            * If the top node is a **sense-disambiguated lexicalized concept** with frame files, use the relevant **numbered argument roles** (see Part 3-1-4).
            * If the top node is a **lexical event concept without frame files**, use the relevant **general participant roles** (Part 3-2-1-1).
            * For **circumstantial participants** (e.g. temporal and spatial roles, conditions etc.), use the relevant **general participant roles** (see Part 3-2-1-1).
        * Select the correct **concept** (see Part 3-1-3 for identification of participants expressed as part of the same word of the event):
            * If the participant is overtly expressed as a **nominal**, add the **nominal word from the sentence** to the graph.
                * Highlight the word token in the sentence.
                * Click the "Lexicalized Concept" button, and then the word token in the drop-down menu.
            * If the participant is overtly expressed as a **verb** (e.g. complement clause, adverbial), add the **verbal word from the sentence** to the graph.
                * Highlight the word token in the sentence.
                *  If a citation form of it is in the lexicon already, click the "Lexicalized Concept" button and select this lemma.
                * If it is not in the lexicon yet, click the "add to Lexicon" button and create a lexical entry for it first.
            * If the participant is expressed **pronominally**, is **impersonal**, is a **proper noun**, or is **not expressed overtly**, add the correct **named entity concept label** (e.g. _person_, _thing_, _river_ etc.) to the graph (Part 3-1-2).
                * If the participant's name is overt in the sentence:
                    * Choose the correct label from the "Named Entity Types" drop-down menu
                    * Highlight the word tokens corresponding to it and add them using the "Lexicalized Concept" button.
                * If the participant's name is not overt in the sentence
                    * Choose or type the correct label in the "Abstract Concept" drop-down menu and add it using the "Add Abstract Concept" button.
            * If the participant **has been annotated in the graph for this sentence already** (e.g. reentrancy of a main clause participant in a complement clause), select the constant for this participant in the graph and add it using the "Lexicalized Concept" button.
            * If the participant is expressed as a **participant nominalization**, choose either of the following options:
                * Add the word **directly from the sentence** by highlighting it and using the "Lexicalized Concept" button.
                * Add the correct **named entity concept label** to the graph through the "Named Entity Types" or "Abstract Concept" drop-down menu and modify it with an **inverse argument role** to the relevant event concept (see Part 3-2-1-3).
        * **Repeat** these steps for every node you have added that corresponds to an **event concept**.
    * Annote the **modifiers** of each participant.
        * If a participant is modified by a **property concept**, either:
            * Annotate it with an **:ARG1-of** relation to the **have-mod-91** predicate, and complete the argument structure of this predicate (see Part 3-2-1-1-1, Part 3-2-1-3).
            * Select the **:mod** relation from the "roles" drop-down menu, highlight the modifier word token in the sentence, and add it to the graph using the "Lexicalized Concept" button.
        * If a participant is modified by an **event concept** (e.g. a relative clause), annotate it with an **inverse numbered or general participant role** to this event concept, and complete the argument structure of this predicate (see Part 3-2-1-3).
        * If a participant is modified by an **object concept**:
            * Annotate it with the **:mod** relation or one of its more fine-grained sub-relations if it is a **typifying modifier** (see Part 3-2-2).
            * Annotate it with the **:possessor**, **:part-of** (the part is the parent; **:part** when the whole is the parent), or **:ARG0-of (k / have-rel-role-92)** relations if it is an **anchoring modifier** (see Part 3-2-2, Part 3-2-1-3).
        * If a participant is modified by a **quantifier**, annotate it with the **:quant** relation or otherwise follow the guidelines for quantification (see Part 3-1-5, Part 3-2-2, Part 3-3-4).
        * If a participant is a **named entity**, apply the **:name** and **:wiki** relations to the appropriate named entity category concept node, if you have not done so yet (see Part 3-1-2).
    * Annotate **attributes** of participants and events.
        * Give participants with **overt number marking** (e.g. number-marked NPs, verbal indexes with number information), a **:refer-number** attribute with the relevant value (see Part 3-3-5).
        * Give **_person_ nodes** from pronouns, verbal indexation, or implicit participants - but not those corresponding to named entities - a _:refer-person_ attribute with the relevant value (see Part 3-3-5).
        * Give concepts identified as **events** (see Part 3-1-1 for Event ID guidelines) an **:aspect** attribute with the relevant value (see Part 3-3-1).
        * Give concepts identified as **events** (see Part 3-1-1 for Event ID guidelines) the relevant **modal attributes** (Part 4-3):
            * Give events **under the scope of a modal event** (e.g. a wanting-event) a link to that modal event in the document-level modal dependency (formerly the :modpred relation with the space-building complement-taking predicate as the parent.
            * Give events **under the scope of a reporting event** a **:quote** relation with the reporting verb as the parent, and a **:modal-strength** relation with the relevant strenght.
            * Give **all other events** a **:modal-strength** annotation with the relevant strength.
        * For **interrogative, imperative,** or **expressive** clauses, give the main verb a **:mode** attribute with the relevant value (see Part 3-3-2).
        * Give constituents that are **morphosyntactically negated** or verbs in **polar questions** a **:polarity** attribute with the relevant value (see Part 3-3-3).
        * Give concepts that are modified with a **downtoner** or **intensifier** a **:degree** attribute with the relevant value (Part 3-3-6).

 * Document-level Annotation
    * For any **event concept** or **object concept**:
        * Assess whether it is **coreferential** with a previously mentioned event or object concept. In the case of object concepts, also assess whether it is a **subset** of another concept.
        * If so, choose the relevant **coreference relation**, with the previous mention as the head and the current mention as the child (see Part 4-1).
    * Assess  the **modal dependency structure** generated on the basis of the sentence-level modal annotation.
        * Edit any errors.
        * If possible, substitute the relevant modal strength value for any **:unspecified** links generated between conceivers and events because of **:modpred** relations in the sentence-level annotation.
    * Give every concept **identified as an event** (see Part 3-1-1 for Event ID guidelines) and each **time expression** in the text a temporal annotation (see Part 4-2).

## Part 6. Integrated examples

PRECEDING: A man has been given silver bullets, and told to shoot a Crow Chief. The man rode up behind the Crow Chief. He aimed his gun at him. He fired.

```
\ref    CrowCh(o).096
\tx "wohei,"    hee3oohok
\mb wohei
\ge okay
\ps part
\ft "Wohei, the Crow Chief said to the ones sitting there, "dig for them, dig for them!""
            Hee3- ‘say s.t. to s.o.’ (verb, di-transitive)
            ARG 0 = [Crow Chief] [not overt in sentence]
            ARG 1 = [those sitting there]
            ARG 2 = [wohei/okay] + [dig for them, dig for them]
            Nooxoh- ‘dig for s.t. with a tool’ (verb, transitive)
            ARG 0 = [those sitting there]
            ARG 1 = [bullets] [not overt in sentence]
(s2h / hee3-01
   :ARG0 (s2p / person
       :refer-person 3rd
       :refer-number singular)
   :ARG1 (s2p2 / person
       :ARG0-of (s2x / 3ii'oku 'sit'
           :aspect state
           :modal-strength full-affirmative)
       :mod (s2n / nuhu' 'this')
       :refer-number plural)
   :ARG2 (s2n2 / nooxoh-01
       :ARG0 s2p2
       :ARG1 (s2t / thing)
       :other-role (s2w / wohei)
       :aspect performance
       :modal-strength partial-affirmative
       :mode Imperative)
   :aspect performance
   :modal-strength full-affirmative)
Glosses: hee3-01 = 'say s.t. to s.o.'; nooxoh-01 = 'dig for s.t. with a tool'
(s1s0 / sentence
    :temporal ((past-reference :contained s1h)
            (s1h :overlap s1x)
            (s1h :after s1n2))
    :modal ((author :full-affirmative s1h)
            (author :full-affirmative s1x)
            (author :full-affirmative s1p)
            (s1p :partial-affirmative s1n2)))
\ref    CrowCh(o).097
\tx bii'inowuneehek,
\mb bii'in -owunee  -hek    neihoow- neh' -e'
\ge find.s.t. -2PL  -SUBJ   1.NEG- kill -3/1
\ps vti     -infl   -infl   infl.pref- vta -infl
\ft "If you find [the bullets], he does not kill me."
    Bii’in- ‘find s.t.’ (verb, transitive)
    ARG 0 = [you]
    ARG 1 = [bullets] [not overt in sentence]
    Neh’- ‘kill s.o.’ (verb, transitive)
    ARG 0 = [he]
    ARG 1 = [me]
(e / event
    :actor (p / person
    :theme (n / neh'-01 'kill s.o.'
        :ARG0 (p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (p3 / person
            :refer-person 1st
            :refer-number singular)
        :condition (b / bii'in-01 'find s.t.'
            :ARG0 (p4 / person
            :ARG1 (t / thing)
            :aspect performance
            :modal-strength full-affirmative)
        :aspect performance
        :modal-strength full-negative
        :quote e))
(s2s0 / sentence
    :temporal ((s1h :after s2e)
            (s2e :after s2b)
            (s2b :after s2n))
    :modal ((author :full-affirmative s2e)
            (author :full-affirmative s2p)
            (s2p :neutral-affirmative have-condition)
            (have-condition :full-negative s2n)
            (have-condition :full-affirmative s2b))
    :coref ((s1p :same-entity s2p)
            (s2p :same-entity s2p3)
            (s1p2 :same-entity s2p4)
            (s1t :same-entity s2t)))
\ref    CrowCh(o).098
\tx ciibii'inowuneehek,
\mb cii- bii'in -owunee -hek    noh
\ge NEG- find.s.t. -2PL -SUBJ   and
\ps pref- vti -infl -infl
\ft "If you don't find them, then he kills me."
    SAME ARG STRUCTURE AS PRECEDING
(s2e / event
    :actor (s2p / person
    :theme (s2n / neh'-01 'kill s.o.'
        :ARG0 (s2p2 / person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s2p3 / person
            :refer-person 1st
            :refer-number singular)
        :condition (s2b / bii'in-01 'find s.t.'
            :ARG0 (s2p4 / person
            :ARG1 (s2t / thing)
            :aspect performance
            :modal-strength full-negative)
        :aspect performance
        :modal-strength full-affirmative
        :quote s2e))
(s2s3 / sentence
    :temporal ((s2e :after s3e)
               (s3e :after s3b)
               (s3b :after s3n))
    :modal ((author :full-affirmative s3e)
            (author :full-affirmative s3p)
            (s3p :neutral-affirmative have-condition)
            (have-condition :full-affirmative s3n)
            (have-condition :full-negative s3b))
    :coref ((s2p3 :same-entity s3p)
            (s3p :same-entity s3p3)
            (s2p2 :same-entity s3p2)
            (s2p4 :same-entity s3p4)
            (s2t :same-entity s3t)))
\ref    CrowCh(o).099
\tx wo'oe'onoun he'ih'iinooxoheino'.
\mb wo'oe'onoun he'ih'ii- nooxohei -no'
\ge on.and.on   NARRPAST.IMPERF- dig.holes -pers.PL
\ps part
\ft On and on they were digging (for them).
            Nooxohei- ‘dig, dig for s.t. unspecified’ (verb, intransitive)
            ARG 0 = [the ones sitting there] [not overt in sentence]
            ARG 1 (implied only) = [the bullets] [not overt in sentence, and
(s2n / nooxohei-01
    :ARG0 (s2p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s2t / thing)
    :duration (s2w / wo'oe'onoun 'on and on')
    :aspect activity
    :modal-strength full-affirmative)
(s2s4 / sentence
    :temporal (s3e :after s4n)
    :modal (author :full-affirmative s4n)
    :coref ((s3p4 :same-entity s4p)
            (s3t :same-entity s4t)
            (s1n2 :same-event s4n)))
\ref    CrowCh(o).100
\tx he'ihnooko'wuuteen.
\mb he'ih- nooko'wuutee-  ni
\ge NARRPAST- white.streak.in/on.ground
\ps pref- vii- OS.OBV
\ft The ground had a white mark/streak in it.
    Nooko’wuutee- ‘there is a white mark in the ground’ or ‘the ground is marked white’ (verb, intransitive)
    ARG 0 = [the ground] (incorporated into the verb)
(s2h / have-mod-91
       :ARG1 (s2t /thing)
       :ARG2 (s2n / nooko'wuutee 'have.white.streak')
       :aspect state
       :modal-strength full-affirmative)
(s2s5 / sentence
    :temporal (s4n :overlap s5h)
    :modal (author :full-affirmative s5h))
\ref    CrowCh(o).101
\tx niisootoxuuus   ne'no'uxoo';
\mb niisootox- uuus ne'- no'uxoo -'
\ge seven- days
\ps pref- ni.pl
\ft For seven days they are digging (for them).
            No’uxoo- ‘a certain time arrives, comes’ (verb, intransitive)
            ARG 0 = [(end of) seven days]
            Nooxohei- ‘dig for s.t. unspecified’ (verb, intransitive)
            SEE ARG STRUCTURE ABOVE SENTENCE 4
(s2n / nooxohei-01
    :ARG0 (s2p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s2t / thing)
    :duration (s2t2 / temporal-quantity
        :unit (s2u / uuus)
        :quant 7)
    :aspect activity
    :modal-strength full-affirmative)
(s2s6 / sentence
    :temporal (s5h :overlap s6n)
    :modal (author :full-affirmative s6n)
    :coref ((s4p :same-entity s6p)
            (s4t :same-entity s6t)))
\ref    CrowCh(o).102
\tx hoo3ontii3i';
\mb hoo3ontii -3i'
\ge fail.to.do.s.t. -3PL
\ps vai.t -infl
\ft They failed to find them;
    Hoo3ontii- ‘fail to do s.t.’ (verb, intransitive)
    ARG 0 = [the ones sitting there] [not overt in the sentence]
    ARG 1 (implied only) = [find the bullets by digging] [not overt in the sentence, and the verb is syntactically/grammatically intransitive, though semantically transitive]
   (s2h / hoo3ontii
       :ARG0 (s2p / person
           :refer-person 3rd
           :refer-number plural)
       :ARG1 (s2e / event
           :mod s2h)
       :aspect performance
       :modal-strength full-affirmative)
   (s2s7 / sentence
       :temporal (s6n :after s7h)
       :modal ((author :full-affirmative s7h)
               (author :full-affirmative s7p)
               (s7p :unspecified s7e))
       :coref ((s6p :same-entity s7p)
               (s2b :same-event s7e)))

Or:
nuhu'   3ii'okuni3i,    "nooxohowu',    nooxohowu'!"
hee3oohok       nuhu'   3ii'oku -ni3i   nooxoh -owu'            nooxoh-owu'
said.to.s.o.    this    IC.sit -4PL     dig.hole.with.tool -2PL.IMPER   dig.hole.with.too -2PL.IMPER
vta.3s/4        det     vai -infl       vti -infl   vti -infl
neihoowneh'e'.
:refer-person 2nd
:refer-number plural)
noh     ne'neh'einoo."
ne'- neh' -einoo
then- kill -3S/1S
part    pref- vta -infl
:refer-person 2nd
:refer-number plural)
Glosses: nooxohei-01 = 'dig for s.t. unspecified'; uuus = 'day'; hoo3ontii = 'fail to do s.t.'
pref- vai.o -infl
verb is syntactically/grammatically intransitive, though
semantically transitive]
nooxoheino'.
nooxohei -no'
then- arrive -0S    dig.holes -pers.PL
pref- vai+aff -infl vai.o -infl
```

## Part 7. Alphabetical Index of UMR Annotation Categories

In the following alphabetical index, annotation values are distinguished by their italic typeface in the first column. In the last column, the principal section(s) in which each term is defined or discussed is indicated in boldface.

| Term | Category | Sections |
|---|---|---|
| -00 suffix | UMR annotation convention | 2-2-1, **3-1-4** |
| *1st person* | Person semantic category, person annotation value | 2-1, 3-1-3-1, **3-3-5** |
| *2nd person* | Person semantic category, person annotation value | 2-1, **3-3-5** |
| *3rd person* | Person semantic category, person annotation value | 2-1, 3-1-3-1, **3-3-5** |
| Ability | Modal semantic category | 3-3-1-2, **3-3-1-3** |
| Absolute time expression | Temporal semantic category | **4-2-1-2** |
| Abstract concept | Category of UMR objects | 1, 2-1, **2-2-3**, 2-2-4, 3-1-1-3, 3-1-3-5, 3-1-6 |
| Abstract Meaning Representation (AMR) | Annotation scheme | 1, **2-1**, 2-2, 2-2-1, 2-2-2, 2-2-3, 2-2-4, 2-2-5, 3-1-2, 3-2-1, 3-2-1-3, 3-2-2, 3-3-2, 3-3-3, 3-3-5, 3-3-6 |
| *Activity* | Aspectual semantic category, aspect annotation value | 2-1, 2-2-5, 3-3-1, **3-3-1-4**, 3-3-1-5 |
| *Actor* | Participant role | 2-1, 2-2-1, 3-1-3-1, **3-2-1-1**, 3-2-1-1-2, 3-3-5 |
| *Actor-of* | Participant role | **3-2-1-3** |
| (pure) Addition | Discourse relation | **3-1-6** |
| Additive | Discourse relation | **3-1-6** |
| Adjective | Part of Speech | 2-2-5, **3-3-1**, 3-3-3, 4-3-2 |
| Adverbial subordination | Strategy | **3-1-6** |
| Adversative | Discourse relation | **3-1-6** |
| *Aff* | Modal annotation value | 1, 4-2-2-1, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-3, 4-3-1-6, 4-3-2 |
| *Affectee* | Participant role | **3-2-1-1**, 3-2-1-1-2 |
| *After* | Temporal annotation value | 1, **4-2-2-1**, 4-2-2-3, 4-2-2-4 |
| *Age* | Non-participant role relation | **3-2-2-2** |
| Anaphoric expression | Coreference semantic category | 4-1, **4-1-1** |
| Anchoring modification | Modification semantic category | **3-2-2-2** |
| And + but | Discourse relation | **3-1-6** |
| And + contrast | Discourse relation | **3-1-6** |
| And + unexpected | Discourse relation | **3-1-6** |
| Anterior | Discourse relation | **3-1-6** |
| Anticausative | Valency-changing category | **3-2-1-1-2** |
| Antipassive | Valency-changing category | **3-2-1-1-2** |
| Applicative | Valency-changing category | 3-1-3-2, **3-2-1-1-2** |
| Apprehensional | Discourse relation | **3-1-6** |
| Arabic | Language | 2-2 |
| Arapaho | Language | 3-1-3-1 |
| *ARG0* | Participant role | 2-1, 2-2-1, 3-1-3-5, 3-2-1, 3-2-1-1-1, **3-2-1-2** |
| *ARG0-of* | Participant role | **3-2-1-3** |
| *ARG1* | Participant role | 2-1, 2-2-1, 3-1-3-5, 3-2-1, 3-2-1-1-1, **3-2-1-2**, 3-2-1-2, 4-3-1 |
| *ARG1-of* | Participant role | **3-2-1-3** |
| *ARG2* | Participant role | 2-2-1, 3-2-1, **3-2-1-2**, 4-3-1 |
| Argument | Semantic category | 1, 2-1, 2-2, **2-2-1**, 3-1-3, 3-1-3-1, 3-1-3-4, 3-1-3-5, 3-1-4, 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-1-2, 3-2-1-2-1, 3-2-1-3, 3-3-5 |
| Argument structure | UMR annotation category | 1, 2-1, 2-2, 2-2-1, 2-2-2, 3-1-3-2, 3-1-3-4, 3-1-3-5, **3-2-1**, 3-2-1-3 |
| Aspect | Semantic category, UMR attribute | 1, 2-1, 2-2, 2-2-4, 2-2-5, **3-1-1**, 3-1-3-3, 3-2-1-3, 3-2-2-3, 3-3-1, 3-3-1-1, 3-3-1-2, 3-3-1-3, 3-3-1-4, 3-3-1-5, 4-2-1-2, 4-2-2-1 |
| Assertion | Modal semantic category | **4-3-2** |
| Associated motion | Semantic category | **3-1-3-4** |
| *Atelic Process* | Aspectual semantic category, aspect annotation value | 3-3-1, 3-3-1-3, **3-3-1-4** |
| Attribute | Category of UMR objects | 2-1, 2-2-4, **2-2-5**, 3-1-3-3, 3-1-6, 3-2-1-3, 3-2-2-3, **3-3**, 3-3-1, 3-3-2, 3-3-3, 3-3-4, 3-3-5, 3-3-6 |
| *Author/author* | Modal annotation value | 1, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-3, 4-3-1-6 |
| Auxiliary | Strategy | **3-1-3-3** |
| Balinese | Language | 3-2-1 |
| Before | Temporal annotation value | 1, 4-2, **4-2-2-1** |
| Bezhta | Language | 3-2-1-1-2 |
| Bound morphology | Strategy | 3-1-3, 3-1-3-2, **3-1-3-3**, 3-2-1-2-1, 3-3-6 |
| *Calendar* | Temporal annotation relation | **3-2-2-1** |
| Cardinality | Quantification semantic category | 3-2-2-2, **3-2-2-5** |
| Causal relations | Semantic category | 3-1-1-3, **3-1-6**, 4-2-2-2, 4-2-2-3 |
| Causative | Valency-changing category | 3-1-3-2, **3-2-1-1-2** |
| *Cause* | Participant role | 3-1-3-2, 3-1-6, **3-2-1-1** |
| Caused event | Semantic category | **3-1-3-2**, 3-1-6, **4-2-2-3** |
| *Causer* | Participant role | **3-2-1-1**, 3-2-1-1-2 |
| Caused event | Semantic category | **3-1-3-2**, 3-1-6, **4-2-2-3** |
| *Century* | Temporal annotation relation | **3-2-2-1** |
| Certainty | Modal semantic category | 4-3, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-3, 4-3-1-3, 4-3-1-5, 4-3-2 |
| Change of state | Event type | **3-2-1-1**, 3-2-1-1-2 |
| Chinese | Language | 2-2, 3-1-4 |
| Circumstantial | Participant role category | **3-2-1-1** |
| Circumstantial locative | Participant role category | 3-1-3-4, **3-2-2-3** |
| Circumstantial temporal | Participant role category | **3-2-2-3** |
| Classifier | Strategy | **3-1-3-1** |
| Command | Mode semantic category | 3-2-2-6, **3-3-2**, 4-3-1-1-3 |
| *Companion* | Participant role | **3-2-1-1** |
| Completive | Aspectual semantic category | 3-1-3-3, **3-3-1-5** |
| Complex figure construal | Information packaging | **3-1-6** |
| Complex sentence | Sentence type | **3-1-6**, 4-3-1-4, 4-3-1-5 |
| Compound | Strategy | **3-1-1-2** |
| Conative | Modal semantic category | **3-1-3-3** |
| *Conceiver* | Modal annotation value | 4-2-2-1, 4-3, **4-3-1-1** |
| Concept | Category of UMR objects | 1, **2-1**, 2-2, 2-2-1, 2-2-2, 2-2-3, 2-2-4, 2-2-5, **3-1**, 3-1-1, 3-1-3, 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-5, 3-1-3-6, 3-1-4, 3-1-5, 3-2-1-3, 3-2-2-4, 3-2-2-5, 3-2-2-6, 3-3-5, 3-3-6 |
| Concept-word mismatch | UMR annotation complication | **3-1-3** |
| *Concession* | Participant role | **3-1-6**, 3-2-2-6 |
| Concessive | Discourse relation | **3-1-6** |
| Concessive conditional | Discourse relation | **3-1-6** |
| Concrete time expression | Temporal semantic category | **4-2-1-2** |
| *Condition* | Participant role | 3-1-6, 3-2-2-6, 4-3-1, **4-3-1-5**, 4-3-2 |
| Conditional | Discourse relation | **3-1-6**, 4-3-1, 4-3-1-5 |
| Conjunctive | Discourse relation | **3-1-6** |
| *Consist-of* | Non-participant role relation | 2-2-4, **3-2-2-2** |
| Consecutive | Discourse relation | **3-1-6** |
| Constant | Category of UMR objects | **1** |
| Contact | Event type | **3-2-1-1** |
| *Contained* | Temporal annotation value | 1, **4-2-2-1**, 4-2-2-2 |
| Container adverbial | Aspectual semantic category | **3-3-1-5** |
| Continuative | Aspectual semantic category | 3-1-3-3, **3-3-1-4** |
| (pure) Contrast | Discourse relation | **3-1-6** |
| Coordination | Strategy | **3-1-6**, 3-2-2-4 |
| Coreference | Semantic category | 1, 2-1, 2-2, 3-1-1-4, 3-1-3-1, **4-1**, 4-1-1, 4-1-2 |
| Coreference, entities | Coreference semantic category | 3-1-3-1, **4-1-1** |
| Coreference, events | Coreference semantic category | 3-1-1-4, **4-1-2** |
| Counterfactual | Modal semantic category | **4-3-2** |
| *Country* | Named entity type | **3-1-2** |
| Creation | Event type | **3-2-1-1** |
| Cross-lingual annotation | UMR annotation practice | **1**, 2-2, 2-2-3, 2-2-4, 2-2-5, 3-1-1, 3-1-1-1, 3-1-1-2, 3-1-3, 3-1-3-2, 3-1-3-3, 3-1-3-5, 3-2-1-1, 3-3-5, 4-3-1-1-2 |
| *Day* | Temporal annotation relation | 2-2-4, **3-2-2-1** |
| *Dayperiod* | Temporal annotation relation | **3-2-2-1** |
| *Decade* | Temporal annotation relation | **3-2-2-1** |
| Degree | Semantic category, UMR attribute | 2-1, 2-2-5, **3-3-6** |
| Deontic | Modal semantic category | 4-2-2-4, 4-3, 4-3-1-1, **4-3-1-1-3**, 4-3-1-6, 4-3-2 |
| Desiderative | Modal semantic category | 3-1-3-3, 4-2-2-4, **4-3-1-1-3**, 4-3-1-2, 4-3-1-6, 4-3-2 |
| Direct evidence | Evidential semantic category | 4-3-1-1, **4-3-1-1-2** |
| *Directed achievement* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Directed activity* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-4**, 3-3-1-5 |
| *Directed endeavor* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Direction* | Non-participant role relation | **3-2-2-3** |
| Discourse relations | Semantic category | **3-1-6** |
| Disjunctive | Discourse relation | **3-1-6** |
| Document Creation Time (document-creation-time) | Temporal annotation value | 1, 3-3-1-4, 4-2, **4-2-1-1**, 4-2-1-2 |
| Document-level representation | UMR annotation practice | 1, 2-1, 2-2, 2-2-5, 3-1-6, 3-3-3, **4**, 4-1-1, 4-2, 4-3-1, 4-3-1-4 |
| Doubt | Modal semantic category | **4-3-1-6**, 4-3-2 |
| *Downtoner* | Degree semantic category, degree annotation value | 2-1, **3-3-6** |
| *Dual* | Number semantic category, number annotation value | 2-1, **3-3-5** |
| *Duration* | Non-participant role relation | 2-2-4, **3-2-2-3** |
| Durative adverbial | Aspectual semantic category | **3-3-1-5** |
| Edge | Category of UMR objects | **2-1**, 2-2, 2-2-1, 4-3 |
| Embedded interrogative | Semantic category | **3-2-1-3** |
| *Endeavor* | Aspectual semantic category, aspect annotation value | 2-1, 2-2-5, 3-3-1, **3-3-1-5** |
| English | Language | 1, 2-2, 2-2-1, 2-2-5, 3-1-3, 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-3-5, 3-1-4, 3-1-6, 3-2-1, 3-2-1-1-1, 3-2-1-1-2, 3-3-1, 3-3-1-1, 3-3-1-2, 3-3-1-3, 3-3-1-5, 3-3-3, 3-3-5, 3-3-6, 4-3-1-6, 4-3-2 |
| Epistemic modality | Modal semantic category | 3-1-6, 4-3, 4-3-1, **4-3-1-1**, 4-3-1-1-2, 4-3-1-4, 4-3-1-6, 4-3-2 |
| *Equal* | Degree semantic category, degree annotation value | **3-3-6** |
| Equational | Non-verbal clause category | **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| *Era* | Temporal annotation relation | **3-2-2-1** |
| Event | Semantic category | 1, 2-1, 2-2-1, **3-1-1**, 3-1-1-1, 3-1-1-2, 3-1-1-3, 3-1-1-4, 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-6, 3-2-1, 3-2-1-1, 3-2-1-1-2, 3-2-1-2, 3-2-1-3, 3-2-2-3, 3-3-1, 3-3-1-1, 3-3-1-2, 3-3-1-3, 3-3-1-4, 3-3-1-5, 4-1-2, 4-2, 4-2-1-1, 4-2-1-2, 4-2-1-3, 4-2-2-1, 4-2-2-2, 4-2-2-3, 4-2-2-4, 4-3, 4-3-1, 4-3-1-1, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-2, 4-3-1-3, 4-3-1-4, 4-3-1-5, 4-3-1-6, 4-3-2 |
| Event identification | UMR annotation practice | 2-2-1, **3-1-1**, 3-1-1-1, 3-1-1-2, 3-1-1-3, 3-1-1-4, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-3-5, 3-2-1-2, 3-3-1, 3-3-1-1, 3-3-1-3, 4-2-2-1, 4-2-2-3, 4-3-1, 4-3-1-1-3, 4-3-1-2, 4-3-2 |
| Event nominal | Strategy | **3-1-1**, 3-1-1-2, **3-3-1-1** |
| Eventive modifier | Modification semantic category | 2-2-1, **3-1-1-2**, 3-2-1-3 |
| Evidentiality | Semantic category | 4-3, 4-3-1-1, **4-3-1-1-2** |
| *Example* | Non-participant role relation | **3-2-2-6** |
| *Exclusive* | Person semantic category, person annotation value | **3-3-5** |
| Exclusive disjunctive | Discourse relation | **3-1-6** |
| Exhaustive disjunction | Discourse relation | **3-1-6** |
| *Experiencer* | Participant role | 2-1, **3-2-1-1**, 4-3-1-6 |
| Experiential | Event type | **3-2-1-1** |
| *Expressive* | Mode annotation value | 2-1, **3-3-2** |
| External cause | Participant role category | **3-2-1-1** |
| FactBank | Annotation scheme | **4-3-1-1** |
| Factive predicate | Event type | **4-3-1-6**, 4-3-2 |
| Falam Chin | Language | 3-2-1-1-2 |
| Fear | Modal semantic category | **4-3-2** |
| Figure-ground construal | Information packaging | **3-1-6** |
| *Force* | Participant role | **3-2-1-1** |
| Frame files | Annotation scheme | **3-1-4**, 3-2-1, 3-2-1-1-1, **3-2-1-2**, 3-2-1-2-1, 3-2-1-3, 4-3, 4-3-1-6 |
| *Frequency* | Non-participant role relation | 2-2-4, **3-2-2-3** |
| Frustrative | Modal semantic category | **3-1-3-3** |
| Full support | Modal semantic category | **4-3-1-1***, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-6, 4-3-2 |
| Future-oriented modality | Modal semantic category | 4-3-1-1, **4-3-1-1-3** |
| *Future_ref* | Temporal annotation value | **4-2-1-1**, 4-2-1-2 |
| General participant roles | Participant role category | 2-1, 2-2-1, 3-2-1, **3-2-1-1**, 3-2-1-1-2, 3-2-1-2-1, 3-2-1-3, 3-2-2 |
| Generic events | Event type | **3-1-1-4** |
| Gerund | Strategy | **3-1-1**, 3-3-1-1 |
| *Goal* | Participant role | 3-1-3-4, **3-2-1-1** |
| *Greater plural* | Number semantic category, Number annotation value | **3-3-5** |
| *Habitual* | Aspectual semantic category, aspect annotation value | 2-1, 2-2-5, 3-3-1, **3-3-1-2** |
| Hope | Modal semantic category | **4-3-2** |
| Hua | Language | 3-1-6 |
| Identity | Coreference semantic category | **4-1-1, 4-1-2** |
| *Imperative* | Mode annotation value | 2-1, 3-1-6, 3-2-2-6, **3-3-2**, 4-3-2 |
| *Imperfective* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-3** |
| Implicit event | Event type | **3-1-1-4**, 3-1-3-5 |
| Implicit participant | Participant type | 2-1, 3-2-1-1, 3-2-1-1-2, **3-2-1-2**, 3-3-5 |
| Inactive action | Event type | **3-3-1-3** |
| Inceptive | Aspectual semantic category | **3-3-1-4** |
| Inchoative | Aspectual semantic category | **3-1-3-3** |
| *Inclusive* | Person semantic category, person annotation value | **3-3-5** |
| Inclusive disjunctive | Discourse relation | **3-1-6** |
| *Incremental accomplishment* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| Independent argument structure | UMR annotation diagnostic | **3-1-3-4** |
| Indirect evidence | Evidential semantic category | **4-3-1-1-2** |
| Inferred evidence | Evidential semantic category | **4-3-1-1** |
| *Inherent state* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-3** |
| *Instrument* | Participant role | 3-1-3-1, **3-2-1-1** |
| *Intensifier* | Degree semantic category, degree annotation value | 2-1, **3-3-6** |
| Intention | Modal semantic category | **4-3-1-1-3** |
| *Interrogative* | Mode annotation value | 2-1, **3-3-2** |
| Inverse participant roles | Participant role category | **3-2-1-3** |
| *Irreversible directed achievement* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Irreversible state* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-3** |
| Juxtaposition | Strategy | **3-1-3-5** |
| *Key event* | Temporal annotation value | **4-2-1-3**, 4-2-2-1 |
| Kinship relations | Semantic category | **3-2-1-3**, 3-2-2-2 |
| Kukama | Language | 3-1-3-2, 3-1-3-5, 3-2-1-1-1, 3-2-1-1-2 |
| Lattice | Category of UMR objects | 2-2-4, 3-1-6, 3-3-1, 3-3-1-1, 3-3-5, 4-3, 4-3-1-1 |
| Lemma | Category of UMR objects | 2-1, 3-1-3-6, **3-1-4** |
| Lexicon | Category of UMR objects | 2-1, 2-2-1, **3-1-4**, 3-2-1, 3-2-1-1-1, 3-2-1-2, 3-2-1-2-1, 3-2-1-3, 3-3-6 |
| Locatable time expression | Temporal semantic category | **4-2-1-2** |
| Manipuri | Language | 3-1-3-3 |
| *Manner* | Participant role | 3-1-6, **3-2-1-1** |
| *Material* | Participant role | **3-2-1-1** |
| Means | Discourse relation | **3-1-6** |
| *Medium* | Non-participant role relation | 2-2-4, **3-2-2-2** |
| Mensural constructions | Quantification semantic category | 2-2, **3-2-2-5** |
| Metanodes | Temporal annotation category | 4-2, 4-2-1, **4-2-1-1**, 4-2-2-1 |
| *Mod* | Non-participant role relation | 2-2-4, **3-2-2-2** |
| *Mod* | Modal annotation value | 4-3-1, **4-3-1-2** |
| Modal dependencies | Category of UMR objects | 1, 2-1, 3-1-3-3, 3-3-3, 4-2-2-1, **4-3**, 4-3-1, 4-3-1-6, 4-3-2 |
| Modal strength | Modal semantic category | 4-3, 4-3-1, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-3, 4-3-1-6, 4-3-2 |
| Modal verbs/auxiliaries | Strategy | **3-1-3-3**, 3-3-1-3, 4-3-1, 4-3-1-1-3, 4-3-1-2, 4-3-1-3, 4-3-1-4, 4-3-1-5, **4-3-1-6**, 4-3-2 |
| Modality | Semantic category | 1, 2-1, 2-2, 2-2-5, 3-1-1, 3-1-3-3, 3-3-1, 3-3-1-2, 3-3-1-3, 3-3-3, 4-2-2-1, 4-2-2-4, **4-3**, 4-3-1, 4-3-1-1, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-2, 4-3-1-3, 4-3-1-4, 4-3-1-5, 4-3-1-6, 4-3-2 |
| Mode | UMR attribute | 2-1, 2-2-5, **3-3-2** |
| Modification | Information packaging | 2-2, 2-2-1, 2-2-4, 2-2-5, **3-1-1**, 3-1-1-2, 3-1-1-3, 3-2-1-3, 3-2-2, 3-2-2-2, 3-2-2-3, 4-2 |
| *Modstr* | Modal annotation value | 4-2-2-1, 4-3, 4-3-1, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-2, 4-3-1-3, 4-3-1-4, 4-3-1-5, 4-3-1-6 |
| *Month* | Temporal annotation relation | 2-2-4, **3-2-2-1** |
| Motion | Event type | 3-1-1-4, **3-1-3-4, 3-2-1-1** |
| Multi-word expression | UMR annotation complication | 1, 2-1, 2-2-2, 3-1-3, **3-1-3-6** |
| *Name* | Non-participant role relation | 2-1, **3-2-2-4** |
| Named entity | Category of UMR objects | 1, 2-1, **3-1-2**, 3-1-3-1, 3-2-2-4, 3-3-5, 4-1 |
| *Neg* | Modal annotation value | **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-3, 4-3-1-6, 4-3-2 |
| Negation | Modal semantic category | 2-1, 2-2, 3-1-3-2, 3-1-5, 3-1-6, **3-3-3, 4-3-1-1**, 4-3-1-1-1, 4-3-1-4, 4-3-1-5, 4-3-1-6, 4-3-2 |
| Negative circumstantial | Discourse relation | **3-1-6** |
| *Neut* | Modal annotation value | 1, **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-3, 4-3-1-3, 4-3-1-6, 4-3-2 |
| *neutral-negative* | Modal annotation value | **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-3, 4-3-1-6, 4-3-2 |
| Neutral support | Modal semantic category | 1, **4-3-1-1**, 4-3-1-1-3, 4-3-2 |
| Node | Category of UMR objects | 2-1, **2-2**, 2-2-1, 2-2-3, 2-2-5, 3-2-1-3, 3-2-2-4, 3-2-2-6, 3-3-5, 4-1-1, 4-1-2, 4-2, 4-2-1, 4-2-1-1, 4-2-1-2, 4-2-2-1, 4-3, 4-3-1, 4-3-2 |
| Nominal modification | Modification semantic category | 3-1-1, **3-2-1-3**, **3-2-2-2** |
| *Non-1st person* | Person semantic category, person annotation value | **3-3-5** |
| *Non-3rd person* | Person semantic category, person annotation value | **3-3-5** |
| Non-exhaustive disjunction | Discourse relation | **3-1-6** |
| Non-finite complement | Strategy | **3-1-1-2** |
| *Non-full* | Modal semantic category, modal annotation value | **4-3-1-1**, 4-3-1-4 |
| *Non-incremental accomplishment* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Non-neutral* | Modal semantic category, modal annotation value | **4-3-1-1** |
| Non-participant role relation | Category of UMR relations | 2-2-4, **3-2-2** |
| Non-result path expression | UMR annotation diagnostic | **3-3-1-5** |
| *Non-singular* | Number semantic category, Number annotation value | **3-3-5** |
| Non-verbal clauses | Semantic category | 2-2-1, 2-2-3, 3-1-1-3, **3-1-3-5**, 3-2-1-1-1, 3-2-1-2, 3-2-1-3, 3-3-1-3 |
| Noun | Part of Speech | 2-2, 2-2-1, **3-3-1**, 3-1-3-1, 3-2-1-3, 3-2-2-2 |
| Noun incorporation | Strategy | **3-1-3-1** |
| NP | Strategy | 3-1-3-1, 3-1-3-4, 3-1-3-5, 3-2-1-3, 3-2-2, **3-2-2-2** |
| Number | Semantic category | 2-1, 2-2-5, 3-1-3-1, **3-3-5** |
| Numbered/lexicalized participant roles | Participant role category | 2-1, 2-2-1, 3-1-3-5, 3-2-1, 3-2-1-1-1, **3-2-1-2**, 3-2-1-2-1, 3-2-1-3, 3-2-2 |
| Object concept | Semantic category | **3-1-1**, 3-1-1-2, 3-1-1-3, 3-1-3-5, 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-3, 3-2-2-2, 3-2-2-3, 3-2-2-5, 3-2-2-6, 3-3-2, 3-3-5, 4-1-1 |
| Obligation | Modal semantic category | 2-1, **4-3-1-6**, 4-3-2 |
| Optative | Modal semantic category | **3-1-3-3** |
| *OpX* | Non-participant role relation | **3-2-2-4**, 4-2 |
| *Ord* | Non-participant role relation | **3-2-2-5** |
| Ordinal | Quantification semantic category | **3-2-2-5** |
| *Other* | Non-participant role relation | 2-2-4, 3-2-1-1, **3-2-2-6** |
| *Overlap* | Temporal annotation value | 1, **4-2-2-1**, 4-2-2-2 |
| Partial support | Modal semantic category | **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-2 |
| Participant identification | UMR annotation practice | 2-2-1, **3-1-3-1**, 3-1-3-5, 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-1-2, 3-2-1-2 |
| Participant nominalization | Strategy | **3-2-1-3** |
| Participant roles | Semantic category | 2-1, 2-2-1, 3-1-1, 3-1-3-1, 3-1-3-2, 3-1-6, **3-2-1**, 3-2-1-1, 3-2-1-1-1, 3-2-1-1-2, 3-2-1-2, 3-2-1-2-1, 3-2-1-3, 4-3, 4-3-1, 4-3-1-4 |
| Participle | Strategy | **3-1-1**, 3-1-1-2, 3-2-1-3 |
| *Part-of* | Non-participant role relation | **3-2-2-2** |
| Part-whole relations | Semantic category | **3-2-2-2** |
| Passive | Valency-changing category | 3-2-1, **3-2-1-1-2** |
| *past-reference* | Temporal annotation value | **4-2-1-1**, 4-2-1-2 |
| *Path* | Non-participant role relation | **3-2-2-3** |
| *Paucal* | Number semantic category, Number annotation value | 2-1, **3-3-5** |
| *Perfective* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Performance* | Aspectual semantic category, aspect annotation value | 2-1, 2-2-5, 3-3-1, **3-3-1-5** |
| Permissive | Modal semantic category | 4-3, **4-3-1-1-3**, 4-3-1-6, 4-3-2 |
| *Person* | Named entity type | 1, 2-1, **3-1-2**, 3-1-3-1, 3-2-1-3, 3-3-5, 4-1-1 |
| Person | Semantic category | 2-1, 2-2-5, 3-1-3-1, **3-3-5** |
| Phasal aspect | Aspectual semantic category | **3-1-3-3** |
| *Place* | Participant role | **3-2-1-1** |
| *Plural* | Number semantic category, Number annotation value | 2-1, 3-2-1-1, **3-3-5** |
| *Point state* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-3**, 3-3-1-5 |
| Polarity | Modal semantic category | 2-1, 2-2-5, 3-1-6, **3-3-3**, 4-3, 4-3-1, **4-3-1-1**, 4-3-1-1-1 |
| *Polite* | Non-participant role relation | **3-2-2-6** |
| Positive circumstantial | Discourse relation | **3-1-6** |
| *Poss* | Non-participant role relation | **3-2-2-2** |
| Possession | Semantic category | 2-2-3, **3-1-1-3**, 3-1-3-5, 3-2-1-1, 3-2-1-1-1, 3-2-1-1-2, **3-2-2-2** |
| Possibility | Modal semantic category | 2-1, **4-3-1-1** |
| Posterior | Discourse relation | **3-1-6** |
| Pragmatic valency alternation | Valency-changing category | 3-2-1, **3-2-1-1-2** |
| Predicate | Category of UMR objects | 1, 2-1, 2-2, **2-2-1**, 2-2-3, 2-2-5, 3-3-1, 3-1-1-1, 3-1-1-3, 3-1-3, 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-3-5, 3-1-4, 3-1-5, 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-2, 3-2-1-2-1, 3-2-1-3, 3-2-2, 3-3-1-3, 4-2, 4-2-2-3, 4-3-1-3, 4-3-1-6, 4-3-2 |
| Predicate-argument structure | Semantic category | 1, 2-1, 2-2, **2-2-1**, 3-1-3, 3-1-3-1, 3-1-3-5, **3-2-1**, 3-2-1-1, 3-2-1-1-1, 3-2-1-2, 3-2-1-2-1, 3-2-1-3 |
| Predication | Information packaging | 2-2, **3-1-1**, 3-1-1-1, 3-1-1-3, 3-1-3-5, 3-2-1-1-1, 3-1-3-3, 4-2-2-3 |
| Predicative location | Non-verbal clause category | **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| Predicative possession | Non-verbal clause category | **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| Predicativization/predicativized argument | Strategy | **3-1-3-5**, 3-2-1-1-1 |
| *Present_ref* | Temporal annotation value | **4-2-1-1**, 4-2-1-2 |
| *Process* | Aspectual semantic category, aspect annotation value | 2-1, 3-3-1, 3-3-1-1 |
| Pronominal affixes | Strategy | **3-1-3-1**, 3-1-3-5, **3-3-5** |
| Pronoun | Part of Speech | 2-1, **3-1-3-1, 4-1**, 4-1-1 |
| PropBank | Annotation scheme | **2-2-1**, 3-2-1, 3-2-1-2, 3-2-1-3 |
| Property concept | Semantic category | **3-1-1**, 3-1-1-3, 3-1-3-5, 3-1-6, 3-2-1-1-1, 3-3-1-3, 3-3-2, 3-3-6 |
| Property predication | Non-verbal clause category | **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| *Prt* | Modal annotation value | **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-2, 4-3-1-1-3, 4-3-1-6, 4-3-2 |
| *partial-negative* | Modal annotation value | **4-3-1-1**, 4-3-1-1-1, 4-3-1-1-3, 4-3-1-6, 4-3-2 |
| Purpose | Discourse relation | **3-1-6**, 4-2-2-4, 4-3-1, 4-3-1-4, 4-3-2 |
| *Purpose* | Participant role | 3-1-6, **3-2-1-1**, 4-3-1, **4-3-1-4** |
| *Quant* | Quantification annotation value | 2-1, 2-2-5, **3-2-2-5, 3-3-4** |
| Quantification | Semantic category | 1, 2-1, 2-2, 2-2-5, **3-1-5**, 3-2-2-2, **3-2-2-5**, 3-3-1-3, **3-3-4**, 4-2-1-2 |
| *Quarter* | Temporal annotation relation | **3-2-2-1** |
| *Quot* | Modal annotation value | 4-3, 4-3-1, **4-3-1-3** |
| *Range* | Non-participant role relation | 2-1, **3-2-2-5** |
| *Recipient* | Participant role | **3-2-1-1**, 3-2-1-1-2 |
| Reciprocal | Valency-changing category | 3-2-1, **3-2-1-1-2** |
| Ref-number | UMR attribute | 2-1, 2-2-5, **3-3-5** |
| Ref-person | UMR attribute | 2-1, 2-2-5, **3-3-5** |
| Reference | Information packaging | 2-2, 2-2-1, 2-2-4, 2-2-5, **3-1-1**, 3-1-1-2, 3-1-1-3, 3-2-1-3, 3-2-2, 3-2-2-2, 3-2-2-3, 4-2 |
| Reference time | Temporal annotation value | 1, 3-1-1-2, **4-2-1-2** |
| Referring expression | Information packaging | 2-2, 2-2-4, 3-2-1-3, 3-2-2-2, 3-3-1-1 |
| Reflexive | Valency-changing category | 3-1-3-2, **3-2-1-1-2** |
| Relation | Category of UMR objects | 1, 2-1, **2-2**, 2-2-1, 2-2-4, 2-2-5, 3-1-3-3, 3-1-6, **3-2**, 3-2-1-1, 3-2-1-3, 3-2-2, 3-2-2-1, 3-2-2-2, 3-2-2-3, 3-2-2-4, 3-2-2-5, 3-2-2-6, 4-1-1, 4-1-2, 4-2, 4-2-1, 4-2-1-1, 4-2-2-1, 4-2-2-2, 4-2-2-3, 4-2-2-4, 4-3-1, 4-3-1-1-2, 4-3-1-2, 4-3-1-3, 4-3-1-4, 4-3-1-5 |
| Relative clause | Strategy | 3-1-1, 3-1-1-2, **3-2-1-3** |
| Relative time expression | Temporal semantic category | 4-2, **4-2-1-2** |
| Reported event | Event type | 4-2-2-1, 4-3, 4-3-1, 4-3-1-1, **4-3-1-3** |
| Reported evidence | Evidential semantic category | **4-3-1-1** |
| Reported event | Event type | 4-2-2-1, 4-3-1, **4-3-1-3** |
| *Reversible directed achievement* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| *Reversible state* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-3** |
| Road map | UMR annotation practice | 3-2-1, 3-2-1-1-1, 3-2-1-1-2, 3-2-1-3, 4-3 |
| *root* | Temporal, modal annotation value | **4-2-1**, 4-2-1-2 |
| *Same-entity* | Coreference annotation value | **4-1-1** |
| *Same-event* | Coreference annotation value | **4-1-2** |
| Sanapaná | Language | 2-2-1, 2-2-2, 2-2-3, 3-1-3-2, 3-1-3-4, 3-3-5, 3-3-6 |
| *Scale* | Non-participant role relation | **3-2-2-5** |
| Scope | Semantic category | 2-1, 2-2-5, 3-1-3-2, **3-1-5**, 3-3-1-3, 4-3-1, 4-3-1-1-3, 4-3-1-2, 4-3-1-3 |
| *Season* | Temporal annotation relation | **3-2-2-1** |
| Second-hand evidence | Evidential semantic category | **4-3-1-1** |
| Semantic type | Semantic category | **3-1-1**, 3-1-1-2, 3-1-1-3 |
| Semantic valency alternation | Valency-changing category | 3-2-1, **3-2-1-1-2** |
| *Semelfactive* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| Semi-modals | Modal semantic category | **3-1-3-3** |
| Sense disambiguation | UMR annotation practice | 2-1, 2-2-1, **3-1-4** |
| Sentence-level representation | UMR annotation practice | 1, 2-1, 2-2, 2-2-5, **3**, 3-1-6, 3-3-3, 4-2, 4-3-1, 4-3-1-4, 4-3-1-5 |
| Serial verb construction | Strategy | **2-2** |
| Shipibo-konibo | Language | **3-2-1-1-2** |
| Simultaneous | Discourse relation | **3-1-6** |
| *Singular* | Number semantic category, Number annotation value | 2-1, **3-3-5** |
| *Source* | Participant role | **3-2-1-1** |
| Stage 0 annotation | UMR annotation practice | 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-1-2, 3-2-1-2, 3-2-1-3, 4-3, 4-3-1, 4-3-1-2, 4-3-1-6 |
| Stage 1 annotation | UMR annotation practice | 3-2-1, 3-2-1-1-1, 3-2-1-2, 3-2-1-2-1, 4-3 |
| *Start* | Participant role | **3-2-1-1** |
| *State* | Aspectual semantic category, aspect annotation value | 2-1, 2-2-1, 2-2-5, 3-1-1, 3-1-1-3, 3-3-1, 3-3-1-1, **3-3-1-3**, 3-3-1-5, 4-2-2-1 |
| *Stimulus* | Participant role | **3-2-1-1** |
| *Stimulus-of* | Participant role | **3-2-1-3** |
| Subevent | Coreference, temporal semantic category | 4-1-2, 4-2-2-1, **4-2-2-2** |
| *Subset-of* | Coreference annotation value | **4-1-1, 4-1-2** |
| Substitution | Discourse relation | **3-1-6** |
| *Temp* | Temporal annotation value | 4-2-1, **4-2-1-1** |
| *Temporal* | Participant role | 2-1, **3-1-6, 3-2-1-1**, 4-2 |
| Temporal dependencies | Category of UMR objects | 1, 2-1, 3-1-3-3, **4-2**, 4-2-1, 4-2-1-1, 4-2-1-2, 4-2-2-1 |
| Temporal superstructure | UMR annotation procedure | 4-2, **4-2-1**, 4-2-1-1, 4-2-1-2, 4-2-1-3, 4-2-2-1 |
| Terminative | Aspectual semantic category | **3-3-1-5** |
| *Theme* | Participant role | 2-2-1, 3-1-3-1, **3-2-1-1**, 3-2-1-1-2 |
| Thetic location | Non-verbal clause category | **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| Thetic possession | Non-verbal clause category | 2-2-3, **3-1-1-3**, 3-1-3-5, 3-2-1-1-1 |
| *Thing* | Named entity type | **3-1-3-1, 3-3-5** |
| Time expression | Temporal semantic category | 4-2, 4-2-1, 4-2-1-1, **4-2-1-2**, 4-2-1-3, 4-2-2-1 |
| TimeML | Annotation scheme | **3-1-1** |
| *Timezone* | Temporal annotation relation | **3-2-2-1** |
| *Topic* | Non-participant role relation | 2-2-4, **3-2-2-2** |
| Torau | Language | 3-2-1 |
| Transfer | Event type | **3-2-1-1, 3-2-1-1-2** |
| *Trial* | Number semantic category, Number annotation value | **3-3-5** |
| Typifying modifier | Modification semantic category, Number annotation value | 2-2-4, **3-2-2-2** |
| *Undergoer* | Participant role | 2-2-1, 3-1-3-1, **3-2-1-1**, 3-2-1-1-2, 3-3-5 |
| *Undergoer-of* | Participant role | **3-2-1-3** |
| *Undirected activity* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-4**, 3-3-1-5 |
| *Undirected endeavor* | Aspectual semantic category, aspect annotation value | 3-3-1, **3-3-1-5** |
| Unexpected co-occurrence | Discourse relation | **3-1-6** |
| Uniform Meaning Representation (UMR) | Annotation scheme | **1**, 2-1, 2-2, 2-2-1, 2-2-2, 2-2-3, 2-2-4, 2-2-5, 3-1-1, 3-1-1-1, 3-1-1-3, 3-1-1-4, 3-1-3, 3-1-3-1, 3-1-3-2, 3-1-3-3, 3-1-3-4, 3-1-3-5, 3-1-4, 3-1-5, 3-1-6, 3-2-1, 3-2-1-1, 3-2-1-1-1, 3-2-1-3, 3-2-2, 3-2-2-2, 3-2-2-6, 3-3, 3-3-1-3, 3-3-2, 3-3-3, 3-3-5, 3-3-6, 4-1, 4-1-1, 4-1-2, 4-2, 4-3, 4-3-1-1 |
| *Unit* | Non-participant role relation | **3-2-2-5** |
| Unity under modalization | UMR annotation diagnostic | **3-1-3-3** |
| Unity under negation | UMR annotation diagnostic | **3-1-3-2** |
| Unlocatable time expression | Temporal semantic category | **4-2-1-2** |
| Vague time expression | Temporal semantic category | **4-2-1-2** |
| Valency-changing operation | Semantic category | **3-1-3-2**, 3-2-1, **3-2-1-1-2**, 3-2-1-2-1 |
| Valency-increasing applicative | Valency-changing category | **3-2-1-1-2** |
| Valency-rearranging applicative | Valency-changing category | **3-2-1-1-2** |
| *Value* | Non-participant role relation | 2-1, 2-2-5, **3-2-2-5** |
| Venitive | Associated motion semantic category | **3-1-3-4** |
| Verb | Part of Speech | 2-2-1, 2-2-2, 2-2-3, **3-1-1**, 3-1-1-1, 3-1-1-2, 3-1-3-1, 3-1-3-2, 3-1-3-4, 3-1-3-5, 3-1-6, 3-2-1-1, 3-2-1-1-2, 3-1-3-3, 3-3-5, 4-3-1-6 |
| Verbal argument indexation | Strategy | **3-1-3-1, 3-3-5** |
| Verbal predicate | Strategy | **3-1-3-5** |
| *Weekday* | Temporal annotation relation | **3-2-2-1** |
| *Wiki* | Non-participant role relation | **3-2-2-4** |
| Wish | Modal semantic category | **3-1-3-3, 4-3-1-6**, 4-3-2 |
| Word senses | Category of UMR objects | 1, 2-1, 2-2-1, **3-1-4** |
| Yabem | Language | 3-2-1-1-1 |
| *Year* | Temporal annotation relation | 2-2-4, **3-2-2-1** |
| *Year2* | Temporal annotation relation | **3-2-2-1** |

