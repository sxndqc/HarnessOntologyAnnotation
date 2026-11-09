# Gold UMR annotations of sentences like those of english_umr-0005

From ai-native-annotator.github.io data/skillparse/resources/gold/en/gold.json (no test document).

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

## english_umr-0111, sentence 21

# :: snt21
Index: 1                2                3                4                5                6                7                8                9                10               11               12               13               14               15               16               17               18               19               20               21               22               
Words: Running          for              POTUS            is               a                whole            hell             of               a                lot              easier           that             being            POTUS.Especially when             you              don't            have             the              skills           for              it.              

# sentence level graph:
(s21h5 / have-degree-91
       :ARG1 (s21r / run-02
                   :ARG0 (s21y / you)
                   :ARG1 (s21p / president
                               :ARG3-of (s21h / have-org-role-92
                                              :ARG2 (s21c / country
                                                          :name (s21n / name
                                                                      :op1 "United"
                                                                      :op2 "States")
                                                          :wiki "United_States"))))
       :ARG2 (s21e / easy-05)
       :ARG3 (s21m / more
                   :quant (s21l / lot
                                :mod (s21h2 / hell
                                            :mod (s21w / whole))))
       :ARG4 (s21h3 / have-org-role-92
                    :ARG1 s21y
                    :ARG2 s21c
                    :ARG3 s21p)
       :condition (s21h4 / have-03
                         :ARG0 s21y
                         :ARG1 (s21s / skill
                                     :purpose s21h3)
                         :mod (s21e2 / especially)
                         :polarity -))

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

## english_umr-0208, sentence 682

# :: snt682
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          
Words: The         businessman suddenly    realized    that        there       was         no          hope        of          being       left        in          peace       until       he          answered    this        question    .           

# sentence level graph:
(s682r / realize-01
       :ARG0 (s682p2 / person
                     :ARG1-of (s682h2 / have-role-91
                                      :ARG3 (s682b / businessman)))
       :ARG1 (s682h / hopeful-03
                    :ARG0 s682p2
                    :ARG1 (s682l / leave-14
                                 :ARG1 (s682p / peace-01
                                              :ARG1 s682p2
                                              :aspect state
                                              :modal-strength full-affirmative))
                    :temporal (s682u / until
                                     :op1 (s682a / answer-01
                                                 :ARG0 s682p2
                                                 :ARG1 (s682q / question-01
                                                              :ARG1 (s682t / this))
                                                 :aspect performance
                                                 :modal-strength full-affirmative))
                    :polarity -
                    :aspect state
                    :modal-strength full-negative)
       :ARG1-of (s682s / suddenness-01)
       :aspect performance
       :modal-strength full-affirmative)

# alignment:

# document level annotation:

## english_umr-0011, sentence 4

# :: snt4
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        
Words: After     seeing    those     bus       tours     to        AIG       execs     homes,    promoted  on        ACORN's   website,  I         am        wondering why       those     same      people    aren't    outraged  at        this.     

# sentence level graph:
(s4w / wonder-01
     :ARG0 (s4i / i)
     :ARG1 (s4t4 / thing
                 :ARG0-of (s4c / cause-01
                               :ARG1 (s4o / outrage-01
                                          :ARG0 (s4t / this)
                                          :ARG1 (s4p / person
                                                     :mod (s4t2 / this)
                                                     :ARG1-of (s4s / same-01))
                                          :polarity -)))
     :temporal (s4a2 / after
                     :op1 (s4s2 / see-01
                                :ARG1 (s4t3 / tour
                                            :mod (s4b / bus)
                                            :destination (s4h / home
                                                              :possessor (s4p2 / person
                                                                               :ARG1-of (s4h2 / have-org-role-92
                                                                                              :ARG2 (s4c2 / company
                                                                                                          :name (s4n / name
                                                                                                                     :op1 "AIG")
                                                                                                          :wiki "American_International_Group")
                                                                                              :ARG3 (s4e / executive))))
                                            :ARG1-of (s4p3 / promote-02
                                                           :ARG0 (s4w2 / website
                                                                       :possessor (s4i2 / international-organization
                                                                                        :name (s4n2 / name
                                                                                                    :op1 "ACORN")
                                                                                        :wiki "Association_of_Community_Organizations_for_Reform_Now")))))))

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

## english_umr-0361, sentence 56

# :: snt56
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          
Words: <Architect> so          instead     of          that        higher      yellow      coming      off         of          that        side        of          the         other       one         it          should      come        off         of          the         side        closest     to          the         green       

# sentence level graph:
(s56h4 / have-substitute-91
       :ARG1 (s56r / recommend-01
                   :ARG1 (s56c / come-33
                               :ARG1 (s56t / thing
                                           :color (s56y / yellow)
                                           :ARG1-of (s56h3 / have-degree-91
                                                           :ARG2 (s56h2 / high-02
                                                                        :ARG1 s56t
                                                                        :ARG3 (s56c3 / cartesian-framework-91
                                                                                     :ARG1 (s56b / build-space)))
                                                           :ARG3 (s56m2 / more))
                                           :mod (s56t2 / that))
                               :ARG3 (s56s / side
                                           :ARG1-of (s56h / have-degree-91
                                                          :ARG2 (s56c2 / close-10
                                                                       :ARG1 s56s
                                                                       :ARG2 (s56t6 / thing
                                                                                    :color (s56g / green)))
                                                          :ARG3 (s56m / most)))
                               :direction (s56t5 / trajectory
                                                 :ARG3-of (s56o2 / off-06
                                                                 :ARG2 s56s))))
       :ARG2 (s56c4 / come-33
                    :ARG1 s56t
                    :ARG3 (s56s2 / side
                                 :mod (s56t3 / that)
                                 :part-of (s56t4 / thing
                                                 :ARG1-of (s56o / other-01)))
                    :direction (s56t7 / trajectory
                                      :ARG3-of (s56o3 / off-06
                                                      :ARG2 s56s2))))

# alignment:

# document level annotation:

## english_umr-0545, sentence 31

# :: snt31
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          
Words: <Architect> so          you         see         that        yellow      block       that's      the         highest?    place       a           block       to          the         right       of          it          

# sentence level graph:
(s31a / and
      :op1 (s31s / see-01
                  :ARG0 (s31y / you)
                  :ARG1 (s31b / block
                              :mod (s31t / that)
                              :ARG1-of (s31h / have-degree-91
                                             :ARG2 (s31h2 / high-02
                                                          :ARG1 s31b
                                                          :ARG6 (s31c / cartesian-framework-91
                                                                      :ARG1 (s31b3 / build-space)))
                                             :ARG3 (s31m2 / most))
                              :color (s31y4 / yellow))
                  :ARG1-of (s31r / request-confirmation-91))
      :op2 (s31p / place-01
                  :ARG0 (s31y3 / you)
                  :ARG1 (s31b2 / block)
                  :ARG2 (s31s2 / space
                               :ARG1-of (s31r2 / right-04
                                               :ARG2 s31b
                                               :ARG3 (s31c2 / cartesian-framework-91
                                                            :ARG1 s31y)))
                  :mode imperative))

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

## english_umr-0021, sentence 1

# :: snt1
Index: 1           2           3           4           5           6           7           8           9           10          
Words: Can         we          PLEASE      get         these       people      a           voice       in          Washington? 

# sentence level graph:
(s1p2 / possible-01
      :ARG1 (s1g / get-01
                 :ARG0 (s1w / we)
                 :ARG1 (s1v / voice
                            :place (s1c / city
                                        :name (s1n / name
                                                   :op1 "Washington")
                                        :wiki "Washington,_D.C."))
                 :ARG4 (s1p / person
                            :mod (s1t / this)))
      :polarity (s1a / umr-unknown)
      :polite +)

# alignment:

# document level annotation:

## english_umr-0131, sentence 6

# :: snt6
Index: 1                                                                                             2                                                                                             3                                                                                             4                                                                                             5                                                                                             
Words: <a                                                                                            href="http://www.businessweek.com/articles/2012-03-16/wanted-more-ceos-in-washington">Herding Pig$                                                                                          To                                                                                            D.C.</a>                                                                                      

# sentence level graph:
(s6h / herd-01
     :ARG1 (s6p / pig)
     :direction (s6c / city
                     :name (s6n / name
                                :op1 "Washington"
                                :op2 "D.C.")
                     :wiki "Washington,_D.C."))

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

## english_umr-0192, sentence 3

# :: snt3
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          42          43          44          45          
Words: Plans       that        give        advertisers discounts   for         maintaining or          increasing  ad          spending    have        become      permanent   fixtures    at          the         news        weeklies    and         underscore  the         fierce      competition between     Newsweek    ,           Time        Warner      Inc.        's          Time        magazine    ,           and         Mortimer    B.          Zuckerman   's          U.S.        News        &           World       Report      .           

# sentence level graph:
(s3a2 / and
      :op1 (s3b / become-01
                :ARG1 (s3p2 / plan
                            :ARG0-of (s3g / give-01
                                          :ARG1 (s3t / thing
                                                     :ARG2-of (s3d / discount-01))
                                          :ARG2 (s3c7 / company
                                                      :ARG0-of (s3a3 / advertise-01))
                                          :ARG1-of (s3c8 / cause-01
                                                         :ARG0 (s3o / or
                                                                    :op1 (s3m2 / maintain-01
                                                                               :ARG0 s3c7
                                                                               :ARG1 (s3m3 / monetary-quantity
                                                                                           :ARG3-of (s3s / spend-01
                                                                                                         :ARG0 s3c7
                                                                                                         :ARG1 (s3a4 / advertise-01))))
                                                                    :op2 (s3i / increase-01
                                                                              :ARG0 s3c7
                                                                              :ARG1 s3m3)))))
                :ARG2 (s3f2 / fixture
                            :mod (s3p3 / permanent)
                            :prep-at (s3m4 / magazine
                                           :mod (s3r / rate-entity-91
                                                     :ARG3 (s3t3 / temporal-quantity
                                                                 :unit (s3w / week)
                                                                 :quant 1))
                                           :mod (s3n2 / news))))
      :op2 (s3u2 / underscore-01
                 :ARG0 s3p2
                 :ARG1 (s3c2 / compete-02
                             :ARG0 (s3a / and
                                        :op1 (s3m5 / magazine
                                                   :name (s3n / name
                                                              :op1 "Newsweek")
                                                   :wiki "Newsweek")
                                        :op2 (s3m6 / magazine
                                                   :name (s3t2 / name
                                                               :op1 "Time"
                                                               :op2 "Magazine")
                                                   :possessor (s3c / company
                                                                   :name (s3n3 / name
                                                                               :op1 "Time"
                                                                               :op2 "Warner"
                                                                               :op3 "Inc.")
                                                                   :wiki "Time_Warner")
                                                   :wiki "Time_(magazine)")
                                        :op3 (s3m7 / magazine
                                                   :name (s3u / name
                                                              :op1 "U.S."
                                                              :op2 "News"
                                                              :op3 "&"
                                                              :op4 "World"
                                                              :op5 "Report")
                                                   :possessor (s3p / person
                                                                   :name (s3m / name
                                                                              :op1 "Mortimer"
                                                                              :op2 "B."
                                                                              :op3 "Zuckerman")
                                                                   :wiki "Mortimer_Zuckerman")
                                                   :wiki "U.S._News_&_World_Report"))
                             :manner (s3f / fierce))))

# alignment:

# document level annotation:

## english_umr-0192, sentence 1

# :: snt1
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          
Words: Newsweek    ,           trying      to          keep        pace        with        rival       Time        magazine    ,           announced   new         advertising rates       for         1990        and         said        it          will        introduce   a           new         incentive   plan        for         advertisers .           

# sentence level graph:
(s1a2 / and
      :op1 (s1a / announce-01
                :ARG0 (s1m2 / magazine
                            :name (s1n / name
                                       :op1 "Newsweek")
                            :wiki "Newsweek")
                :ARG1 (s1r / rate
                           :ARG1-of (s1n2 / new-01)
                           :mod (s1a4 / advertise-01)
                           :temporal (s1d / date-entity
                                          :year 1990)))
      :op2 (s1s / say-01
                :ARG0 s1m2
                :ARG1 (s1i / introduce-02
                           :ARG0 s1m2
                           :ARG1 (s1p3 / plan
                                       :ARG1-of (s1n3 / new-01)
                                       :ARG0-of (s1i2 / incentivize-01
                                                      :ARG1 (s1c2 / company
                                                                  :ARG0-of (s1a3 / advertise-01))))))
      :ARG1-of (s1c / cause-01
                    :ARG0 (s1t3 / try-01
                                :ARG0 s1m2
                                :ARG1 (s1k2 / keep-up-05
                                            :ARG0 s1m2
                                            :ARG1 (s1m / magazine
                                                       :name (s1t / name
                                                                  :op1 "Time")
                                                       :ARG1-of (s1r2 / rival-01
                                                                      :ARG0 s1m2)
                                                       :wiki "Time_(magazine)")))))

# alignment:

# document level annotation:

## english_umr-0041, sentence 5

# :: snt5
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          42          43          44          45          46          47          48          49          50          51          52          53          54          55          
Words: We          also        seem        to          be          losing      the         ability     to          defend      ourselves   politically ,           being       subservient to          the         United      States      in          their       quest       to          capture     resources   ,           and         being       a           part        of          the         European    Union       ,           often       have        to          accept      group       decisions   that        the         country     does        not         agree       with        or          benefit     from        in          any         way         .           

# sentence level graph:
(s5a7 / and
      :op1 (s5s / seem-01
                :ARG1 (s5l / lose-02
                           :ARG0 (s5p3 / person
                                       :refer-person 1st
                                       :refer-number plural)
                           :ARG1 (s5d / defend-01
                                      :ARG0 s5p3
                                      :ARG1 s5p3
                                      :manner (s5p / political)
                                      :aspect activity
                                      :modal-strength neutral-affirmative)
                           :aspect activity
                           :modal-strength partial-affirmative
                           :modal-predicate s5s)
                :mod (s5a6 / also)
                :reason (s5s2 / subservient-01
                              :ARG0 s5p3
                              :ARG1 (s5c3 / country
                                          :wiki "United_States"
                                          :name (s5n2 / name
                                                      :op1 "United"
                                                      :op2 "States"))
                              :ARG2 (s5q / quest-01
                                         :ARG0 s5c3
                                         :ARG1 (s5c4 / capture-01
                                                     :ARG0 s5c3
                                                     :ARG1 (s5r / resource
                                                                :refer-number plural)
                                                     :aspect habitual
                                                     :modal-strength full-affirmative)
                                         :aspect activity
                                         :modal-strength full-affirmative)
                              :aspect state
                              :modal-strength full-affirmative))
      :op2 (s5a3 / accept-01
                 :ARG0 s5p3
                 :ARG1 (s5t / thing
                            :refer-number plural
                            :ARG1-of (s5d2 / decide-01
                                           :ARG0 (s5i / international-organization
                                                      :wiki "European_Union"
                                                      :name (s5n / name
                                                                  :op1 "European"
                                                                  :op2 "Union"))
                                           :manner (s5g / group))
                            :ARG1-of (s5a4 / agree-01
                                           :polarity -
                                           :ARG0 (s5c2 / country)
                                           :aspect state
                                           :modal-strength full-negative)
                            :ARG0-of (s5b / benefit-01
                                          :polarity -
                                          :ARG1 s5c2
                                          :manner (s5w / way
                                                       :mod (s5a5 / any))
                                          :aspect state
                                          :modal-strength full-negative)
                            :aspect process
                            :modal-strength full-affirmative)
                 :frequency (s5o3 / often)
                 :reason (s5h / have-part-91
                              :ARG1 s5i
                              :ARG2 s5p3
                              :aspect state
                              :modal-strength full-affirmative)
                 :aspect habitual
                 :modal-strength partial-affirmative))

# alignment:

# document level annotation:

## english_umr-0013, sentence 11

# :: snt11
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22      23      
Words: I       mean    you     don't   really  think   that    any     of      these   guys    really  give    a       shit    about   their   party   or      their   nation, do      ya?     

# sentence level graph:
(s11m / mean-01
      :ARG0 (s11i / i)
      :ARG2 (s11t / think-01
                  :ARG0 (s11y / you)
                  :ARG1 (s11g / give-16
                              :ARG0 (s11a / any
                                          :ARG1-of (s11i2 / include-91
                                                          :ARG2 (s11g2 / guy
                                                                       :mod (s11t2 / this))))
                              :ARG1 (s11s / shit-01)
                              :ARG2 (s11o / or
                                          :op1 (s11p / party
                                                     :possessor s11a)
                                          :op2 (s11n / nation
                                                     :possessor s11a))
                              :ARG1-of (s11r2 / real-04))
                  :ARG1-of (s11r / real-04)
                  :ARG1-of (s11r3 / request-confirmation-91)
                  :polarity -))

# alignment:

# document level annotation:

## english_umr-0196, sentence 86

# :: snt86
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         
Words: Of         Iraq       's         27         million    prewar     population ,          about      1          in         8          --         some       3.4        million    people     --         have       left       their      homes      since      the        invasion   ,          according  to         the        United     Nations    High       Commission for        Refugees   (          unhcr      )          ,          

# sentence level graph:
(s86s3 / say-01
       :ARG0 (s86i4 / international-organization
                    :name (s86n2 / name
                                 :op1 "United"
                                 :op2 "Nations"
                                 :op3 "High"
                                 :op4 "Commission"
                                 :op5 "for"
                                 :op6 "Refugees")
                    :wiki "United_Nations_High_Commissioner_for_Refugees")
       :ARG1 (s86l / leave-11
                   :ARG0 (s86p4 / person
                                :quant (s86s / some
                                             :op1 3400000)
                                :ARG1-of (s86m / mean-91
                                               :ARG2 (s86p / person
                                                           :ARG1-of (s86i2 / include-91
                                                                           :ARG2 (s86p6 / person
                                                                                        :ARG2-of (s86p7 / populate-01
                                                                                                        :ARG1 (s86c2 / country
                                                                                                                     :name (s86n / name
                                                                                                                                 :op1 "Iraq")
                                                                                                                     :wiki "Iraq")
                                                                                                        :temporal (s86b / before
                                                                                                                        :op1 (s86w / war)))
                                                                                        :quant 27000000)
                                                                           :ARG3 "1/8"))))
                   :ARG1 (s86h / home
                               :possessor s86p4)
                   :temporal (s86s2 / since
                                    :op1 (s86i3 / invade-01))))

# alignment:

# document level annotation:

## english_umr-0213, sentence 1000

# :: snt1000
Index: 1       2       3       4       5       6       7       8       
Words: I       saw     them    ,       several years   ago     .       

# sentence level graph:
(s1000s / see-01
        :ARG0 (s1000i / i)
        :ARG1 (s1000t / they)
        :temporal (s1000b / before
                          :op1 (s1000n / now)
                          :quant (s1000s2 / several
                                          :op1 (s1000t2 / temporal-quantity
                                                        :unit (s1000y / year)
                                                        :quant 1))))

# alignment:

# document level annotation:

## english_umr-0196, sentence 150

# :: snt150
Index: 1           2           3           4           5           6           7           8           9           
Words: Abather     and         Balqes      had         made        several     pilgrimages there       ;           

# sentence level graph:
(s150m / make-01
       :ARG0 (s150a2 / and
                     :op1 (s150p4 / person
                                  :name (s150n / name
                                               :op1 "Abather")
                                  :wiki -)
                     :op2 (s150p5 / person
                                  :name (s150n2 / name
                                                :op1 "Balqes")
                                  :wiki -))
       :ARG1 (s150p3 / pilgrimage
                     :quant (s150s / several))
       :destination (s150t / there))

# alignment:

# document level annotation:

## english_umr-0220, sentence 1237

# :: snt1237
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       
Words: When     we       had      trudged  along    for      several  hours    ,        in       silence  ,        the      darkness fell     ,        and      the      stars    began    to       come     out      .        

# sentence level graph:
(s1237a / and
        :op1 (s1237f / fall-04
                     :ARG1 (s1237d / darkness))
        :op2 (s1237b / begin-01
                     :ARG0 (s1237s / star)
                     :ARG1 (s1237c / come-out-09
                                   :ARG1 s1237s))
        :temporal (s1237t / trudge-01
                          :ARG0 (s1237w / we)
                          :duration (s1237s2 / several
                                             :op1 (s1237t2 / temporal-quantity
                                                           :unit (s1237h / hour)
                                                           :quant 1))
                          :manner (s1237s3 / silent)))

# alignment:

# document level annotation:

## english_umr-0157, sentence 16

# :: snt16
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           
Words: I'm          sure         there        were         plenty       of           Christian    churches     built        during       and          shortly      after        the          various      Crusades     in           what         had          formally     been         Muslim       territories. 

# sentence level graph:
(s16s / sure-02
      :ARG0 (s16i / i)
      :ARG1 (s16b / build-01
                  :ARG1 (s16c / church
                              :mod (s16r / religious-group
                                         :name (s16n / name
                                                     :op1 "Christian")
                                         :wiki "Christian")
                              :quant (s16p / plenty))
                  :duration (s16w / war
                                  :name (s16n2 / name
                                               :op1 "Crusade")
                                  :mod (s16v / various)
                                  :wiki "Crusades")
                  :temporal (s16a / after
                                  :op1 s16w
                                  :ARG1-of (s16s2 / short-07))
                  :place (s16t / territory
                               :possessor (s16r2 / religious-group
                                                 :name (s16n3 / name
                                                              :op1 "Muslim")
                                                 :wiki "Muslim")
                               :mod (s16f / formal))))

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

## english_umr-0195, sentence 50

# :: snt50
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            46            
Words: More          questionable  ,             even          criminal      ,             than          Michael       's            alleged       fooling       around        with          other         kids          ,             were          the           parents       who           allowed       ,             even          encouraged    their         children      to            sleep         over          and           perhaps       share         the           same          bed           with          someone       whose         sexual        predilections have          been          suspect       since         1991          .             

# sentence level graph:
(s50a3 / and
       :op1 (s50h3 / have-degree-91
                   :ARG1 (s50p / person
                               :ARG0-of (s50a / allow-01
                                              :ARG1 (s50a2 / and
                                                           :op1 (s50s / sleep-over-05
                                                                      :ARG0 (s50p7 / person
                                                                                   :ARG1-of (s50h2 / have-rel-role-92
                                                                                                   :ARG2 s50p
                                                                                                   :ARG3 (s50c / child))))
                                                           :op2 (s50s2 / share-01
                                                                       :ARG0 s50p7
                                                                       :ARG1 (s50b / bed
                                                                                   :ARG1-of (s50s7 / same-01))
                                                                       :ARG2 (s50s6 / someone
                                                                                    :possessor-of (s50p3 / predilection
                                                                                                         :mod (s50s3 / sexual)
                                                                                                         :ARG2-of (s50s4 / suspect-01
                                                                                                                         :temporal (s50s5 / since
                                                                                                                                          :op1 (s50d2 / date-entity
                                                                                                                                                      :year 1991)))))
                                                                       :ARG1-of (s50p5 / possible-01))))
                               :ARG0-of (s50e / encourage-01
                                              :ARG1 s50p7
                                              :ARG2 s50a2
                                              :mod (s50e4 / even))
                               :ARG1-of (s50h / have-rel-role-92
                                              :ARG3 (s50p2 / parent)))
                   :ARG2 (s50q / question-03
                               :ARG1 s50p)
                   :ARG3 (s50m / more)
                   :ARG4 (s50a4 / allege-01
                                :ARG1 (s50f / fool-around-02
                                            :ARG0 (s50a5 / and
                                                         :op1 (s50p6 / person
                                                                     :name (s50n / name
                                                                                 :op1 "Michael")
                                                                     :wiki "Michael_Jackson")
                                                         :op2 (s50k / kid
                                                                    :mod (s50o / other))))))
       :op2 (s50h4 / have-degree-91
                   :ARG1 s50p
                   :ARG2 (s50c2 / criminal-03
                                :ARG1 s50p
                                :mod (s50e2 / even))
                   :ARG3 (s50m2 / more)
                   :ARG4 s50a4))

# alignment:

# document level annotation:

## english_umr-0021, sentence 14

# :: snt14
Index: 1               2               3               4               5               6               7               8               9               10              11              12              13              14              15              16              17              18              19              20              21              22              23              24              25              26              27              28              29              30              31              32              
Words: The             members         of              the             minority        party           in              the             House           of              Representatives are             largely         ciphers         anyway,         although        only            a               few             of              them            have            the             excuse          that            they            suffer          from            medically       certifiable     brain           damage.         

# sentence level graph:
(s14i / include-91
      :ARG1 (s14p / person
                  :ARG1-of (s14h / have-org-role-92
                                 :ARG2 (s14p2 / political-party
                                              :mod (s14m2 / minority))
                                 :ARG3 (s14m / member))
                  :ARG1-of (s14h2 / have-org-role-92
                                  :ARG2 (s14g / government-organization
                                              :name (s14n / name
                                                          :op1 "House"
                                                          :op2 "of"
                                                          :op3 "Representatives")
                                              :wiki "United_States_House_of_Representatives")
                                  :ARG3 (s14m3 / member)))
      :ARG2 (s14c / cipher)
      :ARG3 (s14l / large)
      :mod (s14a / anyway)
      :concession (s14e / excuse-02
                        :ARG0 (s14p3 / person
                                     :quant (s14f / few)
                                     :ARG1-of (s14i2 / include-91
                                                     :ARG2 s14p))
                        :ARG2 (s14s / suffer-01
                                    :ARG0 s14p3
                                    :ARG1 (s14d / damage-01
                                                :ARG1 (s14b / brain)
                                                :ARG1-of (s14c2 / certify-01
                                                                :ARG1-of (s14p4 / possible-01)
                                                                :mod (s14m4 / medical))))))

# alignment:

# document level annotation:

## english_umr-0196, sentence 163

# :: snt163
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            46            47            48            
Words: Except        that          ,             as            Amman         unhcr         head          Robert        Breen         told          me            ,             a             1998          agreement     with          Jordan        forbids       the           agency        from          classifying   anyone        as            a             refugee       whom          it            ca            n't           get           out           of            the           country       within        six           months        --            an            impossibility in            the           post          /             11            world         .             

# sentence level graph:
(s163h2 / have-concession-91
        :ARG2 (s163f / forbid-01
                     :ARG0 (s163a2 / agree-01
                                   :ARG0 (s163i3 / international-organization
                                                 :name (s163n2 / name
                                                               :op1 "UNHCR")
                                                 :place (s163c4 / city
                                                                :name (s163n3 / name
                                                                              :op1 "Amman")
                                                                :wiki "Amman")
                                                 :wiki "United_Nations_High_Commissioner_for_Refugees")
                                   :ARG2 (s163c5 / country
                                                 :name (s163n4 / name
                                                               :op1 "Jordan")
                                                 :wiki "Jordan")
                                   :temporal (s163d2 / date-entity
                                                     :year 1998))
                     :ARG1 (s163c6 / classify-01
                                   :ARG0 s163i3
                                   :ARG1 (s163a3 / anyone
                                                 :ARG1-of (s163g / get-05
                                                                 :ARG0 s163i3
                                                                 :ARG2 (s163o / out-06
                                                                              :ARG1 s163i3
                                                                              :ARG2 (s163c7 / country))
                                                                 :ARG1-of (s163p3 / possible-01
                                                                                  :ARG1-of (s163c / contrast-91
                                                                                                  :ARG2 (s163p / possible-01
                                                                                                               :ARG1 s163g
                                                                                                               :temporal (s163w / world
                                                                                                                                :mod (s163a4 / after
                                                                                                                                             :op1 (s163i2 / incident
                                                                                                                                                          :name (s163n5 / name
                                                                                                                                                                        :op1 "9/11")
                                                                                                                                                          :wiki "September_11_attacks")))
                                                                                                               :polarity -))
                                                                                  :polarity -)
                                                                 :temporal (s163a5 / after
                                                                                   :op1 (s163e2 / event)
                                                                                   :quant (s163u / up-to
                                                                                                 :op1 (s163t3 / temporal-quantity
                                                                                                              :unit (s163m2 / month)
                                                                                                              :quant 6)))))
                                   :ARG2 (s163r2 / refugee))
                     :ARG1-of (s163t2 / tell-01
                                      :ARG0 (s163p2 / person
                                                    :name (s163n / name
                                                                 :op1 "Robert"
                                                                 :op2 "Breen")
                                                    :ARG0-of (s163h / head-01
           
… (234 more characters)

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

## english_umr-0112, sentence 6

# :: snt6
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      
Words: Then    forced  them    to      lend    the     money   given   them    by      Bush,   and     also    force   them    to      rewrite loans.  

# sentence level graph:
(s6a / and
     :op1 (s6f / force-01
               :ARG1 (s6t / they)
               :ARG2 (s6l / lend-01
                          :ARG0 s6t
                          :ARG1 (s6m / money
                                     :ARG1-of (s6g / give-01
                                                   :ARG0 (s6p / person
                                                              :name (s6n / name
                                                                         :op1 "Bush")
                                                              :wiki "George_W._Bush")
                                                   :ARG2 s6t)))
               :temporal (s6t2 / then))
     :op2 (s6f2 / force-01
                :ARG1 s6t
                :ARG2 (s6r / rewrite-01
                           :ARG0 s6t
                           :ARG1 (s6l2 / loan-01))
                :mod (s6a2 / also)))

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

## english_umr-0174, sentence 25

# :: snt25
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            
Words: Agricultural, commercial,   and           residential   development   destroyed     much          of            the           swamp,        so            that          the           remaining     portion       within        and           around        the           refuge        represents    less          than          half          of            the           original      size.         

# sentence level graph:
(s25d / destroy-01
      :ARG1 (s25s / swamp
                  :quant (s25m / much))
      :ARG2 (s25d2 / develop-02
                   :ARG1 (s25a / and
                               :op1 (s25a2 / agriculture)
                               :op2 (s25c / commerce)
                               :op3 (s25r / residence)))
      :ARG0-of (s25c2 / cause-01
                      :ARG1 (s25r2 / represent-01
                                   :ARG0 (s25p / portion
                                               :ARG1-of (s25r3 / remain-01)
                                               :place (s25w / within
                                                            :op1 (s25r4 / refuge))
                                               :place (s25a3 / around
                                                             :op1 s25r4))
                                   :ARG1 (s25l / less-than
                                               :op1 (s25h / half
                                                          :part-of (s25s2 / size
                                                                          :mod (s25o / original)))))))

# alignment:

# document level annotation:

## english_umr-0215, sentence 52

# :: snt52
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        
Words: But       my        drawing   is        certainly very      much      less      charming  than      its       model     .         

# sentence level graph:
(s52c3 / contrast-91
       :ARG2 (s52h / have-degree-91
                   :ARG1 (s52p / picture
                               :ARG1-of (s52d / draw-01
                                              :ARG0 (s52i / i)))
                   :ARG2 (s52c / charm-01
                               :ARG0 s52p)
                   :ARG3 (s52l / less
                               :quant (s52m / much
                                            :degree intensifier))
                   :ARG4 (s52m2 / model
                                :possessor s52p)
                   :mod (s52c2 / certain)))

# alignment:

# document level annotation:

## english_umr-0195, sentence 53

# :: snt53
Index: 1          2          3          4          5          6          7          8          9          10         11         12         13         14         15         16         17         18         19         20         21         22         23         
Words: Mahatma    Gandhi     writes     that       '          There      is         a          higher     court      than       courts     of         justice    and        that       is         the        court      of         conscience .          '          

# sentence level graph:
(s53w / write-01
      :ARG0 (s53p2 / person
                   :name (s53n / name
                               :op1 "Mahatma"
                               :op2 "Gandhi")
                   :wiki "Mahatma_Gandhi")
      :ARG1 (s53a / and
                  :op1 (s53e / exist-91
                             :ARG1 (s53t / there)
                             :ARG2 (s53c / court
                                         :ARG1-of (s53h2 / have-degree-91
                                                         :ARG2 (s53h / high-02
                                                                     :ARG1 s53c)
                                                         :ARG3 (s53m2 / more)
                                                         :ARG4 (s53c2 / court
                                                                      :mod (s53j / justice))))
                             :aspect state
                             :modal-strength full-affirmative)
                  :op2 (s53i / identity-91
                             :ARG1 s53c2
                             :ARG2 (s53c3 / court
                                          :mod (s53c4 / conscience))
                             :aspect state
                             :modal-strength full-affirmative)
                  :quote s53w)
      :aspect state
      :modal-strength full-affirmative)

# alignment:

# document level annotation:

## english_umr-0578, sentence 20

# :: snt20
Index: 1              2              3              4              5              6              7              8              9              10             11             12             13             14             15             16             17             18             19             20             21             22             23             24             25             26             27             28             29             30             31             32             33             34             35             36             37             38             39             40             41             42             43             44             45             46             47             48             49             50             51             52             53             54             
Words: The            U.S.           is             one            of             the            few            industrialized nations        that           does           n't            have           a              higher         standard       of             regulation     for            the            smooth         ,              needle         -              like           fibers         such           as             crocidolite    that           are            classified     as             amphobiles     ,              according      to             Brooke         T.             Mossman        ,              a              professor      of             pathlogy       at             the            University     of             Vermont        College        of             Medicine       .              

# sentence level graph:
(s20s / say-91
    :ARG0 (s20p2 / person :wiki - 
        :name (s20n / name :op1 "Brooke" :op2 "T." :op3 "Mossman")
        :ARG1-of (s20h3 / have-org-role-92
            :ARG2 (s20a2 / academic-organization
                :name (s20n2 / name :op1 "College" :op2 "of" :op3 "Medicine")
                :part-of (s20a3 / academic-organization :wiki "University_of_Vermont" 
                    :name (s20n3 / name :op1 "University" :op2 "of" :op3 "Vermont")))
            :ARG3 (s20p3 / professor
                :topic (s20p / pathology))))
    :ARG1 (s20i2 / include-91
        :ARG1 (s20c / country :wiki "United_States" 
            :name (s20n4 / name :op1 "U.S."))
        :ARG2 (s20n5 / nation
            :refer-number plural
            :ARG1-of (s20i3 / include-91
                :ARG2 (s20n6 / nation
                    :refer-number plural
                    :ARG1-of (s20i / industrialize-01)))
            :ARG0-of (s20r / regulate-01 
                :polarity -
                :ARG1 (s20f2 / fiber
                    :refer-number plural
                    :ARG1-of (s20s3 / smooth-06)
                    :ARG2-of (s20r2 / resemble-91
                        :ARG1 (s20n7 / needle))
                    :ARG1-of (s20c4 / classify-01
                        :ARG2 (s20a / amphibole))
                    :example (s20c3 / crocidolite))
                :ARG1-of (s20s2 / standardize-01
                    :ARG1-of (s20h / have-degree-91
                        :ARG2 (s20h2 / high-02
                            :ARG1 s20s2)
                        :ARG3 (s20m2 / more)))
                :aspect state)
            :ARG3 (s20f / few))
        :aspect state
        :quote s20s)
    :aspect state)

# alignment:
s20s: 36-37
s20p2: 38-40
s20n: 38-40
s20h3: 0-0
s20a2: 51-53
s20n2: 51-53
s20a3: 48-50
s20n3: 48-50
s20p3: 43-43
s20p: 45-45
s20i2: 0-0
s20c: 2-2
s20n4: 2-2
s20n5: 9-9
s20i3: 0-0
s20n6: 9-9
s20i: 8-8
s20r: 18-18
s20f2: 26-26
s20s3: 21-21
s20r2: 25-25
s20n7: 23-23
s20c4: 32-32
s20a: 34-34
s20c3: 29-29
s20s2: 13-13,16-16
s20h: 0-0
s20h2: 15-15
s20m2: 15-15
s20f: 7-7

# document level annotation:
(s20s0 / sentence
    :coref ((s20c3 :same-entity s19c3))
    :temporal ((document-creation-time :contains s20s)
            (s20s :contains s20i2)
            (s20s :contains s20r))
    :modal ((root :modal author)
            (author :full-affirmative s20s)
            (author :full-affirmative s20p2)
            (s20p2 :full-negative s20r)
            (s20p2 :full-affirmative s20i2)))

## english_umr-0033, sentence 17

# :: snt17
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      
Words: I       realise that    and     sounds  like    you     do      too     but     it      doesn't make    it      any     easier. 

# sentence level graph:
(s17a / and
      :op1 (s17r / realize-01
                 :ARG0 (s17i / i)
                 :ARG1 (s17t / that))
      :op2 (s17s / sound-01
                 :ARG1 (s17r2 / realize-01
                              :ARG0 (s17y / you)
                              :ARG1 s17t
                              :mod (s17t2 / too))
                 :ARG3 s17i)
      :concession-of (s17m / make-02
                           :ARG1 (s17e / easy-05
                                       :ARG1 (s17i2 / it)
                                       :mod (s17a2 / any)
                                       :ARG2-of (s17h / have-degree-91
                                                      :ARG1 s17i2
                                                      :ARG3 (s17m2 / more)))
                           :ARG0 s17a
                           :polarity -))

# alignment:

# document level annotation:

## english_umr-0178, sentence 26

# :: snt26
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          
Words: One         thing       I           would       like        to          mention,    that        I           hope        John        finds       useful      in          his         quest       to          unravel     this        mystery,    is          that        based       upon        my          own         experiences with        these       creatures,  I           believe     that        John's      encounter   involved    not         one,        but         two         creatures.  

# sentence level graph:
(s26t2 / thing
       :ARG1-of (s26m / mention-01
                      :ARG0 (s26i / i)
                      :ARG1-of (s26l / like-02
                                     :ARG0 s26i))
       :ARG1-of (s26u / useful-05
                      :ARG0 (s26p / person
                                  :name (s26n / name
                                              :op1 "John")
                                  :wiki -)
                      :ARG2 (s26q / quest-01
                                  :ARG0 s26p
                                  :ARG1 (s26u2 / unravel-01
                                               :ARG0 s26p
                                               :ARG1 (s26m2 / mystery
                                                            :mod (s26t3 / this))))
                      :ARG1-of (s26h2 / hope-01
                                      :ARG0 s26i))
       :domain (s26b / believe-01
                     :ARG0 s26i
                     :ARG1 (s26c / contrast-91
                                 :ARG1 (s26i2 / involve-01
                                              :ARG1 (s26c2 / creature
                                                           :quant 1)
                                              :ARG2 (s26e / encounter-01
                                                          :ARG0 s26p)
                                              :polarity -)
                                 :ARG2 (s26i3 / involve-01
                                              :ARG1 (s26c3 / creature
                                                           :quant 2)
                                              :ARG2 s26e))
                     :ARG1-of (s26b2 / base-02
                                     :ARG2 (s26e2 / experience-01
                                                  :ARG0 s26i
                                                  :ARG1 (s26c4 / creature
                                                               :mod (s26t / this)))))
       :quant 1)

# alignment:

# document level annotation:

## english_umr-0321, sentence 2

# :: snt2
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       
Words: ok,      we're    going    to       start    building this     from     the      edge     of       this     grid     that     you're   at       

# sentence level graph:
(s2a / and
     :op1 (s2o / okay-04)
     :op2 (s2s / start-01
               :ARG0 (s2w / we)
               :ARG2 (s2b / build-01
                          :ARG0 s2w
                          :ARG1 (s2t3 / thing
                                      :mod (s2t / this))
                          :source (s2e / edge
                                       :part-of (s2g / grid
                                                     :mod (s2t2 / this))
                                       :place-of (s2y / you)))))

# alignment:

# document level annotation:

## english_umr-0031, sentence 10

# :: snt10
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       
Words: I'm      not      going    to       pass     my       A2       exams,   I've     already  accepted defeat,  that     this     year     of       my       life     is       going    to       make     me       a        failure. 

# sentence level graph:
(s10a / and
      :op1 (s10p / pass-07
                 :ARG1 (s10i / i)
                 :ARG2 (s10e / exam
                             :name (s10n / name
                                         :op1 "A2")
                             :possessor s10i
                             :wiki -)
                 :polarity -)
      :op2 (s10a2 / accept-01
                  :ARG0 s10i
                  :ARG1 (s10a3 / and
                               :op1 (s10d / defeat-01
                                          :ARG1 s10i)
                               :op2 (s10m / make-02
                                          :ARG0 (s10y / year
                                                      :mod (s10t / this)
                                                      :part-of (s10l / live-01
                                                                     :ARG0 s10i))
                                          :ARG1 (s10f / fail-01
                                                      :ARG1 s10i)))
                  :temporal (s10a4 / already)))

# alignment:

# document level annotation:

## english_umr-0204, sentence 17

# :: snt17
Index: 1            2            3            4            5            6            7            8            9            10           11           12           13           14           15           16           17           18           19           20           21           22           23           24           25           26           27           28           29           30           31           32           33           34           35           36           37           38           39           40           41           42           43           44           45           46           47           48           49           50           51           52           
Words: My           Drawing      Number       Two          looked       like         this         :            The          grown        -            ups          '            response     ,            this         time         ,            was          to           advise       me           to           lay          aside        my           drawings     of           boa          constrictors ,            whether      from         the          inside       or           the          outside      ,            and          devote       myself       instead      to           geography    ,            history      ,            arithmetic   and          grammar      .            

# sentence level graph:
(s17a6 / and
       :op1 (s17l / look-02
                  :ARG0 (s17w / work-of-art
                              :name (s17n / name
                                          :op1 "Drawing"
                                          :op2 "Number"
                                          :op3 "Two")
                              :possessor (s17p / person
                                               :refer-person 1st
                                               :refer-number singular)
                              :wiki -)
                  :ARG1 (s17t2 / this)
                  :aspect state
                  :modal-strength full-affirmative)
       :op2 (s17r / respond-01
                  :ARG0 (s17p2 / person
                               :age (s17g / grow-up-04)
                               :refer-number plural)
                  :ARG1 s17p
                  :ARG2 (s17a / advise-01
                              :ARG0 s17p2
                              :ARG1 s17p
                              :ARG2 (s17a3 / and
                                           :op1 (s17l2 / lay-01
                                                       :ARG0 s17p
                                                       :ARG1 (s17t / thing
                                                                   :ARG1-of (s17d2 / draw-01
                                                                                   :ARG0 s17p
                                                                                   :topic (s17b2 / boa
                                                                                                 :mod (s17c2 / constrictor))
                                                                                   :source (s17o / or
                                                                                                 :op1 (s17i2 / inside-01
                                                                                                             :ARG2 s17b2)
                                                                                                 :op2 (s17o2 / out-06
                                                                                                             :ARG2 s17b2)))
                                                                   :refer-number plural)
                                                       :ARG2 (s17a2 / aside)
                                                       :aspect performance
                                                       :modal-strength full-affirmative)
                                           :op2 (s17d3 / devote-01
                                                       :ARG0 s17p
                                                       :ARG1 s17p
                                                       :ARG2 (s17a4 / and
                                                                    :op1 (s17g2 / geography)
                                                                    :op2 (s17h / history)
                                                                    :op3 (s17a5 / arithmetic)
                                                                    :op4 (s17g3 / grammar))))
                              :quote s17a
                              :aspect performance
                              :modal-strength full-affirmative)
                  :temporal (s17t4 / time
                                   :mod (s17t5 / this))
                  :aspect performance
                  :modal-strength full-affirmative))

# alignment:

# document level annotation:

## english_umr-0054, sentence 7

# :: snt7
Index: 1      2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     
Words: I      don't  know   what   God    thinks about  it     and    will   not    lie    and    tell   you    I      do     know.  

# sentence level graph:
(s7a / and
     :op1 (s7k2 / know-01
                :ARG0 (s7i2 / i)
                :ARG1 (s7t / thing
                           :ARG1-of (s7t2 / think-01
                                          :ARG0 (s7p / person
                                                     :name (s7n / name
                                                                :op1 "God")
                                                     :wiki "God")
                                          :ARG2 (s7i3 / it)))
                :polarity -)
     :op2 (s7a2 / and
                :op1 (s7l / lie-08
                          :ARG0 s7i2
                          :polarity -)
                :op2 (s7t3 / tell-01
                           :ARG0 s7i2
                           :ARG1 (s7k3 / know-01
                                       :ARG0 s7i2)
                           :ARG2 (s7y2 / you))))

# alignment:

# document level annotation:

## english_umr-0171, sentence 6

# :: snt6
Index: 1     2     3     4     5     6     
Words: I     don't think that  will  fly.  

# sentence level graph:
(s6t / think-01
     :ARG0 (s6i / i)
     :ARG1 (s6f / fly-01
                :ARG1 (s6t2 / that))
     :polarity -)

# alignment:

# document level annotation:

## english_umr-0580, sentence 32

# :: snt32
Index: 1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    
Words: they  don't e     .     .     I     don't think they  even  look  at    each  other ,     

# sentence level graph:
(s32t / think-01
  :ARG0 (s32p3 / person
	  :refer-person 1st
	  :refer-number singular)
  :ARG1 (s32l / look-01
	  :polarity -
	  :ARG0 (s32p / person
                :refer-person 3rd
                :refer-number plural)
	  :ARG1 s32p
	  :mod (s32e / even)
	  :aspect performance
	  :modal-predicate s32t)
  :aspect state)

# alignment:
s32t: 8-8
s32p3: 6-6
s32l: 11-11
s32p: 0-0
s32e: 10-10

# document level annotation:
(s32s0 / sentence
  :temporal ((s30c :overlap s32l))
  :modal ((root :modal author)
	  (author :neutral-negative s32l))
  :coref ((s31p :same-entity s32p)
	  (s14p :same-entity s32p3)))

## english_umr-0027, sentence 5

# :: snt5
Index: 1         2         3         4         5         6         
Words: What      court     can       review    that      decision? 

# sentence level graph:
(s5p / possible-01
     :ARG1 (s5r / review-01
                :ARG0 (s5c / court
                           :mod (s5a / umr-unknown))
                :ARG1 (s5t / thing
                           :ARG1-of (s5d / decide-01))))

# alignment:

# document level annotation:

## english_umr-0141, sentence 20

# :: snt20
Index: 1              2              3              4              5              6              7              8              9              10             11             12             13             
Words: This           represents     a              significant    implicit       policy         decision       with           enormous       distributional and            political      consequences.  

# sentence level graph:
(s20r / represent-01
      :ARG0 (s20t / this)
      :ARG1 (s20d / decide-01
                  :ARG3 (s20p / policy-01
                              :mod (s20i / implicit)
                              :ARG1-of (s20s / significant-02))
                  :ARG1-of (s20c2 / consequence-03
                                  :mod (s20e / enormous)
                                  :mod (s20d2 / distribute-01)
                                  :mod (s20p2 / politics))))

# alignment:

# document level annotation:

## english_umr-0153, sentence 3

# :: snt3
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        
Words: Nobody    would     defend    the       decency   of        his       decision  to        do        that      ,         including me        .         

# sentence level graph:
(s3d / defend-01
     :ARG0 (s3p / person
                :mod (s3a / all)
                :ARG2-of (s3i2 / include-91
                               :ARG1 (s3p2 / person
                                           :refer-person 1st
                                           :refer-number singular))
                :refer-person 3rd
                :refer-number plural)
     :ARG1 (s3d2 / decent-03
                 :ARG2 (s3d3 / decide-01
                             :ARG0 (s3p3 / person
                                         :refer-person 3rd
                                         :refer-number singular)
                             :ARG1 (s3d4 / do-02
                                         :ARG0 s3p3
                                         :ARG1 (s3t / thing
                                                    :mod (s3t2 / that))
                                         :aspect process
                                         :modal-strength full-affirmative)
                             :aspect performance
                             :modal-strength full-affirmative)
                 :aspect state
                 :modal-strength full-affirmative)
     :polarity -
     :aspect state
     :modal-strength full-negative)

# alignment:

# document level annotation:

## english_umr-0039, sentence 16

# :: snt16
Index: 1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18        19        20        21        22        23        24        25        26        27        28        29        30        
Words: For       non-EU    migrants  and       those     seeking   to        live      in        the       country,  the       support   and       resources to        enable    decisions on        their     future    to        be        made      in        a         short     period    of        time.     

# sentence level graph:
(s16b / benefit-01
      :ARG0 (s16a / and
                  :op1 (s16s2 / support-01)
                  :op2 (s16r / resource)
                  :ARG0-of (s16e / enable-01
                                 :ARG1 (s16d / decide-01
                                             :ARG3 (s16f / future
                                                         :possessor (s16a2 / and
                                                                           :op1 (s16p2 / person
                                                                                       :ARG0-of (s16m2 / migrate-01)
                                                                                       :mod (s16i / international-organization
                                                                                                  :name (s16n / name
                                                                                                              :op1 "EU")
                                                                                                  :polarity -
                                                                                                  :wiki "European_Union"))
                                                                           :op2 (s16p3 / person
                                                                                       :ARG0-of (s16s3 / seek-01
                                                                                                       :ARG1 (s16l / live-01
                                                                                                                   :ARG0 s16p3
                                                                                                                   :place (s16c / country))))))
                                             :temporal (s16a3 / after
                                                              :op1 (s16n2 / now)
                                                              :quant (s16p / period
                                                                           :duration (s16s / short-07))))))
      :ARG1 s16a2)

# alignment:

# document level annotation:

## english_umr-0055, sentence 3

# :: snt3
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21       22       23       24       25       26       27       28       29       30       31       32       33       34       
Words: The      people   who      control  commerce have     made     the      decision that     the      middle   class    made     too      much     money    back     in       the      1980's   and      they     didn't   have     enough   to       buy      all      the      Polo     Ponies   they     wanted.  

# sentence level graph:
(s3d2 / decide-01
      :ARG0 (s3p / person
                 :ARG0-of (s3c / control-01
                               :ARG1 (s3c2 / commerce)))
      :ARG1 (s3a / and
                 :op1 (s3m2 / make-05
                            :ARG0 (s3c3 / class
                                        :mod (s3m3 / middle))
                            :ARG1 (s3m4 / money
                                        :ARG1-of (s3h / have-quant-91
                                                      :ARG2 (s3m5 / much)
                                                      :ARG3 (s3t2 / too)))
                            :temporal (s3b / before)
                            :temporal (s3d3 / date-entity
                                            :decade 1980))
                 :op2 (s3h2 / have-03
                            :ARG0 s3p
                            :ARG1-of (s3h3 / have-quant-91
                                           :ARG3 (s3e / enough)
                                           :ARG6 (s3b2 / buy-01
                                                       :ARG0 s3p
                                                       :ARG1 (s3a2 / animal
                                                                   :name (s3n / name
                                                                              :op1 "Polo"
                                                                              :op2 "Pony")
                                                                   :ARG1-of (s3w / want-01
                                                                                 :ARG0 s3p)
                                                                   :mod (s3a3 / all)
                                                                   :wiki -)))
                            :polarity -)))

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

## english_umr-0032, sentence 30

# :: snt30
Index: 1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      
Words: I'm     17      I       started self    harming last    year,   mainly  cutting my      arms,   but     I       have    stopped since   the     last    few     months, 

# sentence level graph:
(s30c / contrast-91
      :ARG1 (s30a / and
                  :op1 (s30a2 / age-01
                              :ARG1 (s30i / i
                                          :part (s30a3 / arm))
                              :ARG2 (s30t2 / temporal-quantity
                                           :unit (s30y / year)
                                           :quant 17))
                  :op2 (s30s / start-01
                             :ARG0 s30i
                             :ARG1 (s30h / harm-01
                                         :ARG1 (s30s2 / self)
                                         :ARG1-of (s30m / mean-91
                                                        :ARG2 (s30c2 / cut-01
                                                                     :ARG1 s30a3
                                                                     :mod (s30m3 / main))))
                             :temporal (s30y2 / year
                                              :mod (s30l / last))))
      :ARG2 (s30s3 / stop-01
                   :ARG0 s30i
                   :ARG1 s30h
                   :temporal (s30b / before
                                   :op1 (s30n / now)
                                   :quant (s30f / few
                                                :op1 (s30t3 / temporal-quantity
                                                            :unit (s30m4 / month)
                                                            :quant 1)))))

# alignment:

# document level annotation:

## english_umr-0256, sentence 103

# :: snt103
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          
Words: <Architect> the         last        one         is          suspended   in          the         air         so          put         1           placeholder on          the         back        of          the         last        piece       

# sentence level graph:
(s103s / suspend-02
       :ARG1 (s103o / one
                    :ord (s103o2 / ordinal-entity
                                 :value "-1"))
       :place (s103a / air)
       :ARG0-of (s103c / cause-01
                       :ARG1 (s103p / put-01
                                    :ARG0 (s103y / you)
                                    :ARG1 (s103t / thing
                                                 :ARG0-of (s103h / hold-01
                                                                 :ARG1 (s103p2 / place))
                                                 :quant 1)
                                    :ARG2 (s103s2 / space
                                                  :ARG1-of (s103b / back-12
                                                                  :ARG2 (s103p3 / piece
                                                                                :ord (s103o4 / ordinal-entity
                                                                                             :value "-1"))
                                                                  :ARG3 (s103c2 / cartesian-framework-91
                                                                                :FR (s103i2 / intrinsic))))
                                    :mode imperative)))

# alignment:

# document level annotation:

## english_umr-0202, sentence 2

# :: snt2
Index: 1              2              3              4              5              6              7              8              9              10             11             12             13             14             15             16             17             18             19             20             21             22             23             24             25             26             27             28             29             30             31             32             33             34             35             36             37             38             39             40             41             42             43             44             45             46             47             48             49             50             51             52             53             54             55             56             57             58             59             60             61             62             63             64             65             66             67             68             69             
Words: Although       the            distribution   system         of             the            new            legislative    power          in             Iraq           had            generally      taken          care           of             the            interests      of             all            parties        ,              and            found          a              relatively     reasonable     balance        point          among          all            ethnic         groups         and            sects          --             otherwise      a              management     committee      ,              the            interim        constitution   ,              and            the            current        interim        government     would          not            have           been           successfully   generated      --             this           does           not            mean           that           there          were           no             contradictions among          them           .              

# sentence level graph:
(s2a6 / and
      :op1 (s2h / have-concession-91
                :ARG2 (s2a / and
                           :op1 (s2c / care-03
                                     :ARG0 (s2s / system
                                                :mod (s2d / distribute-01)
                                                :possessor (s2p2 / power
                                                                 :ARG1-of (s2n / new-01)
                                                                 :instrument-of (s2l / legislate-01)
                                                                 :place (s2c3 / country
                                                                              :name (s2n2 / name
                                                                                          :op1 "Iraq")
                                                                              :wiki "Iraq")))
                                     :ARG1 (s2t2 / thing
                                                 :ARG2-of (s2i / interest-01
                                                               :ARG1 (s2p / party
                                                                          :mod (s2a2 / all))))
                                     :manner (s2g / general-02))
                           :op2 (s2f / find-01
                                     :ARG0 s2s
                                     :ARG1 (s2p3 / point
                                                 :mod (s2b / balance-01
                                                           :ARG1 (s2a3 / and
                                                                       :op1 (s2e / ethnic-group)
                                                                       :op2 (s2s2 / sect)
                                                                       :mod (s2a4 / all)))
                                                 :ARG1-of (s2r / reasonable-02
                                                               :ARG2-of (s2r2 / relative-05))))))
      :op2 (s2g3 / generate-01
                 :ARG1 (s2a5 / and
                             :op1 (s2c4 / committee
                                        :ARG0-of (s2m2 / manage-01))
                             :op2 (s2c5 / constitution
                                        :mod (s2i2 / interim))
                             :op3 (s2g4 / government-organization
                                        :ARG0-of (s2g5 / govern-01
                                                       :temporal (s2c6 / current))
                                        :mod s2i2))
                 :ARG1-of (s2s3 / succeed-01)
                 :condition (s2h2 / have-polarity-91
                                  :ARG1 s2a
                                  :ARG2 -)
                 :polarity -)
      :ARG1-of (s2m / mean-01
                    :ARG2 (s2c2 / contradict-01
                                :ARG0 s2a3
                                :polarity -)
                    :polarity -))

# alignment:

# document level annotation:

## english_umr-0038, sentence 56

# :: snt56
Index: 1         2         3         4         5         6         7         8         9         10        11        12        
Words: How       about     a         doctor    or        nurse     that      doesn't   actually  have      any       patients? 

# sentence level graph:
(s56h / have-03
      :ARG0 (s56o / or
                  :op1 (s56d / doctor)
                  :op2 (s56n / nurse))
      :ARG1 (s56p / person
                  :mod (s56a / any)
                  :ARG1-of (s56h2 / have-rel-role-92
                                  :ARG2 s56o
                                  :ARG3 (s56p2 / patient)))
      :ARG1-of (s56a3 / actual-02)
      :polarity (s56a2 / umr-unknown)
      :polarity -)

# alignment:

# document level annotation:

## english_umr-0219, sentence 1210

# :: snt1210
Index: 1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       
Words: You      need     only     swallow  one      pill     a        week     ,        and      you      would    feel     no       need     of       anything to       drink    .        

# sentence level graph:
(s1210c / cause-01
        :ARG0 (s1210n / need-01
                      :ARG0 (s1210y / you)
                      :ARG1 (s1210s / swallow-01
                                    :ARG1 (s1210r / rate-entity-91
                                                  :ARG1 (s1210p / pill
                                                                :quant 1)
                                                  :ARG3 (s1210t / temporal-quantity
                                                                :unit (s1210w / week)
                                                                :quant 1)))
                      :mod (s1210o / only))
        :ARG1 (s1210f / feel-01
                      :ARG0 s1210y
                      :ARG1 (s1210n2 / need-01
                                     :ARG0 s1210y
                                     :ARG1 (s1210d / drink-01
                                                   :ARG0 s1210y
                                                   :ARG1 (s1210a2 / anything)))
                      :polarity -))

# alignment:

# document level annotation:

## english_umr-0211, sentence 930

# :: snt930
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          22          23          24          25          26          27          28          29          30          31          32          33          34          35          36          37          38          39          40          41          42          43          44          45          46          47          48          49          50          51          
Words: Only        the         man         who         was         in          charge      of          the         single      lamp        at          the         North       Pole        ,           and         his         colleague   who         was         responsible for         the         single      lamp        at          the         South       Pole        -           -           only        these       two         would       live        free        from        toil        and         care        :           they        would       be          busy        twice       a           year        .           

# sentence level graph:
(s930l / live-01
       :ARG0 (s930a2 / and
                     :op1 (s930m / man
                                 :ARG1-of (s930c4 / charge-05
                                                  :ARG2 (s930l2 / lamp
                                                                :ARG1-of (s930s / single-02)
                                                                :place (s930w / world-region
                                                                              :name (s930n3 / name
                                                                                            :op1 "North"
                                                                                            :op2 "Pole")
                                                                              :wiki "North_Pole")))
                                 :mod (s930o / only))
                     :op2 (s930c3 / colleague
                                  :possessor s930m
                                  :ARG0-of (s930r / responsible-03
                                                  :ARG1 (s930l4 / lamp
                                                                :ARG1-of (s930s2 / single-02))
                                                  :place (s930w2 / world-region
                                                                 :name (s930n / name
                                                                              :op1 "South"
                                                                              :op2 "Pole")
                                                                 :wiki "South_Pole")))
                     :mod (s930p / person
                                 :mod (s930t4 / this)
                                 :mod (s930o2 / only)
                                 :quant 2))
       :ARG3-of (s930f / free-04
                       :ARG1 s930a2
                       :ARG2 (s930a / and
                                    :op1 (s930t / toil-01)
                                    :op2 (s930c / care-01)))
       :ARG1-of (s930c2 / cause-01
                        :ARG0 (s930b / busy-01
                                     :ARG1 s930a2
                                     :frequency (s930r2 / rate-entity-91
                                                        :ARG2 (s930t3 / temporal-quantity
                                                                      :unit (s930y / year)
                                                                      :quant 1)
                                                        :ARG1 2))))

# alignment:

# document level annotation:

## english_umr-0378, sentence 4

# :: snt4
Index: 1           2           3           4           5           6           
Words: <Architect> you'll      need        only        green       blocks.     

# sentence level graph:
(s4n / need-01
     :ARG0 (s4y / you)
     :ARG1 (s4b / block
                :color (s4g / green)
                :mod (s4o / only)
                :refer-number plural))

# alignment:

# document level annotation:

## english_umr-0304, sentence 83

# :: snt83
Index: 1           2           3           4           5           6           7           
Words: <Architect> this        looks       like        a           narrow      staircase   

# sentence level graph:
(s83l / look-02
      :ARG0 (s83t / this)
      :ARG1 (s83s / staircase
                  :ARG1-of (s83n / narrow-02)))

# alignment:

# document level annotation:

## english_umr-0472, sentence 38

# :: snt38
Index: 1            2            3            4            5            6            
Words: <Builder>    diagonal     staircase    with         this         orientation? 

# sentence level graph:
(s38s / staircase
      :ARG1-of (s38d / diagonal-02)
      :orientation (s38t / this)
      :ARG1-of (s38r / request-confirmation-91))

# alignment:

# document level annotation:

## english_umr-0248, sentence 4

# :: snt4
Index: 1           2           3           4           5           6           7           8           9           
Words: <Architect> alright     this        thing       looks       like        an          artistic    staircase   

# sentence level graph:
(s4a / and
     :op1 (s4a2 / all-right)
     :op2 (s4l / look-02
               :ARG0 (s4t / thing
                          :mod (s4t2 / this))
               :ARG1 (s4s / staircase
                          :mod (s4a3 / artistic))))

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

## english_umr-0201, sentence 5

# :: snt5
Index: 1             2             3             4             5             6             7             8             9             10            11            12            13            14            15            16            17            18            19            20            21            22            23            24            25            26            27            28            29            30            31            32            33            34            35            36            37            38            39            40            41            42            43            44            45            46            47            48            49            50            51            52            53            54            55            56            57            58            59            60            61            62            63            64            65            66            
Words: Others        may           agree         with          him           ,             or            they          may           accept        some          parts         while         disagreeing   with          other         parts         ,             or            in            the           future        we            might         discover      that          the           general       direction     of            Darwin        's            evolution     is            largely       correct       though        filled        with          a             lot           of            errors        ,             and           that          there         might         be            an            improved      version       of            evolution     which         is            more          accurate      and           comprehensive than          what          Darwin        had           proposed      .             

# sentence level graph:
(s5p2 / possible-01
      :ARG1 (s5o / or
                 :op1 (s5a / agree-01
                           :ARG0 (s5o2 / other)
                           :ARG2 (s5h / he))
                 :op2 (s5c / contrast-91
                           :ARG1 (s5a2 / accept-01
                                       :ARG0 s5o2
                                       :ARG1 (s5p3 / part
                                                   :mod (s5s / some)))
                           :ARG2 (s5d3 / disagree-01
                                       :ARG0 s5o2
                                       :ARG2 (s5p4 / part
                                                   :mod (s5o3 / other))))
                 :op3 (s5d2 / discover-01
                            :ARG0 (s5w / we)
                            :ARG1 (s5a3 / and
                                        :op1 (s5c2 / correct-02
                                                   :ARG1 (s5d4 / direction
                                                               :ARG1-of (s5g / general-02)
                                                               :possessor (s5e / evolve-02
                                                                               :mod (s5p6 / person
                                                                                          :name (s5n / name
                                                                                                     :op1 "Darwin")
                                                                                          :wiki "Charles_Darwin")))
                                                   :concession (s5f / fill-01
                                                                    :ARG1 s5d4
                                                                    :ARG2 (s5e2 / error
                                                                                :quant (s5l2 / lot)))
                                                   :degree (s5l / large))
                                        :op2 (s5p5 / possible-01
                                                   :ARG1 (s5v / version
                                                              :mod (s5e3 / evolve-02)
                                                              :ARG1-of (s5i / improve-01)
                                                              :ARG1-of (s5h2 / have-degree-91
                                                                             :ARG2 (s5a4 / and
                                                                                         :op1 (s5a5 / accurate)
                                                                                         :op2 (s5c3 / comprehensive))
                                                                             :ARG3 (s5m / more)
                                                                             :ARG4 (s5t / thing
                                                                                        :ARG1-of (s5p7 / propose-01
                                                                                                       :ARG0 s5p6))))))
                            :temporal (s5f2 / future))))

# alignment:

# document level annotation:

## english_umr-0520, sentence 19

# :: snt19
Index: 1           2           3           4           5           6           7           8           9           10          11          12          13          14          15          16          17          18          19          20          21          
Words: <Architect> Okay        cool.       Now         two         more        blue        blocks      in          a           diagonal    line        from        that        block,      toward      where       you         are         right       now         

# sentence level graph:
(s19a2 / and
      :op1 (s19a / and
                  :op1 (s19o / okay-04)
                  :op2 (s19c / cool-04))
      :op2 (s19b / be-destined-for-91
                  :ARG1 (s19b2 / block
                               :color (s19b3 / blue)
                               :mod (s19m2 / more)
                               :quant 2)
                  :ARG2 (s19s / space
                              :configuration (s19l / line
                                                   :ARG4-of (s19t2 / toward-01
                                                                   :ARG2 (s19s2 / space
                                                                                :place-of (s19y / you)
                                                                                :temporal (s19n2 / now
                                                                                                 :mod (s19r / right-yy))))
                                                   :ARG1-of (s19d / diagonal-02)
                                                   :source (s19b4 / block
                                                                  :mod (s19t / that)))
                              :refer-number plural)
                  :temporal (s19n / now)))

# alignment:

# document level annotation:
