label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22_chs, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")
    y 2q "啊哈哈..."
    y "内容不是关键。"
    y "我的思维最近有些超级活跃了，所以我就用了你的笔把它写下来。"
    y 2o "啊--"
    y 2q "这只...是昨天从你书包里掉出来的笔，所以为了保管，我就把它带回家了..."
    y "我，唔..."
    y 2y6 "我只是...很喜欢...这支笔...写起来的感觉。"
    y "所以我就...用它...写了这首诗。"
    y "而现在你在摸着它..."
    y 2y5 "啊哈哈哈。"
    y 3p "我-我没事！！"
    y 3o "我刚刚..."
    y "..."
    y 4c "...我们可以当作没有发生过刚刚的对话吗？"
    y "不过你可以留着这首诗..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23_chs, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter)
    y "你喜欢它吗？"
    y "我是写给你的！"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "以防你看不出来，我先告诉你这首诗是关于[gtext]"
    y 1y6 "更重要的是，我给它赋予了我的气味。"
    y "看到了吗，我难道不是俱乐部里最体贴的人吗？"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    $ pause(0.2)
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "我..."
    y "我觉得我...想吐。"
    show yuri at lhide
    hide yuri
    $ pause(1.0)
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2_chs)
        n 2a "还不错，是吧？"
        mc "比起昨天那首要长多了。"
        n 2w "昨天那首太短了..."
        n "我只是热热身而已！"
        n 2c "希望你不会误以为那是我的上限。"
        mc "不，当然不会..."
        n 2a "不管怎么说，这首诗的主旨还是相当直白的。"
        n "我都怀疑需不需要我来解释。"
        n 2g "比如说，所有人都会认同这首诗的主题是一个愚昧的混蛋..."
        n "所有人都有某种奇怪的爱好，或者说一种内疚的快乐。"
        n 5q "某种你害怕别人发现、并且因此取笑或是看轻你的东西。"
        n 1e "...但是这只会让人变得愚蠢！"
        n "只要他们没有伤害到任何人，并且从中得到了快乐，谁在乎他们喜欢什么呢？"
        n 1q "我觉得人们真的需要学会尊重别人的奇怪爱好..."
        n 1x "...比如说就在这个社团里的某两位女生，我就不说出她们的名字了。"
        n 1s "讽刺的是，即便是在我感觉舒服的地方，也没有人尊重我..."
        n 1u "...天哪，你搞得我抱怨得太多了！"
        "{i}（...我做了什么啊喂？）{/i}"
        mc "就我个人来说，我是尊重你的..."
        n 1h "好吧--"
        n "那就谢谢了..."
        n 1s "...但是很明显地是，你更“尊重”优里，所以..."
        n 42c "算了...既然我们分享完了，那你现在可以走了。"
    return
label ch22_n_end2:
    call showpoem (poem_n2b_chs, revert_music=False)
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "为什么你今天不和我一起读呢？"
    n 1m "我一直在等你。"
    n "我等了你好久。"
    n "这是我今天唯一一件期待的事情。"
    n "为什么你要毁了它？"
    n "你是更喜欢优里吗？"
    n 1k "我觉得你最好不要和她交往。"
    n "你在听我说话吗？"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "优里是一个死变态。"
    n "现在应该很明显了。"
    n "所以和我玩吧。"
    n "好吗？"
    n "你并不讨厌我，[player]，对吗？"
    n "你讨厌我吗？"
    show natsuki_ghost_blood zorder 3
    n "你想让我哭着回家吗？"
    n "社团是我唯一一个觉得安全的地方。"
    n "不要毁了它。"
    n "不要毁了它。"
    n "求求你了。"
    n "只要别和优里说话。"
    n "而是跟我来玩。"
    n "我只有这些了..."
    n "陪我玩。"
    stop music
    hide n_rects_ghost3
    n ghost2 "快 来 陪 我 玩！！！"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    $ pause(1)
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    $ pause(0.5)
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    $ pause(0.25)
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    $ pause(0.5)
    show end:
        xzoom -1
    with dissolve_cg
    $ pause(2.0)
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23_chs, revert_music=False)
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(3.0)
    stop music
    hide screen tear
    show natsuki ghost_base
    n "我改变主意了。"
    n "请忘掉刚刚你读到的一切。"
    n "尝试做任何事情都没有意义。"
    n "优里那么让人讨厌都是她自己的错。"
    n "你听得见我说话吗，[player]？"
    n "如果你能花更多时间和莫妮卡在一起，那么所有这些问题都会消失。"
    n "对于你这样美好的人来说，优里和我实在太糟糕了。"
    n "从现在开始，只选莫妮卡。"
    n "只选莫妮卡。"
    hide natsuki
    $ style.say_dialogue = style.edited
    "只选莫妮卡。"
    menu:
        "只选莫妮卡。"
        "只选莫妮卡。":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "只选莫妮卡。", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "只选莫妮卡。" with Dissolve(0.5, alpha=True)
    $ pause(1.0)
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21_chs)
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22_chs, revert_music=False)
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    $ pause(2)
    show screen tear(20, 0.3, 0.3, 0, 40)
    $ pause(0.5)
    hide screen tear
    play music t5c
    m 5 "抱歉，我知道这样说有些抽象。"
    m "我只是试着...唔..."
    m 1r "算了，别在意。"
    m "解释没有意义。"
    m 1i "话说回来..."
    m 3b "以下是莫妮卡的今日写作小窍门！"
    m "有时候你会发现自己面对一个非常困难的抉择..."
    m "当这样的情况发生时，别忘了保存游戏！"
    m 3k "你永远也不会知道什么时候...唔..."
    m 3i "...我在和谁说话？"
    m "能听到我说话吗？"
    m 3g "告诉我，你能听到我说话。"
    m "什么都可以。"
    $ renpy.call_screen("dialog", "帮帮我。", ok_action=Return())
    m 3k "...以上就是我今天的建议！"
    m "感谢倾听～"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        $ pause(3.0)
    else:
        show black zorder 1
        $ pause(2.0)
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "天哪！真是吓了我一跳！{fast}"
    window auto
    m "唔..."
    m 1m "好吧，我觉得我似乎把，呃...“写”诗这件事搞砸了。"
    m "我只是想要..."
    m 1i "...算了。"
    m "我们进行下一步吧..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "..."
        n "害，果不其然啊..."
        mc "...？"
        n 2w "[player]，得了吧。"
        n "我又不傻。"
        n 2h "我知道你在优里身上花了多少时间..."
        n "很明显你更在乎给她留下印象，而不是努力提高写作水平。"
        n 2w "坦率地说，这有点可悲。"
        n 4h "为什么你要来这个社团呢，[player]？"
        n "老实说..."
        n "我原以为新加入一个成员可以让大家更多地参与到一起。"
        n 4s "而不是变本加厉地彼此排斥。"
        n 1u "这真是一个傻逼至极的活动..."
        n 12c "...听着，我今天心情不好，而且我现在也不想说话。"
        n "请你赶紧滚蛋。"
        $ skip_poem = True
        return
    else:


        n 1k "...唔。"
        n "我更喜欢你上一首诗。"
        mc "诶？真的吗？"
        n 2c "是啊。我能看出来你这首大胆了一些。"
        n "但是你在这方面还是不够好。它没达到效果。"
        mc "你说的也许没错，不过我只是想要尝试不同的东西。"
        mc "我还在摸索过程中。"
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "...唔。"
        n 2k "好吧，不得不说它比上一首更好。"
        n "很高兴能看到你的努力。"
        mc "那就好..."
        label ch22_n_med_shared:
            n 2c "只要确保你能受到每个人的一些影响就行了。"
            n "我觉得你至少有些受到了优里的影响，不是吗？"
            n 5q "我是说，我知道你一直，比如说..."
            n "和她待在一起，或是别的什么..."
            n 1w "但是你知道的，莫妮卡和我也跟她一样好！"
            n 1q "我的意思是，在诗词方面！"
            n 1h "所以你真的应该试着学些什么，否则你永远都不会进步的！"
            n "这是我写的..."
            n "我会确保你能从中学到些东西的。"
            return


    elif n_poemappeal[0] == 0:
        n "...哼。"
        n 2k "好吧，它不比你上一首差。"
        n "但我也不能说它比上一首好。"
        mc "呼..."
        n 2c "嗯？你“呼”什么？"
        mc "啊...只要不是那么不堪，我都会当作是胜利。"
        mc "而且我觉得你大概是最挑剔的。"
        n 1p "嘿-嘿！是什么让你--"
        n 1q "{i}（等等，刚刚那句也许是表扬...？){/i}"
        n 4y "啊-啊哈！真高兴看到有人意识到了我的丰富阅历！"
        n "那么，只要你继续练习，也许有一天你也会像我一样好的！"
        mc "那...呃..."
        "我怀疑夏树完全误解了我的意思。"
        jump ch22_n_med_shared
    else:


        n "...哼。"
        n 2c "好吧，它还不算太糟。"
        n "不过在看过你的上一首诗之后，这首还是相当让人失望的。"
        n 2s "但话又说回来，如果这首诗跟你上一首一样好，那我会气疯的。"
        mc "好吧，我只是想这次尝试些稍微不同的东西。"
        label ch22_n_med_shared2:
            n 2c "很合理。你还是新手，所以我也不会指望你一下子就找到自己的风格。"
            n "我是说，社团里的每个人的写作方式都大不相同..."
            n "可能你会受到我们所有人的一些影响。"
            n 2q "举个例子..."
            n 5q "我注意到你今天和优里待了一会儿..."
            n "并不是说我在乎你和谁待在一起。"
            n 5w "毕竟我一直都被教育着，永远不要期待从任何人身上得到任何东西。"
            n 5s "所以我也不是在等你什么的。"
            n 5h "不过，你也至少应该看看我的诗..."
            n "可能你可以从中学到些什么。"
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "我不会再读一首你那讨好优里的诗。"
        n 5s "但我还是会让你读我的诗。"
        n "这是有原因的。"
        n 5x "我也很希望我不需要这么做..."
        n "但不幸的是，我没有太多的选择。"
        n 5h "你就...仔细读它，好吗？"
        n "然后你就可以走了。"
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...搞咩啊。"
        n "我觉得你到头来，什么都没有学到。"
        n "老实说，我不知道自己为什么当初会抱有希望。"
        label ch23_n_bad_shared:
            n 42c "这明显就是受到了优里的影响..."
            n "我才发现你这么容易被影响到。"
            n "在社团里和她那么久地待在一起..."
            n "现在又试着像她那些写诗..."
            n 1s "真是愚蠢啊。"
            n "至少莫妮卡欣赏我的诗...."
            n 1r "...呃。"
            n 1q "好吧...我猜现在该把我的诗给你看了。"
            n "我真的很讨厌必须要这么做。"
            n "但不幸的是，我没有太多的选择。"
            n 1h "你就...仔细读它，好吗？"
            n "然后你就可以走了。"
            return
    else:

        n "..."
        n 2r "哦，天哪。"
        n "这真是一个大退步。"
        mc "诶？"
        n 2c "比起这首，我对你之前的两首要喜欢得多。"
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "...这首诗还行。"
        mc "还行？"
        n "是啊，至少比昨天的要好。"
        label ch23_n_shared:
            n 2c "我还是不知道你有多在乎写作，不过无所谓，你的表现还行。"
            n 4r "即便除了优里外，你基本不和其他人待在一起..."
            n 4h "我还是觉得，有大家都能参与的活动会好一点。"
            n 4w "所以你最好还是继续加油！"
            n "我是说..."
            n 1h "我知道我不是部长或者副部长之类的..."
            n "但是这并不意味着你可以让我失望，知道吗？"
            n 1q "那么，现在也读一读我的诗吧。"
            n "但是你要清楚一点..."
            n 1h "这首诗...对我有很大的意义。"
            n "所以请你仔细读它，好吗？"
            return
    else:
        n "..."
        n 2k "...这首诗还行。"
        mc "还行？"
        n "嗯，是的。"
        n "差不多和昨天那首一样好。"
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "什么？"
    n "你把你的诗给过优里了？"
    n 4x "卧槽！"
    n "你们两个什么毛病啊？"
    n 1s "哼..."
    n "反正我也不想读它。"
    n 1r "你甚至都不想给我看，真是惹到我了。"
    n 1x "...呃。"
    n 1q "好吧...不管怎么说我还是要让你读的诗。"
    n "我真的很讨厌必须要这么做。"
    n "但不幸的是，我没有太多的选择。"
    n 1h "你就...仔细读它，好吗？"
    n "然后你就可以走了。"
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "我一直在等着呢..."
    y "我们来看看你为今天写了些什么。"
    y 3m "..."
    "优里微笑着做了个深呼吸。"
    y "我喜欢拿着它。"
    mc "...？"
    y 3p "啊，我是说--"
    y "这首诗很好！"
    y 3o "它，啊..."
    y 2q "...好吧，还有些你可以继续努力的地方..."
    y "不过问题不大。"
    y 2s "感觉你写的任何东西都是珍宝。"
    y 2d "啊哈哈..."
    y 2o "有点尴尬..."
    y "我-我们进行下一步吧..."
    y 2t "这是我写的诗。"
    y "你不用勉强自己喜欢..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "我一直在等着呢..."
        y "我们来看看你为今天写了些什么。"
        y 2e "..."
        y "......"
        "优里面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y "...你是怎么做到这么快上手的？"
        label ch22_y_good_shared:
            y 2v "就在昨天，我还在告诉你那些值得练习的技术..."
            mc "可能原因就是这个..."
            mc "你解释得很棒。"
            mc "我也很想试着加入更多的意象。"
            show yuri 4b zorder 2 at t11
            "优里明显地吞咽了下口水。"
            "甚至她的双手也出汗了。"
            y 4e "啊-啊..."
            y "我真开心..."
            y 3y5 "被重视的感觉真好，[player]！"
            y "你写的一切对我来说都是珍宝。"
            y 3m "仅仅是拿着它都会让我心跳不已..."
            y 3q "啊哈哈..."
            y "我想写一首关于这种感受的诗..."
            y 3y6 "有什么不好的吗，[player]？"
            y "我没有表现得很奇怪，对吧？"
            y 3s "我-我现在比平时更难掩饰我的感情..."
            y 3m "我有点窘迫。"
            y 3y6 "不过现在，我只想让你也读我的诗。"
            y 3y5 "好吗？"
            return
    else:

        y 2b "我一直在等着呢..."
        y "我们来看看你为今天写了些什么。"
        y 2e "..."
        y "......"
        "优里面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y 2t "这首比昨天的还要好..."
        y "...你是怎么做到这么快上手的？"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "终于..."
    y 3y5 "啊哈哈..."
    show yuri 3m
    "优里把我的诗放到了她的脸上，深深地吸了口气。"
    y 3y6 "我喜欢它。"
    y "我喜欢它的一切。"
    y 3y5 "[player]，我想把它带回家。"
    y "可以让我留着它吗？"
    y "拜托？"
    mc "当然，我不介意..."
    y 2y5 "啊哈哈。"
    y "你对我真好，[player]..."
    y "我从来没有遇到过像你这么好的人。"
    y 2y6 "我会死的..."
    y 3y5 "别-别当真，只不过--！"
    y "我不知道该怎么形容。"
    y "这样的感觉没关系的，对吧？"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "并不太糟，是吧？"
    "优里把我的诗拿到了胸前。"
    y 3m "我会把它带回家，放在我的房间里。"
    y "我希望当你想到我拿着它时，你会感觉很好。"
    $ style.say_dialogue = style.normal
    y 3y5 "我会小心对待它的！"
    $ style.say_dialogue = style.edited
    y 3y6 "我甚至会在一遍又一遍阅读的同时自慰。"
    $ _history_list.pop()
    y "我会用纸割开自己，这样你的皮脂就会进入到我的血液中。"
    $ _history_list.pop()
    y 3y1 "啊哈哈哈哈哈。"
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "你也可以看看我的诗。"
    y "而且，在你读完之后，我敢肯定你也会想留着它的。"
    y 2y6 "给你，拿着吧。我等不及了。"
    y 2y5 "快点！读它！"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "嗨，[player]！"
    m "到目前为止，你在文学部过得开心吗？"
    mc "啊...还好。"
    m 1k "好！很高兴听到你这么说！"
    m 4a "顺便，由于你是新来的..."
    m "如果你对社团有什么建议，比如说新的活动，或是可以改进的地方..."
    m 4b "可以随时跟我说哦。"
    m "有事别怕提出来，好吗？"
    show monika 4a
    mc "好的...我会记住的。"
    "我不怕提出问题就怪了。"
    "在没有完全融入之前，我最好还是随波逐流吧。"
    m 1a "话说回来..."
    m "你想跟我分享一下你的诗吗？"
    mc "虽然有些尴尬，不过我想也只能这么做了。"
    m 5a "啊哈哈哈！"
    m "别担心，[player]！"
    m "我们今天都会有一点尴尬的嘛。"
    m "但我们很快就都能学会该如何克服它。"
    mc "是的，说得没错。"
    "我把我的诗递给了莫妮卡。"
    m 2a "...唔！"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    m 1a "话说回来，你想现在读一读我的诗吗？"
    m 1e "别担心，我的水平不是很好..."
    mc "你自称水平不是很好，但你的语气听起来还是自信满满的啊。"
    m 1j "好吧...是因为我的语气必须自信满满啦。"
    m 1b "这并不意味着我心里真的总是自信满满，明白吗？"
    mc "这样啊..."
    mc "好了，那我们来读你的吧。"
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "嗨，又见面了，[player]！"
        m "写得怎么样？"
        mc "还行吧，我觉得..."
        m 2k "我来看看。"
        m 2b "只要它不太差！"
        m 2a "我都为你的努力而开心。"
        m "也许你很快就会想出一篇杰作的！"
        mc "啊哈哈，我就不指望了..."
        m 2a "谁知道呢！"
        m "想跟我分享一下你为今天写的东西吗？"
        mc "当然...给。"
        "我把我的诗给了莫妮卡。"
        m "..."
        m "...没问题！"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene

    m 1a "不过话说回来..."
    m "你想现在读读我的诗吗？"
    m "我还挺喜欢这首诗的表现方式的，所以希望你也喜欢～"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene
    if y_appeal < 3:
        m 1a "话说回来..."
        if y_gave:
            m 1m "我觉得我们不用担心你的诗了..."
            m "优里至少应该在拿走之前礼貌地让你写完它。"
            m 1r "...好吧，算了。"
            m "如果她这么做会开心的话，那我也不会去拦她。"
            m 1a "对我而言..."
        m 1e "我真的非常...非常用心地写了这首诗，所以..."
        m "我希望它，呃，见效了。"
        m 1r "给..."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "我喜欢这首诗，[player]！"
    mc "真的吗...？"
    m 2e "它比我想象中的要可爱多了。"
    m 2k "啊哈哈哈！"
    mc "哦天哪...."
    m 1b "不是，不是！"
    m "它只是有点让我想起了夏树写的东西。"
    m "而她也是个好的诗人。"
    m 5a "所以你就当它是表扬吧！"
    mc "啊哈哈..."
    mc "既然你都这么说了。"
    m "是的！"
    m 3b "如果你对夏树感兴趣的话，那么你要在身上经常带点零食。"
    m "她就会像小狗一样粘着你的。"
    m 3k "啊哈哈！"
    m 1a "夏树的爸爸不给她午饭钱，也不会在家里给她留吃的，所以她常常都处在挑剔的情绪中..."
    m "不过有时候，她只是失去了所有的力气、变得麻木。"
    m "就像之前那样。"
    m 2d "这只是一个猜测，不过我觉得她长得这么小，就是因为营养不良影响到了青春期的发育..."
    m 2b "...不过，嘿，有些人也喜欢较小的女生，你知道的吗？"
    m 5a "抱歉...我只是想看到积极的一面！"

    return

label m2_yuri_1:
    m 1a "写得很好，[player]！"
    m "我读它的时候，脑子里都是“哦”这样的声音。"
    m 1j "真的非常有隐喻性！"
    m 1a "不知道为什么，不过我没有想到你会这么深入。"
    m 3b "我想我之前低估你了！"
    mc "大家最容易对我保持一个较低的期待值。"
    mc "这样一来，一旦我努力了，它就会变得很明显。"
    m 5a "啊哈哈！这可不太公平啊！"
    m "好吧，不管怎么说，我觉得它还是起效了。"
    m 2a "你知道优里喜欢这种文字的，对吧？"
    m "那种充满意象和隐喻的文字。"
    m 2d "有时候我觉得优里的思想是完全脱离现实的。"
    m "不过我并不是说这样不好。"
    m 2a "只不过有时候我的感觉会是，她对别人完全放弃了。"
    m "她花了那么多时间在她自己的脑海中，可能对她来说，那里才是更有趣的地方..."
    m 2b "不过这也是为什么，当你亲切地对待她时，她会变得那么开心。"
    m "我不觉得她习惯于被那样惯着。"
    m 2j "她肯定很渴求社交活动，所以也不要因为她表现地过强而责怪她。"
    m 2d "就像之前那样..."
    m "我想，如果她太兴奋的话，她最终会退出并寻找独处时间的。"
    "突然，门开了。"
    m 2b "优里！"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "我回来了..."
    y "我有错过什么吗？"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "没什么..."
    m "嗯，我们刚开始彼此分享诗。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "诶？"
    y "已经开始了吗？"
    y 2v "抱-抱歉我迟到了..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "不用道歉！"
    m 2a "我们还有很多时间，所以我很高兴你能慢慢来。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "好吧..."
    y "谢谢你，莫妮卡。"
    y "我想我现在应该去拿我的诗了。"
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player]，我觉得你之前看到了不该看的东西。"
    m "我本来不想告诉你，但是我现在觉得自己别无选择。"
    m 1r "你在优里那边花这么多时间，这是很危险的。"
    m 1i "我也不知道为什么，不过当她在你身边时，她似乎变得相当容易激动..."
    m 3d "这本身并不是问题。"
    m "但是当优里太激动时，她会找一个地方躲起来，开始用小刀割伤自己。"
    m 2e "这不就一团糟了吗？"
    m "她甚至每天都带一把不同的刀到学校来，似乎她有收藏之类的..."
    m 2d "我的意思是，这肯定不是因为她抑郁之类的！"
    m "我觉得她只是会从中获得快感。"
    m 2m "它可能甚至，就像是，性一样..."
    m 1i "但关键在于，你是在激活她。"
    m 1d "我可没说这是你的错!"
    m 1a "但是我觉得这就是为什么我需要向你解释这一切..."
    m "所以我在想，如果你跟她保持距离，那么对她而言可能是最好的。"
    m 5 "与此同时，不要羞于多花一些时间和我在一起..."
    m "坦白地说，至少我有在脑海中考虑过...而且我知道该如何对待我的社团成员。"
    return

label m2_yuri_3:
    stop music
    m 1i "可别说我没警告过你啊，[player]。"
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
