# Gold UMR annotations of sentences like those of english_umr-0006

From ai-native-annotator.github.io data/skillparse/resources/gold/en/gold.json (no test document).

## english_umr-0030, sentence 25

# :: snt25
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        
Words: And       try       and       get       deadlines extended, if        you're    honest    I'm       sure      your      uni       will      allow     it.       

# sentence level graph:
(s25a3 / and
      :op2 (s25s / sure-02
                  :ARG0 (s25i / i)
                  :ARG1 (s25a / allow-01
                              :ARG0 (s25u / university
                                          :possessor (s25y2 / you))
                              :ARG1 (s25i2 / it))
                  :condition (s25h / honest-01
                                   :ARG0 (s25y / you)))
      :op1 (s25a2 / and
                   :op1 (s25t / try-01
                              :ARG0 s25y
                              :ARG1 (s25g / get-04
                                          :ARG0 s25y
                                          :ARG1 (s25e / extend-01
                                                      :ARG1 (s25d / deadline)))
                              :mode imperative)))

# alignment:

# document level annotation:

## english_umr-0030, sentence 11

# :: snt11
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         
Words: -          Now        the        work-load  is         up         to         my         neck,      I          have       major      deadlines  to         hit,       I          am         depressed, the        anxiety    is         resulting  in         me         feeling    miserable  all        the        time.      

# sentence level graph:
(s11a / and
      :op1 (s11l / load-01
                 :ARG1 (s11i / i
                             :part (s11n2 / neck))
                 :ARG2 (s11t2 / thing
                              :ARG1-of (s11w / work-01))
                 :temporal (s11n / now)
                 :extent s11n2)
      :op2 (s11o / obligate-01
                 :ARG2 (s11h / hit-02
                             :ARG0 s11i
                             :ARG1 (s11d2 / deadline
                                          :ARG1-of (s11m / major-02))))
      :op3 (s11d / depress-01
                 :ARG1 s11i)
      :op4 (s11r / result-01
                 :ARG1 (s11a2 / anxiety)
                 :ARG2 (s11f / feel-01
                             :ARG0 s11i
                             :ARG1 (s11m2 / miserable)
                             :frequency (s11t / time
                                              :mod (s11a3 / all)))))

# alignment:

# document level annotation:

## english_umr-0030, sentence 18

# :: snt18
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        
Words: Perhaps   go        and       see       your      doctor,   and       see       if        there's   any       way       you       can       get       your      deadlines extended  to        try       and       ease      the       pressure  a         bit?      

# sentence level graph:
(s18a / and
      :op1 (s18a2 / and
                  :op1 (s18g / go-02
                             :ARG0 (s18y / you)
                             :mode imperative)
                  :op2 (s18s2 / see-01
                              :ARG0 s18y
                              :ARG1 (s18p4 / person
                                           :ARG1-of (s18h / have-org-role-92
                                                          :ARG2 s18y
                                                          :ARG3 (s18d / doctor)))
                              :mode imperative)
                  :ARG1-of (s18p / possible-01))
      :op2 (s18s / see-01
                 :ARG0 s18y
                 :ARG1 (s18w / way
                             :manner-of (s18g2 / get-04
                                               :ARG1 (s18e / extend-01
                                                           :ARG0 s18y
                                                           :ARG1 (s18d2 / deadline
                                                                        :possessor s18y)
                                                           :purpose (s18t2 / try-01
                                                                           :ARG0 s18y
                                                                           :ARG1 (s18e2 / ease-02
                                                                                        :ARG0 s18y
                                                                                        :ARG1 (s18p3 / pressure)
                                                                                        :degree (s18b / bit))))
                                               :ARG1-of (s18p2 / possible-01))
                             :polarity (s18a3 / umr-unknown))
                 :mode imperative))

# alignment:

# document level annotation:

## english_umr-0038, sentence 9

# :: snt9
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         
Words: Likewise   when       services   had        to         shut       down       after      a          day        because    of         snow,      the        media      launched   a          full       blown      attack     and        everyday   people     were       saying     how        disgusting it         was.       

# sentence level graph:
(s9a / and
     :op1 (s9l / launch-01
               :ARG0 (s9m / media)
               :ARG1 (s9a2 / attack-01
                           :ARG0 s9m
                           :ARG1-of (s9b / blow-01)
                           :mod (s9f / full)))
     :op2 (s9s / say-01
               :ARG0 (s9p / person
                          :mod (s9e / everyday))
               :ARG1 (s9t3 / thing
                           :degree-of (s9d / disgust-01
                                           :ARG0 (s9i / it))))
     :temporal (s9o / obligate-01
                    :ARG1 (s9s2 / service)
                    :ARG2 (s9s3 / shut-down-05
                                :ARG1 s9s2)
                    :temporal (s9a3 / after
                                    :quant (s9t / temporal-quantity
                                                :unit (s9d2 / day)
                                                :quant 1))
                    :ARG1-of (s9c / cause-01
                                  :ARG0 (s9s4 / snow-01)))
     :mod (s9l2 / likewise))

# alignment:

# document level annotation:

## english_umr-0202, sentence 4

# :: snt4
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        31        32        33        34        35        36        37        38        39        
Words: Although  under     the       balance   of        interests some      of        Sunni     political figures   were      involved  in        politics  ,         what      the       Sunni     radical   groups    were      most      concerned about     was       that      the       Shiites   would     turn      around    and       suppress  them      in        the       future    .         

# sentence level graph:
(s4h / have-concession-91
     :ARG1 (s4a3 / and
                 :op1 (s4t / turn-01
                           :ARG1 (s4r3 / religious-group
                                       :name (s4n4 / name
                                                   :op1 "Shiites")
                                       :wiki "Shia_Islam")
                           :direction (s4a2 / around))
                 :op2 (s4s3 / suppress-01
                            :ARG0 s4r3
                            :ARG1 (s4r2 / religious-group
                                        :name (s4n3 / name
                                                    :op1 "Sunni")
                                        :wiki "Sunni_Islam"))
                 :temporal (s4f / future)
                 :ARG0-of (s4c / concern-01
                               :ARG1 (s4g / group
                                          :ARG1-of (s4r / radical-02)
                                          :mod s4r2)
                               :ARG2-of (s4h2 / have-degree-91
                                              :ARG1 s4g
                                              :ARG3 (s4m / most))))
     :ARG2 (s4i2 / involve-01
                 :ARG1 (s4f3 / figure
                             :mod (s4s / some)
                             :mod (s4p / politics)
                             :ARG1-of (s4i3 / include-91
                                            :ARG2 (s4f2 / figure
                                                        :mod s4p
                                                        :mod s4r2))
                             :mod s4r2)
                 :ARG2 s4p
                 :ARG1-of (s4c2 / cause-01
                                :ARG0 (s4b / balance-01
                                           :ARG1 (s4i4 / interest)))))

# alignment:

# document level annotation:

## english_umr-0038, sentence 8

# :: snt8
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          
Words: When        petrol      costs       rose        when        Labour      were        in          government, there       was         a           media       frenzy.     

# sentence level graph:
(s8c2 / cause-01
      :ARG0 (s8r / rise-01
                 :ARG1 (s8c / cost-01
                            :ARG1 (s8p / petrol))
                 :temporal (s8g / govern-01
                                :ARG0 (s8p2 / political-organization
                                            :name (s8n / name
                                                       :op1 "Labour")
                                            :wiki "Labour_Party_(UK)")))
      :ARG1 (s8f / frenzy
                 :mod (s8m / media)))

# alignment:

# document level annotation:

## english_umr-0245, sentence 86

# :: snt86
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          
Words: <Architect> if          you         could       do          that        exact       structure   so          that        its         on          the         left        side        of          the         red         square      from        where       you         were        standing    it          will        be          correct     

# sentence level graph:
(s86c / correct-02
      :ARG1 (s86i2 / it)
      :condition (s86d / do-02
                       :ARG0 (s86y / you
                                   :temporal (s86b / before
                                                   :temporal-of (s86s3 / stand-01
                                                                       :ARG0 s86y
                                                                       :ARG2 (s86s4 / space))))
                       :ARG1 (s86s / structure
                                   :mod (s86e / exact)
                                   :mod (s86t / that))
                       :manner (s86l / left-20
                                     :ARG1 s86s
                                     :ARG2 (s86s2 / square
                                                  :color (s86r / red))
                                     :ARG3 (s86c2 / cartesian-framework-91
                                                  :ARG1 s86y
                                                  :orientation FV1))))

# alignment:

# document level annotation:

## english_umr-0578, sentence 12

# :: snt12
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         
Words: From       1953       to         1955       ,          9.8        billion    Kent       cigarettes with       the        filters    were       sold       ,          the        company    said       .          

# sentence level graph:
(s12s / say-01
    :ARG0 (s12c / company)
    :ARG1 (s12s2 / sell-01
        :ARG1 (s12p / product :wiki "Kent_(cigarette)"
            :quant 9800000000 
            :name (s12n / name :op1 "Kent" :op2 "cigarette")
            :part (s12t / thing
                :refer-number plural
                :instrument-of (s12f / filter-02)))
        :temporal (s12d / date-interval
            :op1 (s12d2 / date-entity :year 1953)
            :op2 (s12d3 / date-entity :year 1955))
        :aspect performance
        :quote s12s)
    :aspect performance)

# alignment:
s12s: 18-18
s12c: 17-17
s12s2: 14-14
s12p: 8-9
s12n: 8-9
s12t: 12-12
s12f: 12-12
s12d: 1-1
s12d2: 2-2
s12d3: 4-4

# document level annotation:
(s12s0 / sentence
    :coref ((s12t :same-entity s11t)
            (s8p :subset-of s12p)
            (s12c :same-entity s11c))
    :temporal ((document-creation-time :before s12s)
            (s12s2 :after s12s)
            (root :depends-on s12d2)
            (root :depends-on s12d3)
            (s12s2 :overlap s12d2)
            (s12s2 :overlap s12d3))
    :modal ((root :modal author)
            (author :full-affirmative s12s)
            (author :full-affirmative s12c)
            (s12c :full-affirmative s12s2)))

## english_umr-0211, sentence 927

# :: snt927
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           39           40           
Words: After        that         would        come         the          turn         of           the          lamplighters of           Russia       and          the          Indies       ;            then         those        of           Africa       and          Europe       ,            then         those        of           South        America      ;            then         those        of           South        America      ;            then         those        of           North        America      .            

# sentence level graph:
(s927c8 / come-03
        :ARG1 (s927t2 / turn
                      :possessor (s927p / person
                                        :ARG0-of (s927l / light-04
                                                        :ARG1 (s927l2 / lamp)
                                                        :ARG0 (s927p3 / person
                                                                      :place (s927c2 / continent
                                                                                     :name (s927n / name
                                                                                                  :op1 "South"
                                                                                                  :op2 "America")
                                                                                     :wiki "South_America"))
                                                        :ARG0 (s927p2 / person
                                                                      :place (s927a4 / and
                                                                                     :op1 (s927c4 / continent
                                                                                                  :name (s927n5 / name
                                                                                                                :op1 "Africa")
                                                                                                  :wiki "Africa")
                                                                                     :op2 (s927c5 / continent
                                                                                                  :name (s927n6 / name
                                                                                                                :op1 "Europe")
                                                                                                  :wiki "Europe")))
                                                        :ARG0 (s927p4 / person
                                                                      :place (s927a2 / and
                                                                                     :op1 (s927c / country
                                                                                                 :name (s927n3 / name
                                                                                                               :op1 "Russia")
                                                                                                 :wiki "Russia")
                                                                                     :op2 (s927w / world-region
                                                                                                 :name (s927n4 / name
                                                                                                               :op1 "Indies")
                                                                                                 :wiki "East_Indies"))))
                                        :place (s927c3 / continent
                                                       :name (s927n2 / name
                                                                     :op1 "North"
                                                                     :op2 "America")
                                                       :wiki "North_America"))
                      :temporal (s927a / after
                                       :op1 (s927t / turn
                                                   :possessor s927p3
                                                   :temporal (s927a6 / after
                                                                     :op1 (s927t3 / turn
                                                                                  :possessor s927p2
                                                                                  :temporal (s927a3 / after
                                                                                                    :op1 (s927t4 / turn
                                                                                                                 :possessor s927p4))))))))

# alignment:

# document level annotation:

## english_umr-0263, sentence 6

# :: snt6
Index: 1           2           3           4           5           6           7           8           9           10          11          
Words: <Architect> ok          there       are         2           flat        crosses     and         2           upright     crosses.    

# sentence level graph:
(s6a / and
     :op1 (s6o / okay-04)
     :op2 (s6c / cross
               :ARG1-of (s6f / flat-06)
               :quant 2)
     :op3 (s6c2 / cross
                :ARG1-of (s6u / upright-08
                              :ARG3 (s6c3 / cartesian-framework-91
                                          :ARG1 (s6b / build-space)))
                :quant 2))

# alignment:

# document level annotation:

## english_umr-0040, sentence 1

# :: snt1
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          
Words: I           think       immigration levels      are         high,       and         our         past        pm's        like        gordon      brown       think       that        talking     about       high        immigration is          bigoted.    

# sentence level graph:
(s1a / and
     :op1 (s1t / think-01
               :ARG0 (s1i / i)
               :ARG1 (s1h / high-02
                          :ARG1 (s1l / level
                                     :mod (s1i2 / immigrate-01))))
     :op2 (s1t2 / think-01
                :ARG0 (s1p4 / person
                            :possessor (s1w / we)
                            :example (s1p / person
                                          :name (s1n / name
                                                     :op1 "Gordon"
                                                     :op2 "Brown")
                                          :wiki "Gordon_Brown")
                            :ARG1-of (s1h2 / have-org-role-92
                                           :ARG3 (s1m / minister
                                                      :mod (s1p2 / prime))
                                           :temporal (s1p3 / past)))
                :ARG1 (s1b / bigot
                           :domain (s1t3 / talk-01
                                         :ARG1 s1h))))

# alignment:

# document level annotation:

## english_umr-0211, sentence 920

# :: snt920
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            46            47            
Words: One           can           count         ,             there         111           kings         (             not           forgetting    ,             to            be            sure          ,             the           Negro         kings         among         them          )             ,             7000          geographers   ,             900,000       businessmen   ,             7,500,000     tipplers      ,             311,000,000   conceited     men           -             -             that          is            to            say           ,             about         2,000,000,000 grown         -             ups           .             

# sentence level graph:
(s920p / possible-01
       :ARG1 (s920a3 / and
                     :op1 (s920c / count-01
                                 :ARG0 (s920o / one)
                                 :ARG1 (s920a / and
                                              :op1 (s920p5 / person
                                                           :ARG1-of (s920h2 / have-org-role-92
                                                                            :ARG3 (s920k / king))
                                                           :quant 111)
                                              :op2 (s920g2 / geographer
                                                           :quant 7000)
                                              :op3 (s920b / businessman
                                                          :quant 900000)
                                              :op4 (s920p4 / person
                                                           :ARG0-of (s920t2 / tipple-01)
                                                           :quant 7500000)
                                              :op5 (s920m / man
                                                          :mod (s920c2 / conceited)
                                                          :quant 311000000)
                                              :mod (s920g3 / grown-up
                                                           :quant (s920a2 / about
                                                                          :op1 2000000000)))
                                 :place (s920t / there))
                     :op2 (s920f / forget-01
                                 :ARG0 s920o
                                 :ARG1 (s920n / negro
                                              :ARG1-of (s920i2 / include-91
                                                               :ARG2 s920p5)
                                              :ARG1-of (s920h / have-org-role-92
                                                              :ARG3 (s920k2 / king)))
                                 :mod (s920t3 / to-be-sure)
                                 :polarity -)))

# alignment:

# document level annotation:

## english_umr-0420, sentence 12

# :: snt12
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          
Words: <Architect> so          from        the         first       green       you         placed      add         two         90          degrees     to          what        you         just        made        

# sentence level graph:
(s12a / add-02
      :ARG0 (s12y / you)
      :ARG1 (s12t / thing
                  :consist (s12t4 / thing)
                  :quant 2)
      :ARG2 (s12t3 / thing
                   :ord (s12o2 / ordinal-entity
                               :value 1)
                   :ARG1-of (s12p / place-01
                                  :ARG0 s12y)
                   :color (s12g / green))
      :manner (s12o / orient-01
                    :ARG1 s12t4
                    :ARG4 (s12r / relative-orientation
                                :op1 (s12t2 / thing
                                            :ARG1-of (s12m / make-01
                                                           :ARG0 s12y
                                                           :temporal (s12j / just)))
                                :quant (s12a2 / angle-quantity
                                              :unit (s12d / degree)
                                              :quant 90)))
      :mode imperative)

# alignment:

# document level annotation:

## english_umr-0196, sentence 38

# :: snt38
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        31        32        33        34        35        36        37        38        39        40        41        42        43        44        45        46        47        48        49        50        51        52        53        54        
Words: He        explained Balqes    '         gripe     and       what      the       loss      of        her       job       had       meant     for       their     family    ,         including their     3         -         year      -         old       son       and       Balqes    '         14        -         year      -         old       son       from      a         previous  marriage  (         her       first     husband   had       been      killed    in        the       Iran      -         Iraq      War       )         .         

# sentence level graph:
(s38a4 / and
       :op1 (s38e2 / explain-01
                    :ARG0 (s38h / he)
                    :ARG1 (s38a / and
                                :op1 (s38g / gripe-01
                                           :ARG0 (s38p2 / person
                                                        :name (s38n / name
                                                                    :op1 "Balqes")
                                                        :wiki -))
                                :op2 (s38t2 / thing
                                            :ARG2-of (s38m / mean-01
                                                           :ARG1 (s38l / lose-02
                                                                       :ARG1 (s38j / job
                                                                                   :possessor s38p2))
                                                           :ARG3 (s38f / family
                                                                       :ARG2-of (s38i2 / include-01
                                                                                       :ARG1 (s38a3 / and
                                                                                                    :op1 (s38p3 / person
                                                                                                                :age (s38t4 / temporal-quantity
                                                                                                                            :unit (s38y / year)
                                                                                                                            :quant 3)
                                                                                                                :ARG1-of (s38h3 / have-rel-role-92
                                                                                                                                :ARG2 (s38a2 / and
                                                                                                                                             :op1 s38h
                                                                                                                                             :op2 s38p2)
                                                                                                                                :ARG3 (s38s / son)))
                                                                                                    :op2 (s38p4 / person
                                                                                                                :age (s38t / temporal-quantity
                                                                                                                           :unit (s38y2 / year)
                                                                                                                           :quant 14)
                                                                                                                :source (s38m2 / marry-01
                                                                                                                               :ARG1 s38p2
                                                                                                                               :temporal (s38p / previous))
                                                                                                                :ARG1-of (s38h4 / have-rel-role-92
                                                                                                                                :ARG2 s38p2
                                                                                                                                :ARG3 (s38s2 / son)))))
                                                                       :ARG2-of (s38h6 / have-org-role-92
                                                                                       :ARG1 s38a2
                                                                                       :ARG3 (s38m4 / member)))))))
       :op2 (s38k / kill-01
                   :ARG1 (s38p5 / person
                                :ARG1-of (s38h2 / have-rel-role-92
                                                :ARG2 (s38s3 / she)
                                                :ARG3 (s38h5 / husband
                                                             :ord (s38o / ordinal-entity
                                                                        :value 1))))
                   :temporal (s38w / war
                                   :name (s38n2 / name
                                                :op1 "Iran-Iraq"
                                                :op2 "War")
                              
… (73 more characters)

## english_umr-0489, sentence 55

# :: snt55
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          
Words: <Architect> okay,       do          another     three       by          two         green       rectangle   that        is          flush       with        what        you         just        put         down,       no          the         right       

# sentence level graph:
(s55a2 / and
       :op1 (s55o2 / okay-04)
       :op2 (s55d / do-02
                  :ARG0 (s55y / you)
                  :ARG1 (s55r / rectangle
                              :mod (s55a / another)
                              :ARG1-of (s55f / flush-04
                                             :ARG2 (s55t / thing
                                                         :ARG1-of (s55p / put-down-17
                                                                        :ARG0 s55y
                                                                        :temporal (s55j / just))))
                              :color (s55g / green)
                              :size (s55d2 / dimension-entity
                                            :value 3)
                              :size (s55d3 / dimension-entity
                                           :value 2))
                  :place (s55s / space
                               :ARG1-of (s55r2 / right-04
                                               :ARG2 s55t
                                               :ARG3 (s55c / cartesian-framework-91
                                                           :ARG1 s55y))
                               :refer-number plural)
                  :mode imperative))

# alignment:

# document level annotation:

## english_umr-0042, sentence 6

# :: snt6
Index: 1                    2                    3                    4                    5                    6                    7                    8                    9                    10                   11                   12                   13                   14                   15                   16                   17                   18                   19                   20                   21                   22                   23                   24                   25                   26                   
Words: So                   not                  only                 will                 the                  invasion             create               British              jobs,                take                 people               off                  the                  streets,             provide              invaluable           battle-field         experience           and                  be                   self-financing....it could                actually             be                   PROFIT               MAKING!              

# sentence level graph:
(s6c / cause-01
     :ARG1 (s6a / and
                :op1 (s6c2 / create-01
                           :ARG0 (s6i / invade-01)
                           :ARG1 (s6j / job
                                      :mod (s6c3 / country
                                                 :name (s6n / name
                                                            :op1 "Great"
                                                            :op2 "Britain")
                                                 :wiki "United_Kingdom"))
                           :manner (s6o / only
                                        :polarity -))
                :op2 (s6t / take-off-07
                          :ARG1 (s6p / person)
                          :source (s6s / street))
                :op3 (s6p2 / provide-01
                           :ARG1 (s6e / experience
                                      :mod (s6f2 / field
                                                 :place-of (s6b / battle-01))
                                      :ARG1-of (s6v / value-01
                                                    :ARG1-of (s6p5 / possible-01
                                                                   :polarity -))))
                :op4 (s6f / finance-01
                          :ARG0 s6i
                          :ARG1 s6i)
                :op5 (s6p3 / possible-01
                           :ARG1 (s6m / make-01
                                      :ARG1 (s6p4 / profit)
                                      :ARG1-of (s6a2 / actual-02)))))

# alignment:

# document level annotation:

## english_umr-0126, sentence 5

# :: snt5
Index: 1        2        3        4        5        6        7        8        9        10       11       12       
Words: Only     thing    ,        I        havn't   seen     anything nobel    about    the      OWS      ...      

# sentence level graph:
(s5c / contrast-91
     :ARG2 (s5s / see-01
                :ARG0 (s5p2 / person
                            :refer-person 1st
                            :refer-number singular)
                :ARG1 (s5n / noble-01
                           :ARG1 (s5p / political-organization
                                      :name (s5n2 / name
                                                  :op1 "OWS")
                                      :wiki "Occupy_Wall_Street")
                           :aspect state
                           :modal-strength full-affirmative)
                :polarity -
                :aspect state
                :modal-strength full-negative))

# alignment:

# document level annotation:

## english_umr-0193, sentence 82

# :: snt82
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      
Words: How     much    money   could   you     save    if      you     could   get     by      with    only    one     car     instead of      two     ?       

# sentence level graph:
(s82p / possible-01
      :ARG1 (s82s / save-01
                  :ARG0 (s82y / you)
                  :ARG1 (s82a / umr-unknown)
                  :condition (s82p2 / possible-01
                                    :ARG1 (s82g / get-by-17
                                                :ARG0 s82y
                                                :ARG1 (s82c / car
                                                            :mod (s82o / only)
                                                            :ARG1-of (s82h / have-substitute-91
                                                                           :ARG2 (s82c2 / car
                                                                                        :quant 2))
                                                            :quant 1)))))

# alignment:

# document level annotation:

## english_umr-0041, sentence 8

# :: snt8
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         
Words: Also,      what       would      be         the        positives  and        negatives  for        the        general    population if         it         ever       were       to         happen?    

# sentence level graph:
(s8a / and
     :op1 (s8p / positive
               :domain (s8a4 / umr-unknown))
     :op2 (s8n / negative-02
               :ARG0 (s8a2 / umr-unknown))
     :affectee (s8p2 / population
                     :ARG1-of (s8g / general-02))
     :mod (s8a3 / also)
     :condition (s8i / it
                     :temporal (s8e / ever)))

# alignment:

# document level annotation:

## english_umr-0201, sentence 4

# :: snt4
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        
Words: Darwin    proposed  Evolution Theory    ,         but       it        was       just      a         theory    ,         and       he        himself   also      admitted  that      there     were      many      questions ,         

# sentence level graph:
(s4c / contrast-91
     :ARG1 (s4p2 / propose-01
                 :ARG0 (s4p3 / person
                             :name (s4n / name
                                        :op1 "Darwin")
                             :wiki "Charles_Darwin")
                 :ARG1 (s4t4 / theory
                             :topic (s4e / evolve-02)))
     :ARG2 (s4a / and
                :op1 (s4t / theory
                          :mod (s4j / just)
                          :domain s4t4)
                :op2 (s4a2 / admit-01
                           :ARG0 s4p3
                           :ARG1 (s4t3 / thing
                                       :ARG1-of (s4q / question-01)
                                       :quant (s4m / many))
                           :mod (s4a3 / also))))

# alignment:

# document level annotation:

## english_umr-0174, sentence 9

# :: snt9
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          42          43          44          45          46          47          48          49          50          51          52          
Words: After       centuries   of          logging     and         other       human       activities  which       were        devastating the         swamp's     ecosystems, the         Great       Dismal      Swamp       National    Wildlife    Refuge      was         created     in          1973        when        the         Union       Camp        Corporation of          Franklin,   Virginia    donated     49,100      acres       (200        km²)        of          land;       the         refuge      was         officially  established through     The         Dismal      Swamp       Act         of          1974.       

# sentence level graph:
(s9a6 / and
      :op1 (s9c / create-01
                :ARG1 (s9w / wetland
                           :name (s9n2 / name
                                       :op1 "Great"
                                       :op2 "Dismal"
                                       :op3 "Swamp"
                                       :op4 "National"
                                       :op5 "Wildlife"
                                       :op6 "Refuge")
                           :wiki "Great_Dismal_Swamp_National_Wildlife_Refuge")
                :temporal (s9d / date-entity
                               :year 1973)
                :temporal (s9a3 / after
                                :op1 (s9a4 / and
                                           :op1 (s9l / log-03)
                                           :op2 (s9t / thing
                                                     :ARG1-of (s9a5 / activity-06
                                                                    :ARG0 (s9h / human)
                                                                    :mod (s9o / other))
                                                     :ARG0-of (s9d4 / devastate-01
                                                                    :ARG1 (s9e / ecosystem
                                                                               :part-of (s9s2 / swamp))))
                                           :duration (s9m2 / multiple
                                                           :op1 (s9t2 / temporal-quantity
                                                                      :unit (s9c2 / century)
                                                                      :quant 1))))
                :temporal (s9d5 / donate-01
                                :ARG0 (s9c3 / company
                                            :name (s9n3 / name
                                                        :op1 "Union"
                                                        :op2 "Camp"
                                                        :op3 "Corporation")
                                            :place (s9c4 / city
                                                         :name (s9n4 / name
                                                                     :op1 "Franklin")
                                                         :place (s9s / state
                                                                     :name (s9n / name
                                                                                :op1 "Virginia")
                                                                     :wiki "Virginia")
                                                         :wiki "Franklin,_Virginia")
                                            :wiki "Union_Camp_Corporation")
                                :ARG1 (s9l2 / land
                                            :quant (s9a / area-quantity
                                                        :unit (s9a2 / acre)
                                                        :quant 49100))))
      :op2 (s9e2 / establish-01
                 :ARG0 (s9l3 / law
                             :name (s9n5 / name
                                         :op1 "The"
                                         :op2 "Dismal"
                                         :op3 "Swamp"
                                         :op4 "Act")
                             :temporal (s9d3 / date-entity
                                             :year 1974)
                             :wiki -)
                 :ARG1 s9w
                 :manner (s9o2 / official)))

# alignment:

# document level annotation:

## english_umr-0108, sentence 11

# :: snt11
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            
Words: I             picked        it            because       instead       of            using         his           political     capital       at            the           beginning     of            his           presidency    to            adress        jobs,         unemployment, the           budget        defecit,      and           the           national      debt          he            used          up            all           that          capital       getting       Obamacare     passed.       

# sentence level graph:
(s11c / cause-01
      :ARG0 (s11h3 / have-substitute-91
                   :ARG1 (s11u / use-up-04
                               :ARG0 (s11h / he)
                               :ARG1 (s11c2 / capital
                                            :mod (s11p2 / politics)
                                            :possessor s11h)
                               :ARG2 (s11g / get-04
                                           :ARG0 s11h
                                           :ARG1 (s11p3 / pass-01
                                                        :ARG2 (s11l / law
                                                                    :name (s11n2 / name
                                                                                 :op1 "Obamacare")
                                                                    :wiki "Patient_Protection_and_Affordable_Care_Act"))))
                   :ARG2 (s11u2 / use-01
                                :ARG0 s11h
                                :ARG1 s11c2
                                :ARG2 (s11a / address-02
                                            :ARG0 s11h
                                            :ARG1 (s11a2 / and
                                                         :op1 (s11j / job)
                                                         :op2 (s11e / employ-01
                                                                    :polarity -)
                                                         :op3 (s11d / deficit
                                                                    :mod (s11b / budget))
                                                         :op4 (s11d2 / debt
                                                                     :mod (s11n / nation))))
                                :temporal (s11b2 / begin-01
                                                 :ARG1 (s11h2 / have-org-role-92
                                                              :ARG1 s11h
                                                              :ARG3 (s11p4 / president)))))
      :ARG1 (s11p / pick-01
                  :ARG0 (s11i / i)
                  :ARG1 (s11i2 / it)))

# alignment:

# document level annotation:

## english_umr-0194, sentence 5

# :: snt5
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          
Words: Though      close       to          Reagan      National    Airport     and         dense       with        hotels      ,           the         area        has         long        been        seen        as          a           gloomy      1960s       era         enclave     of          offices     connected   by          underground passages    .           

# sentence level graph:
(s5s / see-01
     :ARG1 (s5a2 / area)
     :ARG2 (s5e / enclave
                :consist-of (s5o / office
                                 :ARG1-of (s5c2 / connect-01
                                                :ARG3 (s5p / passage
                                                           :place (s5u / underground))))
                :mod (s5e2 / era
                           :mod (s5d3 / date-entity
                                      :decade 1960))
                :mod (s5g / gloomy))
     :concession (s5a / and
                      :op1 (s5c / close-10
                                :ARG1 s5a2
                                :ARG2 (s5a3 / airport
                                            :name (s5n / name
                                                       :op1 "Reagan"
                                                       :op2 "National"
                                                       :op3 "Airport")
                                            :wiki "Ronald_Reagan_Washington_National_Airport"))
                      :op2 (s5d2 / dense
                                 :prep-with (s5h / hotel)))
     :ARG1-of (s5l / long-03))

# alignment:

# document level annotation:

## english_umr-0193, sentence 75

# :: snt75
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          
Words: Somehow     I           doubt       she         would       have        gotten      on          board       with        fundamental change      if          it          involved    massive     central     and         regional    planning    .           

# sentence level graph:
(s75d / doubt-01
      :ARG0 (s75i / i)
      :ARG1 (s75g / get-05
                  :ARG1 (s75s / she)
                  :ARG2 (s75b / board-01
                              :companion (s75c / change-01
                                                 :mod (s75f / fundamental)))
                  :condition (s75i2 / involve-01
                                    :ARG1 (s75p / plan-01
                                                :mod (s75c2 / central)
                                                :mod (s75r / region)
                                                :mod (s75m / massive))
                                    :ARG2 s75c))
      :mod (s75s2 / somehow))

# alignment:

# document level annotation:

## english_umr-0174, sentence 2

# :: snt2
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           
Words: The          Great        Dismal       Swamp        is           a            marshy       area         on           the          Coastal      Plain        of           southeastern Virginia     and          northeastern North        Carolina     between      Norfolk,     Virginia,    and          Elizabeth    City,        North        Carolina     in           the          United       States.      

# sentence level graph:
(s2a / area
     :mod (s2m / marshy)
     :place (s2p / province
                 :name (s2n4 / name
                             :op1 "Coastal"
                             :op2 "Plain")
                 :place (s2s3 / southeast
                              :part-of (s2s / state
                                            :name (s2n / name
                                                       :op1 "Virginia")
                                            :wiki "Virginia"))
                 :place (s2n5 / northeast
                              :part-of (s2s2 / state
                                             :name (s2n2 / name
                                                         :op1 "North"
                                                         :op2 "Carolina")
                                             :wiki "North_Carolina"))
                 :wiki -)
     :place (s2b / between
                 :op1 (s2c2 / city
                            :name (s2n6 / name
                                        :op1 "Norfolk")
                            :place s2s
                            :wiki "Norfolk,_Virginia")
                 :op2 (s2c3 / city
                            :name (s2n7 / name
                                        :op1 "Elizabeth"
                                        :op2 "City")
                            :place s2s2
                            :wiki "Elizabeth_City,_North_Carolina"))
     :place (s2c / country
                 :name (s2n3 / name
                             :op1 "United"
                             :op2 "States")
                 :wiki "United_States")
     :domain (s2l / local-region
                  :name (s2n8 / name
                              :op1 "Great"
                              :op2 "Dismal"
                              :op3 "Swamp")
                  :wiki "Great_Dismal_Swamp"))

# alignment:

# document level annotation:

## english_umr-0193, sentence 43

# :: snt43
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          
Words: Rather      than        drilling    for         oil         and         gas         off         the         Atlantic    Coast       ,           we          should      be          offering    enormous    incentives  for         comapnies   and         individuals who         want        to          work        on          alternative fuel        solutions   to          locate      their       business    here        .           

# sentence level graph:
(s43r / recommend-01
      :ARG1 (s43o / offer-01
                  :ARG0 (s43w / we)
                  :ARG1 (s43t / thing
                              :ARG0-of (s43i / incentivize-01
                                             :ARG1 (s43a2 / and
                                                          :op1 (s43c / company)
                                                          :op2 (s43i2 / individual)
                                                          :ARG0-of (s43w2 / want-01
                                                                          :ARG1 (s43w3 / work-01
                                                                                       :ARG0 s43a2
                                                                                       :ARG1 (s43t2 / thing
                                                                                                    :ARG0-of (s43s / solve-01)
                                                                                                    :mod (s43f / fuel
                                                                                                               :mod (s43a3 / alternative)))))))
                              :mod (s43e / enormous))
                  :ARG3 s43a2
                  :purpose (s43l2 / locate-01
                                  :ARG0 s43a2
                                  :ARG1 (s43b / business
                                              :possessor s43a2)
                                  :place (s43h / here)))
      :ARG1-of (s43h2 / have-substitute-91
                      :ARG2 (s43d / drill-01
                                  :ARG3 (s43a4 / and
                                               :op1 (s43o2 / oil)
                                               :op2 (s43g / gas))
                                  :place (s43o3 / off
                                                :op1 (s43c2 / country-region
                                                            :name (s43n / name
                                                                        :op1 "Atlantic"
                                                                        :op2 "Coast")
                                                            :wiki "East_Coast_of_the_United_States")))))

# alignment:

# document level annotation:

## english_umr-0364, sentence 36

# :: snt36
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          
Words: <Architect> There       will        be          two         other       shapes      like        this,       but         they        will        be          floating    

# sentence level graph:
(s36c / contrast-91
      :ARG1 (s36t / thing
                  :ARG1-of (s36s / shape-01)
                  :ARG1-of (s36r / resemble-91
                                 :ARG2 (s36t2 / this))
                  :quant 2)
      :ARG2 (s36f / float-01
                  :ARG1 s36t))

# alignment:

# document level annotation:

## english_umr-0196, sentence 185

# :: snt185
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            46            47            48            49            50            51            52            53            54            55            56            
Words: Likewise      ,             in            its           2006          annual        refugee       report        to            Congress      ,             the           State         Department    focused       mainly        on            those         Saddam        -             era           exiles        ,             and           blithely      intoned       ,             ``            It            is            hoped         that          significant   numbers       of            Iraqi         refugees      will          soon          be            able          to            return        home          ,             although      the           security      situation     will          remain        an            important     consideration .             ''            

# sentence level graph:
(s185a / and
       :op1 (s185f / focus-01
                   :ARG0 (s185g2 / government-organization
                                 :name (s185n / name
                                              :op1 "State"
                                              :op2 "Department")
                                 :wiki "United_States_Department_of_State")
                   :ARG2 (s185p2 / person
                                 :ARG1-of (s185e / exile-01
                                                 :temporal (s185e2 / era
                                                                   :mod (s185p3 / person
                                                                                :name (s185n2 / name
                                                                                              :op1 "Saddam")
                                                                                :wiki "Saddam_Hussein"))))
                   :medium (s185r / report-01
                                  :ARG0 s185g2
                                  :ARG2 (s185g3 / government-organization
                                                :name (s185n3 / name
                                                              :op1 "Congress")
                                                :wiki "United_States_Congress")
                                  :topic (s185r2 / refugee)
                                  :temporal (s185d2 / date-entity
                                                    :year 2006)
                                  :frequency (s185r6 / rate-entity-91
                                                     :ARG3 (s185t / temporal-quantity
                                                                  :unit (s185y / year)
                                                                  :quant 1)))
                   :mod (s185m / main))
       :op2 (s185i2 / intone-01
                    :ARG0 s185g2
                    :ARG1 (s185h / hopeful-03
                                 :ARG1 (s185p4 / possible-01
                                               :ARG1 (s185r3 / return-01
                                                             :ARG1 (s185n4 / number
                                                                           :ARG1-of (s185s / significant-02)
                                                                           :quant-of (s185r4 / refugee
                                                                                             :mod (s185c3 / country
                                                                                                          :name (s185n5 / name
                                                                                                                        :op1 "Iraq")
                                                                                                          :wiki "Iraq")))
                                                             :ARG4 (s185h2 / home))
                                               :temporal (s185s4 / soon)
                                               :concession (s185r5 / remain-01
                                                                   :ARG1 (s185s5 / situation
                                                                                 :mod (s185s6 / security))
                                                                   :ARG3 (s185c4 / consider-02
                                                                                 :ARG1 s185s5
                                                                                 :ARG1-of (s185i / important-01)))))
                    :manner (s185b / blithe))
       :mod (s185l / likewise))

# alignment:

# document level annotation:

## english_umr-0150, sentence 10

# :: snt10
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          
Words: Decisions   of          the         most        horrific    choices     are         caused      by          tyrannical  governments and         leaders     that        force       men         and         women       of          good        will        to          make        such        choices.    

# sentence level graph:
(s10c / cause-01
      :ARG0 (s10a / and
                  :op1 (s10g / government-organization
                             :ARG0-of (s10g2 / govern-01)
                             :mod (s10t / tyrannical))
                  :op2 (s10p / person
                             :ARG0-of (s10l / lead-01)
                             :mod s10t)
                  :ARG0-of (s10f / force-01
                                 :ARG1 (s10a2 / and
                                              :op1 (s10m / man)
                                              :op2 (s10w / woman)
                                              :ARG0-of (s10h / have-03
                                                             :ARG1 (s10w2 / will-02
                                                                          :ARG1-of (s10g3 / good-02))))
                                 :ARG2 (s10c2 / choose-01
                                              :ARG0 s10a2
                                              :mod (s10s / such))))
      :ARG1 (s10t2 / thing
                   :ARG1-of (s10d / decide-01
                                  :ARG3 (s10t3 / thing
                                               :ARG1-of (s10c3 / choose-01)
                                               :ARG1-of (s10h3 / have-degree-91
                                                               :ARG2 (s10h2 / horrific)
                                                               :ARG3 (s10m2 / most))))))

# alignment:

# document level annotation:

## english_umr-0020, sentence 20

# :: snt20
Index: 1              2              3              4              5              6              7              8              9              10             11             12             13             14             15             16             17             18             19             20             21             22             23             24             25             26             27             28             29             30             31             32             33             34             
Words: If             elections      were           held           their,         or             if             there          was            a              struggle       for            power,         the            regime         that           woudl          arise          would          be             friendly       with           Iran           and            extremely      antagonistic   to             the            U.S.:          quite          understandably I              might          add.           

# sentence level graph:
(s20a6 / and
       :op1 (s20a2 / and
                   :op1 (s20f / friendly-01
                              :ARG1 (s20r / regime
                                          :ARG1-of (s20a3 / arise-02))
                              :ARG2 (s20c / country
                                          :name (s20n / name
                                                      :op1 "Iran")
                                          :wiki "Iran"))
                   :op2 (s20a5 / antagonize-01
                               :ARG0 s20r
                               :ARG1 (s20c2 / country
                                            :name (s20n2 / name
                                                         :op1 "U.S.")
                                            :wiki "United_States")
                               :degree (s20e2 / extreme))
                   :condition (s20o / or
                                    :op1 (s20h / hold-04
                                               :ARG1 (s20e / elect-01)
                                               :place (s20t / there))
                                    :op2 (s20s / struggle-01
                                               :ARG2 (s20p / power))))
       :op2 (s20p2 / possible-01
                   :ARG1 (s20a4 / add-01
                                :ARG0 (s20i / i)
                                :ARG1 (s20u / understand-01
                                            :ARG1 s20a2
                                            :ARG1-of (s20p3 / possible-01
                                                            :degree (s20q / quite))))))

# alignment:

# document level annotation:

## english_umr-0057, sentence 20

# :: snt20
Index: 1              2              3              4              5              6              7              8              9              10             11             12             13             14             15             16             17             18             19             20             21             22             23             24             25             26             27             28             29             30             31             32             33             34             
Words: If             elections      were           held           their,         or             if             there          was            a              struggle       for            power,         the            regime         that           woudl          arise          would          be             friendly       with           Iran           and            extremely      antagonistic   to             the            U.S.:          quite          understandably I              might          add.           

# sentence level graph:
(s20a6 / and
       :op1 (s20a2 / and
                   :op1 (s20f / friendly-01
                              :ARG1 (s20r / regime
                                          :ARG1-of (s20a3 / arise-02))
                              :ARG2 (s20c / country
                                          :name (s20n / name
                                                      :op1 "Iran")
                                          :wiki "Iran"))
                   :op2 (s20a5 / antagonize-01
                               :ARG0 s20r
                               :ARG1 (s20c2 / country
                                            :name (s20n2 / name
                                                         :op1 "U.S.")
                                            :wiki "United_States")
                               :degree (s20e2 / extreme))
                   :condition (s20o / or
                                    :op1 (s20h / hold-04
                                               :ARG1 (s20e / elect-01)
                                               :place (s20t / there))
                                    :op2 (s20s / struggle-01
                                               :ARG2 (s20p / power))))
       :op2 (s20p2 / possible-01
                   :ARG1 (s20a4 / add-01
                                :ARG0 (s20i / i)
                                :ARG1 (s20u / understand-01
                                            :ARG1 s20a2
                                            :ARG1-of (s20p3 / possible-01
                                                            :degree (s20q / quite))))))

# alignment:

# document level annotation:

## english_umr-0196, sentence 181

# :: snt181
Index: 1         2         3         4         5         6         7         8         
Words: there     were      thousands with      the       same      story     .         

# sentence level graph:
(s181h / have-03
       :ARG0 (s181p / person
                    :quant (s181m / multiple
                                  :op1 1000))
       :ARG1 (s181s / story
                    :ARG1-of (s181s2 / same-01)))

# alignment:

# document level annotation:

## english_umr-0221, sentence 1282

# :: snt1282
Index: 1       2       3       4       5       6       7       8       9       10      
Words: This    one     was     like    a       well    in      a       village .       

# sentence level graph:
(s1282r / resemble-91
        :ARG1 (s1282w / well
                      :mod (s1282t / this))
        :ARG2 (s1282w2 / well
                       :place (s1282v / village)))

# alignment:

# document level annotation:

## english_umr-0217, sentence 1141

# :: snt1141
Index: 1        2        3        4        5        6        7        8        9        
Words: Every    Thursday they     dance    with     the      village  girls    .        

# sentence level graph:
(s1141d / dance-01
        :ARG0 (s1141t / they)
        :ARG2 (s1141g / girl
                      :source (s1141v / village))
        :frequency (s1141r / rate-entity-91
                           :ARG4 (s1141d2 / date-entity
                                          :weekday (s1141t2 / thursday))))

# alignment:

# document level annotation:

## english_umr-0221, sentence 1283

# :: snt1283
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       
Words: But      there    was      no       village  here     ,        and      I        thought  I        must     be       dreaming ...      

# sentence level graph:
(s1283c3 / contrast-91
         :ARG2 (s1283a / and
                       :op1 (s1283v / village
                                    :place (s1283h / here)
                                    :polarity -)
                       :op2 (s1283t / think-01
                                    :ARG0 (s1283i / i)
                                    :ARG1 (s1283d / dream-01
                                                  :ARG0 s1283i))))

# alignment:

# document level annotation:

## english_umr-0208, sentence 713

# :: snt713
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22      
Words: "       This    man     ,       "       the     little  prince  said    to      himself ,       "       reasons a       little  like    my      poor    tippler ...     "       

# sentence level graph:
(s713s / say-01
       :ARG0 (s713p / prince
                    :mod (s713l / little))
       :ARG1 (s713r / reason-01
                    :ARG0 (s713m / man
                                 :mod (s713t2 / this))
                    :ARG1-of (s713r2 / resemble-91
                                     :ARG2 (s713r3 / reason-01
                                                   :ARG0 (s713p2 / person
                                                                 :ARG0-of (s713t / tipple-01)
                                                                 :mod (s713p3 / poor)
                                                                 :possessor s713p))
                                     :degree downtoner)
                    :quote s713s)
       :ARG2 s713p)

# alignment:

# document level annotation:

## english_umr-0221, sentence 1325

# :: snt1325
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       26       
Words: The      little   prince   looked   them     over     ,        and      laughed  as       he       said     :        "        Your     baobabs  -        -        they     look     a        little   like     cabbages .        "        

# sentence level graph:
(s1325a / and
        :op1 (s1325l / look-01
                     :ARG0 (s1325p / prince
                                   :mod (s1325l2 / little))
                     :ARG1 (s1325t / they))
        :op2 (s1325l3 / laugh-01
                      :ARG0 s1325p
                      :temporal (s1325s / say-01
                                        :ARG0 s1325p
                                        :ARG1 (s1325l4 / look-02
                                                       :ARG0 (s1325b / baobab
                                                                     :possessor (s1325y / you))
                                                       :ARG1 (s1325c / cabbage)
                                                       :quote s1325s
                                                       :degree downtoner))))

# alignment:

# document level annotation:

## english_umr-0220, sentence 1272

# :: snt1272
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         40         41         42         43         44         45         46         47         48         49         50         51         52         53         54         55         56         57         58         59         60         61         62         63         64         65         66         67         68         69         70         
Words: As         his        lips       opened     slightly   with       the        suspicious of         a          half       -          smile      ,          I          said       to         myself     ,          again      :          "          What       moves      me         so         deeply     ,          about      this       little     prince     who        is         sleeping   here       ,          is         his        loyalty    to         a          flower     -          -          the        image      of         a          rose       that       shines     through    his        whole      being      like       the        flame      of         a          lamp       ,          even       when       he         is         asleep     ...        "          

# sentence level graph:
(s1272s / say-01
        :ARG0 (s1272i / i)
        :ARG1 (s1272m / move-05
                      :ARG0 (s1272p / prince
                                    :mod (s1272l / little)
                                    :ARG0-of (s1272s2 / sleep-01
                                                      :place (s1272h / here))
                                    :part (s1272l4 / lip))
                      :ARG1 s1272i
                      :ARG2 (s1272l2 / loyal-01
                                     :ARG1 s1272p
                                     :ARG2 (s1272f / flower
                                                   :op1 (s1272i2 / image
                                                                 :possessor (s1272r / rose
                                                                                    :ARG1-of (s1272s3 / shine-01
                                                                                                      :ARG2 (s1272t / through
                                                                                                                    :op1 (s1272b / being
                                                                                                                                 :possessor s1272p
                                                                                                                                 :mod (s1272w / whole)))
                                                                                                      :ARG1-of (s1272r2 / resemble-91
                                                                                                                        :ARG2 (s1272f2 / flame-01
                                                                                                                                       :ARG1 (s1272l3 / lamp)))
                                                                                                      :concession (s1272e / even-when
                                                                                                                          :op1 (s1272s6 / sleep-01
                                                                                                                                        :ARG0 s1272p)))))))
                      :ARG1-of (s1272d / deep-02)
                      :quote s1272s)
        :ARG2 s1272i
        :temporal (s1272o / open-01
                          :ARG1 s1272l4
                          :manner (s1272s8 / smile-01
                                           :extent (s1272h3 / half)
                                           :manner (s1272s5 / suspicion))
                          :degree downtoner)
        :mod (s1272a2 / again))

# alignment:

# document level annotation:

## english_umr-0020, sentence 22

# :: snt22
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        31        32        33        34        35        36        37        38        39        40        41        42        43        44        45        46        47        48        49        50        51        52        53        54        55        56        57        58        59        
Words: And       so,       after     all       that,     which     you       might     justly    consider  paranoia, my        question  is        basically this;     in        light     of        the       threat    of        peak      oil,      and       of        the       general   decline   in        American  economic  might     relative  the       rest      of        the       world     (not      to        mention   the       current   U.S.      crisis),  what      do        think     the       world     will      look      like      in        a         decade    or        two?      

# sentence level graph:
(s22a / and
      :op2 (s22q / question-01
                 :ARG0 (s22i / i)
                 :ARG1 (s22t6 / thing
                              :ARG1-of (s22l / look-02
                                             :ARG0 (s22w / world)
                                             :temporal (s22a7 / after
                                                              :op1 (s22n / now)
                                                              :quant (s22b / between
                                                                           :op1 (s22t / temporal-quantity
                                                                                      :unit (s22d / decade)
                                                                                      :quant 1)
                                                                           :op2 (s22t3 / temporal-quantity
                                                                                       :unit (s22d2 / decade)
                                                                                       :quant 2)))
                                             :ARG1-of (s22t2 / think-01
                                                             :ARG0 (s22y / you))))
                 :ARG1-of (s22c / cause-01
                                :ARG0 (s22a3 / and
                                             :op1 (s22t4 / threaten-01
                                                         :ARG1 (s22p / peak-01
                                                                     :ARG1 (s22o2 / oil)))
                                             :op2 (s22d3 / decline-01
                                                         :ARG1 (s22m / might
                                                                     :possessor (s22e / economy
                                                                                      :possessor (s22c4 / country
                                                                                                        :name (s22n2 / name
                                                                                                                     :op1 "United"
                                                                                                                     :op2 "States")
                                                                                                        :wiki "United_States")))
                                                         :ARG1-of (s22g / general-02)
                                                         :ARG2-of (s22r2 / relative-05
                                                                         :ARG3 (s22a6 / and
                                                                                      :op1 (s22r / rest
                                                                                                 :part-of (s22w2 / world))
                                                                                      :op2 (s22c2 / crisis
                                                                                                  :temporal (s22c5 / current)
                                                                                                  :possessor s22c4))))))
                 :temporal (s22a4 / after
                                  :op1 (s22t5 / that
                                              :mod (s22a5 / all)
                                              :ARG2-of (s22h2 / have-role-91
                                                              :ARG1 (s22p3 / paranoia)
                                                              :ARG1-of (s22c3 / consider-01
                                                                              :ARG0 s22y
                                                                              :ARG1-of (s22p2 / possible-01)
                                                                              :ARG1-of (s22j / just-02))))))
      :mod (s22s / so))

# alignment:

# document level annotation:

## english_umr-0057, sentence 22

# :: snt22
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        31        32        33        34        35        36        37        38        39        40        41        42        43        44        45        46        47        48        49        50        51        52        53        54        55        56        57        58        59        
Words: And       so,       after     all       that,     which     you       might     justly    consider  paranoia, my        question  is        basically this;     in        light     of        the       threat    of        peak      oil,      and       of        the       general   decline   in        American  economic  might     relative  the       rest      of        the       world     (not      to        mention   the       current   U.S.      crisis),  what      do        think     the       world     will      look      like      in        a         decade    or        two?      

# sentence level graph:
(s22a / and
      :op2 (s22q / question-01
                 :ARG0 (s22i / i)
                 :ARG1 (s22t6 / thing
                              :ARG1-of (s22l / look-02
                                             :ARG0 (s22w / world)
                                             :temporal (s22a7 / after
                                                              :op1 (s22n / now)
                                                              :quant (s22b / between
                                                                           :op1 (s22t / temporal-quantity
                                                                                      :unit (s22d / decade)
                                                                                      :quant 1)
                                                                           :op2 (s22t3 / temporal-quantity
                                                                                       :unit (s22d2 / decade)
                                                                                       :quant 2)))
                                             :ARG1-of (s22t2 / think-01
                                                             :ARG0 (s22y / you))))
                 :ARG1-of (s22c / cause-01
                                :ARG0 (s22a3 / and
                                             :op1 (s22t4 / threaten-01
                                                         :ARG1 (s22p / peak-01
                                                                     :ARG1 (s22o2 / oil)))
                                             :op2 (s22d3 / decline-01
                                                         :ARG1 (s22m / might
                                                                     :possessor (s22e / economy
                                                                                      :possessor (s22c4 / country
                                                                                                        :name (s22n2 / name
                                                                                                                     :op1 "United"
                                                                                                                     :op2 "States")
                                                                                                        :wiki "United_States")))
                                                         :ARG1-of (s22g / general-02)
                                                         :ARG2-of (s22r2 / relative-05
                                                                         :ARG3 (s22a6 / and
                                                                                      :op1 (s22r / rest
                                                                                                 :part-of (s22w2 / world))
                                                                                      :op2 (s22c2 / crisis
                                                                                                  :temporal (s22c5 / current)
                                                                                                  :possessor s22c4))))))
                 :temporal (s22a4 / after
                                  :op1 (s22t5 / that
                                              :mod (s22a5 / all)
                                              :ARG2-of (s22h2 / have-role-91
                                                              :ARG1 (s22p3 / paranoia)
                                                              :ARG1-of (s22c3 / consider-01
                                                                              :ARG0 s22y
                                                                              :ARG1-of (s22p2 / possible-01)
                                                                              :ARG1-of (s22j / just-02))))))
      :mod (s22s / so))

# alignment:

# document level annotation:

## english_umr-0216, sentence 1025

# :: snt1025
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       26       27       28       29       
Words: But      it       happened that     after    walking  for      a        long     time     through  sand     ,        and      rocks    ,        and      snow     ,        the      little   prince   at       last     came     upon     a        road     .        

# sentence level graph:
(s1025c / contrast-91
        :ARG2 (s1025c2 / come-upon-26
                       :ARG0 (s1025p / prince
                                     :mod (s1025l / little))
                       :ARG1 (s1025r / road)
                       :temporal (s1025a / after
                                         :op1 (s1025w / walk-01
                                                      :ARG0 s1025p
                                                      :path (s1025a2 / and
                                                                     :op1 (s1025s / sand)
                                                                     :op2 (s1025r2 / rock)
                                                                     :op3 (s1025t / thing
                                                                                  :ARG1-of (s1025s2 / snow-01)))
                                                      :ARG1-of (s1025l3 / long-03)))
                       :temporal (s1025a3 / at-last)))

# alignment:

# document level annotation:

## english_umr-0197, sentence 4

# :: snt4
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          42          43          44          45          46          47          48          49          50          51          52          53          54          55          56          57          58          59          60          61          62          63          64          65          66          67          68          69          70          71          72          73          
Words: At          that        time        ,           DONEWS      did         not         have        the         function    of          tallying    traffic     statistics  (           I           have        the         habit       of          looking     at          the         statistics  of          everything  )           ;           and         even        though      MSN         had         that        function    ,           others      needed      to          sign        on          to          MSN         before      they        could       reply       ,           this        meant       that        after       reading     the         entries     ,           many        could       not         reply       even        if          they        wanted      to          ,           hence       largely     reducing    the         interactive element     .           

# sentence level graph:
(s4a2 / and
      :op1 (s4a4 / and
                 :op1 (s4f / function-01
                           :ARG0 (s4p3 / product
                                       :name (s4n / name
                                                  :op1 "DONEWS")
                                       :wiki "DoNews")
                           :ARG1 (s4t / tally-01
                                      :ARG0 s4p3
                                      :ARG1 (s4s / statistic
                                                 :mod (s4t2 / traffic)))
                           :temporal (s4t3 / time
                                           :mod (s4t4 / that))
                           :polarity -)
                 :op2 (s4h / have-03
                           :ARG0 (s4i3 / i)
                           :ARG1 (s4h2 / habit
                                       :mod (s4l / look-01
                                                 :ARG0 s4i3
                                                 :ARG1 (s4s2 / statistic
                                                             :topic (s4e / everything))))))
      :op2 (s4n3 / need-01
                 :ARG0 (s4o3 / other)
                 :ARG1 (s4s3 / sign-on-04
                             :ARG0 s4o3
                             :ARG1 (s4p4 / product
                                         :name (s4n2 / name
                                                     :op1 "MSN")
                                         :wiki "MSN")
                             :temporal (s4b / before
                                            :op1 (s4p / possible-01
                                                      :ARG1 (s4r / reply-01
                                                                 :ARG0 s4o3))))
                 :concession (s4f2 / function-01
                                   :ARG0 s4p4
                                   :ARG1 s4t)
                 :ARG1-of (s4m / mean-01
                               :ARG2 (s4p2 / possible-01
                                           :ARG1 (s4r2 / reply-01
                                                       :ARG0 (s4m2 / many))
                                           :temporal (s4a3 / after
                                                           :op1 (s4r3 / read-01
                                                                      :ARG0 s4o3
                                                                      :ARG1 (s4e2 / entry)))
                                           :concession (s4e4 / even-if
                                                             :op1 (s4w / want-01
                                                                       :ARG0 s4m2
                                                                       :ARG1 s4r2))
                                           :polarity -))
                 :ARG0-of (s4r4 / reduce-01
                                :ARG1 (s4e3 / element
                                            :mod (s4i / interactive))
                                :ARG2 (s4l2 / large))))

# alignment:

# document level annotation:

## english_umr-0038, sentence 47

# :: snt47
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           
Words: This         comes        the          same         week         that         reports      (costing     the          taxpayer     millions)    are          finally      published,   having       been         commissioned by           Labour,      but          never        released     due          to           their        findings     which        basically    concluded    that         Labour       made         the          worst        mistakes     imaginable   on           immigration. 

# sentence level graph:
(s47c / come-01
      :ARG1 (s47t / this)
      :temporal (s47w / week
                      :ARG1-of (s47s / same-01)
                      :temporal-of (s47p / publish-01
                                         :ARG1 (s47r / report-01
                                                     :ARG1-of (s47c2 / cost-01
                                                                     :ARG2 (s47p2 / person
                                                                                  :ARG0-of (s47p3 / pay-01
                                                                                                  :ARG3 (s47t2 / tax)))
                                                                     :ARG3 (s47m2 / multiple
                                                                                  :op1 (s47m / monetary-quantity
                                                                                             :unit (s47d / dollar)
                                                                                             :quant 1000000)))
                                                     :ARG1-of (s47c3 / commission-01
                                                                     :ARG0 (s47p4 / political-organization
                                                                                  :name (s47n / name
                                                                                              :op1 "Labour")
                                                                                  :wiki "Labour_Party_(UK)")
                                                                     :ARG1-of (s47c4 / contrast-91
                                                                                     :ARG2 (s47r2 / release-01
                                                                                                  :ARG1 s47r
                                                                                                  :temporal (s47e / ever)
                                                                                                  :ARG1-of (s47c5 / cause-01
                                                                                                                  :ARG0 (s47t3 / thing
                                                                                                                               :ARG1-of (s47f2 / find-01
                                                                                                                                               :ARG0 s47r)
                                                                                                                               :ARG0-of (s47c6 / conclude-01
                                                                                                                                               :ARG1 (s47m3 / mistake-02
                                                                                                                                                            :ARG0 s47p4
                                                                                                                                                            :ARG1 (s47i / immigrate-01)
                                                                                                                                                            :ARG1-of (s47i2 / imagine-01
                                                                                                                                                                            :ARG1-of (s47p5 / possible-01))
                                                                                                                                                            :ARG1-of (s47h / have-degree-91
                                                                                                                                                                           :ARG2 (s47b / bad-05
                                                                                                                                                                                       :ARG1 s47m3)
                                                                                                                                                                           :ARG3 (s47m4 / most)))
                                                                                                                                               :mod (s47b2 / basic))))
                                                                                                  :polarity -))))
                                         :mod (s47f / final))))

# alignment:

# document level annotation:

## english_umr-0200, sentence 10

# :: snt10
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            
Words: Carr          also          said          that          the           police        had           applied       for           a             search        warrant       from          the           court         yesterday     morning       ,             and           entered       the           unit          in            the           afternoon     with          the           warrant       for           a             detailed      investigation ,             in            order         to            understand    more          about         the           incident      .             

# sentence level graph:
(s10s / say-01
      :ARG0 (s10p2 / person
                   :name (s10n / name
                               :op1 "Carr")
                   :wiki -)
      :ARG1 (s10a3 / and
                   :op1 (s10a / apply-01
                              :ARG0 (s10p3 / police)
                              :ARG1 (s10w / warrant
                                          :mod (s10s2 / search-01))
                              :ARG2 (s10c2 / court)
                              :temporal (s10d / date-entity
                                              :dayperiod (s10m / morning)
                                              :mod (s10y / yesterday)))
                   :op2 (s10e / enter-01
                              :ARG0 s10p3
                              :ARG1 (s10u / unit)
                              :temporal (s10d2 / date-entity
                                               :dayperiod (s10a4 / afternoon))
                              :purpose (s10u2 / understand-01
                                              :ARG0 s10p3
                                              :ARG1 (s10m2 / more)
                                              :ARG2 (s10i / incident))
                              :manner (s10w2 / warrant
                                             :purpose (s10i2 / investigate-01
                                                             :ARG0 s10p3
                                                             :manner (s10d3 / detail)))))
      :mod (s10a6 / also))

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

## english_umr-0225, sentence 149

# :: snt149
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        31        32        33        34        35        36        37        38        39        40        41        42        43        44        45        46        47        48        49        50        51        52        53        54        55        
Words: I         knew      very      well      that      in        addition  to        the       great     planets   --        such      as        the       Earth     ,         Jupiter   ,         Mars      ,         Venus     --        to        which     we        have      given     names     ,         there     are       also      hundreds  of        others    ,         some      of        which     are       so        small     that      one       has       a         hard      time      seeing    them      through   the       telescope .         

# sentence level graph:
(s149k / know-01
       :ARG0 (s149p8 / person
                     :refer-person 1st
                     :refer-number singular)
       :ARG1 (s149e / exist-91
                    :ARG1 (s149t2 / there)
                    :ARG2 (s149a2 / and
                                  :op1 (s149p / planet
                                              :ARG1-of (s149g / great-01)
                                              :example (s149p2 / planet
                                                               :name (s149n / name
                                                                            :op1 "Earth")
                                                               :wiki "Earth")
                                              :example (s149p3 / planet
                                                               :name (s149n2 / name
                                                                             :op1 "Jupiter")
                                                               :wiki "Jupiter")
                                              :example (s149p4 / planet
                                                               :name (s149n3 / name
                                                                             :op1 "Mars")
                                                               :wiki "Mars")
                                              :example (s149p5 / planet
                                                               :name (s149n4 / name
                                                                             :op1 "Venus")
                                                               :wiki "Venus")
                                              :ARG1-of (s149n5 / name-01
                                                               :ARG0 (s149p9 / person
                                                                             :refer-person 1st
                                                                             :refer-number plural)
                                                               :aspect performance
                                                               :modal-strength full-affirmative)
                                              :refer-number plural)
                                  :op2 (s149p7 / planet
                                               :quant (s149m / multiple
                                                             :op1 100)
                                               :ARG1-of (s149o / other-01)
                                               :ARG2-of (s149i2 / include-91
                                                                :ARG1 (s149p6 / planet
                                                                              :quant (s149s / some)
                                                                              :ARG1-of (s149h / have-degree-91
                                                                                              :ARG2 (s149s2 / small)
                                                                                              :ARG3 (s149s3 / so)
                                                                                              :ARG6 (s149h3 / have-a-time-04
                                                                                                            :ARG1 (s149p10 / person
                                                                                                                           :refer-person 3rd
                                                                                                                           :refer-number singular)
                                                                                                            :ARG4 (s149h2 / hard-01
                                                                                                                          :ARG1 (s149s4 / see-01
                                                                                                                                        :ARG0 s149p10
                                                                                                                                        :ARG1 s149p6
                                                                                                                                        :instrument (s149t / telescope)
                                                                                                                                        :aspect activity
                                                                                                                                        :modal-strength full-affirmative))
                                                                               
… (559 more characters)

## english_umr-0174, sentence 16

# :: snt16
Index: 1                2                3                4                5                6                7                8                9                10               11               12               13               14               15               16               17               18               19               20               21               22               23               24               25               26               27               
Words: Scientists       believe[citation needed]          the              lake             could            have             been             created          by               the              impact           of               a                meteoroid        because          it               is               oval             shaped,          looking          like             the              impact           of               a                meteoroid.       

# sentence level graph:
(s16b / believe-01
      :ARG0 (s16s / scientist)
      :ARG1 (s16p2 / possible-01
                   :ARG1 (s16c / create-01
                               :ARG0 (s16i / impact-02
                                           :ARG2 (s16m / meteoroid))
                               :ARG1 (s16l / lake)))
      :ARG1-of (s16c2 / cause-01
                      :ARG0 (s16s2 / shape
                                   :mod (s16o / oval)
                                   :possessor s16l
                                   :ARG1-of (s16r / resemble-91
                                                  :ARG2 s16i)))
      :ARG0-of (s16n / need-01
                     :ARG1 (s16t / thing
                                 :ARG1-of (s16c3 / cite-01))))

# alignment:

# document level annotation:

## english_umr-0201, sentence 10

# :: snt10
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         
Words: Therefore  ,          Jesus      is         more       vulnerable to         criticism  than       Darwin     ,          because    once       an         error      is         found      ,          then       he         could      not        be         the        true       god        .          

# sentence level graph:
(s10h2 / have-reason-91
       :ARG1 (s10h / have-degree-91
                   :ARG1 (s10p4 / person
                                :name (s10n / name
                                            :op1 "Jesus")
                                :wiki "Jesus")
                   :ARG2 (s10v / vulnerable-01
                               :ARG1 s10p4
                               :ARG2 (s10c / criticize-01))
                   :ARG3 (s10m / more)
                   :ARG4 (s10p5 / person
                                :name (s10n2 / name
                                             :op1 "Darwin")
                                :wiki "Charles_Darwin")
                   :ARG1-of (s10c2 / cause-01
                                   :ARG0 (s10p6 / possible-01
                                                :ARG1 (s10g / god
                                                            :domain s10p4
                                                            :ARG1-of (s10t / true-01))
                                                :temporal (s10f / find-01
                                                                :ARG1 (s10e / error))
                                                :polarity -))))

# alignment:

# document level annotation:

## english_umr-0109, sentence 1

# :: snt1
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           
Words: If           Obama        had          been         even         more         antipathetic to           Republicans  than         he           already      was,         the          backlash     from         the          people       would        have         been         even         stronger     than         the          profound     levels       it           reached      in           2010.        

# sentence level graph:
(s1h / have-condition-91
     :ARG1 (s1h3 / have-degree-91
                 :ARG1 (s1b / backlash-01
                            :ARG0 (s1p3 / person))
                 :ARG2 (s1s3 / strong-02
                             :ARG1 s1b)
                 :ARG3 (s1m2 / more
                             :mod (s1e2 / even))
                 :ARG4 (s1l / level
                            :mod (s1p4 / profound)
                            :degree-of (s1s4 / strong-02)
                            :ARG1-of (s1r / reach-01
                                          :ARG0 s1b
                                          :temporal (s1d / date-entity
                                                         :year 2010))))
     :ARG2 (s1h2 / have-degree-91
                 :ARG1 (s1p / person
                            :name (s1n / name
                                       :op1 "Obama")
                            :wiki "Barack_Obama")
                 :ARG2 (s1s / sympathize-01
                            :ARG0 s1p
                            :ARG1 (s1p2 / political-organization
                                        :name (s1n2 / name
                                                    :op1 "Republican")
                                        :wiki "Republican_Party_(United_States)")
                            :polarity -)
                 :ARG3 (s1m / more
                            :mod (s1e / even))
                 :ARG4 (s1s2 / sympathize-01
                             :ARG0 s1p
                             :ARG1 s1p2
                             :temporal (s1a / already)
                             :polarity -)))

# alignment:

# document level annotation:

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

## english_umr-0038, sentence 18

# :: snt18
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        
Words: It's      been      almost    17        months    since     the       coalition has       been      in        now,      not       15        months    as        one       of        you       said,     or        just      6         months    as        another   one       of        you       said      

# sentence level graph:
(s18h / have-duration-91
      :ARG2 (s18a / almost
                  :op1 (s18t / temporal-quantity
                             :unit (s18m / month)
                             :quant 17))
      :temporal (s18s / since
                      :op1 (s18c / coalition))
      :temporal (s18n / now)
      :ARG1-of (s18c2 / contrast-91
                      :ARG2 (s18o / or
                                  :op1 (s18t2 / temporal-quantity
                                              :unit (s18m2 / month)
                                              :ARG1-of (s18s2 / say-01
                                                              :ARG0 (s18o2 / one
                                                                           :ARG1-of (s18i / include-91
                                                                                          :ARG2 (s18y / you))))
                                              :quant 15
                                              :polarity -)
                                  :op2 (s18t3 / temporal-quantity
                                              :unit (s18m3 / month)
                                              :mod (s18j / just)
                                              :ARG1-of (s18s3 / say-01
                                                              :ARG0 (s18o3 / one
                                                                           :mod (s18a2 / another)
                                                                           :ARG1-of s18i))
                                              :quant 6))))

# alignment:

# document level annotation:

## english_umr-0148, sentence 16

# :: snt16
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           39           40           
Words: And          yet          you          IGNORE       the          fact         that         until        the          second       Atomic       Bomb         was          dropped      the          Japanese     had          NO           INTENTION    of           surrendering and          even         after        the          second       attack       it           took         direct       intervention from         the          Emperor      to           force        the          Army         to           surrender.   

# sentence level graph:
(s16i / ignore-01
      :ARG0 (s16y / you)
      :ARG1 (s16a2 / and
                   :op1 (s16i2 / intend-01
                               :ARG0 (s16c / country
                                           :name (s16n2 / name
                                                        :op1 "Japan")
                                           :wiki "Japan")
                               :ARG1 (s16s / surrender-01
                                           :ARG0 s16c)
                               :temporal (s16u / until
                                               :op1 (s16d / drop-01
                                                          :ARG1 (s16b / bomb
                                                                      :mod (s16a / atom)
                                                                      :ord (s16o / ordinal-entity
                                                                                 :value 2))))
                               :polarity -)
                   :op2 (s16t / take-10
                              :ARG1 (s16i3 / intervene-01
                                           :ARG0 (s16p / person
                                                       :ARG1-of (s16h / have-org-role-92
                                                                      :ARG3 (s16e / emperor)))
                                           :mod (s16d2 / direct))
                              :purpose (s16f / force-01
                                             :ARG0 s16i3
                                             :ARG2 (s16s2 / surrender-01
                                                          :ARG0 (s16m / armed-organization
                                                                      :name (s16n3 / name
                                                                                   :op1 "Army")
                                                                      :wiki "United_States_Army")))
                              :temporal (s16a3 / after
                                               :op1 (s16a4 / attack-01
                                                           :ord s16o)
                                               :mod (s16e2 / even))))
      :mod (s16y2 / yet))

# alignment:

# document level annotation:

## english_umr-0217, sentence 1168

# :: snt1168
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           39           40           41           42           43           44           45           46           47           48           49           50           51           52           53           54           55           56           57           58           59           60           61           62           63           64           65           66           67           68           69           70           71           72           73           74           75           76           77           78           79           80           81           82           83           84           85           86           87           88           89           90           91           92           93           94           95           96           97           98           99           100          101          
Words: But          in           herself      alone        she          is           more         important    than         all          the          hundreds     of           you          other        roses        :            because      it           is           she          that         I            have         watered      ;            because      it           is           she          that         I            have         put          under        the          glass        globe        ;            because      it           is           she          that         I            have         sheltered    behind       the          screen       ;            because      it           is           for          her          that         I            have         killed       the          caterpillars (            except       the          two          or           three        that         we           saved        to           become       butterflies  )            ;            because      it           is           she          that         I            have         listened     to           ,            when         she          grumbled     ,            or           boasted      ,            or           ever         sometimes    when         she          said         nothing      .            

# sentence level graph:
(s1168s8 / say-91
         :ARG1 (s1168c4 / contrast-91
                        :ARG2 (s1168h / have-degree-91
                                      :ARG1 (s1168s / she
                                                    :mod (s1168a / alone))
                                      :ARG2 (s1168i3 / important-01
                                                     :ARG1 s1168s)
                                      :ARG3 (s1168m / more)
                                      :ARG4 (s1168r / rose
                                                    :mod (s1168a3 / all)
                                                    :mod (s1168o / other)
                                                    :quant (s1168m2 / multiple
                                                                    :op1 100))
                                      :ARG1-of (s1168c / cause-01
                                                       :ARG0 (s1168a2 / and
                                                                      :op1 (s1168w / water-01
                                                                                   :ARG0 (s1168i2 / i)
                                                                                   :ARG1 s1168s)
                                                                      :op2 (s1168p / put-01
                                                                                   :ARG0 s1168i2
                                                                                   :ARG1 s1168s
                                                                                   :ARG2 (s1168u / under
                                                                                                 :op1 (s1168g / globe
                                                                                                              :material (s1168g2 / glass))))
                                                                      :op3 (s1168s3 / shelter-01
                                                                                    :ARG0 s1168i2
                                                                                    :ARG1 s1168s
                                                                                    :ARG2 (s1168b2 / behind
                                                                                                   :op1 (s1168s4 / screen)))
                                                                      :op4 (s1168k / kill-01
                                                                                   :ARG0 s1168i2
                                                                                   :ARG1 (s1168c2 / caterpillar
                                                                                                  :ARG1-of (s1168h2 / have-subtraction-91
                                                                                                                    :ARG2 (s1168c3 / caterpillar
                                                                                                                                   :quant (s1168o2 / or
                                                                                                                                                   :op1 2
                
… (2836 more characters)

## english_umr-0086, sentence 10

# :: snt10
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          
Words: However,    I           temper      that        with        the         realization that        said        Republicans are         fighting    him         tooth       and         nail        on          everything. 

# sentence level graph:
(s10h / have-concession-91
      :ARG1 (s10t / temper-01
                  :ARG0 (s10i / i)
                  :ARG1 (s10t2 / that)
                  :manner (s10r / realize-01
                                :ARG0 s10i
                                :ARG1 (s10f / fight-01
                                            :ARG0 (s10p2 / person
                                                         :ARG1-of (s10h3 / have-org-role-92
                                                                         :ARG2 (s10p / political-organization
                                                                                     :name (s10n / name
                                                                                                 :op1 "Republican")
                                                                                     :wiki "Republican_Party_(United_States)"))
                                                         :ARG1-of (s10s / say-01))
                                            :ARG1 (s10h2 / he)
                                            :ARG2 (s10e / everything)
                                            :manner (s10a / and
                                                          :op1 (s10t3 / tooth)
                                                          :op2 (s10n2 / nail))))))

# alignment:

# document level annotation:

## english_umr-0216, sentence 1037

# :: snt1037
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         40         41         42         
Words: "          She        would      be         very       much       annoyed    ,          "          he         said       to         himself    ,          "          if         she        should     see        that       ...        she        would      cough      most       dreadfully ,          and        she        would      pretend    that       she        was        dying      ,          to         avoid      being      laughed    at         .          

# sentence level graph:
(s1037s / say-01
        :ARG0 (s1037h / he)
        :ARG1 (s1037a / and
                      :op1 (s1037a2 / annoy-01
                                    :ARG1 (s1037s2 / she)
                                    :degree intensifier)
                      :op2 (s1037c / cough-01
                                   :ARG0 s1037s2
                                   :ARG1-of (s1037h2 / have-degree-91
                                                     :ARG2 (s1037d2 / dreadful-02
                                                                    :ARG1 s1037c)
                                                     :ARG3 (s1037m / most)))
                      :op3 (s1037p / pretend-01
                                   :ARG0 s1037s2
                                   :ARG1 (s1037d / die-01
                                                 :ARG1 s1037s2)
                                   :purpose (s1037a3 / avoid-01
                                                     :ARG0 s1037s2
                                                     :ARG1 (s1037l / laugh-01
                                                                   :ARG2 s1037s2)))
                      :condition (s1037s3 / see-01
                                          :ARG0 s1037s2
                                          :ARG1 (s1037t / that))
                      :quote s1037s)
        :ARG2 s1037h)

# alignment:

# document level annotation:

## english_umr-0112, sentence 7

# :: snt7
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        
Words: That      certainly would     have      helped    get       the       country   going     again     and       was       being     called    for       by        some      of        the       more      far       left      liberals. 

# sentence level graph:
(s7a / and
     :op1 (s7h / help-01
               :ARG0 (s7t / that)
               :ARG1 (s7g / get-04
                          :ARG0 s7t
                          :ARG1 (s7g2 / go-09
                                      :ARG1 (s7c / country)
                                      :mod (s7a2 / again)))
               :mod (s7c2 / certain))
     :op2 (s7c3 / call-03
                :ARG0 (s7p / person
                           :quant (s7s / some)
                           :ARG1-of (s7h2 / have-degree-91
                                          :ARG2 (s7l2 / left-19
                                                      :ARG1 s7p
                                                      :degree (s7f / far))
                                          :ARG3 (s7m / most)
                                          :ARG5 (s7p2 / person
                                                      :ARG1-of (s7l / liberal-02))))
                :ARG1 s7t))

# alignment:

# document level annotation:

## english_umr-0046, sentence 3

# :: snt3
Index: 1                     2                     3                     4                     5                     6                     7                     8                     9                     10                    11                    12                    13                    14                    15                    16                    17                    18                    19                    20                    21                    22                    23                    24                    25                    26                    27                    28                    29                    30                    31                    32                    33                    34                    35                    36                    37                    38                    
Words: I'm                   looking               to                    trying                to                    start                 volunteering          sometime              in                    the                   near                  future                and                   was                   a                     rainbow/brownie/guide when                  younger               and                   think                 i                     might                 enjoy                 helping               out                   but                   have                  no                    idea                  how                   to                    make                  the                   first                 steps                 to                    get                   involved              

# sentence level graph:
(s3a / and
     :op1 (s3l / look-04
               :ARG0 (s3i / i)
               :ARG1 (s3t / try-01
                          :ARG0 s3i
                          :ARG1 (s3s / start-01
                                     :ARG0 s3i
                                     :ARG1 (s3v / volunteer-01
                                                :ARG0 s3i
                                                :temporal (s3s2 / sometime)
                                                :temporal (s3f / future
                                                               :ARG1-of (s3n / near-02))))))
     :op2 (s3s3 / slash
                :op1 (s3r / rainbow)
                :op2 (s3b / brownie)
                :op3 (s3g / guide)
                :domain s3i
                :temporal (s3y / young
                               :ARG2-of (s3h3 / have-degree-91
                                              :ARG1 s3i
                                              :ARG3 (s3m / more))))
     :op3 (s3t2 / think-01
                :ARG0 s3i
                :ARG1 (s3p / possible-01
                           :ARG1 (s3e / enjoy-01
                                      :ARG0 s3i
                                      :ARG1 (s3h / help-out-03
                                                 :ARG0 s3i)))
                :ARG1-of (s3c / contrast-91
                              :ARG2 (s3h2 / have-03
                                          :ARG0 s3i
                                          :ARG1 (s3i2 / idea
                                                      :mod (s3s5 / step-01
                                                                 :ARG0 s3i
                                                                 :ARG2 (s3i3 / involve-01
                                                                             :ARG1 s3i)
                                                                 :ord (s3o / ordinal-entity
                                                                           :value 1))
                                                      :polarity -)))))

# alignment:

# document level annotation:

## english_umr-0015, sentence 5

# :: snt5
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       
Words: IMO....  she      is       helping  him      more     now,     because  he       is       hurting  himself, more.    

# sentence level graph:
(s5o / opine-01
     :ARG0 (s5i / i)
     :ARG1 (s5h / help-01
                :ARG0 (s5s / she)
                :ARG1 (s5h2 / he)
                :quant (s5m / more)
                :temporal (s5n / now)
                :ARG1-of (s5c / cause-01
                              :ARG0 (s5h3 / hurt-01
                                          :ARG0 s5h2
                                          :ARG1 s5h2
                                          :quant (s5m2 / more)))))

# alignment:

# document level annotation:

## english_umr-0052, sentence 3

# :: snt3
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         
Words: Government has        restricted market     forces     from       weeding    out        insurance  companies  who        act        out        as         you        stated     by         preventing people     from       purchasing insurance  across     state      lines.     

# sentence level graph:
(s3r / restrict-01
     :ARG0 (s3g / government-organization
                :ARG0-of (s3g2 / govern-01))
     :ARG1 (s3w / weed-01
                :ARG0 (s3f / force
                           :possessor (s3m / market))
                :ARG2 (s3c / company
                           :ARG0-of (s3i / insure-02)
                           :ARG0-of (s3a / act-out-03
                                         :ARG1 (s3s / state-01
                                                    :ARG0 (s3y / you)))))
     :manner (s3p / prevent-01
                  :ARG0 s3g
                  :ARG1 (s3p2 / person)
                  :ARG2 (s3p3 / purchase-01
                              :ARG0 s3p2
                              :ARG1 s3i
                              :place (s3a2 / across
                                           :op1 (s3l / line
                                                     :mod (s3s2 / state))))))

# alignment:

# document level annotation:

## english_umr-0212, sentence 980

# :: snt980
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       
Words: "        Whomever I        touch    ,        I        send     back     to       the      earth    from     whence   he       came     ,        "        the      snake    spoke    again    .        

# sentence level graph:
(s980s / speak-01
       :ARG0 (s980s2 / snake)
       :ARG1 (s980s3 / send-01
                     :ARG0 s980s2
                     :ARG1 (s980p / person
                                  :ARG1-of (s980t / touch-01
                                                  :ARG0 s980s2)
                                  :mod (s980a2 / any))
                     :ARG2 (s980b / back
                                  :op1 (s980e / earth
                                              :ARG3-of (s980c / come-01
                                                              :ARG1 s980p)))
                     :quote s980s)
       :mod (s980a / again))

# alignment:

# document level annotation:
