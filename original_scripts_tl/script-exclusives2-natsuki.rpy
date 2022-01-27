init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "呃...！"
    "我听见夏树在储藏间那里发出了一声窝火的声音。"
    "看起来她正在烦恼着。"
    "我走过去，看看她是不是需要帮忙。"
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "你在找什么吗？"
    $ style.say_dialogue = style.edited
    n 4x "操你妈aaaaaaaaaaaaaaaaaaaaaaaaaaaaa的莫妮卡！"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "莫妮卡讨厌鬼..."
    n "从来都把我的东西到处乱放！"
    n "如果有人老是把你的东西乱放，整理起来又有什么意义啊？"
    "夏树把书架上的漫画重新插进套装盒中。"
    mc "漫画..."
    n 2c "我记得你也看漫画，对吧？"
    mc "啊--"
    mc "...偶尔吧..."
    "漫画这种东西，在不知道对方的态度前，你不能直接承认自己非常喜欢它。"
    mc "...你怎么知道？"
    n 2k "我听你之前提起过。"
    n "而且，看你的表情就知道了。"
    "这是什么意思...？"
    mc "我-我知道了..."
    "在一个书架的边上，有一本漫画埋在了一堆各种各样的书中。"
    "我有点好奇，把它从书堆里抽了出来。"
    n 1b "原来它在{i}这里{/i}！"
    "夏树从我手里抢过了那本漫画。"
    "她转过身，把那本漫画按照册号重新插回漫画盒中。"
    n 4d "啊，舒服多了！"
    n "看着一套漫画里缺了一本可能是世界上最气人的事情。"
    mc "我懂这种感觉..."
    "我凑近看了眼她赞赏着的这套漫画。"
    mc "帕菲女孩...？"
    "我从没听说过这个系列。"
    "要么它不是我喜欢的类型，要么就是个粪作。"
    n 5g "如果你要品头论足的话，你可以在透过门上的玻璃朝外面说。"
    "她指着教室门。"
    mc "喂-喂，我可没又要评头论足...！"
    mc "我还什么都没说呢。"
    n 5c "你的语调已经表现出来了。"
    $ style.say_dialogue = style.normal
    n "但我要先告诉你一件事，[player]。"
    n 4l "这句话也适用于整个文学部：{nw}"
    $ _history_list[-1].what = "这句话也适用于整个文学部：不要光凭封面就评判一本书！"
    $ style.say_dialogue = style.edited
    n "不要光凭封 ffffff fff 面就ppppppppppppp 判一bbbbbbb{space=20}b{space=40}b{space=120}s{space=160}s{space=200}ssss书" #不要光凭封面就评判一本书！
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "实际上--"
    "夏树从盒子里抽出帕菲女孩的第一册。"
    n "我会告诉你为什么！"
    "她把漫画塞进我的手里。"
    mc "啊..."
    "我看着封面。"
    "上面画着四个盛装美少女摆出漫画女主角的姿势。"
    "这个...“萌”过头了。"
    n 4b "别傻站着！"
    mc "呜哇--"
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树抓着我的手臂把我拖出了储藏间。"
    "然后她靠墙坐下了，就坐在窗台下。"
    "然后在她拍了拍边上的地面，示意我坐在那里。"
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "椅子不是更舒服么...？"
    "我坐了下来。"
    n 2k "椅子不行。"
    n "那样就没法让我们两个一起读了。"
    mc "诶？为什么？"
    mc "啊...我知道了，两个人像这样更容易凑近一点..."
    n 2o "--！"
    n 5r "不-不要直接说出来！"
    n "让我都觉得怪怪的了！"
    "夏树交叉着手臂，挪远了一些。"
    mc "抱歉..."
    show natsuki 5g
    "我也没想到要和她坐得这么近..."
    "虽然这样也不坏啦。"
    "我打开了漫画。"
    "不一会儿，夏树又悄悄地挪了回来，似乎希望我没有发现她的动作。"
    "我能感觉到从身边透来的视线，其实夏树比我还想看这本漫画。"
    n 1k "哇，自从我上次读了这个开头已经过去多久了...？"
    mc "嗯？"
    mc "你不会时不时地回头翻一翻前面几册么？"
    n 2k "一般不会。"
    n "可能等到整个系列读完的时候，我会回去看一下。"
    n 2c "喂，你倒是有认真看漫画么？"
    mc "嗯..."
    "我正在看，但是没什么特别的桥段，所以我可以一边看一边聊天。"
    "感觉就是一群高中女生聚在一起。"
    "纯粹的日常剧情。"
    "我感觉自己有些厌倦日常系的作品了，因为这种类型通常缺乏剧情展开，很难让人产生兴趣。"
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...你这样坐着不会感到无聊吗？"
    n "并没有！"
    mc "即便你只是在这看着我读？"
    n "好吧...！"
    n "我...觉得没问题。"
    mc "既然你这样说的话..."
    mc "...可能把自己喜欢的作品推荐给别人，也蛮有趣的。"
    mc "我自己也会因为朋友在读我喜欢的漫画而高兴。"
    mc "你明白我的意思吧？"
    n "...？"
    mc "嗯？"
    mc "你不明白？"
    show n_cg1_exp2 at cgfade
    n "唔..."
    n "我...没有..."
    n "嗯，我不是很懂。"
    mc "...什么？"
    mc "你不和自己的朋友一起看漫画吗？"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "你能别这么直接说出来吗？"
    n "真是的..."
    mc "啊...对不起..."
    n "哼。"
    n "说得好像我有可以一起看漫画的朋友一样..."
    n "他们都觉得漫画是给小屁孩看的。"
    n "每当我提起漫画，他们的样子就像是在说..."
    n "“诶？你三岁小孩吗？”之类的。"
    n "真想揍爆她们的脸..."
    mc "呃，我知道有这种人的..."
    mc "说真的，能找到一个不对你评头论足的朋友已经够难了，更何况对方还要同样喜欢漫画..."
    mc "我已经差不多是个失败者了，所以我觉得自己会被慢慢吸引到败者组里。"
    mc "但对你这样的人来说可能会难一点..."
    hide n_cg1_exp3
    n "哼。"
    n "好吧，你说得还挺对的。"
    "{i}...等下，哪个部分？？{/i}"
    $ style.say_dialogue = style.normal
    n "我的意思是，我甚至都没法把漫画放在自己房间里..."
    # 修改对话文字风格
    $ style.say_dialogue = style.edited
    n "我爸看到这些东西后，绝逼会把我打得屁滚尿流。"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "我根本不知道我爸在发现这些后会怎么样。" # 覆写对话历史
    n "至少放在部室里挺安全的。"
    show n_cg1_exp3 at cgfade
    n "除了有莫妮卡这个什么都不懂的混蛋以外..."
    n "可恶！我难道就赢不了吗？"
    mc "嗯，但最终付出也有回报了，不是吗？"
    mc "我是说，至少我在这里，能够阅读这本漫画。"
    n "好吧，可是这又没解决我的问题。"
    mc "也许吧..."
    mc "但至少你也乐在其中，不是吗？"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...所以呢？"
    mc "啊哈哈。"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "天哪，你玩够了没有？！"
    n "你到底还读不读了？"
    mc "好吧，好吧。"
    "我又翻了一页。"
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "时间就这样流逝。"
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "夏树现在出奇地安静。"
    "我悄悄瞥了她一眼。"
    hide black with dissolve_cg
    "她似乎快要睡着了。"
    mc "喂，夏树..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "唔-嗯...？"
    "突然之间，夏树倒向了我。"
    play sound fall
    $ style.say_dialogue = style.normal
    mc "嘿-嘿--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "哦，天哪..."
    m 1d "夏树，你还好吗？"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "来，把这个吃了..."
    show monika zorder 2 at t21
    "莫妮卡从她的包里拿出了类似能量棒一样的东西。"
    "然后把它丢向了夏树。"
    "夏树的眼睛又一下子有神起来。"
    "她猛地一把抓起地上的能量棒，扯掉了外包装。"
    show natsuki zorder 3 at f22
    n 1s "我跟你说过不要让我吃——嗯..."
    show natsuki zorder 2 at t22
    "她连话都没说完，就把那东西塞到了嘴里。"
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "别担心，[player]。"
    m "她没事的。"
    m "只是时不时会出现这样的情况。"
    m 1a "所以我在包里都会给她准备一些零食。"
    m 5a "话说回来...！"
    m "我们何不就在现在分享诗呢？"

    return

