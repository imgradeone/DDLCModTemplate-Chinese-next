image exception_bg = "#dadada"
image fake_exception = Text("发生了异常。", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "今天就是学园祭了。"
    "虽然平时总是和纱世里一起上学，但是今天更特别。"
    "可纱世里没接我的电话。"
    "我考虑过直接去她家叫醒她，但又觉得似乎有点做过头了。"
    "与此同时，学园祭的准备工作应该差不多完成了。"
    if ch4_scene == "natsuki":
        "我小心翼翼地托着两个相叠的托盘，将蛋糕全带了出来。"
        "夏树的短信现在像风暴一样袭来，但是我的两只手都腾不开，根本没办法回复她。"
    else:
        "我和优里上色的条幅已经干了，我轻柔地将它卷好带了出来。"
        "她发来短信温柔地提醒我该带的东西，我也又检查了一遍让她放心。"
    "有趣的是，我对赏诗会的感受可能与夏树差不多。"
    "我更期待着表演结束之后与纱世里和[ch4_name_chs]逛学园祭。"
    "不过以我对莫妮卡的了解，赏诗会肯定会相当成功的。"

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]！"
    m "你今天第一个到呢。"
    m "谢谢你来这么早!"
    mc "好奇怪啊，我以为至少优里会在。"
    "莫妮卡正在将诗册摆满教室里的课桌。"
    "这些诗册肯定就是她周末准备的，里面收录了我们要朗诵的那些诗。"
    "最后，我还是随便在网上找了一首莫妮卡可能喜欢的诗，然后提交给了她。"
    "所以，一会儿我就要朗诵那首了。"
    m 1d "我有点惊讶你没和纱世里一起来。"
    mc "没，她又睡过头了..."
    mc "那个小笨蛋。"
    mc "我本来以为像今天这么重要，她应该再努力一些的..."
    "说是这么说，可是我忽然想起来纱世里昨天与我讲的那些话..."
    "我突然感觉很不安，我知道这对她来说应该没那么简单。"
    "而我只是说出了习惯性的想法。"
    "好像..."
    "或许我应该去她家里叫醒她的?"
    m 1k "啊哈哈。"
    m 4b "你应该再对她负责一点的，[player]!"
    m "我是说，尤其是在你们昨天的情感交流之后..."
    m "你算是把她晾在家里了，你知道吗?"
    show monika 4a
    mc "情感交流...？"
    mc "莫妮卡-- 你连这个都知道??"
    m 2a "当然知道。"
    m "毕竟我是社团的部长。"
    mc "但--!"
    "我甚至尴尬地结巴起来。"
    "纱世里真的这么快就把昨天的事告诉莫妮卡了?"
    if sayori_confess:
        "我们现在是...情侣的事情?"
        "我可还没有做向其他人公开的打算..."
    else:
        "昨天我拒绝了她告白的事？"
        "搞得我像是个坏人一样..."
        "但是拒绝确实对她来说更好，不是吗?"
    mc "天哪..."
    mc "事情和你想得不一样，所以..."
    m 2j "别担心。"
    m "我知道的可能比你想象的要多得多。"
    mc "呃...？"
    "莫妮卡和平时一样友善，但我听完后却觉得脊背开始阵阵发凉。"
    m 5 "嘿，你要不要来检查一下这些诗册?"
    m "我感觉做得还不错!"
    mc "嗯，可以啊。"
    "我随便拿起了一本桌上的诗册。"
    mc "嗯，确实挺好的。"
    mc "这些诗册这么精致，大家一定会更认真地看待社团的。"
    m "是啊，我也这么想!"
    show monika zorder 1 at thide
    hide monika
    "我翻了几页。"
    "每个成员的诗都工整地印刷在各自的分页上，看起来就像是专业的诗册。"
    "我认出了那天夏树和优里练习时所朗诵的诗。"
    mc "这个是...?"
    "我翻到了纱世里的诗。"
    "这首与她那天练习的不同。"
    "是一首我从没读过的..."
    call showpoem (poem_s3_chs, music=False)
    mc "啊--"
    "这是...？"
    "我读着这首诗，有点反胃。"
    show monika 1d zorder 2 at t11
    m "[player]？"
    m "怎么了？"
    mc "嗯，没什么..."
    "这首诗与纱世里的其他诗都完全不同。"
    "但不仅如此..."
    mc "我-我改主意了!"
    mc "我得先去接一下纱世里，所以..."
    m "啊--"
    m 1b "嗯，没问题!"
    m "别花太长时间，可以吗?"
    scene bg corridor with wipeleft
    "我迅速离开了教室。"
    m "别累坏自己～"
    "莫妮卡在后面喊道。"
    "我加快了我的脚步。"

    scene bg residential_day with wipeleft_scene
    "我早上都在想些什么？"
    "我本应为了纱世里多做一些事的。"
    "叫她起床，甚至只是等她一起来上学对我来说真的不算什么。"
    "就算只是陪她走去学校都能让她非常开心。"
    "而且..."
    "我昨天告诉她我对她会一如既往的好。"
    "对她来说这样就够了，我也一定会尽力做到。"

    scene bg house with wipeleft
    "我赶到了纱世里的家，并且敲起了门。"
    "我没指望会有回应，毕竟她也根本没接电话。"
    "就像昨天一样，我自己打开了门走了进去。"
    scene black with wipeleft
    mc "纱世里?"
    "她睡得真是沉啊..."
    "我咽了下口水。"
    "我不敢相信我真的做了。"
    "在她家里叫她起床..."
    if sayori_confess:
        "这确实是男朋友应该做的事情，对吧?"
    else:
        "这不更像是男朋友才应该做的事情吗?"
    "不管怎样..."
    "现在只能这样做了。"

    "我站在纱世里的房间外敲了敲门。"
    mc "纱世里?"
    mc "醒一醒啦，傻瓜..."
    "没有回应。"
    "我真的不想就这样走进她的房间..."
    "这算是侵犯隐私吧?"
    "但是她真的让我没其他办法了。"
    "我轻轻地打开了房门。"
    mc "{cps=30}.......纱世--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing.", False)
        except: pass
    $ pause(6.0)


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "怎么会这样...？"
    "{i}怎么会这样？？{/i}"
    "这是什么噩梦吗?"
    "这...这肯定是。"
    "这不是真的。"
    "这不可能是真的。"
    "纱世里绝对不会做这种事。"
    "就在几天前，一切都还和往常一样。"
    "所以我才不敢相信我的眼睛...！"
    scene black with dissolve_cg
    "我尽力压制着想吐的冲动。"
    "就在昨天..."
    "我还告诉纱世里我会守护她。"
    "我告诉她，我知道怎样才对她最好、一切都会好起来的。"
    "但为什么...?"
    "她为什么要这么做..."
    "我什么忙都没帮到吗?"
    "我到底做错了什么?"
    if sayori_confess:
        "向她告白吗..."
        "我本不该向她告白的。"
        "她根本就不需要这个。"
        "她甚至告诉我她被别人关心时是多么的痛苦。"
        "那我到底是为什么向她告白，让她更加痛苦的呢?"
    else:
        "拒绝了她的告白吗..."
        "肯定是这件事把她压垮了。"
        "她的尖叫还回响在我的耳边。"
        "当她最需要我的时候，为什么我却对她做了这样的事?"
    "为什么我是如此的自私？"
    "这都是我的错--!"
    "我不断地设想着所有我本可以做的事去阻止这场悲剧的发生。"
    "只要我再多花点时间陪她。"
    "陪她去学校。"
    if sayori_confess:
        "和她保持一直以来的朋友关系..."
    else:
        "接受她的告白..."
    "...那样我就可以阻止这件事的发生了。"
    "我知道我本可以阻止的!"
    "滚你妈的文学部。"
    "滚你妈的学园祭。"
    "我刚刚...失去了我最好的朋友。"
    "与我一起长大的人。"
    "她永远地离开了。"
    "我没办法让她复活。"
    "这并不是一个游戏，让我可以重来，去尝试各种选择。"
    "我只有一次机会，而我却大意了。"
    "现在我到死都会怀抱着这份罪恶感。"
    "我的生命中没有任何东西比她的更重要..."
    "但是我依旧无法以我的力量拯救她。"
    "并且现在..."
    "我永远无法重来了。"
    "永远。"
    "永远。"
    "永远。"
    "永远。"
    "永远..."
    $ in_sayori_kill = False


    return

