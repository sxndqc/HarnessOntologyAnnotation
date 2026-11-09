# Gold UMR annotations of sentences like those of english_umr-0008

From ai-native-annotator.github.io data/skillparse/resources/gold/en/gold.json (no test document).

## english_umr-0578, sentence 4

# :: snt4
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          
Words: Although    preliminary findings    were        reported    more        than        a           year        ago         ,           the         latest      results     appear      in          today       's          New         England     Journal     of          Medicine    ,           a           forum       likely      to          bring       new         attention   to          the         problem     .           

# sentence level graph:
(s4a / appear-01
    :ARG1 (s4t4 / thing
        :ARG2-of (s4r3 / result-01
            :mod (s4l / last)))
    :place (s4p3 / publication-91
        :ARG4 (s4j / journal :wiki "The_New_England_Journal_of_Medicine" 
            :name (s4n / name :op1 "New" :op2 "England" :op3 "Journal" :op4 "of" :op5 "Medicine")
            :ARG1-of (s4h / have-role-91 
                :ARG3 (s4f / forum
                    :ARG0-of (s4b / bring-01
                        :ARG1 (s4a2 / attend-02
                        :ARG1 (s4p / problem)
                        :ARG1-of (s4n2 / new-02
                            :ARG2 s4p))
                        :ARG2 s4p
                        :aspect activity)))
        :ARG6 (s4t / today)))
    :concession (s4r2 / report-01
        :ARG1 (s4t2 / thing
            :refer-number plural
            :ARG1-of (s4f2 / find-01)
            :mod (s4p2 / preliminary))
        :temporal (s4b2 / before
            :op1 (s4n3 / now)
            :quant (s4m3 / more-than
                :op1 (s4t3 / temporal-quantity :quant 1
                :unit (s4y / year))))
        :aspect performance)
    :aspect state)

# alignment:
s4a: 14-14
s4t4: 13-13
s4r3: 13-13
s4l: 12-12
s4p3: 0-0
s4j: 18-22
s4n: 18-22
s4h: 0-0
s4f: 25-25
s4b: 28-28
s4a2: 30-30
s4n2: 29-29
s4p: 33-33
s4t: 16-16
s4r2: 5-5
s4t2: 3-3
s4f2: 3-3
s4p2: 2-2
s4b2: 10-10
s4n3: 10-10
s4m3: 6-7
s4t3: 8-9
s4y: 9-9

# document level annotation:
(s4s0 / sentence
    :coref ((s4t4 :subset-of s4a2)
            (s4p :same-entity s3c5))
    :temporal ((document-creation-time :before s4r2)
            (document-creation-time :contains s4a)
            (document-creation-time :depends-on s4b2)
            (document-creation-time :after s4b)
            (document-creation-time :depends-on s4t))
    :modal ((root :modal author)
            (author :full-affirmative s4a)
            (author :full-affirmative s4r2)
            (author :partial-affirmative s4b)))

## english_umr-0578, sentence 13

# :: snt13
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        
Words: Among     33        men       who       worked    closely   with      the       substance ,         28        have      died      --        more      than      three     times     the       expected  number    .         

# sentence level graph:
(s13d / die-01
    :ARG1 (s13m / man 
        :quant 28
        :quant (s13m4 / more-than
            :op1 (s13p / product-of 
                :op1 3
                :op2 (s13n2 / number
                    :ARG1-of (s13e2 / expect-01
                        :aspect state))))
        :ARG1-of (s13i / include-91
            :ARG2 (s13m2 / man 
                :quant 33
                :ARG0-of (s13w / work-01
                    :ARG1 (s13s / substance)
                    :manner (s13c / close-10)
                    :aspect activity))))
    :aspect performance)

# alignment:
s13d: 13-13
s13m: 3-3
s13m4: 15-16
s13p: 18-18
s13n2: 21-21
s13e2: 20-20
s13i: 1-1
s13m2: 3-3
s13w: 5-5
s13s: 9-9
s13c: 6-6

# document level annotation:
(s13s0 / sentence
    :coref ((s13m2 :same-entity s1p6)
            (s13m :same-entity s1p7)
            (s13s :same-entity s11a))
    :temporal ((document-creation-time :before s13d)
            (document-creation-time :before s13e2)
            (s13w :after s13d)
            (s1e :overlap s13w))
    :modal ((root :modal author)
            (author :full-affirmative s13d)
            (author :full-affirmative s13w)
            (author :full-affirmative s13e2)))

## english_umr-0461, sentence 59

# :: snt59
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          
Words: <Builder>   feel        free        to          give        more        than        one         direction   at          a           time        if          you're      comfortable 

# sentence level graph:
(s59f / feel-01
      :ARG0 (s59y / you)
      :ARG1 (s59f2 / free-04
                   :ARG1 s59y
                   :ARG2 (s59d / direct-01
                               :ARG0 s59y
                               :condition (s59c / comfortable-02
                                                :ARG1 s59y)
                               :frequency (s59r / rate-entity-91
                                                :ARG1 (s59m / more-than
                                                            :op1 1)
                                                :ARG2 (s59a / at-a-time))))
      :mode imperative)

# alignment:

# document level annotation:

## english_umr-0019, sentence 3

# :: snt3
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        
Words: I         heard     it        costs     upwards   of        one       million   dollars   to        execute   one       prisoner; that      sure      buys      a         whole     lot       of        years     in        prison.   

# sentence level graph:
(s3c / cost-01
     :ARG1 (s3e / execute-01
                :ARG1 (s3p / person
                           :ARG1-of (s3i2 / imprison-01)
                           :quant 1))
     :ARG2 (s3u / upwards
                :op1 (s3m / monetary-quantity
                          :unit (s3d / dollar)
                          :ARG3-of (s3b / buy-01
                                        :ARG1 (s3i3 / imprison-01
                                                    :duration (s3l / lot
                                                                   :op1 (s3t2 / temporal-quantity
                                                                              :unit (s3y2 / year)
                                                                              :quant 1)
                                                                   :degree (s3w / whole)))
                                        :ARG1-of (s3s / sure-02))
                          :quant 1000000))
     :ARG1-of (s3h / hear-01
                   :ARG0 (s3i / i)))

# alignment:

# document level annotation:

## english_umr-0215, sentence 40

# :: snt40
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       
Words: It       was      a        question of       life     or       death    for      me       :        I        had      scarcely enough   drinking water    to       last     a        week     .        

# sentence level graph:
(s40q / question-01
      :ARG0 (s40i / i)
      :ARG1 (s40u / umr-choice
                  :op1 (s40l / live-01)
                  :op2 (s40d / die-01))
      :ARG1-of (s40h3 / have-reason-91
                      :ARG2 (s40h / have-03
                                  :ARG0 s40i
                                  :ARG1 (s40w / water
                                              :purpose (s40d2 / drink-01)
                                              :ARG1-of (s40h2 / have-quant-91
                                                              :ARG3 (s40e / enough
                                                                          :mod (s40s / scarce))
                                                              :ARG6 (s40l2 / last-03
                                                                           :ARG2 (s40t / temporal-quantity
                                                                                       :unit (s40w2 / week)
                                                                                       :quant 1)
                                                                           :ARG3 s40i))))))

# alignment:

# document level annotation:

## english_umr-0192, sentence 2

# :: snt2
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          
Words: The         new         ad          plan        from        Newsweek    ,           a           unit        of          the         Washington  Post        Co.         ,           is          the         second      incentive   plan        the         magazine    has         offered     advertisers in          three       years       .           

# sentence level graph:
(s2p3 / plan
      :domain (s2p4 / plan
                    :ARG1-of (s2n2 / new-01)
                    :mod (s2a / advertise-01)
                    :source (s2m / magazine
                                 :name (s2n / name
                                            :op1 "Newsweek")
                                 :part-of (s2n3 / newspaper
                                                :name (s2w / name
                                                           :op1 "Washington"
                                                           :op2 "Post"
                                                           :op3 "Co.")
                                                :wiki "The_Washington_Post")
                                 :wiki "Newsweek"))
      :ARG1-of (s2o / offer-01
                    :ARG0 s2m
                    :ARG3 (s2c3 / company
                                :ARG0-of (s2a2 / advertise-01)))
      :ARG0-of (s2i2 / incentivize-01)
      :ord (s2o2 / ordinal-entity
                 :range (s2t / temporal-quantity
                             :unit (s2y / year)
                             :quant 3)
                 :value 2))

# alignment:

# document level annotation:

## english_umr-0050, sentence 2

# :: snt2
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          
Words: The         women       who         need        the         pill        for         legitimate  medical     reasons     are         a           tiny        minority    who         would       incur       a           very        small       cost        to          the         healthcare  system      for         their       medication. 

# sentence level graph:
(s2h2 / have-role-91
      :ARG1 (s2w / woman
                 :ARG0-of (s2n / need-01
                               :ARG1 (s2p / pill)
                               :purpose (s2r / reason
                                             :mod (s2m / medicine)
                                             :ARG1-of (s2l / legitimate-02))))
      :ARG2 (s2m2 / minority
                  :mod (s2t / tiny)
                  :ARG0-of (s2i / incur-01
                                :ARG1 (s2c / cost-01
                                           :ARG1 (s2m3 / medicate-01
                                                       :ARG1 s2w)
                                           :ARG2 (s2s / small
                                                      :degree (s2v / very))
                                           :ARG3 (s2s2 / system
                                                       :mod (s2h / healthcare))))))

# alignment:

# document level annotation:

## english_umr-0141, sentence 28

# :: snt28
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        
Words: A         health   plan     is        not       a         commodity like      a        gallon    of        milk.    A         health    plan      in        Las       Vegas     is        quite     different from      one       in        Portland. 

# sentence level graph:
(s28a / and
      :op1 (s28c / commodity
                  :domain (s28p / plan
                                :mod (s28h / health))
                  :ARG1-of (s28r / resemble-91
                                 :ARG2 (s28m2 / milk
                                              :quant (s28v / volume-quantity
                                                           :unit (s28g / gallon)
                                                           :quant 1)))
                  :polarity -)
      :op2 (s28d / differ-02
                  :ARG1 (s28p2 / plan
                               :mod (s28h2 / health)
                               :place (s28c2 / city
                                             :name (s28n / name
                                                         :op1 "Las"
                                                         :op2 "Vegas")
                                             :wiki "Las_Vegas"))
                  :ARG2 (s28p3 / plan
                               :mod (s28h3 / health)
                               :place (s28c3 / city
                                             :name (s28n2 / name
                                                          :op1 "Portland")
                                             :wiki "Portland,_Oregon"))
                  :degree (s28q / quite)))

# alignment:

# document level annotation:

## english_umr-0111, sentence 11

# :: snt11
Index: 1                2                3                4                5                6                7                8                9                10               11               12               13               14               15               16               17               18               19               20               21               
Words: He               got              a                health-care      reform           bill             that             his              campaign         contributors,    who              included         health-insurance companies        in               large            amounts,         could            be               happy            with.            

# sentence level graph:
(s11g / get-01
      :ARG0 (s11h / he)
      :ARG1 (s11b / bill
                  :topic (s11r / reform-01
                               :ARG1 (s11h3 / healthcare))
                  :ARG0-of (s11h4 / happy-01
                                  :ARG1 (s11p / person
                                              :ARG0-of (s11c / contribute-01
                                                             :ARG2 (s11c2 / campaign-01
                                                                          :ARG0 s11h))
                                              :ARG2-of (s11i / include-91
                                                             :ARG1 (s11c3 / company
                                                                          :ARG0-of (s11i2 / insure-02
                                                                                          :ARG1 (s11h2 / healthy)))
                                                             :ARG3 (s11a / amount
                                                                         :mod (s11l / large))))
                                  :ARG1-of (s11p2 / possible-01))))

# alignment:

# document level annotation:

## english_umr-0065, sentence 14

# :: snt14
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       
Words: They     say      the      hardest  job      in       the      military is       being    a        military spouse   and      my       wife     was      one      for      most     of       my       military career   .        

# sentence level graph:
(s14a / and
      :op1 (s14s / say-01
                 :ARG0 (s14p3 / person
                              :refer-person 3rd
                              :refer-number plural)
                 :ARG1 (s14i / identity-91
                             :ARG1 (s14j / job
                                         :ARG1-of (s14h6 / have-degree-91
                                                         :ARG2 (s14h2 / hard-02)
                                                         :ARG3 (s14m / most))
                                         :ARG4-of (s14h3 / have-org-role-92
                                                         :ARG2 (s14m2 / military)))
                             :ARG2 (s14h / have-rel-role-92
                                         :ARG2 (s14p / person
                                                     :ARG1-of (s14h4 / have-org-role-92
                                                                     :ARG2 s14m2))
                                         :ARG3 (s14s2 / spouse)
                                         :aspect state
                                         :modal-strength full-affirmative)
                             :quote s14s
                             :aspect state
                             :modal-strength full-affirmative)
                 :aspect habitual
                 :modal-strength full-affirmative)
      :op2 (s14h7 / have-org-role-92
                  :ARG1 (s14p2 / person
                               :ARG1-of (s14h5 / have-rel-role-92
                                               :ARG2 (s14p4 / person
                                                            :refer-person 1st
                                                            :refer-number singular)
                                               :ARG3 (s14w / wife)))
                  :ARG3 s14m2
                  :ARG4 s14h
                  :duration (s14t / temporal-quantity
                                  :quant (s14m3 / most)
                                  :duration-of (s14c / career
                                                     :mod (s14h8 / have-org-role-92
                                                                 :ARG1 s14p4
                                                                 :ARG3 s14m2)))
                  :aspect state
                  :modal-strength full-affirmative))

# alignment:

# document level annotation:

## english_umr-0148, sentence 14

# :: snt14
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         
Words: In         Japan      the        civilian   side       was        more       apt        to         seeking    peace      than       the        military   but        in         the        US         it         was        the        military   that       was        pushing    for        peace      more       than       the        civilian   leadership under      Truman.    

# sentence level graph:
(s14c4 / contrast-91
       :ARG1 (s14h / have-degree-91
                   :ARG1 (s14s / side
                               :mod (s14c3 / civilian))
                   :ARG2 (s14a / apt-01
                               :ARG1 (s14s2 / seek-01
                                            :ARG1 (s14p / peace)))
                   :ARG3 (s14m / more)
                   :ARG4 (s14m2 / military)
                   :place (s14c / country
                                :name (s14n / name
                                            :op1 "Japan")
                                :wiki "Japan"))
       :ARG2 (s14h2 / have-degree-91
                    :ARG1 (s14m4 / military)
                    :ARG2 (s14p2 / push-02
                                 :ARG0 s14m4
                                 :ARG2 s14p
                                 :place (s14c2 / country
                                               :name (s14n2 / name
                                                            :op1 "US")
                                               :wiki "United_States"))
                    :ARG3 (s14m3 / more)
                    :ARG4 (s14l / lead-02
                                :ARG0 (s14p3 / person
                                             :name (s14n3 / name
                                                          :op1 "Truman")
                                             :wiki "Harry_S._Truman")
                                :ARG1 (s14c5 / civilian))))

# alignment:

# document level annotation:

## english_umr-0120, sentence 4

# :: snt4
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           
Words: We           have         a            determinable tax          base         from         which        to           draw         these        revenues,    so           lets        assume       that         expected     revenue,     without      difficult    to           support      GDP          changes      based        upon         certain      plans,       remains      the          same.        

# sentence level graph:
(s4h / have-03
     :ARG0 (s4w / we)
     :ARG1 (s4b / base
                :mod (s4t / tax-01)
                :ARG1-of (s4d2 / determine-01
                               :ARG1-of (s4p2 / possible-01))
                :ARG2-of (s4d3 / draw-02
                               :ARG1 (s4r / revenue
                                          :mod (s4t2 / this))))
     :ARG0-of (s4c / cause-01
                   :ARG1 (s4a / assume-02
                              :ARG0 s4w
                              :ARG1 (s4r2 / remain-01
                                          :ARG1 (s4r3 / revenue
                                                      :ARG1-of (s4e / expect-01))
                                          :ARG3 (s4s / same-01
                                                     :ARG1 s4r3)
                                          :manner (s4h2 / have-03
                                                        :ARG1 (s4d4 / difficult
                                                                    :domain (s4s2 / support-01
                                                                                  :ARG1 (s4c2 / change-01
                                                                                              :ARG1 (s4p / product
                                                                                                         :ARG1-of (s4g / gross-03)
                                                                                                         :mod (s4d / domestic))
                                                                                              :ARG1-of (s4b2 / base-02
                                                                                                             :ARG2 (s4p3 / plan-01
                                                                                                                         :mod (s4c3 / certain))))))
                                                        :polarity -))
                              :mode imperative)))

# alignment:

# document level annotation:

## english_umr-0065, sentence 15

# :: snt15
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           39           40           41           42           43           44           45           46           47           48           49           50           51           
Words: As           a            retiree      she          has          medical      benefits     and          arrangements have         been         made         (            which        are          ONLY         available    to           a            legal        spouse       )            that         she          will         receive      part         of           my           retirement   check        if           I            were         to           pass         before       she          does         so           that         she          will         have         something    to           care         for          herself      with         .            

# sentence level graph:
(s15a / and
      :op1 (s15h3 / have-03
                  :ARG0 (s15p4 / person
                               :refer-person 3rd
                               :refer-number singular)
                  :ARG1 (s15t2 / thing
                               :refer-number plural
                               :theme-of (s15b / benefit-01
                                               :ARG1 s15p4
                                               :mod (s15m / medicine)))
                  :cause (s15r / retire-01
                               :ARG0 s15p4
                               :aspect state)
                  :aspect state
                  :modal-strength full-affirmative)
      :op2 (s15a2 / arrange-01
                  :ARG1 (s15r2 / receive-01
                               :ARG0 s15p4
                               :ARG1 (s15t / thing
                                           :part-of (s15c / check
                                                          :mod (s15r3 / retire-01
                                                                      :ARG0 (s15p5 / person
                                                                                    :refer-person 1st
                                                                                    :refer-number singular)
                                                                      :aspect performance
                                                                      :modal-strength full-affirmative)
                                                          :possessor s15p5))
                               :condition (s15p / pass-20
                                                :ARG1 s15p5
                                                :temporal (s15b2 / before
                                                                 :op1 (s15p2 / pass-20
                                                                             :ARG1 s15p4
                                                                             :aspect performance
                                                                             :modal-strength full-affirmative))
                                                :aspect performance
                                                :modal-strength full-affirmative)
                               :aspect performance
                               :modal-strength full-affirmative)
                  :purpose (s15h / have-03
                                 :ARG0 s15p4
                                 :ARG1 (s15t3 / thing
                                              :refer-person 3rd
                                              :refer-number singular
                                              :mod (s15s2 / some)
                                              :instrument-of (s15c2 / care-03
                                                                    :ARG0 s15p4
                                                                    :ARG1 s15p4
                                                                    :aspect activity
                                                                    :modal-strength full-affirmative))
                                 :aspect state
                                 :modal-strength full-affirmative)
                  :ARG2-of (s15a3 / available-02
                                  :ARG1 (s15p3 / person
                                               :ARG1-of (s15h2 / have-rel-role-92
                                                               :ARG3 (s15s3 / spouse
                                                                            :ARG1-of (s15l / legal-02)))
                                               :mod (s15o / only))
                                  :aspect state
                                  :modal-strength full-affirmative)
                  :aspect performance
                  :modal-strength full-affirmative))

# alignment:

# document level annotation:

## english_umr-0283, sentence 5

# :: snt5
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          
Words: <Architect> we          need        2           3x3         purple      windows     (with       the         center      open)       next        to          each        other       but         with        1           space       in          between     the         squares.    

# sentence level graph:
(s5n / need-01
     :ARG1 (s5b / be-destined-for-91
                :ARG1 (s5w / window
                           :size (s5d / dimension-entity
                                      :value 3)
                           :size (s5d2 / dimension-entity
                                       :value 3)
                           :ARG2-of (s5c / center-03
                                         :ARG1 (s5t / thing
                                                    :ARG1-of (s5o / open-06)))
                           :quant 2)
                :manner (s5n2 / next-to-02
                              :ARG1 (s5s2 / square
                                          :ARG1-of (s5i2 / include-91
                                                         :ARG2 s5w))
                              :ARG2 (s5s3 / square
                                          :ARG1-of (s5i3 / include-91
                                                         :ARG2 s5w))
                              :ARG3 (s5c3 / cartesian-framework-91
                                          :ARG1 (s5b3 / build-space))
                              :ARG1-of (s5c2 / contrast-91
                                             :ARG2 (s5b2 / between-01
                                                         :ARG1 (s5s / space
                                                                    :quant 1)
                                                         :ARG2 s5s2
                                                         :ARG3 s5s3)))))

# alignment:

# document level annotation:

## english_umr-0020, sentence 1

# :: snt1
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           
Words: According    to           most         analyses,    from         within       and          without      the          petroleum    Industry,    the          world        supply       of           oil,         relative     consumption, will         effectively  peak         in           the          next         decade.      

# sentence level graph:
(s1s / say-01
     :ARG0 (s1a4 / and
                 :op1 (s1a / analysis
                           :source (s1i2 / industry
                                         :mod (s1p / petroleum)))
                 :op2 (s1a2 / analysis
                            :ARG1-of (s1h / have-source-91
                                          :ARG2 s1i2
                                          :polarity -))
                 :mod (s1m / most))
     :ARG1 (s1p2 / peak-01
                 :ARG1 (s1a3 / and
                             :op1 (s1s2 / supply-01
                                        :ARG0 (s1w3 / world)
                                        :ARG1 (s1o / oil))
                             :op2 (s1c / consume-01
                                       :ARG1 s1o
                                       :ARG1-of (s1r / relative-05)))
                 :ARG1-of (s1e / effective-04)
                 :temporal (s1d / decade
                                :mod (s1n / next))))

# alignment:

# document level annotation:

## english_umr-0578, sentence 15

# :: snt15
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           
Words: The          total        of           18           deaths       from         malignant    mesothelioma ,            lung         cancer       and          asbestosis   was          far          higher       than         expected     ,            the          researchers  said         .            

# sentence level graph:
(s15s / say-01
    :ARG0 (s15p / person
        :ARG0-of (s15r / research-01))
    :ARG1 (s15h2 / have-degree-91
        :ARG1 (s15q / quantity :quant 18
            :ARG2-of (s15h3 / have-quant-91 
                :ARG1 (s15s2 / sum-of 
                    :op1 (s15d / die-01
                        :cause (s15d4 / disease :wiki "Mesothelioma" 
                            :name (s15n / name :op1 "malignant" :op2 "mesothelioma"))
                        :aspect performance)
                    :op2 (s15d5 / die-01
                        :cause (s15d2 / disease :wiki "Lung_cancer" 
                            :name (s15n2 / name :op1 "lung" :op2 "cancer"))
                        :aspect performance)
                    :op3 (s15d6 / die-01
                        :cause (s15d3 / disease :wiki "Asbestosis" 
                            :name (s15n3 / name :op1 "asbestosis"))
                        :aspect performance))))
        :ARG2 (s15h / high-02)
        :ARG3 (s15m / more
            :degree intensifier)
        :ARG4 (s15q2 / quantity
            :ARG1-of (s15e / expect-01
                :ARG0 s15p
                :aspect state))
        :aspect state
        :quote s15s)
    :aspect performance)

# alignment:
s15s: 22-22
s15p: 21-21
s15r: 21-21
s15h2: 16-16
s15q: 2-2
s15h3: 0-0
s15s2: 2-2
s15d: 5-5
s15d4: 7-8
s15n: 7-8
s15d5: 5-5
s15d2: 10-11
s15n2: 10-11
s15d6: 5-5
s15d3: 13-13
s15n3: 13-13
s15h: 16-16
s15m: 16-16
s15q2: 0-0
s15e: 18-18

# document level annotation:
(s15s0 / sentence
    :coref ((s13d :subset-of s15d)
            (s13d :subset-of s15d5)
            (s13d :subset-of s15d6)
            (s15p :same-entity s10t3)
            (s14d :subset-of s15d4)
            (s14d :subset-of s15d3)
            (s14d :subset-of s15d2))
    :temporal ((document-creation-time :before s15s)
            (s15s :contains s15e)
            (s15s :before s15d)
            (s15s :before s15d5)
            (s15s :before s15d6)
            (s15h :before s15e))
    :modal ((root :modal author)
            (author :full-affirmative s15s)
            (author :full-affirmative s15p)
            (s15p :full-affirmative s15h2)
            (s15p :full-affirmative s15e)
            (s15p :full-affirmative s15d)
            (s15p :full-affirmative s15d5)
            (s15p :full-affirmative s15d6)))

## english_umr-0199, sentence 8

# :: snt8
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          
Words: Cunliffe    said        ,           it          has         presently   not         been        decided     when        or          how         the         biometric   information will        be          collected   from        people      's          bodies      .           

# sentence level graph:
(s8s / say-01
     :ARG0 (s8p2 / person
                 :name (s8n / name
                            :op1 "Cunliffe")
                 :wiki "David_Cunliffe")
     :ARG1 (s8d / decide-01
                :ARG3 (s8o / or
                           :op1 (s8t2 / time
                                      :temporal-of (s8c3 / collect-01
                                                         :ARG1 (s8i / information
                                                                    :mod (s8b / biometric))
                                                         :ARG2 (s8b2 / body
                                                                     :possessor (s8p4 / person))
                                                         :manner (s8t / thing)))
                           :op2 s8t)
                :temporal (s8p3 / present)
                :polarity -))

# alignment:

# document level annotation:

## english_umr-0010, sentence 2

# :: snt2
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          
Words: Where       is          the         morality    in          creating    a           life        when        food        and         clean       water       are         rare        commodities ?           

# sentence level graph:
(s2m / moral-02
     :reason (s2u / umr-unknown)
     :ARG1 (s2c4 / create-01
                 :ARG1 (s2t / thing
                            :ARG1-of (s2l2 / live-01))
                 :temporal (s2h / have-role-91
                                :ARG1 (s2a2 / and
                                            :op1 (s2f / food)
                                            :op2 (s2w / water
                                                      :ARG1-of (s2c3 / clean-01)))
                                :ARG3 (s2c2 / commodity
                                            :ARG1-of (s2r / rare-02)
                                            :refer-number plural)
                                :aspect state
                                :modal-strength full-affirmative)
                 :aspect performance
                 :modal-strength full-affirmative)
     :aspect state
     :modal-strength full-affirmative)

# alignment:

# document level annotation:

## english_umr-0058, sentence 1

# :: snt1
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            
Words: we            all           knew          that          Santorums     biggest       set           back          was           the           fact          that          he            doesn't       come          off           as            presidential, but           he            does          have          one           vital         thing         going         for           him,,he       is            very          likable       and           the           GOP           and           Conservative  base          will          settle        for           him           much          more          than          Romney.       

# sentence level graph:
(s1a4 / and
      :op1 (s1c / contrast-91
                 :ARG1 (s1k / know-01
                            :ARG0 (s1w / we
                                       :mod (s1a3 / all))
                            :ARG1 (s1c2 / come-across-15
                                        :ARG1 (s1p3 / person
                                                    :name (s1n3 / name
                                                                :op1 "Santorum")
                                                    :wiki "Rick_Santorum")
                                        :ARG2 (s1p4 / person
                                                    :ARG1-of (s1h / have-org-role-92
                                                                  :ARG3 (s1p5 / president)))
                                        :ARG1-of (s1m / mean-91
                                                      :ARG2 (s1s / setback
                                                                 :possessor s1p3
                                                                 :ARG1-of (s1h4 / have-degree-91
                                                                                :ARG2 (s1b2 / big)
                                                                                :ARG3 (s1m3 / most))))
                                        :polarity -))
                 :ARG2 (s1h2 / have-03
                             :ARG0 s1p3
                             :ARG1 (s1t / thing
                                        :mod (s1v / vital)
                                        :ARG1-of (s1g / go-21
                                                      :ARG2 s1p3)
                                        :quant 1)))
      :op2 (s1a / and
                 :op1 (s1l / likable
                           :domain (s1h3 / he)
                           :degree (s1v2 / very))
                 :op2 (s1s2 / settle-01
                            :ARG0 (s1a2 / and
                                        :op1 (s1b / base
                                                  :mod (s1p / political-organization
                                                            :name (s1n / name
                                                                       :op1 "GOP")
                                                            :wiki "Republican_Party_(United_States)"))
                                        :op2 (s1b3 / base
                                                   :mod (s1c3 / conservative)))
                            :ARG2 s1h3
                            :ARG1-of (s1h5 / have-quant-91
                                           :ARG2 (s1m5 / much)
                                           :ARG3 (s1m4 / more)
                                           :ARG4 (s1s3 / settle-01
                                                       :ARG0 s1a2
                                                       :ARG1 (s1p6 / person
                                                                   :name (s1n6 / name
                                                                               :op1 "Romney")
                                                                   :wiki "Mitt_Romney"))))))

# alignment:

# document level annotation:

## english_umr-0195, sentence 60

# :: snt60
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         40         41         42         43         44         45         
Words: When       Michael    finds      the        courage    to         act        on         what       his        duty       toward     other      children   demands    --         submit     to         voluntary  neutering  --         which      will       be         tantamount to         his        final      confession ,          the        saving     grace      and        glory      that       is         his        Neverland  will       become     his        forever    land       .          

# sentence level graph:
(s60h / have-role-91
      :ARG1 (s60b / become-01
                  :ARG1 (s60f2 / facility
                               :name (s60n2 / name
                                            :op1 "Neverland")
                               :possessor (s60p2 / person
                                                 :name (s60n3 / name
                                                              :op1 "Michael")
                                                 :wiki "Michael_Jackson")
                               :wiki "Neverland_Ranch")
                  :ARG2 (s60l / land
                              :ARG2-of (s60h2 / have-place-91
                                              :ARG1 s60p2
                                              :duration (s60f3 / forever)))
                  :aspect performance
                  :modal-strength full-affirmative)
      :ARG3 (s60a / and
                  :op1 (s60g / grace)
                  :op2 (s60g2 / glory)
                  :ARG0-of (s60s / save-02
                                 :ARG1 s60p2
                                 :aspect activity
                                 :modal-strength full-affirmative))
      :temporal (s60f4 / find-01
                       :ARG0 s60p2
                       :ARG1 (s60c / courage)
                       :purpose (s60a2 / act-02
                                       :ARG0 s60p2
                                       :ARG1 (s60s2 / submit-02
                                                    :ARG0 s60p2
                                                    :ARG2 (s60n / neuter-01
                                                                :ARG1 s60p2
                                                                :ARG1-of (s60v / voluntary-02
                                                                               :ARG0 s60p2
                                                                               :ARG2 s60p2)
                                                                :aspect performance
                                                                :modal-strength full-affirmative)
                                                    :ARG1-of (s60t / tantamount-01
                                                                   :ARG2 (s60c3 / confess-01
                                                                                :ARG0 s60p2
                                                                                :mod (s60f5 / final)
                                                                                :aspect performance
                                                                                :modal-strength full-affirmative)
                                                                   :aspect state
                                                                   :modal-strength full-affirmative)
                                                    :ARG1-of (s60d / demand-01
                                                                   :ARG0 (s60d2 / duty-01
                                                                                :ARG0 s60p2
                                                                                :ARG1 s60s2
                                                                                :ARG2 (s60c2 / child
                                                                                             :ARG1-of (s60o / other-01)
                                                                                             :refer-number plural))
                                                                   :aspect state
                                                                   :modal-strength full-affirmative)
                                                    :aspect performance
                                                    :modal-strength full-affirmative)
                                       :aspect performance
                                       :modal-strength full-affirmative)
                       :aspect performance
                       :modal-strength full-affirmative)
      :aspect state
      :modal-strength full-affirmative)

# alignment:

# document level annotation:

## english_umr-0229, sentence 417

# :: snt417
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          
Words: So          the         little      prince      ,           in          spite       of          all         the         good        will        that        was         inseparable from        his         love        ,           had         soon        come        to          doubt       her         .           

# sentence level graph:
(s417c / come-04
       :ARG1 (s417p / prince
                    :mod (s417l / little))
       :ARG2 (s417d / doubt-01
                    :ARG0 s417p
                    :ARG1 (s417s3 / she))
       :temporal (s417s / soon)
       :ARG1-of (s417h / have-reason-91)
       :concession (s417w / will
                          :ARG1-of (s417g / good-02)
                          :mod (s417a / all)
                          :ARG1-of (s417s2 / separate-01
                                           :ARG2 (s417l2 / love-01
                                                         :ARG0 s417p)
                                           :ARG1-of (s417p2 / possible-01
                                                            :polarity -))))

# alignment:

# document level annotation:

## english_umr-0038, sentence 39

# :: snt39
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         40         41         42         
Words: whilst     I          agree      that       D          Cameron    and        the        tories     aren't     doing      everything they       said       they       would,     they       are        trying     to         cut        back       the        welfare    state      and        dismantle  some       of         the        ridiculous laws       that       stop       businesses and        workers    from       operating  at         their      highest    

# sentence level graph:
(s39c / contrast-91
      :ARG1 (s39t / try-01
                  :ARG0 (s39t2 / they)
                  :ARG1 (s39a / and
                              :op1 (s39c2 / cut-back-05
                                          :ARG0 s39t2
                                          :ARG1 (s39s / state
                                                      :mod (s39w / welfare)))
                              :op2 (s39d / dismantle-01
                                         :ARG0 s39t2
                                         :ARG1 (s39s2 / some
                                                      :ARG1-of (s39i / include-91
                                                                     :ARG2 (s39l / law
                                                                                 :ARG1-of (s39r / ridiculous-02)
                                                                                 :ARG0-of (s39s3 / stop-03
                                                                                                 :ARG1 (s39a2 / and
                                                                                                              :op1 (s39b / business)
                                                                                                              :op2 (s39p / person
                                                                                                                         :ARG0-of (s39w2 / work-01)))
                                                                                                 :ARG2 (s39o / operate-01
                                                                                                             :ARG0 s39a2
                                                                                                             :manner (s39h / high-02
                                                                                                                           :ARG2-of (s39h2 / have-degree-91
                                                                                                                                           :ARG1 s39o
                                                                                                                                           :ARG3 (s39m / most)))))))))))
      :ARG2 (s39a3 / agree-01
                   :ARG0 (s39i2 / i)
                   :ARG1 (s39d2 / do-02
                                :ARG0 (s39a4 / and
                                             :op1 (s39p2 / person
                                                         :name (s39n / name
                                                                     :op1 "D"
                                                                     :op2 "Cameron")
                                                         :wiki "David_Cameron")
                                             :op2 (s39p3 / political-organization
                                                         :name (s39n2 / name
                                                                      :op1 "Tory")
                                                         :wiki "Conservative_Party_(UK)"))
                                :ARG1 (s39e / everything
                                            :ARG1-of (s39s4 / say-01
                                                            :ARG3 (s39d3 / do-02
                                                                         :ARG0 s39a4)))
                                :polarity -)))

# alignment:

# document level annotation:

## english_umr-0525, sentence 58

# :: snt58
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          
Words: <Architect> Now         we          need        to          make        a           floating    block       which       is          one         space       higher      than        that        blue,       next        to          it          on          the         side        away        from        the         red         

# sentence level graph:
(s58n / need-01
      :ARG0 (s58w / we)
      :ARG1 (s58m / make-01
                  :ARG0 s58w
                  :ARG1 (s58b / block
                              :ARG1-of (s58f / float-01)
                              :place (s58s / space
                                           :ARG1-of (s58h / have-degree-91
                                                          :ARG2 (s58h2 / high-02
                                                                       :ARG1 s58s
                                                                       :ARG6 (s58c / cartesian-framework-91
                                                                                   :ARG1 (s58b3 / build-space)))
                                                          :ARG3 (s58m2 / more
                                                                       :quant (s58d / distance-quantity
                                                                                    :unit (s58s3 / space)
                                                                                    :quant 1))
                                                          :ARG4 (s58t / thing
                                                                      :color (s58b2 / blue)
                                                                      :mod (s58t2 / that)
                                                                      :part (s58s2 / side
                                                                                   :ARG1-of (s58a / away-01
                                                                                                  :ARG2 (s58t3 / thing
                                                                                                               :color (s58r / red))))))
                                           :ARG1-of (s58n3 / next-to-02
                                                           :ARG2 s58s2
                                                           :ARG2 s58c))))
      :temporal (s58n2 / now))

# alignment:

# document level annotation:

## english_umr-0214, sentence 1010

# :: snt1010
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       26       27       28       29       30       31       32       33       34       35       36       
Words: "        From     a        mountain as       high     as       this     one      ,        "        he       said     to       himself  ,        "        I        shall    be       able     to       see      the      whole    planet   at       one      glance   ,        and      all      the      people   ...      "        

# sentence level graph:
(s1010s / say-01
        :ARG0 (s1010h / he)
        :ARG1 (s1010p / possible-01
                      :ARG1 (s1010s2 / see-01
                                     :ARG0 s1010h
                                     :ARG1 (s1010a / and
                                                   :op1 (s1010p2 / planet
                                                                 :extent (s1010w / whole))
                                                   :op2 (s1010p3 / person
                                                                 :mod (s1010a3 / all)))
                                     :place (s1010m / mountain
                                                    :ARG1-of (s1010h3 / have-degree-91
                                                                      :ARG2 (s1010h2 / high-02
                                                                                     :ARG1 s1010m)
                                                                      :ARG3 (s1010e / equal)
                                                                      :ARG4 (s1010m2 / mountain
                                                                                     :mod (s1010t / this))))
                                     :manner (s1010g / glance-01
                                                     :quant 1))
                      :quote s1010s)
        :ARG2 s1010h)

# alignment:

# document level annotation:
