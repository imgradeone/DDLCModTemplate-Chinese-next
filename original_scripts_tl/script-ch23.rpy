image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        $ pause(7)
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "嗨，[player]！"
    y "我一直都在等你呢。"
    y 2d "你准备好继续看书了吗？"
    y "我今天带了最好的茶--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "莫妮卡！"
    n "我告诉过你不要--"
    n 1g "呃..."
    n "她又迟到了吗？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "你还是和平常一样肆意妄为啊，夏树。"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "什么？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "你就那么喜欢用你无休无止的嚎叫打断我的对话吗？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "你在说些什么啊？！"
    n 1q "你意思是，我每天都会这样吗？"
    n "我刚刚真的只是没太注意，好吗？我错了。"
    n 4u "说真的...你最近到底怎么了？"
    if n_appeal >= 2:
        n "你听我说..."
        n "我已经反思过昨天的行为了。"
        n 2q "我确实说得有点过分了..."
        n 1q "一定是我当时觉得被吓到了之类的。"
        n 1h "我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，除非他们性格差到爆..."
        n 5w "我觉得这次再来一个女生的话，也挺好的..."
        n 5u "所以..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "夏树..."
        $ style.say_dialogue = style.edited
        y 1f "没人在乎的。"
        y "您咋不试试钻到售货机底下捡捡硬币呢？"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "--！"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        $ pause(1.0)
        show monika 1g at l31
        m "哦，天哪..."
        m "我又是最后一个到的！"
        show yuri zorder 3 at f32
        y 1f "你又去练钢琴了？"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "是啊..."
        m "啊哈哈..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "那你的毅力可真强哦。"
        y "组织这个社团，还要挤出时间练钢琴..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "嗯，也许不是毅力..."
        m 3a "我觉得是热情驱动着我。"
        m "它也激励着我更努力地准备学园祭呢。"
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "我？"
        y 2o "没-没有吧..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "我真的很异常吗...？"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "看到了吗，{i}绝对{/i}有问题。"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "我会克服的！"
        y 3y6 "这都不是什么值得一提的事情..."
        y 3o "我只是觉得有些紧张..."
        y 3n "总-总之，别讨论这个啦！"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "嗯，我只是觉得我需要把这件事讲出来罢了。"
        n 5q "我其实也没那么在意..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "哦，天哪..."
        m "我又是最后一个到的！"
        show natsuki zorder 3 at f33
        n 2c "嗯，[player] 也刚刚才来。"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "你又去练钢琴了？"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "是啊..."
        m "啊哈哈..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "那你的毅力挺强的。"
        y "组织这个社团，还要挤出时间练钢琴..."
        show yuri 1a at t32 zorder 2
        show monika at f31 zorder 3
        m 1a "嗯，也许不是毅力..."
        m 3a "我觉得是热情驱动着我。"
        m "它也激励着我更努力地准备学园祭，还有..."
        m 3n "嗯..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "好吧..."
        m "我-我忘记了些东西..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "呃，说到这个，夏树..."
        y "我们昨天又谈了谈，然后..."
        y 2t "嗯...我们应该支持学园祭的活动。"
        y 2l "不过...！"
        y 2h "我理解你不希望社团改变的感受。"
        y "我们都和你的感受差不多。"
        y 2f "所以只要我们齐心协力，这个社团就永远不会成为我们不喜欢的样子。"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "唔，还有..."
        y "如果你也能帮忙来准备学园祭的话..."
        y 3r "...我会买一部新的漫画送给你！"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "啊哈哈哈！"
        n "抱歉，你最后那段话真的很好笑哇。"
        n 2c "不过，你听我说..."
        n "我已经反思过昨天的行为了。"
        n 2q "我确实说得有点过分了..."
        n 1q "一定是我当时觉得被吓到了之类的。"
        n 1h "我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，除非他们性格差到爆..."
        n 5w "我觉得这次再来一个女生的话，也挺好的..."
        n 5e "...但更重要的是，我可不愿意看到学园祭活动只是因为我没有加入才办得很糟！"
        n "你也知道我是个专家的！"
        n 5c "所以我也会帮忙的，确保万无一失。"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "谢天谢地..."
        y "莫妮卡，是不是很棒啊？"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...莫妮卡？"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "啊--"
        m 1n "是啊，那太好了！"
        m "你一定会帮上大忙的，夏树。"
    m 5 "总之，[player]..."
    m "你今天想要做些什么呢？"
    m "我在想，其实我们可以--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "我们今天已经有计划了。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "啊..."
    m "是吗，优里？"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "对啊。"
    y "[player] 正和我读一本小说读得起劲呢。"
    y 1y5 "我终于引导他进入文学的世界了，难道你不开心吗，莫妮卡？"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "我..."
    m "我以为..."
    m "只是--"
    m 1r "其实，这不重要的。"
    m 1i "真的没什么的。"
    m "你们想干什么都可以。"
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}（好耶！）{/i}{w=0.5}{nw}"
    y 2u "唔...谢谢你的理解，莫妮卡。"
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "好啦，各位！"
    m "是时候分配一下学园祭的准备工作了。"
    m 1i "让我们快点把这事弄完。"
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "天哪..."
        n "为什么今天的氛围这么奇怪？"
        n "你看，就连优里都不能免疫。"
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "唔..."
    y "死气沉沉的气氛，通常暗示着将要发生可怕的事情..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "好啦，能赶快搞定吗？"
    m 2d "我会去准备印刷和装订所有的小诗册。"
    if n_appeal >= 2:
        m 2i "夏树，你可以做一些纸杯蛋糕。"
        m "我知道你至少做这个还挺拿手的。"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "夏树，我只是说--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "我想做纸杯蛋糕！"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...嗯，好。"
        m "很高兴我们还在同一频道上。"
    m 3n "优里，你可以..."
    m 1r "...好吧，没事。"
    m 1i "做你想做的吧，只要你觉得对学园祭有帮助就行了。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "莫妮卡..."
    y "我又不是废人！"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "我-我知道啊！"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "我已经想好我要做什么了。"
    y 1h "没有合适的气氛，就没办法成功开好一个赏诗大会的。"
    y "所以我会去做些装饰，再去弄一些漂亮的灯光烘托气氛。"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "这个，好像？"
    m "是个不错的主意！"
    m 1a "那么现在所有人都有事情做了。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "诶？"
    y "那 [player] 呢？"
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 2b "[player] 会来帮我的忙。"
    show monika 2a at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "等等，帮你？"
    n "莫妮卡，你的工作最简单啊喂！！！"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1i "抱歉，但这就是安排。"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 1f "凭什么？！！"
    n "你到底想搞什么？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "我-我觉得夏树说得没错！"
    y "不仅仅是因为你的工作本身就更适合一个人完成..."
    y 3l "更何况我的工作更倾向于劳力，所以最适合有人来帮忙打下手。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "我的也是！"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "什么，你的小蛋糕吗？"
    y "就这？拜托。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "说得好像 {i}你{/i} 他娘很懂一样！"
    n 1x "你只关心如何把 [player] 拴在你和那本弱智才会看的书旁边吧。"
    n 1f "说的是你，{i}还有{/i} 莫妮卡！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "嘿！"
    m "我可什么都没做啊！"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "好啊，那就别滥用职权，让 [player] 自己决定去帮谁呗！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "我可没有...滥用职权啊。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "不，莫妮卡，你就是在滥用职权。"
    y "让 [player] 自己选，好吗？"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "OK，得！"
    m "随你便。"
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "天哪..."
    n "[player]，我知道你肯定已经受够他们两个了。"
    n 3c "我们可以--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "夏树，闭上你他娘的臭嘴！让他自己做决定，好吗？"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}你{/i}才该闭嘴！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "我的老天爷啊..."
    m 1i "这简直没完没了了。赶快做决定吧，好吗？"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("夏树。", "natsuki"), ("优里。", "yuri"), ("莫妮卡。", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m "耶，你选我了！"
    m "我们可以这周末在你家见面。"
    m "我保证这会很有趣的。"
    m "所以周日你方便吗？"
    show natsuki 1e zorder 3 at f31
    n "你他娘的在逗我吗？"
    n "这可一点都不公平！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "夏树，这非常公平。"
    m "这就是他自己的选择。"
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "不，这一点都不公平！"
    y "你就是把重活累活全分给我们，然后自己带上了 [player] 跑。"
    y "厚颜无耻！！！"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "优里，我都没给你分配工作。"
    m 2i "我都让你自己决定的。"
    m "你现在有一点点不讲道理。"
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "我又不讲道理了？"
    y 2y3 "啊哈哈哈哈哈！"
    y "莫妮卡，没想到你这么妄自尊大、自私自利！"
    y "每次你只要没能参与进来，就把 [player] 从我身边拖走，次次如此。"
    y 1y1 "你是嫉妒吗？"
    y "还是癫了？"
    y 1y3 "还是你对自己的憎恨溢了一地，就开始随便往别人身上泼呢？"
    y 1y4 "我给你个建议。考虑一下自裁怎么样？"
    y "对你的精神健康会有特大的帮助。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "优里，你说的话可有点吓人..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "夏树，咱们先撤吧。"
    m 1i "我认为她不想让我们在这里继续待着了。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "看吧，想让你们滚不是很简单嘛。"
    y "我仅仅只是想要和他再多独处那么一会。"
    y "这样的要求很过分吗？"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "优里跟在莫妮卡和夏树后面，走到教室门。"
    show monika 5a zorder 2 at t11
    m "嘿，[player]..."
    m "优里真的有点那啥，对吧？"
    show monika zorder 1 at thide
    hide monika
    "莫妮卡咯咯笑着被优里推出门外。"
    python:
        if renpy.android:
            try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/have a nice weekend!")
            except: open(os.environ['ANDROID_PUBLIC'] + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/")
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
            except: pass
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
            except: pass
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
            except: pass
        else:
            try: renpy.file(config.basedir + "/have a nice weekend!")
            except: open(config.basedir + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/")
            try: os.remove(config.basedir + "/hxppy thxughts.png")
            except: pass
            try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
            except: pass
            try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
            except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "终于啊。"
    y 2y1 "终于啊！！！"
    y 2s "这就是我真心想要的。"
    y 1y6 "[player]，没必要去和莫妮卡一起度过整个周末了。"
    y "没必要听她的。"
    y 1y5 "就来我家吧。"
    y 3y5 "一整天，就我们两个人..."
    y "听起来不是很棒吗？"
    y 3y1 "啊哈哈哈哈！"
    y 3y4 "哇哦...我是有什么地方不对劲吧？"
    y "但是你知道吗？"
    y 1y3 "我根本不在乎了。"
    y "我这辈子从来没感觉这么爽过。"
    y 1y4 "只是和你待在一起就已经远超我所能想象到的极致愉悦了。"
    y "我对你上瘾了。"
    y 3y4 "就像是如果不能和你呼吸同一片空气，我马上就会死一样。"
    y 4a "感觉不是超棒吗，有一个这么在乎你的人？"
    y "有一个愿意整个人生都以你为中心的人？"
    y 2y6 "但是如果这感觉真是这么好..."
    y 2y4 "那为什么会感觉越来越可能发生可怕的事情呢？"
    y 2y6 "也许这就是为什么我一开始还打算阻止我自己的..."
    y "但是这份爱慕太强烈了。"
    y 3y1 "我现在根本不在乎了，[player]！"
    y "我必须要告诉你！"
    y 3y4 "我...我爱你爱到发疯！"
    y "就像是我的每一寸肌肤...每一滴血液...都在尖叫着你的名字。"
    y 3y3 "后果是什么已经无所谓了！"
    y "莫妮卡有没有在听我也不管了！"
    y 3w "求你了，[player]，看看我有多爱你。"
    y 3m "我爱你爱到甚至偷了你的笔拿去自慰。"
    y 3y4 "我只想要扒开你的表皮，在你的体内游走。"
    y 3y6 "我想要让你永远属于我。"
    y "而我也只属于你。"
    y "听起来是不是很完美啊？"
    y 3s "所以，[player]，告诉我。"
    y "告诉我，你想成为我的爱人。"
    y "你接受我的告白吗？"

    menu:
        "接受。":
            jump yuri_kill
        "不接受。":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    $ pause(1.0)


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ renpy.save_persistent()
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...啊哈哈哈哈哈。"
    y "啊哈哈哈哈哈哈哈！"
    $ style.say_dialogue = style.normal
    y 3y5 "啊哈哈哈哈哈哈！"
    $ style.say_dialogue = style.edited
    y 3y3 "啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1

    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)

    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3

    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)

    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5

    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    hide blood
    hide blood2

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    $ renpy.save_persistent()
    python:
        _history_list = []
        m.add_history(None, "", """欢迎加入文学部！我一直梦想着，可以为我热爱的事物做些特别的事情。既然你成为了社团的一员，那么你就可以帮我在这个可爱的游戏里实现梦想！你每天都可以和四个可爱而又特殊的社团成员闲聊、进行有趣的活动：纱世里，青春而又阳光，将幸福视为最重要的东西；夏树，这个外表看起来可爱的女孩，可能随时都会给你自信一击；优里，害羞而又神秘，在书的世界中寻找到了慰藉；……当然还有，莫妮卡，文学部的部长！就是我！我超级期待你能和所有人交上朋友，帮助文学部成为所有成员的贴心之处。我已经能看出来你是个小甜心了——你能保证和花最长的时间和我在一起吗？欢迎加入文学部！我一直梦想着，可以为我热爱的事物做些特别的事情。既然你成为了社团的一员，那么你就可以帮我在这个可爱的游戏里实现梦想！你每天都可以和四个可爱而又特殊的社团成员闲聊、进行有趣的活动：纱世里，青春而又阳光，将幸福视为最重要的东西；夏树，这个外表看起来可爱的女孩，可能随时都会给你自信一击；优里，害羞而又神秘，在书的世界中寻找到了慰藉；……当然还有，莫妮卡，文学部的部长！就是我！我超级期待你能和所有人交上朋友，帮助文学部成为所有成员的贴心之处。我已经能看出来你是个小甜心了——你能保证和花最长的时间和我在一起吗？欢迎加入文学部！我一直梦想着，可以为我热爱的事物做些特别的事情。既然你成为了社团的一员，那么你就可以帮我在这个可爱的游戏里实现梦想！你每天都可以和四个可爱而又特殊的社团成员闲聊、进行有趣的活动：纱世里，青春而又阳光，将幸福视为最重要的东西；夏树，这个外表看起来可爱的女孩，可能随时都会给你自信一击；优里，害羞而又神秘，在书的世界中寻找到了慰藉；……当然还有，莫妮卡，文学部的部长！就是我！我超级期待你能和所有人交上朋友，帮助文学部成为所有成员的贴心之处。我已经能看出来你是个小甜心了——你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我在一起吗？你能保证和花最长的时间和我""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/have a nice weekend!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ renpy.save_persistent()
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "好啦，终于是学园祭的时间啦！"
    show natsuki 4k zorder 2 at t11
    n "哇哦，你居然到得比我早？"
    n "我觉得我已经够早--{nw}"
    show natsuki scream at h11
    n "噫啊！"
    n "啊啊啊啊啊啊啊啊啊啊啊！！！"
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki at lhide
    hide natsuki
    "夏树飞速跑开了。"
    m "..."
    show monika 2b zorder 2 at t11
    m "我来啦！"
    m 2d "[player]，刚刚是不是发生了什么？"
    m "夏树刚刚跑了过去..."
    m 2i "...哦..."
    m "....哦。"
    m 2r "..."
    m 2l "啊哈哈哈！"
    m "嘛，真是难堪。"
    m 2d "等下，你难道整个周末都在这里吗，[player]？"
    m "天哪..."
    m 2g "我都没发现脚本已经崩坏到这个地步了。"
    m "真的非常抱歉！"
    m "那肯定很无聊吧..."
    m 2e "我会帮你清理干净的，好吗？"
    m "稍微等我一下就好..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    $ pause(1.0)
    m 2a "可以了。"
    m 2j "我现在想拿一个纸杯蛋糕了。"
    $ gtext = glitchtext(10)
    "莫妮卡揭开锡箔纸，从 [gtext] 的托盘里拿出了一个纸杯蛋糕。"
    m 2b "说真的，这些蛋糕相当美味！"
    m "我必须再吃一个，毕竟这是我最后一次有机会吃到它们了。"
    m 2a "我是说，在这些蛋糕还有其他东西的存在消失之前。"
    m "...不过总之，我真的不能让你再等太久了。"
    m 2j "稍微忍耐一下，好吗？"
    m 2a "应该只要几秒钟就好。"

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    return

