# Gold UMR annotations of sentences like those of chinese_umr-0028

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0020, sentence 7

# :: snt7
Index:  1    2  3  4    5    6    7    8    9   10 11 12   13   14 15   16 17   18 19   20   21   22   23 24
Words: 但  近年   来  ，  中国   由于   出现   人口   萎缩   现象   ，  且  男女   比例   不  均匀   ，  导致   在  中国   结婚   极为   困难   。 

# sentence level graph:
(s7b / but
	:op1 (s7i2 / implicit-argument)
	:op2 (s7x / 导致-01
		:effect (s7x2 / 困难-01
			:ARG1 (s7x4 / 结婚
				:place (s7x5 / 国家
					:name (s7n / name
						:op1 "中国")))
			:degree (s7x3 / 极为))
		:cause (s7a / and
			:op1 (s7x9 / 出现-01
				:ARG1 (s7x13 / 现象
					:mod (s7x14 / 萎缩-01
						:ARG1 (s7x15 / 人口)
						:aspect habitual))
				:place (s7x12 / 国家
					:name (s7n2 / name
						:op1 "中国"))
				:aspect habitual)
			:op2 (s7x6 / 均匀-01
				:ARG1 (s7x7 / 比例
					:mod (s7x8 / 男女))
				:polarity -
				:aspect habitual))
		:temporal (s7x10 / 近年
			:mod (s7x11 / 来))
		:aspect performance))

# alignment:
s7a: 0-0
s7b: 0-0
s7i2: 0-0
s7n: 0-0
s7n2: 0-0
s7x: 18-18
s7x10: 2-2
s7x11: 3-3
s7x12: 0-0
s7x13: 10-10
s7x14: 9-9
s7x15: 8-8
s7x2: 23-23
s7x3: 22-22
s7x4: 21-21
s7x5: 0-0
s7x6: 16-16
s7x7: 14-14
s7x8: 13-13
s7x9: 7-7

# document level annotation:
(s7s0 / sentence
	:temporal ((document-creation-time :overlap s7b)
		(s7b :depends-on s7x9)
		(s7b :depends-on s7x14)
		(s7b :depends-on s7x6)
		(s7b :depends-on s7x))
	:modal ((root :modal author)
		(author :full-affirmative s7x14)
		(author :full-affirmative s7x9)
		(author :full-negative s7x6)
		(author :full-affirmative s7x))
	:coref ((s6a :same-event s7i2)))

## chinese_umr-0010, sentence 7

# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 但 近年 来 ， 中国 由于 出现 人口 萎缩 现象 ， 且 男女 比例 不 均匀 ， 导致 在 中国 结婚 极为 困难 。

# sentence level graph:
(s7c / 导致-01
    :ARG0 (s7a / and
        :op1 (s7x / 出现-01
            :ARG1 (s7x2 / 现象
                :mod (s7x5 / 萎缩-01
                    :ARG1 (s7x16 / 人口)
                    :aspect process
                    :modal-strength full-affirmative))
            :place (s7c2 / country
                :name (s7n3 / name
                    :op1 "中国"))
            :aspect performance
            :modal-strength full-affirmative)
        :op2 (s7x6 / 均匀-01
            :ARG1 (s7x10 / 比例
                :mod (s7x11 / 男女))
            :polarity -
            :aspect state
            :modal-strength full-negative))
    :ARG1 (s7x12 / 困难-01
        :ARG1 (s7x14 / 结婚-01
            :place s7c2
            :aspect performance
            :modal-strength unspecified)
        :degree (s7x13 / 极为)
        :aspect state
        :modal-strength full-affirmative)
    :temporal (s7x3 / 来
        :op1 (s7x4 / 近年))
    :mod (s7b / 但)
    :aspect performance
    :modal-strength full-affirmative)

# alignment:
s7a: 0-0
s7b: 1-1
s7c: 18-18
s7c2: 0-0
s7c3: 0-0
s7h: 0-0
s7n: 0-0
s7n3: 0-0
s7x: 7-7
s7x10: 14-14
s7x11: 13-13
s7x12: 23-23
s7x13: 22-22
s7x14: 21-21
s7x16: 8-8
s7x2: 10-10
s7x3: 3-3
s7x4: 2-2
s7x5: 9-9
s7x6: 16-16

# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :overlap s7x3)
            (s7x3 :contained s7c)
            (s7c :overlap s7x)
            (s7x :overlap s7x5)
            (s7c :overlap s7x6)
            (s7c :overlap s7x12)
            (s7x12 :overlap s7x14))
    :modal ((author :full-affirmative s7x)
            (root :modal author)
            (author :full-affirmative s7x5)
            (author :full-negative s7x6)
            (author :full-affirmative s7x12)
            (author :full-affirmative s7c)
            (author :unspecified s7x14))
    :coref ((s6c :same-entity s7c2))
)

## chinese_umr-0025, sentence 383

# :: snt383
Index:    1  2    3  4  5  6  7  8  9 10 11
Words: 而且   ，  老虎   是  不  会  吃  草  的  ”  。 

# sentence level graph:
(s383x12 / say
	:ARG1 (s383x14 / progression
		:ARG2 (s383x6 / 会-02
			:ARG0 (s383x3 / 老虎)
			:ARG1 (s383x7 / 吃-01
				:ARG1 (s383x8 / 草))
			:mode judgement
			:polarity -)))

# alignment:
s383x12: 0-0
s383x14: 0-0
s383x3: 3-3
s383x6: 6-6
s383x7: 7-7
s383x8: 8-8

# document level annotation:
(s383s0 / sentence)

## chinese_umr-0025, sentence 974

# :: snt974
Index:  1    2  3  4      5  6  7    8  9   10 11   12 13
Words: 它  上面   全  是  干巴巴    的  ，  而且   又  尖利   又  咸涩   ， 

# sentence level graph:
(s974x14 / progression
	:ARG1 (s974x5 / 干巴巴
		:mod (s974x3 / 全-01))
	:ARG1 (s974y1 / identity-91
		:ARG0 (s974x2 / 上面
			:possessor-of (s974x1 / individual-person
				:refer-person 3
				:refer-number singular))
		:ARG1 s974x5)
	:ARG2 (s974x20 / and
		:op1 (s974x10 / 尖利-01)
		:op2 (s974x12 / 咸涩)
		:ARG0 s974x2))

# alignment:
s974x1: 0-0
s974x10: 10-10
s974x12: 12-12
s974x14: 0-0
s974x2: 2-2
s974x20: 0-0
s974x3: 3-3
s974x5: 5-5
s974y1: 0-0

# document level annotation:
(s974s0 / sentence)

## chinese_umr-0025, sentence 1062

# :: snt1062
Index:    1  2  3    4  5    6  7  8  9   10 11   12 13 14
Words: 而且   ，  我  甚至   会  喜欢   那  风  吹  麦浪   的  声音   …  ” 

# sentence level graph:
(s1062x15 / say
	:ARG1 (s1062x17 / progression
		:ARG2 (s1062x5 / 会-02
			:ARG0 (s1062x6 / 喜欢-01
				:ARG0 (s1062x3 / individual-person
					:refer-person 1
					:refer-number singular)
				:ARG1 (s1062x12 / 声音
					:mod (s1062x9 / 吹-02
						:ARG0 (s1062x8 / 风)
						:ARG1 (s1062x10 / 麦浪))
					:mod (s1062x7 / 那)))
			:mod (s1062x4 / 甚至))))

# alignment:
s1062x10: 10-10
s1062x12: 12-12
s1062x15: 0-0
s1062x17: 0-0
s1062x3: 0-0
s1062x4: 4-4
s1062x5: 5-5
s1062x6: 6-6
s1062x7: 7-7
s1062x8: 8-8
s1062x9: 9-9

# document level annotation:
(s1062s0 / sentence)

## chinese_umr-0009, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 和 早前 的 传闻 相同 ， 头盔 可 透过 眼球 、 手部 和 语音 控制 ， 并且 能够 连线 并 操作 苹果 的 Mac 电脑 。

# sentence level graph:
(s4x3 / 相同-01
    :ARG0 (s4a2 / and
        :op1 (s4x / 传闻
            :mod (s4x14 / 早前))
        :op2 (s4a3 / and
            :op1 (s4x15 / 控制-01
                :ARG1 (s4x17 / 头盔)
                :medium (s4a / and
                    :op1 (s4x9 / 眼球)
                    :op2 (s4x8 / 手部)
                    :op3 (s4x5 / 语音))
                :aspect activity
                :modal-strength neutral-affirmative)
            :op2 (s4a4 / and
                :op1 (s4x16 / 连线-01
                    :ARG0 (s4a5 / and
                        :op1 s4x17
                        :op2 (s4p / product
                            :name (s4n3 / name
                                :op1 "Mac"
                                :op2 "电脑")
                            :mod (s4c / company
                                :name (s4n / name
                                    :op1 "苹果"))))
                    :aspect performance
                    :modal-strength neutral-affirmative)
                :op2 (s4x18 / 操作-01
                    :ARG0 s4x17
                    :ARG1 s4p
                    :aspect activity
                    :modal-strength neutral-affirmative))))
    :aspect state
    :modal-strength full-affirmative)

# alignment:
s4a: 0-0
s4a3: 0-0
s4a4: 0-0
s4c: 0-0
s4n: 0-0
s4n3: 0-0
s4p: 0-0
s4s: 0-0
s4x: 4-4
s4x14: 2-2
s4x15: 15-15
s4x16: 19-19
s4x17: 7-7
s4x18: 21-21
s4x3: 5-5
s4x5: 14-14
s4x6: 9-9
s4x8: 12-12
s4x9: 10-10

# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :overlap s4x3)
            (document-creation-time :overlap s4x15)
            (document-creation-time :overlap s4x16)
            (document-creation-time :overlap s4x18))
    :modal ((author :full-affirmative s4x3)
            (root :modal author)
            (author :neutral-affirmative s4x15)
            (author :neutral-affirmative s4x16)
            (author :neutral-affirmative s4x18))
    :coref ((s3x23 :same-entity s4x17)
            (s2c :same-entity s4c))
)

## chinese_umr-0025, sentence 14

# :: snt14
Index:    1      2  3    4    5  6    7  8  9 10   11   12 13 14   15 16 17   18 19   20 21     22   23   24 25
Words: 既然   大人们    不  能够   理解   。  于是   我  又  把  巨蟒   肚子   里  的  情况   画  了  出来   ，  以便   让  大人们    能够   看懂   。 

# sentence level graph:
(s14x26 / causation
	:ARG1 (s14x4 / 能够-01
		:ARG0 (s14x5 / 理解-01
			:ARG0 (s14x2 / 大人们))
		:modal-strength neutral-negative
		:polarity -)
	:ARG2 (s14x16 / 画-01
		:ARG0 (s14x8 / individual-person
			:refer-person 1
			:refer-number singular
			:modal-strength (s14x55 / full-affirmative))
		:aspect performance
		:mod (s14x9 / 又)
		:ARG1 (s14x15 / 情况
			:place (s14x12 / 肚子
				:part-of (s14x11 / 巨蟒)))
		:purpose (s14x21 / 让-02
			:ARG1 (s14x22 / 大人们)
			:ARG2 (s14x23 / 能够-01
				:ARG0 (s14x24 / 看懂
					:ARG0 s14x22
					:modal-strength (s14x53 / full-affirmative))
				:modal-strength neutral-affirmative)
			:modal-strength (s14x54 / partial-affirmative
				:conceiver s14x8))
		:modal-strength (s14x52 / full-affirmative)))

# alignment:
s14x11: 11-11
s14x12: 12-12
s14x15: 15-15
s14x16: 16-16
s14x2: 2-2
s14x21: 21-21
s14x22: 2-2
s14x23: 4-4
s14x24: 24-24
s14x26: 0-0
s14x4: 4-4
s14x5: 5-5
s14x52: 0-0
s14x53: 0-0
s14x54: 0-0
s14x55: 0-0
s14x8: 0-0
s14x9: 9-9

# document level annotation:
(s14s0 / sentence)

## chinese_umr-0025, sentence 1157

# :: snt1157
Index:  1  2  3  4    5    6    7  8    9   10 11   12 13
Words: 这  是  一  位  贩卖   能够   止渴   的  精制   药丸   的  商人   。 

# sentence level graph:
(s1157y1 / identity-91
	:ARG0 (s1157x1 / 这)
	:ARG1 (s1157x12 / 商人
		:ARG0-of (s1157x5 / 贩卖-01
			:ARG1 (s1157x10 / 药丸
				:mod (s1157x9 / 精制)
				:ARG0-of (s1157x7 / 止渴-01
					:ARG0-of (s1157x6 / 能够-01
						:modal-strength neutral-affirmative))))
		:quant 1
		:unit (s1157x4 / 位)))

# alignment:
s1157x1: 1-1
s1157x10: 10-10
s1157x12: 12-12
s1157x4: 4-4
s1157x5: 5-5
s1157x6: 6-6
s1157x7: 7-7
s1157x9: 9-9
s1157y1: 0-0

# document level annotation:
(s1157s0 / sentence)

## chinese_umr-0025, sentence 675

# :: snt675
Index: 1  2    3  4    5    6  7    8  9 10 11
Words: “ 你  拥有   这  许多   星星   有  什么   用  ？  ” 

# sentence level graph:
(s675x12 / say
	:ARG1 (s675x3 / 拥有-01
		:ARG0 (s675x2 / individual-person
			:refer-person 2
			:refer-number singular)
		:ARG1 (s675x6 / 星星
			:quant (s675x5 / 许多)
			:mod (s675x4 / 这))
		:purpose (s675x7 / amr-unknown)
		:mode interrogative))

# alignment:
s675x12: 0-0
s675x2: 0-0
s675x3: 3-3
s675x4: 4-4
s675x5: 5-5
s675x6: 6-6
s675x7: 0-0

# document level annotation:
(s675s0 / sentence)

## chinese_umr-0001, sentence 3

# :: snt3
Index: 1 2  3 4  5  6 7  8 9  10 11 12 13 14 15
Words: 该 周报 也 曾经 短暂 的 拥有 过 一个 属  自己 的  电视 节目 。 

# sentence level graph:
(s3x / 拥有-01
    :ARG0 (s3x2 / 周报
        :mod (s3x3 / 该))
    :ARG1 (s3x4 / 节目
        :medium (s3x5 / 电视)
        :ARG0-of (s3x6 / 属-02
            :ARG1 s3x2
            :aspect state)
        :quant 1
        :unit (s3x7 / 个))
    :mod (s3x8 / 也)
    :temporal (s3x9 / 曾经)
    :duration (s3x10 / 短暂)
    :aspect state)


# alignment:
s3x: 7-7
s3x10: 5-5
s3x2: 2-2
s3x3: 1-1
s3x4: 14-14
s3x5: 13-13
s3x6: 10-10
s3x7: 9-9
s3x8: 3-3
s3x9: 4-4

# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :before s3x)
        (s3x :overlap s3x6))
    :modal ((root :modal author)
        (author :full-affirmative s3x6)
        (author :full-affirmative s3x))
    :coref ((s2x2 :same-entity s3x2)))

## chinese_umr-0025, sentence 245

# :: snt245
Index:  1    2  3    4    5    6  7  8    9 10 11 12 13   14 15 16   17 18 19
Words: 我  提出   的  这个   教训   意义   是  很  重大   的  ，  花  点  功夫   是  很  值得   的  。 

# sentence level graph:
(s245x20 / and
				:op1 (s245x9 / 重大-01
											:ARG0 (s245x6 / 意义
																		:mod (s245x5 / 教训
																								:ARG1-of (s245x2 / 提出-01
																																	:ARG0 (s245x1 / individual-person
																																								:refer-person 1
																																								:refer-number singular))
																								:mod (s245x4 / 个
																															/ 这)
																								:unit s245x4))
											:degree (s245x8 / 很)
											:mode judgement)
				:op2 (s245x17 / 值得
											:degree (s245x16 / 很)
											:ARG0 (s245x12 / 花-01
																			:ARG1 (s245x14 / 功夫
																										:quant (s245x13 / 点)))
											:mode judgement))

# alignment:
s245x1: 0-0
s245x12: 12-12
s245x13: 13-13
s245x14: 14-14
s245x16: 8-8
s245x17: 17-17
s245x2: 2-2
s245x20: 0-0
s245x4: 4-4
s245x5: 5-5
s245x6: 6-6
s245x8: 8-8
s245x9: 9-9

# document level annotation:
(s245s0 / sentence)

## chinese_umr-0006, sentence 31

# :: snt31
Index: 1  2 3  4   5 6 7    8  9    10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25    26 27 28 29 30 31 32 33  34 35 36  37 38 39 40 41 42 43 44 45 46  47 48
Words: 剩下 的 四强 设计师 须 在 四个月内 运用 一万美元 的  预算 设计 一个 包含 12 款  设计 的  秋装 系列 ，  而  工作 期间 提姆·冈恩 并  会  亲自 拜访 和  指导 四强 设计师 ，  而  设计师 回到 纽约 后  并  会  有  缝纫 助手 协助 设计师 完成 设计

# sentence level graph:
(s31a / and
    :op1 (s31x30 / 须-01
        :ARG0 (s31x2 / 设计师
            :mod (s31x3 / 四强)
            :ARG0-of (s31x4 / 剩下-01
                :aspect state))
        :ARG1 (s31x5 / 运用-01
            :ARG0 s31x2
            :ARG1 (s31x6 / 预算
                :ARG1-of (s31i2 / identity-91
                    :ARG2 (s31m / monetary-quantity
                        :unit (s31x8 / 美元)
                        :quant 10000)
                    :aspect state))
            :purpose (s31x / 设计-01
                :ARG0 s31x2
                :ARG1 (s31x13 / 系列
                    :ARG0-of (s31x14 / 包含-01
                        :ARG1 (s31x31 / 设计
                            :unit (s31x32 / 款)
                            :quant 12)
                        :aspect state)
                    :unit (s31x33 / 个)
                    :quant 1
                    :topic (s31x34 / 秋装))
                :aspect performance
                :range (s31x7 / 内
                    :op1 (s31t2 / temporal-quantity
                        :quant 4
                        :unit (s31x9 / 月))))
            :aspect performance))
    :op2 (s31x10 / 拜访-01
        :ARG0 (s31i3 / individual-person
            :name (s31n / name
                :op1 "提姆·冈恩"))
        :ARG1 s31x2
        :aspect performance
        :manner (s31x12 / 亲自)
        :temporal (s31x11 / 期间
            :op1 (s31x15 / 工作-01
                :ARG0 s31x2)))
    :op3 (s31x16 / 指导-01
        :ARG0 s31i3
        :ARG1 s31x2
        :temporal s31x11
        :manner s31x12
        :aspect performance)
    :op4 (s31x19 / 协助-02
        :ARG0 (s31x26 / 助手
            :topic (s31x27 / 缝纫))
        :ARG1 s31x2
        :ARG2 (s31x20 / 完成-01
            :ARG1 (s31x22 / 设计)
            :aspect performance)
        :temporal (s31x17 / 后
            :op1 (s31x18 / 回到-01
                :ARG0 s31x2
                :ARG1 (s31c / city
                    :name (s31n2 / name
                        :op1 "纽约"))
                :aspect performance))
        :aspect performance))


# alignment:
s31a: 0-0
s31c: 0-0
s31i2: 0-0
s31i3: 0-0
s31m: 0-0
s31n: 0-0
s31n2: 0-0
s31t2: 0-0
s31x: 12-12
s31x10: 29-29
s31x11: 24-24
s31x12: 28-28
s31x13: 20-20
s31x14: 14-14
s31x15: 23-23
s31x16: 31-31
s31x17: 39-39
s31x18: 37-37
s31x19: 45-45
s31x2: 4-4
s31x20: 47-47
s31x22: 12-12
s31x26: 44-44
s31x27: 43-43
s31x3: 3-3
s31x30: 5-5
s31x31: 12-12
s31x32: 16-16
s31x33: 7-7
s31x34: 19-19
s31x4: 1-1
s31x5: 8-8
s31x6: 11-11
s31x7: 7-7
s31x8: 9-9
s31x9: 7-7

# document level annotation:
(s31s0 / sentence
    :temporal ((document-creation-time :before s31x30)
        (s31x30 :overlap s31x4)
        (s31x30 :overlap s31x5)
        (s31x5 :overlap s31x)
        (s31x :overlap s31x14)
        (s31x30 :overlap s31x10)
        (s31x10 :overlap s31x15)
        (s31x10 :overlap s31x16)
        (s31x16 :overlap s31x19)
        (s31x19 :overlap s31x20)
        (s31x19 :before s31x18))
    :modal ((root :modal author)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2)
        (s31x2 :full-affirmative s31x30)
        (s31x30 :unspecified s31x)
        (s31x2 :full-affirmative s31x30)
        (s31x30 :unspecified s31x5)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2)
        (author :full-affirmative s31x2))
    :coref ((s3i8 :same-entity s31i3)
        (s28c :same-entity s31c)))

## chinese_umr-0006, sentence 21

# :: snt21
Index: 1   2 3 4  5  6 7  8   9 10 11           12 13 14 15 16   17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32  33 34 35 36
Words: 设计师 须 以 两人 一队 ， 每队 设计师 须 以  所罗门·R·古根汉美术馆 为  灵感 ，  运用 惠普公司 提供 的  布料 设计 软件 设计 花纹 布料 ，  并  运用 其  布料 设计 一款 前卫派 时装 和  一款 成衣

# sentence level graph:
(s21a / and
    :op1 (s21x / 须-01
        :ARG0 (s21x3 / 设计师)
        :ARG1 (s21i2 / implicit-predicate
            :ARG0 (s21x4 / 人
                :quant 2)
            :ARG2 (s21x5 / 队
                :quant 1)
            :aspect state)
        :aspect state)
    :op2 (s21x2 / 须-01
        :ARG1 (s21a2 / and
            :op1 (s21x23 / 为-01
                :ARG0 (s21m / museum
                    :name (s21n2 / name
                        :op1 "所罗门·R·古根汉美术馆"))
                :ARG1 (s21x24 / 灵感)
                :aspect state)
            :op2 (s21x18 / 运用-01
                :ARG0 s21x3
                :ARG1 (s21x19 / 软件
                    :ARG1-of (s21x20 / 提供-01
                        :ARG0 (s21c / company
                            :name (s21n / name
                                :op1 "惠普公司"))
                        :aspect performance)
                    :topic (s21x21 / 设计-01
                        :ARG1 (s21x22 / 布料)
                        :aspect process))
                :purpose (s21x15 / 设计-01
                    :ARG0 s21x3
                    :ARG1 (s21x28 / 布料
                        :mod (s21x29 / 花纹))
                    :aspect performance)
                :aspect performance)
            :op3 (s21x7 / 运用-01
                :ARG0 s21x3
                :ARG1 (s21x8 / 布料
                    :ARG1-of (s21i3 / implicit-predicate
                        :ARG0 s21x3
                        :aspect performance))
                :purpose (s21x6 / 设计-01
                    :ARG0 s21x3
                    :ARG1 (s21a4 / and
                        :op1 (s21x10 / 时装
                            :mod (s21x11 / 前卫派)
                            :quant 1
                            :unit (s21x12 / 款))
                        :op2 (s21x13 / 成衣
                            :quant 1
                            :unit (s21x14 / 款)))
                    :aspect performance)
                :aspect performance))))


# alignment:
s21a: 0-0
s21a2: 0-0
s21a4: 0-0
s21c: 0-0
s21i2: 0-0
s21i3: 0-0
s21m: 0-0
s21n: 0-0
s21n2: 0-0
s21x: 2-2
s21x10: 33-33
s21x11: 32-32
s21x12: 31-31
s21x13: 36-36
s21x14: 31-31
s21x15: 20-20
s21x18: 15-15
s21x19: 21-21
s21x2: 2-2
s21x20: 17-17
s21x21: 20-20
s21x22: 19-19
s21x23: 12-12
s21x24: 13-13
s21x28: 19-19
s21x29: 23-23
s21x3: 1-1
s21x4: 4-4
s21x5: 5-5
s21x6: 20-20
s21x7: 15-15
s21x8: 19-19

# document level annotation:
(s21s0 / sentence
    :temporal ((document-creation-time :overlap s21x)
        (s21x :overlap s21i2)
        (s21x :overlap s21x2)
        (s21x2 :overlap s21x23)
        (s21x2 :overlap s21x18)
        (s21x18 :overlap s21x20)
        (s21x18 :overlap s21x15)
        (s21x2 :overlap s21x7)
        (s21x7 :overlap s21i3)
        (s21x7 :overlap s21x6))
    :modal ((root :modal author)
        (s21x3 :full-affirmative s21x)
        (s21x :unspecified s21i2)
        (author :full-affirmative s21x3)
        (s21x3 :full-affirmative s21x2)
        (s21x2 :unspecified s21x23)
        (author :full-affirmative s21x3)
        (author :full-affirmative s21x3)
        (s21x3 :full-affirmative s21x2)
        (s21x2 :unspecified s21x15)
        (s21x3 :full-affirmative s21x2)
        (s21x2 :unspecified s21x18)
        (author :full-affirmative s21x3)
        (s21x3 :full-affirmative s21x2)
        (s21x2 :unspecified s21x6)
        (s21x3 :full-affirmative s21x2)
        (s21x2 :unspecified s21x7)))

## chinese_umr-0006, sentence 12

# :: snt12
Index: 1  2   3 4 5  6 7  8  9  10 11 12 13   14 15       16 17 18 19 20 21 22  23 24 25 26 27 28 29   30 31 32 33 34 35 36 37 38  39 40
Words: 两队 设计师 须 为 海蒂 · 克隆 设计 两款 用作 宣传 其  香水品牌 「  Surprise 」  的  礼服 ，  而  每队 设计师 须  设计 4  款  用作 拍摄 电视广告 的  礼服 和  2  款  用作 出席 香水 发布会 的  礼服

# sentence level graph:
(s12a / and
    :op1 (s12x / 须-01
        :ARG0 (s12x18 / 设计师
            :part (s12x19 / 队
                :quant 2))
        :ARG1 (s12x17 / 设计-01
            :ARG0 s12x18
            :ARG1 (s12x20 / 礼服
                :ARG1-of (s12x21 / 用作-01
                    :ARG2 (s12x22 / 宣传-01
                        :ARG1 (s12c2 / company
                            :name (s12n3 / name
                                :op1 "Surprise")
                            :ARG1-of (s12i3 / identity-91
                                :ARG2 (s12x23 / 品牌
                                    :name (s12n / name
                                        :op1 (s12s / surprise))
                                    :topic (s12x24 / 香水)
                                    :possessor s12i2)))
                        :aspect process)
                    :aspect state)
                :unit (s12x26 / 款)
                :quant 2)
            :affectee (s12i2 / individual-person
                :name (s12n2 / name
                    :op1 "海蒂"
                    :op2 "克隆"))
            :aspect performance))
    :op2 (s12x27 / 须-01
        :ARG0 (s12x15 / 设计师
            :mod (s12x16 / 每队))
        :ARG1 (s12x2 / 设计-01
            :ARG0 s12x15
            :ARG1 (s12a3 / and
                :op1 (s12x9 / 礼服
                    :ARG1-of (s12x10 / 用作-01
                        :ARG2 (s12x11 / 拍摄-01
                            :ARG1 (s12x12 / 广告
                                :mod (s12x13 / 电视))
                            :aspect process)
                        :aspect state)
                    :quant 4
                    :unit (s12x14 / 款))
                :op2 (s12x3 / 礼服
                    :unit (s12x4 / 款)
                    :quant 2
                    :ARG1-of (s12x5 / 用作-01
                        :ARG2 (s12x6 / 出席-01
                            :ARG1 (s12x7 / 发布会
                                :topic (s12x8 / 香水))
                            :aspect process)
                        :aspect state)))
            :aspect process)
        :aspect state))


# alignment:
s12a: 0-0
s12a3: 0-0
s12c2: 0-0
s12i2: 0-0
s12i3: 0-0
s12n: 0-0
s12n2: 0-0
s12n3: 0-0
s12s: 15-15
s12x: 3-3
s12x10: 10-10
s12x11: 28-28
s12x12: 29-29
s12x13: 29-29
s12x14: 26-26
s12x15: 2-2
s12x16: 21-21
s12x17: 8-8
s12x18: 2-2
s12x19: 1-1
s12x2: 8-8
s12x20: 18-18
s12x21: 10-10
s12x22: 11-11
s12x23: 13-13
s12x24: 37-37
s12x26: 26-26
s12x27: 3-3
s12x3: 18-18
s12x4: 26-26
s12x5: 10-10
s12x6: 36-36
s12x7: 38-38
s12x8: 37-37
s12x9: 18-18

# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
        (s12x :overlap s12x17)
        (s12x17 :overlap s12x21)
        (s12x21 :overlap s12x22)
        (s12x :overlap s12x27)
        (s12x27 :overlap s12x2)
        (s12x10 :overlap s12x11)
        (s12x2 :overlap s12x6)
        (s12x2 :after s12x5)
        (s12x2 :after s12x5))
    :modal ((root :modal author)
        (author :full-affirmative s12x18)
        (author :full-affirmative s12x18)
        (s12x18 :full-affirmative s12x)
        (s12x :unspecified s12x17)
        (author :full-affirmative s12x18)
        (author :full-affirmative s12x18)
        (author :full-affirmative s12x18)
        (author :full-affirmative s12x18)
        (s12x18 :full-affirmative s12x27)
        (s12x27 :unspecified s12x2)
        (author :full-affirmative s12x18))
    :coref ((s11x31 :same-entity s12x18)
        (s12x18 :same-entity s12x15)
        (s3i4 :same-entity s12i2)))

## chinese_umr-0026, sentence 26

# :: snt26
Index:    1    2  3  4    5    6    7  8  9 10   11   12   13   14 15
Words: 双方   落座   后  ，  主客   分别   致辞   ，  并  请  台湾   学生   代表   发言   。 

# sentence level graph:
(s26c / consecutive
	:op1 (s26x / 落座-01
		:ARG0 (s26x2 / 双方)
		:aspect performance)
	:op2 (s26x3 / 致辞-01
		:ARG0 (s26x4 / 主客)
		:manner (s26x5 / 分别)
		:aspect performance)
	:op3 (s26x6 / 发言-01
		:ARG0 (s26x7 / 学生代表
			:mod (s26x8 / 台湾))
		:aspect performance))

# alignment:
s26c: 0-0
s26x: 2-2
s26x2: 1-1
s26x3: 7-7
s26x4: 5-5
s26x5: 6-6
s26x6: 14-14
s26x7: 12-12
s26x8: 11-11

# document level annotation:
(s26s0 / sentence
	:temporal ((document-creation-time :before s26x)
		(s26x :after s26x3)
		(s26x3 :after s26x6)))
	:modal ((root :modal author)
		(author :full-affirmative s26x)
		(author :full-affirmative s26x3)
		(author :full-affirmative s26x6)
		(root :modal author))

## chinese_umr-0007, sentence 34

# :: snt34
Index: 1 2  3 4  5  6 7  8 9  10 11 12  13 14
Words: 此 游戏 有 两个 结局 ， 分别 是 柯南 结局 和  金田一 结局 。 

# sentence level graph:
(s34e / exist-91
    :ARG1 (s34x2 / 游戏
        :mod (s34x4 / 此))
    :ARG2 (s34x3 / 结局
        :quant 2
        :unit (s34x5 / 个)
        :ARG1-of (s34i2 / identity-91
            :ARG2 (s34a / and
                :op1 (s34x6 / 结局
                    :topic (s34i3 / individual-person
                        :name (s34n / name
                            :op1 "柯南")))
                :op2 (s34x7 / 结局
                    :topic (s34i4 / individual-person
                        :name (s34n2 / name
                            :op1 "金田一"))))
            :mod (s34x8 / 分别-01)
            :aspect state))
    :aspect state)


# alignment:
s34a: 0-0
s34e: 0-0
s34i2: 0-0
s34i3: 0-0
s34i4: 0-0
s34n: 0-0
s34n2: 0-0
s34x2: 2-2
s34x3: 5-5
s34x4: 1-1
s34x5: 4-4
s34x6: 5-5
s34x7: 5-5
s34x8: 7-7

# document level annotation:
(s34s0 / sentence
    :temporal ((document-creation-time :overlap s34e))
    :modal ((root :modal author)
        (author :full-affirmative s34i2)
        (author :full-affirmative s34e))
    :coref ((s2x5 :same-entity s34x2)
        (s25i3 :same-entity s34i3)
        (s32i4 :same-entity s34i4)))

## chinese_umr-0007, sentence 59

# :: snt59
Index: 1    2 3 4  5 6  7 8  9  10 11 12 13 14 15 16  17 18 19 20 21 22 23 24
Words: 除此以外 ， 此 游戏 还 包含 了 三种 形式 的  特殊 调查 ，  分别 是  俯视图 调查 、  3D 调查 和  笔记 调查 。 

# sentence level graph:
(s59x / 包含-01
    :ARG0 (s59x15 / 游戏
        :mod (s59x16 / 此))
    :ARG1 (s59x4 / 调查
        :ARG1-of (s59i2 / identity-91
            :ARG2 (s59a2 / and
                :op1 (s59x5 / 调查
                    :instrument (s59x6 / 俯视图))
                :op2 (s59x7 / 调查
                    :mod (s59x8 / 3d))
                :op3 (s59x9 / 调查
                    :instrument (s59x10 / 笔记)))
            :mod (s59x11 / 分别)
            :aspect state)
        :manner (s59x12 / 形式
            :unit (s59x13 / 种)
            :quant 3)
        :ARG0-of (s59x14 / 特殊-01
            :aspect state))
    :aspect state
    :mod (s59x3 / 还)
    :ARG1-of (s59s / subtract-91
        :ARG2 (s59t / thing
            :refer-number singular
            :refer-person 3rd)))


# alignment:
s59a2: 0-0
s59i2: 0-0
s59s: 0-0
s59t: 0-0
s59x: 6-6
s59x10: 22-22
s59x11: 14-14
s59x12: 9-9
s59x13: 8-8
s59x14: 11-11
s59x15: 4-4
s59x16: 3-3
s59x3: 5-5
s59x4: 12-12
s59x5: 12-12
s59x6: 16-16
s59x7: 12-12
s59x8: 19-19
s59x9: 12-12

# document level annotation:
(s59s0 / sentence
    :temporal ((document-creation-time :overlap s59x)
        (s59x :overlap s59x14))
    :modal ((root :modal author)
        (author :full-affirmative s59i2)
        (author :full-affirmative s59x12)
        (author :full-affirmative s59x)
        (author :full-affirmative s59x14))
    :coref ((s58x6 :same-entity s59x15)
        (s58x2 :same-entity s59t)))

## chinese_umr-0004, sentence 55

# :: snt55
Index: 1  2  3 4  5   6 7 8   9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47   48 49 50 51   52 53 54 55 56 57 58  59   60 61 62 63 64 65
Words: 娱乐 报纸 《 影音 俱乐部 》 的 阿拉斯 代尔 给  这集 B  的  评分 ，  赞扬 琼斯 在  剧中 起到 的  作用 和  配角 们  的  演出 ，  但  同时 ，  他  对  戴  立克 为何 把  人们 变成 猪  奴隶 表示 不解 ，  并  认为 1930 年代 的  纽约 种族歧视 严重 ，  故  身为 黑人 的  罗所门 不太可能 成为 胡佛 村  的  领袖 。 

# sentence level graph:
(s55a / and
    :op1 (s55x4 / 给-01
        :ARG0 (s55i2 / individual-person
            :name (s55n / name
                :op1 "阿拉斯"
                :op2 "代尔")
            :ARG0-of (s55h / have-org-role-91
                :ARG1 (s55n2 / newspaper
                    :name (s55n3 / name
                        :op1 "影音"
                        :op2 "俱乐部")
                    :ARG1 (s55i3 / identity-91
                        :ARG2 (s55x5 / 报纸
                            :mod (s55x6 / 娱乐))
                        :aspect state))))
        :ARG1 (s55x8 / 集
            :mod (s55x9 / 这))
        :ARG2 (s55s / score-on-scale-91
            :ARG1 (s55b / b))
        :aspect performance)
    :op2 (s55x / 赞扬-02
        :ARG0 s55i2
        :ARG1 (s55a2 / and
            :op1 (s55x7 / 作用-01
                :ARG0 (s55i5 / individual-person
                    :name (s55n8 / name
                        :op1 "琼斯"))
                :place (s55x10 / 剧中)
                :aspect performance)
            :op2 (s55x2 / 演出-01
                :ARG0 (s55x3 / 配角
                    :refer-number plural)
                :aspect habitual))
        :aspect performance)
    :op3 (s55b2 / but-91
        :ARG2 (s55x11 / 表示-02
            :ARG0 s55i2
            :ARG1 (s55x12 / 不解-01
                :ARG0 s55i2
                :ARG1 (s55u / umr-unknown
                    :reason-of (s55x13 / 变成-01
                        :ARG0 (s55e / ethnic-group
                            :name (s55n4 / name
                                :op1 "戴"
                                :op2 "立克"))
                        :ARG1 (s55x14 / 人
                            :refer-number plural)
                        :ARG2 (s55x15 / 奴隶
                            :mod (s55x16 / 猪))
                        :aspect performance))
                :aspect state)
            :aspect performance))
    :op4 (s55x17 / 认为-01
        :ARG0 s55i2
        :ARG1 (s55h2 / have-reason-91
            :ARG1 (s55x18 / 严重-01
                :ARG0 (s55x19 / 歧视
                    :mod (s55x20 / 种族))
                :place (s55c / city
                    :name (s55n5 / name
                        :op1 "纽约"))
                :temporal (s55d / date-entity
                    :era 1930)
                :aspect state)
            :ARG2 (s55x21 / 成为-01
                :ARG0 (s55i4 / individual-person
                    :name (s55n7 / name
                        :op1 "罗所门")
                    :ARG0-of (s55x23 / 身为-01
                        :ARG1 (s55x24 / 黑人)
                        :aspect state))
                :ARG1 (s55x22 / 领袖
                    :place (s55c2 / city-district
                        :name (s55n6 / name
                            :op1 "胡佛"
                            :op2 "村")))
                :aspect performance)
            :aspect state)
        :aspect state))


# alignment:
s55a: 0-0
s55a2: 0-0
s55b: 12-12
s55b2: 12-12
s55c: 0-0
s55c2: 0-0
s55d: 0-0
s55e: 0-0
s55h: 0-0
s55h2: 0-0
s55i2: 0-0
s55i3: 0-0
s55i4: 0-0
s55i5: 0-0
s55n: 0-0
s55n2: 0-0
s55n3: 0-0
s55n4: 0-0
s55n5: 0-0
s55n6: 0-0
s55n7: 0-0
s55n8: 0-0
s55s: 0-0
s55u: 0-0
s55x: 16-16
s55x10: 19-19
s55x11: 42-42
s55x12: 43-43
s55x13: 39-39
s55x14: 38-38
s55x15: 41-41
s55x16: 40-40
s55x17: 46-46
s55x18: 52-52
s55x19: 51-51
s55x2: 27-27
s55x20: 51-51
s55x21: 60-60
s55x22: 64-64
s55x23: 55-55
s55x24: 56-56
s55x3: 24-24
s55x4: 10-10
s55x5: 2-2
s55x6: 1-1
s55x7: 22-22
s55x8: 11-11
s55x9: 11-11

# document level annotation:
(s55s0 / sentence
    :temporal ((document-creation-time :before s55x4)
        (s55x4 :overlap s55x)
        (s55x :overlap s55x7)
        (s55x :overlap s55x2)
        (s55x :overlap s55x11)
        (s55x11 :overlap s55x12)
        (s55x12 :overlap s55x13)
        (s55x11 :overlap s55x17)
        (s55x17 :overlap s55x18)
        (s55x18 :overlap s55x21)
        (s55x21 :overlap s55x23))
    :modal ((root :modal author)
        (author :full-affirmative s55i3)
        (author :full-affirmative s55x4)
        (author :full-affirmative s55x7)
        (author :full-affirmative s55x2)
        (author :full-affirmative s55x)
        (author :full-affirmative s55x13)
        (author :full-affirmative s55x12)
        (author :full-affirmative s55x11)
        (author :full-affirmative s55x18)
        (author :full-affirmative s55x23)
        (author :neutral-negative s55x21)
        (author :full-affirmative s55h2)
        (author :full-affirmative s55x17))
    :coref ((s54x18 :same-entity s55x8)
        (s34i3 :same-entity s55i5)
        (s54e :same-entity s55e)
        (s54x5 :same-entity s55x15)
        (s13i2 :same-entity s55i4)
        (s45c :same-entity s55c2)))

## chinese_umr-0025, sentence 993

# :: snt993
Index:  1  2  3  4  5    6  7  8  9 10 11   12   13 14 15   16 17   18   19 20 21 22   23 24   25   26 27 28 29 30   31 32 33 34 35   36 37 38     39 40   41 42 43
Words: 这  朵  花  ，  再  加上   三  座  只  有  我  膝盖   那么   高  的  火山   ，  而且   其中   一  座  还  可能   是  永远   熄灭   了  的  ，  这  一切   不  会  使  我  成为   一  个  了不起    的  王子   …  ” 

# sentence level graph:
(s993x46 / say
	:ARG1 (s993x33 / 会-02
		:ARG0 (s993x34 / 使-01
			:ARG0 (s993x31 / 一切
				:mod (s993x30 / 这)
				:ARG0-of (s993x52 / mean
					:ARG1 (s993x53 / and
						:op1 (s993x3 / 花
							:mod (s993x1 / 这)
							:unit (s993x2 / 朵))
						:op2 (s993x16 / 火山
							:quant 3
							:unit (s993x8 / 座)
							:ARG0-of (s993x14 / 高-02
								:ARG1 (s993x12 / 膝盖
									:part-of (s993x11 / individual-person
										:refer-person 1
										:refer-number singular))
								:degree (s993x13 / 那么)
								:mod (s993x9 / 只有))
							:ARG2-of (s993x19 / include-91
								:ARG1 (s993x66 / thing
									:unit (s993x21 / 座)
									:ARG1-of (s993x26 / 熄灭-01
										:mod (s993x25 / 永远)
										:aspect performance
										:ARG0-of (s993x23 / 可能
											:mod (s993x22 / 还)))))))))
			:ARG1 (s993x35 / individual-person
				:refer-person 1
				:refer-number singular)
			:ARG2 (s993x36 / 成为-01
				:ARG0 s993x35
				:ARG1 (s993x41 / 王子
					:mod (s993x39 / 了不起)
					:quant 1
					:unit (s993x38 / 个))))
		:polarity -))

# alignment:
s993x1: 1-1
s993x11: 0-0
s993x12: 12-12
s993x13: 13-13
s993x14: 14-14
s993x16: 16-16
s993x19: 0-0
s993x2: 2-2
s993x21: 8-8
s993x22: 22-22
s993x23: 23-23
s993x25: 25-25
s993x26: 26-26
s993x3: 3-3
s993x30: 1-1
s993x31: 31-31
s993x33: 33-33
s993x34: 34-34
s993x35: 0-0
s993x36: 36-36
s993x38: 38-38
s993x39: 39-39
s993x41: 41-41
s993x46: 0-0
s993x52: 0-0
s993x53: 0-0
s993x66: 0-0
s993x8: 8-8
s993x9: 9-9

# document level annotation:
(s993s0 / sentence)

## chinese_umr-0001, sentence 22

# :: snt22
Index: 1 2  3 4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
Words: 在 其他 的 八卦 小报 纷纷 转向 报导 名人 隐私 与  八卦 的  同时 ，  只有 《  世界 新闻 周报 》  仍  坚持 报导 这些 为  主流 媒体 所  「  忽略 」  的  怪异 「  新闻 事件 」  。 

# sentence level graph:
(s22h / have-temporal-91
    :ARG1 (s22x / 坚持-01
        :ARG0 (s22n2 / newspaper
            :name (s22n / name
                :op1 "《"
                :op2 "世界"
                :op3 "新闻"
                :op4 "周报"
                :op5 "》")
            :mod (s22x3 / 只有))
        :ARG1 (s22x2 / 报导-01
            :ARG1 (s22x4 / 事件
                :ARG1-of (s22x5 / 忽略-01
                    :ARG0 (s22x6 / 媒体
                        :mod (s22x7 / 主流))
                    :aspect performance)
                :mod (s22x8 / 怪异)
                :topic (s22x9 / 新闻))
            :aspect habitual)
        :aspect state)
    :ARG2 (s22x11 / 转向-01
        :ARG0 (s22x16 / 小报
            :topic (s22x17 / 八卦)
            :mod (s22x18 / 其他)
            :manner (s22x19 / 纷纷))
        :ARG2 (s22x12 / 报导-01
            :ARG1 (s22a / and
                :op1 (s22x13 / 隐私
                    :possessor (s22x15 / 名人))
                :op2 (s22x14 / 八卦))
            :aspect habitual)
        :aspect performance))


# alignment:
s22a: 0-0
s22h: 0-0
s22n: 0-0
s22n2: 0-0
s22x: 23-23
s22x11: 7-7
s22x12: 8-8
s22x13: 10-10
s22x14: 4-4
s22x15: 9-9
s22x16: 5-5
s22x17: 4-4
s22x18: 2-2
s22x19: 6-6
s22x2: 8-8
s22x3: 16-16
s22x4: 37-37
s22x5: 31-31
s22x6: 28-28
s22x7: 27-27
s22x8: 34-34
s22x9: 19-19

# document level annotation:
(s22s0 / sentence
    :temporal ((document-creation-time :before s22x)
        (s22x :overlap s22x2)
        (s22x2 :overlap s22x5)
        (s22x :overlap s22x11)
        (s22x11 :overlap s22x12))
    :modal ((root :modal author)
        (author :full-affirmative s22x5)
        (author :full-affirmative s22x2)
        (author :full-affirmative s22x)
        (author :full-affirmative s22x12)
        (author :full-affirmative s22x11))
    :coref ((s17x4 :same-entity s22n2)))

## chinese_umr-0006, sentence 33

# :: snt33
Index: 1  2   3 4  5  6 7  8  9  10 11  12 13 14 15 16 17 18  19 20 21 22  23 24 25 26 27 28 29 30 31 32  33 34 35 36
Words: 三强 设计师 须 运用 剩下 的 时间 继续 完成 最后 时装周 系列 的  准备 工作 ，  为  模特儿 试衣 ，  与  造型师 讨论 发型 和  化妆 的  设计 ，  最后 在  时装周 展示 其  时装 系列

# sentence level graph:
(s33x / 须-01
    :ARG0 (s33x24 / 设计师
        :mod (s33x25 / 三强))
    :ARG1 (s33a3 / and
        :op1 (s33x9 / 运用-01
            :ARG0 s33x24
            :ARG1 (s33x10 / 时间
                :mod (s33x11 / 剩下))
            :purpose (s33x4 / 完成-01
                :ARG0 s33x24
                :ARG1 (s33x8 / 工作
                    :ARG1-of (s33i2 / include-91
                        :ARG2 (s33a / and
                            :op1 (s33x17 / 试-01
                                :ARG0 (s33x18 / 模特儿)
                                :ARG1 (s33x22 / 衣)
                                :aspect performance)
                            :op2 (s33x12 / 讨论-01
                                :ARG0 s33x24
                                :ARG1 (s33x14 / 设计-01
                                    :topic (s33x16 / 发型)
                                    :topic (s33x15 / 化妆)
                                    :aspect performance)
                                :companion (s33x13 / 造型师)
                                :aspect performance))
                        :aspect state)
                    :ARG1-of (s33i3 / identity-91
                        :ARG2 (s33x7 / 准备-01
                            :ARG0 s33x24
                            :ARG1 (s33x19 / 系列
                                :part-of (s33x20 / 时装周
                                    :mod (s33x21 / 最后)))
                            :aspect performance)
                        :aspect state))
                :aspect performance)
            :aspect performance)
        :op2 (s33x2 / 展示-01
            :ARG0 s33x24
            :ARG1 (s33x3 / 系列
                :topic (s33x5 / 时装)
                :possessor s33x24)
            :place (s33x6 / 时装周)
            :temporal (s33x23 / 最后)
            :aspect performance))
    :aspect state)


# alignment:
s33a: 0-0
s33a3: 0-0
s33i2: 0-0
s33i3: 0-0
s33x: 3-3
s33x10: 7-7
s33x11: 5-5
s33x12: 23-23
s33x13: 22-22
s33x14: 28-28
s33x15: 26-26
s33x16: 24-24
s33x17: 19-19
s33x18: 18-18
s33x19: 12-12
s33x2: 33-33
s33x20: 11-11
s33x21: 10-10
s33x22: 19-19
s33x23: 10-10
s33x24: 2-2
s33x25: 1-1
s33x3: 12-12
s33x4: 9-9
s33x5: 35-35
s33x6: 11-11
s33x7: 14-14
s33x8: 15-15
s33x9: 4-4

# document level annotation:
(s33s0 / sentence
    :temporal ((document-creation-time :before s33x)
        (s33x :overlap s33x9)
        (s33x9 :overlap s33x4)
        (s33x4 :overlap s33i2)
        (s33i2 :overlap s33x17)
        (s33x17 :overlap s33x12)
        (s33x12 :overlap s33x14)
        (s33i2 :overlap s33i3)
        (s33i3 :overlap s33x7)
        (s33x9 :after s33x2))
    :modal ((root :modal author)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x17)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x14)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x12)
        (author :full-affirmative s33x24)
        (author :full-affirmative s33x24)
        (author :full-affirmative s33x24)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x4)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x9)
        (s33x24 :full-affirmative s33x)
        (s33x :unspecified s33x2)
        (author :full-affirmative s33x24))
    :coref ((s32x12 :same-entity s33x24)))

## chinese_umr-0025, sentence 1084

# :: snt1084
Index:  1  2  3    4    5  6    7  8
Words: 我  就  会  发现   幸福   的  代价   。 

# sentence level graph:
(s1084x3 / 会-02
	:ARG0 (s1084x4 / 发现-01
		:ARG0 (s1084x1 / individual-person
			:refer-person 1
			:refer-number singular)
		:ARG1 (s1084x7 / 代价
			:mod (s1084x5 / 幸福)))
	:mod (s1084x2 / 就))

# alignment:
s1084x1: 0-0
s1084x2: 2-2
s1084x3: 3-3
s1084x4: 4-4
s1084x5: 5-5
s1084x7: 7-7

# document level annotation:
(s1084s0 / sentence)

## chinese_umr-0025, sentence 1082

# :: snt1082
Index:    1  2    3  4  5  6  7    8    9 10
Words: 时间   越  临近   ，  我  就  越  感到   幸福   。 

# sentence level graph:
(s1082x2 / 越
	:ARG1 (s1082x3 / 临近-01
		:ARG0 (s1082x1 / 时间))
	:ARG2 (s1082x8 / 感到-01
		:ARG1 (s1082x9 / 幸福)
		:ARG0 (s1082x5 / individual-person
			:refer-person 1
			:refer-number singular)))

# alignment:
s1082x1: 1-1
s1082x2: 2-2
s1082x3: 3-3
s1082x5: 0-0
s1082x8: 8-8
s1082x9: 9-9

# document level annotation:
(s1082s0 / sentence)

## chinese_umr-0008, sentence 6

# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
Words: 朗埃克 在 设计 金币 时 想 了 多种 办法 确保 新币 和 2.5 美元 金币 有 显著 区别 ， 不但 采用 的 坯饼 更 薄 ， 而且 设计 图案 也 是 别具一格 。

# sentence level graph:
(s6a / and
    :op1 (s6x / 想-04
        :ARG0 (s6p / person
            :name (s6n / name
                :op1 "朗埃克"))
        :ARG1 (s6x11 / 办法
            :quant (s6x3 / 多)
            :unit (s6x4 / 种))
        :purpose (s6e / 确保-01
            :ARG0 s6p
            :ARG1 (s6x5 / 有-01
                :ARG0 (s6a3 / and
                    :op1 (s6x8 / 新币)
                    :op2 (s6x9 / 金币
                        :mod (s6m / monetary-quantity
                            :quant 2.5
                            :unit (s6x10 / 美元))))
                :ARG1 (s6x6 / 区别
                    :mod (s6x7 / 显著))
                :aspect state)
            :aspect performance)
        :temporal (s6d2 / 设计-01
            :ARG0 s6p
            :ARG1 (s6x2 / 金币)
            :aspect activity)
        :aspect performance)
    :op2 (s6a2 / and
        :op1 (s6x12 / 薄-01
            :ARG0 (s6x13 / 坯饼
                :ARG1-of (s6x18 / 采用-01
                    :ARG0 s6p
                    :aspect performance))
            :degree (s6x19 / 更)
            :aspect state)
        :op2 (s6x14 / 别具一格-01
            :ARG0 (s6x15 / 图案
                :mod (s6x16 / 设计))
            :mod (s6x20 / 也)
            :aspect state)))

# alignment:
s6a: 0-0
s6a2: 0-0
s6d2: 3-3
s6e: 10-10
s6e2: 0-0
s6i2: 0-0
s6n: 0-0
s6p: 0-0
s6t: 5-5
s6x: 6-6
s6x10: 14-14
s6x11: 9-9
s6x12: 25-25
s6x13: 23-23
s6x14: 32-32
s6x15: 29-29
s6x16: 3-3
s6x18: 21-21
s6x19: 24-24
s6x2: 4-4
s6x20: 30-30
s6x3: 8-8
s6x4: 8-8
s6x5: 16-16
s6x6: 18-18
s6x7: 17-17
s6x8: 11-11
s6x9: 4-4

# document level annotation:
(s6s0 / sentence
    :temporal ((document-creation-time :before s6d2)
            (s6d2 :overlap s6x)
            (s6x :overlap s6e)
            (s6e :overlap s6x5)
            (s6d2 :overlap s6x12)
            (s6x12 :overlap s6x18)
            (s6d2 :overlap s6x14))
    :modal ((author :full-affirmative s6x)
            (root :modal author)
            (author :full-affirmative s6x12)
            (author :full-affirmative s6x14)
            (s6p :partial-affirmative purpose)
            (purpose :full-affirmative s6e)
            (author :full-affirmative s6p)
            (author :full-affirmative s6d2)
            (s6p :partial-affirmative s6x5)
            (author :full-affirmative s6x18))
    :coref ((s1p :same-entity s6p)
            (s5x4 :same-entity s6x2)
            (s6x2 :same-entity s6x8)
            (s1x :same-event s6d2))
)

## chinese_umr-0025, sentence 153

# :: snt153
Index:  1  2    3  4    5  6    7    8  9   10   11 12   13   14   15 16 17   18 19 20 21   22   23   24 25   26 27
Words: 我  给  你们   讲  关于   小  行星   B612 的  这些   细节   ，  并且   告诉   你们   它  的  编号   ，  这  是  由于   这些   大人   的  缘故   。 

# sentence level graph:
(s153x28 / causation
	:ARG2 (s153x30 / and
		:op1 (s153x4 / 讲-01
			:ARG0 (s153x1 / individual-person
				:refer-person 1
				:refer-number singular)
			:ARG2 (s153x3 / individual-person
				:refer-person 2
				:refer-number plural)
			:ARG1 (s153x11 / 细节
				:mod (s153x10 / 这些)
				:topic (s153x7 / 行星
					:mod (s153x6 / 小)
					:name (s153x8 / name
						:op1 "b612")))
			:modal-strength (s153x49 / full-affirmative
				:conceiver (s153x50 / author)))
		:op2 (s153x14 / 告诉-01
			:ARG2 (s153x15 / individual-person
				:refer-person 2
				:refer-number plural)
			:ARG1 (s153x18 / 编号
				:possessor-of (s153x16 / individual-person
					:refer-person 3
					:refer-number singular))
			:ARG0 s153x1
			:modal-strength (s153x51 / full-affirmative
				:conceiver (s153x52 / author))))
	:ARG1 (s153x26 / 缘故
		:mod (s153x24 / 大人
			:mod (s153x23 / 这些)))
	:ARG1 (s153y1 / identity-91
		:ARG0 (s153x20 / 这)
		:ARG1 s153x26))

# alignment:
s153x1: 0-0
s153x10: 10-10
s153x11: 11-11
s153x14: 14-14
s153x15: 0-0
s153x16: 0-0
s153x18: 18-18
s153x20: 20-20
s153x23: 10-10
s153x24: 24-24
s153x26: 26-26
s153x28: 0-0
s153x3: 0-0
s153x30: 0-0
s153x4: 4-4
s153x49: 0-0
s153x50: 0-0
s153x51: 0-0
s153x52: 0-0
s153x6: 6-6
s153x7: 7-7
s153x8: 0-0
s153y1: 0-0

# document level annotation:
(s153s0 / sentence)

## chinese_umr-0025, sentence 990

# :: snt990
Index:  1    2        3  4  5  6 7    8  9   10   11 12 13 14   15 16 17   18 19 20 21   22 23 24   25 26   27 28   29 30 31   32 33 34 35   36   37 38
Words: 小  王子   自言自语     地  说  ：  “ 如果   她  看到   这些   ，  她  是  一定   会  很  恼火   …  她  会  咳嗽   得  更  厉害   ，  并且   为  避免   让  人  耻笑   ，  她  会  佯装   死去   。 

# sentence level graph:
(s990x5 / 说-01
	:ARG0 (s990x2 / 王子
		:mod (s990x1 / 小))
	:manner (s990x3 / 自言自语)
	:ARG1 (s990x44 / condition
		:ARG1 (s990x10 / 看到-01
			:ARG0 (s990x9 / individual-person
				:refer-person 3
				:refer-number singular)
			:ARG1 (s990x11 / 这些)
			:modal-strength (s990x72 / full-affirmative))
		:ARG2 (s990x48 / and
			:op1 (s990x15 / 一定
				:ARG0 (s990x16 / 会-02
					:ARG0 (s990x18 / 恼火-01
						:degree (s990x17 / 很)
						:ARG0 (s990x13 / individual-person
							:refer-person 3
							:refer-number singular)
						:modal-strength (s990x73 / full-affirmative)))
				:mode judgement)
			:op2 (s990x21 / 会-02
				:ARG0 (s990x22 / 咳嗽-01
					:ARG0 (s990x20 / individual-person
						:refer-person 3
						:refer-number singular)
					:degree (s990x25 / 厉害
						:degree (s990x24 / 更))
					:modal-strength (s990x74 / full-affirmative)))
			:op3 (s990x35 / 会-02
				:ARG0 (s990x36 / 佯装-01
					:ARG0 (s990x34 / individual-person
						:refer-person 3
						:refer-number singular)
					:ARG1 (s990x37 / 死去-01
						:ARG0 s990x34
						:modal-strength (s990x75 / full-affirmative)))
				:purpose (s990x29 / 避免-01
					:ARG1 (s990x32 / 耻笑-01
						:ARG0 (s990x31 / 人)
						:ARG1 s990x9))))
		:quote (s990x5 / 说-01)
		:modal-strength (s990x71 / neutral-affirmative
			:conceiver s990x2)))

# alignment:
s990x1: 1-1
s990x10: 10-10
s990x11: 11-11
s990x13: 0-0
s990x15: 15-15
s990x16: 16-16
s990x17: 17-17
s990x18: 18-18
s990x2: 2-2
s990x20: 0-0
s990x21: 16-16
s990x22: 22-22
s990x24: 24-24
s990x25: 25-25
s990x29: 29-29
s990x3: 3-3
s990x31: 31-31
s990x32: 32-32
s990x34: 0-0
s990x35: 16-16
s990x36: 36-36
s990x37: 37-37
s990x44: 0-0
s990x48: 0-0
s990x5: 5-5
s990x71: 0-0
s990x72: 0-0
s990x73: 0-0
s990x74: 0-0
s990x75: 0-0
s990x9: 0-0

# document level annotation:
(s990s0 / sentence)

## chinese_umr-0025, sentence 1059

# :: snt1059
Index:    1  2  3  4  5      6  7    8  9
Words: 但是   ，  你  有  着  金黄色    的  头发   。 

# sentence level graph:
(s1059x10 / contrast
	:ARG2 (s1059x4 / 有-01
		:aspect activity
		:ARG1 (s1059x8 / 头发
			:mod (s1059x6 / 金黄色))
		:ARG0 (s1059x3 / individual-person
			:refer-person 2
			:refer-number singular)
		:modal-strength (s1059x17 / full-affirmative)))

# alignment:
s1059x10: 0-0
s1059x17: 0-0
s1059x3: 0-0
s1059x4: 4-4
s1059x6: 6-6
s1059x8: 8-8

# document level annotation:
(s1059s0 / sentence)

## chinese_umr-0025, sentence 316

# :: snt316
Index:    1  2    3  4      5  6    7  8  9   10 11 12
Words: 摇动   着  脑袋   ，  金黄色    的  头发   随  风  颤动   着  。 

# sentence level graph:
(s316x13 / and
	:op1 (s316x1 / 摇动-01
		:aspect activity
		:ARG1 (s316x3 / 脑袋)
		:modal-strength (s316x24 / full-affirmative))
	:op2 (s316x10 / 颤动-01
		:ARG0 (s316x7 / 头发
			:mod (s316x5 / 金黄色))
		:manner (s316x8 / 随-01
			:ARG1 (s316x9 / 风))
		:aspect activity
		:modal-strength (s316x25 / full-affirmative)))

# alignment:
s316x1: 1-1
s316x10: 10-10
s316x13: 0-0
s316x24: 0-0
s316x25: 0-0
s316x3: 3-3
s316x5: 5-5
s316x7: 7-7
s316x8: 8-8
s316x9: 9-9

# document level annotation:
(s316s0 / sentence)

## chinese_umr-0020, sentence 4

# :: snt4
Index:  1    2    3  4    5    6  7  8    9   10 11 12   13 14   15   16     17   18 19   20 21 22   23   24   25 26   27   28 29   30 31   32 33 34
Words: 在  中国   民间   有  一种   习俗   ，  当  男女   结婚   时  ，  新郎   将  给予   新娘   一部分    财产   或  首饰   ，  以  作为   结婚   聘礼   ，  这种   习俗   被  称为   “  彩礼   ”  。 

# sentence level graph:
(s4a / and
	:op1 (s4x4 / 有-05
		:ARG1 (s4x5 / 习俗
			:unit (s4x6 / 种
				:quant (s4x7 / 一))
			:aspect habitual)
		:aspect habitual
		:place (s4l / location
			:part (s4c / country
				:name (s4n2 / name
					:op1 "中国")
				:mod (s4x18 / 民间))))
	:op2 (s4x8 / 给予-01
		:ARG0 (s4x15 / 新郎)
		:ARG1 (s4x14 / 新娘)
		:ARG2 (s4a2 / and
			:op1 (s4x12 / 财产
				:quant (s4x13 / 一部分))
			:op2 (s4x11 / 首饰))
		:purpose (s4x9 / 聘礼
			:mod (s4x10 / 结婚))
		:mod (s4t / temporal
			:op1 (s4x16 / 结婚-01
				:ARG0 (s4x17 / 男女)))
		:ARG1 (s4x2 / 习俗))
	:op3 (s4x / 称为-01
		:ARG1 (s4x3 / 习俗
			:mod (s4x19 / 这种))
		:ARG2 (s4d / dowry
			:name (s4n / name
				:op1 "彩礼"))))

# alignment:
s4a: 0-0
s4a2: 0-0
s4c: 0-0
s4d: 0-0
s4l: 0-0
s4n: 0-0
s4n2: 0-0
s4t: 0-0
s4x: 30-30
s4x10: 10-10
s4x11: 20-20
s4x12: 18-18
s4x13: 17-17
s4x14: 16-16
s4x15: 13-13
s4x16: 10-10
s4x17: 9-9
s4x18: 3-3
s4x19: 27-27
s4x2: 6-6
s4x3: 6-6
s4x4: 4-4
s4x5: 6-6
s4x6: 5-5
s4x7: 5-5
s4x8: 15-15
s4x9: 25-25

# document level annotation:
(s4s0 / sentence
	:temporal ((document-creation-time :overlap s4x4)
		(s4x4 :depends-on s4x8)
		(s4x4 :depends-on s4t)
		(s4x4 :overlap s4x))
	:modal ((root :modal author)
		(author :full-affirmative s4x5)
		(author :full-affirmative s4x4))
	:coref ((s4x7 :same-entity s4x19)
		(s4x5 :same-event s4x3)))

## chinese_umr-0010, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Words: 在 中国 民间 有 一种 习俗 ， 当 男女 结婚 时 ， 新郎 将 给予 新娘 一部分 财产 或 首饰 ， 以 作为 结婚 聘礼 ， 这种 习俗 被 称为 “ 彩礼 ” 。

# sentence level graph:
(s4a2 / and
    :op1 (s4x18 / 有-03
        :ARG0 (s4x6 / 民间
            :mod (s4c / country
                :name (s4n / name
                    :op1 "中国")))
        :ARG1 (s4x / 习俗
            :unit (s4x2 / 种)
            :quant 1
            :ARG1-of (s4x15 / 称为-01
                :ARG2 (s4x16 / 彩礼)
                :aspect state
                :modal-strength full-affirmative))
        :aspect state
        :modal-strength full-affirmative)
    :op2 (s4x17 / 给予-01
        :ARG0 (s4x11 / 新郎)
        :ARG1 (s4a / or
            :op1 (s4x7 / 财产
                :quant (s4x8 / 一部分))
            :op2 (s4x9 / 首饰))
        :ARG2 (s4x10 / 新娘)
        :purpose (s4x12 / 作为-02
            :ARG0 s4a
            :ARG1 (s4x19 / 聘礼
                :mod (s4x13 / 结婚))
            :aspect state
            :modal-strength full-affirmative)
        :temporal (s4x3 / 时
            :op1 (s4x4 / 结婚-01
                :ARG0 (s4x5 / 男女)
                :aspect habitual
                :modal-strength undefined))
        :aspect habitual
        :modal-strength full-affirmative))

# alignment:
s4a: 0-0
s4a2: 0-0
s4c: 0-0
s4h: 0-0
s4n: 0-0
s4n2: 0-0
s4x: 6-6
s4x10: 16-16
s4x11: 13-13
s4x12: 25-25
s4x13: 10-10
s4x15: 30-30
s4x16: 32-32
s4x17: 15-15
s4x18: 4-4
s4x19: 25-25
s4x2: 5-5
s4x3: 11-11
s4x4: 10-10
s4x5: 9-9
s4x6: 3-3
s4x7: 18-18
s4x8: 17-17
s4x9: 20-20

# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :overlap s4x18)
            (s4x18 :overlap s4x15)
            (s4x18 :overlap s4x17)
            (s4x17 :overlap s4x12)
            (s4x17 :overlap s4x3)
            (s4x3 :overlap s4x4))
    :modal ((author :full-affirmative s4x15)
            (root :modal author)
            (author :full-affirmative s4x17)
            (author :full-affirmative s4x11)
            (s4x11 :partial-affirmative purpose)
            (purpose :full-affirmative s4x12)
            (author :full-affirmative s4x18)
            (author :unspecified s4x4))
    :coref ()
)

## chinese_umr-0020, sentence 2

# :: snt2
Index:    1  2  3    4    5    6    7    8  9   10   11   12   13 14   15   16   17 18   19 20   21 22 23
Words: 此前   也  有  部分   地方   政府   发布   文件   ，  禁止   收取   天价   彩礼   ，  要求   摒弃   这种   “  落后   的  习俗   ”  。 

# sentence level graph:
(s2x6 / 也
	:ARG0 (s2i2 / implicit-argument)
	:ARG1 (s2x11 / 有-05
		:ARG0 (s2g / government-organization
			:possessor-of (s2x18 / 地方)
			:quant (s2x19 / 部分))
		:ARG1 (s2a2 / and
			:op1 (s2x / 发布-01
				:ARG1 (s2x2 / 文件
					:ARG1-of (s2a / and))
				:aspect performance)
			:op2 (s2x10 / 禁止-01
				:ARG1 (s2x12 / 收取-01
					:ARG1 (s2x13 / 彩礼
						:mod (s2x14 / 天价))
					:aspect performance)
				:aspect habitual)
			:op3 (s2x3 / 要求-01
				:ARG1 (s2x4 / 摒弃-01
					:ARG1 (s2x5 / 习俗
						:mod (s2x9 / 落后)
						:mod (s2x16 / 这种))
					:aspect performance)
				:aspect habitual)))
	:temporal (s2x15 / 此前))

# alignment:
s2a: 0-0
s2a2: 0-0
s2g: 0-0
s2i2: 0-0
s2x: 7-7
s2x10: 10-10
s2x11: 3-3
s2x12: 11-11
s2x13: 13-13
s2x14: 12-12
s2x15: 1-1
s2x16: 17-17
s2x18: 5-5
s2x19: 4-4
s2x2: 8-8
s2x3: 15-15
s2x4: 16-16
s2x5: 21-21
s2x6: 2-2
s2x9: 19-19

# document level annotation:
(s2s0 / sentence
	:temporal ((s1a :before s2x6)
		(s2a2 :depends-on s2x)
		(s2x :overlap s2x10)
		(s2x :overlap s2x3)
		(s2x10 :depends-on s2x12)
		(s2x3 :depends-on s2x4))
	:modal ((root :modal author)
		(author :full-affirmative s2x)
		(author :full-affirmative s2x12)
		(author :full-affirmative s2x10)
		(author :full-affirmative s2x4)
		(author :full-affirmative s2x3))
	:coref ((s1g2 :subset-of s2x18)))

## chinese_umr-0025, sentence 1328

# :: snt1328
Index:  1    2  3    4    5  6  7 8 9
Words: 你  不久   就  可以   回家   去  了  … ”

# sentence level graph:
(s1328x10 / say
	:ARG1 (s1328x4 / 可以-01
		:ARG0 (s1328x5 / 回家-01
			:ARG0 (s1328x1 / individual-person
				:refer-person 2
				:refer-number singular))
		:temporal (s1328x2 / 不久)
		:mod (s1328x3 / 就)
		:smood (s1328x7 / 了)))

# alignment:
s1328x1: 0-0
s1328x10: 0-0
s1328x2: 2-2
s1328x3: 3-3
s1328x4: 4-4
s1328x5: 5-5
s1328x7: 7-7

# document level annotation:
(s1328s0 / sentence)

## chinese_umr-0025, sentence 1490

# :: snt1490
Index:    1    2    3  4  5  6  7    8  9 10
Words: 赶快   写信   告诉   我  ，  他  又  回来   了  … 

# sentence level graph:
(s1490x3 / 告诉-01
	:manner (s1490x2 / 写信
		:mod (s1490x1 / 赶快))
	:ARG2 (s1490x4 / individual-person
		:refer-person 1
		:refer-number singular)
	:ARG1 (s1490x8 / 回来-01
		:ARG0 (s1490x6 / individual-person
			:refer-person 3
			:refer-number singular)
		:mod (s1490x7 / 又))
	:mode imperative
	:modal-strength (s1490x21 / partial-affirmative))

# alignment:
s1490x1: 1-1
s1490x2: 2-2
s1490x21: 0-0
s1490x3: 3-3
s1490x4: 0-0
s1490x6: 0-0
s1490x7: 7-7
s1490x8: 8-8

# document level annotation:
(s1490s0 / sentence)

## chinese_umr-0025, sentence 1332

# :: snt1332
Index:    1  2  3    4  5  6  7 8  9   10 11 12 13 14 15 16 17 18 19 20 21
Words: 然后   ，  他  忧伤   地  说  ：  “ 我  回家   要  远  得  多  …  要  难  得  多  …  ” 

# sentence level graph:
(s1332x22 / temporal
	:ARG2 (s1332x6 / 说-01
		:ARG0 (s1332x3 / individual-person
			:refer-person 3
			:refer-number singular)
		:manner (s1332x4 / 忧伤)
		:ARG1 (s1332x27 / and
			:op1 (s1332x11 / 要-03
				:ARG0 (s1332x12 / 远-01
					:degree (s1332x14 / 多)
					:ARG0 (s1332x10 / 回家-01
						:ARG0 (s1332x9 / individual-person
							:refer-person 1
							:refer-number singular))))
			:op2 (s1332x16 / 要-03
				:ARG0 (s1332x17 / 难-01
					:degree (s1332x19 / 多))))
		:modal-strength (s1332x36 / full-affirmative)))

# alignment:
s1332x10: 10-10
s1332x11: 11-11
s1332x12: 12-12
s1332x14: 14-14
s1332x16: 11-11
s1332x17: 17-17
s1332x19: 14-14
s1332x22: 0-0
s1332x27: 0-0
s1332x3: 0-0
s1332x36: 0-0
s1332x4: 4-4
s1332x6: 6-6
s1332x9: 0-0

# document level annotation:
(s1332s0 / sentence)
