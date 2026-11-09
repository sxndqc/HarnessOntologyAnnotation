# Gold UMR annotations of sentences like those of chinese_umr-0031

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

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

## chinese_umr-0017, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Words: 独立 观察员 指出 ， 实际 数字 可能 要 高 得 多 ， 330 个 镇区 中 只有 72 个 仍 在 缅军 控制 之下 ， 尽管 这些 镇区 包括 所有 主要 人口 中心 。

# sentence level graph:
(s10x / 指出-01
	:ARG0 (s10x2 / 观察员
		:mod (s10x3 / 独立))
	:ARG1 (s10a / and
		:op1 (s10x4 / 高-01
			:ARG0 (s10x5 / 数字
				:mod (s10x6 / 实际))
			:degree (s10x9 / 得多)
			:aspect state
			:mod (s10x8 / 要)
			:mod (s10x7 / 可能))
		:op2 (s10h / have-concession-91
			:ARG1 (s10x10 / 控制-01
				:ARG0 (s10x11 / armed-organization
					:name (s10n / name
						:op1 "缅军"))
				:ARG1 (s10x12 / 镇区
					:quant 72
					:unit (s10x13 / 个)
					:mod (s10x16 / 只有)
					:part-of (s10i2 / implicit-argument
						:quant 330
						:unit (s10x14 / 个)))
				:aspect state
				:mod (s10x15 / 仍))
			:ARG2 (s10x17 / 包括-01
				:ARG0 s10x12
				:ARG1 (s10x20 / 中心
					:quant (s10x21 / 所有)
					:mod (s10x22 / 主要)
					:mod (s10x23 / 人口))
				:aspect state))))

# alignment:
s10a: 0-0
s10i2: 0-0
s10x: 3-3
s10x10: 23-23
s10x11: 22-22
s10x12: 15-15
s10x13: 14-14
s10x14: 14-14
s10x15: 20-20
s10x16: 17-17
s10x17: 29-29
s10x18: 15-15
s10x19: 27-27
s10x2: 2-2
s10x20: 33-33
s10x21: 30-30
s10x22: 31-31
s10x23: 32-32
s10x3: 1-1
s10x4: 9-9
s10x5: 6-6
s10x6: 5-5
s10x7: 7-7
s10x8: 8-8
s10x9: 10-10

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10x)
            (document-creation-time :overlap s10x4)
            (document-creation-time :overlap s10x17))
    :modal ((root :modal author)
            (author :full-affirmative s10x)
            (author :full-affirmative s10x2)
            (s10x2 :neutral-affirmative s10x4)
            (s10x2 :full-affirmative s10x10)
            (s10x2 :full-affirmative s10x17))
    :coref ((s3m2 :same-entity s10x11))
)

## chinese_umr-0025, sentence 691

# :: snt691
Index:    1  2  3    4  5  6  7    8  9   10 11   12   13   14 15 16 17 18   19   20   21 22 23
Words: 既然   在  我  之前   不  曾  有  任何   人  想到   要  占有   这些   星星   ，  那  我  就  占有   这些   星星   。  ” 

# sentence level graph:
(s691x24 / say
	:ARG1 (s691x26 / causation
		:ARG1 (s691x10 / 想到-01
			:ARG0 (s691x9 / 人
				:mod (s691x8 / 任何)
				:polarity -)
			:ARG1 (s691x11 / 要-03
				:ARG0 (s691x12 / 占有-01
					:ARG1 (s691x14 / 星星
						:mod (s691x13 / 这些))
					:ARG0 s691x9))
			:temporal (s691x4 / 之前
				:op1 (s691x3 / individual-person
					:refer-person 1
					:refer-number singular)))
		:ARG2 (s691x19 / 占有-01
			:ARG0 (s691x17 / individual-person
				:refer-person 1
				:refer-number singular)
			:ARG1 (s691x21 / 星星
				:mod (s691x20 / 这些)))))

# alignment:
s691x10: 10-10
s691x11: 11-11
s691x12: 12-12
s691x13: 13-13
s691x14: 14-14
s691x17: 0-0
s691x19: 12-12
s691x20: 13-13
s691x21: 14-14
s691x24: 0-0
s691x26: 0-0
s691x3: 0-0
s691x4: 4-4
s691x8: 8-8
s691x9: 9-9

# document level annotation:
(s691s0 / sentence)

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

## chinese_umr-0017, sentence 4

# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 截至 2023 年 3 月 ， 联合国 （ UN ） 估计 ， 自 2021 年 2 月 政变 以来 ， 缅甸 有 1760 万 人 需要 人道 援助 ， 160 万 人 在 境内 流离失所 ， 超过 55,000 座 民用 建筑 被 摧毁 。

# sentence level graph:
(s4x / 估计-01
	:ARG0 (s4i2 / international-organization
		:name (s4n / name
			:op1 "联合国"
			:op2 "UN"))
	:ARG1 (s4a / and
		:op1 (s4x2 / 需要-01
			:ARG0 (s4x21 / 人
				:quant (s4x20 / 1760万))
			:ARG1 (s4x11 / 援助
				:mod (s4x12 / 人道))
			:place (s4c2 / country
				:name (s4n2 / name
					:op1 "缅甸"))
			:temporal (s4x7 / 自
				:temporal (s4d / date-entity
					:year 2021
					:month 2)
				:temporal-of (s4x8 / 政变-01))
			:aspect state)
		:op2 (s4x3 / 流离失所-01
			:ARG0 (s4x10 / 人
				:quant (s4x9 / 160万))
			:place (s4x15 / 境内)
			:temporal s4x7
			:aspect state)
		:op3 (s4x4 / 摧毁-01
			:ARG1 (s4x16 / 建筑
				:mod (s4x17 / 民用)
				:unit (s4x18 / 座)
				:quant (s4x5 / 55000
					:mod (s4x6 / 超过)))
			:place s4c2
			:temporal s4x7
			:aspect performance))
	:temporal (s4x19 / 截至
		:temporal (s4d2 / date-entity
			:year 2023
			:month 3))
	:aspect performance)

# alignment:
s4a: 0-0
s4c2: 9-9
s4d: 0-0
s4d2: 0-0
s4h: 0-0
s4h2: 0-0
s4i2: 0-0
s4n: 0-0
s4n2: 0-0
s4x: 11-11
s4x10: 25-25
s4x11: 28-28
s4x12: 27-27
s4x15: 34-34
s4x16: 41-41
s4x17: 40-40
s4x18: 39-39
s4x19: 1-1
s4x2: 26-26
s4x20: 23-23
s4x21: 25-25
s4x3: 35-35
s4x4: 43-43
s4x5: 0-0
s4x6: 37-37
s4x7: 13-13
s4x8: 18-18
s4x9: 24-24

# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :before s4x)
            (document-creation-time :before s4x2)
            (document-creation-time :before s4x3)
            (document-creation-time :before s4x4))
    :modal ((root :modal author)
            (author :full-affirmative s4x2)
            (author :full-affirmative s4x3)
            (author :full-affirmative s4x4)
            (author :full-affirmative s4x))
    :coref ((s1c2 :same-entity s4c2)
            (s1x15 :same-event s4x8))
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

## chinese_umr-0025, sentence 244

# :: snt244
Index:    1  2  3  4      5    6  7  8    9 10   11 12 13   14       15 16 17 18   19   20 21 22   23   24 25 26 27     28 29 30 31 32 33 34 35   36 37 38 39 40 41 42
Words: 为了   叫  我  的  朋友们    警惕   这  种  危险   —— 他们   同  我  一样   长期以来     和  这  种  危险   接触   ，  却  没有   意识   到  它  的  危险性    —— 我  花  了  很  大  的  功夫   画  了  这  副  画  。 

# sentence level graph:
(s244x37 / 画-01
	:ARG0 (s244x30 / individual-person
		:refer-person 1
		:refer-number singular
		:modal-strength (s244x85 / full-affirmative
			:conceiver (s244x87 / author)))
	:ARG1 (s244x41 / 画
		:mod (s244x39 / 这)
		:unit (s244x40 / 副))
	:aspect performance
	:manner (s244x31 / 花-01
		:ARG0 s244x30
		:ARG1 (s244x36 / 功夫
			:mod (s244x34 / 大
				:degree (s244x33 / 很)))
		:aspect performance
		:modal-strength (s244x82 / full-affirmative
			:conceiver (s244x86 / author)))
	:purpose (s244x2 / 叫-01
		:ARG1 (s244x5 / 朋友们
			:possessor-of (s244x3 / individual-person
				:refer-person 1
				:refer-number singular)
			:ARG0-of (s244x60 / mean
				:ARG1 (s244x61 / contrast
					:ARG1 (s244x20 / 接触-01
						:ARG0 (s244x11 / individual-person
							:refer-person 3
							:refer-number plural)
						:ARG1 (s244x19 / 危险
							:mod (s244x17 / 这)
							:unit (s244x18 / 种))
						:duration (s244x15 / 长期以来))
					:ARG2 (s244x24 / 意识-01
						:ARG1 (s244x28 / 危险性
							:possessor-of (s244x26 / individual-person
								:refer-person 3
								:refer-number singular))
						:polarity -)
					:manner (s244x12 / 一样
						:ARG0 s244x11
						:ARG1 (s244x13 / individual-person
							:refer-person 1
							:refer-number singular)))))
		:ARG2 (s244x6 / 警惕-01
			:ARG0 s244x5
			:ARG1 (s244x9 / 危险
				:mod (s244x7 / 这)
				:unit (s244x8 / 种))
			:modal-strength (s244x81 / full-affirmative))
		:modal-strength (s244x84 / partial-affirmative
			:conceiver s244x3))
	:modal-strength (s244x83 / full-affirmative
		:conceiver (s244x88 / author)))

# alignment:
s244x11: 0-0
s244x12: 14-14
s244x13: 0-0
s244x15: 15-15
s244x17: 7-7
s244x18: 8-8
s244x19: 9-9
s244x2: 2-2
s244x20: 20-20
s244x24: 24-24
s244x26: 0-0
s244x28: 28-28
s244x3: 0-0
s244x30: 0-0
s244x31: 31-31
s244x33: 33-33
s244x34: 34-34
s244x36: 36-36
s244x37: 37-37
s244x39: 7-7
s244x40: 40-40
s244x41: 37-37
s244x5: 5-5
s244x6: 6-6
s244x60: 0-0
s244x61: 0-0
s244x7: 7-7
s244x8: 8-8
s244x81: 0-0
s244x82: 0-0
s244x83: 0-0
s244x84: 0-0
s244x85: 0-0
s244x86: 0-0
s244x87: 0-0
s244x88: 0-0
s244x9: 9-9

# document level annotation:
(s244s0 / sentence)

## chinese_umr-0025, sentence 241

# :: snt241
Index:    1        2  3    4  5    6  7  8  9   10 11 12   13 14 15   16 17 18 19   20 21     22   23 24 25 26   27 28 29 30 31 32   33   34 35 36 37 38 39 40   41   42 43 44   45 46
Words: 可是   猴面包树     的  危险   ，  大家   都  不  大  了解   ，  对  迷失   在  小  行星   上  的  人  来说   ，  危险性    非常   之  大  ，  因此   这  一  回  ，  我  贸然   打破   了  我  的  这  种  不  喜欢   教训   人  的  惯例   。 

# sentence level graph:
(s241x47 / contrast
	:ARG2 (s241x50 / causation
		:ARG1 (s241x51 / and
			:op1 (s241x10 / 了解-01
				:ARG0 (s241x6 / 大家)
				:mod (s241x7 / 都)
				:modal-strength (s241x84 / full-negative)
				:polarity -
				:degree (s241x9 / 大)
				:ARG1 (s241x4 / 危险-01
					:ARG0 (s241x2 / 猴面包树)))
			:op2 (s241x20 / 来说-01
				:ARG1 (s241x19 / 人
					:ARG0-of (s241x13 / 迷失-02
						:place (s241x16 / 行星
							:mod (s241x15 / 小))))
				:ARG2 (s241x25 / 大-01
					:ARG0 (s241x22 / 危险性)
					:degree (s241x23 / 非常))
				:ARG0 s241x2))
		:ARG2 (s241x34 / 打破-01
			:ARG0 (s241x32 / individual-person
				:refer-person 1
				:refer-number singular)
			:manner (s241x33 / 贸然)
			:aspect performance
			:ARG1 (s241x45 / 惯例
				:possessor-of (s241x36 / individual-person
					:refer-person 1
					:refer-number singular)
				:ARG0-of (s241x74 / mean
					:ARG1 (s241x41 / 喜欢-01
						:polarity -
						:ARG1 (s241x42 / 教训
							:ARG1 (s241x43 / 人))
						:ARG0 s241x32))
				:mod (s241x38 / 这)
				:unit (s241x39 / 种))
			:temporal (s241x30 / 回
				:mod (s241x28 / 这)
				:quant 1)
			:modal-strength (s241x85 / full-affirmative))))

# alignment:
s241x10: 10-10
s241x13: 13-13
s241x15: 15-15
s241x16: 16-16
s241x19: 19-19
s241x2: 2-2
s241x20: 20-20
s241x22: 22-22
s241x23: 23-23
s241x25: 9-9
s241x28: 28-28
s241x30: 30-30
s241x32: 0-0
s241x33: 33-33
s241x34: 34-34
s241x36: 0-0
s241x38: 28-28
s241x39: 39-39
s241x4: 4-4
s241x41: 41-41
s241x42: 42-42
s241x43: 19-19
s241x45: 45-45
s241x47: 0-0
s241x50: 0-0
s241x51: 0-0
s241x6: 6-6
s241x7: 7-7
s241x74: 0-0
s241x84: 0-0
s241x85: 0-0
s241x9: 9-9

# document level annotation:
(s241s0 / sentence)

## chinese_umr-0025, sentence 1173

# :: snt1173
Index: 1  2  3  4    5  6 7
Words: “ 他  不  顾  危险   。  ”

# sentence level graph:
(s1173x8 / say
	:ARG1 (s1173x4 / 顾
		:ARG0 (s1173x2 / individual-person
			:refer-person 3
			:refer-number singular)
		:ARG1 (s1173x5 / 危险)
		:modal-strength (s1173x14 / full-negative)
		:polarity -))

# alignment:
s1173x14: 0-0
s1173x2: 0-0
s1173x4: 4-4
s1173x5: 5-5
s1173x8: 0-0

# document level annotation:
(s1173s0 / sentence)

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

## chinese_umr-0025, sentence 285

# :: snt285
Index:    1  2  3  4  5  6    7    8    9 10 11 12   13 14   15 16   17 18
Words: 饮水   也  快  完  了  ，  担心   可能   发生   最  坏  的  情况   ，  心里   很  着急   。 

# sentence level graph:
(s285x19 / causation
	:ARG1 (s285x21 / and
		:op1 (s285x4 / 完-01
			:ARG0 (s285x1 / 饮水)
			:mod (s285x3 / 快)
			:mod (s285x2 / 也)
			:aspect performance)
		:op2 (s285x7 / 担心
			:ARG1 (s285x8 / 可能-01
				:ARG0 (s285x9 / 发生-01
					:ARG0 (s285x13 / 情况
						:mod (s285x11 / 坏
							:degree (s285x10 / 最)))
					:modal-predicate s285x7
					:modal-strength (s285x37 / neutral-affirmative)))))
	:ARG2 (s285x17 / 着急-01
		:ARG0 (s285x15 / 心里)
		:degree (s285x16 / 很)))

# alignment:
s285x1: 1-1
s285x10: 10-10
s285x11: 11-11
s285x13: 13-13
s285x15: 15-15
s285x16: 16-16
s285x17: 17-17
s285x19: 0-0
s285x2: 2-2
s285x21: 0-0
s285x3: 3-3
s285x37: 0-0
s285x4: 4-4
s285x7: 7-7
s285x8: 8-8
s285x9: 9-9

# document level annotation:
(s285s0 / sentence)

## chinese_umr-0025, sentence 119

# :: snt119
Index:  1    2  3  4  5  6    7  8    9   10 11   12 13 14   15   16 17 18 19 20 21 22 23   24 25     26 27 28 29   30 31 32 33 34 35   36 37 38 39 40
Words: 他  一面   看  着  我  的  飞机   ，  一面   微微   地  点点   头  ，  接着   说道   ：  “  可  不  是  么  ，  乘坐   这  玩艺儿    ，  你  不  可能   是  从  很  远  的  地方   来  的  …  ” 

# sentence level graph:
(s119x41 / temporal
	:ARG1 (s119x43 / and
		:op1 (s119x3 / 看-02
			:ARG0 (s119x1 / individual-person
				:refer-person 3
				:refer-number singular)
			:ARG1 (s119x7 / 飞机
				:possessor-of (s119x5 / individual-person
					:refer-person 1
					:refer-number singular))
			:modal-strength (s119x67 / full-affirmative
				:conceiver (s119x68 / author)))
		:op2 (s119x12 / 点头-01
			:ARG0 s119x1
			:degree (s119x10 / 微微)
			:modal-strength (s119x69 / full-affirmative
				:conceiver (s119x70 / author))))
	:ARG2 (s119x16 / 说道-01
		:ARG0 s119x1
		:ARG1 (s119x53 / and
			:op1 (s119x19 / 可不是
				:mode expressive)
			:op2 (s119x30 / 可能-01
				:polarity -
				:ARG0 (s119x37 / 来-01
					:ARG0 (s119x28 / individual-person
						:refer-person 2
						:refer-number singular
						:modal-strength (s119x74 / full-affirmative
							:conceiver s119x1))
					:ARG2 (s119x36 / 地方
						:mod (s119x34 / 远
							:degree (s119x33 / 很)))
					:mode judgement
					:manner (s119x24 / 乘坐-01
						:ARG0 s119x28
						:ARG1 (s119x26 / 玩艺儿
							:mod (s119x25 / 这)))
					:modal-strength (s119x73 / full-negative
						:conceiver s119x1))))
		:modal-strength (s119x71 / full-affirmative
			:conceiver (s119x72 / author))))

# alignment:
s119x1: 0-0
s119x10: 10-10
s119x12: 13-13
s119x16: 16-16
s119x19: 19-19
s119x24: 24-24
s119x25: 25-25
s119x26: 26-26
s119x28: 0-0
s119x3: 3-3
s119x30: 30-30
s119x33: 33-33
s119x34: 34-34
s119x36: 36-36
s119x37: 37-37
s119x41: 0-0
s119x43: 0-0
s119x5: 0-0
s119x53: 0-0
s119x67: 0-0
s119x68: 0-0
s119x69: 0-0
s119x7: 7-7
s119x70: 0-0
s119x71: 0-0
s119x72: 0-0
s119x73: 0-0
s119x74: 0-0

# document level annotation:
(s119s0 / sentence)

## chinese_umr-0026, sentence 8

# :: snt8
Index:    1    2    3    4    5    6  7    8    9 10   11   12     13 14     15   16   17   18 19
Words: 由于   本次   行程   包括   到访   北京   ，  当时   外界   就  已经   预测   习近平    与  马英九    将会   再次   会面   。 

# sentence level graph:
(s8x16 / 预测-01
	:ARG0 (s8x17 / 外界)
	:ARG1 (s8x19 / 会面-01
		:ARG0 (s8a / and
			:op1 (s8i2 / individual-person
				:name (s8n / name
					:op1 "习近平"))
			:op2 (s8i3 / individual-person
				:name (s8n2 / name
					:op1 "马英九")))
		:frequency (s8x20 / 再次)
		:aspect process)
	:temporal (s8x18 / 当时)
	:reason (s8x / 包括-01
		:ARG0 (s8x3 / 行程-01
			:mod (s8x4 / 本次)
			:aspect process)
		:ARG1 (s8x5 / 到访-01
			:ARG1 (s8c / city
				:name (s8n3 / name
					:op1 "北京"))
			:aspect habitual)
		:aspect state)
	:mod (s8x2 / 已经)
	:aspect performance)

# alignment:
s8a: 0-0
s8c: 0-0
s8i2: 0-0
s8i3: 0-0
s8n: 0-0
s8n2: 0-0
s8n3: 0-0
s8x: 4-4
s8x16: 12-12
s8x17: 9-9
s8x18: 8-8
s8x19: 18-18
s8x2: 11-11
s8x20: 17-17
s8x3: 3-3
s8x4: 2-2
s8x5: 5-5

# document level annotation:
(s8s0 / sentence
	:temporal ((document-creation-time :before s8x16)
		(s8x16 :after s8x19)
		(document-creation-time :before s8x)
		(s8x3 :overlap s8x5)))
	:modal ((root :modal author)
		(author :partial-affirmative s8x19)
		(author :full-affirmative s8x3)
		(author :full-affirmative s8x5)
		(author :full-affirmative s8x)
		(author :full-affirmative s8x16)
		(root :modal author))

## chinese_umr-0016, sentence 13

# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
Words: 政务司 司长 陈国基 说 ， “ 对于 这场 大雨 ， 雨势 非常 非常 大 ， 正如 同事 提及 ， 它 是 五百 年 一 遇 ， 雨 又 大 又 突然 ， 可 预测 程度 很 低 ， 所以 我们 无法 如 应对 之前 的 台风 苏拉 般 大幅 提早 预告 。”

# sentence level graph:
(s13x / 说-01
    :ARG0 (s13i2 / individual-person
        :name (s13n / name
            :op1 "陈国基")
        :ARG1-of (s13h / have-org-role-91
            :ARG2 (s13g / government-organization
                :name (s13n2 / name
                    :op1 "政务司"))
            :ARG3 (s13r / 司长)))
    :ARG1 (s13a2 / and
        :op1 (s13x2 / 大-01
            :ARG0 (s13x17 / 雨势
                :possessor (s13x20 / 大雨
                    :mod (s13x15 / 这场)))
            :degree (s13x14 / 非常)
            :aspect state)
        :op2 (s13x13 / 提及-01
            :ARG0 (s13x22 / 同事
                :ARG2-of (s13h2 / have-rel-role-91
                    :ARG1 s13i2))
            :ARG1 (s13x23 / 遇-01
                :ARG1 s13x20
                :aspect habitual
                :frequency (s13r2 / rate-entity-91
                    :ARG1 1
                    :ARG3 (s13t / temporal-quantity
                        :quant 500
                        :unit (s13x12 / 年))))
            :aspect performance
            :mod (s13x5 / 正如))
        :op3 (s13a3 / and
            :op1 (s13x26 / 大-01
                :ARG0 s13x20
                :aspect state)
            :op2 (s13x28 / 突然-01
                :ARG0 s13x20
                :aspect state)
            :ARG2-of (s13h4 / have-cause-91
                :ARG1 (s13x3 / 低-01
                    :ARG0 (s13x16 / 程度
                        :possessor s13x20
                        :mod (s13x18 / 可预测))
                    :aspect state
                    :mod (s13x4 / 很)
                    :ARG2-of (s13h5 / have-cause-91
                        :ARG1 (s13x6 / 预告-01
                            :ARG0 (s13p / person
                                :refer-person 1st
                                :refer-number plural)
                            :ARG1 s13x20
                            :ARG1-of (s13x7 / 提早-01
                                :ARG2 (s13x8 / 大幅))
                            :example (s13x9 / 应对-01
                                :ARG0 s13p
                                :ARG1 (s13n3 / natural-disaster
                                    :name (s13n4 / name
                                        :op1 "苏拉")
                                    :mod (s13x24 / 台风))
                                :aspect performance)
                            :aspect performance)))))
        :quote s13x)
    :aspect performance)

# alignment:
s13a2: 0-0
s13a3: 0-0
s13g: 0-0
s13h: 0-0
s13h2: 0-0
s13h3: 0-0
s13h4: 0-0
s13h5: 0-0
s13i2: 0-0
s13n: 0-0
s13n2: 0-0
s13n3: 0-0
s13n4: 0-0
s13p: 0-0
s13r: 2-2
s13r2: 0-0
s13s: 0-0
s13t: 0-0
s13x: 4-4
s13x12: 23-23
s13x13: 18-18
s13x14: 12-12
s13x15: 8-8
s13x16: 35-35
s13x17: 11-11
s13x18: 33-33
s13x2: 14-14
s13x20: 9-9
s13x22: 17-17
s13x23: 25-25
s13x26: 14-14
s13x28: 31-31
s13x3: 37-37
s13x4: 36-36
s13x5: 16-16
s13x6: 51-51
s13x7: 50-50
s13x8: 49-49
s13x9: 43-43

# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x)
            (s13x :overlap s13x2)
            (s13x :before s13x13)
            (present-reference :overlap s13x23)
            (s13x :overlap s13x26)
            (s13x :overlap s13x28)
            (s13x :overlap s13x3)
            (s13x13 :before s13x9)
            (s13x13 :before s13x7)
            (s13x7 :overlap s13x6))
    :modal ((root :modal author)
            (author :full-affirmative s13x2)
            (author :full-affirmative s13x23)
            (author :full-affirmative s13x13)
            (author :full-affirmative s13x26)
            (author :full-affirmative s13x28)
            (author :full-affirmative s13x3)
            (author :full-affirmative s13x9)
            (author :full-affirmative s13x)
            (author :unspecified s13i2)
            (s13i2 :unspecified s13a2)
            (author :neutral-negative s13x6))
    :coref ((s8x5 :same-event s13x20))
)

## chinese_umr-0025, sentence 284

# :: snt284
Index:  1    2    3    4    5  6    7  8
Words: 我  发现   机器   故障   似乎   很  严重   ， 

# sentence level graph:
(s284x2 / 发现-01
	:ARG0 (s284x1 / individual-person
		:refer-person 1
		:refer-number singular)
	:ARG1 (s284x5 / 似乎-01
		:ARG0 (s284x7 / 严重-01
			:degree (s284x6 / 很)
			:ARG0 (s284x4 / 故障-01
				:ARG0 (s284x3 / 机器)))))

# alignment:
s284x1: 0-0
s284x2: 2-2
s284x3: 3-3
s284x4: 4-4
s284x5: 5-5
s284x6: 6-6
s284x7: 7-7

# document level annotation:
(s284s0 / sentence)

## chinese_umr-0013, sentence 3

# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 地震 期间 ， 全 台 共 发布 2 则 国家 级 警报 ， 分别 为 上午 7 时 58 分 18 秒 及 24 秒 。

# sentence level graph:
(s3x / 发布-01
	:ARG1 (s3x5 / 警报
		:quant 2
		:unit (s3x6 / 则)
		:mod (s3x7 / 国家级))
	:place (s3r / country-region
		:name (s3n / name
			:op1 "台湾")
		:mod (s3x10 / 全))
	:aspect performance
	:temporal (s3x8 / 期间
		:op1 (s3x9 / 地震-01
			:aspect performance))
	:temporal (s3a / and
		:op1 (s3d2 / date-entity
			:dayperiod (s3x11 / 上午)
			:time 07:58:18)
		:op2 (s3d / date-entity
			:dayperiod s3x11
			:time 07:58:24)))

# alignment:
s3a: 0-0
s3d: 0-0
s3d2: 0-0
s3h: 8-8
s3h2: 17-17
s3n: 0-0
s3r: 0-0
s3x: 7-7
s3x5: 12-12
s3x6: 9-9
s3x7: 10-10
s3x8: 2-2
s3x9: 1-1

# document level annotation:
(s3s0 / sentence
	:temporal ((s3x8 :contained s3x)
		(s3x :overlap s3a))
	:modal ((root :modal author)
		(author :full-affirmative s3x)
		(author :full-affirmative s3x)))

## chinese_umr-0005, sentence 33

# :: snt33
Index: 1  2 3  4  5 6  7 8 9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
Words: 为此 ， 于海 认为 ， 国歌 是 “ 国家 的  第一 声音 、  是  国家 声音 的  标志 ”  ，  理应 受到 法律 的  保护 ，  所以 必须 要  立法 保护 国歌 。 

# sentence level graph:
(s33x / 认为-02
    :ARG0 (s33i2 / individual-person
        :name (s33n / name
            :op1 "于海"))
    :ARG1 (s33h / have-reason-91
        :ARG1 (s33x11 / 必须-01
            :ARG0 (s33x12 / 立法-01
                :purpose (s33x13 / 保护-01
                    :ARG1 (s33x14 / 国歌))))
        :ARG2 (s33h2 / have-reason-91
            :ARG1 (s33x17 / 理应-00
                :ARG0 (s33x3 / 受到-01
                    :ARG1 (s33x5 / 保护-01
                        :ARG0 (s33x16 / 法律)
                        :ARG1 s33x14
                        :aspect process)
                    :aspect performance)
                :aspect state)
            :ARG2 (s33a / and
                :op1 (s33i4 / identity-91
                    :ARG1 s33x14
                    :ARG2 (s33x9 / 声音
                        :mod (s33x10 / 国家)
                        :ord (s33o / ordinal-entity
                            :value 1))
                    :aspect state)
                :op2 (s33i3 / identity-91
                    :ARG1 s33x14
                    :ARG2 (s33x6 / 标志
                        :mod (s33x7 / 声音
                            :mod (s33x8 / 国家)))
                    :aspect state)))
        :aspect state)
    :reason (s33t / thing
        :refer-number singular
        :refer-person 3rd)
    :aspect state)


# alignment:
s33a: 0-0
s33h: 0-0
s33h2: 0-0
s33i2: 0-0
s33i3: 0-0
s33i4: 0-0
s33n: 0-0
s33o: 0-0
s33t: 0-0
s33x: 4-4
s33x10: 9-9
s33x11: 28-28
s33x12: 30-30
s33x13: 25-25
s33x14: 6-6
s33x16: 23-23
s33x17: 21-21
s33x3: 22-22
s33x5: 25-25
s33x6: 18-18
s33x7: 12-12
s33x8: 9-9
s33x9: 12-12

# document level annotation:
(s33s0 / sentence
    :temporal ((document-creation-time :before s33x)
        (s33x :overlap s33x11)
        (s33x11 :overlap s33x12)
        (s33x12 :overlap s33x13)
        (s33x :overlap s33i3)
        (s33x :overlap s33i4)
        (s33x :overlap s33x8)
        (s33x8 :overlap s33x9))
    :modal ((root :modal author)
        (author :full-affirmative s33i3)
        (author :full-affirmative s33i4)
        (author :full-affirmative s33x9)
        (author :strong-partial-affirmative s33x8)
        (author :full-affirmative s33h)
        (author :full-affirmative s33x))
    :coref ((s32i2 :same-entity s33i2)
        (s32x4 :same-event s33t)))

## chinese_umr-0034, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Words: 和 巴黎 奥运 开幕 时 一样 ， 残奥 闭幕 礼 同样 在 雨中 举行 ， 下届 残奥 举办 城市 洛杉矶 市长 巴斯 接过 国际 残奥 委员会 会旗 ， 洛杉矶 呈献 六分钟 的 交接 表演

# sentence level graph:
(s5c1 / and
    :op1 (s5x / 举行-01
        :ARG1 (s5x1 / 礼
            :mod (s5x2 / 闭幕-01
                :ARG0 (s5x3 / 残奥)
                :aspect performance))
        :ARG0-of (s5x6 / 一样-02
            :ARG1 (s5x8 / 开幕-01
                :ARG0 (s5x7 / 奥运
                    :place (s5c / human-settlement
                        :name (s5n / name
                            :op1 "巴黎")))
                :aspect performance))
        :temporal (s5x5 / 雨)
        :mod (s5x4 / 同样)
        :aspect performance)
    :op2 (s5x9 / 接过-01
        :ARG0 (s5p / individual-person
            :name (s5n1 / name
                :op1 "巴斯")
            :ARG1-of (s5h / have-org-role-91
                :ARG2 (s5c3 / human-settlement
                    :name (s5n2 / name
                        :op1 "洛杉矶")
                    :ARG0-of (s5x12 / 举办-01
                        :ARG1 (s5x13 / 残奥
                            :mod (s5x14 / 下届))
                        :aspect performance))
                :ARG3 (s5x10 / 市长)))
        :ARG1 (s5x11 / 会旗
            :possessor (s5i / international-organization
                :name (s5n3 / name
                    :op1 "国际"
                    :op2 "残奥"
                    :op3 "委员会")))
        :aspect performance)
    :op3 (s5x15 / 呈献-01
        :ARG0 s5c3
        :ARG1 (s5x16 / 表演
            :duration (s5t / temporal-quantity
                :unit (s5x18 / 分钟)
                :quant 6)
            :mod (s5x17 / 交接))
        :aspect performance))

# alignment:
s5c: 2-2
s5c1: 0-0
s5c2: 20-20
s5c3: 29-29
s5h: 0-0
s5i: 8-26
s5n: 0-0
s5n1: 0-0
s5n2: 0-0
s5n3: 0-0
s5n4: 0-0
s5p: 0-0
s5t: 0-0
s5x: 14-14
s5x1: 10-10
s5x10: 21-21
s5x11: 27-27
s5x12: 18-18
s5x13: 17-17
s5x14: 16-16
s5x15: 30-30
s5x16: 34-34
s5x17: 33-33
s5x18: 31-31
s5x2: 9-9
s5x3: 8-8
s5x4: 11-11
s5x5: 13-13
s5x6: 6-6
s5x7: 3-3
s5x8: 4-4
s5x9: 23-23

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x8)
            (s5x8 :after s5x2)
            (s5x2 :overlap s5x)
            (s5x9 :after s5x15)
            (s5x15 :after s5x12)
            (s5x :contained s5x9)
            (s5x :contained s5x15))
    :modal ((root :modal author)
            (author :full-affirmative s5x8)
            (author :full-affirmative s5x2)
            (author :full-affirmative s5x)
            (author :full-affirmative s5x12)
            (author :full-affirmative s5x9)
            (author :full-affirmative s5x15))
    :coref ((s2x7 :same-event s5x2))
)

## chinese_umr-0017, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 在 许多 村庄 和 城镇 ， 军政府 的 袭击 导致 数万 人 被 驱逐 。

# sentence level graph:
(s8x / 导致-01
	:ARG0 (s8x2 / 袭击-01
		:ARG0 (s8x9 / 军政府)
		:place (s8a / and
			:op1 (s8x4 / 村庄)
			:op2 (s8x5 / 城镇)
			:quant (s8x3 / 许多))
		:aspect performance)
	:ARG1 (s8x6 / 驱逐-01
		:ARG1 (s8x11 / 人
			:quant (s8x10 / 数万))
		:aspect performance)
	:aspect performance)

# alignment:
s8a: 0-0
s8h: 0-0
s8x: 10-10
s8x10: 11-11
s8x11: 12-12
s8x2: 9-9
s8x3: 2-2
s8x4: 3-3
s8x5: 5-5
s8x6: 14-14
s8x9: 7-7

# document level annotation:
(s8s0 / sentence
    :temporal ((document-creation-time :before s8x)
            (document-creation-time :before s8x2)
            (document-creation-time :before s8x6)
            (s8x2 :after s8x6))
    :modal ((root :modal author)
            (author :full-affirmative s8x2)
            (author :full-affirmative s8x6)
            (author :full-affirmative s8x))
    :coref ((s6x16 :same-entity s8x9))
)

## chinese_umr-0019, sentence 8

# :: snt8
Index:    1  2      3    4  5    6    7    8    9   10 11   12   13 14
Words: 广州   市  教育局    强调   ，  不要   强制   要求   学生   统一   穿  校服   返校   。 

# sentence level graph:
(s8x / 强调-01
	:ARG0 (s8p / political-organization
		:name (s8n / name
			:op1 (s8x2 / 教育局))
		:place (s8c / city
			:name (s8n2 / name
				:op1 "广州")))
	:ARG1 (s8x4 / 强制-01
		:ARG0 s8p
		:ARG1 (s8x5 / 要求-01
			:aspect performance)
		:ARG2 (s8x6 / 学生)
		:ARG3 (s8x7 / 穿-01
			:ARG1 (s8x8 / 校服)
			:manner (s8x9 / 统一)
			:aspect state)
		:ARG4 (s8x10 / 返校-01)
		:polarity -
		:aspect performance)
	:aspect performance)

# alignment:
s8c: 0-0
s8n: 0-0
s8n2: 0-0
s8p: 0-0
s8x: 4-4
s8x10: 13-13
s8x2: 3-3
s8x4: 7-7
s8x5: 8-8
s8x6: 9-9
s8x7: 11-11
s8x8: 12-12
s8x9: 10-10

# document level annotation:
(s8s0 / sentence
	:temporal ((document-creation-time :before s8x)
		(s8x :after s8x4)
		(s8x :after s8x7)
		(s8x4 :overlap s8x5)))
	:modal ((root :modal author)
		(author :full-affirmative s8x5)
		(author :full-affirmative s8x7)
		(author :full-negative s8x4)
		(author :full-affirmative s8x)
		(root :modal author))

## chinese_umr-0015, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 广州 市 教育局 强调 ， 不要 强制 要求 学生 统一 穿 校服 返校 。

# sentence level graph:
(s8x / 强调-01
    :ARG0 (s8x2 / government-organization
        :name (s8n / name
            :op1 "广州市教育局"))
    :ARG1 (s8x4 / 要求-02
        :ARG1 (s8x7 / 学生)
        :ARG2 (s8x6 / 穿-01
            :ARG0 s8x7
            :ARG1 (s8x8 / 校服)
            :mod (s8x5 / 统一)
            :temporal (s8x9 / 返校-01
                :ARG0 s8x7
                :aspect process)
            :aspect state)
        :mod (s8x11 / 强制)
        :mode imperative
        :modal-strength partial-negative
        :aspect process)
    :aspect performance)

# alignment:
s8g: 0-0
s8n: 0-0
s8n2: 0-0
s8x: 4-4
s8x11: 7-7
s8x2: 3-3
s8x3: 2-2
s8x4: 8-8
s8x5: 10-10
s8x6: 11-11
s8x7: 9-9
s8x8: 12-12
s8x9: 13-13

# document level annotation:
(s8s0 / sentence
    :temporal ((s2a :after s8x)
            (s8x :depends-on s8x4)
            (s8x4 :depends-on s8x6))
    :modal ((root :modal author)
            (author :full-affirmative s8x)
            (author :full-affirmative s8x2)
            (s8x2 :partial-negative s8x4)
            (s8x2 :unspecified s8x6)
            (s8x2 :unspecified s8x9))
    :coref ()
)

## chinese_umr-0021, sentence 9

# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 此后 本 影 继续 向 东北 斜贯 墨西哥 、 美国 和 加拿大 东南部 ， 进入 北大西洋 ， 逐渐 转向 东北 移动 ， 在 日落 时分 结束 于 爱尔兰 西南 约 810 公里 的 洋面 。

# sentence level graph:
(s9a / consecutive
	:op1 (s9x / 继续-01
		:ARG0 (s9x2 / 本影)
		:ARG1 (s9x4 / 贯穿-01
			:ARG0 s9x2
			:ARG1 (s9a2 / and
				:op1 (s9c / country
					:name (s9n2 / name
						:op1 "墨西哥"))
				:op2 (s9c2 / country
					:name (s9n / name
						:op1 "美国"))
				:op3 (s9x5 / 东南部
					:part-of (s9c3 / country
						:name (s9n3 / name
							:op1 "加拿大"))))
			:direction (s9x21 / 东北)
			:manner (s9x22 / 斜)
			:aspect activity)
		:temporal (s9x3 / 此后)
		:aspect activity)
	:op2 (s9x6 / 进入-01
		:ARG0 s9x2
		:ARG1 (s9o / ocean
			:name (s9n4 / name
				:op1 "北大西洋"))
		:aspect performance)
	:op3 (s9a3 / and
		:op1 (s9x15 / 转向-01
			:ARG1 s9x2
			:ARG2 (s9x9 / 东北)
			:manner (s9x8 / 逐渐)
			:aspect directed-activity)
		:op2 (s9x7 / 移动-01
			:ARG0 s9x2
			:direction s9x9
			:aspect activity))
	:op4 (s9x10 / 结束-01
		:ARG0 s9x2
		:temporal (s9x11 / 日落)
		:place (s9x12 / 洋面
			:place (s9x16 / 处
				:direction (s9x13 / 西南
					:op1 (s9c5 / country
						:name (s9n6 / name
							:op1 "爱尔兰")))
				:extent (s9d / distance-quantity
					:quant 810
					:unit (s9x14 / 公里))))
		:aspect performance))

# alignment:
s9a: 0-0
s9a2: 0-0
s9c: 0-0
s9c2: 0-0
s9c3: 0-0
s9c5: 0-0
s9d: 0-0
s9n: 0-0
s9n2: 0-0
s9n3: 0-0
s9n4: 0-0
s9n6: 0-0
s9o: 0-0
s9x: 4-4
s9x10: 26-26
s9x11: 24-24
s9x12: 34-34
s9x13: 29-29
s9x14: 32-32
s9x2: 2-2
s9x3: 1-1
s9x4: 7-7
s9x5: 13-13
s9x6: 15-15
s9x7: 21-21
s9x8: 18-18
s9x9: 6-6

# document level annotation:
(s9s0 / sentence
    :temporal ((document-creation-time :before s9x)
            (s9x4 :overlap s9x6)
            (s9x4 :overlap s9x7)
            (s9x7 :after s9x10)
            (s9x7 :overlap s9x15))
    :modal ((root :modal author)
            (author :full-affirmative s9x4)
            (author :full-affirmative s9x)
            (author :full-affirmative s9x6)
            (author :full-affirmative s9x7)
            (author :full-affirmative s9x10)
            (author :full-affirmative s9x15))
    :coref ()
)

## chinese_umr-0016, sentence 2

# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 受 风暴 海葵 残留 云带 影响 ， 香港 各区 7 日 起 普遍 降 暴雨 ， 洪水 涌入 港铁 黄大仙 站 的 大堂 和 月台 。

# sentence level graph:
(s2a / and
    :op1 (s2x / 降-01
        :ARG1 (s2x2 / 暴雨)
        :place (s2x3 / 各区
            :part-of (s2c / country-partition
                :name (s2n4 / name
                    :op1 "香港")))
        :manner (s2x5 / 普遍)
        :cause (s2x6 / 影响-01
            :ARG0 (s2x7 / 云带
                :ARG0-of (s2x4 / 残留-01
                    :cause (s2n2 / natural-disaster
                        :name (s2n3 / name
                            :op1 (s2x9 / 海葵))
                        :ARG1-of (s2i2 / identity-91
                            :ARG2 (s2x8 / 风暴)
                            :aspect state))))
            :aspect performance)
        :aspect process
        :temporal (s2x19 / 起
            :op1 (s2d / date-entity
                :day 7)))
    :op2 (s2x10 / 出现-01
        :ARG0 s2x3
        :theme (s2a3 / and
            :op1 (s2x20 / 浸-01
                :ARG0 (s2x18 / 水)
                :aspect process)
            :op2 (s2x21 / 倾泻-01
                :ARG1 (s2x17 / 山泥)
                :aspect process))
        :aspect performance)
    :op3 (s2x11 / 涌入-01
        :ARG0 (s2x12 / 洪水)
        :ARG1 (s2a2 / and
            :op1 (s2x13 / 大堂
                :part-of (s2s / building
                    :name (s2n / name
                        :op1 "黄大仙"
                        :op2 "站")
                    :part-of (s2x14 / corporation
                        :name (s2n5 / name
                            :op1 "港铁"))))
            :op2 (s2x15 / 月台
                :part-of s2s))
        :aspect performance))

# alignment:
s2a: 0-0
s2a2: 0-0
s2c: 0-0
s2d: 0-0
s2i2: 0-0
s2n: 0-0
s2n2: 0-0
s2n3: 0-0
s2n4: 0-0
s2s: 0-0
s2x: 14-14
s2x10: 12-12
s2x11: 18-18
s2x12: 17-17
s2x13: 23-23
s2x14: 19-19
s2x15: 25-25
s2x2: 15-15
s2x3: 9-9
s2x4: 4-4
s2x5: 13-13
s2x6: 6-6
s2x7: 5-5
s2x8: 2-2
s2x9: 3-3

# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x4)
            (s2x4 :overlap s2x)
            (s2x :overlap s2x11)
            (s2x :overlap s2x10)
            (s2x4 :overlap s2x6))
    :modal ((root :modal author)
            (author :full-affirmative s2x6)
            (author :full-affirmative s2x)
            (author :full-affirmative s2x11))
    :coref ((s1c2 :same-entity s2c))
)

## chinese_umr-0025, sentence 485

# :: snt485
Index:    1    2  3    4  5    6  7    8  9 10   11   12   13 14
Words: 因为   国王   所  要求   的  主要   是  保持   他  的  威严   受到   尊敬   。 

# sentence level graph:
(s485x15 / causation
	:ARG1 (s485x8 / 保持-01
		:ARG1 (s485x11 / 威严
			:possessor-of (s485x9 / individual-person
				:refer-person 3
				:refer-number singular))
		:ARG2 (s485x12 / 受到-01
			:ARG0 s485x11
			:ARG1 (s485x13 / 尊敬-01
				:ARG1 s485x11))
		:mod (s485x6 / 主要-01))
	:ARG1 (s485y1 / identity-91
		:ARG0 (s485x21 / thing
			:ARG1-of (s485x4 / 要求-01
				:ARG0 (s485x2 / 国王)))
		:ARG1 s485x8))

# alignment:
s485x11: 11-11
s485x12: 12-12
s485x13: 13-13
s485x15: 0-0
s485x2: 2-2
s485x21: 0-0
s485x4: 4-4
s485x6: 6-6
s485x8: 8-8
s485x9: 0-0
s485y1: 0-0

# document level annotation:
(s485s0 / sentence)

## chinese_umr-0025, sentence 861

# :: snt861
Index:    1  2    3  4  5    6    7  8    9 10
Words: 很少   会  出现   一  个  海洋   干涸   的  现象   。 

# sentence level graph:
(s861x2 / 会-02
	:ARG0 (s861x3 / 出现-01
		:ARG1 (s861x9 / 现象
			:ARG0-of (s861x15 / mean
				:ARG1 (s861x7 / 干涸-01
					:ARG0 (s861x6 / 海洋
						:quant 1
						:unit (s861x5 / 个)))))
		:frequency (s861x1 / 很少)
		:modal-strength (s861x21 / neutral-affirmative)))

# alignment:
s861x1: 1-1
s861x15: 0-0
s861x2: 2-2
s861x21: 0-0
s861x3: 3-3
s861x5: 5-5
s861x6: 6-6
s861x7: 7-7
s861x9: 9-9

# document level annotation:
(s861s0 / sentence)

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

## chinese_umr-0021, sentence 3

# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Words: 月球 本影 接触 地表 而 使 该 区域 完全 得 不 到 阳光 ， 就 会 形成 日全食 ， 同时 在 本影 两侧 数千 公里 的 半影 范围 内 遮挡 部分 阳光 ， 形成 日偏食 。

# sentence level graph:
(s3a / and
	:op1 (s3h / have-condition-91
		:ARG1 (s3x / 形成-01
			:ARG2 (s3x2 / 日全食)
			:aspect performance)
		:ARG2 (s3x3 / 接触-01
			:ARG0 (s3x4 / 本影
				:possessor (s3x5 / planet
					:name (s3n / name
						:op1 "月球")))
			:ARG1 (s3x6 / 地表)
			:cause-of (s3x7 / 得到-01
				:ARG0 (s3x13 / 区域
					:mod (s3x14 / 该))
				:ARG1 (s3x8 / 阳光)
				:manner (s3x25 / 完全)
				:aspect state
				:polarity -)
			:aspect performance))
	:op2 (s3x17 / 遮挡-01
		:ARG0 s3x4
		:ARG1 (s3x10 / 阳光
			:mod (s3x11 / 部分))
		:temporal (s3x12 / 同时)
		:aspect performance
		:place (s3x9 / 范围
			:possessor (s3x20 / 半影
				:place (s3x21 / 两侧
					:op1 s3x4)
				:extent (s3d / distance-quantity
					:quant (s3x22 / 千
						:mod (s3x23 / 数))
					:unit (s3x24 / 公里))))
		:cause-of (s3x15 / 形成-01
			:ARG2 (s3x16 / 日偏食)
			:aspect performance)))

# alignment:
s3a: 0-0
s3h: 0-0
s3h2: 0-0
s3x: 17-17
s3x10: 13-13
s3x11: 31-31
s3x12: 20-20
s3x13: 8-8
s3x14: 7-7
s3x15: 17-17
s3x16: 35-35
s3x17: 30-30
s3x18: 2-2
s3x19: 1-1
s3x2: 18-18
s3x20: 2-2
s3x21: 23-23
s3x22: 24-24
s3x23: 24-24
s3x24: 25-25
s3x3: 3-3
s3x4: 2-2
s3x5: 1-1
s3x6: 4-4
s3x7: 10-10
s3x8: 13-13
s3x9: 27-27

# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :before s3x)
            (document-creation-time :before s3x15)
            (s3x3 :after s3x7)
            (s3x :before s3x3)
            (s3x15 :before s3x17))
    :modal ((root :modal author)
            (author :full-affirmative s3x)
            (author :full-negative s3x7)
            (author :full-affirmative s3x3)
            (author :full-affirmative s3x15)
            (author :full-affirmative s3x17))
    :coref ()
)

## chinese_umr-0022, sentence 3

# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12
Words: 该 物种 的 模式 产地 在 美洲 和 亚洲 的 海域 。

# sentence level graph:
(s3h / have-place-91
	:ARG1 (s3x / 产地
		:mod (s3x3 / 模式)
		:possessor (s3x4 / 物种
			:mod (s3x5 / 该)))
	:ARG2 (s3x2 / 海域
		:mod (s3a / and
			:op1 (s3c / continent
				:name (s3n / name
					:op1 "美洲"))
			:op2 (s3c2 / continent
				:name (s3n2 / name
					:op1 "亚洲"))))
	:aspect state)

# alignment:
s3a: 0-0
s3c: 0-0
s3c2: 0-0
s3h: 0-0
s3n: 0-0
s3n2: 0-0
s3x: 5-5
s3x2: 11-11
s3x3: 4-4
s3x4: 2-2
s3x5: 1-1

# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :overlap s3h))
    :modal ((root :modal author)
            (author :full-affirmative s3h))
    :coref ((s1a :same-entity s3x4))
)

## chinese_umr-0020, sentence 6

# :: snt6
Index:    1    2  3    4    5  6    7  8    9 10   11 12 13 14 15   16   17   18   19 20   21   22 23   24     25   26 27 28   29 30
Words: 不同   地区   的  彩礼   通常   不  一样   ，  女方   在  结婚   前  也  会  视  男方   条件   决定   金额   ，  这种   习俗   在  中国   大部分    地区   均  有  出现   。 

# sentence level graph:
(s6a / and-91
	:op1 (s6x20 / 一样-01
		:ARG0 (s6x21 / 彩礼
			:source (s6x22 / 地区
				:quant (s6x23 / 同
					:polarity -)))
		:manner (s6x24 / 通常))
	:op2 (s6x5 / 决定-01
		:ARG0 (s6x6 / 女方)
		:ARG1 (s6x7 / 金额
			:ARG1-of (s6x8 / 视-01
				:ARG0 s6x6
				:ARG1 (s6x9 / 条件
					:possessor-of (s6x10 / 男方))))
		:temporal (s6x11 / 前
			:op1 (s6x12 / 结婚))
		:mod (s6x13 / 也)
		:aspect performance)
	:op3 (s6x14 / 出现-01
		:ARG1 (s6x15 / 习俗
			:mod (s6x4 / 这种))
		:place (s6x17 / 地区
			:part (s6x18 / 中国
				:mod (s6x19 / 大部分)))
		:aspect habitual
		:mod (s6x / 均)))

# alignment:
s6a: 0-0
s6x: 27-27
s6x10: 16-16
s6x11: 12-12
s6x12: 11-11
s6x13: 13-13
s6x14: 29-29
s6x15: 22-22
s6x17: 2-2
s6x18: 24-24
s6x19: 25-25
s6x20: 7-7
s6x21: 4-4
s6x22: 2-2
s6x23: 1-1
s6x24: 5-5
s6x4: 21-21
s6x5: 18-18
s6x6: 9-9
s6x7: 19-19
s6x8: 15-15
s6x9: 17-17

# document level annotation:
(s6s0 / sentence
	:temporal ((s6x11 :before s6x8)
		(document-creation-time :overlap s6x20)
		(s6x20 :depends-on s6x14)
		(s6x20 :depends-on s6x5)
		(s6x5 :before s6x8)
		(document-creation-time :overlap s6a)
		(s6x11 :depends-on s6x5))
	:modal ((root :modal author)
		(author :neutral-negative s6x20)
		(author :full-affirmative s6x5)
		(author :full-affirmative s6x14)
		(author :full-negative s6x20))
	:coref ((s6x7 :same-entity s6x4)))

## chinese_umr-0010, sentence 6

# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
Words: 不同 地区 的 彩礼 通常 不 一样 ， 女方 在 结婚 前 也 会 视 男方 条件 决定 金额 ， 这种 习俗 在 中国 大部分 地区 均 有 出现 。

# sentence level graph:
(s6a / and
    :op1 (s6x20 / 一样-01
        :ARG0 (s6x2 / 彩礼
            :place (s6x3 / 地区
                :mod (s6x / 不同)))
        :mod (s6x4 / 通常)
        :polarity -
        :aspect state)
    :op2 (s6x5 / 决定-01
        :ARG0 (s6x6 / 女方)
        :ARG1 (s6x7 / 金额)
        :temporal (s6x11 / 前
            :op1 (s6x21 / 结婚-01
                :aspect performance))
        :mod (s6x13 / 也)
        :manner (s6x8 / 视-01
            :ARG0 s6x6
            :ARG1 (s6x9 / 条件
                :possessor (s6x10 / 男方))
            :aspect process)
        :aspect performance)
    :op3 (s6x14 / 出现-01
        :ARG0 (s6x17 / 地区
            :part-of (s6c / country
                :name (s6n / name
                    :op1 "中国"))
            :quant (s6x12 / 大部分))
        :ARG1 (s6x15 / 习俗
            :mod (s6x16 / 这种))
        :mod (s6x18 / 均)
        :aspect habitual))

# alignment:
s6a: 0-0
s6c: 0-0
s6n: 0-0
s6x: 1-1
s6x10: 16-16
s6x11: 12-12
s6x12: 25-25
s6x13: 13-13
s6x14: 29-29
s6x15: 22-22
s6x16: 21-21
s6x17: 2-2
s6x18: 27-27
s6x2: 4-4
s6x20: 7-7
s6x21: 11-11
s6x3: 2-2
s6x4: 5-5
s6x5: 18-18
s6x6: 9-9
s6x7: 19-19
s6x8: 15-15
s6x9: 17-17

# document level annotation:
(s6s0 / sentence
    :temporal ((document-creation-time :overlap s6x20)
            (s6x20 :overlap s6x5)
            (s6x20 :overlap s6x14)
            (s6x5 :overlap s6x8)
            (s6x11 :contained s6x5)
            (s6x11 :after s6x21))
    :modal ((author :full-negative s6x20)
            (root :modal author)
            (author :full-affirmative s6x5)
            (author :unspecified s6x21)
            (author :full-affirmative s6x14))
    :coref ((s4x :same-entity s6x15))
)
