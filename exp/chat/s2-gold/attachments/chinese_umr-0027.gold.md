# Gold UMR annotations of sentences like those of chinese_umr-0027

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0002, sentence 49

# :: snt49
Index: 1     2  3    4   5  6 7    8 9  10  11 12 13 14 15 16 17 18 19 20 21 22 23 24   25 26 27  28 29 30 31 32 33   34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61  62   63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
Words: 曼彻斯特城 足球 俱乐部队 总教练 佩普 · 瓜迪奥拉 在 听闻 爆炸案 事件 后  相当 震惊 ，  因为 他  的  妻儿 正好 也  参与 了  亚莉安娜 当晚 的  演唱会 ，  虽然 事后 得知 妻儿 安然无恙 ，  不过 因为 该  事件 造成 的  伤亡 ，  球团 对于 有关 家庭 的  相关 问题 并未 表态 后续 的  意见 ，  但  在  事发 当晚 ，  主球场 阿提哈德 球场 就  被  当地 政府 指定 为  紧急 救难 中心 ，  协助 安顿 事件 中  的  伤员 者  。 

# sentence level graph:
(s49a / and
    :op1 (s49b / but-91
        :ARG1 (s49h / have-reason-91
            :ARG1 (s49x / 震惊-01
                :ARG0 (s49i2 / individual-person
                    :name (s49n / name
                        :op1 "佩普"
                        :op2 "·"
                        :op3 "瓜迪奥拉")
                    :ARG1-of (s49h2 / have-org-role-91
                        :ARG2 (s49s / sports-organization
                            :name (s49n2 / name
                                :op1 "曼彻斯特城"
                                :op2 "足球"
                                :op3 "俱乐部队"))
                        :ARG3 (s49x4 / 教练
                            :mod (s49x5 / 总))))
                :temporal (s49x6 / 后
                    :op1 (s49x7 / 听闻-01
                        :ARG0 s49i2
                        :ARG1 (s49x8 / 事件
                            :ARG1-of (s49i3 / identity-91
                                :ARG2 (s49x9 / 爆炸案)
                                :aspect state))
                        :aspect performance))
                :degree intensifier
                :aspect state
                :mod (s49x38 / 相当))
            :ARG2 (s49x2 / 参与-01
                :ARG0 (s49p / person
                    :refer-number plural
                    :ARG1-of (s49h3 / have-rel-role-91
                        :ARG2 s49i2
                        :ARG3 (s49x10 / 妻儿)))
                :ARG1 (s49x13 / 演唱会
                    :temporal (s49x14 / 当晚)
                    :ARG1-of (s49i6 / implicit-argument
                        :ARG0 (s49i4 / individual-person
                            :name (s49n3 / name
                                :op1 "亚莉安娜"))
                        :aspect performance))
                :mod (s49x11 / 正好)
                :mod (s49x12 / 也)
                :aspect performance))
        :ARG2 (s49x3 / 得知-01
            :ARG0 s49i2
            :ARG2 (s49x15 / 安然无恙
                :ARG2-of (s49h4 / have-mod-91
                    :ARG1 s49p
                    :aspect state))
            :aspect state))
    :op2 (s49b3 / but-91
        :ARG1 (s49x16 / 表态-01
            :ARG0 s49s
            :ARG1 (s49x17 / 意见
                :mod (s49x18 / 后续)
                :topic (s49x19 / 问题
                    :ARG1-of (s49x20 / 相关-01
                        :ARG2 (s49x21 / 家庭))))
            :aspect performance
            :reason (s49x22 / 伤亡-01
                :ARG1-of (s49x23 / 造成-01
                    :ARG0 s49x9))))
    :op3 (s49b2 / but-91
        :ARG1 (s49x24 / 指定-02
            :ARG0 (s49x25 / 政府
                :place (s49x27 / 当地))
            :ARG1 (s49s2 / sports-facility
                :name (s49n4 / name
                    :op1 "阿提哈德"
                    :op2 "球场")
                :ARG1-of (s49i5 / identity-91
                    :ARG2 (s49x28 / 球场
                        :mod (s49x29 / 主))))
            :ARG2 (s49x26 / 中心
                :mod (s49x30 / 救难
                    :mod (s49x31 / 紧急)))
            :aspect state
            :purpose (s49x32 / 协助-02
                :ARG2 (s49x33 / 安顿-01
                    :ARG1 (s49x34 / 员
                        :ARG0-of (s49x35 / 伤-01
                            :reason s49x9))
                    :aspect performance)
                :aspect process)
            :temporal (s49x36 / 当晚
                :op1 (s49x37 / 事发-01
                    :aspect performance)))))


# alignment:
s49a: 0-0
s49b: 0-0
s49b2: 0-0
s49b3: 0-0
s49h: 0-0
s49h2: 0-0
s49h3: 0-0
s49h4: 0-0
s49i2: 0-0
s49i3: 0-0
s49i4: 0-0
s49i5: 0-0
s49i6: 0-0
s49n: 0-0
s49n2: 0-0
s49n3: 0-0
s49n4: 0-0
s49p: 0-0
s49s: 0-0
s49s2: 0-0
s49x: 14-14
s49x10: 19-19
s49x11: 20-20
s49x12: 21-21
s49x13: 27-27
s49x14: 25-25
s49x15: 33-33
s49x16: 51-51
s49x17: 54-54
s49x18: 52-52
s49x19: 49-49
s49x2: 22-22
s49x20: 48-48
s49x21: 46-46
s49x22: 41-41
s49x23: 39-39
s49x24: 68-68
s49x25: 67-67
s49x26: 72-72
s49x27: 66-66
s49x28: 63-63
s49x29: 61-61
s49x3: 31-31
s49x30: 71-71
s49x31: 70-70
s49x32: 74-74
s49x33: 75-75
s49x34: 79-79
s49x35: 41-41
s49x36: 25-25
s49x37: 58-58
s49x38: 13-13
s49x4: 4-4
s49x5: 4-4
s49x6: 12-12
s49x7: 9-9
s49x8: 11-11
s49x9: 10-10

# document level annotation:
(s49s0 / sentence
    :temporal ((document-creation-time :before s49x)
        (s49x :before s49x7)
        (s49x :before s49x2)
        (s49x2 :after s49x3)
        (s49x2 :after s49x3)
        (s49x3 :overlap s49h4)
        (s49x3 :after s49x16)
        (s49x16 :overlap s49x20)
        (s49x16 :before s49x22)
        (s49x22 :overlap s49x23)
        (document-creation-time :before s49x24)
        (s49x24 :after s49x32)
        (s49x32 :overlap s49x33)
        (s49x33 :before s49x35)
        (s49x24 :before s49x37))
    :modal ((root :modal author)
        (author :full-affirmative s49i3)
        (author :full-affirmative s49x7)
        (author :full-affirmative s49x)
        (author :full-affirmative s49i6)
        (author :full-affirmative s49x2)
        (author :full-affirmative s49h4)
        (author :full-affirmative s49x3)
        (author :full-negative s49x16)
        (author :full-affirmative s49x24)
        (author :full-affirmative s49x33)
        (author :full-affirmative s49x32)
        (author :full-affirmative s49x37))
    :coref ((s48s :same-entity s49s)
        (s47x21 :same-event s49x8)
        (s37x5 :same-event s49x13)
        (s10i2 :same-entity s49i4)
        (s47x22 :same-event s49x37)))

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

## chinese_umr-0002, sentence 10

# :: snt10
Index: 1  2   3  4 5  6 7  8
Words: 歌手 格兰德 并未 在 事件 中 受伤 。

# sentence level graph:
(s10x / 受伤-01
    :ARG0 (s10i2 / individual-person
        :name (s10n / name
            :op1 "格兰德")
        :ARG1-of (s10i3 / identity-91
            :ARG2 (s10x2 / 歌手)))
    :place (s10x3 / 事件)
    :aspect performance
    :polarity -)


# alignment:
s10i2: 0-0
s10i3: 0-0
s10n: 0-0
s10x: 7-7
s10x2: 1-1
s10x3: 5-5

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10x))
    :modal ((root :modal author)
        (author :full-negative s10x))
    :coref ((s3i3 :same-entity s10i2)
        (s3x :same-event s10x3)))

## chinese_umr-0002, sentence 20

# :: snt20
Index: 1  2 3 4    5  6 7  8  9  10 11 12 13 14 15 16  17 18 19 20 21 22 23 24 25 26 27  28 29 30 31 32 33
Words: 警方 还 在 曼彻斯特 南部 的 另外 两个 地点 展开 行动 ，  并  突袭 了  华里区 的  一个 住址 ，  逮捕 了  三名 可能 是  支援 袭击者 “  网络 ”  的  人士 。 

# sentence level graph:
(s20a / and
    :op1 (s20x / 展开-01
        :ARG0 (s20x4 / 警方)
        :ARG1 (s20x5 / 行动-01
            :ARG0 s20x4
            :aspect activity)
        :place (s20x6 / 地点
            :mod (s20x7 / 另外)
            :quant 2
            :unit (s20x8 / 个)
            :place (s20x9 / 南部
                :part-of (s20c / city
                    :name (s20n / name
                        :op1 "曼彻斯特"))))
        :aspect performance
        :mod (s20x19 / 还))
    :op2 (s20x2 / 突袭-01
        :ARG0 s20x4
        :ARG1 (s20x10 / 住址
            :quant 1
            :unit (s20x11 / 个)
            :place (s20c2 / city-district
                :name (s20n2 / name
                    :op1 "华里区")))
        :aspect performance)
    :op3 (s20x3 / 逮捕-01
        :ARG0 s20x4
        :ARG1 (s20x12 / 人士
            :quant 3
            :unit (s20x13 / 名)
            :ARG0-of (s20x14 / 支援-01
                :ARG1 (s20x15 / 网络
                    :part-of (s20x16 / 者
                        :ARG0-of (s20x17 / 袭击-01
                            :aspect performance)))
                :aspect habitual))
        :aspect performance))


# alignment:
s20a: 0-0
s20c: 0-0
s20c2: 0-0
s20n: 0-0
s20n2: 0-0
s20x: 10-10
s20x10: 19-19
s20x11: 8-8
s20x12: 32-32
s20x13: 23-23
s20x14: 26-26
s20x15: 29-29
s20x16: 27-27
s20x17: 27-27
s20x19: 2-2
s20x2: 14-14
s20x3: 21-21
s20x4: 1-1
s20x5: 11-11
s20x6: 9-9
s20x7: 7-7
s20x8: 8-8
s20x9: 5-5

# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20x)
        (s20x :overlap s20x5)
        (s20x5 :overlap s20x2)
        (s20x2 :overlap s20x3)
        (s20x3 :before s20x14)
        (s20x14 :overlap s20x17))
    :modal ((root :modal author)
        (author :full-affirmative s20x5)
        (author :full-affirmative s20x)
        (author :full-affirmative s20x2)
        (author :full-affirmative s20x17)
        (author :full-affirmative s20x14)
        (author :full-affirmative s20x3)
        (author :neutral-affirmative s20x14))
    :coref ((s19i7 :same-entity s20x16)))

## chinese_umr-0002, sentence 24

# :: snt24
Index: 1   2 3  4 5 6 7  8 9 10 11 12 13 14 15 16 17 18  19 20 21
Words: 袭击者 的 父亲 和 他 的 弟弟 于 5 月  23 日  和  24 日  分别 被  叙利亚 当局 逮捕 。 

# sentence level graph:
(s24a / and
    :op1 (s24x / 逮捕-01
        :ARG0 (s24x6 / 当局
            :place (s24c / country
                :name (s24n / name
                    :op1 "叙利亚")))
        :ARG1 (s24x3 / 父亲
            :ARG3-of (s24h / have-rel-role-91
                :ARG2 (s24x4 / 者
                    :ARG0-of (s24x5 / 袭击-01
                        :aspect performance))))
        :temporal (s24d / date-entity
            :day 23
            :month 5)
        :aspect performance)
    :op2 (s24x2 / 逮捕-01
        :ARG0 s24x6
        :ARG1 (s24x7 / 弟弟
            :ARG3-of (s24h2 / have-rel-role-91
                :ARG2 s24x4))
        :temporal (s24d2 / date-entity
            :day 24
            :month 5)
        :aspect performance))


# alignment:
s24a: 0-0
s24c: 0-0
s24d: 0-0
s24d2: 0-0
s24h: 0-0
s24h2: 0-0
s24n: 0-0
s24x: 20-20
s24x2: 20-20
s24x3: 3-3
s24x4: 1-1
s24x5: 1-1
s24x6: 19-19
s24x7: 7-7

# document level annotation:
(s24s0 / sentence
    :temporal ((s24d :overlap s24x)
        (s24d2 :overlap s24x2)
        (document-creation-time :before s24d)
        (document-creation-time :before s24d2)
        (s24x :after s24x2))
    :modal ((root :modal author)
        (author :full-affirmative s24x5)
        (author :full-affirmative s24x)
        (author :full-affirmative s24x2))
    :coref ((s17x2 :subset-of s24x3)
        (s12x11 :subset-of s24x7)
        (s22x14 :same-event s24x5)))

## chinese_umr-0015, sentence 3

# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Words: 随着 积雪 带来 的 南方 寒潮 ， 广东 广州 等 地 迎来 今年 最低 温 。

# sentence level graph:
(s3x / 迎来-01
    :ARG0 (s3c / city
        :name (s3n / name
            :op1 "广州")
        :part-of (s3p / province
            :name (s3n2 / name
                :op1 "广东")))
    :ARG1 (s3x2 / 温
        :temporal (s3x4 / 今年)
        :mod (s3x10 / 低
            :degree (s3x11 / 最)))
    :temporal (s3x5 / 随着
        :op1 (s3x6 / 带来-01
            :ARG0 (s3x7 / 积雪)
            :ARG1 (s3x8 / 寒潮
                :place (s3x9 / 南方))
            :aspect performance))
    :aspect performance)

# alignment:
s3c: 0-0
s3h: 0-0
s3n: 0-0
s3n2: 0-0
s3p: 0-0
s3x: 12-12
s3x10: 14-14
s3x11: 14-14
s3x2: 15-15
s3x4: 13-13
s3x5: 1-1
s3x6: 3-3
s3x7: 2-2
s3x8: 6-6
s3x9: 5-5

# document level annotation:
(s3s0 / sentence
    :temporal ((s3x :overlap s3x6))
    :modal ((root :modal author)
            (author :full-affirmative s3x6)
            (author :full-affirmative s3x))
    :coref ((s2x7 :same-entity s3x8))
)

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

## chinese_umr-0033, sentence 12

# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Words: 另外 ， 以色列 警方 拘捕 一名 商人 ， 指被 伊朗 招揽 成为 刺客 ， 讨论 过 行刺 总理 内塔尼亚胡

# sentence level graph:
(s12c / consecutive
    :op1 (s12x / 拘捕-01
        :ARG0 (s12x3 / 警方
            :possessor (s12c2 / country
                :name (s12n / name
                    :op1 "以色列")))
        :ARG1 (s12x4 / 商人
            :quant 1
            :unit (s12x5 / 名))
        :mod (s12x2 / 另外)
        :aspect performance)
    :op2 (s12x6 / 指-02
        :ARG0 s12x3
        :ARG1 (s12a / and
            :op1 (s12x7 / 招揽-01
                :ARG0 (s12c3 / country
                    :name (s12n2 / name
                        :op1 "伊朗"))
                :ARG1 s12x4
                :result (s12i3 / identity-91
                    :ARG1 s12x4
                    :ARG2 (s12x8 / 刺客)
                    :aspect state)
                :aspect performance)
            :op2 (s12x9 / 讨论-01
                :ARG0 s12x4
                :ARG1 (s12x10 / 行刺-01
                    :ARG0 s12x4
                    :ARG1 (s12i2 / individual-person
                        :name (s12n3 / name
                            :op1 "内塔尼亚胡")
                        :ARG1-of (s12i4 / identity-91
                            :ARG2 (s12x11 / 总理)
                            :aspect state))
                    :aspect performance)
                :aspect performance))
        :aspect performance))

# alignment:
s12a: 0-0
s12a2: 0-0
s12c: 0-0
s12c2: 3-3
s12c3: 10-10
s12i2: 19-19
s12i3: 0-0
s12i4: 0-0
s12n: 0-0
s12n2: 0-0
s12n3: 0-0
s12x: 5-5
s12x10: 17-17
s12x11: 18-18
s12x2: 1-1
s12x3: 4-4
s12x4: 7-7
s12x5: 6-6
s12x6: 9-9
s12x7: 11-11
s12x8: 13-13
s12x9: 15-15

# document level annotation:
(s12s0 / sentence
    :temporal ((s12x9 :before s12x7)
            (s12x :before s12x9)
            (s12x6 :before s12x))
    :modal ((root :modal author)
            (author :full-affirmative s12x)
            (author :full-affirmative s12x6)
            (author :full-affirmative s12x3)
            (s12x3 :full-affirmative s12x7)
            (s12x3 :full-affirmative s12x9)
            (s12x3 :neutral-affirmative s12x10))
    :coref ((s6c2 :same-entity s12c2)
            (s3c2 :same-entity s12c3))
)

## chinese_umr-0007, sentence 6

# :: snt6
Index: 1  2 3  4 5  6 7  8  9  10 11 12 13  14 15 16 17 18 19  20 21 22 23 24 25 26 27  28 29 30 31 32
Words: 他们 在 调查 时 发现 了 很多 奇怪 事件 ，  其中 包括 金田一 描述 的  「  另  一个 夕闇岛 」  、  25 年前 的  惨剧 、  一之濑 惠一 自杀 事件 等  。 

# sentence level graph:
(s6x / 发现-01
    :ARG0 (s6p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s6x2 / 事件
        :quant (s6x4 / 很多)
        :ARG0-of (s6x5 / 奇怪-01
            :aspect state)
        :ARG2-of (s6i2 / include-91
            :ARG1 (s6e / event
                :name (s6n / name
                    :op1 "另"
                    :op2 "一个"
                    :op3 "夕闇岛")
                :ARG1-of (s6x9 / 描述-01
                    :ARG0 (s6i3 / individual-person
                        :name (s6n2 / name
                            :op1 "金田一"))
                    :aspect state))
            :ARG2 (s6x6 / 惨剧
                :temporal (s6x10 / 前
                    :op1 (s6t / temporal-quantity
                        :quant 25
                        :unit (s6x11 / 年))))
            :ARG3 (s6x7 / 事件
                :ARG1-of (s6i4 / identity-91
                    :ARG2 (s6x12 / 自杀-01
                        :ARG0 (s6i5 / individual-person
                            :name (s6n3 / name
                                :op1 "一之濑"
                                :op2 "惠一"))
                        :aspect performance)))
            :ARG4 (s6x8 / 等)
            :aspect state))
    :temporal (s6x3 / 调查-01
        :ARG0 s6p
        :aspect performance)
    :aspect performance)


# alignment:
s6e: 0-0
s6i2: 0-0
s6i3: 0-0
s6i4: 0-0
s6i5: 0-0
s6n: 0-0
s6n2: 0-0
s6n3: 0-0
s6p: 0-0
s6t: 0-0
s6x: 5-5
s6x10: 23-23
s6x11: 23-23
s6x12: 29-29
s6x2: 9-9
s6x3: 3-3
s6x4: 7-7
s6x5: 8-8
s6x6: 25-25
s6x7: 9-9
s6x8: 31-31
s6x9: 14-14

# document level annotation:
(s6s0 / sentence
    :temporal ((s3x2 :overlap s6x3)
        (s6x3 :contained s6x)
        (s6x :overlap s6x5)
        (s6x5 :overlap s6i2)
        (s6i2 :overlap s6x9)
        (s6i2 :before s6x12))
    :modal ((root :modal author)
        (author :full-affirmative s6x5)
        (author :full-affirmative s6x9)
        (author :full-affirmative s6x12)
        (author :full-affirmative s6i2)
        (author :full-affirmative s6x3)
        (author :full-affirmative s6x))
    :coref ((s5i5 :same-entity s6i3)
        (s4p :same-entity s6p)
        (s3x2 :same-event s6x3)))

## chinese_umr-0025, sentence 374

# :: snt374
Index:  1  2  3    4    5    6  7 8 9
Words: 我  是  与  太阳   同时   出生   的  … ”

# sentence level graph:
(s374x10 / say
	:ARG1 (s374x6 / 出生-01
		:ARG0 (s374x1 / individual-person
			:refer-person 1
			:refer-number singular)
		:temporal (s374x5 / 同时
			:ARG1 (s374x4 / 太阳))
		:mode judgement
		:modal-strength (s374x18 / full-affirmative)))

# alignment:
s374x1: 0-0
s374x10: 0-0
s374x18: 0-0
s374x4: 4-4
s374x5: 5-5
s374x6: 6-6

# document level annotation:
(s374s0 / sentence)

## chinese_umr-0004, sentence 20

# :: snt20
Index: 1  2 3  4 5  6   7
Words: 同时 ， 他们 还 制伏 格拉斯 。

# sentence level graph:
(s20x / 制伏-00
    :ARG0 (s20p / person
        :refer-number plural
        :refer-person 3rd)
    :ARG1 (s20i2 / individual-person
        :name (s20n / name
            :op1 "格拉斯"))
    :temporal (s20x2 / 同时)
    :mod (s20x3 / 还)
    :aspect performance)


# alignment:
s20i2: 0-0
s20n: 0-0
s20p: 0-0
s20x: 5-5
s20x2: 1-1
s20x3: 4-4

# document level annotation:
(s20s0 / sentence
    :temporal ((s19x :overlap s20x))
    :modal ((root :modal author)
        (author :full-affirmative s20x))
    :coref ((s19i2 :same-entity s20i2)
        (s19e :same-entity s20p)))

## chinese_umr-0001, sentence 39

# :: snt39
Index: 1  2   3  4  5  6   7 8  9   10 11 12
Words: 该文 右下角 特意 同时 刊登 伊拉克 前 总统 萨达姆 的  照片 。 

# sentence level graph:
(s39x / 刊登-01
    :ARG1 (s39x7 / 右下角
        :part (s39x8 / 文
            :mod (s39x9 / 该)))
    :ARG2 (s39x2 / 照片
        :topic (s39i2 / individual-person
            :name (s39n / name
                :op1 "萨达姆")
            :ARG1-of (s39h / have-org-role-91
                :ARG2 (s39c / country
                    :name (s39n2 / name
                        :op1 "伊拉克"))
                :ARG3 (s39x3 / 总统
                    :mod (s39x4 / 前)))))
    :manner (s39x5 / 特意)
    :temporal (s39x6 / 同时)
    :aspect performance)


# alignment:
s39c: 0-0
s39h: 0-0
s39i2: 0-0
s39n: 0-0
s39n2: 0-0
s39x: 5-5
s39x2: 11-11
s39x3: 8-8
s39x4: 7-7
s39x5: 3-3
s39x6: 4-4
s39x7: 2-2
s39x8: 1-1
s39x9: 1-1

# document level annotation:
(s39s0 / sentence
    :temporal ((s37x2 :overlap s39x))
    :modal ((root :modal author)
        (author :full-affirmative s39x))
    :coref ((s38x3 :same-entity s39x8)))

## chinese_umr-0002, sentence 7

# :: snt7
Index: 1  2  3  4 5 6  7 8  9 10 11 12 13 14 15 16 17
Words: 警方 声称 23 人 在 爆炸 中 身亡 ， 另有 包括 儿童 在内 59 人  受伤 。 

# sentence level graph:
(s7x / 声称-01
    :ARG0 (s7x2 / 警方)
    :ARG1 (s7a / and
        :op1 (s7x3 / 身亡-01
            :ARG0 (s7x4 / 人
                :quant 23)
            :reason (s7x5 / 爆炸-01)
            :aspect performance)
        :op3 (s7x6 / 受伤-01
            :ARG0 (s7x7 / 人
                :quant 59
                :ARG0-of (s7x8 / 包括-01
                    :ARG1 (s7x9 / 儿童)
                    :aspect state))
            :aspect performance))
    :aspect performance)


# alignment:
s7a: 0-0
s7x: 2-2
s7x2: 1-1
s7x3: 8-8
s7x4: 4-4
s7x5: 6-6
s7x6: 16-16
s7x7: 4-4
s7x8: 11-11
s7x9: 12-12

# document level annotation:
(s7s0 / sentence
    :temporal ((s7x :before s7x3)
        (s7x3 :before s7x5)
        (s7x :before s7x6)
        (s7x6 :overlap s7x8)
        (s6x7 :after s7x))
    :modal ((root :modal author)
        (author :full-affirmative s7x3)
        (author :full-affirmative s7x8)
        (author :full-affirmative s7x6)
        (author :full-affirmative s7x))
    :coref ((s6x7 :same-event s7x5)
        (s6x3 :same-event s7x3)))

## chinese_umr-0002, sentence 38

# :: snt38
Index: 1  2  3  4 5  6 7  8  9  10 11 12 13 14 15 16 17 18 19
Words: 附近 一家 酒店 向 走失 的 儿童 提供 庇护 ，  警方 将  父母 们  带到 酒店 认领 小孩 。 

# sentence level graph:
(s38a / and
    :op1 (s38x / 提供-02
        :ARG0 (s38x2 / 酒店
            :place (s38x3 / 附近)
            :quant 1
            :unit (s38x4 / 家))
        :ARG2 (s38x5 / 儿童
            :ARG0-of (s38x6 / 走失-00
                :aspect state))
        :ARG3 (s38x12 / 庇护-01
            :ARG0 s38x2
            :ARG1 s38x5
            :aspect performance)
        :aspect performance)
    :op2 (s38x7 / 带到-01
        :ARG0 (s38x13 / 警方)
        :ARG1 (s38x9 / 父母
            :refer-number plural)
        :ARG2 s38x2
        :aspect performance
        :purpose (s38x8 / 认领-00
            :ARG0 s38x9
            :ARG1 (s38x10 / 小孩)
            :aspect performance)))


# alignment:
s38a: 0-0
s38x: 8-8
s38x10: 18-18
s38x12: 9-9
s38x13: 11-11
s38x2: 3-3
s38x3: 1-1
s38x4: 2-2
s38x5: 7-7
s38x6: 5-5
s38x7: 15-15
s38x8: 17-17
s38x9: 13-13

# document level annotation:
(s38s0 / sentence
    :temporal ((s37x :after s38x)
        (s38x :before s38x6)
        (s38x :overlap s38x12)
        (s38x :after s38x7)
        (s38x7 :after s38x8))
    :modal ((root :modal author)
        (author :full-affirmative s38x6)
        (author :full-affirmative s38x12)
        (author :full-affirmative s38x)
        (author :full-affirmative s38x7)
        (author :full-affirmative s38x8))
    :coref ((s37x3 :same-entity s38x5)
        (s37x2 :same-entity s38x9)))

## chinese_umr-0002, sentence 34

# :: snt34
Index: 1   2  3 4 5  6 7 8  9  10 11 12 13 14 15 16 17 18 19 20
Words: 第二天 傍晚 1 点 32 分 ， 警方 在座 堂  花园 发现 可疑 物品 ，  出动 爆炸 控制 小组 。 

# sentence level graph:
(s34c / consecutive
    :op1 (s34x / 发现-01
        :ARG0 (s34x6 / 警方)
        :ARG1 (s34x7 / 物品
            :ARG0-of (s34x8 / 可疑-01
                :aspect state)
            :place (s34p / park
                :name (s34n / name
                    :op1 "座堂"
                    :op2 "花园")))
        :temporal (s34d / date-entity
            :day (s34x9 / 第二天)
            :time (s34h / h13m32))
        :aspect performance)
    :op2 (s34x2 / 出动-01
        :ARG0 s34x6
        :ARG1 (s34x3 / 小组
            :ARG0-of (s34x4 / 控制-01
                :ARG1 (s34x5 / 爆炸-01
                    :aspect process)
                :aspect activity))
        :aspect performance))


# alignment:
s34c: 0-0
s34d: 0-0
s34h: 3-3
s34n: 0-0
s34p: 0-0
s34x: 12-12
s34x2: 16-16
s34x3: 19-19
s34x4: 18-18
s34x5: 17-17
s34x6: 8-8
s34x7: 14-14
s34x8: 13-13
s34x9: 1-1

# document level annotation:
(s34s0 / sentence
    :temporal ((s34d :overlap s34x)
        (document-creation-time :before s34d)
        (s34x :overlap s34x8)
        (s34x :after s34x2)
        (s34x2 :overlap s34x4))
    :modal ((root :modal author)
        (author :neutral-affirmative s34x8)
        (author :full-affirmative s34x)
        (author :full-affirmative s34x5)
        (author :full-affirmative s34x4)
        (author :full-affirmative s34x2)
        (author :full-affirmative s34x8)))

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

## chinese_umr-0025, sentence 36

# :: snt36
Index:    1    2  3  4    5  6      7  8    9 10   11 12 13 14   15   16   17   18   19 20   21   22 23
Words: 当时   由于   我  既  没有   带  机械师    也  没有   带  旅客   ，  我  就  试图   独自   完成   这个   困难   的  维修   工作   。 

# sentence level graph:
(s36x24 / causation
				:ARG1 (s36x26 / and
											:op1 (s36x6 / 带-02
																	:ARG1 (s36x7 / 机械师)
																	:modal-strength (s36x49 / full-negative)
																	:polarity -)
											:op2 (s36x10 / 带-01
																	:ARG1 (s36x11 / 旅客)
																	:modal-strength (s36x50 / full-negative)
																	:polarity -)
											:ARG0 (s36x3 / individual-person
																	:refer-person 1
																	:refer-number singular))
				:ARG2 (s36x15 / 试图-01
											:ARG0 (s36x13 / individual-person
																		:refer-person 1
																		:refer-number singular)
											:ARG1 (s36x17 / 完成-01
																		:manner (s36x16 / 独自
																										:ARG1 (s36x22 / 工作
																																	:mod (s36x19 / 困难)
																																	:mod (s36x21 / 维修)
																																	:mod (s36x18 / 个
																																							/ 这)
																																	:unit s36x18))
																		:ARG0 s36x13
																		:modal-predicate s36x15
																		:modal-strength (s36x47 / neutral-affirmative
																										:conceiver s36x13))))

# alignment:
s36x10: 6-6
s36x11: 11-11
s36x13: 0-0
s36x15: 15-15
s36x16: 16-16
s36x17: 17-17
s36x18: 18-18
s36x19: 19-19
s36x21: 21-21
s36x22: 22-22
s36x24: 0-0
s36x26: 0-0
s36x3: 0-0
s36x47: 0-0
s36x49: 0-0
s36x50: 0-0
s36x6: 6-6
s36x7: 7-7

# document level annotation:
(s36s0 / sentence)

## chinese_umr-0006, sentence 10

# :: snt10
Index: 1  2   3 4 5 6  7  8      9  10 11 12 13  14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37   38 39 40  
Words: 每队 设计师 须 为 由 知名 演员 苏珊·莎朗顿 创办 的  乒乓 社交 俱乐部 设计 5款 工作 制服 ，  当中 包含 男  、  女  侍应 服  和  球童 服  ，  而  本次 挑战 并  会  采用 3名 女模特儿 和  2名 男模特儿

# sentence level graph:
(s10a / and
    :op1 (s10x / 须-01
        :ARG0 (s10x3 / 设计师
            :part (s10x31 / 队
                :mod (s10x32 / 每)))
        :ARG1 (s10x15 / 设计-01
            :ARG0 s10x3
            :ARG1 (s10x16 / 制服
                :ARG0-of (s10x19 / 包含-01
                    :ARG1 (s10a4 / and
                        :op1 (s10x17 / 侍应服
                            :mod (s10x21 / 男))
                        :op2 (s10x20 / 侍应服
                            :mod (s10x29 / 女))
                        :op3 (s10x18 / 球童服))
                    :aspect state)
                :unit (s10x23 / 款)
                :quant 5
                :mod (s10x24 / 工作))
            :affectee (s10x25 / 俱乐部
                :ARG1-of (s10x26 / 创办-01
                    :ARG0 (s10i2 / individual-person
                        :name (s10n / name
                            :op1 "苏珊·莎朗顿")
                        :ARG1-of (s10i3 / identity-91
                            :ARG2 (s10x22 / 演员
                                :mod (s10x30 / 知名))))
                    :aspect performance)
                :topic (s10x27 / 社交
                    :mod (s10x28 / 乒乓)))
            :aspect performance)
        :aspect state)
    :op2 (s10x2 / 采用-01
        :ARG0 (s10x12 / 挑战
            :mod (s10x13 / 本次))
        :ARG1 (s10a3 / and
            :op1 (s10x9 / 模特儿
                :mod (s10x10 / 女)
                :quant 3
                :unit (s10x11 / 名))
            :op2 (s10x6 / 模特儿
                :mod (s10x7 / 男)
                :quant 2
                :unit (s10x8 / 名)))
        :mod (s10x5 / 并)
        :aspect performance))


# alignment:
s10a: 0-0
s10a3: 0-0
s10a4: 0-0
s10i2: 0-0
s10i3: 0-0
s10n: 0-0
s10x: 3-3
s10x10: 23-23
s10x11: 6-6
s10x12: 32-32
s10x13: 31-31
s10x15: 14-14
s10x16: 17-17
s10x17: 24-24
s10x18: 25-25
s10x19: 20-20
s10x2: 35-35
s10x20: 24-24
s10x21: 21-21
s10x22: 7-7
s10x23: 15-15
s10x24: 16-16
s10x25: 13-13
s10x26: 9-9
s10x27: 12-12
s10x28: 11-11
s10x29: 23-23
s10x3: 2-2
s10x30: 6-6
s10x31: 1-1
s10x32: 1-1
s10x5: 33-33
s10x6: 37-37
s10x7: 21-21
s10x8: 6-6
s10x9: 37-37

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10x)
        (s10x :overlap s10x15)
        (s10x15 :overlap s10x19)
        (s10x15 :before s10x26)
        (s10x :overlap s10x2))
    :modal ((root :modal author)
        (author :full-affirmative s10x19)
        (author :full-affirmative s10x26)
        (author :full-affirmative s10x15)
        (author :full-affirmative s10x)
        (author :full-affirmative s10x2))
    :coref ((s9x14 :same-entity s10x3)))

## chinese_umr-0018, sentence 28

# :: snt28
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41
Words: 澳大利亚 籍 的 人道 工作者 家属 要求 调查 事件 是否 涉及 战争 罪行 ， 美加 籍 的 人道 工作者 家属 则 拒绝 接受 以色列 的 道歉 ， 他们 要求 展开 独立 调查 并 要求 美国 停止 为 以色列 提供 武器 。

# sentence level graph:
(s28a / and
	:op1 (s28x / 要求-01
		:ARG0 (s28f / 家属
			:possessor (s28w / 工作者
				:mod (s28h / 人道)
				:mod (s28n6 / nationality
					:name (s28n / name
						:op1 "澳大利亚"))))
		:ARG1 (s28i / 调查-01
			:ARG1 (s28t / truth-value
				:polarity-of (s28x3 / 涉及-01
					:ARG0 (s28x4 / 事件)
					:ARG1 (s28x6 / 罪行
						:mod (s28x7 / 战争))
					:aspect state))
			:aspect performance)
		:aspect performance)
	:op2 (s28a5 / and
		:op1 (s28x5 / 拒绝-01
			:ARG0 (s28x10 / 家属
				:possessor (s28x11 / 工作者
					:mod (s28x12 / 人道)
					:mod (s28a3 / and
						:op1 (s28n3 / nationality
							:name (s28n7 / name
								:op1 "美国"))
						:op2 (s28n8 / nationality
							:name (s28n9 / name
								:op1 "加拿大")))))
			:ARG1 (s28x8 / 接受-01
				:ARG0 s28x10
				:ARG1 (s28x9 / 道歉-01
					:ARG0 (s28c / country
						:name (s28n2 / name
							:op1 "以色列"))
					:aspect performance)
				:aspect performance)
			:aspect performance)
		:op2 (s28a2 / and
			:op1 (s28x19 / 要求-02
				:ARG0 s28x10
				:ARG2 (s28x16 / 展开-01
					:ARG1 (s28x17 / 调查-01
						:mod (s28x18 / 独立)
						:aspect activity)
					:aspect activity)
				:aspect performance)
			:op2 (s28x2 / 要求-02
				:ARG0 s28x10
				:ARG1 (s28c2 / country
					:name (s28n5 / name
						:op1 "美国"))
				:ARG2 (s28x13 / 停止-01
					:ARG0 s28c2
					:ARG1 (s28x14 / 提供-01
						:ARG0 s28c2
						:ARG1 (s28x15 / 武器)
						:ARG2 (s28c3 / country
							:name (s28n4 / name
								:op1 "以色列"))
						:aspect habitual)
					:aspect performance)
				:aspect performance))))

# alignment:
s28a: 0-0
s28a2: 0-0
s28a3: 0-0
s28a5: 0-0
s28c: 0-0
s28c2: 0-0
s28c3: 0-0
s28f: 6-6
s28h: 4-4
s28i: 8-8
s28n: 0-0
s28n2: 0-0
s28n3: 0-0
s28n4: 0-0
s28n5: 0-0
s28n6: 0-0
s28n7: 0-0
s28n8: 0-0
s28n9: 0-0
s28t: 0-0
s28w: 5-5
s28x: 7-7
s28x10: 6-6
s28x11: 5-5
s28x12: 4-4
s28x13: 36-36
s28x14: 39-39
s28x15: 40-40
s28x16: 30-30
s28x17: 8-8
s28x18: 31-31
s28x19: 7-7
s28x2: 7-7
s28x3: 11-11
s28x4: 9-9
s28x5: 22-22
s28x6: 13-13
s28x7: 12-12
s28x8: 23-23
s28x9: 26-26

# document level annotation:
(s28s0 / sentence
    :temporal ((document-creation-time :before s28x)
            (s28x :before s28x3)
            (document-creation-time :before s28x5)
            (s28x5 :overlap s28x8)
            (s28x8 :before s28x9)
            (s28x :after s28i)
            (s28x19 :after s28x16)
            (s28x16 :overlap s28x17)
            (s28x19 :overlap s28x2)
            (s28x5 :overlap s28x19)
            (s28x2 :after s28x13)
            (s28x13 :overlap s28x14))
    :modal ((root :modal author)
            (author :full-affirmative s28x3)
            (author :full-affirmative s28i)
            (author :full-affirmative s28x)
            (author :full-affirmative s28x9)
            (author :full-affirmative s28x8)
            (author :full-affirmative s28x5)
            (author :full-affirmative s28x16)
            (author :full-affirmative s28x19)
            (author :full-affirmative s28x14)
            (author :full-affirmative s28x13)
            (author :full-affirmative s28x2))
    :coref ()
)

## chinese_umr-0025, sentence 336

# :: snt336
Index:  1    2  3  4    5  6  7
Words: 他  无法   再  说  下去   了  ， 

# sentence level graph:
(s336x2 / 无法-01
	:ARG0 (s336x4 / 说-01
		:ARG0 (s336x1 / individual-person
			:refer-person 3
			:refer-number singular)
		:mod (s336x3 / 再)
		:modal-strength (s336x15 / full-negative))
	:aspect performance)

# alignment:
s336x1: 0-0
s336x15: 0-0
s336x2: 2-2
s336x3: 3-3
s336x4: 4-4

# document level annotation:
(s336s0 / sentence)

## chinese_umr-0019, sentence 3

# :: snt3
Index:    1    2    3  4    5    6  7    8    9 10 11   12   13   14 15 16
Words: 随着   积雪   带来   的  南方   寒潮   ，  广东   广州   等  地  迎来   今年   最低   温  。 

# sentence level graph:
(s3x / 迎来-01
	:ARG0 (s3a / and
		:op1 (s3c / city
			:name (s3n / name
				:op1 "广州")
			:part-of (s3p / province
				:name (s3n2 / name
					:op1 "广东")))
		:op2 (s3x2 / 等)
		:op3 (s3x3 / 地))
	:ARG1 (s3x6 / 温
		:ARG1-of (s3h / have-degree-91
			:ARG2 (s3x7 / 低)
			:ARG3 (s3x8 / 最)))
	:temporal (s3x9 / 今年)
	:reason (s3x10 / 寒潮
		:cause-of (s3x12 / 积雪)
		:place (s3x4 / 南方))
	:aspect performance)

# alignment:
s3a: 0-0
s3c: 0-0
s3h: 0-0
s3n: 0-0
s3n2: 0-0
s3p: 0-0
s3x: 12-12
s3x10: 6-6
s3x12: 2-2
s3x2: 10-10
s3x3: 11-11
s3x4: 5-5
s3x6: 15-15
s3x7: 14-14
s3x8: 14-14
s3x9: 13-13

# document level annotation:
(s3s0 / sentence
	:temporal ((document-creation-time :before s3x)))
	:modal ((root :modal author)
		(author :full-affirmative s3x)
		(root :modal author))

## chinese_umr-0006, sentence 17

# :: snt17
Index: 1 2  3     4 5 6  7   8 9  10 11 12    13 14 15 16 17 18      
Words: 而 同样 保持真我队 并 可 选择 梦之队 的 一名 队员 加入 保持真我队 ，  结果 他们 选择 了  Michelle

# sentence level graph:
(s17c / consecutive
    :op1 (s17x4 / 选择-01
        :ARG0 (s17o / organization
            :name (s17n2 / name
                :op1 "保持真我队"))
        :ARG1 (s17x5 / 队员
            :unit (s17x6 / 名)
            :quant 1
            :part (s17o2 / organization
                :name (s17n3 / name
                    :op1 "梦之队"))
            :ARG0-of (s17x3 / 加入-01
                :ARG1 s17o))
        :aspect performance
        :mod (s17x7 / 同样))
    :ARG2 (s17x / 选择-01
        :ARG0 s17o
        :ARG1 (s17i2 / individaul-person
            :name (s17n / name
                :op1 "Michelle"))
        :aspect performance
        :mod (s17x2 / 结果)))


# alignment:
s17c: 0-0
s17i2: 0-0
s17n: 0-0
s17n2: 0-0
s17n3: 0-0
s17o: 0-0
s17o2: 0-0
s17x: 6-6
s17x2: 14-14
s17x3: 11-11
s17x4: 6-6
s17x5: 10-10
s17x6: 9-9
s17x7: 2-2

# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17x4)
        (s17x4 :overlap s17x3)
        (s17x4 :overlap s17x))
    :modal ((root :modal author)
        (author :neutral-affirmative s17x4)
        (author :full-affirmative s17x))
    :coref ((s16o3 :same-entity s17o)
        (s16o2 :same-entity s17o2)))

## chinese_umr-0002, sentence 5

# :: snt5
Index: 1 2    3  4  5  6 7  8  9 10 11 12 13 14 15
Words: 大 曼彻斯特 警察 宣布 事件 为 恐怖 袭击 ， 认定 其  为  自杀 攻击 。 

# sentence level graph:
(s5a / and
    :op1 (s5x / 宣布-01
        :ARG0 (s5x3 / 警察
            :place (s5l / local-region
                :name (s5n / name
                    :op1 "大"
                    :op2 "曼彻斯特")))
        :ARG1 (s5x4 / 事件)
        :ARG2 (s5x5 / 袭击
            :mod (s5x6 / 恐怖))
        :aspect performance)
    :op2 (s5x2 / 认定-02
        :ARG0 s5x3
        :ARG1 s5x4
        :ARG2 (s5x7 / 攻击-01
            :manner (s5x8 / 自杀-01
                :aspect performance)
            :aspect performance)
        :aspect performance))


# alignment:
s5a: 0-0
s5l: 0-0
s5n: 0-0
s5x: 4-4
s5x2: 10-10
s5x3: 3-3
s5x4: 5-5
s5x5: 8-8
s5x6: 7-7
s5x7: 14-14
s5x8: 13-13

# document level annotation:
(s5s0 / sentence
    :temporal ((s4x10 :after s5x)
        (s5x :overlap s5x2)
        (s5x2 :before s5x7)
        (s5x7 :overlap s5x8))
    :modal ((root :modal author)
        (author :full-affirmative s5x)
        (author :full-affirmative s5x8)
        (author :full-affirmative s5x7)
        (author :full-affirmative s5x2))
    :coref ((s4x10 :same-event s5x4)
        (s4x10 :same-event s5x7)))

## chinese_umr-0024, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
Words: 自 2020 年 10 月 以来 ， 和 他 的 企业 帝国 一直 承受 着 来自 政府 的 巨大 压力 ， 他 在 演讲 中 攻击 中国 的 金融 监管 机构 ， 并 批评 金融 体系 已经 过时 。

# sentence level graph:
(s10a / and
	:op1 (s10x / 承受-01
		:ARG0 (s10x2 / 帝国
			:mod (s10x3 / 企业)
			:possessor (s10p2 / person
				:refer-person 3rd
				:refer-number singular))
		:ARG1 (s10x4 / 压力
			:mod (s10x5 / 巨大)
			:source (s10x6 / 政府))
		:temporal (s10d / date-interval
			:op1 (s10d2 / date-entity
				:year 2020
				:month 10)
			:op2 (s10d3 / now))
		:mod (s10x17 / 一直)
		:aspect activity)
	:op2 (s10a2 / and
		:op1 (s10x7 / 攻击-01
			:ARG0 s10p2
			:ARG1 (s10x8 / 机构
				:mod (s10x9 / 监管)
				:mod (s10x10 / 金融)
				:possessor (s10c / country
					:name (s10n / name
						:op1 "中国")))
			:place (s10x11 / 中
				:op1 (s10x12 / 演讲))
			:aspect performance)
		:op2 (s10x13 / 批评-01
			:ARG0 s10p2
			:ARG1 (s10x16 / 过时-01
				:ARG0 (s10x14 / 体系
					:mod (s10x15 / 金融))
				:mod (s10x18 / 已经)
				:aspect state)
			:aspect performance)))

# alignment:
s10a: 0-0
s10a2: 0-0
s10c: 0-0
s10d: 0-0
s10d2: 0-0
s10d3: 0-0
s10n: 0-0
s10p2: 0-0
s10x: 14-14
s10x10: 29-29
s10x11: 25-25
s10x12: 24-24
s10x13: 34-34
s10x14: 36-36
s10x15: 29-29
s10x16: 38-38
s10x2: 12-12
s10x3: 11-11
s10x4: 20-20
s10x5: 19-19
s10x6: 17-17
s10x7: 26-26
s10x8: 31-31
s10x9: 30-30

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :overlap s10x)
            (s10x :contained s10x7)
            (s10x :contained s10x13))
    :modal ((root :modal author)
            (author :full-affirmative s10x)
            (author :full-affirmative s10x7)
            (author :full-affirmative s10x13)
            (author :full-affirmative s10p2)
            (s10p2 :full-affirmative s10x16))
    :coref ()
)

## chinese_umr-0003, sentence 17

# :: snt17
Index: 1   2  3  4 5  6 7 8   9 10 11 12 13 14 15 16 17 18 19 20 21   22 23 24 25 26 27 28 29 30 31  32 33 34 35 36 37 38 39 40 41 42 43 44  45 46 47 48 49 50 51 52 53 54 55 56 57 58 59  60 61 62 63
Words: 有见于 来自 中国 和 台湾 而 操 普通话 的 移民 逐渐 增加 ，  城市 电视 再度 进行 改革 ，  于  1998 年  6  月  1  日  转型 为  一个 全  普通话 频道 ，  对象 由  讲  粤语 的  香港 移民 转移 为  讲  普通话 的  中国 移民 和  台湾 移民 ，  并  改为 播放 中国 大陆 和  台湾 电视台 制作 的  节目 。 

# sentence level graph:
(s17h / have-reason-91
    :ARG1 (s17a / and
        :op1 (s17x6 / 改革-01
            :ARG1 (s17c3 / company
                :name (s17n4 / name
                    :op1 "城市"
                    :op2 "电视"))
            :mod (s17x10 / 再度)
            :aspect performance)
        :op2 (s17x7 / 转型-01
            :ARG0 s17c3
            :temporal (s17d / date-entity
                :year 1998
                :month 6
                :day 1)
            :end-state (s17x11 / 频道
                :quant 1
                :unit (s17x12 / 个)
                :mod (s17x13 / 全)
                :medium (s17l2 / language
                    :name (s17n5 / name
                        :op1 "普通话")))
            :aspect performance)
        :op3 (s17x8 / 转移-01
            :ARG1 (s17x14 / 对象)
            :ARG2 (s17x15 / 移民
                :mod (s17c4 / country-region
                    :name (s17n6 / name
                        :op1 "香港"))
                :ARG0-of (s17x16 / 讲-01
                    :ARG1 (s17l3 / language
                        :name (s17n7 / name
                            :op1 "粤语"))
                    :aspect state))
            :ARG3 (s17a4 / and
                :op1 (s17x17 / 移民
                    :mod (s17c5 / country
                        :name (s17n8 / name
                            :op1 "中国")))
                :op2 (s17x18 / 移民
                    :mod (s17c6 / country-region
                        :name (s17n9 / name
                            :op1 "台湾")))
                :ARG0-of (s17x19 / 讲-01
                    :ARG1 (s17l4 / language
                        :name (s17n10 / name
                            :op1 "普通话"))
                    :aspect state))
            :aspect performance)
        :op4 (s17x9 / 改为-01
            :ARG2 (s17x20 / 播放-01
                :ARG1 (s17x21 / 节目
                    :ARG1-of (s17x22 / 制作-01
                        :ARG0 (s17a5 / and
                            :op1 (s17x23 / 电视台
                                :place (s17c7 / country-region
                                    :name (s17n11 / name
                                        :op1 "中国"
                                        :op2 "大陆")))
                            :op2 (s17x24 / 电视台
                                :place (s17c8 / country-region
                                    :name (s17n12 / name
                                        :op1 "台湾"))))
                        :aspect performance))
                :aspect habitual)
            :aspect performance))
    :ARG2 (s17x / 增加-01
        :ARG1 (s17x3 / 移民
            :ARG0-of (s17a2 / and)
            :ARG0-of (s17x5 / 操-01
                :ARG1 (s17l / language
                    :name (s17n / name
                        :op1 "普通话"))
                :reason (s17x4 / 来自-01
                    :ARG0 s17x3
                    :ARG1 (s17a3 / and
                        :op1 (s17c / country
                            :name (s17n2 / name
                                :op1 "中国"))
                        :op2 (s17c2 / country-region
                            :name (s17n3 / name
                                :op1 "台湾")))
                    :aspect state)
                :aspect state))
        :manner (s17x2 / 逐渐)
        :aspect state))


# alignment:
s17a: 0-0
s17a2: 0-0
s17a3: 0-0
s17a4: 0-0
s17a5: 0-0
s17c: 0-0
s17c2: 0-0
s17c3: 0-0
s17c4: 0-0
s17c5: 0-0
s17c6: 0-0
s17c7: 0-0
s17c8: 0-0
s17d: 0-0
s17h: 0-0
s17l: 0-0
s17l2: 0-0
s17l3: 0-0
s17l4: 0-0
s17n: 0-0
s17n10: 0-0
s17n11: 0-0
s17n12: 0-0
s17n2: 0-0
s17n3: 0-0
s17n4: 0-0
s17n5: 0-0
s17n6: 0-0
s17n7: 0-0
s17n8: 0-0
s17n9: 0-0
s17x: 12-12
s17x10: 16-16
s17x11: 32-32
s17x12: 29-29
s17x13: 30-30
s17x14: 34-34
s17x15: 10-10
s17x16: 36-36
s17x17: 10-10
s17x18: 10-10
s17x19: 36-36
s17x2: 11-11
s17x20: 54-54
s17x21: 62-62
s17x22: 60-60
s17x23: 59-59
s17x24: 59-59
s17x3: 10-10
s17x4: 2-2
s17x5: 7-7
s17x6: 18-18
s17x7: 27-27
s17x8: 41-41
s17x9: 53-53

# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17d)
        (s17x6 :overlap s17x7)
        (s17x7 :overlap s17d)
        (s17x7 :overlap s17x8)
        (s17x8 :overlap s17x16)
        (s17x8 :overlap s17x19)
        (s17x8 :overlap s17x9)
        (s17x9 :overlap s17x20)
        (s17x20 :before s17x22)
        (s17x9 :before s17x)
        (s17x :overlap s17x5)
        (s17x :overlap s17x4))
    :modal ((root :modal author)
        (author :full-affirmative s17c3)
        (s17c3 :full-affirmative s17x9)
        (s17x9 :unspecified s17x20)
        (author :full-affirmative s17c3))
    :coref ((s16c2 :same-entity s17c3)))

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

## chinese_umr-0025, sentence 1183

# :: snt1183
Index:    1  2  3    4    5  6  7  8  9   10   11 12   13 14   15   16 17
Words: 由于   渴  我  有点   发烧   ，  我  看  着  这些   星星   ，  象是   在  做梦   一样   。 

# sentence level graph:
(s1183x18 / and
	:op1 (s1183x20 / causation
		:ARG1 (s1183x2 / 渴-01
			:ARG0 (s1183x3 / individual-person
				:refer-person 1
				:refer-number singular))
		:ARG2 (s1183x5 / 发烧-01
			:ARG0 s1183x3
			:degree (s1183x4 / 有点)))
	:op2 (s1183x13 / 像-01
		:ARG0 (s1183x8 / 看-01
			:ARG0 (s1183x7 / individual-person
				:refer-person 1
				:refer-number singular)
			:aspect activity
			:ARG1 (s1183x11 / 星星
				:mod (s1183x10 / 这些)))
		:ARG1 (s1183x15 / 做梦-01
			:aspect activity
			:ARG0 s1183x7)))

# alignment:
s1183x10: 10-10
s1183x11: 11-11
s1183x13: 0-0
s1183x15: 15-15
s1183x18: 0-0
s1183x2: 2-2
s1183x20: 0-0
s1183x3: 0-0
s1183x4: 4-4
s1183x5: 5-5
s1183x7: 0-0
s1183x8: 8-8

# document level annotation:
(s1183s0 / sentence)

## chinese_umr-0013, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57
Words: 视频 发布 后 遭 大批 网友 批评 其 “ 收礼 收到 手软 ” 、“ 都 是 民脂民膏 ” 等 ， 随后 傅崐萁 将 视频 移除 ， 并 于 6 日 接受 媒体 访问 时 表示 “ 自古 以来 大灾 大难 ， 我们 要 惜福 ， 才能 息灾 ， 造 任何 口业 ， 都 会 祸延 子孙 。”

# sentence level graph:
(s10c / consecutive
	:op1 (s10x / 批评-01
		:ARG0 (s10x2 / 网友)
		:ARG1 (s10i / individual-person
			:name (s10n / name
				:op1 "傅崐萁"))
		:ARG2 (s10a2 / and
			:op1 (s10x9 / 收礼-01
				:ARG0 s10i
				:ARG1 (s10x29 / 礼)
				:result (s10x17 / 手软-01
					:aspect state)
				:aspect performance)
			:op2 (s10i3 / identity-91
				:ARG1 s10x29
				:ARG2 (s10x27 / 民脂民膏)
				:mod (s10x26 / 都)
				:aspect state))
		:aspect performance
		:temporal (s10x6 / 后
			:op1 (s10x7 / 发布-01
				:ARG1 (s10x8 / 视频)
				:aspect performance)))
	:op2 (s10x4 / 移除-01
		:ARG0 s10i
		:ARG1 s10x8
		:aspect performance)
	:op3 (s10x5 / 表示-01
		:ARG0 s10i
		:ARG1 (s10a / and
			:op1 (s10x14 / 大灾-大难
				:temporal (s10x15 / 以来
					:op1 (s10x16 / 自古)))
			:op2 (s10h / have-condition-91
				:ARG1 (s10x19 / 息灾-00
					:actor (s10p / person
						:name (s10n3 / name
							:op1 "我们")
						:refer-number plural
						:refer-person 1st)
					:aspect performance
					:modal-strength neutral-affirmative)
				:ARG2 (s10x18 / 惜福-00
					:actor s10p
					:aspect activity
					:modal-strength partial-affirmative))
			:op3 (s10h2 / have-cause-91
				:ARG1 (s10x22 / 祸延-00
					:undergoer (s10x23 / 子孙)
					:mod (s10x25 / 都)
					:aspect process
					:modal-strength full-affirmative)
				:ARG2 (s10x20 / 造-01
					:ARG0 s10p
					:ARG1 (s10x21 / 口业
						:mod (s10x24 / 任何))
					:aspect process))
			:quote s10x5)
		:aspect performance
		:temporal (s10d / date-entity
			:day 6)
		:temporal (s10x10 / 时
			:op1 (s10x11 / 接受-01
				:ARG0 s10i
				:ARG1 (s10x12 / 访问-01
					:ARG0 (s10x13 / 媒体)
					:ARG1 s10i
					:aspect activity)
				:aspect activity))))

# alignment:
s10a: 0-0
s10a2: 0-0
s10c: 0-0
s10d: 0-0
s10h: 0-0
s10h2: 0-0
s10i: 0-0
s10i2: 0-0
s10i3: 0-0
s10n: 0-0
s10n2: 0-0
s10n3: 0-0
s10p: 0-0
s10x: 7-7
s10x10: 34-34
s10x11: 31-31
s10x12: 33-33
s10x13: 32-32
s10x14: 39-39
s10x15: 38-38
s10x16: 37-37
s10x17: 12-12
s10x18: 44-44
s10x19: 47-47
s10x2: 6-6
s10x20: 49-49
s10x21: 51-51
s10x22: 55-55
s10x23: 56-56
s10x24: 50-50
s10x25: 15-15
s10x26: 15-15
s10x27: 17-17
s10x28: 11-11
s10x3: 1-1
s10x4: 25-25
s10x5: 35-35
s10x6: 3-3
s10x7: 2-2
s10x8: 1-1
s10x9: 10-10

# document level annotation:
(s10s0 / sentence
    :temporal ((s10x :after s10x4)
            (s10x11 :after s10x5)
            (s10x7 :after s10x)
            (document-creation-time :before s10x)
            (s10x :before s10x9)
            (s10x4 :after s10x12)
            (s10x12 :overlap s10x5)
            (s10x5 :after s10x18)
            (s10x20 :after s10x22)
            (s10x18 :after s10x19))
    :modal ((root :modal author)
            (author :full-affirmative s10x9)
            (author :full-affirmative s10x)
            (author :full-affirmative s10x7)
            (author :full-affirmative s10x4)
            (author :full-affirmative s10x5)
            (author :neutral-affirmative s10x12)
            (author :full-affirmative s10x11)
            (root :modal author)
            (author :full-affirmative s10i)
            (s10i :full-affirmative s10x14)
            (s10i :neutral-affirmative s10h)
            (s10h :full-affirmative s10x18)
            (s10h :neutral-affirmative s10x19)
            (s10i :neutral-affirmative s10x20)
            (s10i :full-affirmative s10x22))
    :coref ()
)

## chinese_umr-0002, sentence 30

# :: snt30
Index: 1  2  3  4 5  6  7 8 9   10 11 12 13 14 15 16 17 18   19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45  46 47 48 49
Words: 内政 大臣 安珀 · 路德 表示 她 对 阿贝迪 的  名字 和  其他 交给 美国 和  法国 情报部门 的  绝密 信息 在  案发 数  小时 内在 新闻 媒体 中  泄露 表示 愤怒 ，  这  妨碍 了  调查 工作 ，  调查 人员 需要 避免 引起 袭击者 共犯 的  警觉 。 

# sentence level graph:
(s30x / 表示-01
    :ARG0 (s30i2 / individual-person
        :name (s30n / name
            :op1 "安珀"
            :op2 "·"
            :op3 "路德")
        :ARG1-of (s30h / have-org-role-91
            :ARG3 (s30x2 / 大臣
                :mod (s30x3 / 内政))))
    :ARG1 (s30a / and
        :op1 (s30x4 / 表示-01
            :ARG0 s30i2
            :ARG1 (s30x5 / 愤怒-01
                :ARG0 s30i2
                :aspect state
                :quote s30x)
            :ARG3 (s30x6 / 泄露-01
                :ARG0 (s30x7 / 媒体
                    :mod (s30x8 / 新闻))
                :ARG1 (s30a2 / and
                    :op1 (s30x9 / 名字
                        :possessor (s30i3 / individual-person
                            :name (s30n2 / name
                                :op1 "阿贝迪")))
                    :op2 (s30x10 / 信息
                        :mod (s30x11 / 绝密)
                        :subtraction s30x9)
                    :ARG1-of (s30x12 / 交给-01
                        :ARG2 (s30a3 / and
                            :op1 (s30x13 / 部门
                                :mod (s30x14 / 情报)
                                :place (s30c / country
                                    :name (s30n3 / name
                                        :op1 "美国")))
                            :op2 (s30x15 / 部门
                                :mod (s30x16 / 情报)
                                :place (s30c2 / country
                                    :name (s30n4 / name
                                        :op1 "法国"))))
                        :aspect performance
                        :quote s30x))
                :ARG0-of (s30x17 / 妨碍-01
                    :ARG1 (s30x18 / 工作
                        :mod (s30x19 / 调查-01
                            :aspect activity))
                    :aspect performance
                    :quote s30x)
                :aspect performance
                :quote s30x
                :temporal (s30x29 / 内
                    :op1 (s30t / temporal-quantity
                        :quant (s30x30 / 数)
                        :unit (s30x31 / 小时)
                        :temporal (s30i4 / implicit-argument
                            :op1 (s30x32 / 案发-01
                                :aspect performance)))))
            :quote s30x
            :aspect performance)
        :op2 (s30x20 / 需要-02
            :ARG1 (s30x21 / 人员
                :ARG0-of (s30x22 / 调查-01
                    :aspect activity
                    :quote s30x))
            :ARG2 (s30x23 / 避免-01
                :ARG0 s30x21
                :ARG1 (s30x24 / 引起-01
                    :ARG1 (s30x25 / 警觉-01
                        :ARG0 (s30x26 / 共犯
                            :ARG3-of (s30h2 / have-rel-role-91
                                :ARG2 (s30x27 / 者
                                    :ARG0-of (s30x28 / 袭击-01
                                        :aspect performance))))
                        :aspect state
                        :quote s30x)
                    :aspect performance
                    :quote s30x)
                :quote s30x
                :aspect performance)
            :aspect state
            :quote s30x))
    :aspect performance)


# alignment:
s30a: 0-0
s30a2: 0-0
s30a3: 0-0
s30c: 0-0
s30c2: 0-0
s30h: 0-0
s30h2: 0-0
s30i2: 0-0
s30i3: 0-0
s30i4: 0-0
s30n: 0-0
s30n2: 0-0
s30n3: 0-0
s30n4: 0-0
s30t: 0-0
s30x: 6-6
s30x10: 21-21
s30x11: 20-20
s30x12: 14-14
s30x13: 18-18
s30x14: 18-18
s30x15: 18-18
s30x16: 18-18
s30x17: 35-35
s30x18: 38-38
s30x19: 37-37
s30x2: 2-2
s30x20: 42-42
s30x21: 41-41
s30x22: 37-37
s30x23: 43-43
s30x24: 44-44
s30x25: 48-48
s30x26: 46-46
s30x27: 45-45
s30x28: 45-45
s30x29: 1-1
s30x3: 1-1
s30x30: 24-24
s30x31: 25-25
s30x32: 23-23
s30x4: 6-6
s30x5: 32-32
s30x6: 30-30
s30x7: 28-28
s30x8: 27-27
s30x9: 11-11

# document level annotation:
(s30s0 / sentence
    :temporal ((document-creation-time :before s30x)
        (s30x :overlap s30x4)
        (s30x4 :overlap s30x5)
        (s30x5 :before s30x6)
        (s30x6 :before s30x12)
        (s30x6 :after s30x17)
        (s30x6 :before s30x32)
        (s30x :overlap s30x20)
        (s30x20 :overlap s30x22)
        (s30x20 :overlap s30x23)
        (s30x23 :overlap s30x24)
        (s30x24 :overlap s30x25)
        (s30x25 :before s30x28))
    :modal ((root :modal author)
        (s30i2 :full-affirmative s30x5)
        (author :full-affirmative s30x12)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x19)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x17)
        (author :full-affirmative s30i2)
        (s30i2 :full-affirmative s30x6)
        (author :full-affirmative s30x32)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x4)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x22)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x28)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x25)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x24)
        (author :full-affirmative s30i2)
        (s30i2 :full-affirmative s30x23)
        (author :full-affirmative s30x20)
        (author :full-affirmative s30i2)
        (author :full-affirmative s30x)
        (author :full-affirmative s30i2))
    :coref ((s28x7 :same-entity s30x27)
        (s28x7 :same-entity s30i3)))

## chinese_umr-0002, sentence 33

# :: snt33
Index: 1   2  3 4 5 6  7  8 9  10 11 12 13 14 15   16  17 18 19 20 21 22 23 24 25 26 27 28 29  30 31 32 33 34 35 36 37  38  39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
Words: BBC 报道 称 ： “ 英国 政府 和 警察 在  美国 报纸 明显 展示 曼彻斯特 爆炸案 现场 的  照片 后  表示 愤怒 。  反恐 警察 主任 表示 泄露 无形中 摧毁 了  他们 的  调查 行动 及  受害者 目击者 的  自信 。  白厅 消息 人士 补充 道  ：  ‘  我们 深感 愤怒 ，  这种 行为 绝对 不能 接受 。  ’ 

# sentence level graph:
(s33x / 称-02
    :ARG0 (s33x2 / 报道-01
        :ARG0 (s33c / company
            :name (s33n / name
                :op1 "BBC"))
        :aspect performance)
    :ARG1 (s33a / and
        :op1 (s33x3 / 表示-01
            :ARG0 (s33a2 / and
                :op1 (s33x4 / 政府
                    :place (s33c2 / country
                        :name (s33n2 / name
                            :op1 "英国")))
                :op2 (s33x5 / 警察
                    :place s33c2))
            :ARG1 (s33x6 / 愤怒-01
                :ARG0 s33a2
                :aspect state
                :quote s33x2)
            :temporal (s33x7 / 后
                :op1 (s33x8 / 展示-01
                    :ARG0 (s33x10 / 报纸
                        :place (s33c3 / country
                            :name (s33n3 / name
                                :op1 "美国")))
                    :ARG1 (s33x9 / 照片
                        :topic (s33x11 / 爆炸案
                            :place (s33c4 / city
                                :name (s33n4 / name
                                    :op1 "曼彻斯特")))
                        :mod (s33x12 / 现场))
                    :manner (s33x13 / 明显)
                    :aspect performance
                    :quote s33x2))
            :aspect performance
            :quote s33x2)
        :op2 (s33x14 / 表示-01
            :ARG0 (s33x16 / 主任
                :mod (s33x17 / 警察
                    :ARG0-of (s33x18 / 反-01
                        :ARG1 (s33x19 / 恐))))
            :ARG1 (s33x20 / 摧毁-01
                :ARG0 (s33x21 / 泄露-02
                    :aspect performance)
                :ARG1 (s33a3 / and
                    :op1 (s33x23 / 行动-01
                        :ARG1 (s33x24 / 调查-01
                            :ARG0 s33x17
                            :aspect activity)
                        :aspect activity)
                    :op2 (s33x25 / 自信-01
                        :ARG0 (s33x27 / 者
                            :ARG0-of (s33x28 / 受害-01
                                :aspect performance)))
                    :op3 (s33x26 / 自信-01
                        :ARG0 (s33x29 / 者
                            :ARG0-of (s33x30 / 目击-01
                                :aspect performance))))
                :mod (s33x22 / 无形中)
                :quote s33x2)
            :aspect performance
            :quote s33x2)
        :op3 (s33x15 / 道-01
            :ARG0 (s33x31 / 人士
                :mod (s33x32 / 消息)
                :place (s33g / government-organization
                    :name (s33n5 / name
                        :op1 "白厅")))
            :ARG1 (s33a4 / and
                :op1 (s33x34 / 愤怒-01
                    :ARG0 (s33p / person
                        :refer-person 1st
                        :refer-number plural)
                    :degree intensifier
                    :aspect state
                    :quote s33x15)
                :ARG0 (s33x36 / 接受-01
                    :ARG1 (s33x37 / 行为
                        :mod (s33x38 / 这种))
                    :mod (s33x39 / 绝对)
                    :aspect performance))
            :mod (s33x33 / 补充-01)
            :aspect performance
            :quote s33x2))
    :aspect performance)


# alignment:
s33a: 0-0
s33a2: 0-0
s33a3: 0-0
s33a4: 0-0
s33c: 0-0
s33c2: 0-0
s33c3: 0-0
s33c4: 0-0
s33g: 0-0
s33n: 0-0
s33n2: 0-0
s33n3: 0-0
s33n4: 0-0
s33n5: 0-0
s33p: 0-0
s33x: 3-3
s33x10: 12-12
s33x11: 16-16
s33x12: 17-17
s33x13: 13-13
s33x14: 21-21
s33x15: 46-46
s33x16: 26-26
s33x17: 9-9
s33x18: 24-24
s33x19: 24-24
s33x2: 2-2
s33x20: 30-30
s33x21: 28-28
s33x22: 29-29
s33x23: 35-35
s33x24: 34-34
s33x25: 40-40
s33x26: 40-40
s33x27: 37-37
s33x28: 37-37
s33x29: 37-37
s33x3: 21-21
s33x30: 38-38
s33x31: 44-44
s33x32: 43-43
s33x33: 45-45
s33x34: 22-22
s33x36: 57-57
s33x37: 54-54
s33x38: 53-53
s33x39: 55-55
s33x4: 7-7
s33x5: 9-9
s33x6: 22-22
s33x7: 20-20
s33x8: 14-14
s33x9: 19-19

# document level annotation:
(s33s0 / sentence
    :temporal ((document-creation-time :before s33x)
        (s33x :overlap s33x2)
        (s33x :overlap s33x3)
        (s33x3 :overlap s33x6)
        (s33x6 :before s33x8)
        (s33x :before s33x14)
        (s33x14 :before s33x20)
        (s33x20 :before s33x21)
        (s33x20 :overlap s33x23)
        (s33x23 :overlap s33x24)
        (s33x20 :before s33x28)
        (s33x20 :before s33x30))
    :modal ((root :modal author)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x2)
        (s33x2 :full-affirmative s33x6)
        (author :full-affirmative s33x8)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x3)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x21)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x24)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x23)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x28)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x30)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x14)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x34)
        (author :full-affirmative s33x2)
        (author :neutral-negative s33x36)
        (author :neutral-negative s33x2)
        (author :full-affirmative s33x15)
        (author :full-affirmative s33x2)
        (author :full-affirmative s33x)
        (author :full-affirmative s33x2))
    :coref ((s26x4 :same-event s33x8)
        (s25x9 :same-event s33x11)
        (s26x2 :same-entity s33x9)
 
… (34 more characters)

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

## chinese_umr-0021, sentence 11

# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89
Words: 除了 狭窄 的 全食 带 内 能 看见 日全食 之外 ， 月球 半影 覆盖 范围 内 都 能 看到 日偏食 ， 包括 波利尼西亚 中东部 ， 北美洲 除 阿拉斯加 大部 、 加拿大 与 阿拉斯加 交界 地区 、 多米尼克 中南部 、 向风群岛 以外 的 绝大部分 （ 背风安 的 列斯群岛 中 仅 阿鲁巴 能 看到 日偏食 ） ， 科隆群岛 、 哥伦比亚 的 加勒比海 沿岸 地区 、 委内瑞拉 西北角 ， 冰岛 、 扬马延岛 、 斯瓦尔巴群岛 、 法罗群岛 、 爱尔兰 、 英国 西北部 、 伊比利亚半岛 西北角 、 亚速尔群岛 、 马德拉群岛 、 加那利群岛 中西部 。

# sentence level graph:
(s11s / and
	:op1 (s11x / 看见-01
		:ARG1 (s11x4 / 日全食)
		:place (s11x2 / 全食带
			:mod (s11x3 / 狭窄))
		:aspect activity)
	:op2 (s11x5 / 看到-01
		:ARG1 (s11x9 / 日偏食)
		:place (s11x6 / 范围
			:ARG1-of (s11x7 / 覆盖-01
				:ARG0 (s11x8 / 半影
					:possessor (s11c / planet
						:name (s11n / name
							:op1 "月球")))
				:aspect state)
			:ARG0-of (s11x10 / 包括-01
				:ARG1 (s11a / and
					:op1 (s11x11 / 中东部
						:part-of (s11c2 / world-region
							:name (s11n2 / name
								:op1 "波利尼西亚")))
					:op2 (s11x30 / 部分
						:mod (s11x31 / 绝大)
						:part-of (s11x12 / continent
							:name (s11n21 / name
								:op1 "北美洲"))
						:mod (s11x32 / 以外
							:op1 (s11a2 / and
								:op1 (s11x13 / 大部
									:part-of (s11p / local-region
										:name (s11n3 / name
											:op1 "阿拉斯加")))
								:op2 (s11x14 / 地区
									:place (s11x15 / 交界-01
										:ARG0 (s11a3 / and
											:op1 (s11c3 / country
												:name (s11n4 / name
													:op1 "加拿大"))
											:op2 (s11p2 / local-region
												:name (s11n5 / name
													:op1 "阿拉斯加")))
										:aspect state))
								:op3 (s11x20 / 中南部
									:part-of (s11c4 / country
										:name (s11n6 / name
											:op1 "多米尼克")))
								:op4 (s11i12 / island
									:name (s11n22 / name
										:op1 "向风群岛")))))
					:op3 (s11i2 / island
						:name (s11n7 / name
							:op1 "科隆群岛"))
					:op4 (s11x17 / 地区
						:part-of (s11c5 / country
							:name (s11n9 / name
								:op1 "哥伦比亚"))
						:place (s11x18 / 沿岸
							:op1 (s11o / ocean
								:name (s11n8 / name
									:op1 "加勒比海"))))
					:op5 (s11x19 / 西北角
						:part-of (s11c6 / country
							:name (s11n10 / name
								:op1 "委内瑞拉")))
					:op6 (s11c7 / country
						:name (s11n11 / name
							:op1 "冰岛"))
					:op7 (s11i3 / island
						:name (s11n12 / name
							:op1 "扬马延岛"))
					:op8 (s11i4 / island
						:name (s11n13 / name
							:op1 "斯瓦尔巴群岛"))
					:op9 (s11i5 / island
						:name (s11n14 / name
							:op1 "法罗群岛"))
					:op10 (s11c8 / country
						:name (s11n15 / name
							:op1 "爱尔兰"))
					:op11 (s11x22 / 西北部
						:part-of (s11c10 / country
							:name (s11n16 / name
								:op1 "英国")))
					:op12 (s11x16 / 西北角
						:part-of (s11g / geographic-entity
							:name (s11n17 / name
								:op1 "伊比利亚半岛")))
					:op13 (s11i7 / island
						:name (s11n18 / name
							:op1 "亚速尔群岛"))
					:op14 (s11i9 / island
						:name (s11n20 / name
							:op1 "马德拉群岛"))
					:op15 (s11x21 / 中西部
						:part-of (s11i8 / island
							:name (s11n19 / name
								:op1 "加那利群岛"))))
				:aspect state))
		:mod (s11x33 / 都)
		:aspect activity)
	:op3 (s11x23 / 看到-01
		:ARG1 s11x9
		:place (s11i10 / island
			:name (s11n23 / name
				:op1 "阿鲁巴")
			:part-of (s11i11 / island
				:name (s11n24 / name
					:op1 "背风安的列斯群岛"))
			:mod (s11x24 / 仅))
		:aspect activity))

# alignment:
s11a: 0-0
s11a2: 0-0
s11a3: 0-0
s11a4: 0-0
s11c: 0-0
s11c10: 0-0
s11c2: 0-0
s11c3: 0-0
s11c4: 0-0
s11c5: 0-0
s11c6: 0-0
s11c7: 0-0
s11c8: 0-0
s11g: 0-0
s11i2: 0-0
s11i3: 0-0
s11i4: 0-0
s11i5: 0-0
s11i6: 0-0
s11i7: 0-0
s11i8: 0-0
s11i9: 0-0
s11n: 0-0
s11n10: 0-0
s11n11: 0-0
s11n12: 0-0
s11n13: 0-0
s11n14: 0-0
s11n15: 0-0
s11n16: 0-0
s11n17: 0-0
s11n18: 0-0
s11n19: 0-0
s11n2: 0-0
s11n20: 0-0
s11n3: 0-0
s11n4: 0-0
s11n5: 0-0
s11n6: 0-0
s11n7: 0-0
s11n8: 0-0
s11n9: 0-0
s11o: 0-0
s11p: 0-0
s11p2: 0-0
s11s: 0-0
s11x: 8-8
s11x10: 22-22
s11x11: 24-24
s11x12: 26-26
s11x13: 29-29
s11x14: 35-35
s11x15: 34-34
s11x16: 65-65
s11x17: 35-35
s11x18: 61-61
s11x19: 65-65
s11x2: 4-4
s11x20: 38-38
s11x21: 88-88
s11x22: 78-78
s11x3: 2-2
s11x4: 9-9
s11x5: 19-19
s11x6: 15-15
s11x7: 14-14
s11x8: 13-13
s11x9: 20-20

# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11x5)
            (s11x5 :overlap s11x7)
            (s11x5 :overlap s11x23))
    :modal ((root :modal author)
            (author :full-affirmative s11x7)
            (author :full-affirmative s11x15)
            (author :full-affirmative s11x10)
            (author :full-affirmative s11x5)
            (author :full-affirmative s11x)
            (author :neutral-affirmative s11x23))
    :coref ()
)

## chinese_umr-0034, sentence 2

# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61
Words: 闭幕礼 在 法兰西 体育场 举行 ， 巴黎 奥组委 主席 埃斯坦盖 致辞 时 说 ， 残 奥 闭幕 意味着 整个 巴黎 2024 年 奥运 及 残奥 的 结束 ， 但 奥运 的 讯息 仍然 相随 ： “ 让 我们 继续 尝试 ， 让 我们 继续 跌倒 ， 让 我们 继续 爬起 ， 让 我们 继续 行动 ， 让 我们 继续 相信 ”

# sentence level graph:
(s2a1 / and
    :op1 (s2x2 / 说-01
        :ARG0 (s2p / individual-person
            :name (s2n / name
                :op1 "埃斯坦盖")
            :ARG1-of (s2h / have-org-role-91
                :ARG2 (s2s / sports-organization
                    :name (s2n2 / name
                        :op1 "巴黎"
                        :op2 "奥组委"))
                :ARG3 (s2x3 / 主席)))
        :ARG1 (s2c / contrast-91
            :ARG1 (s2x5 / 意味着-01
                :ARG0 (s2x7 / 闭幕-01
                    :ARG0 (s2x8 / 残奥)
                    :aspect performance)
                :ARG1 (s2x10 / 结束-01
                    :ARG1 (s2a / and
                        :op1 (s2x11 / 奥运)
                        :op2 (s2x12 / 残奥)
                        :mod (s2x13 / 整个)
                        :place (s2c1 / human-settlement
                            :name (s2n3 / name
                                :op1 "巴黎"))
                        :temporal (s2d / date-entity
                            :year 2024))
                    :aspect performance)
                :aspect state)
            :ARG2 (s2x6 / 相随-01
                :ARG0 (s2x15 / 讯息
                    :possessor (s2x16 / 奥运)
                    :topic (s2a2 / and
                        :op1 (s2x17 / 尝试-01
                            :ARG0 (s2x18 / person
                                :refer-person 1st
                                :refer-number plural)
                            :mode imperative
                            :aspect activity)
                        :op2 (s2x20 / 跌倒-01
                            :ARG0 s2x18
                            :mode imperative
                            :aspect performance)
                        :op3 (s2x21 / 爬起-00
                            :ARG0 s2x18
                            :mode imperative
                            :aspect performance)
                        :op4 (s2x22 / 行动-01
                            :ARG0 s2x18
                            :mode imperative
                            :aspect activity)
                        :op5 (s2x23 / 相信-01
                            :ARG0 s2x18
                            :mode imperative
                            :aspect state)
                        :mod (s2x19 / 继续)))
                :mod (s2x14 / 仍然)
                :aspect state))
        :temporal (s2x4 / 致辞-01
            :ARG0 s2p
            :aspect performance)
        :aspect performance)
    :op2 (s2x / 举行-01
        :ARG1 (s2x1 / 闭幕礼)
        :place (s2s1 / facility
            :name (s2n1 / name
                :op1 "法兰西"
                :op2 "体育场"))
        :aspect performance))

# alignment:
s2a: 0-0
s2a1: 0-0
s2a2: 0-0
s2c: 0-0
s2c1: 20-20
s2d: 0-0
s2h: 0-0
s2n: 0-0
s2n1: 0-0
s2n2: 0-0
s2n3: 0-0
s2p: 0-0
s2s: 7-20
s2s1: 3-4
s2x: 5-5
s2x1: 1-1
s2x10: 27-27
s2x11: 23-23
s2x12: 25-25
s2x13: 19-19
s2x14: 33-33
s2x15: 32-32
s2x16: 30-30
s2x17: 40-40
s2x18: 43-43
s2x19: 44-44
s2x2: 13-13
s2x20: 45-45
s2x21: 50-50
s2x22: 55-55
s2x23: 60-60
s2x3: 9-9
s2x4: 11-11
s2x5: 18-18
s2x6: 34-34
s2x7: 17-17
s2x8: 16-16
s2x9: 15-15

# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x)
            (s2x :contained s2x4)
            (s2x5 :overlap s2x6)
            (s2x4 :overlap s2x2)
            (s2x2 :overlap s2x5)
            (s2x5 :overlap s2x7)
            (s2x7 :overlap s2x10)
            (s2x2 :after s2x17)
            (s2x2 :after s2x20)
            (s2x2 :after s2x21)
            (s2x2 :after s2x22)
            (s2x2 :after s2x23))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :full-affirmative s2x4)
            (author :full-affirmative s2p)
            (s2p :full-affirmative s2x5)
            (s2p :full-affirmative s2x6)
            (s2p :full-affirmative s2x22)
            (s2p :full-affirmative s2x23)
            (author :full-affirmative s2x2)
            (s2p :full-affirmative s2c)
            (s2p :full-affirmative s2x7)
            (s2p :partial-affirmative s2x17)
            (s2p :partial-affirmative s2x20)
            (s2p :partial-affirmative s2x21)
            (s2p :partial-affirmative s2x22)
            (s2p :partial-affirmative s2x23)
            (s2p :full-affirmative s2x10))
    :coref ((s1x3 :same-event s2x1)
            (s2x1 :same-event s2x7)
            (s1c1 :same-entity s2c1))
)

## chinese_umr-0008, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 部分 来源 认为 ， 这种 金币 是 为了 方便 人们 大量 购买 邮票 。

# sentence level graph:
(s5x / 认为-01
    :ARG0 (s5x2 / 来源
        :quant (s5x3 / 部分))
    :ARG1 (s5x11 / 为了-01
        :ARG0 (s5x4 / 金币
            :mod (s5x5 / 这)
            :unit (s5x12 / 种))
        :ARG1 (s5x6 / 方便-01
            :ARG1 (s5x7 / 人们)
            :ARG2 (s5x8 / 购买-01
                :ARG1 (s5x9 / 邮票)
		    :manner (s5x10 / 大量)
                :aspect process)
            :aspect state)
        :aspect state)
    :aspect state)

# alignment:
s5i2: 0-0
s5x: 3-3
s5x10: 11-11
s5x11: 5-5
s5x12: 5-5
s5x2: 2-2
s5x3: 1-1
s5x4: 6-6
s5x5: 5-5
s5x6: 9-9
s5x7: 10-10
s5x8: 12-12
s5x9: 13-13

# document level annotation:
(s5s0 / sentence
    :temporal ((s5x6 :overlap s5x8)
            (document-creation-time :overlap s5x)
            (s5x :overlap s5x11)
            (s5x11 :overlap s5x6))
    :modal ((author :full-affirmative s5x)
            (root :modal author)
            (author :full-affirmative s5x2)
            (s5x2 :full-affirmative s5x11)
            (s5x2 :partial-affirmative s5x6)
            (s5x2 :partial-affirmative s5x8))
    :coref ((s4x8 :same-entity s5x4))
)

## chinese_umr-0025, sentence 882

# :: snt882
Index:    1  2    3  4    5  6    7  8  9 10   11 12 13 14 15   16   17 18 19   20 21   22 23 24 25 26   27 28 29   30 31   32 33   34   35 36 37   38                     39 40 41   42   43 44
Words: 为了   使  你们   对  地球   的  大小   有  一  个  概念   ，  我  想  要  告诉   你们   ：  在  发明   电  之前   ，  在  六  个  大洲   上  ，  为了   点  路灯   ，  需要   维持   一  支  为数   四十六万二千五百一十一            人  的  真正   大军   。 

# sentence level graph:
(s882x14 / 想要-01
	:ARG0 (s882x13 / individual-person
		:refer-person 1
		:refer-number singular)
	:ARG1 (s882x16 / 告诉-01
		:ARG1 (s882x34 / 需要-01
			:ARG1 (s882x35 / 维持-01
				:ARG1 (s882x43 / 大军
					:mod (s882x42 / 真正)
					:mod (s882x40 / 人
						:quant 462511)
					:quant 1
					:unit (s882x37 / 支))
				:modal-strength (s882x81 / full-affirmative
					:conceiver s882x13))
			:purpose (s882x31 / 点-01
				:ARG1 (s882x32 / 路灯)
				:modal-strength (s882x79 / partial-affirmative
					:conceiver (s882x80 / person)))
			:place (s882x27 / 大洲
				:quant 6
				:unit (s882x26 / 个))
			:temporal (s882x22 / 之前
				:op1 (s882x20 / 发明-01
					:ARG1 (s882x21 / 电))))
		:ARG2 (s882x17 / individual-person
			:refer-person 2
			:refer-number plural)
		:modal-strength (s882x76 / partial-affirmative)
		:modal-predicate (s882x14 / 想要-01)))

# alignment:
s882x13: 0-0
s882x14: 14-14
s882x16: 16-16
s882x17: 0-0
s882x20: 20-20
s882x21: 21-21
s882x22: 22-22
s882x26: 10-10
s882x27: 27-27
s882x31: 31-31
s882x32: 32-32
s882x34: 34-34
s882x35: 35-35
s882x37: 37-37
s882x40: 40-40
s882x42: 42-42
s882x43: 43-43
s882x76: 0-0
s882x79: 0-0
s882x80: 0-0
s882x81: 0-0

# document level annotation:
(s882s0 / sentence)

## chinese_umr-0025, sentence 609

# :: snt609
Index: 1    2    3  4 5    6    7  8
Words: “ 为了   忘却   。  ” 酒鬼   回答   。 

# sentence level graph:
(s609x7 / 回答-01
	:ARG0 (s609x6 / 酒鬼)
	:ARG2 (s609x2 / 为了
		:ARG1 (s609x3 / 忘却))
	:modal-strength (s609x14 / full-affirmative))

# alignment:
s609x14: 0-0
s609x2: 2-2
s609x3: 3-3
s609x6: 6-6
s609x7: 7-7

# document level annotation:
(s609s0 / sentence)
