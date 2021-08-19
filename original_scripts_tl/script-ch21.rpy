label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "[player]，咱们又见面啦！"
    m "我还以为你会放我们鸽子呢。哈哈哈！"
    mc "不会的，别担心。"
    mc "我至少还是个守信的人嘛，虽说这么自夸有点奇怪。"
    show monika zorder 1 at thide
    hide monika
    "好吧，我又回到了文学部。"
    "我到得最晚，其他人都已经在闲聊了。"
    show yuri glitch2 zorder 2 at t32
    y "谢谢你信守了诺言呢，[player]。"
    y "希望这个承诺对你来说不至于太过沉重。"
    y 1u "逼着你你在还不熟悉文学的时候就一头扎进去..."
    show natsuki glitch1 zorder 2 at i33
    n "拜托哦！说得好像他可以偷懒一样！"
    n 4e "你已经是被莫妮卡拉来的了。"
    n "我不知道你是打算过来随便看看的，还是什么别的..."
    n "不过你要是不把我们当回事的话，那你就完蛋了。"
    show monika 2b onlayer front at l41
    m "夏树，你管得也真宽啊，明明自己都把漫画收藏放在部室里了。"
    n 4o "M-M-M...！！"
    show monika onlayer front at lhide
    hide monika onlayer front
    "夏树不知该说\"莫妮卡\"还是\"漫画\"才好。"
    show natsuki at h33
    n 1v "漫画也是文学！！"
    show natsuki zorder 1 at thide
    hide natsuki
    "迅速败下阵来的夏树跌坐回了她的座位。"
    show yuri 2s zorder 2 at t11
    y "抱歉，[player]..." # 二周目 part start
    y "我们会尽力让你在社团里感到舒适的，好吗？"
    show yuri 2g
    "优里向夏树投去了责备的一瞥。"
    y 1a "呃，不管怎样..."
    y "现在既然你已经是社团的正式成员了..."
    y "...也许你会有兴趣挑一本书来读读看？"
    mc "唔..."
    mc "我也没理由拒绝对吧。"
    mc "就像你说的，我已经是社团的一员了。"
    mc "所以，你说的没错，我是应该开始读点什么了。"
    y 4b "等-等一下..."
    y "我不是那个意思！"
    y "呃..."
    y "如果你真的不喜欢，那就当我没说过，就好吧..."
    mc "啊--不，不是那样，优里。"
    mc "我确实想要尽力成为社团的一员。"
    mc "所以即使我现在并不经常读书，我也很乐意听你的建议从现在开始读。"
    y 3t "你-你确定...？"
    y "我只是感觉..."
    y 3u "...呃，作为副部长的话..."
    y "...我大概应该让你从你喜欢的东西入手。"
    "优里把手伸进包里，掏出了一本书。"
    y "我希望你可以更快地融入进来..."
    y "所以我就找了本我觉得你可能会喜欢的书。"
    y "故事不长，所以即使你平时不怎么看书，也应该可以专注地读完。"
    y "而且我们可以，嗯..."
    show yuri at sink
    y 4b "一起讨论...如果你愿意的话..."
    "这-这..."
    "这个女孩怎么这么可爱呢？"
    "就连我这样不常常看书的人，她都去挑了一本她认为我会喜欢的书给我..."
    "我热情地接过了那本书。"
    show yuri 2m zorder 2 at t11
    y "呼..."
    y 2a "嗯，你可以按照自己的节奏来。"
    y "期待能听到你的想法。"
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "鉴于大家都已经到场，我本以为莫妮卡会开始主持已经安排好的社团活动。"
    "然而她并没有。"
    "优里已经把脸埋进了书里。"
    "我情不自禁地注意到了她那认真的表情，仿佛等待这次机会已久。"
    "与此同时，夏树在储藏间里到处翻找着什么。"


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "呼..."
    "终于结束了。"
    "我环视了教室一圈。"
    "气氛比我预想中的更压抑一些。"
    "就好像所有人都在挑剔我那平庸的写作水平..."
    "即使她们都在说客套话，我的诗还是完全没有办法与她们的作品相提并论。"
    "毕竟这里是文学部嘛。"
    "我叹了口气。"
    "看来我终归是作茧自缚了。"
    "房间的另一头，莫妮卡正在她的笔记本上写着些什么。"
    "我的目光随后转移到了优里和夏树身上。"
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "她们慎重地交换了纸张，分享着各自的诗。"
    show yuri 2i zorder 2 at t21
    "在她们一起阅读时，我在一旁注意着她们的表情变化。"
    "夏树失望地皱起眉头。"
    "与此同时，优里苦笑着。"
    show natsuki zorder 3 at f22
    n 1q "{i}（这文风是怎么回事啊...？）{/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "诶？"
    y "呃...你刚刚说了什么吗？"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "哦，没什么。"
    "夏树不以为然地把诗单手放回桌子上。"
    n "还算蛮秀吧。"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "啊——谢谢..."
    y "你的诗...挺可爱的..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "可爱？"
    n 1h "你是不是完全没理解我的象征手法？"
    n "这首诗很明显是在写放弃这种感受的。"
    n "这样的主题能用可爱来形容吗？"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "我-我当然注意到了！"
    y "我只是说..."
    y 3h "用词方面，大概..."
    y "我只是想说点好听的..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "诶？"
    n 4w "你的意思是，这首诗就连找点好听的话来形容都那么困难吗？"
    n "谢谢您嗷，你这话说出来实际上一点都不好听！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "唔..."
    y "好吧，我确实有几个建议..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "哼。"
    n "我要是想听建议，就会去找真正喜欢这首诗的人。"
    n "顺带一提，这首诗真有人 {i}喜欢{/i} 哦。"
    n 5e "莫妮卡喜欢。"
    n "[player] 也喜欢！"
    n "所以基于这些，我也乐意给你我的一点建议。"
    n "首先——"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "不好意思..."
    y "你的好意我心领了，不过我的写作风格是我花了大量时间建立起来的。"
    y 2h "我不想短时间内改变它，除非我遇到了什么特别激发我灵感的事情。"
    y "但迄今为止还没有。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "你...！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "而且 [player] 同样也喜欢我的诗。"
    y "他甚至还跟我说，我的诗给他留下了深刻的印象。"
    stop music fadeout 1.0
    "夏树突然站了起来。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "哦？"
    n "优里，我才发现你投入了很多精力去取悦我们的新成员嘛。"
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "诶-诶？！"
    y "我不是那个意思..."
    y 1o "唔..."
    y "你...你只不过是..."
    "优里也站了起来。"
    y 2r "你只不过是嫉妒 [player] 更珍视我的建议，而不是你的！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "哈！你又知道他没有更重视 {i}我{/i} 的建议了？"
    n "你就那么自负吗？"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "我...！"
    y "不..."
    y "如果我像你说的那样自负..."
    y 1r "...我就会故意把我做的一切都变得可爱过头！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "唔唔唔...！"
    n 1f "哼，你猜怎么着？！"
    n "某些人自从 [player] 一出现，胸部就神奇地大了一个罩杯！！"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "夏-夏树！！"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "呃，夏树，你说得是不是有点——"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "关你屁事！"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "把自己的不安情绪投射到别人身上..."
    y "你还真是太年轻了，夏树。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "又是 {i}我{/i} 了？看看现在是谁在逼逼赖赖，你这个欲求不满的神经质贱人！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "神经质...？"
    y 2r "很抱歉，相对于你的心理年龄而言，理解我可能对你这种人来说太难了！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "看到了吧？？"
    n "歪打正着！"
    n 4e "大部分人初中毕业后就学会克制自己了，可不像你。"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "想要教训我的话，你先收起你那四处招惹人的有病态度吧！"
    y "你以为你可以通过自己可爱的穿着和行为，来掩盖你那糟糕的性格吗？"
    y 1k "到最后你唯一看起来可爱的地方就只剩下你可怜地做这种无用功了。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "嚯，说这种话的时候小心点，优里，可小心话别太锋利，划伤了自己。"
    n "哦，抱歉，我的错...你不是已经在划了吗？"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "你-你刚刚是说我在割伤自己吗？？"
    y 3r "你他妈脑子是进水了吧！？"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "来啊，继续啊！"
    n "让[player]来听听你的真实想法！"
    n "当他听完以后，一定会被优里女神迷得神魂颠倒的咯！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "啊-啊--！"
    show yuri zorder 2 at t21
    "突然，优里转向了我，仿佛刚刚才意识到我站在那里。"
    show yuri zorder 3 at f21
    y 2n "[player]...！"
    y "她--她就是想让我难堪...！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "我才没有！"
    n "是她先挑起来的！"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}我当初怎么就被牵扯进来了呢？！{/cps}{nw}"
    "{cps=*2}我对写作一窍不通啊...{/cps}{nw}"
    "{cps=*2}不过不管我站在谁的一边，那个人对我的评价可能会更高吧！{/cps}{nw}"
    "{cps=*2}所以，当然是要选...！{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "夏树。":
                jump menu_click
            "优里。":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "嗯..."
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "嘿，[player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "我们何不\n先离开\n一下？"
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "好吗？"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "非常抱歉..."
    m "她们真的不应该把你牵扯进来的。"
    m 1e "对我们来说，也许不要搅和进去是最好的..."
    m "等她们不吵了我们再回去吧。"
    m 5 "啊哈哈..."
    m "真是个不称职的部长，对吧？"
    m 1m "我甚至都没办法正面处理部员的情绪..."
    m "我有时候也希望自己变得更强硬一点。"
    m "但是我实在不擅长反对别人..."
    m 1e "你能理解的，对吧？"
    m "总之..."
    m 1a "如果这能让你少花点时间在她们身上，那就太好了。"
    m 1j "我很乐意多陪陪你..."
    show monika zorder 1 at thide
    hide monika
    "突然，夏树跑出了教室。"
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "她很快跑远了。"
    show monika 1l zorder 2 at t11
    m "哦天哪..."
    m "...好吧，看来她们吵完了..."
    scene bg club_day2
    with wipeleft_scene
    y "我不是那个意思..."
    y "我不是那个意思..."
    y "我不是那个意思..."
    "优里用手捂着额头，不断地在她的座位前后摇摆着。"
    mc "优里...？"
    show yuri 4d zorder 2 at t11
    y "我不是那个意思！！"
    mc "我-我相信你..."
    "我完全无法想象优里可能对夏树讲了些什么。"
    "或者已经说了些什么。"
    y "[player]。"
    y "请不要因为这个讨厌我。"
    y "拜托了！"
    y "我从来不是这个样子！"
    y "今天的我一定是有哪里不对了..."
    show monika 1d zorder 3 at f31
    m "没事的，优里。"
    m "我们知道你不是那个意思。"
    m 1j "况且，我很确定夏树明天就会全忘了的。"
    m 1a "全都忘掉。"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "总之，今天的社团活动就到这里吧，你们想回家的话可以回去了。"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "优里看着我，似乎想要说些什么。"
    "但是她也不断瞟着莫妮卡..."
    show yuri zorder 3 at f32
    y 2v "你-你可以先走的，莫妮卡..."
    y "我想稍微多待一会。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "我是部长，所以我才应该是最后离开的那个。"
    m "我会等你弄完的。"
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "呃--我是副部长，所以..."
    y "今天就让我代行这个职责好了。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "听起来就像是你想做什么事，但是又不想让我在身边，优里。"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "不-不是你想的那样！"
    y 3o "不是那样..."
    y 3n "我只是..."
    y 3q "我只是都还没来得及和[player]讨论我的书..."
    y "你要是在一边听的话...也许会有点尴尬..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*叹气*{/i}"
    m 1d "这样的话，我也没得选了，不是吗？"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "我-我很抱歉给你添麻烦了..."
    $ gtext = glitchtext(20)
    y 1s "但是我真的希望你可以理{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "但是我真的希望你可以理{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return

