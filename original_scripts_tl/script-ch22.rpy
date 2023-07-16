image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "又是平常的一天，眨眼间已经到了社团活动的时间了。"
    "几天过去，我对文学部已经相当习惯了。"
    "走进部室，迎来的又是那熟悉的一幕。"
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "欢迎回来，[player]..."
    hide yuri_half2
    mc "啊，嗨，优里..."
    "我不太确定是因为我，还是因为优里的脸色..."
    "昨天的争吵的影响似乎依旧让氛围有些沉重。"
    y 2v "唔-唔..."
    "优里侧着头，视线在教室里徘徊。"
    "夏树正在一边看漫画。"
    "令人惊讶的是，莫妮卡还没有到。"
    "突然，优里抓着我的胳膊把我拉到了教室的角落。"
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "关于昨天的事..."
    y "我..."
    y 2v "我真的需要道歉。"
    y "以前从来没有发生过这样的事..."
    y 2t "而且...可能那个什么来了..."
    y "我昨天情绪上不是很好。"
    y 2w "请千万不要认为我们一直都是这样！"
    y "不光是我，夏树也一样..."
    show yuri 2t
    mc "优里..."
    mc "你能反省与道歉，我就已经很开心了。"
    mc "还是别太计较这件事了。"
    mc "就算是我才来这里几天，我也能感觉到昨天的异常..."
    mc "也许我们昨天只是因为第一次分享诗，所以有点过分敏感了。"
    mc "不过无论原因是什么..."
    mc "这件事并没有让我看轻你。"
    mc "不如说我早就认定你不会是个坏人了。"
    mc "更何况现在你在道歉，我就更肯定你不是真心那样做了。"
    y 3t "啊-啊..."
    y "[player]..."
    y 3u "别这么直白地说这种话..."
    y "会让我不小心太开心的。"
    y 1s "你能这样理解我真的非常感激..."
    y "你能加入社团也是。"
    y "有你在身边，一切似乎都明亮了起来，而且--"
    y 1t "呃--"
    y 4c "抱歉，我在说些什么...？"
    y "我只是--"
    show natsuki 2c zorder 3 at f33
    n "嘿，你们看见莫妮卡了吗？"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "啊--！"
    mc "没，我没见到..."
    mc "我也在想她去哪了呢。"
    show natsuki zorder 3 at f33
    n 5g "真是的..."
    n 5c "优里，我猜你也没见到她吧？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "优里很显然被夏树那样冷静地跟她说话吓了一跳。"
    y "没-没，我没见..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "天哪，这一点也不像她的风格。"
    n "我知道有点傻，但是我就是忍不住去担心她一下..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "怎么啦？"
    n "你这样看着我干嘛？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "唔-唔..."
    y "夏树，昨天的事..."
    y 3w "我-我只是想道歉！"
    y "我发誓我说的话都只是一时冲动！"
    y 3t "从现在起，我会更加尽力控制住自己的情绪的..."
    y "所以--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "优里，你到底在说些什么？"
    n "你昨天是做了什么吗？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...诶？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "天哪..."
    $ style.say_dialogue = style.edited
    n "不管你在在意什么事情，我觉得肯定没什么大不了啦。"
    n "我根本不记得有发生过什么。"
    n "你总是太计较那些无所谓的小事情了吧？"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "但-但是..."
    show yuri zorder 2 at t32
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "mibulls sailcloth blindsight lifeline anan rectipetality faultlessly offered scleromalacia neighed catholicate"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "你要是非要道歉我就接受啦，如果这样能让你好受些的话。"
    n "另外，我其实总是担心你在暗地里讨厌我或者别的什么，所以我能听到你坦诚布公还挺开心的。"
    n 2z "诶嘿嘿。"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "没-没有，怎么会...！"
    y "我不讨厌你..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "啊哈哈。"
    n "嘛，你是有点古怪，不过我也不讨厌你的。"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "夏树转向了我。"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "你的考验可还没完哦。"
    show natsuki zorder 2 at t33
    mc "嘿...！"
    "突然，门被猛地拉开了。"
    show monika 1g at l41
    m "抱歉！非常抱歉！"
    mc "啊，你来了..."
    show monika zorder 3 at f41
    m "我真不是有意迟到的..."
    m "希望你们没有担心我之类的！"
    show monika zorder 2 at t41
    mc "没有..."
    mc "好吧，其实夏树挺担心的。"
    show natsuki zorder 3 at f33
    n 1p "我-我可没有！"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "啊哈哈。"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...话说回来，你为什么迟到了啊？"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "啊..."
    m "嗯，今天的上一段时间是自习课。"
    m "说实话，我忘了时间..."
    m "啊哈哈..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "那也没道理啊。"
    n "你至少应该听到下课铃了吧。"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "那一定是因为被我练钢琴的声音盖过去了..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "钢琴...？"
    y "我之前还不知道你会弹钢琴，莫妮卡。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "啊，我还差得远呢。"
    m 1m "虽然有练了一段时间了，不过我的水平还不够好。"
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "但是..."
    y "你肯定也已经付出相当多的努力。"
    y "所以，我依旧很佩服。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "喔，谢谢你，优里～"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "偶尔弹几次给我们听听嘛！"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "啊哈哈，这就..."
    "莫妮卡看向了我。"
    m 1a "好吧，其实我正在写一首歌，不过还差一点..."
    m "也许等到我弹得稍微好些的时候，我会的。"
    show monika zorder 2 at t41
    mc "听起来好厉害。"
    mc "我很期待哦。"
    show monika zorder 3 at f41
    m 1b "真的吗？"
    m "那样的话..."
    m "我不会让你失望的，[player]"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "莫妮卡甜甜地微笑着。"
    mc "啊..."
    mc "我不是想给你压力之类的！"
    m 1a "啊哈哈，别担心。"
    m "我本来也在想着要弹给你（们）听的。"
    m "这大概就是为什么我最近加大了练习强度了吧。"
    mc "我明白了..."
    "我不太确定莫妮卡到底是指整个文学部，还是只弹给我..."
    mc "这样的话，祝你好运。"
    m 1j "谢谢～！"
    m 1a "话说，我没有错过什么吧，有吗？"
    mc "没...没什么。"
    show monika zorder 1 at thide
    hide monika
    "我觉得还是不要说我们三个刚刚发生的事比较好。"
    "另外，夏树已经跑到储藏间那边去了。"
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "唔..."
    y "你说的那些话让我很开心..."
    y "我在想也许我们今天可以一起做些什么。"
    y 3o "我是说--在社团里！"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "啊，我也觉得。"
        mc "毕竟你送了我那本书，我想我也没有什么理由拒绝。"
        mc "只是，我觉得我应该先确认夏树没有在等着我。"
        mc "昨天我们一起看完漫画后，她--"
        if n_appeal >= 2:
            y 3r "她没事！"
            $ style.say_dialogue = style.normal
            y 3h "她正在那边好好看漫画呢，你瞧？"
            $ style.say_dialogue = style.edited
            y 3f "不要总想着她了。"
            y "她已经习惯被无视了。"
            y "来吧，我们去那边。"
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            $ pause(2.0)
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "她-她没事！"
            y 3h "她正在那边看漫画呢。"
            y 3y6 "所以没关系的，对吧？"
            mc "啊--"
            mc "那这样的话，我觉得没问题..."
    else:
        $ y_appeal = 2
        mc "嗯，当然可以。"
        mc "我本来也是这么打算的。"
    show yuri zorder 2 at h11
    y 3y5 "好！"
    y "那我们开始吗？"
    y "我们去找个地方坐--"
    y 3n "啊-啊--"
    y "我会不会，有点强迫你了...？"
    y 4c "真是对不起！"
    y "我的心...因为一些原因，跳得很厉害..."
    mc "别想太多了。"
    mc "这样不是显得更元气满满了嘛。"
    y 3q "是-是啊！"
    y "但是..."
    y 3j "我真的需要冷静一下。"
    y "不然我没办法专心读书..."
    mc "慢慢来。"
    "优里做了一个深呼吸，随后从书包里拿出了一本书。"
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("你解锁了一首特别诗篇。\n现在要看看吗？", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "好了，各位！"
    m "大家分享完诗了吧？"
    $ config.mouse = None
    m "我们今天需要商量点事，请大家都坐到房间的前面来..."
    show natsuki 3c at f31 zorder 3
    n "是关于学园祭的吗？"
    show natsuki at t31 zorder 2
    show monika 1j at f32 zorder 3
    m "嗯，差不多~"
    show monika 1a at t32 zorder 2
    show natsuki 1m at f31 zorder 3
    n "呃...我们必须准备学园祭吗？"
    n "似乎没办法在短短几天内就整出什么像样的东西来啊。"
    n "可能到头来，我们只会变得很难堪，也吸引不了新成员加入。"
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "我也有这种担心呢。"
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "我并不擅长临时抱佛脚..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "别担心那么多啦！"
    m "我们就简单地来，好吗？"
    m 2a "看..."
    m 2m "我知道大家自从 [player] 加入之后都变得更加的...有活力...而且我们也开始了一些社团活动。"
    m 2d "但是现在还不是自满的时候。"
    m "我们还是只有四个社团成员..."
    m 2a "而且学园祭是我们唯一真正的去招募更多人的机会，懂吧？"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "可是，招新又有什么好处呢？"
    n "如果只是想正式成立的话，我们已经有足够的社员了。"
    n "人越多只会变得更吵，也更难管。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "夏树..."
    m "我认为你根本没有正确地看待这件事。"
    m "难道你不想和更多人分享你的热情吗？"
    m 3e "启发他们找到当初同样把你带到这里的感情？"
    m "文学部应该是一个让人们自由表达自我的地方。"
    m "还应该是一个亲密得让人不想离开的地方。"
    m 2e "我知道你也是这样想的，对吧？"
    m 2b "大家都这么想的！"
    m "所以，这就是为什么我们应该努力在学园祭上做出点什么...哪怕只是不起眼的小事！"
    m "对吧，[player]?"
    show monika 2a zorder 2 at t32
    mc "啊..."
    show natsuki zorder 3 at f31
    n 42c "哦，天哪！"
    n "莫妮卡，你不能因为 [player] 不擅长回绝别人就利用他同意你啊。"
    stop music fadeout 1
    n 1c "莫妮卡，你品，你细品。"
    n "你真的觉得有人在加入文学部之前考虑过别人的事吗？"
    n "优里在 [player] 来之前连话都不说。"
    n 2b "至于我，我只是觉得留在这儿比在家好点罢了。"
    n "而 [player] 一开始甚至都对文学没什么兴趣。"
    n "就这。"
    n 4w "很抱歉，但你是唯一一个对招揽新人有兴趣的人。"
    n "我觉得现在这样就挺好的。"
    n 4q "我知道，你毕竟是部长，但你这次确实应该考虑一下我们其他人的意见。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "莫妮卡很明显被夏树的话吓了一跳。"
    play music t9
    m 1m "这...压根就不对啊。"
    m 2m "我敢肯定，优里和 [player] 也希望能多招一些新成员..."
    m 2p "...对吧？"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "我不知道优里怎么认为，但我其实不在乎。"
    "如果我表现得像莫妮卡期待中那样热切的话，那我就是在说谎。"
    "但是，如果救不救场取决于我的话..."
    mc "嗯--"
    show monika zorder 3 at f32
    m 1i "不。"
    m "夏树说的没错。"
    m 1g "这个社团..."
    m "其实只是一小部分人拿来散心的地方罢了。"
    m 1r "我为什么会觉得大家都会以我的角度来考虑呢？"
    show monika zorder 2 at t32
    mc "但是这也不是说我们反对找些新成员之类的..."
    show monika zorder 3 at f32
    m 1i "[player]，你到底是为什么才来的？"
    m "你当时希望从中得到什么？"
    show monika zorder 2 at t32
    mc "呃--"
    "我最好还是别说实话吧。"
    show monika at f32 zorder 3
    m 1p "其实..."
    m "如果没记错的话，你甚至没有不加入的选择。"
    show monika zorder 1 at thide
    hide monika
    "莫妮卡坐了下来，只是盯着她的桌子。"
    m "那这一切又有什么意义呢？"
    m "或许办这个社团一开始就是个错误？"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "夏树，看你干的好事..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "啥，我？"
    n 1s "我只是把我的想法讲出来罢了..."
    n "说实话又是罪了？"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 2l "这和说实话没关系。"
    y "是你说话的方式有问题。"
    y 2h "另外，你也没有权力代表所有人..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "你懂个锤子啊！"
    n 5s "我只是..."
    n "我只是想要一个可以舒服地与几个朋友相处的地方而已。"
    n 5u "我希望这个社团是这样，有错吗？"
    n "现在...现在真的没有几个这样适合我的地方了..."
    n 5x "而且莫妮卡还想毁了它！"
    show natsuki zorder 2 at t31
    mc "她没想毁--"
    show natsuki at f31 zorder 3
    n 1g "你错了，[player]。"
    n "那不一样。"
    n 1q "如果按她的方向来，很快这里就会变味了。"
    n "如果我想那样，那我可能早就加入到别的什么弱智社团了。"
    n 12d "但这个社团..."
    n "至少..."
    n 12e "至少有那么一点点时间..."
    n "让我感到安心。"
    "夏树开始收拾自己的东西。"
    n 12d "我还是回家吧。"
    n "我感觉...我不再属于这里了。"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "夏树..."
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树无视了优里，径直走出了教室。"
    show yuri zorder 2 at t11
    y 3v "..."
    y "完蛋..."
    y "我该咋办啊..."
    mc "那么..."
    mc "你对学园祭有什么想法吗？"
    y 4b "我-我不知道..."
    $ style.say_dialogue = style.normal
    y "其实无所谓的吧，我觉得..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "谁在乎那个死缠滥干的玻璃心啊？"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "我的意思是，我喜欢现在这个文学部的样子，安静平和..."
    y "而且我只是...觉得和你在这里挺好的..."
    y 2t "不过！"
    y "我可是副部长啊..."
    y "我不该逃避我的责任..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "她就算是自裁了，也不会有人会为她哭。"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    $ pause(0.5)
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    $ pause(0.75)
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "我应该尽力考虑所有人的感受，然后去做正确的决定。"
    y 1t "那么你呢，[player]？"
    y "那在部室之外，你想做些什么？"
    "优里问了和莫妮卡相同的问题。"
    "我决定迂回一下，毕竟这比一言不发要好。"
    mc "...我认为最重要的是每个人都要和睦相处..."
    mc "...而文学部本身，则是提供一些独家的东西。"
    mc "我不觉得这取决于成员数量，而是成员的素质。"
    mc "这样才会让文学部最终变成一个特别的地方。"
    y 1u "我懂..."
    y "你说的没错呢。"
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "每个成员都以自己独特的方式为社团做贡献。"
    y "随着成员的成长，社团的面貌也会逐渐改变。"
    y 1h "我不觉得这一定是件坏事。"
    y "只是稍微离开一下自己的舒适区的话..."
    y 1a "所以如果你希望帮助莫妮卡准备学园祭的话，我也会帮忙的。"
    hide blood_eye2
    mc "可以。"
    mc "嗯，也许我们明天可以和夏树好好谈谈..."
    "优里点了点头。"
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "嘿，优里..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "诶？"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "唔，我知道昨天的气氛有点尴尬..."
    m "但是我还是应该告诉你，其实你是个很棒的副部长。"
    m 1e "而且，也是个很棒的朋友。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "莫-莫妮卡..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "为了让文学部变成最棒的社团，我会尽我一切努力的。"
    m "好吧？"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...我也会的。"
    show yuri at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "嗯..."
    m "那我们今天就先回家吧。"
    m "明天再讨论关于学园祭的事情。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "好的。"
    y "我很期待呢。"
    y 1a "[player]，那现在走吗？"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "嗯--"
    m 1p "别误会了，我..."
    m "我想在离开之前和 [player] 说几句话。"
    m 1d "只是问问他这段时间以来的感受之类的事情..."
    m "作为部长，这对我来说挺重要的。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "优里看起来有点不高兴，但是她没有反对。"
    y 2t "好吧。"
    y 2s "我相信你的判断，莫妮卡。"
    y "那么，明天见。"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "明天见~"
    show yuri zorder 1 at thide
    hide yuri
    "莫妮卡向正在离开教室的优里挥了挥手。"

    show monika 2a zorder 2 at t11
    m "呼..."
    m 2e "最近的事情变得有点麻烦了，不是吗？"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player]，我只希望你在俱乐部过得开心。"
    m "我不愿意看到你不开心的样子。"
    m 2m "我觉得这大概是我作为部长的责任..."
    stop music
    m 4e "而且我真的很在乎你...你知道吗？"
    m "我不喜欢看到她们让你为难。"
    m 4r "尤其是夏树有点太刻薄..."
    m 4m "另外优里也有点...你懂的。"
    m 5a "啊哈哈..."
    m "有时候感觉就像是只有你和我两个真人一样。"
    m "你懂吧？"
    m 1g "但是挺奇怪的，你在这都这么久了，我们几乎都没有单独相处过。"
    m 1n "啊...我..."
    m "虽然只有几天..."
    m 1l "抱歉，我不是故意说一些奇怪的话的！"
    m 1e "其实有些事情我早就想和你说了..."
    m "一些只有你才能理解的事情。"
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "所以这就是为什么--\"{space=5000}{w=0.75}{nw}"
    m 1g "等等，我还没说完啊！\"{space=5000}{w=0.5}{nw}"
    m "别啊！\"{space=5000}{w=0.5}{nw}"
    m "快停下！\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return

