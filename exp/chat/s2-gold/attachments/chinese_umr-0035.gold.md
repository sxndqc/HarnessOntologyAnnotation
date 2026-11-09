# Gold UMR annotations of sentences like those of chinese_umr-0035

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0001, sentence 50

# :: snt50
Index: 1 2  3  4 5  6  7 8  9  10 11 12 13 14 15 16 17 18 19  20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38
Words: 《 时代 商报 》 引用 报导 ， 美国 总统 布什 因为 美国 国债 数字 庞大 ，  要  把  夏威夷 卖  给  日本 还债 ，  新闻 并  置于 该报 的  头版 ，  许多 网络 媒体 也  跟进 报导 。 

# sentence level graph:
(s50a / and
    :op1 (s50x / 引用-01
        :ARG0 (s50n / newspaper
            :name (s50n2 / name
                :op1 "《"
                :op2 "时代"
                :op3 "商报"
                :op4 "》"))
        :ARG1 (s50x4 / 报导-01
            :ARG1 (s50h / have-reason-91
                :ARG1 (s50x5 / 卖-01
                    :ARG0 (s50i3 / individual-person
                        :name (s50n6 / name
                            :op1 "布什")
                        :ARG1-of (s50h2 / have-org-role-91
                            :ARG2 (s50c2 / country
                                :name (s50n5 / name
                                    :op1 "美国"))
                            :ARG3 (s50x7 / 总统)))
                    :ARG1 (s50s / state
                        :name (s50n4 / name
                            :op1 "夏威夷"))
                    :ARG2 (s50c / country
                        :name (s50n3 / name
                            :op1 "日本"))
                    :quote s50x4
                    :aspect process
                    :purpose (s50x6 / 还债-01
                        :quote s50x4
                        :aspect process))
                :ARG2 (s50x15 / 庞大-01
                    :ARG0 (s50x16 / 数字
                        :topic (s50x17 / 国债
                            :possessor (s50c3 / country
                                :name (s50n7 / name
                                    :op1 "美国"))))))
            :aspect performance)
        :aspect performance)
    :op2 (s50x2 / 置-01
        :ARG1 (s50x8 / 新闻)
        :ARG2 (s50x9 / 头版
            :part s50n)
        :aspect state)
    :op3 (s50x3 / 跟进-02
        :ARG0 (s50x12 / 媒体
            :medium (s50x13 / 网络)
            :quant (s50x14 / 许多))
        :ARG1 (s50x10 / 报导-01
            :aspect performance)
        :mod (s50x11 / 也)
        :aspect performance))


# alignment:
s50a: 0-0
s50c: 0-0
s50c2: 0-0
s50c3: 0-0
s50h: 0-0
s50h2: 0-0
s50i3: 0-0
s50n: 0-0
s50n2: 0-0
s50n3: 0-0
s50n4: 0-0
s50n5: 0-0
s50n6: 0-0
s50n7: 0-0
s50s: 0-0
s50x: 5-5
s50x10: 6-6
s50x11: 35-35
s50x12: 34-34
s50x13: 33-33
s50x14: 32-32
s50x15: 15-15
s50x16: 14-14
s50x17: 13-13
s50x2: 27-27
s50x3: 36-36
s50x4: 6-6
s50x5: 20-20
s50x6: 23-23
s50x7: 9-9
s50x8: 25-25
s50x9: 30-30

# document level annotation:
(s50s0 / sentence
    :temporal ((document-creation-time :before s50x)
        (s50x :before s50x4)
        (s50x4 :overlap s50x5)
        (s50x5 :overlap s50x6)
        (s50x :after s50x3)
        (s50x3 :overlap s50x10))
    :modal ((root :modal author)
        (s50n :partial-affirmative s50x5)
        (author :partial-affirmative s50x6)
        (author :partial-affirmative s50n)
        (author :full-affirmative s50x4)
        (author :full-affirmative s50n)
        (author :full-affirmative s50x)
        (author :full-affirmative s50n)
        (author :full-affirmative s50x2)
        (author :full-affirmative s50n)
        (author :full-affirmative s50x10)
        (author :full-affirmative s50n)
        (author :full-affirmative s50x3)
        (author :full-affirmative s50n)))

## chinese_umr-0001, sentence 51

# :: snt51
Index: 1   2 3 4  5  6 7 8 9  10  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27  28 29 30 31 32 33 34   35 36 37 38 39  40 41 42 43  44
Words: 新华网 、 《 东森 新闻 报 》 、 中央 电视台 网站 等  引用 报导 ，  形容 了  美国 白宫 安全 官员 开除 了  一  年轻 女  实习生 ，  因为 她  进入 白宫 引诱 布什总统 ，  而  幕后 的  操作者 可能 是  美国 民主党 。 

# sentence level graph:
(s51x / 引用-01
    :ARG0 (s51a / and
        :op1 (s51n / newspaper
            :name (s51n2 / name
                :op1 "新华网"))
        :op2 (s51n3 / newspaper
            :name (s51n4 / name
                :op1 "《"
                :op2 "东森"
                :op3 "新闻"
                :op4 "报"
                :op5 "》"))
        :op3 (s51n5 / newspaper
            :name (s51n6 / name
                :op1 "中央"
                :op2 "电视台"
                :op3 "网站"))
        :op4 (s51x2 / 等))
    :ARG1 (s51x3 / 报导-01
        :ARG0-of (s51x4 / 形容-01
            :ARG1 (s51h / have-reason-91
                :ARG1 (s51x5 / 开除-01
                    :ARG0 (s51x9 / 官员
                        :mod (s51x10 / 安全)
                        :place (s51b / building
                            :name (s51n7 / name
                                :op1 "白宫")
                            :place (s51c / country
                                :name (s51n8 / name
                                    :op1 "美国"))))
                    :ARG1 (s51x6 / 实习生
                        :mod (s51x7 / 女)
                        :mod (s51x8 / 年轻)
                        :quant 1)
                    :aspect performance
                    :quote s51x3)
                :ARG2 (s51a2 / and
                    :op1 (s51x11 / 进入-01
                        :ARG0 s51x6
                        :ARG1 s51b
                        :purpose (s51x12 / 引诱-01
                            :ARG0 s51x6
                            :ARG1 (s51i3 / individual-person
                                :name (s51n9 / name
                                    :op1 "布什总统"))
                            :aspect process
                            :quote s51x3)
                        :aspect performance
                        :quote s51x3)
                    :op2 (s51i2 / identity-91
                        :ARG1 (s51x13 / 者
                            :ARG0-of (s51x14 / 操作-01
                                :place (s51x15 / 幕后)
                                :aspect performance))
                        :ARG2 (s51p / political-party
                            :name (s51n10 / name
                                :op1 "美国"
                                :op2 "民主党"))
                        :aspect state
                        :quote s51x3)))
            :aspect performance)
        :aspect performance)
    :aspect performance)


# alignment:
s51a: 0-0
s51a2: 0-0
s51b: 0-0
s51c: 0-0
s51h: 0-0
s51i2: 0-0
s51i3: 0-0
s51n: 0-0
s51n10: 0-0
s51n2: 0-0
s51n3: 0-0
s51n4: 0-0
s51n5: 0-0
s51n6: 0-0
s51n7: 0-0
s51n8: 0-0
s51n9: 0-0
s51p: 0-0
s51x: 13-13
s51x10: 20-20
s51x11: 31-31
s51x12: 33-33
s51x13: 39-39
s51x14: 39-39
s51x15: 37-37
s51x2: 12-12
s51x3: 14-14
s51x4: 16-16
s51x5: 22-22
s51x6: 27-27
s51x7: 26-26
s51x8: 25-25
s51x9: 21-21

# document level annotation:
(s51s0 / sentence
    :temporal ((document-creation-time :before s51x)
        (s51x :before s51x3)
        (s51x3 :overlap s51x4)
        (s51x4 :before s51x5)
        (s51x5 :before s51x11)
        (s51x11 :overlap s51x12)
        (s51x12 :before s51x14))
    :modal ((root :modal author)
        (s51a :partial-affirmative s51x5)
        (author :partial-affirmative s51x12)
        (author :partial-affirmative s51a)
        (author :partial-affirmative s51x11)
        (author :partial-affirmative s51a)
        (author :neutral-affirmative s51i2)
        (author :neutral-affirmative s51a)
        (author :full-affirmative s51x4)
        (author :full-affirmative s51a)
        (author :full-affirmative s51x3)
        (author :full-affirmative s51a)
        (author :full-affirmative s51x)
        (author :full-affirmative s51a)))

## chinese_umr-0001, sentence 41

# :: snt41
Index: 1  2  3  4  5  6  7  8 9 10 11 12  13 14 15 16 17 18 19  20 21 22 23 24 25 26 27 28  29 30 31 32
Words: 尽管 当局 认为 照片 不具 任何 意义 ， 前 美国 总统 柯林顿 仍  要求 把  照片 复制 给  葛培理 牧师 、  教宗 若望 保禄 二世 等  具  影响力 的  宗教 人物 。 

# sentence level graph:
(s41b / but-91
    :ARG1 (s41x / 要求-03
        :ARG0 (s41i2 / individual-person
            :name (s41n / name
                :op1 "柯林顿")
            :ARG1-of (s41h / have-org-role-91
                :ARG2 (s41c / country
                    :name (s41n2 / name
                        :op1 "美国"))
                :ARG3 (s41x3 / 总统
                    :mod (s41x4 / 前))))
        :ARG1 (s41c2 / consecutive
            :op1 (s41x5 / 复制-01
                :ARG1 (s41x7 / 照片)
                :aspect performance
                :quote s41i6)
            :op2 (s41x6 / 给-01
                :ARG1 s41x7
                :ARG2 (s41x8 / 人物
                    :mod (s41x9 / 宗教)
                    :ARG0-of (s41x10 / 具-01
                        :ARG1 (s41x11 / 影响力)
                        :aspect state)
                    :example (s41a / and
                        :op1 (s41i3 / individual-person
                            :name (s41n3 / name
                                :op1 "葛培理"
                                :op2 "牧师"))
                        :op2 (s41i4 / individual-person
                            :name (s41n4 / name
                                :op1 "教宗"
                                :op2 "若望"
                                :op3 "保禄"
                                :op4 "二世"))
                        :op3 (s41x12 / 等)))
                :aspect performance
                :quote s41i6))
        :aspect performance
        :quote (s41i6 / implicit-predicate))
    :ARG2 (s41x2 / 认为-01
        :ARG0 (s41x13 / 当局)
        :ARG1 (s41x14 / 具-01
            :ARG0 s41x7
            :ARG1 (s41x15 / 意义
                :mod (s41x16 / 任何))
            :aspect state
            :polarity -)
        :aspect state
        :quote s41i6))


# alignment:
s41a: 0-0
s41b: 0-0
s41c: 0-0
s41c2: 0-0
s41h: 0-0
s41i2: 0-0
s41i3: 0-0
s41i4: 0-0
s41i6: 0-0
s41n: 0-0
s41n2: 0-0
s41n3: 0-0
s41n4: 0-0
s41x: 14-14
s41x10: 27-27
s41x11: 28-28
s41x12: 26-26
s41x13: 2-2
s41x14: 27-27
s41x15: 7-7
s41x16: 6-6
s41x2: 3-3
s41x3: 11-11
s41x4: 9-9
s41x5: 17-17
s41x6: 18-18
s41x7: 4-4
s41x8: 31-31
s41x9: 30-30

# document level annotation:
(s41s0 / sentence
    :temporal ((s40x3 :overlap s41x)
        (s41x :overlap s41x5)
        (s41x5 :after s41x6)
        (s41x6 :overlap s40x10)
        (s41x :overlap s40x2)
        (s40x2 :overlap s40x14))
    :modal ((root :modal author)
        (s41i2 :partial-affirmative s41x5)
        (author :partial-affirmative s41x10)
        (author :partial-affirmative s41i2)
        (s41i2 :partial-affirmative s41x6)
        (author :partial-affirmative s41x)
        (author :partial-affirmative s41i2)
        (author :full-negative s41x14)
        (author :full-negative s41i2)
        (author :partial-affirmative s41x2)
        (author :partial-affirmative s41i2))
    :coref ((s40x38 :same-entity s41x7)
        (s40x2 :same-event s41i6)))

## chinese_umr-0002, sentence 47

# :: snt47
Index: 1  2  3 4  5 6  7  8 9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
Words: 在此 之前 ， 曼联 也 对外 声明 若 顺利 夺冠 将  不  举办 庆祝 游行 仪式 ，  此外 ，  瑞典 当地 乐团 在  获知 爆炸 事件 后  ，  决议 取消 出席 开幕 演出 ，  并  透过 声明 表示 ：  「  对  我们 而言 ，  这  不是 演出 的  时机 。  」 

# sentence level graph:
(s47a / and
    :op1 (s47x / 声明-01
        :ARG0 (s47s / sports-organization
            :name (s47n / name
                :op1 "曼联"))
        :ARG1 (s47h / have-condition-91
            :ARG1 (s47x6 / 举办-01
                :ARG0 s47s
                :ARG1 (s47x7 / 仪式
                    :mod (s47x8 / 游行-01
                        :purpose (s47x9 / 庆祝-01
                            :aspect process)
                        :aspect process))
                :aspect performance
                :polarity -)
            :ARG2 (s47x4 / 顺利-01
                :ARG0 (s47x5 / 夺冠-01
                    :ARG0 s47s
                    :aspect performance)
                :ARG0 s47s
                :aspect state))
        :aspect performance
        :temporal (s47x19 / 之前
            :op1 (s47t / thing
                :refer-number singular
                :refer-person 3rd))
        :mod (s47x23 / 也))
    :op2 (s47x2 / 决议-01
        :ARG0 (s47x12 / 乐团
            :place (s47x13 / 当地
                :op1 (s47c / country
                    :name (s47n2 / name
                        :op1 "瑞典"))))
        :ARG1 (s47x14 / 取消-01
            :ARG0 s47x12
            :ARG1 (s3x / 出席-01
                :ARG0 s47x12
                :ARG1 (s3x2 / 演出-01
                    :ARG0 s47x12
                    :mod (s3x3 / 开幕-01
                        :aspect process)
                    :aspect performance)
                :aspect performance)
            :aspect performance)
        :temporal (s47x10 / 后
            :op1 (s47x11 / 获知-01
                :ARG0 s47x12
                :ARG1 (s47x21 / 事件
                    :ARG1-of (s47i3 / identity-91
                        :ARG2 (s47x22 / 爆炸-01
                            :aspect performance)
                        :aspect state))
                :aspect performance))
        :aspect performance)
    :op3 (s47x3 / 表示-01
        :ARG1 (s47x20 / 言-01
            :ARG0 (s47i2 / identity-91
                :ARG1 (s47x18 / 这)
                :ARG2 (s47x16 / 时机
                    :temporal-of (s47x17 / 演出-01
                        :aspect process))
                :polarity -
                :aspect state
                :quote s47x3)
            :ARG1 (s47p / person
                :refer-number plural
                :refer-person 1st)
            :aspect state)
        :medium (s47x15 / 声明-01
            :ARG0 s47x12
            :aspect performance)
        :quote s47x12
        :aspect performance))


# alignment:
s3x: 31-31
s3x2: 33-33
s3x3: 32-32
s47a: 0-0
s47c: 0-0
s47h: 0-0
s47i2: 0-0
s47i3: 0-0
s47n: 0-0
s47n2: 0-0
s47p: 0-0
s47s: 0-0
s47t: 0-0
s47x: 7-7
s47x10: 27-27
s47x11: 24-24
s47x12: 22-22
s47x13: 21-21
s47x14: 30-30
s47x15: 7-7
s47x16: 49-49
s47x17: 33-33
s47x18: 45-45
s47x19: 2-2
s47x2: 29-29
s47x20: 43-43
s47x21: 26-26
s47x22: 25-25
s47x23: 5-5
s47x3: 38-38
s47x4: 9-9
s47x5: 10-10
s47x6: 13-13
s47x7: 16-16
s47x8: 15-15
s47x9: 14-14

# document level annotation:
(s47s0 / sentence
    :temporal ((s46x9 :before s47x)
        (s47x :after s47x6)
        (s47x6 :overlap s47x9)
        (s47x :after s47x4)
        (s47x4 :overlap s47x5)
        (document-creation-time :before s47x2)
        (s47x2 :overlap s47x14)
        (s47x14 :overlap s3x2)
        (s3x2 :overlap s3x3)
        (s47x2 :before s47x11)
        (s47x11 :before s47x22)
        (s47x2 :overlap s47x3)
        (s47x3 :overlap s47x18)
        (s47x3 :overlap s47x15))
    :modal ((root :modal author)
        (author :full-affirmative s47x9)
        (author :full-affirmative s47s)
        (author :full-affirmative s47x8)
        (author :full-affirmative s47s)
        (author :full-negative s47x6)
        (author :full-negative s47s)
        (author :neutral-affirmative s47x5)
        (author :neutral-affirmative s47s)
        (author :neutral-affirmative s47x4)
        (author :neutral-affirmative s47s)
        (author :full-affirmative s47x)
        (author :full-affirmative s47s)
        (author :full-affirmative s3x3)
        (author :full-affirmative s47s)
        (author :full-affirmative s3x2)
        (author :full-affirmative s47s)
        (author :full-negative s3x)
        (author :full-negative s47s)
        (s47s :full-affirmative s47x14)
        (author :full-affirmative s47x11)
        (author :full-affirmative s47s)
        (author :full-affirmative s47x2)
        (author :full-affirmative s47s)
        (author :full-negative s47x18)
        (author :full-negative s47s)
        (s47s :full-negative s47i2)
        (s47s :full-affirmative s47x15)
        (author :full-affirmative s47x3)
        (author :full-affirmative s47s)
        (author :full-affirmative s47x22)
        (author :full-affirmative s47i3))
    :coref ((s46s2 :same-entity s47s)
        (s46x9 :same-event s47x20)
        (s46x24 :same-event s47x21)))

## chinese_umr-0014, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
Words: 梵蒂冈 表示 ， 神父 可以 被 允许 在 某些 情况 下 ， 为 同性 伴侣 和 “ 非 传统 ” 伴侣 祝福 ， 但 这 不 应 成为 正式 教堂 仪式 的 一部分 ， 也 不 应 与 民事 结合 或 婚礼 联系 起来 。

# sentence level graph:
(s4x / 表示-01
	:ARG0 (s4c2 / country
		:name (s4n / name
			:op1 "梵蒂冈"))
	:ARG1 (s4b / contrast-91
		:ARG1 (s4x3 / 允许-01
			:ARG1 (s4x5 / 神父)
			:ARG2 (s4x4 / 祝福-01
				:ARG0 s4x5
				:ARG1 (s4a2 / and
					:op1 (s4x6 / 伴侣
						:mod (s4x7 / 同性))
					:op2 (s4x8 / 伴侣
						:mod (s4x9 / 非
							:mod (s4x10 / 传统))))
				:condition (s4x11 / 情况
					:mod (s4x12 / 某些))
				:aspect performance)
			:aspect state
			:modal-strength neutral-affirmative)
		:ARG2 (s4a / and
			:op1 (s4x13 / 成为-01
				:ARG0 s4x4
				:ARG1 (s4x14 / 部分
					:part-of (s4x17 / 仪式
						:mod (s4x15 / 教堂)
						:mod (s4x16 / 正式)))
				:aspect process
				:modal-strength partial-negative)
			:op2 (s4c / 联系-02
				:ARG1 (s4a4 / and
					:op1 s4x4
					:op2 (s4a3 / or
						:op1 (s4x18 / 结合-02
							:mod (s4x19 / 民事)
							:aspect state)
						:op2 (s4x20 / 婚礼)))
				:aspect state
				:modal-strength partial-negative)))
	:aspect performance)

# alignment:
s4a: 0-0
s4a2: 0-0
s4a3: 0-0
s4b: 0-0
s4c: 0-0
s4c2: 0-0
s4n: 0-0
s4x: 2-2
s4x10: 19-19
s4x11: 10-10
s4x12: 9-9
s4x13: 28-28
s4x14: 33-33
s4x15: 30-30
s4x16: 29-29
s4x17: 31-31
s4x18: 40-40
s4x19: 39-39
s4x2: 1-1
s4x20: 42-42
s4x3: 7-7
s4x4: 22-22
s4x5: 4-4
s4x6: 15-15
s4x7: 14-14
s4x8: 15-15
s4x9: 18-18

# document level annotation:
(s4s0 / sentence
    :temporal ()
    :modal ((root :modal author)
            (author :full-affirmative s4x)
            (author :full-affirmative s4c2)
            (s4c2 :neutral-affirmative s4x3)
            (s4c2 :neutral-affirmative s4x4)
            (s4c2 :partial-negative s4x13)
            (s4c2 :partial-negative s4c))
    :coref ()
)

## chinese_umr-0002, sentence 46

# :: snt46
Index: 1  2  3     4  5   6 7  8    9 10 11 12   13 14  15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43   44 45 46  47 48 49 50 51  52 53 54
Words: 当地 球会 曼彻斯特联 足球 俱乐部 与 荷兰 阿贾克斯 在 瑞典 的  2017 年  欧霸杯 决赛 开赛 前  ，  欧洲 足球 协会 为此 举办 了  默哀 仪式 ，  并  在  球场 周边 加强 安全 防护 措施 ，  且  比赛 中  ，  两队 球员 不约而同 地  系上 黑丝带 ，  表达 对此 事件 罹难者 的  哀悼 ； 

# sentence level graph:
(s46a / and
    :op1 (s46x / 举办-01
        :ARG0 (s46s / sports-organization
            :name (s46n / name
                :op1 "欧洲"
                :op2 "足球"
                :op3 "协会"))
        :ARG1 (s46x5 / 仪式
            :manner (s46x6 / 默哀-01
                :aspect performance))
        :purpose (s46x7 / 此)
        :temporal (s46x8 / 前
            :op1 (s46x9 / 开赛-01
                :ARG0 (s46g / game
                    :name (s46n2 / name
                        :op1 "欧霸杯"
                        :op2 "决赛")
                    :temporal (s46d / date-entity
                        :year 2017)
                    :place (s46c / country
                        :name (s46n3 / name
                            :op1 "瑞典"))
                    :ARG1-of (s46i5 / implicit-predicate
                        :ARG0 (s46a3 / and
                            :op1 (s46s5 / sports-organization
                                :name (s46n7 / name
                                    :op1 "曼彻斯特联"
                                    :op2 "足球"
                                    :op3 "俱乐部")
                                :ARG1-of (s46i6 / identity-91
                                    :ARG2 (s46x28 / 球会
                                        :place (s46x29 / 当地))
                                    :aspect state))
                            :op2 (s46s4 / sports-organization
                                :name (s46n6 / name
                                    :op1 "荷兰"
                                    :op2 "阿贾克斯")))))
                :aspect performance))
        :aspect performance)
    :op2 (s46x2 / 加强-01
        :ARG0 s46s
        :ARG1 (s46x10 / 措施
            :place (s46x13 / 周边
                :part-of (s46x14 / 球场))
            :ARG1-of (s46i4 / identity-91
                :ARG2 (s46x11 / 防护-01
                    :aspect performance
                    :mod (s46x12 / 安全))))
        :aspect performance)
    :op3 (s46x3 / 系上-01
        :ARG0 (s46x19 / 球员
            :part-of (s46x20 / 队
                :quant 2
                :ARG1-of (s46i2 / identity-91
                    :ARG2 (s46a2 / and
                        :op1 (s46s2 / sports-organization
                            :name (s46n4 / name
                                :op1 "曼彻斯特联"
                                :op2 "足球"
                                :op3 "俱乐部")
                            :ARG1-of (s46i3 / identity-91
                                :ARG2 (s46x26 / 球会
                                    :place (s46x27 / 当地))
                                :aspect state))
                        :op2 (s46s3 / sports-organization
                            :name (s46n5 / name
                                :op1 "荷兰"
                                :op2 "阿贾克斯")))
                    :aspect state)))
        :ARG1 (s46x17 / 丝带
            :mod (s46x18 / 黑))
        :temporal (s46x15 / 比赛-01
            :aspect performance)
        :manner (s46x16 / 不约而同)
        :aspect performance
        :purpose (s46x4 / 表达-01
            :ARG0 s46x19
            :ARG1 (s46x21 / 哀悼-01
                :ARG1 (s46x22 / 者
                    :ARG0-of (s46x23 / 罹难-01
                        :quote s46x4
                        :aspect performance
                        :cause (s46x24 / 事件
                            :mod (s46x25 / 此))))
                :quote s46x4
                :aspect performance)
            :aspect performance)))


# alignment:
s46a: 0-0
s46a2: 0-0
s46a3: 0-0
s46c: 0-0
s46d: 0-0
s46g: 0-0
s46i2: 0-0
s46i3: 0-0
s46i4: 0-0
s46i5: 0-0
s46i6: 0-0
s46n: 0-0
s46n2: 0-0
s46n3: 0-0
s46n4: 0-0
s46n5: 0-0
s46n6: 0-0
s46n7: 0-0
s46s: 0-0
s46s2: 0-0
s46s3: 0-0
s46s4: 0-0
s46s5: 0-0
s46x: 23-23
s46x10: 35-35
s46x11: 34-34
s46x12: 33-33
s46x13: 31-31
s46x14: 30-30
s46x15: 38-38
s46x16: 43-43
s46x17: 46-46
s46x18: 46-46
s46x19: 42-42
s46x2: 32-32
s46x20: 41-41
s46x21: 53-53
s46x22: 51-51
s46x23: 51-51
s46x24: 50-50
s46x25: 22-22
s46x26: 2-2
s46x27: 1-1
s46x28: 2-2
s46x29: 1-1
s46x3: 45-45
s46x4: 48-48
s46x5: 26-26
s46x6: 25-25
s46x7: 22-22
s46x8: 17-17
s46x9: 16-16

# document level annotation:
(s46s0 / sentence
    :temporal ((document-creation-time :before s46x)
        (s46x :overlap s46x6)
        (s46x :before s46x9)
        (s46x :overlap s46x2)
        (s46x2 :overlap s46x11)
        (s46x2 :overlap s46x3)
        (s46x3 :overlap s46x15)
        (s46x15 :overlap s46x4)
        (s46x4 :overlap s46x21)
        (s46x21 :before s46x23)
        (document-creation-time :before s46d))
    :modal ((root :modal author)
        (author :full-affirmative s46x6)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x9)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x11)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x2)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x15)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x3)
        (author :full-affirmative s46s)
        (s46s :full-affirmative s46x23)
        (author :full-affirmative s46x21)
        (author :full-affirmative s46s)
        (author :full-affirmative s46x4)
        (author :full-affirmative s46s)
        (author :full-affirmative s46i6)
        (author :full-affirmative s46i3)
        (author :full-affirmative s46i2))
    :coref ((s7x3 :same-event s46x23)))

## chinese_umr-0024, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 这 被 视为 政府 安抚 投资者 的 举动 ， 但 马云 回国 是否 能 恢复 企业家 们 对 中国 经济 的 信心 还 需 观察 。

# sentence level graph:
(s5b / contrast-91
	:ARG1 (s5x / 视为-01
		:ARG1 (s5x13 / 这)
		:ARG2 (s5x2 / 举动
			:purpose (s5x3 / 安抚-01
				:ARG0 (s5x4 / 政府)
				:ARG1 (s5x5 / 投资者)
				:aspect activity))
		:aspect state)
	:ARG2 (s5x6 / 观察-01
		:ARG1 (s5x8 / 恢复-02
			:ARG0 (s5x9 / 回国-01
				:ARG0 (s5i2 / individual-person
					:name (s5n / name
						:op1 "马云"))
				:aspect performance)
			:ARG1 (s5x11 / 信心
				:possessor (s5x19 / 企业家)
				:topic (s5x12 / 经济
					:possessor (s5c / country
						:name (s5n2 / name
							:op1 "中国"))))
			:mode interrogative
			:aspect performance)
		:mod (s5x17 / 还)
		:aspect activity))

# alignment:
s5b: 0-0
s5c: 0-0
s5i2: 0-0
s5n: 0-0
s5n2: 0-0
s5x: 3-3
s5x10: 11-11
s5x11: 22-22
s5x12: 20-20
s5x13: 1-1
s5x17: 23-23
s5x18: 24-24
s5x2: 8-8
s5x3: 5-5
s5x4: 4-4
s5x5: 6-6
s5x6: 25-25
s5x7: 14-14
s5x8: 15-15
s5x9: 12-12

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x)
            (s5x3 :before s5x9)
            (s5x6 :overlap s5x8)
            (s5x8 :depends-on s5x9))
    :modal ((root :modal author)
            (author :full-affirmative s5x)
            (author :full-affirmative s5x9)
            (author :unspecified s5x2)
            (author :neutral-affirmative s5x8)
            (author :partial-affirmative s5x6)
            (author :full-affirmative s5x4)
            (s5x4 :partial-affirmative purpose)
            (purpose :full-affirmative s5x3))
    :coref ()
)

## chinese_umr-0024, sentence 15

# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 这 被 视为 政府 安抚 投资者 的 举动 ， 但 马云 回国 是否 能 恢复 企业家 们 对 中国 经济 的 信心 还 需 观察 。

# sentence level graph:
(s15b / contrast-91
	:ARG1 (s15x / 视为-01
		:ARG1 (s15x6 / 这)
		:ARG2 (s15x2 / 举动
			:purpose (s15x3 / 安抚-01
				:ARG0 (s15x4 / 政府)
				:ARG1 (s15x5 / 投资者)
				:aspect activity))
		:aspect state)
	:ARG2 (s15x9 / 观察-01
		:ARG1 (s15x13 / 恢复-02
			:ARG0 (s15x12 / 回国-01
				:ARG0 (s15i2 / individual-person
					:name (s15n / name
						:op1 "马云"))
				:aspect performance)
			:ARG1 (s15x15 / 信心
				:possessor (s15x14 / 企业家
					:refer-number plural)
				:topic (s15x16 / 经济
					:possessor (s15c / country
						:name (s15n2 / name
							:op1 "中国"))))
			:mode interrogative
			:aspect performance)
		:mod (s15x10 / 还)
		:aspect activity))

# alignment:
s15b: 0-0
s15c: 0-0
s15i2: 0-0
s15n: 0-0
s15n2: 0-0
s15x: 3-3
s15x10: 23-23
s15x11: 11-11
s15x12: 12-12
s15x13: 15-15
s15x14: 16-16
s15x15: 0-0
s15x16: 20-20
s15x2: 8-8
s15x3: 5-5
s15x4: 4-4
s15x5: 6-6
s15x6: 1-1
s15x7: 24-24
s15x8: 14-14
s15x9: 25-25

# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :overlap s15x)
            (s15x :before s15x3)
            (s15x12 :after s15x13)
            (s15x13 :overlap s15x9))
    :modal ((root :modal author)
            (author :full-affirmative s15x)
            (author :full-affirmative s15x12)
            (purpose :full-affirmative s15x3)
            (author :neutral-affirmative s15x13)
            (author :partial-affirmative s15x9)
            (author :full-affirmative s15x4)
            (s15x4 :partial-affirmative purpose))
    :coref ()
)

## chinese_umr-0024, sentence 13

# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46
Words: plaintext虽然 中国 当局 最近 几个 月 表示 他们 已经 结束 监管 打击 行动 ， 并 将 寻找 支持 私营 部门 的 方法 ， 但 中国 企业家 们 表示 ， 他们 看到 马云 仍 决定 留在 海外 ， 是 阻碍 企业界 恢复 信心 的 一个 因素 。

# sentence level graph:
(s13h / have-concession-91
	:ARG1 (s13x2 / 表示-01
		:ARG0 (s13x17 / 企业家
			:refer-number plural
			:place (s13c / country
				:name (s13n / name
					:op1 "中国")))
		:ARG1 (s13x19 / 看到-01
			:ARG0 s13x17
			:ARG1 (s13i3 / identity-91
				:ARG1 (s13x4 / 决定-01
					:ARG0 (s13i2 / individual-person
						:name (s13n3 / name
							:op1 "马云"))
					:ARG1 (s13x12 / 留在-01
						:ARG1 s13i2
						:ARG2 (s13x18 / 海外)
						:aspect state)
					:mod (s13x11 / 仍)
					:aspect performance)
				:ARG2 (s13x25 / 因素
					:quant 1
					:unit (s13x26 / 个)
					:ARG0-of (s13x21 / 阻碍-02
						:ARG1 (s13x24 / 企业界)
						:ARG2 (s13x22 / 恢复-02
							:ARG0 s13x24
							:ARG1 (s13x23 / 信心)
							:aspect process)
						:aspect process))
				:aspect state)
			:aspect performance)
		:aspect performance)
	:ARG2 (s13x / 表示-01
		:ARG0 (s13x3 / 当局
			:possessor (s13c2 / country
				:name (s13n2 / name
					:op1 "中国")))
		:ARG1 (s13a / and
			:op1 (s13x5 / 结束-01
				:ARG0 s13x3
				:ARG1 (s13x10 / 行动
					:mod (s13x29 / 打击)
					:mod (s13x30 / 监管))
				:mod (s13x31 / 已经)
				:aspect performance)
			:op2 (s13x13 / 寻找-01
				:ARG0 s13x3
				:ARG1 (s13x6 / 方法
					:mod (s13x14 / 支持-01
						:ARG0 s13x3
						:ARG1 (s13x15 / 部门
							:mod (s13x16 / 私营))
						:aspect activity))
				:aspect process))
		:temporal (s13t / temporal-quantity
			:quant (s13x7 / 几)
			:unit (s13x8 / 月)
			:mod (s13x9 / 最近))
		:aspect performance))

# alignment:
s13a: 0-0
s13a2: 0-0
s13b: 0-0
s13c: 0-0
s13c2: 0-0
s13i2: 0-0
s13n: 0-0
s13n2: 0-0
s13n3: 0-0
s13p: 0-0
s13t: 0-0
s13x: 7-7
s13x10: 13-13
s13x11: 33-33
s13x12: 35-35
s13x13: 17-17
s13x14: 18-18
s13x15: 20-20
s13x16: 19-19
s13x17: 26-26
s13x18: 36-36
s13x19: 31-31
s13x2: 7-7
s13x21: 39-39
s13x22: 41-41
s13x23: 42-42
s13x24: 40-40
s13x29: 12-12
s13x3: 3-3
s13x30: 11-11
s13x4: 34-34
s13x5: 10-10
s13x6: 22-22
s13x7: 5-5
s13x8: 6-6
s13x9: 4-4

# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x)
            (s13x :before s13x5)
            (s13x5 :after s13x13)
            (s13x :after s13x13)
            (document-creation-time :before s13x2)
            (s13x2 :before s13x19)
            (s13x4 :overlap s13x12)
            (s13x4 :after s13x21)
            (s13x21 :overlap s13x22)
            (s13x19 :overlap s13i3))
    :modal ((root :modal author)
            (author :full-affirmative s13x)
            (author :full-affirmative s13x2)
            (author :full-affirmative s13x3)
            (s13x3 :full-affirmative s13x5)
            (s13x3 :partial-affirmative s13x13)
            (s13x3 :partial-affirmative s13x14)
            (author :full-affirmative s13x17)
            (s13x17 :full-affirmative s13x19)
            (s13x17 :full-affirmative s13x4)
            (s13x17 :full-affirmative s13i3)
            (s13x17 :full-affirmative s13x21)
            (s13x17 :neutral-affirmative s13x22))
    :coref ()
)

## chinese_umr-0019, sentence 1

# :: snt1
Index:    1    2    3    4  5    6    7    8    9 10   11 12   13   14 15  16 17 18   19   20   21 22
Words: 随着   冬至   当日   带来   的  罕见   寒潮   袭击   广东   ，  广州   市  气温   急骤   至  3.3 度  ，  打破   近年   纪录   。 

# sentence level graph:
(s1a / 袭击-01
	:ARG0 (s1x / 寒潮
		:mod (s1x2 / 罕见)
		:temporal (s1c / cultural-activity
			:name (s1n / name
				:op1 "冬至")
			:mod (s1x3 / 当日)))
	:ARG1 (s1p / province
		:name (s1n3 / name
			:op1 "广东"))
	:aspect performance
	:temporal (s1x8 / 随着)
	:cause-of (s1x4 / 急骤-00
		:ARG0 (s1x5 / 气温
			:place (s1c2 / city
				:name (s1n4 / name
					:op1 "广州市")))
		:ARG1 (s1x6 / 至-01
			:ARG1 (s1t / temperature-quantity
				:quant 3.3
				:unit (s1x12 / 度)
				:ARG0-of (s1x13 / 打破-01
					:ARG1 (s1x14 / 纪录
						:mod (s1x15 / 近年))
					:aspect performance))
			:aspect state)
		:aspect performance))

# alignment:
s1a: 8-8
s1c: 0-0
s1c2: 0-0
s1n: 0-0
s1n3: 0-0
s1n4: 0-0
s1p: 0-0
s1t: 0-0
s1x: 7-7
s1x12: 17-17
s1x13: 19-19
s1x14: 21-21
s1x15: 20-20
s1x2: 6-6
s1x3: 3-3
s1x4: 14-14
s1x5: 13-13
s1x6: 15-15
s1x8: 1-1

# document level annotation:
(s1s0 / sentence
	:temporal ((document-creation-time :before s1a)
		(s1x4 :after s1x6)
		(s1x4 :contained s1x13)
		(s1a :contained s1x4)
		(s1a :contained s1x13)))
	:modal ((root :modal author)
		(author :full-affirmative s1a)
		(author :full-affirmative s1x13)
		(author :full-affirmative s1x6)
		(author :full-affirmative s1x4)
		(root :modal author))

## chinese_umr-0015, sentence 1

# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
Words: 随着 冬至 当日 带来 的 罕见 寒潮 袭击 广东 ， 广州 市 气温 急骤 至 3.3 度 ， 打破 近年 纪录 。

# sentence level graph:
(s1x4 / 至-01
    :ARG0 (s1x3 / 气温
        :place (s1c / city
            :name (s1n2 / name
                :op1 "广州市")))
    :ARG1 (s1x5 / 度
        :quant 3.3)
    :manner (s1x / 急骤)
    :ARG0-of (s1x6 / 打破-01
        :ARG1 (s1x7 / 纪录
            :mod (s1x8 / 近年))
        :aspect performance)
    :aspect performance
    :temporal (s1x2 / 随着
        :op1 (s1x10 / 袭击-01
            :ARG0 (s1x11 / 寒潮
                :ARG1-of (s1x12 / 带来-01
                    :ARG0 (s1x14 / 冬至
                        :temporal (s1x15 / 当日))
                    :aspect performance)
                :mod (s1x16 / 罕见))
            :ARG1 (s1p / province
                :name (s1n / name
                    :op1 "广东"))
            :aspect performance)))

# alignment:
s1c: 0-0
s1n: 0-0
s1n2: 0-0
s1p: 0-0
s1x: 14-14
s1x10: 8-8
s1x11: 7-7
s1x12: 4-4
s1x14: 2-2
s1x15: 3-3
s1x16: 6-6
s1x2: 1-1
s1x3: 13-13
s1x4: 15-15
s1x5: 17-17
s1x6: 19-19
s1x7: 21-21
s1x8: 20-20

# document level annotation:
(s1s0 / sentence
    :temporal ((s1x4 :before s1x10)
            (document-creation-time :before s1x4)
            (s1x4 :overlap s1x6))
    :modal ((author :full-affirmative s1x6)
            (author :full-affirmative s1x4)
            (root :modal author)
            (author :full-affirmative s1x10)
            (author :full-affirmative s1x6)
            (author :full-affirmative s1x12))
    :coref ()
)

## chinese_umr-0025, sentence 1151

# :: snt1151
Index:    1      2  3    4  5  6      7  8  9 10 11 12 13
Words: 只有   孩子们    把  鼻子   贴  在  玻璃窗    上  往  外  看  。  ” 

# sentence level graph:
(s1151x14 / say
	:ARG1 (s1151x11 / 看-02
		:ARG0 (s1151x2 / 孩子们)
		:direction (s1151x10 / 外)
		:manner (s1151x5 / 贴-01
			:ARG0 s1151x2
			:ARG1 (s1151x4 / 鼻子)
			:ARG2 (s1151x7 / 玻璃窗))
		:mod (s1151x1 / 只有)
		:modal-strength (s1151x23 / full-affirmative)))

# alignment:
s1151x1: 1-1
s1151x10: 10-10
s1151x11: 11-11
s1151x14: 0-0
s1151x2: 2-2
s1151x23: 0-0
s1151x4: 4-4
s1151x5: 5-5
s1151x7: 7-7

# document level annotation:
(s1151s0 / sentence)

## chinese_umr-0026, sentence 13

# :: snt13
Index:  1  2    3    4  5  6  7    8  9   10   11 12   13 14   15   16 17 18 19   20 21
Words: 获  邀  参与   报导   的  仅  有  部分   驻  北京   台媒   与  港媒   ，  外国   媒体   未  获  邀  参加   。 

# sentence level graph:
(s13c / contrast-91
	:op1 (s13x / 参与-01
		:ARG0 (s13a / and
			:op1 (s13x2 / 台媒)
			:op2 (s13x3 / 港媒)
			:ARG0-of (s13x5 / 驻-01
				:ARG1 (s13c2 / city
					:name (s13n / name
						:op1 "北京"))
				:aspect state)
			:mod (s13x6 / 部分)
			:ARG0-of (s13x7 / 获邀-01
				:aspect process))
		:ARG1 (s13x4 / 报导-01)
		:aspect performance)
	:op2 (s13x8 / 获邀-00
		:ARG0 (s13x9 / 媒体
			:mod (s13x10 / 外国))
		:ARG1 (s13x11 / 参加-01
			:aspect activity)
		:aspect process
		:polarity -))

# alignment:
s13a: 0-0
s13c: 0-0
s13c2: 0-0
s13n: 0-0
s13x: 3-3
s13x10: 15-15
s13x11: 20-20
s13x2: 11-11
s13x3: 13-13
s13x4: 4-4
s13x5: 9-9
s13x6: 8-8
s13x7: 1-1
s13x8: 1-1
s13x9: 16-16

# document level annotation:
(s13s0 / sentence
	:temporal ((document-creation-time :before s13x)
		(s13x :before s13x7)
		(s13x :overlap s13x4)
		(s13x :overlap s13x5)
		(s13x :before s13x8)
		(s13x8 :after s13x11)))
	:modal ((root :modal author)
		(author :full-affirmative s13x5)
		(author :full-affirmative s13x7)
		(author :full-affirmative s13x)
		(author :full-affirmative s13x11)
		(author :full-negative s13x8)
		(root :modal author))

## chinese_umr-0021, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 此次 日全食 经过 了 墨西哥 、 美国 、 加拿大 ， 日偏食 则 覆盖 了 大洋洲 东部 、 北美洲 绝大部分 及 周边 部分 地区 。

# sentence level graph:
(s4a / and
	:op1 (s4x / 经过-01
		:ARG0 (s4x2 / 日全食
			:mod (s4x9 / 此次))
		:ARG1 (s4a2 / and
			:op1 (s4c / country
				:name (s4n / name
					:op1 "墨西哥"))
			:op2 (s4c2 / country
				:name (s4n2 / name
					:op1 "美国"))
			:op3 (s4c3 / country
				:name (s4n3 / name
					:op1 "加拿大")))
		:aspect performance)
	:op2 (s4x3 / 覆盖-01
		:ARG0 (s4x4 / 日偏食)
		:ARG1 (s4a3 / and
			:op1 (s4x6 / 东部
				:part-of (s4x5 / continent
					:name (s4n4 / name
						:op1 "大洋洲")))
			:op2 (s4x8 / 部分
				:mod (s4x13 / 绝大)
				:part-of (s4x7 / continent
					:name (s4n5 / name
						:op1 "北美洲")))
			:op3 (s4x10 / 地区
				:mod (s4x11 / 周边)
				:mod (s4x12 / 部分)))
		:aspect performance))

# alignment:
s4a: 0-0
s4a2: 0-0
s4a3: 0-0
s4c: 0-0
s4c2: 0-0
s4c3: 0-0
s4n: 0-0
s4n2: 0-0
s4n3: 0-0
s4x: 3-3
s4x10: 23-23
s4x11: 21-21
s4x12: 22-22
s4x2: 2-2
s4x3: 13-13
s4x4: 11-11
s4x5: 15-15
s4x6: 16-16
s4x7: 18-18
s4x8: 22-22
s4x9: 1-1

# document level annotation:
(s4s0 / sentence
	:temporal ((document-creation-time :before s4x)
		(s4x :overlap s4x3)))
	:modal ((root :modal author)
		(author :full-affirmative s4x)
		(author :full-affirmative s4x3)
		(root :modal author))

## chinese_umr-0005, sentence 9

# :: snt9
Index: 1    2 3 4 5  6 7 8  9  10 11 12 13 14 15  16
Words: 1968 年 底 ， 13 岁 的 于海 虚报 了  年龄 ，  报名 参加 工程兵 。 

# sentence level graph:
(s9a / and
    :op1 (s9x / 虚报-01
        :ARG0 (s9i2 / individual-person
            :name (s9n / name
                :op1 "于海")
            :age (s9t / temporal-quantity
                :quant 13
                :unit (s9x6 / 岁)))
        :ARG1 (s9x7 / 年龄)
        :temporal (s9x8 / 底
            :part-of (s9d / date-entity
                :year 1968))
        :aspect performance)
    :op2 (s9x2 / 报名-01
        :ARG0 (s9s / s9i2)
        :aspect performance
        :purpose (s9x3 / 参加-01
            :ARG0 s9i2
            :ARG1 (s9x4 / 兵
                :topic (s9x5 / 工程))
            :aspect performance)))


# alignment:
s9a: 0-0
s9d: 0-0
s9i2: 0-0
s9n: 0-0
s9s: 0-0
s9t: 0-0
s9x: 9-9
s9x2: 13-13
s9x3: 14-14
s9x4: 15-15
s9x5: 15-15
s9x6: 6-6
s9x7: 11-11
s9x8: 3-3

# document level annotation:
(s9s0 / sentence
    :temporal ((s9x8 :overlap s9x)
        (s9x :overlap s9x2)
        (s9x2 :overlap s9x3))
    :modal ((root :modal author)
        (author :full-affirmative s9x)
        (author :full-affirmative s9x2)
        (author :full-affirmative s9x3)
        (author :full-affirmative s9i2)
        (author :full-affirmative s9i2)
        (s9i2 :full-affirmative s9x2)
        (s9x2 :unspecified s9x3))
    :coref ((s8i2 :same-entity s9i2)))

## chinese_umr-0004, sentence 39

# :: snt39
Index: 1  2  3  4  5 6  7  8  9 10 11 12 13 14 15 16 17 18 19  20 21 22 23  24 25 26 27 28  29 30 31 32 33 34 35 36  37 38 39 40 41 42 43
Words: 比如 雷娜 起初 打算 把 背景 设在 酒吧 内 ，  但  剧集 的  执行 制作 人及 总  编剧 拉塞尔 ·  T  ·  戴维斯 认为 酒吧 播出 的  爵士乐 的  风格 与  剧情 不  相符 ，  故雷娜 最终 将  背景 改为 胡佛 村  。 

# sentence level graph:
(s39i2 / implicit-argument
    :example (s39h / have-reason-91
        :ARG1 (s39b / but-91
            :ARG1 (s39x / 打算-01
                :ARG0 (s39i3 / individual-person
                    :name (s39n / name
                        :op1 "雷娜"))
                :ARG1 (s39x2 / 设在-01
                    :ARG0 s39i3
                    :ARG1 (s39x3 / 背景)
                    :ARG2 (s39x4 / 内
                        :op1 (s39x5 / 酒吧))
                    :aspect state)
                :aspect state)
            :ARG2 (s39x19 / 认为-01
                :ARG0 (s39i6 / individual-person
                    :name (s39n4 / name
                        :op1 "拉塞尔"
                        :op2 "·"
                        :op3 "T"
                        :op4 "·"
                        :op5 "戴维斯")
                    :ARG0-of (s39i7 / identity-91
                        :ARG1 (s39a4 / and
                            :op1 (s39x28 / 制作人
                                :place (s39x29 / 剧集)
                                :mod (s39x30 / 执行-01
                                    :aspect habitual))
                            :op2 (s39x26 / 编剧
                                :mod (s39x27 / 总)))
                        :aspect state))
                :ARG1 (s39x20 / 相符-01
                    :ARG0 (s39a3 / and
                        :op1 (s39x22 / 风格
                            :manner-of (s39x23 / 爵士乐
                                :ARG1-of (s39x24 / 播出-01
                                    :ARG0 (s39x25 / 酒吧)
                                    :aspect habitual)))
                        :op2 (s39x21 / 剧情))
                    :polarity -
                    :aspect state)
                :aspect state))
        :ARG2 (s39x6 / 改为-01
            :ARG0 s39i3
            :ARG1 s39x4
            :ARG2 (s39c / city-district
                :name (s39n2 / name
                    :op1 "胡佛"
                    :op2 "村")))
        :aspect performance))


# alignment:
s39a3: 0-0
s39a4: 0-0
s39b: 21-21
s39c: 21-21
s39h: 0-0
s39i2: 21-21
s39i3: 0-0
s39i6: 0-0
s39i7: 21-21
s39n: 0-0
s39n2: 0-0
s39n4: 0-0
s39x: 4-4
s39x19: 24-24
s39x2: 7-7
s39x20: 34-34
s39x21: 32-32
s39x22: 30-30
s39x23: 28-28
s39x24: 26-26
s39x25: 8-8
s39x26: 18-18
s39x27: 17-17
s39x28: 15-15
s39x29: 12-12
s39x3: 6-6
s39x30: 14-14
s39x4: 9-9
s39x5: 8-8
s39x6: 40-40

# document level annotation:
(s39s0 / sentence
    :temporal ((document-creation-time :before s39x)
        (s39x :overlap s39x2)
        (s39x2 :overlap s39x19)
        (s39x19 :overlap s39x20)
        (s39x20 :overlap s39x24)
        (s39x :after s39x6))
    :modal ((root :modal author)
        (author :full-affirmative s39x2)
        (author :full-affirmative s39x)
        (author :full-affirmative s39x30)
        (author :full-affirmative s39i7)
        (author :full-affirmative s39x24)
        (author :full-negative s39x20)
        (author :full-affirmative s39x19)
        (author :full-affirmative s39h))
    :coref ((s37i2 :same-entity s39i3)
        (s13c2 :same-entity s39c)
        (s36i2 :same-entity s39i6)
        (s1s2 :same-entity s39x29)))

## chinese_umr-0004, sentence 37

# :: snt37
Index: 1  2 3  4  5  6  7  8 9  10 11 12 13 14   15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34   35
Words: 为此 ， 雷娜 特意 观看 一些 旧时 的 怪兽 电影 ，  其中 包括 1931 年  上映 的  《  科学 怪人 》  ，  这  也  使  她  最终 把  这  集以 大  萧条 为  时代背景 。 

# sentence level graph:
(s37x / 观看-01
    :ARG0 (s37i2 / individual-person
        :name (s37n / name
            :op1 "雷娜"))
    :ARG1 (s37x3 / 电影
        :mod (s37x4 / 怪兽)
        :temporal (s37x5 / 旧时)
        :quant (s37x6 / 一些)
        :ARG0-of (s37x7 / 包括-01
            :ARG1 (s37w / work-of-art
                :name (s37n2 / name
                    :op1 "科学"
                    :op2 "怪人")
                :ARG1-of (s37x8 / 上映-01
                    :temporal (s37d / date-entity
                        :year 1931)
                    :aspect performance))
            :aspect state))
    :reason (s37t / thing
        :refer-person 3rd
        :refer-number singular)
    :manner (s37x2 / 特意)
    :aspect habitual
    :cause-of (s37x9 / 为-02
        :ARG0 s37i2
        :ARG1 (s37x10 / 背景
            :mod (s37x11 / 时代)
            :possessor (s37x14 / 集
                :mod (s37x15 / 这)))
        :ARG2 (s37d2 / date-entity
            :era (s37x12 / 大萧条))
        :temporal (s37x13 / 最终)
        :aspect state))


# alignment:
s37d: 0-0
s37d2: 0-0
s37i2: 0-0
s37n: 0-0
s37n2: 0-0
s37t: 0-0
s37w: 0-0
s37x: 5-5
s37x10: 34-34
s37x11: 34-34
s37x12: 31-31
s37x13: 27-27
s37x14: 30-30
s37x15: 23-23
s37x2: 4-4
s37x3: 10-10
s37x4: 9-9
s37x5: 7-7
s37x6: 6-6
s37x7: 13-13
s37x8: 16-16
s37x9: 33-33

# document level annotation:
(s37s0 / sentence
    :temporal ((document-creation-time :before s37x)
        (s37x :overlap s37x7)
        (s37x :before s37x8)
        (s36x :after s37x))
    :modal ((root :modal author)
        (author :full-affirmative s37x8)
        (author :full-affirmative s37x7)
        (author :full-affirmative s37x)
        (author :full-affirmative s37x9))
    :coref ((s36x13 :same-event s37t)
        (s36x4 :same-entity s37x14)))

## chinese_umr-0004, sentence 33

# :: snt33
Index: 1  2 3  4  5 6    7 8  9 10 11 12 13 14 15 16 17 18   19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
Words: 这集 也 不是 首部 以 帝国大厦 为 背景 的 《  异世 奇人 》  剧集 ，  早  在  1966 年  的  《  追捕 》  中  就  到  过  这儿 ，  而  他  的  对手 正是 戴  立克 。 

# sentence level graph:
(s33a / and
    :op1 (s33i2 / identity-91
        :ARG1 (s33x2 / 集
            :mod (s33x3 / 这))
        :ARG2 (s33x4 / 剧集
            :part-of (s33s2 / show
                :name (s33n4 / name
                    :op1 (s33x14 / 异世)
                    :op2 (s33x13 / 奇人))
                :ord (s33o / ordinal-entity
                    :unit (s33x6 / 部)
                    :value 1)
                :ARG0-of (s33x11 / 为-02
                    :ARG1 (s33x12 / 背景)
                    :ARG2 (s33b / building
                        :name (s33n / name
                            :op1 "帝国大厦"))
                    :aspect state)))
        :aspect state
        :polarity -)
    :op2 (s33x / 到-01
        :ARG1 (s33x7 / 这儿)
        :mod (s33x8 / 就)
        :temporal (s33s / show
            :name (s33n2 / name
                :op1 "追捕")
            :temporal (s33d / date-entity
                :year 1966))
        :mod (s33x9 / 早)
        :aspect performance)
    :op3 (s33i3 / identity-91
        :ARG1 (s33x10 / 对手
            :possessor (s33p / person
                :refer-number singular
                :refer-person 3rd))
        :ARG2 (s33e / ethnic-group
            :name (s33n3 / name
                :op1 "戴"
                :op2 "立克"))
        :aspect state))


# alignment:
s33a: 0-0
s33b: 0-0
s33d: 0-0
s33e: 0-0
s33i2: 0-0
s33i3: 0-0
s33n: 0-0
s33n2: 0-0
s33n3: 0-0
s33n4: 0-0
s33o: 0-0
s33p: 0-0
s33s: 0-0
s33s2: 0-0
s33x: 26-26
s33x10: 33-33
s33x11: 7-7
s33x12: 8-8
s33x13: 12-12
s33x14: 11-11
s33x2: 1-1
s33x3: 1-1
s33x4: 14-14
s33x6: 4-4
s33x7: 28-28
s33x8: 25-25
s33x9: 16-16

# document level annotation:
(s33s0 / sentence
    :temporal ((document-creation-time :before s33d)
        (s33x :overlap s33d))
    :modal ((root :modal author)
        (author :full-negative s33i2)
        (author :full-affirmative s33x)
        (author :full-affirmative s33i3)
        (author :full-affirmative s33x11))
    :coref ((s21b :same-entity s33b)
        (s1s2 :same-entity s33s2)
        (s3e :same-entity s33e)))

## chinese_umr-0001, sentence 16

# :: snt16
Index: 1    2 3    4 5 6  7  8 9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27  28   29 30 31 32  33 34 35
Words: 2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当  总统 」  ，  还  注销 了  双方 握手 的  合成 照片 ，  甚至 指  柯林顿 1992 年  也  靠  外星人 背书 当选 。 

# sentence level graph:
(s16a / and
    :op1 (s16x / 报导-01
        :ARG0 (s16x4 / 刊
            :mod (s16x5 / 该))
        :ARG1 (s16x6 / 支持-01
            :ARG0 (s16x7 / 外星人)
            :ARG1 (s16x8 / 当-02
                :ARG0 (s16i2 / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16x9 / 总统))
            :aspect state)
        :quote s16x
        :temporal (s16e / event
            :name (s16n3 / name
                :op1 "2000"
                :op2 "年"
                :op3 "总统大选"))
        :aspect performance)
    :op2 (s16x2 / 注销-00
        :ARG0 s16x4
        :ARG1 (s16x10 / 照片
            :ARG1-of (s16x11 / 合成-01
                :aspect performance)
            :mod (s16x12 / 握手-01
                :ARG0 (s16x13 / 双方)
                :aspect process))
        :aspect performance)
    :op3 (s16x3 / 指-02
        :ARG0 s16x4
        :ARG1 (s16x14 / 当选-01
            :ARG0 (s16i3 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :reason (s16x15 / 背书-00
                :ARG0 (s16x16 / 外星人)
                :aspect performance
                :quote s16x3)
            :temporal (s16d / date-entity
                :year 1992)
            :aspect performance
            :quote s16x3)
        :aspect performance))


# alignment:
s16a: 0-0
s16d: 0-0
s16e: 0-0
s16i2: 0-0
s16i3: 0-0
s16n: 0-0
s16n2: 0-0
s16n3: 0-0
s16x: 7-7
s16x10: 23-23
s16x11: 22-22
s16x12: 20-20
s16x13: 19-19
s16x14: 34-34
s16x15: 33-33
s16x16: 9-9
s16x2: 17-17
s16x3: 26-26
s16x4: 6-6
s16x5: 6-6
s16x6: 10-10
s16x7: 9-9
s16x8: 12-12
s16x9: 13-13

# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16x)
        (s16x :overlap s16x6)
        (s16x6 :overlap s16x8)
        (s16x :overlap s16x2)
        (s16x2 :overlap s16x11)
        (s16x11 :overlap s16x12)
        (s16x2 :overlap s16x3)
        (s16x3 :before s16x14)
        (s16x14 :overlap s16x15))
    :modal ((root :modal author)
        (author :full-affirmative s16x6)
        (author :full-affirmative s16x4)
        (s16x4 :full-affirmative s16x)
        (author :full-affirmative s16x11)
        (author :full-affirmative s16x4)
        (author :full-affirmative s16x12)
        (author :full-affirmative s16x4)
        (s16x4 :full-affirmative s16x2)
        (author :full-affirmative s16x15)
        (author :full-affirmative s16x4)
        (author :full-affirmative s16x14)
        (author :full-affirmative s16x4)
        (s16x4 :full-affirmative s16x3))
    :coref ((s12n :same-entity s16x4)))

## chinese_umr-0017, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
Words: 联合国 人道 事务 协调 厅 （ UNOCHA ） 表示 ， 已 有 4 万 多 人 逃往 孟加拉 、 印度 和 泰国 等 邻国 。

# sentence level graph:
(s5x / 表示-01
	:ARG0 (s5i2 / international-organization
		:name (s5n / name
			:op1 "联合国"
			:op2 "人道"
			:op3 "事务"
			:op4 "协调"
			:op5 "厅"
			:op6 "UNOCHA"))
	:ARG1 (s5x2 / 逃往-01
		:ARG0 (s5x3 / 人
			:quant (s5x4 / 4万多))
		:ARG1 (s5x5 / 邻国
			:example (s5a / and
				:op1 (s5c / country
					:name (s5n2 / name
						:op1 "孟加拉"))
				:op2 (s5c2 / country
					:name (s5n3 / name
						:op1 "印度"))
				:op3 (s5c3 / country
					:name (s5n4 / name
						:op1 "泰国"))))
		:mod (s5x6 / 已)
		:aspect performance)
	:aspect performance)

# alignment:
s5a: 0-0
s5c: 0-0
s5c2: 0-0
s5c3: 0-0
s5h: 0-0
s5i2: 0-0
s5n: 0-0
s5n2: 0-0
s5n3: 0-0
s5n4: 0-0
s5x: 9-9
s5x2: 17-17
s5x3: 16-16
s5x4: 13-13
s5x5: 24-24
s5x6: 11-11

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x)
            (document-creation-time :before s5x2))
    :modal ((root :modal author)
            (author :full-affirmative s5x)
            (author :full-affirmative s5i2)
            (s5i2 :full-affirmative s5x2))
    :coref ()
)

## chinese_umr-0008, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13
Words: 两年 后 ， 国会 又 通过 法案 授权 发行 3 美元 金币 。

# sentence level graph:
(s4a / and
    :op1 (s4x / 通过-01
        :ARG0 (s4g / government-organization
            :name (s4n / name
                :op1 "国会"))
        :ARG1 (s4x6 / 法案)
        :mod (s4x4 / 又)
        :aspect performance)
    :op2 (s4x5 / 授权-01
        :ARG0 s4g
        :ARG1 (s4x7 / 发行-01
            :ARG1 (s4x8 / 金币
                :mod (s4m / monetary-quantity
                    :quant 3
                    :unit (s4x9 / 美元)))
            :aspect performance
            :modal-predicate s4x5)
        :aspect performance)
    :temporal (s4x2 / 后
            :op1 (s4t / temporal-quantity
                :quant 2
                :unit (s4x3 / 年))))

# alignment:
s4g: 0-0
s4n: 0-0
s4x: 9-9
s4x2: 2-2
s4x3: 1-1
s4x4: 5-5
s4x5: 8-8
s4x6: 7-7
s4x7: 12-12
s4x8: 11-11
s4x9: 11-11

# document level annotation:
(s4s0 / sentence
    :temporal ((s3d :after s4x2)
            (s4x2 :overlap s4x)
            (s4x2 :overlap s4x5)
            (s4x5 :overlap s4x7))
    :modal ((root :modal author)
            (author :full-affirmative s4x)
            (author :full-affirmative s4x5)
            (author :full-affirmative s4g)
            (s4g :neutral-affirmative s4x7))
    :coref ((s3g :same-entity s4g)
            (s1x4 :same-entity s4x8))
)

## chinese_umr-0017, sentence 9

# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 2023 年 2 月 ， 政变 两 周年 之 际 ， 国家 行政 委员会 主席 敏昂莱 承认 失去 了 对 “ 超过 三分之一 ” 镇区 的 稳定 控制 。

# sentence level graph:
(s9x / 承认-01
	:ARG0 (s9i / individual-person
		:name (s9n / name
			:op1 "敏昂莱")
		:ARG1-of (s9h / have-org-role-92
			:ARG2 (s9o / government-organization
				:name (s9n2 / name
					:op1 "国家"
					:op2 "行政"
					:op3 "委员会"))
			:ARG3 (s9x2 / 主席)))
	:ARG1 (s9x6 / 失去-01
		:ARG0 s9i
		:ARG1 (s9x3 / 控制-01
			:ARG0 s9i
			:ARG1 (s9x7 / 镇区
				:quant (s9x11 / 三分之一
					:mod (s9x12 / 超过)))
			:aspect state
			:manner (s9x5 / 稳定))
		:aspect performance)
	:temporal (s9d / date-entity
		:year 2023
		:month 2)
	:temporal (s9x4 / 际
		:op1 (s9x13 / 周年
			:quant 2
			:possessor (s9x8 / 政变-01)))
	:aspect performance)

# alignment:
s9d: 0-0
s9h: 0-0
s9i: 0-0
s9n: 0-0
s9n2: 0-0
s9o: 0-0
s9x: 17-17
s9x11: 23-23
s9x12: 22-22
s9x13: 8-8
s9x2: 15-15
s9x3: 28-28
s9x4: 10-10
s9x5: 27-27
s9x6: 18-18
s9x7: 25-25
s9x8: 6-6

# document level annotation:
(s9s0 / sentence
    :temporal ((document-creation-time :before s9x)
            (document-creation-time :before s9x6)
            (s6x13 :before s9x8))
    :modal ((root :modal author)
            (author :full-affirmative s9x)
            (author :full-affirmative s9i)
            (s9i :full-affirmative s9x6)
            (s9i :full-affirmative s9x3))
    :coref ((s6x8 :same-event s9x8))
)

## chinese_umr-0018, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
Words: 事发 前 3 天 ， 参与 审理 南非 诉 以色列 犯下 种族 灭绝 罪 的 联合国 国际法院 法官 一致 通过 临时 裁决 ， 要求 以色列 必须 保证 救援 物资 能够 不受 任何 阻碍 地 进入 加沙 ， 保证 加沙 地带 的 基本 生活 所需 水电 供应 ， 并 展开 人道主义 救援 。

# sentence level graph:
(s8a2 / and
	:op1 (s8x / 通过-01
		:ARG0 (s8p / person
			:ARG1-of (s8h / have-org-role-92
				:ARG2 (s8i2 / international-organization
					:name (s8n5 / name
						:op1 "联合国"
						:op2 "国际法院"))
				:ARG3 (s8x22 / 法官))
			:ARG0-of (s8x23 / 参与-01
				:ARG1 (s8x24 / 审理-01
					:ARG0 s8p
					:ARG1 (s8x25 / 诉-00
						:ARG0 (s8c / country
							:name (s8n3 / name
								:op1 "南非"))
						:ARG1 (s8c2 / country
							:name (s8n4 / name
								:op1 "以色列"))
						:ARG2 (s8x7 / 犯下-01
							:ARG0 s8c2
							:ARG1 (s8x26 / 罪
								:mod (s8x27 / 灭绝-01
									:ARG1 (s8x28 / 种族)
									:aspect performance))
							:aspect performance)
						:aspect performance)
					:aspect performance)
				:aspect performance))
		:ARG1 (s8x21 / 裁决-01
			:mod (s8x29 / 临时)
			:aspect performance)
		:mod (s8x31 / 一致)
		:aspect performance)
	:op2 (s8x30 / 要求-02
		:ARG0 s8p
		:ARG1 s8c2
		:ARG2 (s8a / and
			:op1 (s8x11 / 保证-01
				:ARG0 s8c2
				:ARG1 (s8x12 / 进入-01
					:ARG0 (s8x16 / 物资
						:mod (s8x17 / 救援))
					:ARG1 (s8l / local-region
						:name (s8n2 / name
							:op1 "加沙"
							:op2 "地带"))
					:ARG1-of (s8x14 / 阻碍-01
						:mod (s8x15 / 任何)
						:polarity -
						:aspect performance)
					:aspect performance
					:modal-strength neutral-affirmative)
				:aspect state
				:modal-strength partial-affirmative)
			:op2 (s8x5 / 保证-01
				:ARG0 s8c2
				:ARG1 (s8x6 / 供应-01
					:ARG1 (s8x8 / 水电
						:ARG1-of (s8x9 / 需-01
							:ARG0 (s8x10 / 生活
								:mod (s8x13 / 基本))
							:aspect state))
					:ARG2 s8l
					:aspect activity)
				:aspect state
				:modal-strength partial-affirmative)
			:op3 (s8x2 / 展开-01
				:ARG0 s8c2
				:ARG1 (s8x3 / 救援-01
					:mod (s8x4 / 人道主义)
					:aspect activity)
				:aspect activity
				:modal-strength partial-affirmative))
		:aspect performance)
	:temporal (s8t / temporal-quantity
		:quant 3
		:unit (s8x19 / 天)
		:mod (s8x18 / 前
			:op1 (s8x20 / 事发-01)
			:aspect performance)))

# alignment:
s8a: 0-0
s8a2: 0-0
s8c: 0-0
s8c2: 0-0
s8h: 0-0
s8i2: 0-0
s8l: 0-0
s8n2: 0-0
s8n3: 0-0
s8n4: 0-0
s8n5: 0-0
s8t: 0-0
s8x: 20-20
s8x10: 43-43
s8x11: 27-27
s8x12: 35-35
s8x13: 42-42
s8x14: 33-33
s8x15: 32-32
s8x16: 29-29
s8x17: 28-28
s8x18: 2-2
s8x19: 4-4
s8x2: 49-49
s8x20: 1-1
s8x21: 22-22
s8x22: 18-18
s8x23: 6-6
s8x24: 7-7
s8x25: 9-9
s8x26: 14-14
s8x27: 13-13
s8x28: 12-12
s8x3: 28-28
s8x30: 24-24
s8x31: 19-19
s8x4: 50-50
s8x5: 27-27
s8x6: 46-46
s8x7: 11-11
s8x8: 45-45
s8x9: 44-44

# document level annotation:
(s8s0 / sentence
    :temporal ((s8x23 :overlap s8x24)
            (s8x30 :after s8x11)
            (s8x11 :after s8x12)
            (s8x11 :overlap s8x5)
            (s8x5 :overlap s8x9)
            (s8x5 :after s8x6)
            (s8x5 :overlap s8x2)
            (s8x2 :overlap s8x3)
            (s8t :before s8x23)
            (s8x24 :before s8x25)
            (s8x25 :before s8x7)
            (s8x7 :overlap s8x27)
            (s8x :overlap s8x21)
            (s8x21 :overlap s8x30)
            (document-creation-time :before s8x20)
            (s8t :contained s8x))
    :modal ((root :modal author)
            (author :full-affirmative s8x25)
            (author :full-affirmative s8x24)
            (author :full-affirmative s8x23)
            (author :full-affirmative s8x21)
            (author :full-affirmative s8x)
            (author :full-affirmative s8x9)
            (author :full-affirmative s8x30)
            (author :full-affirmative s8x18)
            (root :modal author)
            (author :neutral-affirmative s8x12)
            (author :partial-affirmative s8x11)
            (author :partial-affirmative s8x5)
            (author :partial-affirmative s8x2)
            (author :full-affirmative s8c)
            (s8c :full-affirmative s8x27)
            (s8c :full-affirmative s8x7)
            (author :full-affirmative s8p)
            (s8p :neutral-negative s8x14)
            (s8p :partial-affirmative s8x11)
            (s8p :partial-affirmative s8x6)
            (s8p :partial-affirmative s8x5)
            (s8p :partial-affirmative s8x2)
            (s8p :partial-affirmative s8x3))
    :coref ((s4x10 :same-event s8x20)
            (s6c2 :same-entity s8c2)
            (s6l :same-entity s8l))
)

## chinese_umr-0009, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
Words: 除开 各个 平台 操作系统 的 年度 更新 外 ， 苹果 还 首次 推出 轻薄 型 个人 笔记本 电脑 MacBook Air 的 15 吋 版本 。 新版 MacBook Air 和 其他 星期一 新 发布 的 Mac 产品 一样 ， 处理器 全部 由 苹果 自主 研发 ， 而非 由 处理器 制造商 英特尔 提供 ， 英特尔 当日 股价 下挫 百分之 4.6 。

# sentence level graph:
(s10m / multi-sentence
    :op1 (s10s1 / and
        :op1 (s10x11 / 更新-01
            :ARG1 (s10x12 / 操作系统
                :mod (s10x14 / 平台
                    :mod (s10x15 / 各个)))
            :mod (s10x16 / 年度)
            :aspect performance
            :modal-strength full-affirmative)
        :op2 (s10x / 推出-01
            :ARG0 (s10c / company
                :name (s10n / name
                    :op1 "苹果"))
            :ARG1 (s10v / 版本
                :mod (s10x3 / 电脑
                        :mod (s10x4 / 笔记本)
                        :mod (s10x5 / 个人)
                        :mod (s10x6 / 型
                            :mod (s10x38 / 轻薄))
                        :name (s10n2 / name
                            :op1 "MacBook"
                            :op2 "Air"))
                :mod (s10q / distance-quantity
                    :quant 15
                    :unit (s10x8 / 吋)))
            :ord (s10o / ordinal-entity
                :value 1
                :unit (s10x9 / 次)
            :mod (s10x40 / 还)
            :aspect performance
            :modal-strength full-affirmative))
    :op2 (s10a / and
        :op1 (s10b / contrast-91
            :ARG1 (s10x17 / 研发-01
                :ARG0 s10c
                :ARG1 (s10x18 / 处理器
                    :quant (s10x19 / 全部)
                    :part-of (s10p2 / product
                        :name (s10n5 / name
                            :op1 "MacBook"
                            :op2 "Air")
                        :mod (s10x29 / 新版)))
                :manner (s10x28 / 自主)
                :mod (s10x37 / 一样-02
                    :ARG0 s10p2
                    :ARG1 (s10x20 / 产品
                        :mod (s10m2 / Mac)
                        :mod (s10x24 / 其他)
                        :ARG1-of (s10x22 / 发布-01
                            :temporal (s10d / date-entity
                                :weekday (s10x23 / 星期一))
                            :mod (s10x21 / 新)
                            :aspect performance
                            :modal-strength full-affirmative))
                    :aspect state
                    :modal-strength full-affirmative)
                :aspect performance
                :modal-strength full-affirmative)
            :ARG2 (s10x25 / 提供-01
                :ARG0 (s10i / company
                    :name (s10n3 / name
                        :op1 "英特尔")
                    :ARG1-of (s10i2 / identity-91
                        :ARG2 (s10x26 / 制造商
                            :mod (s10x27 / 处理器))
                        :aspect state
                        :modal-strength full-affirmative))
                :ARG1 s10x18
                :polarity -
                :aspect state
                :modal-strength full-negative)
        :op2 (s10x33 / 下挫-01
            :ARG0 (s10x34 / 股价
                :mod s10i)
            :extent (s10p3 / percentage-entity
                :value 4.6)
            :temporal (s10d2 / 当日)
            :aspect performance
            :modal-strength full-affirmative)))

# alignment:
s10a: 0-0
s10b: 0-0
s10c: 0-0
s10c2: 42-42
s10d2: 54-54
s10i: 50-53
s10m: 35-35
s10m2: 35-35
s10n: 0-0
s10n2: 0-0
s10n3: 0-0
s10n4: 0-0
s10n5: 0-0
s10p: 0-0
s10p2: 0-0
s10v: 24-24
s10x: 13-13
s10x10: 1-1
s10x11: 7-7
s10x12: 4-4
s10x13: 4-4
s10x14: 3-3
s10x15: 2-2
s10x16: 6-6
s10x17: 44-44
s10x18: 39-39
s10x19: 40-40
s10x2: 0-0
s10x20: 36-36
s10x21: 32-32
s10x22: 33-33
s10x23: 31-31
s10x24: 30-30
s10x25: 51-51
s10x26: 49-49
s10x27: 39-39
s10x28: 43-43
s10x29: 26-26
s10x3: 18-18
s10x33: 56-56
s10x34: 55-55
s10x36: 54-54
s10x37: 37-37
s10x38: 14-14
s10x4: 17-17
s10x40: 11-11
s10x5: 16-16
s10x6: 14-14
s10x7: 24-24
s10x8: 23-23
s10x9: 12-12

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10x)
            (s9x14 :overlap s10x)
            (s9x14 :overlap s10x11)
            (s10x :before s10x17)
            (document-creation-time :overlap s10x37)
            (document-creation-time :depends-on s10d)
            (document-creation-time :depends-on s10d2)
            (s10d :overlap s10d2)
            (s10d :contained s10x22)
            (s10d2 :contained s10x33)
            (document-creation-time :overlap s10i2)
            (document-creation-time :overlap s10x25))
    :modal ((author :full-affirmative s10x)
            (author :full-affirmative s10x33)
            (author :full-negative s10x25)
            (root :modal author)
            (author :full-affirmative s10x)
            (author :full-affirmative s10x22)
            (author :full-affirmative s10x37)
            (author :full-affirmative s10x17)
            (author :full-affirmative s10i2))
    :coref ((s9c3 :same-entity s10c)
            (s10v :same-entity s10p2)
            (s8d2 :same-entity s10d))
)

## chinese_umr-0013, sentence 12

# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92
Words: 台湾 民众 党 立法 委员 张启楷 国会 办公室 主任 王如意 则 以 金门县 议会 全体 职员 捐 一日 薪资 所得 等 进行 对比 ， 称 “ 5.6 万元 的 金额 真的 是 太 离谱 了 ！” 其 发言 其后 广受 公众 质疑 为 道德 勒索 ， 更有 网民 引用 其 党 主席 柯文哲 过往 于 台北市长 任内 之 言论 批评 ： “ 最 讨厌 遇到 地震 等 灾难 就要 捐 一个月 的 薪水 ， ‘ 我 又 没 贪污 ， 我 怎么 （ 有 ） 那么 多 钱 ？ ’ ” 。

# sentence level graph:
(s12a / and
	:op1 (s12x / 称-02
		:ARG0 (s12i3 / individual-person
			:name (s12n7 / name
				:op1 "王如意")
			:ARG1-of (s12h7 / have-org-role-92
				:ARG2 (s12p5 / 办公室
					:mod (s12x42 / 国会)
					:possessor (s12i2 / individual-person
						:name (s12n6 / name
							:op1 "张启楷")
						:ARG1-of (s12h4 / have-org-role-92
							:ARG2 (s12p6 / political-party
								:name (s12n9 / name
									:op1 "台湾"
									:op2 "民众"
									:op3 "党"))
							:ARG3 (s12x40 / 委员
								:mod (s12x41 / 立法))
							:aspect state)))
				:ARG3 (s12x35 / 主任)
				:aspect state))
		:manner (s12x30 / 对比-01
			:ARG0 s12i3
			:ARG1 (s12x5 / 金额
				:quant 5.6
				:unit (s12x6 / 万元))
			:ARG2 (s12x25 / 捐-01
				:ARG0 (s12p3 / person
					:refer-number plural
					:mod (s12x36 / 全体)
					:ARG1-of (s12h8 / have-org-role-92
						:ARG2 (s12g / government-organization
							:name (s12n5 / name
								:op1 "金门县"
								:op2 "议会"))
						:ARG3 (s12x37 / 职员)
						:aspect state))
				:ARG1 (s12x26 / 薪资
					:quant (s12x27 / 1)
					:unit (s12x28 / 日))
				:aspect performance)
			:aspect performance)
		:ARG1 (s12x4 / 离谱-01
			:ARG0 s12x5
			:degree intensifier
			:aspect state
			:quote s12x)
		:aspect performance)
	:op2 (s12x7 / 质疑-01
		:ARG0 (s12x8 / 公众)
		:ARG1 (s12i4 / identity-91
			:ARG1 (s12x9 / 发言-01
				:ARG0 s12i3
				:aspect performance)
			:ARG2 (s12x10 / 勒索
				:mod (s12x31 / 道德))
			:aspect state)
		:aspect performance
		:temporal (s12x32 / 后
			:op1 s12x9))
	:op3 (s12x2 / 批评-01
		:ARG0 (s12p / person
			:refer-number plural
			:mod (s12x43 / 网民))
		:ARG1 s12x9
		:manner (s12x11 / 引用-01
			:ARG0 s12p
			:ARG1 (s12a3 / and
				:op1 (s12x16 / 讨厌-01
					:ARG0 (s12p2 / individual-person
						:name (s12n2 / name
							:op1 "柯文哲")
						:ARG1-of (s12h / have-org-role-92
							:ARG2 s12p6
							:ARG3 (s12x12 / 主席)
							:aspect state)
						:ARG1-of (s12h2 / have-org-role-92
							:ARG2 (s12c / city
								:name (s12n10 / name
									:op1 "台北"
									:op2 "市"))
							:ARG3 (s12x15 / 市长)
							:aspect state))
					:ARG1 (s12x17 / 捐-01
						:ARG0 s12p2
						:ARG1 (s12x18 / 薪水
							:quant (s12x19 / 一)
							:unit (s12x20 / 月))
						:temporal (s12x21 / 遇到-01
							:ARG0 s12p2
							:ARG1 (s12x22 / 灾难
								:example (s12x44 / 地震))
							:aspect performance)
						:aspect habitual
						:modal-strength partial-affirmative)
					:degree (s12x45 / 最)
					:aspect state)
				:op2 (s12x23 / 贪污-01
					:ARG0 s12p2
					:polarity -
					:cause-of (s12h3 / have-91
						:ARG1 s12p2
						:ARG2 (s12x24 / 钱)
						:polarity -
						:aspect state)
					:aspect process)
				:quote s12x11)
			:source (s12x3 / 言论
				:possessor s12p2
				:temporal (s12x14 / 任内
					:op1 s12h2
					:mod (s12x33 / 过往)))
			:aspect performance)
		:aspect performance))

# alignment:
s12a: 0-0
s12a2: 0-0
s12a3: 0-0
s12c: 0-0
s12g: 0-0
s12h: 0-0
s12h3: 0-0
s12h4: 0-0
s12h7: 0-0
s12i2: 0-0
s12i3: 0-0
s12i4: 0-0
s12i5: 0-0
s12n: 0-0
s12n10: 0-0
s12n2: 0-0
s12n3: 0-0
s12n4: 0-0
s12n5: 0-0
s12n6: 0-0
s12n7: 0-0
s12n8: 0-0
s12n9: 0-0
s12p: 0-0
s12p2: 0-0
s12p3: 0-0
s12p5: 0-0
s12p6: 0-0
s12s: 0-0
s12x: 25-25
s12x10: 45-45
s12x11: 49-49
s12x12: 3-3
s12x13: 60-60
s12x14: 57-57
s12x15: 56-56
s12x16: 64-64
s12x17: 17-17
s12x18: 73-73
s12x19: 18-18
s12x2: 60-60
s12x20: 71-71
s12x21: 65-65
s12x22: 66-66
s12x23: 79-79
s12x24: 88-88
s12x25: 17-17
s12x26: 19-19
s12x27: 0-0
s12x28: 18-18
s12x29: 22-22
s12x3: 59-59
s12x30: 23-23
s12x31: 44-44
s12x32: 39-39
s12x33: 54-54
s12x4: 34-34
s12x5: 30-30
s12x6: 28-28
s12x7: 42-42
s12x8: 41-41
s12x9: 38-38

# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :after s12x)
            (s12x :after s12x7)
            (s12x7 :contained s12x2)
            (s12x2 :contained s12x11)
            (s12x30 :after s12x)
            (s12x30 :after s12x4)
            (s12x9 :after s12x7)
            (s12x11 :overlap s12x2)
            (s12x23 :after s12h3))
    :modal ((root :modal author)
            (author :full-affirmative s12x25)
            (author :full-affirmative s12x)
            (author :full-affirmative s12x9)
            (author :full-affirmative s12x7)
            (author :full-affirmative s12x11)
            (author :full-affirmative s12x2)
            (author :full-affirmative s12x30)
            (author :full-affirmative s12i3)
            (s12i3 :full-affirmative s12x4)
            (author :full-affirmative s12p2)
            (s12p2 :full-affirmative s12x16)
            (s12p2 :neutral-affirmative s12x21)
            (s12p2 :partial-affirmative s12x17)
            (s12p2 :full-negative s12x23)
            (s12p2 :full-negative s12h3))
    :coref ()
)

## chinese_umr-0001, sentence 28

# :: snt28
Index: 1  2    3 4  5 6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22  23 24
Words: 不过 2004 年 开始 ， 该刊 开始 加注 警语 ：  「  为了 娱乐 起见 ，  请  读者 暂时 抛开 自己 的  不信任 」  。 

# sentence level graph:
(s28x / 开始-01
    :ARG0 (s28x2 / 刊
        :mod (s28x3 / 该))
    :ARG1 (s28x4 / 加注-00
        :ARG1 (s28x5 / 警语
            :ARG1-of (s28i2 / identity-91
                :ARG1-of (s28x6 / 抛开-01
                    :ARG0 (s28x7 / 者
                        :ARG0-of (s28x8 / 读-01))
                    :ARG1 (s28x9 / 信任-01
                        :ARG0 s28x7
                        :polarity -
                        :aspect process)
                    :temporal (s28x10 / 暂时)
                    :reason (s28x11 / 娱乐)
                    :aspect process
                    :mode imperative)))
        :aspect habitual)
    :temporal (s28x12 / 开始
        :op1 (s28d / date-entity
            :year 2004))
    :aspect activity)


# alignment:
s28d: 0-0
s28i2: 0-0
s28x: 4-4
s28x10: 18-18
s28x11: 13-13
s28x12: 4-4
s28x2: 6-6
s28x3: 6-6
s28x4: 8-8
s28x5: 9-9
s28x6: 19-19
s28x7: 17-17
s28x8: 17-17
s28x9: 22-22

# document level annotation:
(s28s0 / sentence
    :temporal ((document-creation-time :before s28d)
        (s27d :overlap s28x)
        (s28x :overlap s28x4)
        (s27x4 :overlap s28x6)
        (s27x6 :overlap s28x9))
    :modal ((root :modal author)
        (author :full-affirmative s28x8)
        (author :full-negative s28x9)
        (author :partial-affirmative s28x6)
        (author :full-affirmative s28x4)
        (author :full-affirmative s28x))
    :coref ((s27n2 :same-entity s28x2)))

## chinese_umr-0025, sentence 1086

# :: snt1086
Index:    1  2    3  4    5  6 7
Words: 应当   有  一定   的  仪式   。  ”

# sentence level graph:
(s1086x8 / say
	:ARG1 (s1086x1 / 应当-01
		:ARG0 (s1086x2 / 有-03
			:ARG1 (s1086x5 / 仪式
				:mod (s1086x3 / 一定)))
		:modal-strength (s1086x14 / partial-affirmative)))

# alignment:
s1086x1: 1-1
s1086x14: 0-0
s1086x2: 2-2
s1086x3: 3-3
s1086x5: 5-5
s1086x8: 0-0

# document level annotation:
(s1086s0 / sentence)

## chinese_umr-0025, sentence 1181

# :: snt1181
Index:    1    2    3    4  5    6  7  8
Words: 然而   我们   还是   开始   去  寻找   了  。 

# sentence level graph:
(s1181x9 / contrast
	:ARG2 (s1181x4 / 开始-01
		:ARG1 (s1181x5 / 去-01
			:ARG1 (s1181x6 / 寻找-01
				:aspect performance
				:ARG0 (s1181x2 / individual-person
					:refer-person 1
					:refer-number plural)))
		:mod (s1181x3 / 还是)
		:ARG0 s1181x2))

# alignment:
s1181x2: 0-0
s1181x3: 3-3
s1181x4: 4-4
s1181x5: 5-5
s1181x6: 6-6
s1181x9: 0-0

# document level annotation:
(s1181s0 / sentence)

## chinese_umr-0019, sentence 11

# :: snt11
Index:    1    2  3    4    5  6    7    8    9   10 11   12   13 14   15   16   17   18 19
Words: 强制   校服   或  影响   安全   。  教育   部门   指引   学校   以  生命   至上   ，  着重   学生   体验   安全   。 

# sentence level graph:
(s11a / and
	:op1 (s11x / 影响-01
		:ARG0 (s11x15 / 强制-01
			:ARG2 (s11x2 / 校服-00)
			:aspect habitual)
		:ARG1 (s11x3 / 安全-01)
		:aspect state)
	:op2 (s11x4 / 指引-01
		:ARG0 (s11x5 / 部门)
		:ARG1 (s11x8 / 学校)
		:ARG2 (s11x9 / 以-01
			:ARG1 (s11x10 / 生命-至上))
		:aspect performance)
	:op3 (s11x11 / 着重-01
		:ARG1 (s11x12 / 学生)
		:ARG2 (s11x13 / 体验-01
			:ARG1 (s11x14 / 安全)
			:aspect process)
		:aspect state))

# alignment:
s11a: 0-0
s11x: 4-4
s11x10: 12-12
s11x11: 15-15
s11x12: 16-16
s11x13: 17-17
s11x14: 5-5
s11x15: 1-1
s11x2: 2-2
s11x3: 5-5
s11x4: 9-9
s11x5: 8-8
s11x8: 10-10
s11x9: 11-11

# document level annotation:
(s11s0 / sentence
	:temporal ((document-creation-time :overlap s11x)
		(document-creation-time :before s11x4)
		(s11x4 :overlap s11x11)
		(s11x15 :after s11x)
		(s11x15 :overlap s11x2)
		(s11x11 :overlap s11x13)))
	:modal ((root :modal author)
		(author :full-affirmative s11x15)
		(author :partial-negative s11x)
		(author :full-affirmative s11x4)
		(author :full-affirmative s11x13)
		(author :full-affirmative s11x11)
		(root :modal author))

## chinese_umr-0015, sentence 11

# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Words: 强制 校服 或 影响 安全 。 教育 部门 指引 学校 以 生命 至上 ， 着重 学生 体验 安全 。

# sentence level graph:
(s11m / multi-sentence
    :op1 (s11x21 / 影响-01
        :ARG0 (s11x / 校服
            :mod (s11x20 / 强制))
        :ARG1 (s11x23 / 安全)
        :modal-strength neutral-affirmative
        :aspect process)
    :op2 (s11x24 / 指引-01
        :ARG0 (s11x6 / 部门
            :mod (s11x7 / 教育))
        :ARG1 (s11x8 / 学校)
        :ARG2 (s11x15 / 着重-01
            :ARG0 s11x8
            :ARG1 (s11x17 / 体验-01
                :ARG0 (s11x18 / 学生)
                :ARG1 (s11x16 / 安全)
                :aspect process)
            :manner (s11x19 / 生命-至上)
            :modal-strength partial-affirmative
            :aspect habitual)
        :aspect performance))

# alignment:
s11a2: 0-0
s11a3: 0-0
s11h: 0-0
s11i2: 0-0
s11o: 0-0
s11x: 2-2
s11x15: 15-15
s11x16: 5-5
s11x17: 17-17
s11x18: 16-16
s11x19: 12-12
s11x20: 1-1
s11x21: 4-4
s11x23: 5-5
s11x24: 9-9
s11x6: 8-8
s11x7: 7-7
s11x8: 10-10

# document level annotation:
(s11s0 / sentence
    :temporal ()
    :modal ((root :modal author)
            (author :full-affirmative s11x24)
            (author :neutral-affirmative s11x21)
            (author :full-affirmative s11x6)
            (s11x6 :partial-affirmative s11x15))
    :coref ()
)

## chinese_umr-0018, sentence 19

# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73
Words: 根据 以军 的 说法 ， 他们 得到 情报 称 当时 发现 有 一名 持有 枪械 的 武装 人员 混 在 该 货车 中 ， 该名 武装 人员 和 货车 停留 在 仓库 中 ， 而 世界 中央 厨房 的 车队 则 按照 事先 获得 以军 批准 的 路线 离开 仓库 ， 但 负责 确保 世界 中央 厨房 车队 行驶 路线 安全 的 部门 “为了确保交通路线安全”， 还是 向 无人机 操作员 下达 了 攻击 命令 。

# sentence level graph:
(s19x / say-91
	:ARG0 (s19x2 / armed-organization
		:name (s19n3 / name
			:op1 "以军"))
	:ARG1 (s19c / contrast-91
		:ARG1 (s19x5 / 得到-01
			:ARG0 s19x2
			:ARG1 (s19x6 / 情报
				:ARG0-of (s19i2 / say-91
					:ARG1 (s19x7 / 发现-01
						:ARG1 (s19a / and
							:op1 (s19x9 / 混-03
								:ARG0 (s19x12 / 人员
									:unit (s19x13 / 名)
									:quant 1
									:ARG0-of (s19x14 / 持有-01
										:ARG1 (s19x15 / 枪械)
										:aspect state)
									:mod (s19x16 / 武装))
								:place (s19x10 / 货车
									:mod (s19x11 / 该))
								:aspect state)
							:op2 (s19x17 / 停留-01
								:ARG0 (s19a2 / and
									:op1 s19x12
									:op2 s19x10)
								:ARG1 (s19x18 / 仓库)
								:aspect state))
						:temporal (s19x8 / 当时)
						:aspect performance)))
			:aspect performance)
		:ARG2 (s19b / contrast-91
			:ARG1 (s19x3 / 离开-01
				:ARG0 (s19x19 / 车队
					:possessor (s19i4 / international-organization
						:name (s19n / name
							:op1 "世界"
							:op2 "中央"
							:op3 "厨房")))
				:ARG1 s19x18
				:manner (s19x25 / 按照-01
					:ARG1 (s19x20 / 路线
						:ARG1-of (s19x24 / 批准-01
							:ARG0 s19x2
							:temporal (s19x22 / 事先)
							:aspect performance))
					:aspect performance)
				:aspect performance)
			:ARG2 (s19x4 / 下达-01
				:ARG0 (s19x26 / 部门
					:ARG0-of (s19x29 / 负责-01
						:ARG1 (s19x30 / 确保-01
							:ARG0 s19x26
							:ARG1 (s19x23 / 安全-01
								:ARG0 (s19x31 / 路线
									:path-of (s19x32 / 行驶-01
										:ARG0 s19x19
										:aspect activity))
								:aspect state)
							:aspect performance)
						:aspect state))
				:ARG1 (s19x27 / 命令
					:mod (s19x28 / 攻击-01
						:ARG0 (s19x38 / 操作员
							:mod (s19x39 / 无人机))
						:aspect performance))
				:ARG2 s19x38
				:aspect performance
				:purpose (s19x34 / 确保-01
					:ARG0 s19x26
					:ARG1 (s19x35 / 安全-01
						:ARG0 (s19x36 / 路线
							:mod (s19x37 / 交通))
						:aspect state)
					:aspect performance)))))

# alignment:
s19a: 0-0
s19a2: 0-0
s19b: 0-0
s19c: 0-0
s19c3: 0-0
s19i2: 0-0
s19i3: 0-0
s19i4: 0-0
s19n: 0-0
s19n3: 0-0
s19x: 4-4
s19x10: 22-22
s19x11: 21-21
s19x12: 18-18
s19x13: 13-13
s19x14: 14-14
s19x15: 15-15
s19x16: 17-17
s19x17: 30-30
s19x18: 32-32
s19x19: 40-40
s19x2: 0-0
s19x20: 48-48
s19x21: 44-44
s19x22: 43-43
s19x23: 61-61
s19x24: 46-46
s19x25: 42-42
s19x26: 63-63
s19x27: 72-72
s19x28: 71-71
s19x29: 53-53
s19x3: 49-49
s19x30: 54-54
s19x31: 48-48
s19x32: 59-59
s19x34: 54-54
s19x35: 61-61
s19x36: 48-48
s19x37: 64-64
s19x38: 68-68
s19x39: 67-67
s19x4: 69-69
s19x5: 7-7
s19x6: 8-8
s19x7: 11-11
s19x8: 10-10
s19x9: 19-19
s23h: 0-0

# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19x5)
            (s19x3 :overlap s19x29)
            (s19x29 :overlap s19x30)
            (s19x30 :overlap s19x32)
            (s19x32 :overlap s19x23)
            (s19x30 :overlap s19x34)
            (s19x34 :overlap s19x35)
            (s19x3 :overlap s19x4)
            (s19x3 :after s19x28)
            (s19x5 :before s19x7)
            (s19x7 :before s19x14)
            (s19x14 :overlap s19x9)
            (s19x9 :overlap s19x17)
            (s19x17 :after s19x25)
            (s19x3 :before s19x24))
    :modal ((root :modal author)
            (s19x26 :partial-affirmative purpose)
            (purpose :full-affirmative s19x34)
            (author :full-affirmative s19x)
            (author :full-affirmative s19x2)
            (s19x2 :full-affirmative s19x14)
            (s19x2 :full-affirmative s19x9)
            (s19x2 :full-affirmative s19x17)
            (s19x2 :full-affirmative s19x7)
            (s19x2 :full-affirmative s19x5)
            (s19x2 :full-affirmative s19x24)
            (s19x2 :full-affirmative s19x25)
            (s19x2 :full-affirmative s19x3)
            (s19x2 :full-affirmative s19x32)
            (s19x2 :partial-affirmative s19x23)
            (s19x2 :partial-affirmative s19x30)
            (s19x2 :full-affirmative s19x29)
            (s19x2 :partial-affirmative s19x28)
            (s19x2 :full-affirmative s19x4)
            (author :full-affirmative s19x26)
            (purpose :full-affirmative s19x35))
    :coref ((s15x20 :same-entity s19x2)
            (s13i2 :same-entity s19i4)
            (s15x5 :same-entity s19x19)
            (s14x15 :same-entity s19x10)
            (s15x2 :same-entity s19x18))
)

## chinese_umr-0018, sentence 21

# :: snt21
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
Words: 调查 报导 组织 啤令猫 进行 影像 分析 并 报导 这次 空袭 具有 “ 以色列 的 精准 空袭 的 特征 ” ， 第一次 空袭 的 全球 定位 坐标 是 北纬 31.4118 ° 东经 34.3231 ° [ 坐标 1 ] ， 第二次 是 北纬 31.4168 ° 东经 34.3290 ° [ 坐标 2 ] ， 而 第三次 是 北纬 31.4005 ° 东经 34.3115 ° [ 坐标 3 ] 。

# sentence level graph:
(s21a / and
	:op1 (s21x2 / 分析-01
		:ARG0 (s21o2 / organization
			:name (s21n2 / name
				:op1 "啤令猫")
			:ARG1-of (s21i2 / identity-91
				:ARG2 (s21x7 / 组织
					:mod (s21a2 / and
						:op1 (s21x8 / 调查-01
							:aspect process)
						:op2 (s21x9 / 报导-01
							:aspect process)))))
		:ARG1 (s21x3 / 影像)
		:aspect performance)
	:op2 (s21x4 / 报导-01
		:ARG0 s21o2
		:ARG1 (s21e / have-91
			:ARG0 (s21x / 空袭-01
				:mod (s21x5 / 这次)
				:ARG2-of (s21i3 / include-91
					:ARG1 (s21a3 / and
						:op1 (s21x12 / 空袭-01
							:ord (s21o / ordinal-entity
								:value 1)
							:place (s21g / geographical-coordinate-entity
								:lat 31.4118
								:long 34.3231)
							:aspect performance)
						:op2 (s21i5 / 空袭-01
							:ord (s21o3 / ordinal-entity
								:value 2)
							:place (s21g2 / geographical-coordinate-entity
								:lat 31.4168
								:long 34.3290)
							:aspect performance)
						:op3 (s21i6 / 空袭-01
							:ord (s21o4 / ordinal-entity
								:value 3)
							:place (s21g3 / geographical-coordinate-entity
								:lat 31.4005
								:long 34.3115)
							:aspect performance)))
				:aspect performance)
			:ARG1 (s21x6 / 特征
				:possessor (s21x10 / 空袭-01
					:ARG0 (s21c2 / country
						:name (s21n / name
							:op1 "以色列"))
					:manner (s21x11 / 精准)
					:aspect process)))
		:aspect performance))

# alignment:
s21a: 0-0
s21a2: 0-0
s21a3: 0-0
s21c2: 0-0
s21e: 0-0
s21g: 0-0
s21g2: 0-0
s21g3: 0-0
s21i2: 0-0
s21i3: 0-0
s21i4: 0-0
s21i5: 0-0
s21i6: 0-0
s21n: 0-0
s21n2: 0-0
s21o: 0-0
s21o2: 0-0
s21o3: 0-0
s21o4: 0-0
s21x: 11-11
s21x10: 11-11
s21x11: 16-16
s21x12: 11-11
s21x2: 7-7
s21x3: 6-6
s21x4: 2-2
s21x5: 10-10
s21x6: 19-19
s21x7: 3-3
s21x8: 1-1
s21x9: 2-2

# document level annotation:
(s21s0 / sentence
    :temporal ((s21x2 :after s21x4)
            (s21x2 :before s21x)
            (s21x :overlap s21e)
            (document-creation-time :overlap s21x8)
            (s21x8 :overlap s21x9)
            (s21x9 :overlap s21x2)
            (s21x :overlap s21x12)
            (s21x :overlap s21i5)
            (s21x :overlap s21i6)
            (s21x :overlap s21x10))
    :modal ((root :modal author)
            (author :full-affirmative s21x8)
            (author :full-affirmative s21x9)
            (author :full-affirmative s21x2)
            (author :full-affirmative s21x12)
            (author :full-affirmative s21i5)
            (author :full-affirmative s21i6)
            (author :full-affirmative s21x)
            (author :full-affirmative s21x10)
            (author :full-affirmative s21x4))
    :coref ()
)

## chinese_umr-0018, sentence 1

# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
Words: 世界 中央 厨房 车队 加沙 遇袭 案 是 指 2024 年 4 月 1 日 晚 以色列 国防军 对 人道主义 组织 世界 中央 厨房 的 车队 连续 进行 的 3 次 无人机 空袭 事件 ， 当时 该 车队 正在 加沙 地带 中部 城市 代尔拜莱赫 提供 人道 粮食 援助 。

# sentence level graph:
(s1i2 / identity-91
	:ARG1 (s1x14 / 案
		:ARG1-of (s1i3 / identity-91
			:ARG2 (s1x15 / 遇袭-00
				:ARG0 (s1x16 / 车队
					:possessor (s1i6 / international-organization
						:name (s1n7 / name
							:op1 "世界"
							:op2 "中央"
							:op3 "厨房")))
				:place (s1l / local-region
					:name (s1n / name
						:op1 "加沙"))
				:aspect performance)
			:aspect state))
	:ARG2 (s1x4 / 事件
		:mod (s1x / 空袭-01
			:ARG0 (s1a / armed-organization
				:name (s1n3 / name
					:op1 "以色列"
					:op2 "国防军"))
			:ARG1 (s1x2 / 车队
				:possessor (s1i4 / international-organization
					:name (s1n4 / name
						:op1 "世界"
						:op2 "中央"
						:op3 "厨房")
					:ARG1-of (s1i5 / identity-91
						:ARG2 (s1x6 / 组织
							:mod (s1x7 / 人道主义))
						:aspect state)))
			:instrument (s1x5 / 无人机)
			:frequency 3
			:manner (s1x3 / 连续)
			:temporal (s1t / date-entity
				:year 2024
				:month 4
				:day 1
				:dayperiod (s1x8 / 晚))
			:temporal (s1x9 / 提供-01
				:ARG0 s1x2
				:ARG1 (s1x10 / 援助-01
					:ARG1 (s1x11 / 粮食)
					:mod (s1x12 / 人道)
					:aspect process)
				:place (s1c2 / city
					:name (s1n5 / name
						:op1 "代尔拜莱赫")
					:part-of (s1x13 / 中部
						:part-of (s1l2 / local-region
							:name (s1n6 / name
								:op1 "加沙"
								:op2 "地带"))))
				:aspect activity)
			:aspect performance
			:unit (s1x17 / 次)))
	:aspect state)

# alignment:
s1a: 0-0
s1c: 0-0
s1c2: 0-0
s1i2: 0-0
s1i3: 0-0
s1i4: 0-0
s1i5: 0-0
s1i6: 0-0
s1l: 0-0
s1l2: 0-0
s1n: 0-0
s1n2: 0-0
s1n3: 0-0
s1n4: 0-0
s1n5: 0-0
s1n6: 0-0
s1n7: 0-0
s1t: 0-0
s1x: 33-33
s1x10: 48-48
s1x11: 47-47
s1x12: 46-46
s1x13: 42-42
s1x14: 7-7
s1x15: 6-6
s1x16: 4-4
s1x17: 31-31
s1x2: 4-4
s1x3: 27-27
s1x4: 34-34
s1x5: 32-32
s1x6: 21-21
s1x7: 20-20
s1x8: 16-16
s1x9: 45-45

# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1t)
            (s1t :contained s1x15)
            (s1x15 :overlap s1x)
            (s1x :overlap s1x9)
            (s1x9 :overlap s1x10)
            (document-creation-time :overlap s1i3)
            (document-creation-time :overlap s1i5))
    :modal ((root :modal author)
            (author :full-affirmative s1x9)
            (author :full-affirmative s1x)
            (author :full-affirmative s1x15)
            (author :full-affirmative s1x10)
            (author :full-affirmative s1i2)
            (author :full-affirmative s1i3)
            (author :full-affirmative s1i5))
    :coref ()
)

## chinese_umr-0002, sentence 60

# :: snt60
Index: 1  2   3 4  5  6 7  8 9  10   11 12   13 14   15 16  17 18  19 20 21 22 23 24 25 26 27 28  29 30 31 32 33 34  35 36 37 38 39 40   41 42 43 44 45 46   47 48  49 50  51 52  53 54  55 56 57 58 59
Words: 多国 领导人 和 政府 表达 了 慰问 ， 包括 亚美尼亚 、  澳大利亚 、  亚塞拜然 、  比利时 、  加拿大 、  中国 、  法国 、  德国 、  希腊 、  匈牙利 、  印度 、  伊朗 、  以色列 、  日本 、  肯亚 、  马来西亚 、  荷兰 、  挪威 、  巴勒斯坦 、  菲律宾 、  俄罗斯 、  新加坡 、  西班牙 、  瑞典 和  美国 。 

# sentence level graph:
(s60a / and
    :op1 (s60x / 表达-01
        :ARG0 (s60a2 / and
            :op1 (s60x9 / 领导人
                :mod (s60x7 / 国
                    :quant (s60x10 / 多)))
            :op2 (s60x8 / 政府
                :mod s60x7))
        :ARG1 (s60x3 / 慰问-01
            :aspect performance)
        :aspect performance)
    :op2 (s60x2 / 包括-01
        :ARG1 (s60a3 / and
            :op1 (s60c / country
                :name (s60n / name
                    :op1 "亚美尼亚"))
            :op2 (s60c2 / country
                :name (s60n2 / name
                    :op1 "澳大利亚"))
            :op3 (s60c3 / country
                :name (s60n3 / name
                    :op1 "亚塞拜然"))
            :op4 (s60c4 / country
                :name (s60n4 / name
                    :op1 "比利时"))
            :op5 (s60c5 / country
                :name (s60n5 / name
                    :op1 "加拿大"))
            :op6 (s60c6 / country
                :name (s60n6 / name
                    :op1 "中国"))
            :op7 (s60c7 / country
                :name (s60n7 / name
                    :op1 "法国"))
            :op8 (s60c8 / country
                :name (s60n8 / name
                    :op1 "德国"))
            :op9 (s60c9 / country
                :name (s60n9 / name
                    :op1 "希腊"))
            :op10 (s60c10 / country
                :name (s60n10 / name
                    :op1 "匈牙利"))
            :op11 (s60c11 / country
                :name (s60n11 / name
                    :op1 "印度"))
            :op12 (s60c12 / country
                :name (s60n12 / name
                    :op1 "伊朗"))
            :op13 (s60c13 / country
                :name (s60n13 / name
                    :op1 "以色列"))
            :op14 (s60c14 / country
                :name (s60n14 / name
                    :op1 "日本"))
            :op15 (s60c15 / country
                :name (s60n15 / name
                    :op1 "肯亚"))
            :op16 (s60c16 / country
                :name (s60n16 / name
                    :op1 "马来西亚"))
            :op17 (s60c17 / country
                :name (s60n17 / name
                    :op1 "荷兰"))
            :op18 (s60c18 / country
                :name (s60n18 / name
                    :op1 "挪威"))
            :op19 (s60c19 / country
                :name (s60n19 / name
                    :op1 "巴勒斯坦"))
            :op20 (s60c20 / country
                :name (s60n20 / name
                    :op1 "菲律宾"))
            :op21 (s60c21 / country
                :name (s60n21 / name
                    :op1 "俄罗斯"))
            :op22 (s60c22 / country
                :name (s60n22 / name
                    :op1 "新加坡"))
            :op23 (s60c23 / country
                :name (s60n23 / name
                    :op1 "西班牙"))
            :op24 (s60c24 / country
                :name (s60n24 / name
                    :op1 "瑞典"))
            :op25 (s60c25 / country
                :name (s60n25 / name
                    :op1 "美国")))
        :aspect state))


# alignment:
s60a: 0-0
s60a2: 0-0
s60a3: 0-0
s60c: 0-0
s60c10: 0-0
s60c11: 0-0
s60c12: 0-0
s60c13: 0-0
s60c14: 0-0
s60c15: 0-0
s60c16: 0-0
s60c17: 0-0
s60c18: 0-0
s60c19: 0-0
s60c2: 0-0
s60c20: 0-0
s60c21: 0-0
s60c22: 0-0
s60c23: 0-0
s60c24: 0-0
s60c25: 0-0
s60c3: 0-0
s60c4: 0-0
s60c5: 0-0
s60c6: 0-0
s60c7: 0-0
s60c8: 0-0
s60c9: 0-0
s60n: 0-0
s60n10: 0-0
s60n11: 0-0
s60n12: 0-0
s60n13: 0-0
s60n14: 0-0
s60n15: 0-0
s60n16: 0-0
s60n17: 0-0
s60n18: 0-0
s60n19: 0-0
s60n2: 0-0
s60n20: 0-0
s60n21: 0-0
s60n22: 0-0
s60n23: 0-0
s60n24: 0-0
s60n25: 0-0
s60n3: 0-0
s60n4: 0-0
s60n5: 0-0
s60n6: 0-0
s60n7: 0-0
s60n8: 0-0
s60n9: 0-0
s60x: 5-5
s60x10: 1-1
s60x2: 9-9
s60x3: 7-7
s60x7: 1-1
s60x8: 4-4
s60x9: 2-2

# document level annotation:
(s60s0 / sentence
    :temporal ((document-creation-time :before s60x)
        (s60x :overlap s60x2))
    :modal ((root :modal author)
        (author :full-affirmative s60x3)
        (author :full-affirmative s60x)
        (author :full-affirmative s60x2)))

## chinese_umr-0002, sentence 32

# :: snt32
Index: 1  2  3    4 5  6 7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
Words: 情报 机构 我行我素 的 官员 的 这种 背叛 行为 被  认为 对  国际 调查 行动 取得 成功 极其 不利 ，  表明 美国 和  法国 行动 安全 的  漏洞 正  不断 扩大 。 

# sentence level graph:
(s32a / and
    :op1 (s32x / 认为-02
        :ARG1 (s32x3 / 行为
            :mod (s32x4 / 背叛-01
                :ARG0 (s32x6 / 官员
                    :mod (s32x7 / 我行我素)
                    :ARG1-of (s32h / have-org-role-91
                        :ARG2 (s32x8 / 机构
                            :mod (s32x9 / 情报))))
                :aspect performance
                :quote (s32s / s32i2))
            :mod (s32x5 / 这种))
        :ARG2 (s32x10 / 不利-01
            :ARG1 (s32x11 / 成功-01
                :ARG0 (s32x12 / 行动-01
                    :mod (s32x13 / 调查-01
                        :mod (s32x14 / 国际)
                        :aspect activity
                        :quote s32i2)
                    :aspect activity
                    :quote s32i2)
                :aspect process)
            :degree intensifier
            :aspect state
            :quote s32i2)
        :aspect state
        :quote (s32i2 / implicit-predicate))
    :op2 (s32x2 / 表明-01
        :ARG0 s32x3
        :ARG1 (s32x15 / 不断-01
            :ARG0 (s32x16 / 扩大-01
                :ARG1 (s32x17 / 漏洞
                    :mod (s32x18 / 安全))
                :aspect state
                :quote s32i2)
            :aspect state
            :quote s32i2
            :temporal (s32x19 / 正))
        :aspect performance
        :quote s32i2))


# alignment:
s32a: 0-0
s32h: 0-0
s32i2: 0-0
s32s: 0-0
s32x: 11-11
s32x10: 19-19
s32x11: 17-17
s32x12: 15-15
s32x13: 14-14
s32x14: 13-13
s32x15: 30-30
s32x16: 31-31
s32x17: 28-28
s32x18: 26-26
s32x19: 29-29
s32x2: 21-21
s32x3: 9-9
s32x4: 8-8
s32x5: 7-7
s32x6: 5-5
s32x7: 3-3
s32x8: 2-2
s32x9: 1-1

# document level annotation:
(s32s0 / sentence
    :temporal ((s32x :before s32x4)
        (s32x :overlap s32x10)
        (s32x10 :overlap s32x11)
        (s32x11 :overlap s32x12)
        (s32x12 :overlap s32x13)
        (s32x :overlap s32x2)
        (s32x2 :overlap s32x15)
        (s32x15 :overlap s32x16))
    :modal ((root :modal author)
        (s32x6 :full-affirmative s32x4)
        (author :full-affirmative s32x13)
        (author :full-affirmative s32x6)
        (author :full-affirmative s32x12)
        (author :full-affirmative s32x6)
        (s32x6 :full-affirmative s32x11)
        (author :full-affirmative s32x10)
        (author :full-affirmative s32x6)
        (author :full-affirmative s32x)
        (author :full-affirmative s32x6)
        (s32x6 :full-affirmative s32x16)
        (author :full-affirmative s32x15)
        (author :full-affirmative s32x6)
        (author :full-affirmative s32x2)
        (author :full-affirmative s32x6))
    :coref ((s30x :same-event s32i2)))

## chinese_umr-0001, sentence 19

# :: snt19
Index: 1  2  3  4 5  6  7 8  9 10 11 12 13 14 15 16  17 18 19  20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了  一篇 「  美国 买通 外星人 去  追杀 宾拉登 」  。 

# sentence level graph:
(s19h / have-reason-91
    :ARG1 (s19x / 报导-01
        :ARG0 (s19p / person
            :refer-number plural
            :refer-person 3rd)
        :ARG1 (s19p2 / publication
            :name (s19n / name
                :op1 "「"
                :op2 "美国"
                :op3 "买通"
                :op4 "外星人"
                :op5 "去"
                :op6 "追杀"
                :op7 "宾拉登"
                :op8 "」")
            :unit (s19x7 / 篇)
            :quant 1)
        :mod (s19x3 / 也
            :unit (s19x4 / 篇)
            :quant 1)
        :aspect performance)
    :ARG2 (s19x2 / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19x5 / 政策
            :topic (s19x6 / 外交)
            :possessor (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect performance))


# alignment:
s19c: 0-0
s19h: 0-0
s19n: 0-0
s19n2: 0-0
s19p: 0-0
s19p2: 0-0
s19x: 10-10
s19x2: 2-2
s19x3: 9-9
s19x4: 12-12
s19x5: 6-6
s19x6: 5-5
s19x7: 12-12

# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19x)
        (s19x :overlap s19x2))
    :modal ((root :modal author)
        (author :full-affirmative s19x)
        (author :full-affirmative s19x2))
    :coref ((s17x4 :same-entity s19p)))

## chinese_umr-0006, sentence 5

# :: snt5
Index: 1 2  3   4 5  6    7 8  9  10 11 12 13 14    15 16    17 18 19 20 21   22 23 24   25 26 27 28 29 30 31  32 33 34   35  36 37 38 39 40    41 42 43 44 45 46 47
Words: 而 冠军 设计师 可 得到 美丽佳人 的 杂志 内页 特别 专访 、  一辆 2013年 型  Lexus GS 汽车 、  由  惠普公司 提供 价值 五万美元 的  科技 和  设备 、  由  欧莱雅 提供 的  十万美元 创业金 ，  以及 获得 在  罗德与泰勒 销售 其  设计 的  成衣 的  机会

# sentence level graph:
(s5a / and
    :op1 (s5x / 得到-01
        :ARG0 (s5x2 / 设计师
            :mod (s5x3 / 冠军))
        :ARG1 (s5a2 / and
            :op1 (s5x4 / 专访-01
                :ARG0 (s5m3 / magazine
                    :name (s5n / name
                        :op1 "美丽佳人"))
                :ARG1 s5x2
                :mod (s5x5 / 内页
                    :part (s5x6 / 杂志))
                :mod (s5x8 / 特别)
                :aspect performance)
            :op2 (s5v / vehicle
                :name (s5n2 / name
                    :op1 "Lexus"
                    :op2 "GS"
                    :op3 "汽车")
                :mod (s5x9 / 型
                    :temporal (s5d / date-entity
                        :year 2013))
                :quant 1
                :unit (s5x10 / 辆))
            :op3 (s5a3 / and
                :op1 (s5x11 / 科技)
                :op2 (s5x12 / 设备)
                :ARG1-of (s5x13 / 提供-01
                    :ARG0 (s5c / company
                        :name (s5n3 / name
                            :op1 "惠普公司"))
                    :aspect performance)
                :ARG0-of (s5x14 / 价值-01
                    :ARG1 (s5m / monetary-quantity
                        :unit (s5x15 / 美元)
                        :quant (s5x7 / 50000))
                    :aspect state))
            :op4 (s5x17 / 创业金
                :ARG1-of (s5x20 / 提供-01
                    :ARG0 (s5c2 / company
                        :name (s5n4 / name
                            :op1 "欧莱雅"))
                    :aspect performance)
                :ARG1-of (s5i2 / identity-91
                    :ARG2 (s5m2 / monetary-quantity
                        :unit (s5x16 / 美元)
                        :quant (s5x18 / 100000))
                    :aspect state)))
        :aspect performance)
    :op2 (s5x27 / 获得-01
        :ARG0 s5x2
        :ARG1 (s5x21 / 机会
            :ARG1-of (s5i3 / identity-91
                :ARG1 (s5x22 / 销售-01
                    :ARG1 (s5x23 / 成衣
                        :ARG1-of (s5x24 / 设计-01
                            :ARG0 s5x2
                            :aspect performance))
                    :place (s5c3 / company
                        :name (s5n5 / name
                            :op1 "罗德与泰勒"))
                    :aspect performance)
                :aspect state))
        :aspect performance))


# alignment:
s5a: 0-0
s5a2: 0-0
s5a3: 0-0
s5c: 0-0
s5c2: 0-0
s5c3: 0-0
s5d: 0-0
s5i2: 0-0
s5i3: 0-0
s5m: 0-0
s5m2: 0-0
s5m3: 0-0
s5n: 0-0
s5n2: 0-0
s5n3: 0-0
s5n4: 0-0
s5n5: 0-0
s5v: 0-0
s5x: 5-5
s5x10: 13-13
s5x11: 26-26
s5x12: 28-28
s5x13: 22-22
s5x14: 23-23
s5x15: 24-24
s5x16: 24-24
s5x17: 35-35
s5x18: 0-0
s5x2: 3-3
s5x20: 22-22
s5x21: 47-47
s5x22: 41-41
s5x23: 45-45
s5x24: 43-43
s5x27: 38-38
s5x3: 2-2
s5x4: 11-11
s5x5: 9-9
s5x6: 8-8
s5x7: 0-0
s5x8: 10-10
s5x9: 15-15

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x)
        (s5x :overlap s5x4)
        (s5x :overlap s5x13)
        (s5x :overlap s5x14)
        (s5x :overlap s5x20)
        (s5x :overlap s5x27)
        (s5x27 :overlap s5x22)
        (s5x22 :before s5x24))
    :modal ((root :modal author)
        (author :full-affirmative s5x4)
        (author :full-affirmative s5x13)
        (author :full-affirmative s5x14)
        (author :full-affirmative s5x20)
        (author :full-affirmative s5i2)
        (author :neutral-affirmative s5x)
        (author :full-affirmative s5x24)
        (author :full-affirmative s5x22)
        (author :full-affirmative s5i3)
        (author :neutral-affirmative s5x27)))

## chinese_umr-0006, sentence 23

# :: snt23
Index: 1 2   3 4  5  6   7   8  9 10   11 12 13 14 
Words: 而 优胜者 会 获得 一部 笔记本 计算机 以及 由 惠普公司 提供 的  一  万美元

# sentence level graph:
(s23x / 获得-01
    :ARG0 (s23x2 / 优胜者)
    :ARG1 (s23a / and
        :op1 (s23x3 / 计算机
            :mod (s23x5 / 笔记本)
            :quant 1
            :unit (s23x6 / 部))
        :op2 (s23m / monetary-quantity
            :value 10000
            :unit (s23x4 / 美元)
            :ARG1-of (s23x7 / 提供-01
                :ARG0 (s23c / company
                    :name (s23n / name
                        :op1 "惠普公司"))
                :aspect performance)))
    :aspect performance)


# alignment:
s23a: 0-0
s23c: 0-0
s23m: 0-0
s23n: 0-0
s23x: 4-4
s23x2: 2-2
s23x3: 7-7
s23x4: 14-14
s23x5: 6-6
s23x6: 5-5
s23x7: 11-11

# document level annotation:
(s23s0 / sentence
    :temporal ((s22x2 :after s23x)
        (s23x :overlap s23x7))
    :modal ((root :modal author)
        (author :full-affirmative s23x7)
        (author :full-affirmative s23x))
    :coref ((s21c :same-entity s23c)))

## chinese_umr-0002, sentence 36

# :: snt36
Index: 1    2  3 4   5  6  7       8 9  10 11  12 13 14 15 16 17 18 19
Words: 曼彻斯特 居民 和 出租车 公司 透过 Twitter 向 滞留 在  演唱会 的  民众 提供 免费 交通 和  住宿 。 

# sentence level graph:
(s36x / 提供-01
    :ARG0 (s36a / and
        :op1 (s36x2 / 居民
            :place (s36c / city
                :name (s36n / name
                    :op1 "曼彻斯特")))
        :op2 (s36x3 / 公司
            :mod (s36x4 / 出租车)))
    :ARG1 (s36a2 / and
        :op1 (s36x5 / 交通
            :mod (s36x7 / 免费))
        :op2 (s36x6 / 住宿
            :mod s36x7))
    :ARG2 (s36x8 / 民众
        :ARG0-of (s36x9 / 滞留-01
            :ARG1 (s36x10 / 演唱会)
            :aspect state))
    :medium (s36c2 / cultural-artifact
        :name (s36n2 / name
            :op1 "Twitter"))
    :aspect performance)


# alignment:
s36a: 0-0
s36a2: 0-0
s36c: 0-0
s36c2: 0-0
s36n: 0-0
s36n2: 0-0
s36x: 14-14
s36x10: 11-11
s36x2: 2-2
s36x3: 5-5
s36x4: 4-4
s36x5: 16-16
s36x6: 18-18
s36x7: 15-15
s36x8: 13-13
s36x9: 9-9

# document level annotation:
(s36s0 / sentence
    :temporal ((document-creation-time :before s36x)
        (s36x :overlap s36x9))
    :modal ((root :modal author)
        (author :full-affirmative s36x7)
        (author :full-affirmative s36x9)
        (author :full-affirmative s36x))
    :coref ((s3s :same-event s36x10)
        (s33c4 :same-entity s36c)))

## chinese_umr-0008, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
Words: 虽然 美国 西岸 部分 地区 不 接受 纸币 ， 只能 使用 金币 和 银币 ， 但 东部 的 情况 截然 不同 ， 特别 是 在 经济 因 内战 爆发 而 陷入 动荡 后 ， 3 美元 金币 基本上 在 东部 的 商品 交易 中 难得 一见 ， 并且 此后 再也 没有 出现 过 大范围 流通 。

# sentence level graph:
(s8h / have-concession-91
    :ARG2 (s8a / and
        :op1 (s8x4 / 接受-01
            :ARG0 (s8x3 / 地区
                :quant (s8x8 / 部分)
                :place (s8x5 / 西岸
                    :part-of (s8c / country
                        :name (s8n / name
                            :op1 "美国"))))
            :ARG1 (s8x10 / 纸币)
            :polarity -
            :aspect state)
        :op2 (s8x2 / 使用-01
            :ARG1 (s8a2 / and
                :op1 (s8x11 / 金币)
                :op2 (s8x12 / 银币))
            :place s8x3
            :mod (s8x6 / 只能)
            :aspect habitual))
    :ARG1 (s8j / 截然不同-01
        :ARG0 (s8k / 情况
            :place (s8x25 / 东部
                :part-of s8c))
        :aspect state
        :example (s8a3 / and
            :op1 (s8x17 / 难得一见-01
                :ARG1 (s8x18 / 金币
                    :mod (s8m / monetary-quantity
                        :quant 3
                        :unit (s8x19 / 美元)))
                :mod (s8x27 / 基本上)
                :temporal (s8x28 / 交易-01
                    :ARG1 (s8x29 / 商品)
                    :place s8x25
                    :aspect activity)
                :temporal (s8x9 / 后
                    :op1 (s8x13 / 陷入-01
                        :ARG0 (s8x21 / 经济)
                        :ARG1 (s8x7 / 动荡)
                        :reason (s8x20 / 爆发-01
                            :ARG1 (s8x22 / 内战)
                            :aspect performance)
                        :aspect performance)
                    :mod (s8x / 特别))
                :aspect habitual)
            :op2 (s8x24 / 出现-01
                :ARG1 (s8x15 / 流通-01
                    :ARG0 s8x18
                    :mod (s8x16 / 大范围)
                    :aspect process)
                :temporal (s8x30 / 此后)
                :mod (s8x14 / 再也)
                :polarity -
                :aspect performance))))

# alignment:
s8a: 0-0
s8a2: 0-0
s8a3: 0-0
s8b2: 0-0
s8c: 0-0
s8c2: 0-0
s8c3: 0-0
s8j: 21-21
s8k: 19-19
s8n: 0-0
s8n3: 0-0
s8n4: 0-0
s8s: 0-0
s8x: 23-23
s8x10: 8-8
s8x11: 12-12
s8x12: 14-14
s8x13: 31-31
s8x14: 50-50
s8x15: 55-55
s8x16: 54-54
s8x17: 46-46
s8x18: 12-12
s8x19: 36-36
s8x2: 11-11
s8x20: 29-29
s8x21: 26-26
s8x22: 28-28
s8x23: 45-45
s8x24: 52-52
s8x25: 17-40
s8x27: 38-38
s8x28: 43-43
s8x29: 42-42
s8x3: 5-5
s8x30: 49-49
s8x4: 7-7
s8x5: 3-3
s8x6: 10-10
s8x7: 32-32
s8x8: 4-4
s8x9: 33-33

# document level annotation:
(s8s0 / sentence
    :temporal ((s8x20 :after s8x13)
            (document-creation-time :before s8x4)
            (document-creation-time :before s8x2)
            (document-creation-time :before s8j)
            (document-creation-time :before s8x20)
            (s8x13 :after s8x9)
            (s8x9 :contained s8x17)
            (s8x17 :overlap s8x28)
            (s8x13 :after s8x30)
            (s8x30 :contained s8x24)
            (s8x24 :overlap s8x15))
    :modal ((root :modal author)
            (author :full-negative s8x4)
            (author :full-affirmative s8j)
            (author :full-negative s8x24)
            (author :full-affirmative s8x13)
            (author :neutral-affirmative s8x2)
            (author :full-affirmative s8x20)
            (author :full-affirmative s8x17)
            (author :full-affirmative s8x28)
            (author :unspecified s8x15))
    :coref ((s1c :same-entity s8c)
            (s7x1 :same-entity s8x18))
)

## chinese_umr-0021, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79
Words: 另外 ， 发生 在 4 月 初 的 日全食 由于 全食 带 横穿 超过 半个 北美洲 地区 ， 而 在 月影 所 经过 的 国家 或 地区 也 有 超过 6 亿 人 可 欣赏 到 该 日食 ， 其中 超过 6.52 亿 人 可 欣赏 到 日偏食 ， 而 日食 前 预计 4380 万 人 将 在 月球 本影 所 经过 的 地区 可 欣赏 到 日全食 ， 也 因此 别称 为 “ 北美 大 日食 ” 。

# sentence level graph:
(s5x3 / 称为-01
	:ARG1 (s5e / 日全食
		:ARG1-of (s5x / 发生-01
			:temporal (s5d / date-entity
				:month 4
				:mod (s5x2 / 初))
			:aspect performance))
	:ARG2 (s5n / name
		:op1 (s5x4 / 北美)
		:op2 (s5x5 / 大)
		:op3 (s5x6 / 日食))
	:cause (s5a / and
		:op1 (s5x7 / 横穿-01
			:ARG0 (s5x8 / 全食带)
			:ARG1 (s5x11 / 地区
				:quant 0.5
				:unit (s5x10 / 个)
				:mod (s5x9 / 超过)
				:part-of (s5c / continent
					:name (s5n3 / name
						:op1 "北美洲")))
			:aspect activity)
		:op2 (s5x12 / 欣赏-01
			:ARG0 (s5p / person
				:quant 6
				:unit (s5x15 / 亿)
				:mod (s5x16 / 超过))
			:ARG1 s5e
			:place (s5o / or
				:op1 (s5x20 / 国家)
				:op2 (s5x21 / 地区))
			:ARG1-of (s5x18 / 经过-01
				:ARG0 (s5x19 / 月影)
				:ARG1 s5o
				:aspect activity)
			:aspect activity)
		:op3 (s5x22 / 欣赏-01
			:ARG0 (s5x23 / 人
				:quant 6.52
				:unit (s5x25 / 亿)
				:mod (s5x26 / 超过))
			:ARG1 (s5x24 / 日偏食)
			:aspect activity)
		:op4 (s5x31 / 预计-01
			:ARG1 (s5x27 / 欣赏-01
				:ARG0 (s5x28 / 人
					:quant 4380
					:unit (s5x30 / 万))
				:ARG1 s5e
				:place (s5x37 / 地区
					:ARG1-of (s5x34 / 经过-01
						:ARG0 (s5x35 / 本影
							:possessor (s5p2 / planet
								:name (s5n4 / name
									:op1 "月球")))
						:ARG1 s5x37
						:aspect activity))
				:aspect activity)
			:temporal (s5x32 / 前
				:op1 s5e)
			:aspect performance))
	:aspect state)

# alignment:
s5a: 0-0
s5c: 0-0
s5d: 0-0
s5e: 9-9
s5n: 0-0
s5n3: 0-0
s5o: 0-0
s5p: 0-0
s5x: 3-3
s5x10: 15-15
s5x12: 35-35
s5x13: 38-38
s5x15: 32-32
s5x16: 14-14
s5x17: 37-37
s5x18: 23-23
s5x19: 21-21
s5x2: 7-7
s5x20: 25-25
s5x21: 17-17
s5x22: 35-35
s5x23: 33-33
s5x24: 48-48
s5x25: 32-32
s5x26: 14-14
s5x27: 35-35
s5x28: 33-33
s5x29: 9-9
s5x3: 72-72
s5x30: 55-55
s5x31: 53-53
s5x32: 52-52
s5x33: 38-38
s5x34: 23-23
s5x35: 60-60
s5x36: 59-59
s5x4: 75-75
s5x5: 76-76
s5x6: 38-38
s5x7: 13-13
s5x8: 11-11
s5x9: 14-14

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x)
            (s5x7 :overlap s5x12)
            (s5x12 :overlap s5x18)
            (s5x22 :overlap s5x27)
            (s5x22 :contained s5x34))
    :modal ((root :modal author)
            (author :full-affirmative s5x7)
            (author :full-affirmative s5x18)
            (author :full-affirmative s5x12)
            (author :full-affirmative s5x22)
            (author :full-affirmative s5x31)
            (author :full-affirmative s5x34)
            (author :full-affirmative s5x27)
            (author :full-affirmative s5x3)
            (author :full-affirmative s5x))
    :coref ()
)

## chinese_umr-0002, sentence 40

# :: snt40
Index: 1  2   3 4 5 6  7 8 9    10 11 12 13 14 15 16 17  18 19 20 21 22 23 24  
Words: 首相 特雷莎 · 梅 称 事件 是 “ 骇人听闻 的  恐怖 袭击 ”  ，  并  在  第二天 早上 主持 了  民事 紧急 情况 委员会。

# sentence level graph:
(s40c / consecutive
    :op1 (s40x / 称-01
        :ARG0 (s40i3 / individual-person
            :name (s40n / name
                :op1 "特雷莎"
                :op2 "·"
                :op3 "梅")
            :ARG1-of (s40h / have-org-role-91
                :ARG3 (s40x3 / 首相)))
        :ARG1 (s40x4 / 事件)
        :ARG2 (s40x5 / 袭击-01
            :mod (s40x6 / 恐怖)
            :mod (s40x7 / 骇人听闻)
            :quote s40x
            :aspect performance)
        :aspect state)
    :op2 (s40x2 / 主持-01
        :ARG0 s40i3
        :ARG1 (s40x8 / 委员会
            :topic (s40x9 / 情况
                :manner (s40x10 / 紧急)
                :mod (s40x11 / 民事)))
        :aspect performance
        :temporal (s40x13 / 第二天
            :temporal (s40x14 / 早上))))


# alignment:
s40c: 0-0
s40h: 0-0
s40i3: 0-0
s40n: 0-0
s40x: 5-5
s40x10: 22-22
s40x11: 21-21
s40x13: 17-17
s40x14: 18-18
s40x2: 19-19
s40x3: 1-1
s40x4: 6-6
s40x5: 12-12
s40x6: 11-11
s40x7: 9-9
s40x8: 24-24
s40x9: 23-23

# document level annotation:
(s40s0 / sentence
    :temporal ((document-creation-time :before s40x)
        (s40x :after s40x2))
    :modal ((root :modal author)
        (author :full-affirmative s40h)
        (author :full-affirmative s40i3)
        (author :full-affirmative s40x2)
        (author :full-affirmative s40x))
    :coref ((s33x11 :same-event s40x4)))

## chinese_umr-0005, sentence 35

# :: snt35
Index: 1    2 3 4 5 6 7 8    9  10 11 12 13 14  15    16 17  18 19 20 21 22 23 24 25  26 27 28 29
Words: 2017 年 9 月 1 日 ， 第十二届 全国 人民 代表 大会 常务 委员会 第二十九次 会议 第三次 全体 会议 表决 通过 《  中华 人民 共和国 国歌 法  》  。 

# sentence level graph:
(s35x / 表决-01
    :ARG0 (s35x4 / 会议
        :ord (s35o2 / ordinal-entity
            :value 29
            :unit (s35x6 / 次))
        :part (s35p / political-organization
            :name (s35n2 / name
                :op1 "全国"
                :op2 "人民"
                :op3 "代表"
                :op4 "大会"
                :op5 "常务"
                :op6 "委员会")
            :ord (s35o3 / ordinal-entity
                :value 12
                :unit (s35x7 / 届))))
    :ARG1 (s35x2 / 通过-01
        :ARG1 (s35l / law
            :name (s35n / name
                :op1 "中华"
                :op2 "人民"
                :op3 "共和国"
                :op4 "国歌"
                :op5 "法"))
        :aspect performance)
    :aspect performance
    :temporal (s35d / date-entity
        :year 2017
        :month 9
        :day 1)
    :mod (s35x3 / 全体)
    :ord (s35o / ordinal-entity
        :unit (s35x5 / 次)
        :value 3))


# alignment:
s35d: 0-0
s35l: 0-0
s35n: 0-0
s35n2: 0-0
s35o: 0-0
s35o2: 0-0
s35o3: 0-0
s35p: 0-0
s35x: 20-20
s35x2: 21-21
s35x3: 18-18
s35x4: 16-16
s35x5: 15-15
s35x6: 15-15
s35x7: 8-8

# document level annotation:
(s35s0 / sentence
    :temporal ((s35d :overlap s35x)
        (s35x :overlap s35x2))
    :modal ((root :modal author)
        (author :full-affirmative s35x2)
        (author :full-affirmative s35x)))

## chinese_umr-0002, sentence 43

# :: snt43
Index: 1  2  3  4  5    6 7  8  9  10 11
Words: 各大 党派 宣布 暂停 2017 年 英国 大选 竞选 活动 。 

# sentence level graph:
(s43x / 宣布-01
    :ARG0 (s43x6 / 党派
        :mod (s43x7 / 各大))
    :ARG1 (s43x2 / 暂停-01
        :ARG0 (s43x3 / 活动
            :ARG1-of (s43i2 / identity-91
                :ARG2 (s43x4 / 竞选
                    :temporal (s43d / date-entity
                        :year 2017)
                    :place (s43c / country
                        :name (s43n / name
                            :op1 "英国"))
                    :mod (s43x5 / 大选))
                :aspect state))
        :aspect state
        :quote s43x)
    :aspect performance)


# alignment:
s43c: 0-0
s43d: 0-0
s43i2: 0-0
s43n: 0-0
s43x: 3-3
s43x2: 4-4
s43x3: 10-10
s43x4: 9-9
s43x5: 8-8
s43x6: 2-2
s43x7: 1-1

# document level annotation:
(s43s0 / sentence
    :temporal ((document-creation-time :before s43x)
        (document-creation-time :before s43d)
        (s43x :overlap s43x2))
    :modal ((root :modal author)
        (author :neutral-affirmative s43x4)
        (author :neutral-affirmative s43x6)
        (s43x6 :full-affirmative s43x2)
        (author :full-affirmative s43x)
        (author :full-affirmative s43x6)
        (author :full-affirmative s43i2)))

## chinese_umr-0025, sentence 418

# :: snt418
Index:  1  2  3      4  5  6  7    8  9 10
Words: 他  想  ，  说不定    它  还  会  活动   呢  ！ 

# sentence level graph:
(s418x2 / 想-01
	:ARG0 (s418x1 / individual-person
		:refer-person 3
		:refer-number singular)
	:ARG1 (s418x4 / 说不定-01
		:ARG0 (s418x7 / 会-03
			:ARG0 (s418x8 / 活动-01
				:ARG0 (s418x5 / individual-person
					:refer-person 3
					:refer-number singular)
				:modal-strength (s418x21 / neutral-affirmative
					:conceiver s418x1)
				:modal-predicate (s418x2 / 想-01))
			:mod (s418x6 / 还)
			:mode expressive)))

# alignment:
s418x1: 0-0
s418x2: 2-2
s418x21: 0-0
s418x4: 4-4
s418x5: 0-0
s418x6: 6-6
s418x7: 7-7
s418x8: 8-8

# document level annotation:
(s418s0 / sentence)

## chinese_umr-0001, sentence 14

# :: snt14
Index: 1  2   3 4  5   6  7  8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG0 (s14i2 / implicit-argument
        :ARG1-of (s14h / have-degree-91
            :ARG1 (s14x3 / 大)
            :ARG2 (s14x4 / 最)
            :ARG5 (s14x5 / 其中))
        :unit (s14x2 / 宗))
    :ARG1 (s14x6 / 活动-01
        :ARG0 (s14x7 / 外星人)
        :place (s14p / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect activity)
    :aspect state)


# alignment:
s14h: 0-0
s14i2: 0-0
s14n: 0-0
s14p: 0-0
s14x: 4-4
s14x2: 2-2
s14x3: 2-2
s14x4: 2-2
s14x5: 1-1
s14x6: 7-7
s14x7: 5-5

# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14x)
        (s14x :overlap s14x6))
    :modal ((root :modal author)
        (author :full-affirmative s14x6)
        (author :neutral-affirmative s14x)))

## chinese_umr-0001, sentence 20

# :: snt20
Index: 1  2 3  4  5 6  7 8  9   10 11  12 13 14 15 16  17 18 19 20  21  22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是  外星人 ！  」  甚至 被  好事者 贴到 了  美国 参议院 记者团 的  墙上 。 

# sentence level graph:
(s20x / 贴到-01
    :ARG0 (s20x2 / 者
        :ARG0-of (s20x3 / 好事-00
            :aspect state))
    :ARG1 (s20x4 / 墙上
        :place-of (s20x5 / 记者团
            :place (s20b / building
                :name (s20n / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :ARG2 (s20x6 / 新闻
        :unit (s20x7 / 篇)
        :quant 1
        :part-of (s20x8 / 刊
            :mod (s20x9 / 该))
        :ARG1-of (s20i2 / identity-91
            :ARG2 (s20p / publication
                :name (s20n2 / name
                    :op1 "「"
                    :op2 "12"
                    :op3 "位"
                    :op4 "美国"
                    :op5 "参议员"
                    :op6 "是"
                    :op7 "外星人"
                    :op8 "！"
                    :op9 "」"))
            :aspect state))
    :aspect performance)


# alignment:
s20b: 0-0
s20i2: 0-0
s20n: 0-0
s20n2: 0-0
s20p: 0-0
s20x: 17-17
s20x2: 16-16
s20x3: 16-16
s20x4: 23-23
s20x5: 21-21
s20x6: 4-4
s20x7: 3-3
s20x8: 1-1
s20x9: 1-1

# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20x)
        (s20x :overlap s20x3))
    :modal ((root :modal author)
        (author :full-affirmative s20x3)
        (author :full-affirmative s20i2)
        (author :full-affirmative s20x))
    :coref ((s17x4 :same-entity s20x8)))

## chinese_umr-0001, sentence 11

# :: snt11
Index: 1    2 3 4 5 6   7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23  24 25 26 27
Words: 2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了  《  世界 新闻 周报 》  的  发行 ，  不过 周报 的  网络版 仍  继续 生存 。 

# sentence level graph:
(s11b / but-91
    :ARG1 (s11x / 停止-01
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i2 / identity-91
                :ARG2 (s11x6 / 公司
                    :mod (s11x7 / 母))))
        :ARG1 (s11x8 / 发行-01
            :ARG0 s11c
            :ARG1 (s11n2 / newspaper
                :name (s11n3 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect process)
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :aspect performance)
    :ARG2 (s11x2 / 继续-01
        :ARG0 (s11x4 / 网络版
            :part-of (s11x5 / 周报))
        :ARG1 (s11x3 / 生存-01
            :ARG0 s11x4
            :aspect state)
        :temporal s11d
        :aspect activity))


# alignment:
s11b: 0-0
s11c: 0-0
s11d: 0-0
s11i2: 0-0
s11n: 0-0
s11n2: 0-0
s11n3: 0-0
s11x: 10-10
s11x2: 25-25
s11x3: 26-26
s11x4: 23-23
s11x5: 15-15
s11x6: 9-9
s11x7: 6-6
s11x8: 18-18

# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
        (s11d :overlap s11x)
        (s11x :overlap s11x8)
        (s11x :overlap s11x2)
        (s11x2 :overlap s11x3))
    :modal ((root :modal author)
        (author :full-affirmative s11x8)
        (author :full-affirmative s11x)
        (author :full-affirmative s11x3)
        (author :full-affirmative s11x2))
    :coref ((s11n2 :same-entity s11x5)))

## chinese_umr-0002, sentence 54

# :: snt54
Index: 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16   17 18 19 20   21 22 23 24 25
Words: 唱片 公司 其后 确定 取消 危险 尤物 世界 巡回 欧洲 场次 演出 ，  并  让  亚莉安娜 先  返回 美国 佛罗里达 州  的  家  休息 。 

# sentence level graph:
(s54a / and
    :op1 (s54x / 确定-01
        :ARG1 (s54x2 / 公司
            :mod (s54x3 / 唱片))
        :ARG2 (s54x4 / 取消-01
            :ARG1 (s54x5 / 演出-01
                :ARG1 (s54x6 / 场次
                    :part (s54e / event
                        :name (s54n / name
                            :op1 "危险"
                            :op2 "尤物"
                            :op3 "世界"
                            :op4 "巡回"))
                    :place (s54c / continent
                        :name (s54n2 / name
                            :op1 "欧洲")))
                :aspect process)
            :aspect performance)
        :aspect state
        :temporal (s54x11 / 其后))
    :op2 (s54x7 / 让-02
        :ARG0 s54x2
        :ARG1 (s54i2 / individual-person
            :name (s54n3 / name
                :op1 "亚莉安娜"))
        :ARG2 (s54a2 / and
            :op1 (s54x8 / 返回-01
                :ARG0 s54i2
                :ARG1 (s54x10 / 家
                    :place (s54s / state
                        :name (s54n4 / name
                            :op1 "佛罗里达"
                            :op2 "州")
                        :place (s54c2 / country
                            :name (s54n5 / name
                                :op1 "美国"))))
                :aspect performance)
            :op2 (s54x9 / 休息-01
                :ARG0 s54i2
                :aspect performance))
        :aspect performance
        :mod (s54x12 / 先)))


# alignment:
s54a: 0-0
s54a2: 0-0
s54c: 0-0
s54c2: 0-0
s54e: 0-0
s54i2: 0-0
s54n: 0-0
s54n2: 0-0
s54n3: 0-0
s54n4: 0-0
s54n5: 0-0
s54s: 0-0
s54x: 4-4
s54x10: 23-23
s54x11: 3-3
s54x12: 17-17
s54x2: 2-2
s54x3: 1-1
s54x4: 5-5
s54x5: 12-12
s54x6: 11-11
s54x7: 15-15
s54x8: 18-18
s54x9: 24-24

# document level annotation:
(s54s0 / sentence
    :temporal ((document-creation-time :before s54x)
        (s54x :overlap s54x4)
        (s54x4 :after s54x5)
        (s54x :overlap s54x7)
        (s54x7 :overlap s54x8)
        (s54x8 :overlap s54x9))
    :modal ((root :modal author)
        (author :full-affirmative s54x5)
        (author :full-affirmative s54x4)
        (author :full-affirmative s54x)
        (author :full-affirmative s54x8)
        (author :full-affirmative s54x9)
        (author :full-affirmative s54x7))
    :coref ((s53i2 :same-entity s54i2)))

## chinese_umr-0012, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 阿耀 向 维基 新闻 表示 ： “ 有时 压力 并 不 是 一件 坏事 ， 因为 只有 压力 才 会 推动 一个 人 去 发挥 他 所有 的 力 和 爆发 他 的 小宇宙 。”

# sentence level graph:
(s8x / 表示-01
	:ARG0 (s8p / person
		:name (s8n / name
			:op1 "阿耀"))
	:ARG1 (s8c / have-cause-91
		:ARG1 (s8i3 / identity-91
			:ARG1 (s8x18 / 压力)
			:ARG2 (s8x15 / 坏事
				:unit (s8x16 / 件)
				:quant (s8x17 / 一))
			:temporal (s8x14 / 有时)
			:polarity -
			:aspect state)
		:ARG2 (s8x2 / 推动-01
			:ARG0 (s8x3 / 压力
				:mod (s8x13 / 只有))
			:ARG1 (s8x4 / 人
				:quant (s8x5 / 一)
				:unit (s8x6 / 个))
			:ARG2 (s8a / and
				:op1 (s8x7 / 发挥-01
					:ARG0 s8x4
					:ARG1 (s8x8 / 力
						:quant (s8x9 / 所有)
						:possessor s8x4)
					:aspect performance)
				:op2 (s8x11 / 爆发-01
					:ARG0 s8x4
					:ARG1 (s8x12 / 小宇宙
						:possessor s8x4)
					:aspect performance))
			:mod (s8x19 / 才)
			:aspect process
			:modal-strength full-affirmative)
		:quote s8x)
	:ARG2 (s8n2 / newspaper
		:name (s8n3 / name
			:op1 "维基"
			:op2 "新闻"))
	:aspect performance)

# alignment:
s8a: 0-0
s8h: 0-0
s8i3: 0-0
s8n: 0-0
s8n2: 0-0
s8n3: 0-0
s8p: 0-0
s8s: 0-0
s8x: 5-5
s8x10: 26-26
s8x11: 31-31
s8x12: 34-34
s8x13: 9-9
s8x14: 8-8
s8x15: 14-14
s8x16: 13-13
s8x17: 13-13
s8x18: 9-9
s8x2: 21-21
s8x3: 9-9
s8x4: 23-23
s8x5: 13-13
s8x6: 22-22
s8x7: 25-25
s8x8: 29-29
s8x9: 27-27

# document level annotation:
(s8s0 / sentence
    :temporal ((s2x :depends-on s8x))
    :modal ((root :modal author)
            (author :full-affirmative s8p)
            (author :full-affirmative s8x)
            (s8p :full-negative s8i3)
            (s8p :full-affirmative s8x2))
    :coref ()
)

## chinese_umr-0012, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61
Words: 提到 坚持 的 原因 ， 阿耀 表示 许多 人 ， 无论 是 在 城大 时 的 同学 还是 在 中大 的 朋友 ， 都 给 了 他 莫大 的 鼓励 和 支持 ， 但 一些 中学 时代 的 老师 听闻 此事 时 感到 错愕 和 不解 ， 对此 阿耀 表示 ： “ 人生 这场 游戏 要 有 大起大落 才 好玩 。”

# sentence level graph:
(s4b / contrast-91
	:ARG1 (s4x / 表示-01
		:ARG0 (s4p / person
			:name (s4n3 / name
				:op1 "阿耀"))
		:ARG1 (s4x22 / 给-01
			:ARG0 (s4a3 / and
				:op1 (s4x28 / 同学
					:place (s4u2 / organization
						:name (s4n2 / name
							:op1 "城大")))
				:op2 (s4x27 / 朋友
					:place (s4u / organization
						:name (s4n / name
							:op1 "中大"))))
			:ARG1 (s4a2 / and
				:op1 (s4x25 / 鼓励
					:mod (s4x26 / 莫大))
				:op2 (s4x24 / 支持))
			:ARG2 s4p
			:aspect performance)
		:topic (s4x2 / 原因
			:reason-of (s4x3 / 坚持-01
				:ARG0 s4p
				:aspect activity)
			:ARG1-of (s4x4 / 提到-01
				:aspect performance))
		:aspect performance)
	:ARG2 (s4x5 / 感到-01
		:ARG0 (s4x6 / 老师
			:quant "一些"
			:temporal (s4x29 / 时代
				:mod (s4x30 / 中学)))
		:ARG1 (s4a / and
			:op1 (s4x7 / 错愕)
			:op2 (s4x8 / 不解))
		:temporal (s4x9 / 听闻-01
			:ARG0 s4x6
			:ARG1 (s4x10 / 事
				:quant (s4x11 / 此
					:refer-number singular))
			:aspect performance)
		:aspect performance
		:topic-of (s4x12 / 表示-01
			:ARG0 s4p
			:ARG1 (s4h / have-condition-91
				:ARG1 (s4x14 / 好玩-01
					:ARG0 (s4x15 / 人生
						:ARG1-of (s4i2 / identity-91
							:ARG2 (s4x16 / 游戏
								:quant (s4x17 / 这)
								:unit (s4x18 / 场))
							:aspect state))
					:aspect state)
				:ARG2 (s4x20 / 有-01
					:ARG0 s4x15
					:ARG1 (s4x19 / 大起大落)
					:aspect state)
				:quote s4x12)
			:aspect performance)))

# alignment:
s4a: 0-0
s4a2: 0-0
s4a3: 0-0
s4b: 0-0
s4i2: 0-0
s4n: 0-0
s4n2: 0-0
s4n3: 0-0
s4p: 0-0
s4q: 0-0
s4u: 0-0
s4u2: 0-0
s4x: 7-7
s4x10: 41-41
s4x11: 41-41
s4x12: 7-7
s4x13: 6-6
s4x14: 60-60
s4x15: 53-53
s4x16: 55-55
s4x17: 54-54
s4x18: 54-54
s4x19: 58-58
s4x2: 4-4
s4x22: 25-25
s4x23: 27-27
s4x24: 32-32
s4x25: 30-30
s4x26: 28-28
s4x27: 22-22
s4x28: 17-17
s4x3: 2-2
s4x4: 1-1
s4x5: 43-43
s4x6: 36-36
s4x7: 44-44
s4x8: 46-46
s4x9: 40-40

# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :depends-on s4x14)
            (s3x16 :depends-on s4x4)
            (s4x4 :depends-on s4x)
            (s4x :before s4x22)
            (s4x22 :overlap s4x5)
            (s4x5 :after s4x12))
    :modal ((root :modal author)
            (author :full-affirmative s4x)
            (author :full-affirmative s4x5)
            (author :full-affirmative s4x4)
            (author :full-affirmative s4x9)
            (author :full-affirmative s4x12)
            (s4p :unspecified s4h)
            (author :full-affirmative s4p)
            (s4p :full-affirmative s4x22)
            (s4h :full-affirmative s4x20)
            (s4h :full-affirmative s4x14)
            (s4p :neutral-affirmative s4h))
    :coref ((s3p :same-entity s4p))
)

## chinese_umr-0009, sentence 7

# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57
Words: 目前 虚拟 现实 VR 和 增强 现实 AR 头盔 市场 由 2014 年 收购 Oculus 的 Meta 主导 ， Meta 的 高端 级 头盔 Quest Pro 在 美国 刚 推出 时 售卖 1,500 美元 ， 其后 降价 至 999 美元 ， 而 针对 普及 市场 的 最新 款 产品 Quest 3 则 定价 为 500 美元 。

# sentence level graph:
(s7a / and
    :op1 (s7d / 主导-01
        :ARG0 (s7c / company
            :name (s7n / name
                :op1 "Meta")
            :ARG0-of (s7x / 收购-01
                :ARG1 (s7c3 / company
                    :name (s7n6 / name
                        :op1 "Oculus"))
                :temporal (s7d2 / date-entity
                    :year 2014)
                :aspect performance
                :modal-strength full-affirmative))
        :ARG1 (s7m / 市场
            :mod (s7h / 头盔
                :mod (s7a4 / and
                    :op1 (s7x8 / 虚拟现实
                        :name (s7n7 / name
                            :op1 "VR"))
                    :op2 (s7x10 / 增强现实
                        :name (s7n8 / name
                            :op1 "AR")))))
        :temporal (s7x12 / 目前)
        :aspect state
        :modal-strength full-affirmative)
    :op2 (s7s / 售卖-01
        :ARG1 (s7h2 / 头盔
            :name (s7n2 / name
                :op1 "Quest"
                :op2 "Pro")
            :mod s7c
            :mod (s7l / 级
                :mod (s7g / 高端)))
        :value (s7m2 / monetary-quantity
            :quant 1500
            :unit (s7x14 / 美元))
        :temporal (s7x13 / 时
            :op1 (s7x2 / 推出-01
                :ARG1 s7h2
                :place (s7c2 / country
                    :name (s7n3 / name
                        :op1 "美国"))
                :mod (s7x3 / 刚)
                :aspect performance
                :modal-strength full-affirmative))
        :aspect activity
        :modal-strength full-affirmative)
    :op3 (s7r / 降价-01
        :ARG1 s7h2
        :result (s7hv / have-value-91
            :ARG1 s7h2
            :ARG2 (s7m3 / monetary-quantity
                :quant 999
                :unit (s7x15 / 美元))
            :aspect state
            :modal-strength full-affirmative)
        :temporal (s7x4 / 其后)
        :aspect performance
        :modal-strength full-affirmative)
    :op4 (s7p3 / 定价-01
        :ARG0 (s7p4 / product
            :name (s7n4 / name
                :op1 "Quest"
                :op2 3)
            :mod (s7n5 / 最新款)
            :ARG0-of (s7x5 / 针对-01
                :ARG1 (s7x7 / 市场
                    :mod (s7x6 / 普及))
                :aspect state
                :modal-strength full-affirmative))
        :ARG1 (s7m4 / monetary-quantity
            :quant 500
            :unit (s7x16 / 美元))
        :aspect state
        :modal-strength full-affirmative))

# alignment:
s7a: 0-0
s7a4: 0-0
s7c: 0-0
s7c2: 0-0
s7c3: 0-0
s7d: 18-18
s7g: 22-22
s7h: 9-9
s7h2: 9-9
s7h3: 9-9
s7i2: 0-0
s7i3: 0-0
s7l: 23-23
s7m: 10-10
s7m2: 0-0
s7m3: 0-0
s7m4: 0-0
s7n: 0-0
s7n2: 0-0
s7n3: 0-0
s7n4: 0-0
s7n5: 47-47
s7n6: 0-0
s7n7: 0-0
s7n8: 0-0
s7p: 26-26
s7p2: 26-26
s7p3: 53-53
s7p4: 49-49
s7r: 37-37
s7s: 32-32
s7t: 0-0
s7x: 14-14
s7x10: 3-3
s7x11: 6-6
s7x12: 1-1
s7x13: 31-31
s7x14: 34-34
s7x15: 40-40
s7x16: 56-56
s7x2: 30-30
s7x3: 29-29
s7x4: 36-36
s7x5: 43-43
s7x6: 44-44
s7x7: 10-10
s7x8: 3-3
s7x9: 2-2

# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :depends-on s7x12)
            (s7x12 :overlap s7d)
            (root :depends-on s7d2)
            (s7d2 :contained s7x)
            (document-creation-time :before s7x2)
            (s7x2 :overlap s7x13)
            (s7x13 :overlap s7s)
            (s7s :after s7x4)
            (s7x4 :overlap s7r)
            (s7r :after s7hv)
            (document-creation-time :overlap s7p3)
            (document-creation-time :overlap s7x5))
    :modal ((author :full-affirmative s7x)
            (root :modal author)
            (author :full-affirmative s7d)
            (author :full-affirmative s7x2)
            (author :full-affirmative s7s)
            (author :full-affirmative s7hv)
            (author :full-affirmative s7r)
            (author :full-affirmative s7x5)
            (author :full-affirmative s7p3))
    :coref ((s6c :same-entity s7c2))
)

## chinese_umr-0001, sentence 23

# :: snt23
Index: 1 2  3   4  5  6 7  8  9 10 11 12 13 14 15   16 17 18 19
Words: 据 其中 数百篇 该刊 新闻 的 作者 马克 · 米勒 所言 ，  这些 新闻 100% 是  虚构 的  。 

# sentence level graph:
(s23x / 言-02
    :ARG0 (s23i2 / individual-person
        :name (s23n / name
            :op1 "马克"
            :op2 "·"
            :op3 "米勒")
        :ARG0-of (s23i3 / implicit-predicate
            :ARG1 (s23x5 / 新闻
                :part-of (s23x6 / 刊
                    :mod (s23x7 / 该))
                :quant (s23x8 / 数
                    :op1 100)
                :unit (s23x9 / 篇)
                :mod (s23x10 / 其中))))
    :ARG1 (s23x2 / 虚构-01
        :ARG1 (s23x3 / 新闻
            :mod (s23x4 / 这些)
            :refer-number plural)
        :aspect state
        :mod (s23p / percentage-entity
            :value 100))
    :aspect state)


# alignment:
s23i2: 0-0
s23i3: 0-0
s23n: 0-0
s23p: 0-0
s23x: 11-11
s23x10: 2-2
s23x2: 17-17
s23x3: 5-5
s23x4: 13-13
s23x5: 5-5
s23x6: 4-4
s23x7: 4-4
s23x8: 3-3
s23x9: 3-3

# document level annotation:
(s23s0 / sentence
    :temporal ((document-creation-time :before s23x)
        (s23x :overlap s23x2))
    :modal ((root :modal author)
        (author :full-affirmative s23x2)
        (author :full-affirmative s23x))
    :coref ((s22n2 :same-entity s23x6)))

## chinese_umr-0002, sentence 57

# :: snt57
Index: 1  2  3 4  5  6  7  8 9   10 11 12 13 14 15 16
Words: 唱片 公司 也 宣布 部分 欧洲 国家 的 演唱会 及  亚洲 的  巡回 照常 举行 。 

# sentence level graph:
(s57a / and
    :op2 (s57x / 宣布-01
        :ARG0 (s57x2 / 公司
            :mod (s57x3 / 唱片))
        :ARG1 (s57x4 / 照常-01
            :ARG0 (s57x5 / 举行-01
                :ARG1 (s57a2 / and
                    :op1 (s57x6 / 演唱会
                        :place (s57x7 / 国家
                            :mod (s57c / continent
                                :name (s57n / name
                                    :op1 "欧洲")))
                        :mod (s57x8 / 部分))
                    :op2 (s57x9 / 巡回-01
                        :ARG1 (s57c2 / continent
                            :name (s57n2 / name
                                :op1 "亚洲"))
                        :aspect process
                        :quote s57x))
                :aspect process
                :quote s57x)
            :aspect state
            :quote s57x)
        :aspect performance))


# alignment:
s57a: 0-0
s57a2: 0-0
s57c: 0-0
s57c2: 0-0
s57n: 0-0
s57n2: 0-0
s57x: 4-4
s57x2: 2-2
s57x3: 1-1
s57x4: 14-14
s57x5: 15-15
s57x6: 9-9
s57x7: 7-7
s57x8: 5-5
s57x9: 13-13

# document level annotation:
(s57s0 / sentence
    :temporal ((document-creation-time :before s57x)
        (s57x :after s57x4)
        (s57x4 :overlap s57x5)
        (s57x5 :overlap s57x9))
    :modal ((root :modal author)
        (s57x2 :full-affirmative s57x9)
        (author :full-affirmative s57x5)
        (author :full-affirmative s57x2)
        (author :full-affirmative s57x4)
        (author :full-affirmative s57x2)
        (author :full-affirmative s57x)
        (author :full-affirmative s57x2))
    :coref ((s54x2 :same-entity s57x2)))

## chinese_umr-0003, sentence 11

# :: snt11
Index: 1   2  3  4   5  6 7 8  9  10 11 12 13 14 15 16 17   18 19 20 21  22 23 24 25 26 27 28 29 30 31 32 33  34 35 36 37 38
Words: 温哥华 华裔 商人 冯永发 旗下 的 新 时代 集团 联同 电视 广播 国际 有限 公司 于  1992 年  宣布 斥资 925 万  加元 收购 中文 电视 的  资产 ，  并  同时 以  380 万元 收购 国泰 电视 。 

# sentence level graph:
(s11x / 宣布-01
    :ARG0 (s11a2 / and
        :op1 (s11c / company
            :name (s11n3 / name
                :op1 "新"
                :op2 "时代"
                :op3 "集团")
            :mod (s11x2 / 旗下)
            :possessor (s11i2 / individual-person
                :name (s11n2 / name
                    :op1 "冯永发")
                :ARG1-of (s11i3 / identity-91
                    :ARG2 (s11x3 / 商人
                        :mod (s11x4 / 华裔)
                        :place (s11c2 / city
                            :name (s11n / name
                                :op1 "温哥华"))))))
        :op2 (s11c5 / company
            :name (s11n6 / name
                :op1 "电视"
                :op2 "广播"
                :op3 "国际"
                :op4 "有限"
                :op5 "公司")))
    :ARG1 (s11a / and
        :op1 (s11x5 / 斥资-01
            :ARG1 (s11x7 / 收购-01
                :ARG1 (s11x8 / 资产
                    :possessor (s11c3 / company
                        :name (s11n4 / name
                            :op1 "中文"
                            :op2 "电视")))
                :aspect process)
            :ARG2 (s11m / monetary-quantity
                :unit (s11x6 / 加元)
                :quant 9250000)
            :aspect performance)
        :op2 (s11x9 / 收购-01
            :ARG1 (s11c4 / company
                :name (s11n5 / name
                    :op1 "国泰"
                    :op2 "电视"))
            :aspect performance
            :temporal (s11x10 / 同时)
            :instrument (s11m2 / monetary-quantity
                :quant 3800000)))
    :aspect performance)


# alignment:
s11a: 0-0
s11a2: 0-0
s11c: 0-0
s11c2: 0-0
s11c3: 0-0
s11c4: 0-0
s11c5: 0-0
s11i2: 0-0
s11i3: 0-0
s11m: 0-0
s11m2: 0-0
s11n: 0-0
s11n2: 0-0
s11n3: 0-0
s11n4: 0-0
s11n5: 0-0
s11n6: 0-0
s11x: 19-19
s11x10: 31-31
s11x2: 5-5
s11x3: 3-3
s11x4: 2-2
s11x5: 20-20
s11x6: 23-23
s11x7: 24-24
s11x8: 28-28
s11x9: 24-24

# document level annotation:
(s11s0 / sentence
    :temporal ((s11x :overlap s11x5)
        (s11x5 :overlap s11x7)
        (s11x :overlap s11x9))
    :modal ((root :modal author)
        (author :full-affirmative s11x4)
        (author :full-affirmative s11x2)
        (author :full-affirmative s11x)
        (author :full-affirmative s11x9)
        (author :full-affirmative s11x7)
        (author :full-affirmative s11x5))
    :coref ((s5c3 :same-entity s11c2)
        (s10c :same-entity s11c3)))
