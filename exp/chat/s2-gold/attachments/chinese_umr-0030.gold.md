# Gold UMR annotations of sentences like those of chinese_umr-0030

From ai-native-annotator.github.io data/skillparse/resources/gold/zh/gold.json (no test document).

## chinese_umr-0011, sentence 23

# :: snt23
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 根据 2013 年 厦门 晚报 的 报道 ， 福建省 厦门市 内 现在 还 有 总共 11 座 贞孝 节烈 牌坊 ， 而 湖南省 则 至少 有 1 座 。

# sentence level graph:
(s23x13 / say-91
	:ARG0 (s23n2 / newspaper
		:name (s23n7 / name
			:op1 "厦门"
			:op2 "晚报"))
	:ARG1 (s23a / contrast-91
		:ARG1 (s23x / 有-03
			:ARG1 (s23c / city
				:name (s23n5 / name
					:op1 "厦门市")
				:part-of (s23p / province
					:name (s23n4 / name
						:op1 "福建省")))
			:ARG2 (s23x2 / 牌坊
				:mod (s23x3 / 贞孝)
				:mod (s23x4 / 节烈)
				:quant 11
				:unit (s23x5 / 座)
				:mod (s23x6 / 总共))
			:temporal (s23x7 / 现在)
			:mod (s23x8 / 还)
			:aspect state)
		:ARG2 (s23x9 / 有-03
			:ARG1 (s23p3 / province
				:name (s23n6 / name
					:op1 "湖南省"))
			:ARG2 (s23x10 / 牌坊
				:quant 1
				:unit (s23x11 / 座)
				:mod (s23x12 / 至少))
			:aspect state))
	:temporal (s23d / date-entity
		:year 2013))

# alignment:
s23a: 0-0
s23c: 0-0
s23n: 0-0
s23n2: 0-0
s23n4: 0-0
s23n5: 0-0
s23n6: 0-0
s23n7: 0-0
s23p: 0-0
s23p2: 0-0
s23p3: 0-0
s23x: 14-14
s23x10: 20-20
s23x11: 17-17
s23x12: 25-25
s23x13: 7-7
s23x2: 20-20
s23x3: 18-18
s23x4: 19-19
s23x5: 17-17
s23x6: 15-15
s23x7: 12-12
s23x8: 13-13
s23x9: 14-14

# document level annotation:
(s23s0 / sentence
	:temporal ((document-creation-time :overlap s23x)
		(document-creation-time :overlap s23x9))
	:modal ((root :modal author)
		(author :full-affirmative s23x)
		(author :full-affirmative s23x9))
	:coref ((s1x :subset-of s23x2)
		(s1x :subset-of s23x10)))

## chinese_umr-0024, sentence 1

# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
Words: 阿里巴巴 创始人 马云 已经 在 海外 客居 一年 多 ， 最近 已 返回 中国 ， 访问 杭州 一所 私立 学校 ， 讨论 AI 聊天 机器人 “ ChatGPT ” 在 教育 行业 的 影响 。 中国 政府 最近 表示 将 支持 民营 企业 ， 据报 马云 曾 婉拒 回国 邀请 。

# sentence level graph:
(s1m / multi-sentence
	:op1 (s1a / and
		:op1 (s1x / 客居-01
			:ARG0 (s1i2 / individual-person
				:name (s1n / name
					:op1 "马云")
				:ARG1-of (s1h / have-org-role-91
					:ARG2 (s1c / company
						:name (s1n2 / name
							:op1 "阿里巴巴"))
					:ARG3 (s1x3 / 创始人)))
			:ARG1 (s1x21 / 海外)
			:duration (s1t / temporal-quantity
				:quant 1
				:unit (s1x6 / 年)
				:mod (s1x7 / 多))
			:mod (s1x25 / 已经)
			:aspect activity)
		:op2 (s1x8 / 返回-01
			:ARG0 s1i2
			:ARG1 (s1c2 / country
				:name (s1n3 / name
					:op1 "中国"))
			:temporal (s1x10 / 最近)
			:mod (s1x26 / 已)
			:aspect performance)
		:op3 (s1x11 / 访问-01
			:ARG0 s1i2
			:ARG1 (s1x22 / 学校
				:place (s1c3 / city
					:name (s1n4 / name
						:op1 "杭州"))
				:quant 1
				:unit (s1x14 / 所)
				:mod (s1x15 / 私立))
			:aspect performance)
		:op4 (s1x16 / 讨论-01
			:ARG0 s1i2
			:ARG1 (s1x18 / 影响-01
				:ARG0 (s1c5 / computer-program
					:name (s1n5 / name
						:op1 "ChatGPT")
					:ARG1-of (s1i4 / identity-91
						:ARG2 (s1x24 / 机器人
							:mod (s1a2 / ai)
							:mod (s1x17 / 聊天))))
				:ARG1 (s1x19 / 行业
					:mod (s1x20 / 教育))
				:aspect state)
			:aspect performance))
	:op2 (s1a3 / and
		:op1 (s1x27 / 表示-01
			:ARG0 (s1x36 / 政府
				:possessor s1c2)
			:ARG1 (s1x28 / 支持-01
				:ARG0 s1x36
				:ARG1 (s1x29 / 企业
					:mod (s1x30 / 民营))
				:aspect activity)
			:temporal (s1x31 / 最近)
			:aspect performance)
		:op2 (s1s / say-91
			:ARG0 (s1nc / null-conceiver)
			:ARG1 (s1x32 / 拒绝-01
				:ARG0 s1i2
				:ARG1 (s1x33 / 邀请-01
					:ARG1 s1i2
					:ARG2 (s1x34 / 返回-01
						:ARG0 s1i2
						:ARG1 s1c2
						:aspect performance)
					:aspect performance)
				:manner (s1x35 / 婉)
				:temporal (s1x37 / 曾)
				:aspect performance))))

# alignment:
s1a: 0-0
s1a2: 23-23
s1c: 0-0
s1c2: 0-0
s1c5: 0-0
s1i2: 0-0
s1i4: 0-0
s1n: 0-0
s1n2: 0-0
s1n3: 0-0
s1n5: 0-0
s1t: 0-0
s1x: 7-7
s1x10: 11-11
s1x11: 16-16
s1x12: 17-17
s1x13: 0-0
s1x14: 18-18
s1x15: 19-19
s1x16: 22-22
s1x17: 24-24
s1x18: 33-33
s1x19: 31-31
s1x2: 3-3
s1x20: 30-30
s1x21: 6-6
s1x22: 20-20
s1x24: 25-25
s1x3: 2-2
s1x4: 1-1
s1x5: 0-0
s1x6: 8-8
s1x7: 9-9
s1x8: 13-13
s1x9: 14-14

# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1x)
            (s1x :after s1x8)
            (s1x11 :overlap s1x16)
            (document-creation-time :overlap s1x18)
            (document-creation-time :before s1x27)
            (s1x27 :after s1x28)
            (document-creation-time :before s1x32)
            (s1x32 :before s1x33)
            (s1x33 :after s1x34))
    :modal ((author :full-affirmative s1x)
            (author :full-affirmative s1x8)
            (author :full-affirmative s1x18)
            (author :full-affirmative s1x16)
            (author :full-affirmative s1x11)
            (author :full-affirmative s1x27)
            (author :full-affirmative s1x36)
            (s1x36 :partial-affirmative s1x28)
            (author :unspecified s1nc)
            (s1nc :full-affirmative s1x32)
            (s1nc :full-affirmative s1x33)
            (s1nc :unspecified s1x34))
    :coref ()
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

## chinese_umr-0005, sentence 28

# :: snt28
Index: 1 2 3  4  5 6   7  8 9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 他 在 会上 表示 ， 近年来 国歌 的 使用 出现 了  一些 乱象 ，  如  随意 改变 国歌 的  速度 、  情绪 ；  在  演唱 国歌 时  嬉笑 、  打闹 ；  在  婚丧 、  商业 活动 中  播放 国歌 。 

# sentence level graph:
(s28x / 表示-01
    :ARG0 (s28i2 / individual-person
        :refer-number singular
        :refer-person 3rd)
    :ARG1 (s28x2 / 出现-01
        :ARG0 (s28x3 / 使用-01
            :ARG1 (s28x4 / 国歌)
            :aspect performance)
        :ARG1 (s28x5 / 乱象
            :quant (s28x6 / 一些)
            :example (s28a / and
                :op1 (s28x7 / 改变-01
                    :ARG1 (s28a2 / and
                        :op1 (s28x9 / 速度
                            :mod s28x4)
                        :op2 (s28x10 / 情绪
                            :mod s28x4))
                    :manner (s28x8 / 随意)
                    :aspect performance)
                :op2 (s28a3 / and
                    :op1 (s28x12 / 嬉笑-00
                        :aspect performance)
                    :op2 (s28x13 / 打闹-00
                        :aspect performance)
                    :temporal (s28x14 / 演唱-01
                        :ARG1 s28x4
                        :aspect performance))
                :op3 (s28x16 / 播放-01
                    :ARG1 s28x4
                    :aspect performance
                    :place (s28o / or
                        :op1 (s28x20 / 婚丧)
                        :op2 (s28x21 / 活动
                            :topic (s28x22 / 商业))))))
        :aspect state
        :temporal (s28x15 / 近年来))
    :place (s28x11 / 上
        :op1 (s28x18 / 会))
    :aspect performance)


# alignment:
s28a: 0-0
s28a2: 0-0
s28a3: 0-0
s28i2: 0-0
s28o: 0-0
s28x: 4-4
s28x10: 22-22
s28x11: 3-3
s28x12: 28-28
s28x13: 30-30
s28x14: 25-25
s28x15: 6-6
s28x16: 38-38
s28x18: 3-3
s28x2: 10-10
s28x20: 33-33
s28x21: 36-36
s28x22: 35-35
s28x3: 9-9
s28x4: 7-7
s28x5: 13-13
s28x6: 12-12
s28x7: 17-17
s28x8: 16-16
s28x9: 20-20

# document level annotation:
(s28s0 / sentence
    :temporal ((document-creation-time :before s28x)
        (s28x :overlap s28x2)
        (s28x2 :overlap s28x4)
        (s28x2 :overlap s28x7)
        (s28x2 :overlap s28x12)
        (s28x12 :overlap s28x14)
        (s28x2 :overlap s28x13)
        (s28x2 :overlap s28x16))
    :modal ((root :modal author)
        (author :full-affirmative s28x3)
        (author :full-affirmative s28x7)
        (author :full-affirmative s28x14)
        (author :full-affirmative s28x12)
        (author :full-affirmative s28x13)
        (author :full-affirmative s28x16)
        (author :full-affirmative s28x2)
        (author :full-affirmative s28x))
    :coref ((s27i2 :same-entity s28i2)))

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

## chinese_umr-0025, sentence 495

# :: snt495
Index:    1  2  3    4    5    6  7  8
Words: 国王   他  对  什么   进行   统治   呢  ？ 

# sentence level graph:
(s495x5 / 进行-01
	:ARG1 (s495x6 / 统治-01
		:ARG0 (s495x2 / individual-person
			:refer-person 3
			:refer-number singular
			:ARG0-of (s495x13 / mean
				:ARG1 (s495x1 / 国王)))
		:ARG1 (s495x4 / amr-unknown)
		:mode interrogative)
	:ARG0 s495x2)

# alignment:
s495x1: 1-1
s495x13: 0-0
s495x2: 0-0
s495x4: 0-0
s495x5: 5-5
s495x6: 6-6

# document level annotation:
(s495s0 / sentence)

## chinese_umr-0025, sentence 694

# :: snt694
Index: 1  2    3    4    5    6  7 8
Words: “ 我  经营   管理   这些   星星   。  ”

# sentence level graph:
(s694x11 / say
	:ARG1 (s694x13 / and
		:op1 (s694x3 / 经营
			:modal-strength (s694x20 / full-affirmative
				:op2 (s694x4 / 管理-01
					:ARG0 (s694x2 / individual-person
						:refer-person 1
						:refer-number singular)
					:ARG1 (s694x6 / 星星
						:mod (s694x5 / 这些))
					:modal-strength (s694x21 / full-affirmative))))))

# alignment:
s694x11: 0-0
s694x13: 0-0
s694x2: 0-0
s694x20: 0-0
s694x21: 0-0
s694x3: 3-3
s694x4: 4-4
s694x5: 5-5
s694x6: 6-6

# document level annotation:
(s694s0 / sentence)

## chinese_umr-0025, sentence 831

# :: snt831
Index: 1  2  3    4  5  6
Words: “ 这  是  可能   的  。 

# sentence level graph:
(s831x7 / say
	:ARG1 (s831x4 / 可能-01
		:ARG0 (s831x2 / 这)
		:mode judgement))

# alignment:
s831x2: 2-2
s831x4: 4-4
s831x7: 0-0

# document level annotation:
(s831s0 / sentence)

## chinese_umr-0025, sentence 845

# :: snt845
Index: 1      2  3 4        5    6  7  8
Words: “ 怎么样    ？  ” 地理学家     询问   道  。 

# sentence level graph:
(s845x6 / 询问-01
	:ARG0 (s845x5 / 地理学家)
	:ARG1 (s845x2 / 怎么样
		:mode interrogative)
	:modal-strength (s845x14 / full-affirmative))

# alignment:
s845x14: 0-0
s845x2: 2-2
s845x5: 5-5
s845x6: 6-6

# document level annotation:
(s845s0 / sentence)

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

## chinese_umr-0025, sentence 1085

# :: snt1085
Index:    1  2    3  4    5    6    7  8  9 10 11 12   13 14   15   16 17   18 19 20 21   22 23
Words: 但是   ，  如果   你  随便   什么   时候   来  ，  我  就  不  知道   在  什么   时候   该  准备   好  我  的  心情   … 

# sentence level graph:
(s1085x24 / contrast
	:ARG2 (s1085x26 / condition
		:ARG1 (s1085x8 / 来-01
			:ARG0 (s1085x4 / individual-person
				:refer-person 2
				:refer-number singular)
			:temporal (s1085x7 / 时候
				:mod (s1085x6 / 什么)
				:mod (s1085x5 / 随便))
			:modal-strength (s1085x44 / full-affirmative))
		:ARG2 (s1085x13 / 知道-01
			:ARG0 (s1085x10 / individual-person
				:refer-person 1
				:refer-number singular)
			:modal-strength (s1085x45 / full-negative)
			:polarity -
			:ARG1 (s1085x17 / 该
				:ARG0 (s1085x18 / 准备-01
					:manner (s1085x19 / 好)
					:ARG1 (s1085x22 / 心情
						:possessor-of (s1085x20 / individual-person
							:refer-person 1
							:refer-number singular))
					:temporal (s1085x16 / 时候
						:mod (s1085x15 / 什么)))))
		:modal-strength (s1085x46 / neutral-affirmative)))

# alignment:
s1085x10: 0-0
s1085x13: 13-13
s1085x15: 6-6
s1085x16: 7-7
s1085x17: 17-17
s1085x18: 18-18
s1085x19: 19-19
s1085x20: 0-0
s1085x22: 22-22
s1085x24: 0-0
s1085x26: 0-0
s1085x4: 0-0
s1085x44: 0-0
s1085x45: 0-0
s1085x46: 0-0
s1085x5: 5-5
s1085x6: 6-6
s1085x7: 7-7
s1085x8: 8-8

# document level annotation:
(s1085s0 / sentence)

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

## chinese_umr-0025, sentence 991

# :: snt991
Index:    1  2  3  4  5  6  7  8    9 10 11   12   13 14   15   16 17 18   19 20 21   22 23 24   25 26   27   28 29 30
Words: 那么   ，  我  还  得  装  着  去  护理   她  ，  因为   如果   不  这样   的话   ，  她  为了   使  我  难堪   ，  她  可能   会  真的   死去   …  ” 

# sentence level graph:
(s991x31 / say
	:ARG1 (s991x45 / causation
		:ARG1 (s991x46 / condition
			:ARG1 (s991x15 / 这样
				:polarity -)
			:ARG2 (s991x25 / 可能-01
				:ARG0 (s991x26 / 会
					:ARG0 (s991x28 / 死去-01
						:ARG0 (s991x24 / individual-person
							:refer-person 3
							:refer-number singular)
						:mod (s991x27 / 真的)
						:modal-strength (s991x57 / neutral-affirmative
							:purpose (s991x20 / 使-01
								:ARG1 (s991x21 / individual-person
									:refer-person 1
									:refer-number singular)
								:ARG2 (s991x22 / 难堪-01
									:ARG0 s991x21)
								:ARG0 (s991x18 / individual-person
									:refer-person 3
									:refer-number singular)))
						:modal-strength (s991x60 / neutral-affirmative
							:ARG2 (s991x5 / 得-01
								:ARG0 (s991x6 / 装-03
									:aspect activity
									:ARG0 (s991x3 / individual-person
										:refer-person 1
										:refer-number singular)
									:ARG1 (s991x8 / 去-01
										:ARG1 (s991x9 / 护理
											:ARG1 (s991x10 / individual-person
												:refer-person 3
												:refer-number singular)
											:ARG0 s991x3)
										:ARG0 s991x3)
									:modal-strength (s991x56 / partial-affirmative))
								:mod (s991x4 / 还)))))))))

# alignment:
s991x10: 0-0
s991x15: 15-15
s991x18: 0-0
s991x20: 20-20
s991x21: 0-0
s991x22: 22-22
s991x24: 0-0
s991x25: 25-25
s991x26: 26-26
s991x27: 27-27
s991x28: 28-28
s991x3: 0-0
s991x31: 0-0
s991x4: 4-4
s991x45: 0-0
s991x46: 0-0
s991x5: 5-5
s991x56: 0-0
s991x57: 0-0
s991x6: 6-6
s991x60: 0-0
s991x8: 8-8
s991x9: 9-9

# document level annotation:
(s991s0 / sentence)

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

## chinese_umr-0025, sentence 1174

# :: snt1174
Index:  1    2    3  4  5
Words: 我  自己   思量   着  ， 

# sentence level graph:
(s1174x3 / 思量-01
	:ARG0 (s1174x2 / 自己
		:ARG0-of (s1174x10 / mean
			:ARG1 (s1174x1 / individual-person
				:refer-person 1
				:refer-number singular)))
	:modal-strength (s1174x12 / full-affirmative))

# alignment:
s1174x1: 0-0
s1174x10: 0-0
s1174x12: 0-0
s1174x2: 2-2
s1174x3: 3-3

# document level annotation:
(s1174s0 / sentence)

## chinese_umr-0025, sentence 514

# :: snt514
Index:    1    2  3    4  5 6
Words: 将军   还是   我  自己   ？  ”

# sentence level graph:
(s514x7 / say
	:ARG1 (s514x2 / or
		:op1 (s514x1 / 将军)
		:op2 (s514x4 / 自己
			:ARG0-of (s514x12 / mean
				:ARG1 (s514x3 / individual-person
					:refer-person 1
					:refer-number singular)))
		:mode interrogative))

# alignment:
s514x1: 1-1
s514x12: 0-0
s514x2: 0-0
s514x3: 0-0
s514x4: 4-4
s514x7: 0-0

# document level annotation:
(s514s0 / sentence)

## chinese_umr-0025, sentence 987

# :: snt987
Index:  1    2    3    4    5  6
Words: 他  感到   自己   非常   不幸   。 

# sentence level graph:
(s987x2 / 感到-01
	:ARG0 (s987x1 / individual-person
		:refer-person 3
		:refer-number singular)
	:ARG1 (s987x5 / 不幸-01
		:ARG0 (s987x3 / 自己)
		:degree (s987x4 / 非常))
	:modal-strength (s987x13 / full-affirmative))

# alignment:
s987x1: 0-0
s987x13: 0-0
s987x2: 2-2
s987x3: 3-3
s987x4: 4-4
s987x5: 5-5

# document level annotation:
(s987s0 / sentence)

## chinese_umr-0002, sentence 21

# :: snt21
Index: 1  2   3  4  5  6  7  8 9  10 11 12 13  14 15  16 17 18 19 20 21 22 23 24 25
Words: 一位 穆斯林 社区 工作 人员 报称 五年 前 他们 曾  警告 过  英国人 ，  萨尔曼 曾  发表 “  声援 恐怖 分子 ”  的  言论 。 

# sentence level graph:
(s21x / 报-01
    :ARG0 (s21x2 / 人员
        :unit (s21x3 / 位)
        :quant 1
        :ARG0-of (s21x4 / 工作-01
            :aspect habitual
            :place (s21x5 / 社区
                :mod (s21x6 / 穆斯林))))
    :ARG1 (s21x7 / 称-02
        :ARG0 s21x2
        :ARG1 (s21x8 / 警告-01
            :ARG0 s21x2
            :ARG1 (s21x9 / 人
                :refer-number plural
                :place (s21c / country
                    :name (s21n / name
                        :op1 "英国")))
            :aspect performance
            :mod (s21x17 / 曾)
            :temporal (s21x18 / 前
                :op1 (s21t / temporal-quantity
                    :quant 5
                    :unit (s21x19 / 年))))
        :ARG2 (s21x10 / 发表-01
            :ARG0 (s21i2 / individual-person
                :name (s21n2 / name
                    :op1 "萨尔曼"))
            :ARG1 (s21x12 / 言论)
            :ARG3 (s21x13 / 声援-01
                :ARG1 (s21x14 / 分子
                    :mod (s21x15 / 恐怖)))
            :mod (s21x16 / 曾)
            :aspect performance))
    :aspect performance)


# alignment:
s21c: 0-0
s21i2: 0-0
s21n: 0-0
s21n2: 0-0
s21t: 0-0
s21x: 6-6
s21x10: 17-17
s21x12: 24-24
s21x13: 19-19
s21x14: 21-21
s21x15: 20-20
s21x16: 10-10
s21x17: 10-10
s21x18: 8-8
s21x19: 7-7
s21x2: 5-5
s21x3: 1-1
s21x4: 4-4
s21x5: 3-3
s21x6: 2-2
s21x7: 6-6
s21x8: 11-11
s21x9: 5-5

# document level annotation:
(s21s0 / sentence
    :temporal ((document-creation-time :before s21x)
        (s21x :overlap s21x4)
        (s21x :overlap s21x7)
        (s21x7 :before s21x8)
        (s21x8 :before s21x10)
        (s21x10 :overlap s21x13))
    :modal ((root :modal author)
        (author :full-affirmative s21x10)
        (author :full-affirmative s21x7)
        (author :full-affirmative s21x15)
        (author :full-affirmative s21x6)
        (author :full-affirmative s21x)
        (author :full-affirmative s21x8)
        (author :full-affirmative s21x9)
        (s21x9 :full-affirmative s21x4)
        (author :full-affirmative s21x9)
        (author :full-affirmative s21x9)
        (author :full-affirmative s21x19)
        (author :full-affirmative s21x9)
        (author :full-affirmative s21x9)
        (author :full-affirmative s21x2)
        (s21x2 :full-affirmative s21x7)
        (s21x7 :unspecified s21x8)
        (s21x2 :full-affirmative s21x7)
        (s21x7 :unspecified s21x10)
        (author :full-affirmative s21x2))
    :coref ((s20x16 :same-entity s21i2)))

## chinese_umr-0016, sentence 1

# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Words: 香港 及 深圳 受 暴雨 重创 ， 多地 出现 水浸 和 山泥 倾泻 。 香港 启动 为期 16 小时 的 “ 极端 情况 ” ， 当局 形容 雨势 “ 五百年 一 遇 ” 。

# sentence level graph:
(s1m2 / multi-sentence
    :op1 (s1a / and
        :op1 (s1x15 / 重创-01
            :ARG0 (s1x16 / 暴雨)
            :ARG1 (s1a3 / and
                :op1 (s1c2 / country-partition
                    :name (s1n2 / name
                        :op1 "香港"))
                :op2 (s1c / human-settlement
                    :name (s1n / name
                        :op1 "深圳")))
            :aspect performance)
        :op2 (s1x10 / 出现-01
            :ARG0 (s1x13 / 地
                :mod (s1x14 / 多))
            :theme (s1a2 / and
                :op1 (s1x12 / 浸-01
                    :ARG0 (s1x18 / 水)
                    :aspect process)
                :op2 (s1x11 / 倾泻-01
                    :ARG1 (s1x17 / 山泥)
                    :aspect process))
            :aspect performance))
    :op2 (s1a4 / and
        :op1 (s1x6 / 启动-01
            :ARG0 s1c2
            :ARG1 (s1x7 / 情况
                :duration (s1t2 / temporal-quantity
                    :unit (s1x8 / 小时)
                    :quant 16)
                :mod (s1x9 / 极端))
            :aspect performance)
        :op2 (s1x / 形容-03
            :ARG0 (s1x5 / 当局)
            :ARG1 (s1x4 / 雨势)
            :ARG2 (s1x2 / 遇-01
                :aspect habitual
                :frequency (s1t / temporal-quantity
                    :unit (s1x3 / 年)
                    :quant 500))
            :aspect performance)))

# alignment:
s1a: 0-0
s1a2: 0-0
s1a3: 0-0
s1a4: 0-0
s1c: 0-0
s1c2: 0-0
s1m2: 0-0
s1n: 0-0
s1n2: 0-0
s1s: 0-0
s1t: 0-0
s1t2: 0-0
s1x: 27-27
s1x10: 9-9
s1x11: 13-13
s1x12: 10-10
s1x13: 8-8
s1x14: 8-8
s1x15: 6-6
s1x16: 5-5
s1x17: 12-12
s1x18: 10-10
s1x2: 32-32
s1x3: 30-30
s1x4: 28-28
s1x5: 26-26
s1x6: 16-16
s1x7: 23-23
s1x8: 19-19
s1x9: 22-22

# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1x15)
            (s1x15 :overlap s1x10)
            (s1x15 :after s1x6)
            (s1x15 :after s1x)
            (s1x10 :overlap s1x12)
            (s1x10 :overlap s1x11)
            (present-reference :overlap s1x2))
    :modal ((root :modal author)
            (author :full-affirmative s1x15)
            (author :full-affirmative s1x12)
            (author :full-affirmative s1x11)
            (author :full-affirmative s1x10)
            (author :full-affirmative s1x6)
            (author :full-affirmative s1x2)
            (author :full-affirmative s1x))
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

## chinese_umr-0025, sentence 1028

# :: snt1028
Index:    1  2    3  4    5  6  7  8    9 10   11   12   13 14 15
Words: 但是   ，  如果   你  驯服   了  我  ，  我们   就  互相   不可   缺少   了  。 

# sentence level graph:
(s1028x16 / contrast
	:ARG2 (s1028x18 / condition
		:ARG1 (s1028x5 / 驯服-01
			:ARG0 (s1028x4 / individual-person
				:refer-person 2
				:refer-number singular)
			:aspect performance
			:ARG1 (s1028x7 / individual-person
				:refer-person 1
				:refer-number singular)
			:modal-strength (s1028x29 / full-affirmative))
		:ARG2 (s1028x12 / 不可缺少
			:ARG0 (s1028x9 / individual-person
				:refer-person 1
				:refer-number plural)
			:mod (s1028x11 / 互相)
			:smood (s1028x14 / 了)
			:modal-strength (s1028x30 / full-affirmative))
		:modal-strength (s1028x27 / neutral-affirmative)))

# alignment:
s1028x11: 11-11
s1028x12: 12-12
s1028x14: 6-6
s1028x16: 0-0
s1028x18: 0-0
s1028x27: 0-0
s1028x29: 0-0
s1028x30: 0-0
s1028x4: 0-0
s1028x5: 5-5
s1028x7: 0-0
s1028x9: 0-0

# document level annotation:
(s1028s0 / sentence)

## chinese_umr-0029, sentence 2

# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 近日 ， 一 名 上海 网友 在 微博 上 晒出 自己 老公 年终 发放 的 各 种 提货券 、 食品券 ， 大 赞 “ 市政府 真 给力 ” ， 该 微博 瞬间 引起 轩然大波 ， 过 10万 网友 围观 。

# sentence level graph:
(s2x / and
    :op1 (s2x2 / 引起-01
        :temporal (s2x3 / 瞬间)
        :ARG0 (s2x4 / 微博
            :mod (s2x5 / 该))
        :ARG1 (s2x6 / 轩然大波)
        :aspect performance)
    :temporal (s2x7 / 近日)
    :op2 (s2x8 / 围观-01
        :ARG1 s2x4
        :ARG0 (s2x10 / 网友
            :quant (s2x11 / 过
                :op1 100000))
        :aspect activity)
    :op3 (s2x13 / 赞-01
        :degree (s2x14 / 大)
        :ARG0 (s2x15 / 网友
            :mod (s2c / human-settlement
                :name (s2n / name
                    :op1 "上海"))
            :possessor-of (s2x1 / 老公)
            :unit (s2x18 / 名)
            :quant 1)
        :ARG1 (s2x21 / 给力-00
            :degree (s2x22 / 真)
            :ARG0 (s2x23 / 市政府)
            :aspect state)
        :aspect performance)
    :op4 (s2x17 / 晒出-01
        :aspect performance
        :ARG0 s2x15
        :ARG1 (s2x26 / and
            :op1 (s2x32 / 食品券)
            :op2 (s2x27 / 提货券)
            :unit (s2x31 / 种)
            :mod (s2x33 / 各)
            :ARG1-of (s2x28 / 发放-01
                :aspect performance
                :ARG2 s2x1
                :temporal (s2x30 / 年终)))
        :place (s2x34 / social-media
            :name (s2n2 / name
                :op1 "微博"))))

# alignment:
s2c: 5-5
s2n: 0-0
s2x: 0-0
s2x1: 12-12
s2x10: 38-38
s2x11: 36-36
s2x13: 23-23
s2x14: 22-22
s2x15: 6-6
s2x17: 10-10
s2x18: 4-4
s2x2: 33-33
s2x21: 27-27
s2x22: 26-26
s2x23: 25-25
s2x24: 0-0
s2x26: 0-0
s2x27: 18-18
s2x28: 14-14
s2x3: 32-32
s2x30: 13-13
s2x31: 17-17
s2x32: 20-20
s2x33: 16-16
s2x34: 8-8
s2x4: 31-31
s2x5: 30-30
s2x6: 34-34
s2x7: 1-1
s2x8: 39-39

# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :depends-on s2x7)
            (s2x7 :contained s2x17)
            (s2x7 :contained s2x28)
            (s2x7 :contained s2x13)
            (s2x7 :contained s2x21)
            (s2x7 :contained s2x2)
            (s2x7 :contained s2x8)
            (s2x17 :before s2x28)
            (s2x17 :after s2x13)
            (s2x13 :before s2x21)
            (s2x13 :after s2x2)
            (s2x2 :after s2x8))
    :modal ((author :full-affirmative s2x17)
            (author :full-affirmative s2x28)
            (author :full-affirmative s2x13)
            (author :full-affirmative s2x15)
            (s2x15 :full-affirmative s2x21)
            (author :full-affirmative s2x2)
            (author :full-affirmative s2x8)
            (root :modal author))
    :coref ((s1x19 :same-event s2x28)
            (s1x10 :same-entity s2x23)))

## chinese_umr-0029, sentence 1

# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
Words: 形象 大 受 伤害 的 “ 市政府 ” 相关 机构 ， 应该 出面 调查 这 件 事情 的 真伪 ， 并 公布 相关 结果 。

# sentence level graph:
(s1a1 / and
    :op1 (s1x7 / 出面-01
        :aspect performance
        :ARG0 (s1x6 / 机构
            :possessor-of (s1x1 / 形象
                :ARG1-of (s1x2 / 伤害-01
                    :aspect performance
                    :degree (s1x15 / 大)))
            :mod (s1x8 / 相关)
            :possessor (s1x10 / 市政府))
        :ARG1 (s1x / 调查-01
            :aspect process
            :ARG0 s1x6
            :ARG1 (s1x18 / 真伪
                :possessor (s1x19 / 事情
                    :unit (s1x20 / 件)
                    :mod (s1x21 / 这)))))
    :op2 (s1x3 / 公布-01
        :ARG1 (s1x4 / 结果
            :mod (s1x5 / 相关))
        :ARG0 s1x6
        :aspect performance))

# alignment:
s1a1: 0-0
s1x: 14-14
s1x1: 1-1
s1x10: 7-7
s1x11: 0-0
s1x15: 2-2
s1x18: 19-19
s1x19: 17-17
s1x2: 4-4
s1x20: 16-16
s1x21: 15-15
s1x3: 22-22
s1x4: 24-24
s1x5: 23-23
s1x6: 10-10
s1x7: 13-13
s1x8: 9-9
s1x9: 0-0

# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1x2)
            (s1x2 :after s1x7)
            (s1x7 :after s1x)
            (s1x :after s1x3))
    :modal ((author :full-affirmative s1x2)
            (author :partial-affirmative s1x7)
            (author :partial-affirmative s1x)
            (root :modal author)
            (author :partial-affirmative s1x3)
            (author :partial-affirmative s1x6)
            (author :full-affirmative s1x1)))

## chinese_umr-0029, sentence 18

# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
Words: 因此 ， 被 “ 提货姐 ” 在 微博 中 表扬 “ 给力 ” 、 但 事实上 形象 大 受 伤害 的 “ 市政府 ” 相关 机构 ， 应该 出面 来 调查 清楚 这 件 事情 的 真伪 ， 并 公布 相关 结果 。

# sentence level graph:
(s18a1 / and
    :ARG1-of (s18h / have-cause-91)
    :op1 (s18x / 出面-01
        :ARG0 (s18x10 / 机构
            :mod (s18c / contrast-91
                :ARG2 (s18x15 / 伤害-01
                    :aspect performance
                    :manner (s18x18 / 事实上)
                    :ARG1 (s18x17 / 形象
                        :possessor s18x10)
                    :degree (s18x16 / 大))
                :ARG1 (s18x12 / 表扬-01
                    :aspect performance
                    :place (s18x14 / social-media
                        :name (s18n2 / name
                            :op1 "微博"))
                    :ARG2 (s18x13 / 给力-00
                        :aspect state
                        :ARG0 s18x10)
                    :ARG1 s18x10
                    :ARG0 (s18p / individual-person
                        :name (s18n1 / name
                            :op1 "提货姐"))))
            :possessor (s18g / 市政府)
            :mod (s18x11 / 相关))
        :ARG1 (s18x4 / 调查-01
            :aspect process
            :ARG0 s18x10
            :ARG1 (s18x6 / 真伪
                :possessor (s18x7 / 事情
                    :unit (s18x9 / 件)
                    :mod (s18x8 / 这)))
            :manner (s18x5 / 清楚))
        :aspect performance)
    :op2 (s18x1 / 公布-01
        :aspect performance
        :ARG0 s18x10
        :ARG1 (s18x2 / 结果
            :mod (s18x3 / 相关))))

# alignment:
s18a1: 0-0
s18c: 0-0
s18g: 23-23
s18h: 0-0
s18n: 0-0
s18n1: 0-0
s18p: 0-0
s18x: 29-29
s18x1: 40-40
s18x10: 26-26
s18x11: 25-25
s18x12: 10-10
s18x13: 12-12
s18x14: 8-8
s18x15: 20-20
s18x16: 18-18
s18x17: 17-17
s18x18: 16-16
s18x2: 42-42
s18x3: 41-41
s18x4: 31-31
s18x5: 32-32
s18x6: 37-37
s18x7: 35-35
s18x8: 33-33
s18x9: 34-34

# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x12)
            (s18x12 :before s18x13)
            (s18x12 :after s18x15)
            (s18x15 :after s18x)
            (s18x :after s18x4)
            (s18x4 :after s18x1))
    :modal ((author :full-affirmative s18x12)
            (author :full-affirmative s18p)
            (s18p :full-affirmative s18x13)
            (author :full-affirmative s18x15)
            (author :partial-affirmative s18x)
            (author :partial-affirmative s18x4)
            (author :partial-affirmative s18x1)
            (root :modal author)
            (author :full-affirmative s18x13))
    :coref ((s17x8 :same-entity s18p)
            (s17x2 :same-event s18x7))
)
