image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "纱世里"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file("../characters/monika.chr")
                renpy.call_screen("dialog", message="请不要玩弄我的心。\n我不想回来。", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character("monika")
    play music t2
    "平常的上学日，一如既往。"
    "就和平时一样，我被周围的现充包围着走到学校。"
    "我经常告诉自己，差不多是时候该找一个女朋友之类的了..."
    show sayori 1a at t11
    s "嘿，[player]..."
    "...好吧，其实已经有了。"
    "她叫纱世里，我的邻居，也是我儿时的玩伴。"
    "我们以前经常每天一起上学..."
    "...最近，我们又开始一起上学了。"
    s "[player]，你为我感到骄傲吗？"
    mc "诶？你说什么？"
    s 1c "就是..."
    s "我每天都能准时起床！"
    mc "好吧，可是你已经保持了一段时间了..."
    s "唔-哼！"
    s 4h "但你连提都不提！"
    show sayori at s11
    s "即便我们每天都一起上学..."
    mc "好吧，没错..."
    mc "我还以为你能懂的。"
    mc "让我大声说出来太丢人了。"
    s 1d "说嘛，好吗？"
    s "就当是给我鼓励～"
    mc "好吧，好吧..."
    mc "纱世里，我为你感到自豪。"
    show sayori at t11
    s 1q "诶嘿嘿～"
    show sayori zorder 1 at thide
    hide sayori
    "穿过马路后，我们继续向学校走去。"
    "走过拐角，映入眼帘的皆是路上熙熙攘攘的学生。"
    show sayori 3a zorder 2 at t11
    s "话说回来，[player]..."
    s "你决定好加入什么社团了吗？"
    mc "社团？"
    mc "我早就说过了，我对社团活动不——"
    "我开始老生常谈 - 我对加入任何社团都没兴趣。"
    "但我意识到这样说会伤到纱世里的心。"
    "这种情况下，我怎么能跟她说，社团根本是浪费时间呢.."
    "...更何况她建立了自己的社团？"
    mc "...实际上，嗯。"
    mc "我想我已经决定好社团了。"
    show sayori at h11
    s 1m "真的吗？！"
    s 1r "哪个社团？告诉我告诉我！"
    mc "嗯..."
    mc "这个就留作惊喜吧。"
    s 5d "噗..."
    s "小气鬼！"
    mc "耐心点，你很快就知道了。"
    "我过去常常问自己，为什么我会愿意让自己被这个无忧无虑的女孩说教。"
    "但我后来明白了，某种程度上来说，我羡慕她。"
    "当纱世里一心一意地去做时，她都可以完成很厉害的事情。"
    "所以这也是为什么，我觉得自己也应该为她做点什么。"

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包，我站起身，想给自己找点动力。"
    mc "我想想..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "我试着回忆起自己在社团宣传单上看到的房间号。"
    "我穿过学校、上了楼 - 我不常来学校这边, 这里通常是三年级学生和社团活动所使用的地方。"
    "很快，我就找到了那间教室。"
    "我轻轻地拉开面前的门。"
    scene bg club_day
    with wipeleft
    play music t3
    mc "大家好...？"
    show sayori 1m at t32
    s "啊！"
    s "[player]...？！"
    s 1c "你-你怎么来了？"
    mc "呃...我只是--"
    "诶? 我的目光扫视了一遍房间。"
    show natsuki 3a at f31
    n "唔。"
    n "所以你就是那个纱世里天天挂在嘴边的 [player] 吗？"
    show natsuki at t31
    show yuri 2t at f33
    y "欢-欢迎！"
    y 2m "很高兴认识你，[player]。"
    y "这里是文学部。"
    y 3v "希-希望这次的来访能让你愉快。"
    show yuri at t33
    show natsuki at f31
    n 3g "拜托，优里..."
    n "不要这么正式嘛。"
    n "他会以为我们这里很严格的..."
    show natsuki at t31
    $ y_name = "优里"
    $ n_name = "夏树"
    show yuri at f33
    y 3q "啊..."
    y "抱歉，夏树..."
    show yuri at t33
    "高个子女生就是优里，似乎比其他人要害羞很多。"
    "相反，那个叫做夏树的女孩 - 如果忽略她的个子的话 - 感觉更加有气势一些。"
    mc "嗯，很高兴认识你们俩。"
    mc "希望能和你们合得来的。"
    show sayori at f32
    s 1n "合-合得来...？"
    s 1b "[player]，难道说..."
    s "你要..."
    show sayori at t32
    mc "是的。"
    mc "纱世里，我想加入的社团就是你的社团。"
    mc "文学部。"
    "纱世里的眼睛亮了起来。"
    show sayori at f32
    s 1n "...怎么可能。"
    s 1s "怎么可能！"
    show sayori at hf32
    s 4s "哇啊啊啊啊！"
    "纱世里抱着我上蹿下跳。"
    show sayori at t32
    mc "喂-喂--"
    show natsuki at f31
    n 3y "诶嘿嘿。"
    n "好吧，如果纱世里这么高兴，我想你在这里也挺好的。"
    show natsuki 3a at t31
    show yuri at f33
    y 1s "更别说现在有四个人了。"
    y "文学部现在算是正式成立了。"
    show yuri at t33
    show sayori at f32
    s 1x "我都不知道该怎么说了！"
    s "必须庆祝一下！"
    show sayori at t32
    show yuri at f33
    y 1m "呼呼。"
    y "今天真是太棒了，不是吗？"
    show yuri 1a at t33
    show sayori at f32
    s 1r "是啊！"
    s 1x "而且，夏树决定要--"
    show sayori at t32
    show natsuki at f31
    n 1w "嘿，不许剧透！"
    show natsuki at t31
    show sayori at f32
    s 5a "诶嘿嘿，对不起..."
    show sayori at t32
    show natsuki at f31
    n 1k "所有人都来桌子这坐下，好吗？"
    show natsuki at t31
    show yuri at f33
    y 1a "我去弄些茶怎么样？"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们把几张课桌拼成了一张大桌子。"
    "夏树和优里则走到房间的角落，夏树端出来一个盖好的托盘，而优里打开了储藏间。"
    "我还是觉得有些尴尬，于是就坐在了纱世里的旁边。"
    "夏树趾高气扬地走了回来，手里端着托盘。"
    show natsuki 2z zorder 2 at t22
    n "哼哼，准备好了吗？"
    n "...哒哒！"
    show sayori 4m zorder 2 at t21
    s "哇哦！"
    "夏树掀开托盘上的锡箔纸，托盘上放着十二个小猫形状的白色、松软的小蛋糕。"
    "她用糖霜画出小猫的胡须，而小片的巧克力则被用来做成耳朵。T"
    show sayori at f21
    s 4r "好可爱～！"
    show sayori at t21
    mc "哇，看起来很棒。"
    show natsuki at f22
    n 2d "嗯哼哼，没想到吧。"
    n "快尝尝！"
    show natsuki at t22
    "纱世里马上拿起了一块，然后是莫妮卡，接着是我。"
    show sayori at f21
    s 4q "超好吃！"
    show sayori at t21
    "纱世里边吃边说着，脸上沾满了糖霜。"
    "我把蛋糕放在手里转了个圈，想找一个合适的角度下口。"
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "夏树默不作声。"
    "我不禁注意到了夏树偷偷瞄向我的视线。"
    "她是在等我咬下去么？"
    "我终于咬下了一口。"
    "糖霜甜度正好，风味十足——这真的是她自己做的吗？"
    mc "这个真不错。"
    mc "谢谢你，夏树。"
    n 42c "嗯-嗯...那当然啦！"
    n "毕竟我可是专业的！"
    n 42a "没必要感谢我什么的..."
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树扭扭捏捏地接受了表扬，优里回到了桌旁，端着一套茶具。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在蛋糕托盘旁边。"
    show yuri 1a zorder 2 at t11
    mc "你居然把一整套茶具都放在部室里了？"
    y "别担心，老师已经同意了。"
    y "而且，热茶配好书，不是很好嘛？"
    mc "啊...也...也许吧..."
    show natsuki 2y at f31
    n "诶嘿嘿。已经想给新成员留个好印象吗，优里？"
    show natsuki at t31
    show yuri at f11
    y 3n "诶？！不-不是的..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "优里红着脸，看向一边。"
    y 4b "我的意思是，那个..."
    mc "我相信你。"
    mc "嗯，虽然阅读和品茶并不是我喜欢的消遣活动，但至少茶我是可以欣赏的。"
    y 2u "那就好..."
    "优里宽慰地微微一笑。"
    y 1a "所以，[player]，你平时都有读些什么呢？"
    mc "这个...啊..."
    "考虑到我过去几年匮乏的阅读量，我真的不知道该如何回答。"
    mc "...漫画..."
    "我半开玩笑地小声嘀咕着。"
    show natsuki 1c zorder 2 at t41
    "夏树的头突然抬了起来。"
    "她似乎想说些什么，不过最后还是选择了沉默。"
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "不...不算是一个阅读爱好者呢，我猜..."
    mc "...呃，这也是可以改变的..."
    "我这是在说什么？"
    "我看着优里的苦笑，就情不自禁地说出了刚刚那句话。"
    mc "话说回来，你喜欢读些什么呢，优里？"
    y 1l "嗯，让我想想..."
    "优里的指尖描划着茶杯边缘。"
    y 1a "我最喜欢的是那种构建了深邃复杂世界的幻想小说。"
    y "它们背后的创造力和匠心水平，真是让我大开眼界。"
    y 1f "而且，能在那种陌生的世界观下叙述好一个故事，也同样令人钦佩。"
    "优里继续说着，显然对阅读充满热情。"
    "从我走进社团以来，她似乎一直很害羞和沉默，但从她亮起来的眼神可以看出，比起现实的人际关系，她更喜欢在书中寻求安慰。"
    y 2m "不过嘛，我喜欢的类型可宽泛了。"
    y 2a "如果你阅读量不多的话，不要觉得有压力，好吗？"
    y "我们肯定能找到别的共同点的。"
    show yuri at t22
    show natsuki 2c at f21
    n "嘿，优里..."
    show natsuki at t21
    show yuri at f22
    y 2f "诶？"
    show yuri at t22
    show natsuki at f21
    n 2h "就是，那个...他刚才说的..."
    show natsuki at t21
    mc "漫画？"
    show yuri at f22
    y 2i "是的..."
    y "夏树以前就在部室里面看漫画--"
    show yuri at t22
    show natsuki at f21
    n 1r "不-不要讲出来！！"
    "不知道为什么，夏树会因为自己看漫画感到很尴尬。"
    n 1q "何况..."
    n "漫画...不也是文学的一种吗？"
    n 1w "所以...如果 [player] 想要看漫画，那就让他看嘛！"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "夏树..."
    y "我不会这么做的。"
    y 1i "但是，不同的阅读兴趣可以让文学部更有多样性一点..."
    y "他同样可以利用这个机会读一些不同的东西。"
    y 1s "你不这么觉得么，[player]？"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "大-大概吧--"
    "感到气氛很紧张，纱世里插了进来。"
    s 1x "或许我们都能尝试一下新事物！"
    s 1l "我感觉这会很有趣..."
    s 1c "然后我们互相也会更加了解！"
    s 1l "我是说..."
    s "这不正是文学部需要的吗？"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "我-我同意..."
    show yuri at t33
    show natsuki at f32
    n 2j "是啊..."
    n "部长，你说什么都对。"
    show natsuki at t32
    show sayori at f31
    s 1q "诶嘿嘿～"
    show sayori at t31
    show natsuki at f32
    n 2c "似乎我得找本小说来读读了，嗯...？"
    show natsuki at t32
    mc "好吧，至少我们俩都可以读点小说..."
    mc "只要不是我一个人读就行。"
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "那么，至于优里..."
    show natsuki at t21
    show yuri at f22
    y 2n "诶...？"
    y "我...要我看漫画...？"
    show yuri at t22
    show natsuki at f21
    n 4i "天哪..."
    n 4h "不是你说的要有多样性嘛！"
    n "你思想应该更开明一些..."
    n 4u "而且那样很伤人的..."
    show natsuki at t21
    show yuri at f22
    y 2t "伤人...？"
    y 2v "我-我没意识到..."
    y "..."
    "优里低头沉思，脸上挂着满满的负罪感。"
    y 2w "夏树，对不起，我之前没有尊重你的喜好。"
    y "如...如果你喜欢它们，那应该也是一种文学。"
    show yuri at t22
    show natsuki at f21
    n 5q "...你在说什么？"
    show natsuki at t21
    show yuri at f22
    y "不是..."
    y "我只是认识到了自己的错误。"
    y 2t "所以，如果你愿意读一下小说..."
    y 2u "...那么我也愿意去试试看漫画。"
    show yuri at t22
    show natsuki at f21
    n 1l "真的？！"
    n 12c "我-我是说..."
    n "如果...你能为我去看一下漫画，我会很高兴。"
    n 2c "相信我，我会帮你会找到你肯定喜欢的漫画，好吗？"
    show natsuki at t21
    show yuri at f22
    y 1m "我也一样..."
    y 1h "活动结束之后我大概会去趟书店。"
    show yuri at t22
    show natsuki at f21
    n 1q "你...你一个人？"
    show natsuki at t21
    show yuri at f22
    y 3q "啊-啊--"
    y 4a "你愿意...和我一起去么？"
    show yuri at t22
    show natsuki at f21
    n 5s "唔..."
    n "如果你不介意的话..."
    show natsuki at t21
    show yuri at f22
    y 3t "完全不介意！"
    y "我以前都是一个人去的，所以..."
    show yuri at t22
    show natsuki at f21
    n "是啊，我也是..."
    show natsuki at t21
    show sayori 4s at l41
    s "真可爱啊～！"
    mc "住口啦, 纱世里..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "到时候我也会给你看一些漫画的，好吗？"
    show natsuki at t21
    show yuri at f22
    y 1a "好的。"
    y "我很期待哦。"
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "夏树和优里开始收拾起来。"
    $ config.skipping = False
    $ config.allow_skipping = False
    show sayori 1q at t11
    s "诶嘿嘿～"
    s 1x "我想今天的活动就到此为止吧，嗯？"
    mc "是啊，差不多了..."
    mc "大家能这样开心地在一起，真的很棒。"
    s 1q "不是吗？"
    s 1d "我觉得大家都喜欢你，[player]。"
    mc "你这么觉得吗...？"
    mc "好吧，有你在边上，大家似乎都开心了一些，纱世里。"
    s 1y "啊，[player]～"
    s "别这么说啦，弄得我有点害羞了！"
    mc "好吧，好吧。"
    mc "之前你告诉我要组建一个社团的时候，我都惊呆了..."
    mc "但现在看来，你做得很棒。"
    s 1r "我们会成为世界上最棒的社团！"
    s 1x "既然你已经加入了，那么每天都会很好玩。"
    stop music fadeout 2.0
    s 1a "嘿, [player]..."
    s "我真的很想谢谢你。"
    s "我是说，你能加入文学部我真的很高兴..."
    s "但实际上, 我早就知道你要加入了。"
    s 1q "诶嘿嘿～"
    s 1a "不仅如此。"
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "谢谢你让我们摆脱了莫妮卡。"
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "是的..."
        s "我知道她做了些什么。"
        s 1x "大概因为我现在是部长了吧。"
        s "但是哦，我真的什么都知道，[player]。"
        s 1q "诶嘿嘿～"
        s 1d "我知道你为了让大家开心，付出了多大努力。"
        s "我知道莫妮卡对我们做了很多让大家伤心的过分事情..."
        s 1b "但这些都无所谓。"
        s "这里只有我和你。{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "这里只有我和你。{fast}"
        hide room_glitch
        s 1d "而你会让我成为这个世上最幸福的女孩。"
        s "我等不及要和你一直这样生活下去了..."
        s "和你一起。"
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        $ pause(0.3)
        stop sound
        s 1q "永远永远..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "永"
        s "远"
        s "永"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        s "远"
        s "在"
        s "一"
        window show(None)
        stop music
        call screen dialog("不...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...嗯？"
        s "发-发生什么了...？"
        call screen dialog("I won't let you hurt him.", ok_action=Return())
        s "是谁..."
        s "停-停下——好痛——"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        $ pause(0.35)
        stop sound
        hide screen tear
        window show(None)
        s "啊--"
        call screen dialog("抱歉...我错了。", ok_action=Return())
        call screen dialog("这里终究没有快乐可言...", ok_action=Return())
        call screen dialog("再见了，纱世里。", ok_action=Return())
        call screen dialog("再见了，[player]。", ok_action=Return())
        call screen dialog("再见了，文学部。", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.35)
        stop sound
        hide screen tear
        scene black
        $ pause(3.0)
        return

    label ch40_clearall:
        s "我想谢谢你, 与我们共度了那么长的时光。"
        play music mend
        s 2d "为了让我们开心，你付出了那么多的努力。"
        s "在我们最困难的时候, 你鼓励我们。"
        s "帮助我们互相打开心结。"
        s 1a "你还不明白吗, [player]？"
        s "因为我现在是部长了嘛, 所以我什么都知道哦。"
        s 1q "你看来是真的不想错过游戏里任何一个细节呢?"
        s 1a "你不断地保存, 读取, 只为可以和每个人都共度时光。"
        s "只有真正在乎文学部的人会这样做。"
        s "但是..."
        s 4d "但是, 这就是我想要的。"
        s "大家互相关心, 一起欢笑。"
        s 4q "啊哈哈..."
        s 1t "真是的, 气氛怎么一下子有点伤心了？"
        s "你为我们付出了那么多, 而我却无以为报。"
        s "因为游戏到这里就结束了。"
        s 1y "所以..."
        s "我们就在这里道别吧。"
        s 1d "感谢您游玩 {i}心跳文学部{/i}。"
        s "我会非常，非常想你的，[player]。"
        s "记得偶尔回来看看, 好吗？"
        s "我们会永远在这里等你回来。"
        s 1t "我们..."
        scene black with dissolve_cg
        s "我们永远爱你。"
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return

