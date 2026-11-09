# Gold UMR annotations of sentences like those of chinese_umr-0023

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0026, sentence 24

# :: snt24
Index:      1    2    3  4  5      6  7      8      9   10 11     12 13     14 15   16   17     18 19   20     21 22   23   24 25   26   27   28 29   30   31     32 33
Words: 马英九    方面   出席   者  为  马英九    、  马英九    基金会    执行   长  萧旭岑    、  总统府    前  专门   委员   王光慈    ，  以及   国安会    前  咨询   委员   暨  政治   大学   东亚   所  荣誉   教授   邱坤玄    。 

# sentence level graph:
(s24x / 为-01
	:ARG0 (s24x2 / 出席者
		:ARG1-of (s24h3 / have-org-role-91
			:ARG2 (s24x3 / 马英九)))
	:ARG1 (s24a / and
		:op1 (s24i6 / individual-person
			:name (s24n2 / name
				:op1 "马英九"))
		:op2 (s24i2 / individual-person
			:name (s24n3 / name
				:op1 "萧旭岑")
			:ARG1-of (s24h / have-org-role-91
				:ARG2 (s24o / organization
					:name (s24n4 / name
						:op1 "马英九基金会"))
				:ARG3 (s24r / 执行长)))
		:op3 (s24i3 / individual-person
			:name (s24n5 / name
				:op1 "王光慈")
			:ARG1-of (s24h2 / have-org-role-91
				:ARG2 (s24o2 / organization
					:name (s24n6 / name
						:op1 "总统府"))
				:ARG3 (s24r2 / 前专门委员)))
		:op4 (s24i4 / individual-person
			:name (s24n7 / name
				:op1 "邱坤玄")
			:ARG1-of (s24a2 / and
				:op1 (s24h5 / have-org-role-91
					:ARG2 (s24o3 / organization
						:name (s24n8 / name
							:op1 "国安会"))
					:ARG3 (s24x5 / 前咨询委员))
				:op2 (s24h6 / have-org-role-91
					:ARG2 (s24r3 / research-institute
						:name (s24n11 / name
							:op1 "政治大学东亚所"))
					:ARG3 (s24x6 / 荣誉教授)))))
	:aspect state)

# alignment:
s24a: 0-0
s24a2: 0-0
s24h: 0-0
s24h2: 0-0
s24h3: 0-0
s24h5: 0-0
s24h6: 0-0
s24i2: 0-0
s24i3: 0-0
s24i4: 0-0
s24i6: 0-0
s24n11: 0-0
s24n2: 0-0
s24n3: 0-0
s24n4: 0-0
s24n5: 0-0
s24n6: 0-0
s24n7: 0-0
s24n8: 0-0
s24o: 0-0
s24o2: 0-0
s24o3: 0-0
s24r: 10-10
s24r2: 15-15
s24r3: 0-0
s24x: 5-5
s24x2: 3-3
s24x3: 1-1
s24x5: 15-15
s24x6: 30-30

# document level annotation:
(s24s0 / sentence)
	:modal ((root :modal author)
		(author :full-affirmative s24x)
		(root :modal author))

## chinese_umr-0014, sentence 11

# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
Words: 在 天主教堂 ， 祝福 是 一种 祈祷 或 祈求 的 礼拜 仪式 ， 通常 由 神父 执行 ， 请求 上帝 对 被 祝福 的 人 或 人民 表示 仁慈 。 虽然 天主教堂 没有 改变 其 基本 立场 ， 但 这 表明 天主教堂 在 这个 问题 上 的 立场 有 了 一定 的 缓和 。

# sentence level graph:
(s11m / multi-sentence
    :op1 (s11a / and
        :op1 (s11i2 / identity-91
            :ARG1 (s11x15 / 祝福
                :place (s11x16 / 教堂
                    :mod (s11x17 / 天主)))
            :ARG2 (s11x / 仪式
                :mod (s11x2 / 礼拜)
                :mod (s11o2 / or
                    :op1 (s11x5 / 祈祷)
                    :op2 (s11x4 / 祈求)))
            :aspect state)
        :op2 (s11x3 / 执行-01
            :ARG0 (s11x8 / 神父)
            :ARG1 s11x15
            :mod (s11x7 / 通常)
            :aspect habitual)
        :op3 (s11x6 / 请求-01
            :ARG0 s11x8
            :ARG1 (s11x11 / 上帝)
            :ARG2 (s11x10 / 表示-01
                :ARG0 s11x11
                :ARG1 (s11x9 / 仁慈)
                :ARG2 (s11o / or
                    :op1 (s11x13 / 人)
                    :op2 (s11x12 / 人民)
                    :ARG1-of (s11x14 / 祝福-01
                        :aspect performance))
                :aspect performance)
            :aspect habitual))
    :op2 (s11b / have-concession-91
        :ARG1 (s11x27 / 表明-01
            :ARG0 (s11x28 / 这)
            :ARG1 (s11x30 / 缓和-01
                :ARG1 (s11x29 / 立场
                    :topic (s11x19 / 问题
                        :mod (s11x20 / 这个))
                    :possessor (s11x24 / 教堂
                        :mod (s11x25 / 天主)))
                :mod (s11x31 / 一定)
                :aspect inceptive)
            :aspect state)
        :ARG2 (s11x26 / 改变-01
            :ARG0 s11x24
            :ARG1 (s11x22 / 立场
                :mod (s11x23 / 基本)
                :possessor s11x24)
            :polarity -
            :aspect performance)))

# alignment:
s11a: 0-0
s11b: 0-0
s11e: 0-0
s11i2: 0-0
s11m: 0-0
s11o: 0-0
s11o2: 0-0
s11s: 0-0
s11s3: 0-0
s11s4: 0-0
s11x: 12-12
s11x1: 51-52
s11x10: 28-28
s11x11: 20-20
s11x12: 27-27
s11x13: 25-25
s11x14: 4-4
s11x15: 4-4
s11x16: 2-2
s11x17: 2-2
s11x19: 45-45
s11x2: 11-11
s11x20: 44-44
s11x22: 37-37
s11x23: 36-36
s11x24: 2-2
s11x25: 2-2
s11x26: 34-34
s11x27: 41-41
s11x28: 40-40
s11x29: 37-37
s11x3: 17-17
s11x30: 53-53
s11x31: 10-10
s11x4: 9-9
s11x5: 7-7
s11x6: 19-19
s11x7: 14-14
s11x8: 16-16
s11x9: 29-29

# document level annotation:
(s11s0 / sentence)

## chinese_umr-0025, sentence 513

# :: snt513
Index:    1    2  3 4    5  6    7  8  9   10 11 12 13   14   15 16 17 18 19   20 21 22 23 24   25   26 27   28 29 30   31   32   33 34 35 36   37 38 39   40 41 42   43   44   45 46   47   48 49   50 51   52 53 54 55 56   57 58 59
Words: 国王   说道   ：  “ 如果   我  命令   一  个  将军   象  一  只  蝴蝶   那样   从  这  朵  花  飞到   那  朵  花  ，  或者   命令   他  写作   一  个  悲剧   剧本   或者   变  一  只  海鸟   ，  而  如果   这  位  将军   接到   命令   不  执行   的话   ，  那么   ，  我们   中  的  谁  是  错误   的  呢 

# sentence level graph:
(s513x2 / 说道-01
	:ARG0 (s513x1 / 国王)
	:ARG1 (s513x63 / condition
		:ARG1 (s513x64 / contrast
			:ARG1 (s513x25 / or
				:op1 (s513x7 / 命令-01
					:ARG0 (s513x6 / individual-person
						:refer-person 1
						:refer-number singular
						:ARG1 (s513x27 / individual-person
							:refer-person 3
							:refer-number singular))
					:ARG1 (s513x10 / 将军
						:quant 1
						:unit (s513x9 / 个))
					:ARG2 (s513x20 / 飞到-01
						:ARG0 s513x10
						:manner (s513x11 / 像-01
							:ARG1 (s513x14 / 蝴蝶
								:quant 1
								:unit (s513x13 / 只)))
						:ARG2 (s513x19 / 花
							:mod (s513x17 / 这)
							:unit (s513x22 / 朵))
						:modal-predicate s513x7
						:modal-strength (s513x120 / partial-affirmative)))
				:op2 (s513x26 / 命令-01
					:ARG0 s513x6
					:ARG1 s513x27
					:ARG2 (s513x83 / or
						:op1 (s513x28 / 写作-01
							:ARG0 s513x6
							:ARG1 (s513x32 / 剧本
								:mod (s513x31 / 悲剧)
								:quant 1
								:unit (s513x30 / 个))
							:modal-predicate s513x26
							:modal-strength (s513x121 / partial-affirmative))
						:op2 (s513x34 / 变-01
							:ARG0 s513x6
							:ARG2 (s513x37 / 海鸟
								:quant 1
								:unit (s513x36 / 只))
							:modal-predicate s513x26
							:modal-strength (s513x122 / partial-affirmative)))))
			:ARG2 (s513x95 / condition
				:ARG1 (s513x96 / contrast
					:ARG1 (s513x44 / 接到-01
						:ARG0 (s513x43 / 将军
							:unit (s513x42 / 位)
							:mod (s513x41 / 这))
						:ARG1 (s513x45 / 命令)
						:modal-strength (s513x124 / full-affirmative))
					:ARG2 (s513x47 / 执行-01
						:modal-strength (s513x125 / full-negative)
						:polarity -
						:ARG0 s513x43
						:ARG1 s513x45))
				:modal-strength (s513x126 / neutral-affirmative
					:conceiver s513x1)))
		:ARG2 (s513x57 / 错误-01
			:ARG0 (s513x55 / amr-unknown
				:ARG1-of (s513x53 / include-91
					:ARG2 (s513x52 / individual-person
						:refer-person 1
						:refer-number plural)))
			:mode judgement
			:mode interrogative)
		:modal-strength (s513x123 / neutral-affirmative
			:conceiver s513x1)))

# alignment:
s513x1: 1-1
s513x10: 10-10
s513x11: 0-0
s513x120: 0-0
s513x121: 0-0
s513x122: 0-0
s513x123: 0-0
s513x124: 0-0
s513x125: 0-0
s513x126: 0-0
s513x13: 13-13
s513x14: 14-14
s513x17: 17-17
s513x19: 19-19
s513x2: 2-2
s513x20: 20-20
s513x22: 18-18
s513x25: 0-0
s513x26: 7-7
s513x27: 0-0
s513x28: 28-28
s513x30: 9-9
s513x31: 31-31
s513x32: 32-32
s513x34: 34-34
s513x36: 13-13
s513x37: 37-37
s513x41: 17-17
s513x42: 42-42
s513x43: 10-10
s513x44: 44-44
s513x45: 7-7
s513x47: 47-47
s513x52: 0-0
s513x53: 0-0
s513x55: 0-0
s513x57: 57-57
s513x6: 0-0
s513x63: 0-0
s513x64: 0-0
s513x7: 7-7
s513x83: 0-0
s513x9: 9-9
s513x95: 0-0
s513x96: 0-0

# document level annotation:
(s513s0 / sentence)

## chinese_umr-0022, sentence 11

# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Words: 目前 玳瑁 受到 《 濒危 野生 动植物 物种 国际 贸易 公约 》 的 保护 ， 很多 国家 已 禁止 猎捕 玳瑁 ， 也 禁止 进出口 玳瑁 产品 。

# sentence level graph:
(s11a / and
	:op1 (s11x / 保护-01
		:ARG0 (s11t / treaty
			:name (s11n / name
				:op1 "濒危野生动植物物种国际贸易公约"))
		:ARG1 (s11a3 / animal
			:name (s11n2 / name
				:op1 "玳瑁"))
		:temporal (s11x3 / 目前)
		:aspect state)
	:op2 (s11a2 / and
		:op1 (s11x4 / 禁止-01
			:ARG0 (s11x5 / 国家
				:quant (s11x6 / 很多))
			:ARG1 (s11x7 / 猎捕-01
				:ARG1 s11a3
				:modal-strength partial-negative
				:aspect activity)
			:mod (s11x9 / 已)
			:aspect performance)
		:op2 (s11x10 / 禁止-01
			:ARG0 s11x5
			:ARG1 (s11x11 / 进出口-01
				:ARG1 (s11x12 / 产品
					:mod s11a3)
				:modal-strength partial-negative
				:aspect activity)
			:mod (s11x14 / 也)
			:aspect performance)))

# alignment:
s11x: 18-18
s12a: 0-0
s12a2: 0-0
s12n: 0-0
s12t: 0-0
s12x: 14-14
s12x10: 19-19
s12x11: 25-25
s12x12: 27-27
s12x13: 2-2
s12x2: 2-2
s12x3: 1-1
s12x4: 19-19
s12x5: 17-17
s12x6: 16-16
s12x7: 20-20
s12x8: 2-2
s12x9: 18-18

# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :overlap s11x)
            (document-creation-time :depends-on s11x4)
            (document-creation-time :overlap s11x10))
    :modal ((root :modal author)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x4)
            (author :full-affirmative s11x10)
            (author :full-affirmative s11x5)
            (s11x5 :partial-negative s11x7)
            (s11x5 :partial-negative s11x11))
    :coref ()
)

## chinese_umr-0026, sentence 4

# :: snt4
Index:    1  2    3  4    5  6  7    8      9 10 11 12   13   14     15   16   17   18   19   20   21 22 23             24   25   26   27 28 29
Words: 同时   ，  位列   正  国级   党  和  国家   领导人    的  3  位  中共   中央   政治局    常委   亲自   出面   会见   台湾   客人   ，  是  中华人民共和国        历史   以来   第一   次  。 

# sentence level graph:
(s4a / and
	:op1 (s4x / 出面-01
		:ARG0 (s4x2 / 常委
			:ARG1-of (s4h / have-org-role-91
				:ARG2 (s4p2 / political-organization
					:name (s4n2 / name
						:op1 (s4x5 / 中共)
						:op2 (s4x6 / 中央)
						:op3 (s4x13 / 政治局))))
			:value 3
			:unit (s4x7 / 位)
			:ARG0-of (s4x8 / 位列-00
				:ARG0 (s4x9 / 领导人
					:ARG1-of (s4h2 / have-org-role-91
						:ARG2 (s4a2 / and
							:op1 (s4x10 / 党)
							:op2 (s4x11 / 国家))))
				:ARG1 (s4x12 / 国级
					:mod (s4x17 / 正))
				:aspect state))
		:ARG1 (s4x3 / 会见-01
			:ARG1 (s4x4 / 客人
				:place (s4p / province
					:name (s4n / name
						:op1 "台湾")))
			:aspect performance)
		:aspect performance
		:manner (s4x14 / 亲自))
	:op2 (s4i2 / identity-91
		:ARG1 s4x
		:ARG2 (s4c / country
			:name (s4n3 / name
				:op1 "中华人民共和国")
			:ord (s4o / ordinal-entity
				:value 1)
			:range (s4x15 / 以来
				:op1 (s4x16 / 历史)))
		:aspect state))

# alignment:
s4a: 0-0
s4a2: 0-0
s4c: 0-0
s4h: 0-0
s4h2: 0-0
s4i2: 0-0
s4n: 0-0
s4n2: 0-0
s4n3: 0-0
s4o: 0-0
s4p: 0-0
s4p2: 0-0
s4x: 18-18
s4x10: 6-6
s4x11: 8-8
s4x12: 5-5
s4x13: 15-15
s4x14: 17-17
s4x15: 26-26
s4x16: 25-25
s4x17: 4-4
s4x2: 16-16
s4x3: 19-19
s4x4: 21-21
s4x5: 13-13
s4x6: 14-14
s4x7: 12-12
s4x8: 3-3
s4x9: 9-9

# document level annotation:
(s4s0 / sentence
	:temporal ((document-creation-time :before s4x)
		(s4x :overlap s4x3)
		(document-creation-time :overlap s4x8)))
	:modal ((root :modal author)
		(author :full-affirmative s4x8)
		(author :full-affirmative s4x3)
		(author :full-affirmative s4x)
		(author :full-affirmative s4i2)
		(root :modal author))

## chinese_umr-0001, sentence 44

# :: snt44
Index: 1 2   3  4 5  6  7 8    9 10 11 12 13  14 15 16 17 18 19 20 21 22 23 24 25 26 27 28  29 30 31 32 33 34 35 36 37 38 39  40
Words: 《 大纪元 时报 》 引用 报导 ， 1987 年 ，  前  苏联 科学家 公布 了  一条 十分 惊人 的  消息 ，  在  月球 背向 地球 一面 的  火山口 中  ，  停放 着  一架 美国 二战 时期 的  重型 轰炸机 。 

# sentence level graph:
(s44x / 引用-01
    :ARG0 (s44n / newspaper
        :name (s44n2 / name
            :op1 "《"
            :op2 "大纪元"
            :op3 "时报"
            :op4 "》"))
    :ARG1 (s44x2 / 报导-01
        :ARG1 (s44x3 / 公布-01
            :ARG0 (s44x17 / 科学家
                :place (s44c2 / country-region
                    :name (s44n6 / name
                        :op1 "前"
                        :op2 "苏联")))
            :ARG1 (s44x4 / 消息
                :ARG1-of (s44i3 / identity-91
                    :ARG2 (s44x5 / 停放-01
                        :ARG1 (s44x11 / 轰炸机
                            :place (s44c / country
                                :name (s44n5 / name
                                    :op1 "美国"))
                            :temporal (s44d2 / date-entity
                                :era (s44x12 / 二战时期))
                            :unit (s44x13 / 架)
                            :quant 1
                            :mod (s44x14 / 重型))
                        :ARG2 (s44x6 / 中
                            :op1 (s44x7 / 口
                                :part (s44x8 / 火山
                                    :place (s44x9 / 一面
                                        :part (s44p / planet
                                            :name (s44n4 / name
                                                :op1 "月球")
                                            :ARG0-of (s44x10 / 背-01
                                                :ARG1 (s44p2 / planet
                                                    :name (s44n3 / name
                                                        :op1 "地球"))
                                                :quote s44x2
                                                :aspect state))))))
                        :quote s44x2
                        :aspect state))
                :unit (s44x15 / 条)
                :quant 1
                :ARG0-of (s44x16 / 惊人
                    :degree intensifier))
            :quote s44x2
            :aspect performance
            :temporal (s44d / date-entity
                :year 1987))
        :aspect performance)
    :aspect performance)


# alignment:
s44c: 0-0
s44c2: 0-0
s44d: 0-0
s44d2: 0-0
s44i3: 0-0
s44n: 0-0
s44n2: 0-0
s44n3: 0-0
s44n4: 0-0
s44n5: 0-0
s44n6: 0-0
s44p: 0-0
s44p2: 0-0
s44x: 5-5
s44x10: 24-24
s44x11: 39-39
s44x12: 35-35
s44x13: 33-33
s44x14: 38-38
s44x15: 16-16
s44x16: 18-18
s44x17: 13-13
s44x2: 6-6
s44x3: 14-14
s44x4: 20-20
s44x5: 31-31
s44x6: 29-29
s44x7: 28-28
s44x8: 28-28
s44x9: 26-26

# document level annotation:
(s44s0 / sentence
    :temporal ((document-creation-time :before s44x)
        (s44x :before s44x2)
        (document-creation-time :before s44d)
        (s44d :overlap s44x3)
        (s44x3 :overlap s44x5)
        (s44x5 :overlap s44x10))
    :modal ((root :modal author)
        (s44n :partial-affirmative s44x17)
        (author :partial-affirmative s44x8)
        (author :partial-affirmative s44n)
        (author :partial-affirmative s44x3)
        (author :partial-affirmative s44n)
        (author :full-affirmative s44x2)
        (author :full-affirmative s44n)
        (author :full-affirmative s44x)
        (author :full-affirmative s44n)
        (s44n :partial-affirmative s44x10)
        (author :partial-affirmative s44x5))
    :coref ((s40n :same-entity s44n)))

## chinese_umr-0001, sentence 45

# :: snt45
Index: 1  2  3 4 5  6   7 8  9  10 11 12 13 14 15 16
Words: 这个 消息 是 前 苏联 科学家 从 人造 卫星 发回 的  一组 照片 得知 的  。 

# sentence level graph:
(s45x / 得知-01
    :ARG0 (s45x2 / 科学家
        :place (s45c / country-region
            :name (s45n / name
                :op1 "前"
                :op2 "苏联")))
    :ARG1 (s45x3 / 消息
        :mod (s45x4 / 这个))
    :ARG2 (s45x5 / 照片
        :quant 1
        :unit (s45x6 / 组)
        :ARG1-of (s45x7 / 发回-01
            :ARG3 (s45x8 / 卫星
                :ARG0-of (s45x9 / 人造-01
                    :aspect state))
            :aspect performance
            :quote s45i2))
    :aspect performance
    :quote (s45i2 / implicit-predicate))


# alignment:
s45c: 0-0
s45i2: 0-0
s45n: 0-0
s45x: 14-14
s45x2: 6-6
s45x3: 2-2
s45x4: 1-1
s45x5: 13-13
s45x6: 12-12
s45x7: 10-10
s45x8: 9-9
s45x9: 8-8

# document level annotation:
(s45s0 / sentence
    :temporal ((document-creation-time :before s45x)
        (s45x :overlap s45x7))
    :modal ((root :modal author)
        (s45x2 :partial-affirmative s45x7)
        (author :partial-affirmative s45x)
        (author :partial-affirmative s45x2))
    :coref ((s44x17 :same-entity s45x2)
        (s44x2 :same-event s45i2)))

## chinese_umr-0001, sentence 18

# :: snt18
Index: 1 2   3 4  5   6 7  8  9 10 11 12 13 14 15 16 17 18 19 20  21  22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ，  它  在  显著 位置 刊登 一篇 「  苏联 复制 一万个 希特勒 」  。 

# sentence level graph:
(s18h / have-example-91
    :ARG1 (s18i2 / implicit-predicate)
    :ARG2 (s18x / 刊登-01
        :ARG0 (s18t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s18x2 / 位置
            :ARG0-of (s18x3 / 显著-01
                :aspect state))
        :ARG2 (s18p / publication
            :name (s18n / name
                :op1 "「"
                :op2 "苏联"
                :op3 "复制"
                :op4 "一万个"
                :op5 "希特勒"
                :op6 "」")
            :unit (s18x4 / 篇)
            :quant 1)
        :temporal (s18x5 / 争论-01
            :ARG0 (s18x6 / 世界
                :mod (s18x7 / 全))
            :ARG1 (s18x8 / 问题
                :mod (s18x9 / 道德)
                :topic (s18x10 / 人
                    :ARG1-of (s18x11 / 复制-01
                        :aspect process)))
            :aspect activity)
        :aspect performance))


# alignment:
s18h: 0-0
s18i2: 0-0
s18n: 0-0
s18p: 0-0
s18t: 0-0
s18x: 15-15
s18x10: 5-5
s18x11: 19-19
s18x2: 14-14
s18x3: 13-13
s18x4: 16-16
s18x5: 4-4
s18x6: 2-2
s18x7: 2-2
s18x8: 8-8
s18x9: 7-7

# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x)
        (s18x :overlap s18x3)
        (s18x :overlap s18x5))
    :modal ((root :modal author)
        (author :full-affirmative s18x3)
        (author :full-affirmative s18x11)
        (author :full-affirmative s18x5)
        (author :full-affirmative s18x))
    :coref ((s17x4 :same-entity s18t)))

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

## chinese_umr-0001, sentence 49

# :: snt49
Index: 1 2   3  4 5 6 7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  24 25  26 27 28 29 30 31 32 33  34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
Words: 《 大纪元 时报 》 、 《 自由 时报 》 引用 报导 ，  据  美国 世界 新闻 周报 报导 ，  传  恐怖 首脑 宾拉登 下令 八千名 身染 艾滋 的  美女 ，  专门 在  夜总会 和  酒吧 勾引 美国 大兵 ，  以  传播 世纪 绝症 给  他们 ，  以  削弱 美军 战力 。 

# sentence level graph:
(s49x / 引用-01
    :ARG0 (s49a / and
        :op1 (s49n / newspaper
            :name (s49n2 / name
                :op1 "《"
                :op2 "大纪元"
                :op3 "时报"
                :op4 "》"))
        :op2 (s49n3 / newspaper
            :name (s49n4 / name
                :op1 "《"
                :op2 "自由"
                :op3 "时报"
                :op4 "》")))
    :ARG1 (s49x2 / 报导-01
        :ARG1 (s49a2 / and
            :op1 (s49x20 / 据-02
                :ARG1 (s49x21 / 报导-01
                    :ARG0 (s49n9 / newspaper
                        :name (s49n10 / name
                            :op1 "美国"
                            :op2 "世界"
                            :op3 "新闻"
                            :op4 "周报")))
                :aspect state)
            :op2 (s49x3 / 传-01
                :ARG1 (s49x4 / 下令-01
                    :ARG0 (s49i3 / individual-person
                        :name (s49n8 / name
                            :op1 "宾拉登")
                        :ARG1-of (s49i4 / identity-91
                            :ARG2 (s49x18 / 首脑
                                :mod (s49x19 / 恐怖-01))))
                    :ARG1 (s49x5 / 美女
                        :ARG0-of (s49x6 / 勾引-01
                            :ARG1 (s49x15 / 大兵
                                :place (s49c / country
                                    :name (s49n6 / name
                                        :op1 "美国")))
                            :quote s49x2
                            :aspect process
                            :purpose (s49x7 / 传播-01
                                :ARG1 (s49x10 / 绝症
                                    :mod (s49x11 / 世纪))
                                :ARG2 (s49s / s49x13)
                                :quote s49x2
                                :aspect process
                                :purpose (s49x8 / 削弱-01
                                    :ARG1 (s49x9 / 战力
                                        :possessor (s49a3 / armed-organization
                                            :name (s49n5 / name
                                                :op1 "美军")))
                                    :quote s49x2
                                    :aspect process))
                            :mod (s49x12 / 专门)
                            :place (s49x13 / 酒吧)
                            :place (s49x14 / 夜总会))
                        :unit (s49x16 / 名)
                        :quant 8000
                        :ARG0-of (s49x17 / 染-02
                            :ARG1 (s49d / disease
                                :name (s49n7 / name
                                    :op1 "艾滋"))
                            :quote s49x2
                            :aspect process))
                    :quote s49x2
                    :aspect performance)
                :quote s49x2
                :aspect state))
        :aspect performance)
    :aspect performance)


# alignment:
s49a: 0-0
s49a2: 0-0
s49a3: 0-0
s49c: 0-0
s49d: 0-0
s49i3: 0-0
s49i4: 0-0
s49n: 0-0
s49n10: 0-0
s49n2: 0-0
s49n3: 0-0
s49n4: 0-0
s49n5: 0-0
s49n6: 0-0
s49n7: 0-0
s49n8: 0-0
s49n9: 0-0
s49s: 0-0
s49x: 10-10
s49x10: 43-43
s49x11: 42-42
s49x12: 31-31
s49x13: 35-35
s49x14: 33-33
s49x15: 38-38
s49x16: 25-25
s49x17: 26-26
s49x18: 22-22
s49x19: 21-21
s49x2: 11-11
s49x20: 13-13
s49x21: 11-11
s49x3: 20-20
s49x4: 24-24
s49x5: 29-29
s49x6: 36-36
s49x7: 41-41
s49x8: 48-48
s49x9: 50-50

# document level annotation:
(s49s0 / sentence
    :temporal ((document-creation-time :after s49x)
        (s49x2 :before s49x2)
        (s49x2 :overlap s49x20)
        (s49x20 :overlap s49x21)
        (s49x21 :overlap s49x3)
        (s49x3 :before s49x4)
        (s49x4 :overlap s49x6)
        (s49x6 :after s49x7)
        (s49x7 :after s49x8)
        (s49x7 :overlap s49x17))
    :modal ((root :modal author)
        (author :full-affirmative s49x3)
        (author :full-affirmative s49a)
        (s49a :partial-affirmative s49x10)
        (author :partial-affirmative s49x20)
        (author :partial-affirmative s49a)
        (author :partial-affirmative s49x17)
        (author :partial-affirmative s49a)
        (s49a :partial-affirmative s49x12)
        (author :partial-affirmative s49x6)
        (author :partial-affirmative s49a)
        (author :partial-affirmative s49x5)
        (author :partial-affirmative s49a)
        (author :full-affirmative s49x2)
        (author :full-affirmative s49a)
        (author :full-affirmative s49x)
        (author :full-affirmative s49a)
        (author :full-affirmative s49x20)
        (s49a :partial-affirmative s49x6)
        (author :partial-affirmative s49x7)
        (author :partial-affirmative s49x8)
        (s49a :partial-affirmative s49x17)
        (author :partial-affirmative s49x4)
        (author :partial-affirmative s49x3))
    :coref ((s44n :same-entity s49n)))

## chinese_umr-0001, sentence 5

# :: snt5
Index: 1  2 3    4 5  6 7 8  9 10 11 12 13 14 15 16 17 18
Words: 由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上  最富 创意 的  报纸 。 

# sentence level graph:
(s5x / 称为-01
    :ARG1 (s5x2 / 周报
        :mod (s5x3 / 该))
    :ARG2 (s5x4 / 报纸
        :ARG1-of (s5h / have-degree-91
            :ARG2 (s5x5 / 富-01
                :ARG1 (s5x6 / 创意)
                :aspect state)
            :ARG3 (s5x7 / 最))
        :temporal (s5x8 / 上
            :op1 (s5x9 / 历史
                :place (s5c / country
                    :name (s5n / name
                        :op1 "美国")))))
    :reason (s5x10 / 内容
        :possessor s5x2
        :mod (s5x11 / 荒诞不经))
    :aspect performance)


# alignment:
s5c: 0-0
s5h: 0-0
s5n: 0-0
s5x: 10-10
s5x10: 5-5
s5x11: 3-3
s5x2: 8-8
s5x3: 7-7
s5x4: 17-17
s5x5: 14-14
s5x6: 15-15
s5x7: 14-14
s5x8: 13-13
s5x9: 12-12

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :depends-on s5x)
        (s5x :overlap s5x5))
    :modal ((root :modal author)
        (author :full-affirmative s5x5)
        (author :full-affirmative s5x))
    :coref ((s4n :same-entity s5x2)))

## chinese_umr-0002, sentence 18

# :: snt18
Index: 1   2 3     4 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
Words: 阿贝迪 在 法尔洛菲德 的 住处 成为 警察 调查 的 重点 。  武装 警察 利用 遥控 炸药 破门 进入 房屋 。 

# sentence level graph:
(s18a / and
    :op1 (s18x / 成为-01
        :ARG0 (s18x4 / 住处
            :place (s18c / city-district
                :name (s18n2 / name
                    :op1 "法尔洛菲德"))
            :possessor (s18i2 / individual-person
                :name (s18n / name
                    :op1 "阿贝迪")))
        :ARG1 (s18x5 / 重点
            :topic-of (s18x6 / 调查-01
                :ARG0 (s18x7 / 警察)
                :aspect activity))
        :aspect performance)
    :op1 (s18c2 / consecutive
        :op1 (s18x2 / 破-02
            :ARG0 (s18x8 / 警察
                :mod (s18x12 / 武装))
            :ARG1 (s18x9 / 门)
            :instrument (s18x10 / 炸药
                :mod (s18x11 / 遥控-01))
            :aspect performance)
        :op2 (s18x3 / 进入-01
            :ARG0 s18x8
            :ARG1 (s18x13 / 房屋)
            :aspect performance)))


# alignment:
s18a: 0-0
s18c: 0-0
s18c2: 0-0
s18i2: 0-0
s18n: 0-0
s18n2: 0-0
s18x: 6-6
s18x10: 16-16
s18x11: 15-15
s18x12: 12-12
s18x13: 19-19
s18x2: 17-17
s18x3: 18-18
s18x4: 5-5
s18x5: 10-10
s18x6: 8-8
s18x7: 7-7
s18x8: 7-7
s18x9: 17-17

# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x)
        (s18x :overlap s18x6)
        (s18x6 :overlap s18x2)
        (s18x2 :overlap s18x3))
    :modal ((root :modal author)
        (author :full-affirmative s18x6)
        (author :full-affirmative s18x)
        (author :full-affirmative s18x11)
        (author :full-affirmative s18x2)
        (author :full-affirmative s18x3))
    :coref ((s12c4 :same-entity s18c)))

## chinese_umr-0011, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Words: 但 不久 ， 要求 女性 恪守 贞节 的 风俗 习惯 即 因 新文化 运动 引发 的 女性 解放 和 男女 平等 倡议 而 遭到 冲击 。

# sentence level graph:
(s10b / contrast-91
        :ARG1 (s10i / implicit)
	:ARG2 (s10x17 / 遭到-01
		:ARG0 (s10x32 / 习惯
			:mod (s10x / 风俗)
			:mod (s10x2 / 要求-02
				:ARG1 (s10x4 / 女性)
				:ARG2 (s10x5 / 恪守-01
					:ARG1 (s10x3 / 贞节)
					:aspect state)
				:aspect state))
		:ARG1 (s10x27 / 冲击-01
			:ARG1 s10x32
			:aspect performance)
		:cause (s10a3 / and
			:op1 (s10x22 / 解放-01
				:ARG1 (s10x26 / 女性)
				:ARG1-of (s10x23 / 引发-01
					:ARG0 (s10x6 / event
                                                :name (s10n2 / name
                                                        :op1 "新文化"
                                                        :op2 "运动"))
					:aspect performance)
				:aspect performance)
			:op2 (s10x19 / 倡议
				:mod (s10x20 / 平等-01
			                :ARG0 (s10x21 / 男女)
				        :aspect state)
                                :ARG1-of s10x23
				:aspect performance))
                :temporal (s10x18 / 不久)
		:aspect performance))

# alignment:
s10a3: 0-0
s10a4: 0-0
s10b: 0-0
s10x: 9-9
s10x17: 24-24
s10x18: 2-2
s10x19: 22-22
s10x2: 4-4
s10x20: 21-21
s10x21: 20-20
s10x22: 18-18
s10x23: 15-15
s10x25: 13-13
s10x26: 5-5
s10x27: 25-25
s10x3: 7-7
s10x32: 10-10
s10x4: 5-5
s10x5: 6-6
s10x6: 14-14

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10x27)
            (document-creation-time :before s10x22)
            (document-creation-time :before s10x23)
            (document-creation-time :before s10x20)
            (s10x22 :after s10x23)
            (s10x2 :depends-on s10x5))
    :modal ((root :modal author)
            (author :full-affirmative s10x27)
            (author :full-affirmative s10x23)
            (author :full-affirmative s10x22)
            (author :full-affirmative s10x5)
            (author :full-affirmative s10x2)
            (author :full-affirmative s10x20)
            (author :full-affirmative s10x17))
    :coref ()
)

## chinese_umr-0019, sentence 16

# :: snt16
Index:    1    2    3  4    5  6    7  8  9 10   11   12 13   14   15 16
Words: 教育   部门   提醒   ，  学校   在  安排   下  应  以  学生   安全   为  首要   任务   。 

# sentence level graph:
(s16x / 提醒-01
	:ARG0 (s16x2 / 部门
		:mod (s16x3 / 教育))
	:ARG1 (s16x4 / 学校)
	:ARG2 (s16x5 / 安排-01
		:instrument (s16x6 / 任务
			:mod (s16x7 / 首要)
			:ARG0-of (s16x8 / 为
				:ARG1 (s16x9 / 安全
					:mod (s16x10 / 学生))
				:aspect state))
		:aspect performance)
	:aspect performance)

# alignment:
s16x: 3-3
s16x10: 11-11
s16x2: 2-2
s16x3: 1-1
s16x4: 5-5
s16x5: 7-7
s16x6: 15-15
s16x7: 14-14
s16x8: 13-13
s16x9: 12-12

# document level annotation:
(s16s0 / sentence
	:temporal ((document-creation-time :before s16x)
		(s16x :overlap s16x5)))
	:modal ((root :modal author)
		(author :full-affirmative s16x8)
		(author :neutral-affirmative s16x5)
		(author :full-affirmative s16x)
		(root :modal author))

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

## chinese_umr-0022, sentence 10

# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Words: 一些 国家 和 地区 ， 如 中国 大陆 和 日本 ， 常 会 猎取 玳瑁 、 挖 其 巢穴 以 食用 它 的 肉 和 蛋 ， 因此 玳瑁 的 保护 有 很 大 困难 。

# sentence level graph:
(s10h / have-cause-91
	:ARG1 (s10x / 困难-01
		:ARG0 (s10x3 / 保护-01
			:ARG1 (s10a / animal
				:name (s10n / name
					:op1 "玳瑁")))
		:mod (s10x2 / 大)
		:aspect state)
	:ARG2 (s10a2 / and
		:op1 (s10x4 / 猎取-01
			:ARG0 (s10a3 / and
				:op1 (s10x6 / 国家)
				:op2 (s10x7 / 地区)
				:quant (s10x8 / 一些)
				:ARG1-of (s10h2 / have-example-91
					:ARG2 (s10a4 / and
						:op1 (s10c / country-region
							:name (s10n2 / name
								:op1 "中国大陆"))
						:op2 (s10c2 / country
							:name (s10n3 / name
								:op1 "日本")))))
			:ARG1 s10a
			:mod (s10x15 / 常)
			:aspect habitual)
		:op2 (s10x5 / 挖-01
			:ARG0 s10a3
			:ARG1 (s10x9 / 巢穴
				:possessor s10a)
			:aspect habitual)
		:purpose (s10x11 / 食用-01
			:ARG0 s10a3
			:ARG1 (s10a5 / and
				:op1 (s10x12 / 肉
					:possessor s10a)
				:op2 (s10x13 / 蛋
					:possessor s10a))
			:modal-strength full-affirmative
			:aspect process)))

# alignment:
s10a: 0-0
s10a2: 0-0
s10a3: 0-0
s10a4: 0-0
s10a5: 0-0
s10c: 0-0
s10c2: 0-0
s10h: 0-0
s10h2: 0-0
s10n: 0-0
s10n2: 0-0
s10n3: 0-0
s10x: 35-35
s10x10: 18-18
s10x11: 21-21
s10x12: 24-24
s10x13: 26-26
s10x14: 22-22
s10x15: 12-12
s10x2: 34-34
s10x3: 31-31
s10x4: 14-14
s10x5: 17-17
s10x6: 2-2
s10x7: 4-4
s10x8: 1-1
s10x9: 19-19

# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :overlap s10x)
            (document-creation-time :overlap s10x4)
            (document-creation-time :depends-on s10x5)
            (s10x5 :depends-on s10x11))
    :modal ((root :modal author)
            (author :full-affirmative s10x)
            (author :full-affirmative s10x4)
            (author :full-affirmative s10x5)
            (author :full-affirmative s10x11)
            (author :full-affirmative s10h)
            (author :unspecified s10a2)
            (author :partial-affirmative purpose)
            (purpose :full-affirmative s10x11))
    :coref ()
)

## chinese_umr-0005, sentence 1

# :: snt1
Index: 1  2 3  4  5 6 7  8  9   10 11  12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30   31 32 33 34 35  36  37
Words: 于海 ， 山东 日照 人 ， 中华 人民 共和国 军旅 指挥家 ，  国家 一级 指挥 ，  陆军 少将 军衔 ，  毕业 于  中央 音乐 学院 、  北京 大学 ，  1970 年  考入 中国 人民 解放军 军乐团 。 

# sentence level graph:
(s1a / and
    :op1 (s1i5 / identity-91
        :ARG1 (s1i3 / individual-person
            :name (s1n4 / name
                :op1 "于海"))
        :ARG2 (s1x11 / 人
            :place (s1c2 / city
                :name (s1n3 / name
                    :op1 "日照")
                :place (s1p / province
                    :name (s1n2 / name
                        :op1 "山东"))))
        :aspect state)
    :op2 (s1i6 / identity-91
        :ARG1 s1i3
        :ARG2 (s1x10 / 指挥家
            :ARG3-of (s1h3 / have-org-role-91
                :ARG2 (s1x12 / 军旅
                    :place (s1c / country
                        :name (s1n / name
                            :op1 "中华"
                            :op2 "人民"
                            :op3 "共和国")))))
        :aspect state)
    :op3 (s1i7 / identity-91
        :ARG1 s1i3
        :ARG2 (s1x6 / 指挥
            :mod (s1x7 / 国家)
            :mod (s1x8 / 一级))
        :aspect state)
    :op4 (s1i8 / implicit-predicate
        :ARG1 s1i3
        :ARG1 (s1x2 / 军衔
            :ARG1-of (s1i4 / identity-91
                :ARG2 (s1x3 / 少将
                    :mod (s1x4 / 陆军))))
        :aspect state)
    :op5 (s1x / 毕业-01
        :ARG0 s1i3
        :ARG1 (s1a2 / and
            :op1 (s1u / university
                :name (s1n5 / name
                    :op1 "中央"
                    :op2 "音乐"
                    :op3 "学院"))
            :op2 (s1u2 / university
                :name (s1n6 / name
                    :op1 "北京"
                    :op2 "大学")))
        :aspect performance)
    :op6 (s1x5 / 考入-01
        :ARG0 s1i3
        :ARG1 (s1o / organization
            :name (s1n7 / name
                :op1 "中国"
                :op2 "人民"
                :op3 "解放军"
                :op4 "军乐团"))
        :temporal (s1d2 / date-entity
            :year 1970)
        :aspect performance))


# alignment:
s1a: 0-0
s1a2: 0-0
s1c: 0-0
s1c2: 0-0
s1d2: 0-0
s1h3: 0-0
s1i3: 0-0
s1i4: 0-0
s1i5: 0-0
s1i6: 0-0
s1i7: 0-0
s1i8: 0-0
s1n: 0-0
s1n2: 0-0
s1n3: 0-0
s1n4: 0-0
s1n5: 0-0
s1n6: 0-0
s1n7: 0-0
s1o: 0-0
s1p: 0-0
s1u: 0-0
s1u2: 0-0
s1x: 21-21
s1x10: 11-11
s1x11: 5-5
s1x12: 10-10
s1x2: 19-19
s1x3: 18-18
s1x4: 17-17
s1x5: 32-32
s1x6: 15-15
s1x7: 13-13
s1x8: 14-14

# document level annotation:
(s1s0 / sentence
    :temporal ((s1i6 :overlap s1i7)
        (s1i7 :overlap s1i8)
        (s1i8 :before s1x)
        (s1d2 :overlap s1x5))
    :modal ((root :modal author)
        (author :full-affirmative s1x)
        (author :full-affirmative s1x5)
        (author :full-affirmative s1i6)
        (author :full-affirmative s1i7)
        (author :full-affirmative s1i8)))

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

## chinese_umr-0001, sentence 36

# :: snt36
Index: 1 2   3  4 5  6  7 8    9 10 11 12 13 14  15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46  47 48 49 50 51 52
Words: 《 大纪元 时报 》 引用 报导 ， 1995 年 一位 美国 天文 学家 克芬德 ·  路丁 博士 公布 了  他  的  惊人 发现 ，  声称 他  在  观察 火星 时  ，  竟  意外 地  看到 有  4  架  「  二战 」  时期 失踪 的  美国 轰炸机 在  火星 空域 编队 飞行 。 

# sentence level graph:
(s36a2 / and
    :op1 (s36x / 引用-01
        :ARG0 (s36n6 / newspaper
            :name (s36n7 / name
                :op1 "《"
                :op2 "大纪元"
                :op3 "时报"
                :op4 "》"))
        :ARG1 (s36i4 / implicit-argument)
        :aspect performance)
    :ARG1 (s36x2 / 报导-01
        :ARG0 s36n6
        :ARG1 (s36a / and
            :op1 (s36x14 / 公布-01
                :ARG0 (s36i2 / individual-person
                    :name (s36n5 / name
                        :op1 "克芬德"
                        :op2 "·"
                        :op3 "路丁"
                        :op4 "博士")
                    :ARG1-of (s36i3 / identity-91
                        :ARG2 (s36x17 / 天文学家
                            :place (s36c2 / country
                                :name (s36n4 / name
                                    :op1 "美国"))
                            :quant 1
                            :unit (s36x18 / 位))))
                :ARG1 (s36t / thing
                    :ARG1-of (s36x15 / 发现-01
                        :ARG0 s36i2
                        :aspect performance)
                    :ARG0-of (s36x16 / 惊人-01
                        :aspect state))
                :temporal (s36d2 / date-entity
                    :year 1995)
                :aspect performance
                :quote s36x2)
            :op2 (s36x3 / 声称-01
                :ARG0 s36i2
                :ARG1 (s36x4 / 看到-01
                    :ARG0 s36i2
                    :ARG1 (s36x7 / 飞行-01
                        :ARG0 (s36x10 / 轰炸机
                            :place (s36c / country
                                :name (s36n3 / name
                                    :op1 "美国"))
                            :quant 4
                            :unit (s36x11 / 架)
                            :ARG0-of (s36x12 / 失踪-01
                                :temporal (s36d / date-entity
                                    :era (s36x13 / 二战))
                                :aspect state
                                :quote s36x2))
                        :place (s36x8 / 空域
                            :part-of (s36p2 / planet
                                :name (s36n2 / name
                                    :op1 "火星")))
                        :manner (s36x9 / 编队)
                        :aspect activity
                        :quote s36x2)
                    :manner (s36x5 / 意外)
                    :temporal (s36x6 / 观察-01
                        :ARG0 (s36s / s36i2)
                        :ARG1 (s36p / planet
                            :name (s36n / name
                                :op1 "火星")))
                    :aspect performance
                    :quote s36x2)
                :quote s36x2
                :aspect performance))
        :aspect performance))


# alignment:
s36a: 0-0
s36a2: 0-0
s36c: 0-0
s36c2: 0-0
s36d: 0-0
s36d2: 0-0
s36i2: 0-0
s36i3: 0-0
s36i4: 0-0
s36n: 0-0
s36n2: 0-0
s36n3: 0-0
s36n4: 0-0
s36n5: 0-0
s36n6: 0-0
s36n7: 0-0
s36p: 0-0
s36p2: 0-0
s36s: 0-0
s36t: 0-0
s36x: 5-5
s36x10: 46-46
s36x11: 38-38
s36x12: 43-43
s36x13: 40-40
s36x14: 18-18
s36x15: 23-23
s36x16: 22-22
s36x17: 12-12
s36x18: 10-10
s36x2: 6-6
s36x3: 25-25
s36x4: 35-35
s36x5: 33-33
s36x6: 28-28
s36x7: 51-51
s36x8: 49-49
s36x9: 50-50

# document level annotation:
(s36s0 / sentence
    :temporal ((document-creation-time :before s36x)
        (s36x :before s36x2)
        (s36x2 :overlap s36x3)
        (s36x3 :before s36x17)
        (s36x17 :overlap s36x18)
        (s36x3 :overlap s36x4)
        (s36x4 :before s36x7)
        (s36x7 :before s36x11)
        (s36x7 :overlap s36x16))
    :modal ((root :modal author)
        (s36n :partial-affirmative s36x3)
        (author :full-affirmative s36x11)
        (author :full-affirmative s36n)
        (author :partial-affirmative s36x8)
        (author :partial-affirmative s36n)
        (author :partial-affirmative s36x7)
        (author :partial-affirmative s36n)
        (s36n :partial-affirmative s36x4)
        (author :full-affirmative s36x2)
        (author :full-affirmative s36n)
        (author :full-affirmative s36x)
        (author :full-affirmative s36n)
        (author :full-affirmative s36x17)
        (author :full-affirmative s36x18))
    :coref ((s34n :same-entity s36n)))

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

## chinese_umr-0004, sentence 45

# :: snt45
Index: 1  2 3  4  5 6 7  8 9  10   11 12 13 14 15  16 17   18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Words: 比如 在 剧中 胡佛 村 可 清楚 地 看到 帝国大厦 的  正面 ，  而  事实上 ，  中央公园 与  这  大厦 的  距离 为  2  公里 左右 ，  故  这  设定 是  错  的  。 

# sentence level graph:
(s45i2 / implicit-argument
    :example (s45a / and
        :op1 (s45h / have-reason-91
            :ARG1 (s45a2 / and
                :op1 (s45x / 看到-01
                    :ARG1 (s45x2 / 正面
                        :part-of (s45b / building
                            :name (s45n / name
                                :op1 "帝国大厦")))
                    :place (s45c / city-district
                        :name (s45n2 / name
                            :op1 "胡佛"
                            :op2 "村"))
                    :place (s45x3 / 中
                        :op1 (s45x4 / 剧))
                    :aspect state)
                :op2 (s45b2 / but-91
                    :ARG2 (s45x5 / 距离-01
                        :ARG0 (s45a3 / and
                            :op1 (s45p / park
                                :name (s45n3 / name
                                    :op1 "中央公园"))
                            :op2 s45b)
                        :ARG1 (s45x6 / 左右
                            :op1 (s45d / distance-quantity
                                :value 2
                                :unit (s45x7 / 公里)))
                        :mod (s45x11 / 事实上)
                        :aspect state)))
            :ARG2 (s45x8 / 错-01
                :ARG0 (s45x9 / 设定
                    :mod (s45x10 / 这))
                :aspect state)
            :aspect state)))


# alignment:
s45a: 0-0
s45a2: 0-0
s45a3: 0-0
s45b: 0-0
s45b2: 0-0
s45c: 0-0
s45d: 0-0
s45h: 0-0
s45i2: 0-0
s45n: 0-0
s45n2: 0-0
s45n3: 0-0
s45p: 0-0
s45x: 9-9
s45x10: 19-19
s45x11: 15-15
s45x2: 12-12
s45x3: 3-3
s45x4: 3-3
s45x5: 22-22
s45x6: 26-26
s45x7: 25-25
s45x8: 32-32
s45x9: 30-30

# document level annotation:
(s45s0 / sentence
    :temporal ((document-creation-time :before s46x)
        (s46x :overlap s46x3))
    :modal ((root :modal author)
        (author :neutral-affirmative s45x)
        (author :full-affirmative s45x5)
        (author :full-affirmative s45x8)
        (author :full-affirmative s45h))
    :coref ((s40b :same-entity s45b)
        (s43c2 :same-entity s45c)
        (s41p :same-entity s45p)))

## chinese_umr-0025, sentence 101

# :: snt101
Index:    1  2  3  4    5  6    7  8  9   10 11 12 13 14 15   16 17 18   19 20 21   22 23 24   25 26 27   28 29   30 31 32 33 34 35 36 37 38 39 40 41 42   43 44 45
Words: 例如   ，  当  他  第一   次  瞅见   我  的  飞机   时  （  我  就  不  画出   我  的  飞机   了  ，  因为   这  种  图画   对  我  来说   太  复杂   ）  ，  他  问  我  道  ：  “  这  是  个  啥  玩艺   ？  ” 

# sentence level graph:
(s101x1 / 例如
	:ARG0 (s101x34 / 问道-01
		:ARG2 (s101x35 / individual-person
			:refer-person 1
			:refer-number singular)
		:ARG1 (s101x43 / 玩艺
			:mod (s101x52 / amr-unknown)
			:unit (s101x41 / 个)
			:mode interrogative)
		:ARG1 (s101y1 / identity-91
			:ARG0 (s101x39 / 这)
			:ARG1 s101x43)
		:temporal (s101x7 / 瞅见-01
			:ARG0 (s101x4 / individual-person
				:refer-person 3
				:refer-number singular)
			:ord (s101x58 / ordinal-entity
				:value 1
				:unit (s101x6 / 次))
			:ARG1 (s101x10 / 飞机
				:possessor-of (s101x8 / individual-person
					:refer-person 1
					:refer-number singular)
				:ARG0-of (s101x63 / mean
					:ARG1 (s101x64 / causation
						:ARG2 (s101x16 / 画出-01
							:ARG0 (s101x13 / individual-person
								:refer-person 1
								:refer-number singular)
							:modal-strength (s101x79 / full-negative)
							:polarity -
							:ARG1 (s101x19 / 飞机
								:possessor-of (s101x17 / individual-person
									:refer-person 1
									:refer-number singular))
							:smood (s101x20 / 了))
						:ARG1 (s101x28 / 来说
							:ARG0 (s101x25 / 图画
								:mod (s101x23 / 这)
								:unit (s101x24 / 种))
							:ARG1 (s101x27 / individual-person
								:refer-person 1
								:refer-number singular)
							:ARG2 (s101x30 / 复杂-01
								:degree (s101x29 / 太)
								:ARG0 s101x25))))))
		:ARG0 (s101x33 / individual-person
			:refer-person 3
			:refer-number singular)
		:modal-strength (s101x80 / full-affirmative)))

# alignment:
s101x1: 1-1
s101x10: 10-10
s101x13: 0-0
s101x16: 16-16
s101x17: 0-0
s101x19: 10-10
s101x20: 20-20
s101x23: 23-23
s101x24: 24-24
s101x25: 25-25
s101x27: 0-0
s101x28: 28-28
s101x29: 29-29
s101x30: 30-30
s101x33: 0-0
s101x34: 34-34
s101x35: 0-0
s101x39: 23-23
s101x4: 0-0
s101x41: 41-41
s101x43: 43-43
s101x52: 0-0
s101x58: 0-0
s101x6: 6-6
s101x63: 0-0
s101x64: 0-0
s101x7: 7-7
s101x79: 0-0
s101x8: 0-0
s101x80: 0-0
s101y1: 0-0

# document level annotation:
(s101s0 / sentence)

## chinese_umr-0001, sentence 46

# :: snt46
Index: 1 2  3  4 5 6   7 8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
Words: 据 照片 显示 ， 这 架飞机 的 机身 和 机翼 上  有  明显 的  美国 空军 标志 ，  飞机 的  有些 地方 已  被  陨石 破坏 ，  但  机体 依然 完好 。 

# sentence level graph:
(s46x / 显示-01
    :ARG0 (s46x2 / 照片)
    :ARG1 (s46a / and
        :op1 (s46e / exist-91
            :ARG0 (s46a2 / and
                :op1 (s46x3 / 上
                    :op1 (s46x5 / 机身
                        :part-of (s46x6 / 飞机
                            :mod (s46x7 / 这)
                            :unit (s46x8 / 架))))
                :op2 (s46x4 / 上
                    :op1 (s46x9 / 机翼
                        :part-of s46x6)))
            :ARG1 (s46x17 / 标志
                :topic (s46a3 / armed-organization
                    :name (s46n / name
                        :op1 "美国"
                        :op2 "空军")))
            :aspect state
            :quote s46i2)
        :op2 (s46b / but-91
            :ARG1 (s46x14 / 完好-01
                :ARG0 (s46x15 / 机体)
                :mod (s46x16 / 依然)
                :aspect state
                :quote s46i2)
            :ARG2 (s46x10 / 破坏-01
                :ARG0 (s46x11 / 陨石)
                :ARG1 (s46x12 / 地方
                    :quant (s46x13 / 有些)
                    :part-of s46x6)
                :aspect performance
                :quote s46i2)))
    :aspect state
    :quote (s46i2 / implicit-predicate))


# alignment:
s46a: 0-0
s46a2: 0-0
s46a3: 0-0
s46b: 0-0
s46e: 0-0
s46i2: 0-0
s46n: 0-0
s46x: 3-3
s46x10: 26-26
s46x11: 25-25
s46x12: 22-22
s46x13: 21-21
s46x14: 31-31
s46x15: 29-29
s46x16: 30-30
s46x17: 17-17
s46x2: 2-2
s46x3: 11-11
s46x4: 11-11
s46x5: 8-8
s46x6: 19-19
s46x7: 5-5
s46x8: 6-6
s46x9: 10-10

# document level annotation:
(s46s0 / sentence
    :temporal ((document-creation-time :before s46x)
        (s46x :overlap s46e)
        (s46x :overlap s46x14)
        (s46x14 :before s46x10))
    :modal ((root :modal author)
        (s46x2 :partial-affirmative s46e)
        (author :partial-affirmative s46x14)
        (author :partial-affirmative s46x2)
        (author :partial-affirmative s46x10)
        (author :partial-affirmative s46x2)
        (author :partial-affirmative s46x)
        (author :partial-affirmative s46x2))
    :coref ((s45x5 :same-entity s46x2)
        (s44x11 :same-entity s46x6)
        (s45i2 :same-event s46i2)))

## chinese_umr-0021, sentence 2

# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
Words: 新月 当天 （ 即 朔日 ）， 地球 上 观测 到 月球 和 太阳 的 角 距离 极小 ， 此时 月球 如果 恰好 在 月球 交点 附近 ， 穿过 太阳 和 地球 之间 ， 与 地球 、 太阳 接近 一直线 ， 则 会 出现 日食 。

# sentence level graph:
(s2a5 / and
	:op1 (s2x7 / 观测-01
		:ARG1 (s2x8 / 角-距离
			:mod (s2x11 / 极小)
			:mod (s2a3 / and
				:op1 (s2p7 / planet
					:name (s2n3 / name
						:op1 "月球"))
				:op2 (s2p4 / planet
					:name (s2n / name
						:op1 "太阳"))))
		:place (s2p / planet
			:name (s2n4 / name
				:op1 "地球"))
		:temporal (s2x5 / 新月
			:mod (s2x6 / 当天))
		:aspect performance)
	:op2 (s2h / have-condition-91
		:ARG1 (s2x / 出现-01
			:ARG1 (s2x2 / 日食)
			:aspect performance)
		:ARG2 (s2a / and
			:op1 (s2h2 / have-place-91
				:ARG1 s2p7
				:ARG2 (s2x13 / 附近
					:op1 (s2x12 / 交点
						:possessor s2p7))
				:manner (s2x16 / 恰好)
				:aspect state)
			:op2 (s2x3 / 穿过-01
				:ARG0 s2p7
				:ARG1 (s2x4 / 之间
					:op1 s2p4
					:op2 s2p)
				:aspect performance)
			:op3 (s2x9 / 接近-03
				:ARG0 (s2a4 / and
					:op1 s2p7
					:op2 s2p4
					:op3 s2p)
				:ARG1 (s2x10 / 直线
					:quant 1)
				:aspect state)
			:temporal s2x5)))

# alignment:
s2a: 0-0
s2a3: 0-0
s2a4: 0-0
s2h: 0-0
s2n: 0-0
s2n3: 0-0
s2n4: 0-0
s2p: 0-0
s2p4: 0-0
s2p5: 0-0
s2p7: 0-0
s2x: 43-43
s2x10: 39-39
s2x11: 17-17
s2x12: 25-25
s2x13: 26-26
s2x15: 11-11
s2x2: 44-44
s2x3: 28-28
s2x4: 32-32
s2x5: 1-1
s2x6: 2-2
s2x7: 9-9
s2x8: 15-15
s2x9: 38-38

# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x)
            (s2x3 :overlap s2x9)
            (s2x :before s2x3)
            (s2x :before s2x9)
            (s2x3 :overlap s2h2))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :full-affirmative s2x3)
            (author :full-affirmative s2x9)
            (author :full-affirmative s2x7)
            (author :full-affirmative s2h2))
    :coref ()
)

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

## chinese_umr-0001, sentence 47

# :: snt47
Index: 1  2 3    4 5 6 7 8  9  10 11 12  13 14 15 16 17 18 19  20 21   22
Words: 然而 ， 1988 年 7 月 ， 这架 飞机 竟然 从  月球山 神秘 地  消失 了  ，  令  科学家 们  大惑不解 。 

# sentence level graph:
(s47b / but-91
    :ARG1 (s47x / 消失-01
        :ARG0 (s47x2 / 飞机
            :mod (s47x3 / 这)
            :unit (s47x4 / 机))
        :place (s47x5 / 山
            :place (s47p / planet
                :name (s47n / name
                    :op1 "月球")))
        :manner (s47x6 / 神秘)
        :mod (s47x7 / 竟然)
        :cause-of (s47x8 / 大惑不解-01
            :ARG0 (s47x9 / 科学家
                :refer-number plural)
            :aspect state
            :quote s47i2)
        :temporal (s47d / date-entity
            :year 1988
            :month 7)
        :aspect performance
        :quote (s47i2 / implicit-predicate)))


# alignment:
s47b: 0-0
s47d: 0-0
s47i2: 0-0
s47n: 0-0
s47p: 0-0
s47x: 15-15
s47x2: 9-9
s47x3: 8-8
s47x4: 9-9
s47x5: 12-12
s47x6: 13-13
s47x7: 10-10
s47x8: 21-21
s47x9: 19-19

# document level annotation:
(s47s0 / sentence
    :temporal ((document-creation-time :before s47d)
        (s47d :before s47x)
        (s47x :after s47x8))
    :modal ((root :modal author)
        (s47x2 :partial-affirmative s47x8)
        (author :partial-affirmative s47x)
        (author :partial-affirmative s47x2))
    :coref ((s46x6 :same-entity s47x2)
        (s46i2 :same-event s47i2)))

## chinese_umr-0021, sentence 7

# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
Words: 本次 日食 开始 时 ， 月球 本影 在 库克 群岛 波凯莱凯莱岛 西北 约 130 公里 处 的 太平洋 最先 接触 地表 ， 当地 在 日出 时 最先 看到 日全食 。

# sentence level graph:
(s7a / and
	:op1 (s7x / 接触-01
		:ARG0 (s7x16 / 本影
			:possessor (s7p / planet
				:name (s7n / name
					:op1 "月球")))
		:ARG1 (s7x3 / 地表)
		:place (s7x17 / 处
			:part-of (s7l / ocean
				:name (s7n5 / name
					:op1 "太平洋"))
			:direction (s7x2 / 西北
				:op1 (s7i2 / island
					:name (s7n3 / name
						:op1 "波凯莱凯莱岛")
					:part-of (s7i3 / country
						:name (s7n4 / name
							:op1 "库克"
							:op2 "群岛"))))
			:extent (s7d / distance-quantity
				:mod (s7x11 / 约)
				:quant 130
				:unit (s7x12 / 公里)))
		:temporal (s7x6 / 开始-01
			:ARG0 (s7x7 / 日食
				:mod (s7x8 / 本次))
			:aspect performance)
		:aspect performance
		:mod (s7x14 / 最先))
	:op2 (s7x4 / 看到-01
		:ARG1 (s7x5 / 日全食)
		:place (s7x15 / 当地)
		:temporal (s7t / 日出)
		:mod (s7x18 / 最先)
		:aspect performance))

# alignment:
s7c: 0-0
s7d: 0-0
s7i2: 0-0
s7i3: 0-0
s7l: 18-18
s7n: 0-0
s7n3: 0-0
s7n4: 0-0
s7p: 0-0
s7t: 25-25
s7x: 20-20
s7x11: 13-13
s7x12: 15-15
s7x14: 19-19
s7x15: 23-23
s7x16: 7-7
s7x2: 12-12
s7x3: 21-21
s7x4: 28-28
s7x5: 29-29
s7x6: 3-3
s7x7: 2-2
s7x8: 1-1

# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :before s7x)
            (s7x :overlap s7x4)
            (s7x4 :before s7x6))
    :modal ((root :modal author)
            (author :full-affirmative s7x)
            (author :full-affirmative s7x4)
            (author :full-affirmative s7x6))
    :coref ()
)

## chinese_umr-0033, sentence 9

# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
Words: 被指 是 制造商 的 台湾 公司 金 阿波罗 ， 坚决 否认 生产 涉事 设备 ， 另 指 匈牙利 合作 伙伴 获准 使用 金 阿波罗 商标

# sentence level graph:
(s9a / and
    :op1 (s9x / 否认-01
        :ARG0 (s9c3 / company
            :name (s9n3 / name
                :op1 "金"
                :op2 "阿波罗")
            :place (s9c / country
                :name (s9n / name
                    :op1 "台湾"))
            :ARG1-of (s9i2 / identity-91
                :ARG2 (s9x6 / 制造商)
                :ARG1-of (s9x5 / 指-02
                    :aspect performance)
                :aspect state))
        :ARG1 (s9x2 / 生产-01
            :ARG0 s9c3
            :ARG1 (s9x3 / 设备
                :mod (s9x4 / 涉事))
            :aspect performance)
        :manner (s9x19 / 坚决)
        :aspect performance)
    :op2 (s9x7 / 指-02
        :ARG0 s9c3
        :ARG1 (s9x10 / 获准-01
            :ARG0 (s9x9 / 伙伴
                :mod (s9x13 / 合作)
                :place (s9c2 / country
                    :name (s9n2 / name
                        :op1 "匈牙利")))
            :ARG1 (s9x11 / 使用-01
                :ARG0 s9x9
                :ARG1 (s9x12 / 商标
                    :possessor s9c3)
                :aspect activity)
            :aspect performance)
        :mod (s9x8 / 另)
        :aspect performance))

# alignment:
s9a: 0-0
s9c: 5-5
s9c2: 18-18
s9c3: 7-24
s9i2: 0-0
s9n: 0-0
s9n2: 0-0
s9n3: 0-0
s9x: 11-11
s9x10: 21-21
s9x11: 22-22
s9x12: 25-25
s9x13: 19-19
s9x19: 10-10
s9x2: 12-12
s9x3: 14-14
s9x4: 13-13
s9x5: 17-17
s9x6: 3-3
s9x7: 17-17
s9x8: 16-16
s9x9: 20-20

# document level annotation:
(s9s0 / sentence
    :temporal ((s9x10 :before s9x2)
            (s9x11 :before s9x10)
            (s9x :before s9x5)
            (s9x :before s9x2)
            (s9x7 :before s9x))
    :modal ((root :modal author)
            (author :full-affirmative s9x)
            (author :full-affirmative s9x5)
            (author :full-affirmative s9x7)
            (author :full-affirmative s9c3)
            (s9c3 :full-negative s9x2)
            (s9c3 :full-affirmative s9x10)
            (s9c3 :neutral-affirmative s9x11))
    :coref ((s8x4 :same-entity s9x3))
)

## chinese_umr-0015, sentence 16

# :: snt16
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Words: 教育 部门 提醒 ， 学校 在 安排 下 应 以 学生 安全 为 首要 任务 。

# sentence level graph:
(s16x / 提醒-01
    :ARG0 (s16x2 / 部门
        :mod (s16x3 / 教育))
    :ARG1 (s16x5 / 学校)
    :ARG2 (s16x12 / 安排-01
        :ARG0 s16x5
        :manner (s16i2 / identity-91
            :ARG1 (s16x9 / 安全
                :possessor (s16x13 / 学生))
            :ARG2 (s16x14 / 任务
                :mod (s16x15 / 首要))
            :aspect state)
        :aspect activity)
    :aspect performance)

# alignment:
s16h: 0-0
s16i2: 0-0
s16x: 3-3
s16x12: 7-7
s16x13: 11-11
s16x14: 15-15
s16x15: 14-14
s16x2: 2-2
s16x3: 1-1
s16x5: 5-5
s16x9: 12-12

# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16x)
            (s16x :after s16x12))
    :modal ((root :modal author)
            (author :full-affirmative s16x)
            (author :full-affirmative s16x2)
            (s16x2 :partial-affirmative s16i2)
            (s16x2 :partial-affirmative s16x12))
    :coref ()
)

## chinese_umr-0012, sentence 6

# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
Words: 同时 为了 缓解 压力 ， 作为 维基百科 编者 的 他 于 维基百科 的 工作 也 一点 没 落下 ， 成功 完成 了 他 在 美国 专题 的 目标 计划 。

# sentence level graph:
(s6a / and
	:op1 (s6x / 落下-03
		:ARG0 (s6x6 / person
			:refer-person 3rd
			:refer-number singular
			:ARG1-of (s6h / have-role-91
				:ARG2 (s6x7 / 编者
					:mod (s6x8 / website
						:name (s6n2 / name
							:op1 "维基百科")))
				:aspect state))
		:ARG1 (s6w2 / 工作
			:mod s6x8)
		:degree (s6x2 / 一点)
		:polarity -
		:aspect performance
		:purpose (s6x5 / 缓解-01
			:ARG0 s6x6
			:ARG1 (s6y / 压力)
			:aspect performance))
	:op2 (s6x3 / 完成-01
		:ARG0 s6x6
		:ARG1 (s6g / 计划
			:mod (s6g2 / 目标)
			:possessor s6x6
			:topic (s6t / 专题
				:mod (s6c / country
					:name (s6n / name
						:op1 "美国"))))
		:manner (s6x4 / 成功)
		:aspect performance
		:purpose s6x5)
	:temporal (s6t2 / 同时))

# alignment:
s6a: 0-0
s6c: 0-0
s6g: 29-29
s6g2: 28-28
s6n: 0-0
s6t: 26-26
s6t2: 1-1
s6w2: 14-14
s6w3: 7-7
s6x: 18-18
s6x2: 16-16
s6x3: 21-21
s6x4: 20-20
s6x5: 3-3
s6x6: 10-10
s6x7: 8-8
s6x8: 7-7
s6y: 4-4

# document level annotation:
(s6s0 / sentence
    :temporal ((s5x3 :overlap s6t2)
            (s6t2 :overlap s6x)
            (s6t2 :overlap s6x3)
            (s6x :overlap s6h)
            (s6x :overlap s6x5))
    :modal ((root :modal author)
            (author :full-negative s6x)
            (author :full-affirmative s6x3)
            (s6x6 :partial-affirmative purpose)
            (purpose :full-affirmative s6x5)
            (author :full-affirmative s6h)
            (author :full-affirmative s6x6))
    :coref ((s5i2 :same-entity s6x6))
)

## chinese_umr-0016, sentence 14

# :: snt14
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79
Words: 政府 清晨 五时半 宣布 启动 “极端 状况 ” ， 要求 所有 学校 停课 ， 但 只 “ 呼吁 ” 雇主 要 “ 参考 ” 台风 情况 作 弹性 工作 安排 ， 直至 早上 七时 许 才 另发 指引 指 不 应 要求 必要 人员 外 的 雇员 返回 工作 地点 。 当局 解释 指引 是 “ 补充 资料 ” ， 又 指 机制 行之有效 ， 没有 正面 回应 为何 不 在 启动 极端 情况 时 一并 作出 要求 。

# sentence level graph:
(s14m / multi-sentence
    :op1 (s14a3 / and
        :op1 (s14x / 宣布-01
            :ARG0 (s14x9 / 政府)
            :ARG1 (s14x4 / 启动-01
                :ARG1 (s14x7 / 状况
                    :mod (s14x8 / 极端))
                :aspect performance)
            :temporal (s14d / date-entity
                :dayperiod (s14x2 / 清晨)
                :time (s14x3 / 05h30m))
            :aspect performance)
        :op2 (s14b / contrast-91
            :ARG1 (s14x5 / 要求-02
                :ARG0 s14x9
                :ARG1 (s14x10 / 学校
                    :quant (s14x11 / 所有))
                :ARG2 (s14x6 / 停课-01
                    :ARG0 s14x10
                    :modal-strength partial-affirmative
                    :aspect performance)
                :aspect performance)
            :ARG2 (s14x12 / 呼吁-01
                :ARG0 s14x9
                :ARG1 (s14x47 / 雇主)
                :ARG2 (s14x17 / 参考-01
                    :ARG0 s14x47
                    :ARG1 (s14x22 / 情况
                        :possessor (s14x23 / 台风))
                    :ARG2 (s14x18 / 作-01
                        :ARG0 s14x47
                        :ARG1 (s14x19 / 安排-01
                            :ARG1 (s14x20 / 工作-01
                                :aspect process)
                            :mod (s14x21 / 弹性)
                            :aspect process)
                        :aspect performance)
                    :modal-strength partial-affirmative
                    :aspect performance)
                :aspect performance))
        :op3 (s14x24 / 发-01
            :ARG0 s14x9
            :ARG1 (s14x25 / 指引
                :ARG0-of (s14i3 / say-91
                    :ARG1 (s14x27 / 要求-02
                        :ARG0 s14x47
                        :ARG1 (s14x31 / 雇员
                            :subtraction (s14x32 / 人员
                                :mod (s14x33 / 必要)))
                        :ARG2 (s14x28 / 返回-01
                            :ARG0 s14x31
                            :ARG1 (s14x29 / 地点
                                :place-of (s14x26 / 工作-01
                                    :aspect habitual))
                            :aspect performance)
                        :modal-strength partial-negative
                        :aspect state)))
            :aspect performance
            :mod (s14x30 / 另)
            :temporal (s14x48 / 直至
                :op1 (s14d2 / date-entity
                    :time (s14x49 / 许
                        :op1 (s14x50 / 07h00m))
                    :dayperiod (s14x51 / 早上)))))
    :op2 (s14a4 / and
        :op1 (s14x13 / 解释-01
            :ARG0 (s14x34 / 当局)
            :ARG3 (s14i2 / identity-91
                :ARG1 s14x25
                :ARG2 (s14x36 / 资料
                    :mod (s14x37 / 补充))
                :aspect state)
            :aspect state)
        :op2 (s14x14 / 指-02
            :ARG0 s14x34
            :ARG1 (s14x38 / 行之有效-01
                :ARG0 (s14x39 / 机制)
                :aspect state)
            :aspect state)
        :op3 (s14x15 / 回应-01
            :ARG0 s14x34
            :ARG2 (s14u / umr-unknown
                :ARG2-of (s14h / have-reason-91
                    :ARG1 (s14x35 / 作出-01
                        :ARG1 (s14x45 / 要求-02)
                        :aspect performance
                        :polarity -
                        :temporal (s14x41 / 启动-01
                            :ARG0 s14x34
                            :ARG1 (s14x42 / 情况
                                :mod (s14x43 / 极端))
                            :aspect performance)
                        :manner (s14x44 / 一并))))
            :manner (s14x40 / 正面)
            :polarity -
            :aspect performance)))

# alignment:
s14a3: 0-0
s14a4: 0-0
s14b: 0-0
s14d: 0-0
s14d2: 0-0
s14h: 0-0
s14i2: 0-0
s14i3: 0-0
s14m: 0-0
s14u: 0-0
s14x: 4-4
s14x10: 12-12
s14x11: 11-11
s14x12: 18-18
s14x13: 53-53
s14x14: 39-39
s14x15: 68-68
s14x16: 20-20
s14x17: 23-23
s14x18: 27-27
s14x19: 30-30
s14x2: 2-2
s14x20: 29-29
s14x21: 28-28
s14x22: 26-26
s14x23: 25-25
s14x24: 37-37
s14x25: 38-38
s14x26: 29-29
s14x27: 10-10
s14x28: 48-48
s14x29: 50-50
s14x3: 0-0
s14x30: 37-37
s14x31: 47-47
s14x32: 44-44
s14x33: 43-43
s14x34: 52-52
s14x35: 77-77
s14x36: 58-58
s14x37: 57-57
s14x38: 64-64
s14x39: 63-63
s14x4: 5-5
s14x40: 67-67
s14x41: 5-5
s14x42: 26-26
s14x43: 73-73
s14x44: 76-76
s14x45: 10-10
s14x47: 20-20
s14x48: 32-32
s14x49: 35-35
s14x5: 10-10
s14x50: 0-0
s14x51: 33-33
s14x6: 13-13
s14x7: 7-7
s14x8: 73-73
s14x9: 1-1

# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14d)
            (s14d :contained s14x)
            (s14x :after s14x4)
            (s14x :overlap s14x5)
            (s14x5 :after s14x6)
            (s14x5 :overlap s14x12)
            (s14x12 :after s14x17)
            (s14x17 :after s14x18)
            (s14x18 :after s14x20)
            (s14x18 :overlap s14x19)
            (s14d :after s14d2)
            (s14d2 :contained s14x24)
            (s14x24 :overlap s14x27)
            (s14x27 :overlap s14x26)
            (s14x24 :after s14x28)
            (s14x24 :after s14x13)
            (s14x13 :overlap s14x14)
            (s14x14 :overlap s14x38)
            (s14x14 :overlap s14x15)
            (s14x15 :before s14x41)
            (s14x41 :overlap s14x35)
            (s14x35 :overlap s14x45))
    :modal ((root :modal author)
            (author :full-affirmative s14x4)
            (author :full-affirmative s14x)
            (author :full-affirmative s14
… (949 more characters)

## chinese_umr-0014, sentence 12

# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 方济各 于 2013 年 当选 教宗 ， 他 一直 试图 通过 改变 某些 道德 教义 来 吸引 性 少数 群体 进入 教会 。

# sentence level graph:
(s12a / and
    :op1 (s12x / 当选-01
        :ARG0 (s12p / person
            :name (s12n / name
                :op1 "方济各"))
        :ARG1 (s12x4 / 教宗)
        :temporal (s12d / date-entity
            :year 2013)
        :aspect performance)
    :op2 (s12x2 / 试图-01
        :ARG0 s12p
        :ARG1 (s12x3 / 吸引-01
            :ARG1 (s12x5 / 群体
                :mod (s12s / 性
                    :mod (s12s2 / 少数))
                :ARG0-of (s12e / 进入-01
                    :ARG1 (s12x6 / 教会)
                    :aspect performance))
            :manner (s12c2 / 改变-01
                :ARG0 s12p
                :ARG1 (s12d2 / 教义
                    :mod (s12m / 道德)
                    :mod (s12q / 某些))
                :aspect performance)
            :aspect habitual)
        :temporal (s12t / 一直)
        :aspect habitual))

# alignment:
s12a: 0-0
s12c2: 12-12
s12d: 0-0
s12d2: 15-15
s12e: 21-21
s12m: 14-14
s12n: 0-0
s12p: 0-0
s12q: 13-13
s12s: 18-18
s12s2: 19-19
s12t: 9-9
s12x: 5-5
s12x2: 10-10
s12x3: 17-17
s12x4: 6-6
s12x5: 20-20
s12x6: 22-22

# document level annotation:
(s12s0 / sentence)

## chinese_umr-0014, sentence 3

# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 教宗 方济各 宣布 ， 神父 将 被 允许 在 某些 情况 下 为 同性 伴侣 祝福 ， 这 对 罗马 天主教会 中 的 同性恋 社区 具有 重要 意义 。

# sentence level graph:
(s3x / 宣布-01
	:ARG0 (s3p / person
		:name (s3n / name
			:op1 "方济各")
		:ARG1-of (s3h / have-org-role-92
			:ARG2 (s3x12 / religious-organization
				:name (s3n2 / name
					:op1 "罗马"
					:op2 "天主教会"))
			:ARG3 (s3x2 / 教宗)
			:aspect state))
	:ARG1 (s3x3 / 允许-01
		:ARG1 (s3x5 / 神父)
		:ARG2 (s3x4 / 祝福-01
			:ARG0 s3x5
			:ARG1 (s3x6 / 伴侣
				:mod (s3x7 / 同性))
			:condition (s3x8 / 情况
				:mod (s3x9 / 某些))
			:aspect performance)
		:ARG0-of (s3x10 / 具有-01
			:ARG1 (s3x15 / 意义
				:mod (s3x16 / 重要))
			:aspect state
			:affectee (s3x11 / 社区
				:part-of s3x12
				:mod (s3x14 / 同性恋)))
		:aspect state)
	:aspect performance)

# alignment:
s3h: 0-0
s3n: 0-0
s3p: 0-0
s3x: 3-3
s3x10: 26-26
s3x11: 25-25
s3x12: 21-21
s3x13: 20-20
s3x14: 24-24
s3x15: 28-28
s3x16: 27-27
s3x2: 1-1
s3x3: 8-8
s3x4: 16-16
s3x5: 5-5
s3x6: 15-15
s3x7: 14-14
s3x8: 11-11
s3x9: 10-10

# document level annotation:
(s3s0 / sentence
    :temporal ()
    :modal ((root :modal author)
            (author :full-affirmative s3x)
            (author :full-affirmative s3p)
            (s3p :full-affirmative s3x3)
            (s3p :neutral-affirmative s3x4)
            (author :full-affirmative s3x10))
    :coref ()
)

## chinese_umr-0025, sentence 928

# :: snt928
Index: 1  2  3  4    5  6    7  8  9   10   11   12 13
Words: “ 你  是  个  奇怪   的  动物   ，  小  王子   终于   说道   。 

# sentence level graph:
(s928x12 / 说道-01
	:ARG0 (s928x10 / 王子
		:mod (s928x9 / 小))
	:mod (s928x11 / 终于)
	:ARG1 (s928x7 / 动物
		:mod (s928x5 / 奇怪)
		:unit (s928x4 / 个))
	:ARG1 (s928y1 / identity-91
		:ARG0 (s928x2 / individual-person
			:refer-person 2
			:refer-number singular)
		:ARG1 s928x7)
	:modal-strength (s928x24 / full-affirmative))

# alignment:
s928x10: 10-10
s928x11: 11-11
s928x12: 12-12
s928x2: 0-0
s928x24: 0-0
s928x4: 4-4
s928x5: 5-5
s928x7: 7-7
s928x9: 9-9
s928y1: 0-0

# document level annotation:
(s928s0 / sentence)

## chinese_umr-0007, sentence 28

# :: snt28
Index: 1  2 3 4   5  6  7 8 9  10 11 12 13 14
Words: 可是 ， 在 金田一 进入 公馆 后 ， 矿工 便  包围 了  公馆 。 

# sentence level graph:
(s28b / but-91
    :ARG2 (s28x / 包围-01
        :ARG0 (s28x2 / 矿工)
        :ARG1 (s28x3 / 公馆)
        :mod (s28x4 / 便)
        :temporal (s28x5 / 后
            :op1 (s28x6 / 进入-01
                :ARG0 (s28i2 / individual-person
                    :name (s28n / name
                        :op1 "金田一"))
                :ARG1 s28x3
                :aspect performance))
        :aspect performance))


# alignment:
s28b: 0-0
s28i2: 0-0
s28n: 0-0
s28x: 11-11
s28x2: 9-9
s28x3: 6-6
s28x4: 10-10
s28x5: 7-7
s28x6: 5-5

# document level annotation:
(s28s0 / sentence
    :temporal ((s27x :after s28x)
        (s28x :before s28x6))
    :modal ((root :modal author)
        (author :full-affirmative s28x6)
        (author :full-affirmative s28x))
    :coref ((s27i3 :same-entity s28i2)
        (s27x2 :same-entity s28x3)))

## chinese_umr-0005, sentence 16

# :: snt16
Index: 1  2   3 4 5 6 7  8  9  10  11
Words: 进入 军乐团 后 ， 他 被 老师 分配 吹奏 单簧管 。 

# sentence level graph:
(s16x / 分配-01
    :ARG0 (s16x2 / 老师)
    :ARG1 (s16x3 / 吹奏-00
        :ARG0 (s16i3 / individual-person
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s16x4 / 单簧管)
        :aspect habitual)
    :ARG2 s16i3
    :temporal (s16x5 / 后
        :op1 (s16x6 / 进入-01
            :ARG0 s16i3
            :ARG1 (s16x7 / 军乐团)
            :aspect performance))
    :aspect performance)


# alignment:
s16i3: 0-0
s16x: 8-8
s16x2: 7-7
s16x3: 9-9
s16x4: 10-10
s16x5: 3-3
s16x6: 1-1
s16x7: 2-2

# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16x)
        (s16x :overlap s16x3)
        (s16x :before s16x6))
    :modal ((root :modal author)
        (author :full-affirmative s16x3)
        (author :full-affirmative s16x6)
        (author :full-affirmative s16x))
    :coref ((s15i3 :same-entity s16i3)))

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

## chinese_umr-0002, sentence 8

# :: snt8
Index: 1  2  3   4
Words: 死者 包括 袭击者 。

# sentence level graph:
(s8x / 包括-01
    :ARG0 (s8x2 / 者
        :ARG0-of (s8x5 / 死-01
            :aspect state))
    :ARG1 (s8x3 / 者
        :ARG0-of (s8x4 / 袭击-01
            :aspect performance))
    :aspect state)


# alignment:
s8x: 2-2
s8x2: 1-1
s8x3: 1-1
s8x4: 3-3
s8x5: 1-1

# document level annotation:
(s8s0 / sentence
    :temporal ((s8x5 :before s8x4)
        (document-creation-time :overlap s8x))
    :modal ((root :modal author)
        (author :full-affirmative s8x5)
        (author :full-affirmative s8x4)
        (author :full-affirmative s8x))
    :coref ((s7x3 :same-event s8x5)
        (s6x7 :same-event s8x4)))
