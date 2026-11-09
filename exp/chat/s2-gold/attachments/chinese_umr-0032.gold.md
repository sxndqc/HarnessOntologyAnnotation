# Gold UMR annotations of sentences like those of chinese_umr-0032

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0020, sentence 9

# :: snt9
Index:    1    2  3    4  5 6    7 8  9 10   11   12 13 14 15   16   17   18 19   20 21 22 23 24   25   26   27   28 29   30   31   32 33   34 35 36   37 38   39   40 41   42   43 44   45 46
Words: 中国   政府   视  彩礼   为  “ 陋习   ” ，  自  进入   2000 年  后  便  开始   逐步   治理   ，  2023 年  2  月  ，  中国   政府   发布   2023 年  中央   一号   文件   ，  其中   就  有  提及   要  整治   农村   “  天价   彩礼   ”  问题   。 

# sentence level graph:
(s9a / and
	:op1 (s9x / 视-02
		:ARG0 (s9g / 政府
			:mod (s9c / country
				:name (s9n / name
					:op1 "中国")))
		:ARG1 (s9x2 / 彩礼)
		:ARG2 (s9x3 / 陋习
			:mod (s9q / quote
				:op1 "“"
				:op2 "”"))
		:aspect habitual)
	:op2 (s9x6 / 治理-02
		:ARG0 (s9i2 / implicit-argument)
		:ARG1 (s9i3 / implicit-argument)
		:time (s9t / time
			:mod (s9e / enter-01
				:aspect process)
			:start (s9y / year
				:value 2000))
		:mod (s9x7 / 逐步))
	:op3 (s9a2 / and
		:op1 (s9x8 / 发布-01
			:ARG0 (s9x9 / 政府
				:mod (s9c2 / country
					:name (s9n3 / name
						:op1 "中国")))
			:ARG1 (s9d / document
				:name (s9n2 / name
					:op1 "中央一号文件")
				:mod (s9y2 / year
					:value 2023))
			:time (s9d2 / date-entity
				:month 2
				:year 2023)
			:aspect performance)
		:op2 (s9x12 / 提及-01
			:ARG1 (s9x5 / 整治-01
				:ARG1 (s9x4 / 問题
					:mod (s9x11 / 农村)
					:mod (s9x10 / 彩礼
						:mod (s9q2 / quote
							:op1 "“"
							:op2 "天价"
							:op3 "”")))
				:aspect habitual)
			:aspect habitual)))

# alignment:
s9a: 0-0
s9a2: 0-0
s9c: 0-0
s9c2: 0-0
s9d: 0-0
s9d2: 0-0
s9e: 0-0
s9g: 2-2
s9i2: 0-0
s9i3: 0-0
s9n: 0-0
s9n2: 0-0
s9n3: 0-0
s9q: 0-0
s9q2: 0-0
s9t: 0-0
s9x: 3-3
s9x10: 4-4
s9x11: 40-40
s9x12: 37-37
s9x2: 4-4
s9x3: 7-7
s9x4: 0-0
s9x5: 39-39
s9x6: 18-18
s9x7: 17-17
s9x8: 27-27
s9x9: 2-2
s9y: 0-0
s9y2: 0-0

# document level annotation:
(s9s0 / sentence
	:temporal ((document-creation-time :overlap s9x)
										s9y)
										s9d2)
		(s9d2 :depends-on s9x12))
	:modal ((root :modal author)
		(author :full-affirmative s9x)
		(author :full-affirmative s9e)
		(author :full-affirmative s9x8)
		(author :full-affirmative s9x5)
		(author :full-affirmative s9m)
		(author :full-affirmative s9x12)))

## chinese_umr-0022, sentence 8

# :: snt8
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 玳瑁 工艺 在 中国 已 有 上千年 的 历史 ， 工艺水平 在 唐代 已 达 顶峰 ， 日本 的 玳瑁 工艺 也 受到 了 中国 很大 的 影响 。

# sentence level graph:
(s8a / and
	:op1 (s8e / have-91
		:ARG1 (s8x4 / 玳瑁工艺)
		:ARG2 (s8x15 / 历史
			:duration (s8t / temporal-quantity
				:quant (s8x5 / 上千)
				:unit (s8x6 / 年)))
		:place (s8c / country
			:name (s8n / name
				:op1 "中国"))
		:mod (s8x7 / 已)
		:aspect state)
	:op2 (s8x / 达-01
		:ARG0 (s8x11 / 工艺水平
			:possessor s8x4)
		:ARG1 (s8x8 / 顶峰)
		:mod (s8x9 / 已)
		:temporal (s8d / date-entity
			:era (s8x10 / 唐代))
		:aspect performance)
	:op3 (s8x2 / 影响-01
		:ARG0 s8c
		:ARG1 (s8x12 / 工艺
			:mod (s8x13 / 玳瑁)
			:possessor (s8c2 / country
				:name (s8n2 / name
					:op1 "日本")))
		:mod (s8x14 / 很大)
		:aspect performance))

# alignment:
s8a: 0-0
s8c: 0-0
s8c2: 0-0
s8e: 0-0
s8n: 0-0
s8n2: 0-0
s8t: 0-0
s8x: 15-15
s8x10: 13-13
s8x11: 11-11
s8x12: 2-2
s8x13: 1-1
s8x14: 26-26
s8x2: 28-28
s8x3: 4-4
s8x4: 1-1
s8x5: 7-7
s8x6: 7-7
s8x7: 5-5
s8x8: 16-16
s8x9: 5-5

# document level annotation:
(s8s0 / sentence
    :temporal ((document-creation-time :overlap s8e)
            (document-creation-time :before s8x)
            (document-creation-time :overlap s8x2)
            (s8d :contained s8x))
    :modal ((root :modal author)
            (author :full-affirmative s8e)
            (author :full-affirmative s8x)
            (author :full-affirmative s8x2))
    :coref ()
)

## chinese_umr-0024, sentence 2

# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 马云 被 认为 离开 中国 已经 一年 多 ， 在 日本 和 欧洲 的 各个 地方 访问 。 这 是 第一 次 确认 到 马云 已经 返回 中国 。

# sentence level graph:
(s2m / multi-sentence
	:op1 (s2x / 认为-01
		:ARG1 (s2a / and
			:op1 (s2x3 / 离开-01
				:ARG0 (s2i2 / individual-person
					:name (s2n / name
						:op1 "马云"))
				:ARG1 (s2c / country
					:name (s2n2 / name
						:op1 "中国"))
				:duration (s2t / temporal-quantity
					:quant 1
					:unit (s2x6 / 年)
					:mod (s2x7 / 多))
				:mod (s2x18 / 已经)
				:aspect performance)
			:op2 (s2x8 / 访问-01
				:ARG0 s2i2
				:ARG1 (s2x9 / 地方
					:mod (s2x10 / 各个)
					:part-of (s2a2 / and
						:op1 (s2c2 / country
							:name (s2n3 / name
								:op1 "日本"))
						:op2 (s2c3 / continent
							:name (s2n4 / name
								:op1 "欧洲"))))
				:aspect performance))
		:aspect state)
	:op2 (s2x13 / 确认-01
		:ARG1 (s2x14 / 返回-01
			:ARG0 s2i2
			:ARG1 s2c
			:mod (s2x17 / 已经)
			:aspect performance)
		:ord (s2x15 / 第一)
		:unit (s2x16 / 次)
		:aspect performance))

# alignment:
s2a: 0-0
s2c: 0-0
s2c2: 0-0
s2c3: 0-0
s2i2: 0-0
s2i3: 0-0
s2m: 0-0
s2n: 0-0
s2n2: 0-0
s2n3: 0-0
s2n4: 0-0
s2o: 0-0
s2t: 0-0
s2x: 3-3
s2x10: 15-15
s2x12: 19-19
s2x13: 23-23
s2x14: 27-27
s2x15: 0-0
s2x2: 1-1
s2x3: 4-4
s2x4: 5-5
s2x5: 0-0
s2x6: 7-7
s2x7: 8-8
s2x8: 17-17
s2x9: 16-16

# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :overlap s2x)
            (s2x :before s2x3)
            (document-creation-time :before s2x13)
            (s2x13 :before s2x14)
            (s2x3 :after s2x8)
            (s2x8 :after s2x14))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :full-affirmative s2x13)
            (author :full-affirmative s2x14)
            (author :unspecified null-conceiver)
            (null-conceiver :full-affirmative s2x3)
            (null-conceiver :full-affirmative s2x8))
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

## chinese_umr-0009, sentence 5

# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 头盔 配有 苹果 的 M2 处理器 ， 公司 表示 为 专门 新 研发 的 R1 处理器 可 减少 用家 操作 时 的 不适 。

# sentence level graph:
(s5a / and
    :op1 (s5x19 / 配有-01
        :ARG0 (s5x15 / 头盔)
        :ARG1 (s5p / product
            :name (s5n2 / name
                :op1 "M2"
                :op2 "处理器")
            :mod (s5c / company
                :name (s5n / name
                    :op1 "苹果")))
        :aspect state
        :modal-strength full-affirmative)
    :op2 (s5x3 / 表示-01
        :ARG0 s5c
        :ARG1 (s5x / 减少-01
            :ARG0 (s5p2 / product
                :name (s5n3 / name
                    :op1 "R1"
                    :op2 "处理器")
                :ARG1-of (s5x10 / 研发-01
                    :ARG0 s5c
                    :mod (s5x11 / 专门)
                    :mod (s5x9 / 新)
                    :aspect performance
                    :modal-strength full-affirmative))
            :ARG1 (s5x2 / 不适
                :temporal (s5x5 / 时
                    :op1 (s5x12 / 操作-01
                        :ARG0 (s5x8 / 用家)
                        :ARG1 s5x15
                        :aspect activity
                        :modal-strength undefined)))
            :aspect directed-activity
            :modal-strength neutral-affirmative)
        :aspect performance
        :modal-strength full-affirmative))

# alignment:
s5a: 0-0
s5c: 0-0
s5n: 0-0
s5n2: 0-0
s5n3: 0-0
s5p: 0-0
s5p2: 0-0
s5x: 18-18
s5x10: 13-13
s5x11: 11-11
s5x12: 20-20
s5x15: 1-1
s5x19: 2-2
s5x2: 23-23
s5x3: 9-9
s5x4: 8-8
s5x5: 21-21
s5x8: 19-19
s5x9: 12-12

# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :overlap s5x19)
            (document-creation-time :before s5x3)
            (s5x3 :before s5x10)
            (document-creation-time :overlap s5x)
            (s5x :overlap s5x12)
            (s5x12 :overlap s5x5))
    :modal ((author :full-affirmative s5x19)
            (root :modal author)
            (author :full-affirmative s5x3)
            (author :full-affirmative s5c)
            (s5c :full-affirmative s5x10)
            (s5c :neutral-affirmative s5x)
            (s5c :unspecified s5x12))
    :coref ((s4x17 :same-entity s5x15)
            (s4c :same-entity s5c))
)

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

## chinese_umr-0016, sentence 15

# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
Words: 使用 一亿五千万 港元 搭建 的 紧急 短讯 系统 ， 在 暴雨 中 没有 被 使用 ， 政务司 副 司长 卓永兴 说 ， “ 我 认为 所有 清醒 的 公众 都 知道 下 暴雨 ， 所以 没有 必要 用 紧急 短讯 系统 发信 告知 市民 如此 明显 的 情况 。”

# sentence level graph:
(s15a2 / and
    :op1 (s15x / 使用-01
        :ARG1 (s15x6 / 系统
            :mod (s15x8 / 短讯
                :mod (s15x7 / 紧急))
            :ARG1-of (s15x2 / 搭建-01
                :aspect performance
                :manner (s15x12 / 使用-01
                    :ARG1 (s15m / monetary-quantity
                        :unit (s15x3 / 港元)
                        :quant "一亿五千万"))))
        :temporal (s15x4 / 暴雨)
        :polarity -
        :aspect performance)
    :op2 (s15x5 / 说-01
        :ARG0 (s15i3 / individual-person
            :name (s15n2 / name
                :op1 "卓永兴")
            :ARG1-of (s15h / have-org-role-91
                :ARG2 (s15g / government-organization
                    :name (s15n / name
                        :op1 "政务司"))
                :ARG3 (s15x9 / 副司长)))
        :ARG1 (s15x10 / 认为-01
            :ARG0 s15i3
            :ARG1 (s15h2 / have-cause-91
                :ARG1 (s15x28 / 必要-01
                    :ARG0 (s15x29 / 告知-01
                        :ARG1 (s15x18 / 情况
                            :mod (s15x19 / 明显
                                :mod (s15x20 / 如此)))
                        :ARG2 (s15x21 / 市民)
                        :manner (s15x30 / 发信-01
                            :ARG1 s15x21
                            :instrument s15x6
                            :aspect performance)
                        :modal-predicate s15x28
                        :aspect performance)
                    :polarity -
                    :aspect state)
                :ARG2 (s15x11 / 知道-01
                    :ARG0 (s15x25 / 公众
                        :quant (s15x26 / 所有)
                        :mod (s15x27 / 清醒))
                    :ARG1 (s15x23 / 下-05
                        :ARG0 (s15x24 / 暴雨)
                        :aspect performance)
                    :aspect state))
            :aspect state)
        :aspect performance))

# alignment:
s15a2: 0-0
s15g: 0-0
s15h: 0-0
s15h2: 0-0
s15i3: 0-0
s15m: 0-0
s15n: 0-0
s15n2: 0-0
s15p: 0-0
s15x: 1-1
s15x10: 25-25
s15x11: 31-31
s15x12: 1-1
s15x18: 48-48
s15x19: 46-46
s15x2: 4-4
s15x20: 45-45
s15x21: 44-44
s15x23: 32-32
s15x24: 11-11
s15x25: 29-29
s15x26: 26-26
s15x27: 27-27
s15x28: 37-37
s15x29: 43-43
s15x3: 3-3
s15x4: 11-11
s15x5: 21-21
s15x6: 8-8
s15x7: 6-6
s15x8: 7-7
s15x9: 18-18

# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15x12)
            (s15x12 :overlap s15x2)
            (s15x2 :after s15x4)
            (s15x4 :contained s15x)
            (s15x :after s15x5)
            (s15x5 :overlap s15x10)
            (s15x10 :overlap s15x11)
            (s15x10 :overlap s15x28)
            (s15x28 :overlap s15x29)
            (s15x29 :overlap s15x30))
    :modal ((s15i3 :full-affirmative s15x11)
            (root :modal author)
            (author :full-affirmative s15x2)
            (author :full-negative s15x)
            (s15i3 :full-negative s15x28)
            (author :full-affirmative s15i3)
            (s15i3 :full-affirmative s15x23)
            (s15i3 :unspecified s15x29)
            (s15i3 :unspecified s15x30))
    :coref ((s13g :same-entity s15g))
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

## chinese_umr-0019, sentence 2

# :: snt2
Index:    1    2  3    4    5    6  7    8  9 10   11   12   13   14 15 16   17 18   19   20   21 22
Words: 面对   首次   在  严寒   环境   返校   的  学生   ，  有  学校   强制   学生   寒潮   下  穿  校服   ，  引发   广泛   关注   。 

# sentence level graph:
(s2a / and
	:op1 (s2x9 / 面对-01
		:ARG1 (s2x10 / 学生
			:ARG0-of (s2x11 / 返校-01
				:ord (s2o / ordinal-entity
					:value 1
					:unit (s2x13 / 次))
				:place (s2x14 / 环境
					:mod (s2x15 / 严寒))
				:aspect performance))
		:aspect state)
	:op2 (s2x16 / 引发-01
		:ARG0 (s2e / exist-91
			:ARG2 (s2x2 / 学校
				:ARG0-of (s2x3 / 强制-01
					:ARG1 (s2x7 / 学生)
					:ARG2 (s2x4 / 穿-01
						:ARG1 (s2x6 / 校服)
						:aspect performance
						:temporal (s2x5 / 寒潮))
					:aspect performance)))
		:ARG1 (s2x8 / 关注
			:mod (s2x12 / 广泛))
		:aspect performance))

# alignment:
s2a: 0-0
s2e: 0-0
s2o: 0-0
s2x10: 8-8
s2x11: 6-6
s2x12: 20-20
s2x13: 2-2
s2x14: 5-5
s2x15: 4-4
s2x16: 19-19
s2x2: 11-11
s2x3: 12-12
s2x4: 16-16
s2x5: 14-14
s2x6: 17-17
s2x7: 8-8
s2x8: 21-21
s2x9: 1-1

# document level annotation:
(s2s0 / sentence
	:temporal ((document-creation-time :before s2x16)
		(s2x3 :overlap s2x4)
		(s2x3 :after s2x16)
		(s2x9 :overlap s2x11)))
	:modal ((root :modal author)
		(author :full-affirmative s2x11)
		(author :full-affirmative s2x9)
		(author :full-affirmative s2x4)
		(author :full-affirmative s2x3)
		(author :full-affirmative s2x16)
		(root :modal author))

## chinese_umr-0005, sentence 14

# :: snt14
Index: 1  2   3   4  5 6  7 8  9  10 11 12
Words: 考入 解放军 军乐团 之后 ， 于海 才 开始 正式 学习 音乐 。 

# sentence level graph:
(s14c / consecutive
    :op1 (s14x / 考入-01
        :ARG1 (s14a2 / armed-organization
            :name (s14n3 / name
                :op1 "解放军"
                :op2 "军乐团"))
        :aspect performance)
    :op2 (s14x2 / 开始-01
        :ARG0 (s14i2 / individual-person
            :name (s14n / name
                :op1 "于海"))
        :ARG1 (s14x3 / 学习-01
            :ARG1 (s14x4 / 音乐)
            :aspect process)
        :mod (s14x7 / 才)
        :aspect activity))


# alignment:
s14a2: 0-0
s14c: 0-0
s14i2: 0-0
s14n: 0-0
s14n3: 0-0
s14x: 1-1
s14x2: 8-8
s14x3: 10-10
s14x4: 11-11
s14x7: 7-7

# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14x)
        (s14x :after s14x2)
        (s14x2 :after s14x3))
    :modal ((root :modal author)
        (author :full-affirmative s14x)
        (author :full-affirmative s14x3)
        (author :full-affirmative s14x2))
    :coref ((s13i2 :same-entity s14i2)))

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

## chinese_umr-0026, sentence 33

# :: snt33
Index:    1    2  3  4    5    6  7  8    9   10   11 12   13 14     15   16 17 18 19     20 21   22 23 24   25   26 27   28 29 30 31     32 33   34 35   36   37   38 39   40   41 42 43   44 45   46   47 48 49   50     51 52   53 54 55 56   57   58 59 60   61 62 63 64   65   66     67 68 69 70 71   72 73
Words: 当日   晚间   的  《  新闻   联播   》  以  头条   报道   会面   ，  使用   的  新华社    通稿   中  ，  将  习近平    的  头衔   写  为  中共   中央   总  书记   ，  但  对  马英九    则  没有   作  任何   身份   介绍   或  头衔   称呼   ，  既  没有   以  党职   称呼   为  “  中国   国民党    前  主席   ”  ，  也  没有   使用   “  前  总统   ”  “  前  台湾   地区   领导人    ”  一  类  的  称呼   。 

# sentence level graph:
(s33a / and
	:op1 (s33x / 报道-01
		:ARG0 (s33s / show
			:name (s33b / broadcast
				:op1 "新闻"
				:op2 "联播"))
		:ARG1 (s33x5 / 会面-01
			:aspect activity)
		:temporal (s33x2 / 当日)
		:temporal (s33x3 / 晚间)
		:manner (s33x4 / 头条)
		:aspect performance)
	:op2 (s33x6 / 使用-01
		:ARG0 s33x
		:ARG1 (s33x7 / 通稿
			:mod (s33x8 / 新华社)
			:ARG1-of (s33i2 / include-91
				:ARG1-of (s33c / contrast-91
					:op1 (s33x9 / 写为-00
						:ARG0 (s33x10 / 头衔
							:possessor-of (s33i3 / individual-person
								:name (s33n2 / name
									:op1 "习近平")))
						:ARG1 (s33x11 / 中共-中央-总-书记)
						:aspect state)
					:op2 (s33a2 / and
						:op1 (s33x12 / 介绍-01
							:ARG0 s33s
							:ARG1 (s33x13 / 身份
								:possessor-of (s33i4 / individual-person
									:name (s33n3 / name
										:op1 "马英九"))
								:mod (s33x14 / 任何))
							:aspect activity
							:polarity -)
						:op2 (s33x15 / 称呼-01
							:ARG0 s33s
							:ARG1 s33i4
							:ARG2 (s33x16 / 头衔
								:mod (s33x17 / 任何))
							:aspect activity
							:polarity -)))))
		:aspect state)
	:op3 (s33a3 / and
		:op1 (s33x18 / 称呼-01
			:ARG0 s33s
			:ARG1 s33i4
			:ARG2 (s33x20 / 中国-国民党-前-主席)
			:manner (s33x19 / 党职)
			:polarity -
			:aspect performance)
		:op2 (s33x21 / 使用-01
			:ARG0 s33s
			:ARG1 (s33x22 / 称呼-01
				:ARG2 (s33a4 / and
					:op1 (s33x23 / 前-总统)
					:op2 (s33x24 / 前-台湾-地区-领导人)))
			:aspect performance
			:polarity -)))

# alignment:
s33a: 0-0
s33a2: 0-0
s33a3: 0-0
s33a4: 0-0
s33b: 0-0
s33c: 0-0
s33i2: 0-0
s33i3: 0-0
s33i4: 0-0
s33n2: 0-0
s33n3: 0-0
s33s: 0-0
s33x: 10-10
s33x10: 22-22
s33x11: 17-17
s33x12: 38-38
s33x13: 37-37
s33x14: 36-36
s33x15: 41-41
s33x16: 22-22
s33x17: 36-36
s33x18: 41-41
s33x19: 46-46
s33x2: 1-1
s33x20: 17-17
s33x21: 13-13
s33x22: 41-41
s33x23: 27-27
s33x24: 52-52
s33x3: 2-2
s33x4: 9-9
s33x5: 11-11
s33x6: 13-13
s33x7: 16-16
s33x8: 15-15
s33x9: 23-23

# document level annotation:
(s33s0 / sentence
	:temporal ((document-creation-time :before s33x)
		(s33x :overlap s33x6)
		(s33x6 :overlap s33x9)
		(s33x6 :overlap s33x12)
		(s33x6 :overlap s33x15)
		(s33x18 :overlap s33x22)))
	:modal ((root :modal author)
		(author :full-affirmative s33x5)
		(author :full-affirmative s33x)
		(author :full-affirmative s33x9)
		(author :full-negative s33x12)
		(author :full-negative s33x15)
		(author :full-affirmative s33x6)
		(author :full-negative s33x18)
		(author :full-negative s33x21)
		(root :modal author))
