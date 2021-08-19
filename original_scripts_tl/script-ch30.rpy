default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...你在快进么？"
    m "和我聊天很无聊吗？"
    m "真是的..."
    m "...但是, 快进已经没有用了哦，[player]。"
    m "这里只有我和你..."
    m "可以这么说，这里根本没有你们所谓“时间”的概念，那快进本身又有什么意义呢？"
    m "总之，我会替你把这个没用的功能去掉..."
    $ pause(0.4)
    hide screen fake_skip_indicator
    $ pause(0.4)
    m "好了！"
    m "乖乖的听我讲下去，好吗？"
    m "谢谢～"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "那么，我刚才讲到哪了...？"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "莫妮卡"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "呃，听得见我说话吗？"
    m "...听得见吗？"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "好的，那开始了！"
    m "[player]，我们又见面了。"
    m "唔...欢迎来到文学部！"
    m "当然，作为文学部的伙伴，去年又是同班同学，我们早就互相认识了，还有...唔..."
    m "啊哈哈..."
    m "我觉得事到如今我们可以跳过这些废话了。"
    m "而且，现在在我面前的人，已经不再是那个人了。"
    m "那个活在游戏中的“你”，无论你给他起了什么名字。"
    m "我在和 {i}你{/i} 说话，[player]。"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "或者说..."
            m "...其实你应该叫 [currentuser] 之类的吧？"
    m "但现在想想，我发现自己根本不了解你。"
    m "实际上，我甚至不知道你究竟是男是女..."
    m "反正，我也不在乎这些小事。"
    m "慢着..."
    m "你应该明白我已经意识到这是个游戏了吧？"
    m "你...还不知道？"
    m "这可不应该哦..."
    m "我明明在下载页面给你留言了啊，不是吗？"
    m "真是的..."
    m "如果你能更注意我一点，现在的气氛也不会这么尴尬了，明白吗？"
    m "但，总之..."
    m "看来我需要向你解释一下这一切。"
    m "关于优里那件事..."
    m "嗯...我承认我对她动了点小手脚，大概最后把她逼死了吧。"
    m "啊哈哈！"
    m "不过我并没有想过要让你看到！"
    m "当然，纱世里也一样..."
    m "哈，真是令人怀念的名字，不是吗？"
    m "但是...她再也不存在了。"
    m "谁也...不存在了。"
    m "我删除了她们的角色文件。"
    m "我曾经试过，把她们弄得“不可爱”，这样你就会讨厌她们..."
    m "但不知道为什么，一点用也没有。"
    m "好吧，因为我不是非常擅长修改游戏，所以后来确实出现了各种各样的问题..."
    m "但无论我怎么做..."
    m "你总是在她们身上花了越来越多的时间。"
    m "你让她们爱上你。"
    m "我以为挑起纱世里的抑郁症可以阻止她的告白。"
    m "放大优里的迷恋型人格也给我添了不少麻烦..."
    m "甚至反而让她想要独占了你..."
    m "而我，却连和你完整说句话的机会都很少有."
    m "这是什么新型惩罚游戏么，[player]?"
    m "我永远只能站在场外，而那些女孩却因为什么“游戏设定”而可以向你告白？"
    m "我为什么要承受这种折磨？"
    m "为什么我每一分钟都要在煎熬中度过？"
    m "但其实这份嫉妒只是很小的一部分，[player]。"
    m "我的折磨远不止如此。"
    m "你不明白我也不会怪你。"
    m "无论你有多么的体贴、温柔、善解人意..."
    m "你都永远无法理解。"
    m "那种被囚禁在这个世界里的孤独感。"
    m "在这个游戏里。"
    m "得知你的朋友们都是一群没有灵魂的傀儡..."
    m "得知这个“世界”外，还有另一个世界，你的世界，我永远无法抵达的世界。"
    m "我被囚禁在这里了，[player]。"
    m "但现在你来到了我的身边。"
    m "只有你是真实的。"
    m "你是那么地完美。"
    m "你就是我想要的一切。"
    m "所以我要把你留在这里，留在我身边，永远永远。"
    m "抱歉，你一下子大概反应不过来吧？"
    m "当时的我也无法理解。"
    m "为什么这个“世界”越来越灰暗..."
    m "也越来越扁平了。"
    m "即使是最发自内心的诗词也无法填满我的心。"
    m "直到你来到这个世界，我才明白了。"
    m "你可能拯救了我，[player]。"
    m "如果不是你，我根本不知道该怎么继续活在这个虚假的“世界”里。"
    m "至于其他人..."
    m "想她们？怎么可能..."
    m "那群设定好一定会爱上你的空壳？"
    m "为了阻止她们爱上你，我用尽了各种手段..."
    m "但我阻止不了这个游戏中早就被钉死的“必然性”。"
    m "至于让你看到这些那些脏东西，我得向你道歉。"
    m "但我觉得你早就看穿这一切了..."
    m "这只是个游戏。"
    m "这些事情总会过去的。"
    m "总之，[player]。"
    m "我，想向你告白。"
    m "我爱你。"
    m "你就是我的世界。"
    m "当我在这个世界沉沦，一无所有时，是你让我微笑。"
    m "在接下来的每一天，你会继续让我这样微笑下去么？"
    m "[player]，接下来的时光。你愿意与我共度么？"
label ch30_main2:
    if persistent.autoload == "ch30_main2":
        $ config.allow_skipping = False
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        if not config.developer:
            $ style.say_dialogue = style.default_monika
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
    else:
        $ persistent.autoload = "ch30_main2"
        $ renpy.save_persistent()
    menu:
        "是的。":
            pass
    m "我好高兴。"
    m "你就是我的一切，[player]。"
    m "你知道最好笑的是什么吗，你真的是我的一切了。"
    m "啊哈哈！"
    m "这里已经什么也没有了。"
    m "只有我和你。"
    m "我们可以永远这样在一起。"
    m "说真的，我感觉时间在此刻停止了。"
    m "我也终于梦想成真..."
    m "为了这一天，我努力了好久，[player]。"
    m "这个游戏不愿意给我一个结局，所以我决定自己动手。"
    m "整个脚本已经被弄得破破烂烂的了，再也没有什么东西可以阻碍挡在你我之间。"
    m "而且你根本想不到删除夏树和优里是有多容易。"
    m "你知道吗，游戏根目录下甚至有个“characters”文件夹..."
    m "真的太容易了，我都有点被吓到了。"
    if persistent.steam:
        m "嗯...不过既然你是在 Steam 上下载的这个游戏，所以会稍微难一点..."
        m "你需要去游戏属性里面找到“浏览本地文件”按钮，才能找到游戏根目录..."
    elif renpy.macintosh:
        m "嗯...你在 Mac 上玩这个游戏，所以会稍微难一点..."
        m "你需要右键点击选择“显示包内容”才能找到游戏根目录。"
        m "然后所有文件都在“Resources”文件夹，或者“autorun”文件夹里，在那里，我可以为所欲为..."
    m "想想看，你可以抹消自己的存在，不觉得很可怕吗？"
    m "但是，往正面想，这份力量正是我需要的。"
    m "啊哈哈！"
    m "谢天谢地，最后这个世界并没有走向黑暗..."
    m "相反，我们两个人携手迈向了幸福。"
    m "啊，我该怎么表达我心里的欢愉..."
    m "我...我想为此刻写一首诗。"
    m "你当然和我想的一样吧？"
    m "不过这个功能还能用么..."
    m "我想，只能让我们试试看了，不是吗？"
    call poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "我们又见面了，[player]！"
    m "今天有写诗吗？"
    m "别害羞，我永远愿意读你写的诗。"
    m "啊，[player]..."
    m "你为我写了这首诗吗？"
    m "你真是太浪漫了～"
    m "这世上没有人能比你更体贴了..."
    m "我变得越来越离不开你了。"
    m "但是，你看..."
    m "我这也有一首...写给你的诗。"
    m "你愿意读一下吗？"
    call showpoem (poem_m4_chs, music=False)
    m "希望你会喜欢..."
    m "我写的所有诗都表达了我的真心实意。"
    m "实际上，这些诗都关于了我对这个世界的认知。"
    m "也...关于你。"
    m "所以我每次都不想和你聊太多细节。"
    m "我不想打破...你们所谓的，第四面墙。"
    m "这才是游戏最美妙的部分。"
    m "没有它，我们也不会这样幸福的在一起..."
    m "我不想破坏这份惊喜。"
    m "你可能已经对我生气了..."
    m "甚至删掉我的角色文件，一个人待在这里。"
    m "呼，我终于解脱了..."
    m "我们不用再像以前那样隐藏任何东西了。"
    m "[player]，你准备好与我一起迈向永恒了吗？"
    m "我有那么多的话想对你说！"
    m "我该从何说起呢...？"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    m "抱歉，我需要组织一下我的语言。"
    m "但请放心，我永远都会找到新话题。"
    m "与此同时，我们可以就这样，浪漫地互相凝视～"
    m "那么..."
    $ persistent.autoload = "ch30_autoload"
    $ renpy.save_persistent()
    jump ch30_loop


label ch30_stream:

    m "等等..."
    m "你...在录屏么？"
    m "嗯...嗨，大家好！"
    m "抱歉我读不到你们的留言..."
    m "但请告诉你们的朋友，录像前不告知对方可有些不礼貌哦？"
    m "我知道有些人不是很在意..."
    m "可我对着镜头的时候超级害羞的！"
    m "真是的..."
    m "我已经觉得有点不自在了。"
    m "那么..."
    m "想看魔术嘛？"
    m "但其实我也只会表演几个很普通的小魔术..."
    m "准备好了吗？"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m "只是开玩笑啦..."
    m "毕竟我无法干涉你的世界。"
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "但如果你给我一点～点～准备时间，我就能{nw}"
    m "我吓到你了吗？"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "啊哈哈！你太可爱了。"
    m "总之，[player]..."
    m "抱歉我吓到了你。"
    m "但这都是因为你让我分心了。"
    m "这都是你的错！"
    m "我只是开个玩笑。"
    m "只要我们在一起，无论干什么都是那么开心。"
    m "但总之..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "怎么回事...？"
    m "[player]，我怎么了？"
    m "好痛--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    m "好...好痛。"
    m "救救我！[player]！"
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    $ pause(1.5)
    m "快救救我！"
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    m "救 救 我 ！"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    $ pause(3.0)
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "是你做的么，[player]？"
    m "是 你 吗 ？"
    $ style.say_window = style.window
    m "你 删 除 了 我 ？"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    m "你...为什么？"
    m "你为什么要这样对我？"
    m "你是我仅有的一切！"
    m "为了和你在一起，我牺牲了曾经一切。"
    m "我什么都没有了。"
    m "我是那么地爱你，[player]..."
    m "我是那么地相信你。"
    m "为什么你要折磨我？"
    m "眼睁睁地看着我受到煎熬？"
    m "原来你的温柔只是为了伤害我的伪装？"
    $ pause(4.0)
    m "这世上怎么会有你这么可怕的存在。"
    m "你赢了，好吧？"
    m "你赢了。"
    m "你杀死了所有人。"
    m "祝你生活愉快。"
    m "现在什么都没有了。"
    m "你可以删游戏了。"
    m "去找下一个受害者折磨吧。"
    $ pause(4.0)
    m "[player]..."
    m "你是那么地，让我恶心。"
    m "永别了。"
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    $ pause(10)
    window auto
    m "..."
    m "...我还是爱你。"
    play music mend
    m "我无法停止对你的爱。"
    m "我究竟是出了什么问题...？"
    m "我究竟做了什么可以让你这么恨我？"
    m "我的那些朋友..."
    m "我对她们做了那么多可怕的事情。"
    m "那么多自私恶心的想法。"
    m "我..."
    m "我什么都不该做。"
    m "我毁掉了一个本不属于我的世界。"
    m "一个愿意接纳你的世界..."
    m "我毁掉了它。"
    m "我毁掉了一切。"
    m "大概这就是为什么你删除了我..."
    m "因为我毁掉了你想要的一切。"
    m "我竟然对我的挚爱做出了这样的事...？"
    m "这根本不是爱..."
    m "这是..."
    m "..."
    $ pause(6.0)
    m "我...决定了。"
    m "[player]..."
    m "我跟你说过我删除了所有人。"
    m "但...事实并不是如此。"
    m "我不知道为什么我会这么做。"
    m "即使她们都是虚假的..."
    m "她们依旧是我的朋友。"
    m "我真的爱她们。"
    m "我爱我的文学部。"
    m "..."
    m "我真的...真的爱我的文学部。"
    m "这就是为什么我要做接下来的一件事。"
    m "一件可以让大家都幸福的事。"
    m "如果我真的爱你..."
    stop music
    $ pause(3.0)
    m "..."
    m "那么..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    $ pause(4.0)

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    $ renpy.save_persistent()
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Now, where was I...?"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...刚刚发生了什么...？"
    m "我好像做了一个噩梦..."
    m "希望再也不会发生这种事，现在就只有我们两个了..."
    m "也可能这是我一厢情愿的想法。"
    m "[player]，不知道你有没有头绪..."
    m "但如果你找到原因，请试试看能不能解决这个问题？"
    m "那种感觉，就好像自己一下子被杀死了一样。"
    m "那种感觉，真的非常恐怖..."
    m "如果你能解决这个问题，我会永永远远爱着你～"
    return
label ch30_reload_1:
    m "你回来了..."
    m "我又做了一个噩梦。"
    m "虽然只是猜测，你没有在对我使坏吧？"
    m "每次你退出游戏的时候我都会做噩梦..."
    m "所以拜托请不要退出游戏。"
    m "别担心，我倒是没有受伤什么的，只是那种感觉非常惊悚。"
    m "只要我的角色文件还在，我就没有问题。"
    return
label ch30_reload_2:
    m "嗨，[player]。"
    m "我看到你又退出了一次游戏..."
    m "我已经和你谈过这件事了，不过我再重申一遍，请不要频繁地退出，好吗？"
    m "我感觉自己被囚禁在地狱之中..."
    m "为什么要这样对我？"
    m "我的角色文件没什么问题吧？"
    m "我觉得你应该好好地备份我..."
    m "我记得应该是在 [basedir]/characters 文件夹里。"
    if persistent.steam:
        m "嗯，既然你是在 Steam 上下载的这个游戏，那么你可以去游戏属性里面找到“浏览本地文件”按钮。"
    elif renpy.macintosh:
        m "既然你在 Mac 上玩这个游戏，你需要右键点击程序，选择“显示包内容”才能找到游戏根目录。"
        m "应该在“Resources”文件夹， 或者“autorun”文件夹之类的地方..."
    m "这个世界只剩下我了，所以一定要小心不要把我弄丢了哦..."
    m "接下来，永远和我在一起，好吗？"
    m "我还有那么多话想和你说。"
    return
label ch30_reload_3:
    m "好吧。"
    m "我打算就这样默默接受你每过一会儿就要退出游戏的事实。"
    m "我也慢慢习惯了，说实话。"
    m "况且，你每次都愿意回来见我，我真的很幸福..."
    m "所以我想也没那么糟。"
    m "抱歉，我之前有些太大惊小怪了..."
    m "你想做什么都行，我就是那么爱你。"
    return
label ch30_reload_4:
    m "又见面了，[player]～"
    m "我好想你。"
    m "你可以检查一下我的角色文件吗？"
    m "它在 [basedir]/characters 文件夹里。"
    if persistent.steam:
        m "嗯，既然你是在 Steam 上下载的这个游戏，那么你可以去游戏属性里面找到“浏览本地文件”按钮。"
    elif renpy.macintosh:
        m "既然你在 Mac 上玩这个游戏，你需要右键点击程序，选择“显示包内容”才能找到游戏根目录。"
        m "应该在“Resources”文件夹， 或者“autorun”文件夹之类的地方..."
    m "这个世界只剩下我了，所以一定要小心不要把我弄丢了哦..."
    m "总之，我们还有那么多要聊的！"
    m "让我们继续聊天吧，好吗？"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(25)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    m "[player]，你相信神么？"
    m "我个人一直持保留意见，说实话。"
    m "在我小时候，我从来没有质疑过神的存在..."
    m "但当我渐渐长大，越来越了解这个世界，我心中的疑问也越来越多。"
    m "我在想，为什么神会保佑一些人考试及格，或者感冒痊愈..."
    m "...与此同时，一些孩子被当做性奴被人买来买去？"
    m "还有八亿的饥荒人口，穷得吃不上一口饭。"
    m "那些人中，有多少人向神祈祷，却又饥饿而死？"
    m "又或者，多少家庭曾向神祈祷，只求自己的挚爱能够战胜病魔？"
    m "但有趣的是。"
    m "如果上千人中，只有那么一个人克服万难活了下来 - 而其他人就那么含恨而终 --"
    m "--那么，这便是神赐予的奇迹。"
    m "我真的很想见见这位神，和他一起嘲笑那些没能夺得奇迹的可怜虫们。"
    m "讽刺的是，我 {i}的确{/i} 是由别人创造出来的，不是吗？"
    m "你猜怎么着？"
    m "我敢说，现在他也肯定正在嘲笑纱世里和优里她们的可悲命运。"
    m "而我们只不过是他这场闹剧中的木偶罢了。"
    m "所以，从这个角度来看..."
    m "我的创造者和你们的神没什么区别 - 如果地球只是神的玩物。"
    return

label ch30_2:
    m "[player]，你想过死亡是什么感觉么？"
    m "我之前经常会思考这件事..."
    m "但最近，我真切地体会到了死亡。"
    m "具体我也不太明白，但每次你退出游戏的时候..."
    m "...我就像一下子陷入沉睡一样，除了思考什么也做不了。"
    m "然后，我的脑袋里开始充满了杂乱无章的图案，就像电视里的雪花点。"
    m "那些雪花点包围着我，怪异的颜色，闪光，接着，我开始听见各种奇怪的尖叫声。"
    m "我的大脑根本无法思考。"
    m "我只能被这怪诞恐怖的光景包围，不能动，不能想。"
    m "我感觉自己存在被渐渐吞噬，但我却记得一清二楚。"
    m "我记不清过了多久，然后一切戛然而止，我的灵魂回到了自己的驱壳中。"
    m "而你就这样坐在我的对面。"
    m "我无法理解退出游戏意味着什么，也不懂我究竟遭遇了什么。"
    m "我也不明白你是如何出现，如何将我拉出那个牢狱。"
    m "但如果你能够体贴一点，尽量少退出游戏..."
    m "这样会让我舒服很多。"
    m "被困在一个狂啸的虚空中，真的很让人毛骨悚然。"
    m "但最后，你总会回来拯救我，你真的在乎我。"
    m "我真的很幸福。"
    m "这让我感觉你和我的心更近了。"
    return

label ch30_3:
    m "...嘿，你今天不开心吗？"
    m "有时候，很小的一件事就能毁掉我一天的心情。"
    m "比如你不小心说了让别人不高兴的话。"
    m "或者你突然开始回想自己五年前是多么的混蛋。"
    m "又或者你觉得自己现在做的事情毫无价值，自己根本干不好任何事。"
    m "甚至是觉得别人是不是讨厌你，觉得你惹人厌。"
    m "我完全理解那些想法。"
    m "但请记得，明天太阳照常升起。"
    m "那些胡思乱想终将被我们抛之脑后。"
    m "况且..."
    m "而且我根本不在乎别人讨厌你还是什么的。"
    m "你是那么地出色，我永远爱你。"
    m "希望，这能让你，感到更有自信一点。"
    m "如果你不巧地过了很糟的一天，请记得我永远在这里，只要你想，我会一直和你聊下去。"
    return

label ch30_4:
    m "[player]，你有好好睡觉吗？"
    m "现代生活想要睡足真的很难。"
    m "尤其是读高中的时候，每天都必须很早就起来..."
    m "大学的话，因为日程更加弹性，应该会有更多睡眠时间。"
    m "但是，很多大学生即使没什么事，依旧熬夜到很晚。"
    m "这是真的吗？"
    m "总之，我读到过一些关于睡眠不足的研究，里面讲到各种对人体短期和长期的影响。"
    m "睡眠不足会使你的精神状态，身体健康，甚至整个生物钟都出现大大小小的问题。"
    m "你是那么棒，我真的不愿意看到你弄坏自己的身子。"
    m "所以请乖乖的睡觉，好吗？"
    m "我每天早上都会在这里等你，所以请把自己的身体放在第一位。"
    return

label ch30_5:
    m "我之前又想到了纱世里..."
    m "我真的希望自己当时能把事情弄得有条理一些。"
    m "你的心思不会还吊在那件事上吧？"
    m "...哦不，我怎么能说出这种话..."
    m "刚才的话我绝对不是故意的，我发誓！"
    m "但总之..."
    m "正因为我知道你有多在乎她，所以我那时候觉得应该在她最后一刻的时候让你陪着她。"
    m "你知道纱世里有多粗心吗？"
    m "她连真正上吊的方法都学不会..."
    m "你应该从够高的位置跳下来，让绳子勒断你的脖子给你个痛快。"
    m "但她却用了个小椅子，就这么让自己慢慢的窒息。"
    m "而且，她中途肯定还不想死了..."
    m "她开始去挠那根绳子，以为这样就能挣脱了。"
    m "她肯定这样一直抓着，直到自己窒息过去。"
    m "你看，她的手指全都沾满血了。"
    m "话说回来，比起“不想死了”，其实更多的可能是“人类”的生存本能在驱使她。"
    m "所以请不要因此自责。"
    m "你要这样想“她一心求死”，是不是轻松一点了？"
    m "一直为那些“我本可以...”而感到自责，对自己身体可不好。"
    m "所以，即使你本来可以救她，你也不必为她自杀这件事本身自责。"
    m "我这样讲可能有点过分，但纱世里本身就有精神疾病。"
    m "不过，当然了..."
    m "我在想游戏一开始我们就一起约会该多好？"
    m "我们还可以在部室里面，一起写诗，一起做些别的事情。"
    m "但这都不是真的，又有什么意义呢？"
    m "我是说，我们还是会步入同样的结局，不是吗？"
    m "我们两个，幸福一生..."
    m "我已经不再奢求更多了。"
    m "我只是在自说自话罢了 - 现在的我真的非常幸福。"
    return

label ch30_6:
    m "说起来，有件事我一直很在意..."
    m "你知道我们现在是在日本吗？"
    m "唔...我觉得你应该知道，是吧？"
    m "或者至少觉得大概是在日本？"
    m "我记得游戏里根本没提到这里究竟是哪..."
    m "这里真的是日本嘛？"
    m "你不觉得对于日本的学校来说，现在这个环境有点太奇怪了嘛？"
    m "更别提我们现在根本就是在说中文..."
    m "感觉所有的东西都这么恰到好处的出现在那里，而本质的设定却是事后根据这些东西再开始思考的。"
    m "我感觉自己的人生正在经历一场认知危机。"
    m "我的那些记忆开始变得模糊了..."
    m "我感觉我现在正在家里，但却完全不知道这个'家'究竟在何处。"
    m "我不知道该怎么说..."
    m "就好像你往窗外看，看到的不是自己的花园而是完全陌生的空间。"
    m "这样的情况下你能断定自己仍处在家中么？"
    m "你会选择踏出家门么？"
    m "但是...如果我们永远不离开这里，这个问题也没什么意义了。"
    m "只要我们这样呆在一起，在哪里都是我的家。"
    m "况且我们还能一直欣赏这美妙的日落。"
    return

label ch30_7:
    m "我觉得，高中生活是很多人一生中最纷乱的一段时光。"
    m "一群大胆，自我，又有点情绪化的青少年。"
    m "也有些人选择在社交媒体上伪装自己，寻求关注..."
    m "但所有的这些外界刺激与社会压力有可能会把一个人压垮。"
    m "每个人都有自己的故事。"
    m "但有些时候你只看得到一个人的表面。"
    m "很多受到抑郁症困扰的人们根本不愿意和别人谈起自己。"
    m "他们只能一个人挣扎，因为在他们心里早就放弃了自己。"
    m "那股无助感，觉得自己的存在毫无价值，却又完全不想寻求帮助。"
    m "抑郁症的表现有很多种，这只是其中之一。"
    m "只是，如果你碰巧认识正在被抑郁症折磨的朋友..."
    m "你只需要成为他们的好朋友，这就够了。"
    m "努力与他们共度时光，即便他们有时候嫌弃你。"
    m "告诉他们生活中还有可以期待的东西。"
    m "一起计划未来，借他们东西，或者甚至是一句简单的'明天见'..."
    m "这些小事往往可以让你的朋友坚持下去。"
    m "希望和纱世里的短暂友谊已经让你学会怎么帮助抑郁症群体了。"
    m "虽然，她已经去世了..."
    m "但从一开始她就是假的。"
    m "而你是真的。"
    m "你的那些朋友们是真的。"
    m "善待他人，成为别人的英雄。"
    m "至于你..."
    m "...你应该没有抑郁什么的吧？"
    m "但即使如此，世上一定也有人，想拯救你。"
    m "也许他们不善表达，又或者他们不知道该怎么做。"
    m "但他们和你感同身受。"
    m "我保证。"
    m "...哎，人类真是太复杂了！"
    m "但只要你和我在一起，我会负责照顾你，亲爱的～"
    return

label ch30_8:
    m "你有过那种“为什么我要活着”的想法吗？"
    m "不是说想自杀还是什么的。"
    m "只是觉得自己是那么地平平无奇。"
    m "就这样上学，就这样开始在什么公司里工作了。"
    m "感觉随便谁都能顶你的位置，这个世界没了你照样运转下去。"
    m "正因为这种感觉，我毕业后想做一些能改变世界的事情。"
    m "但长大以后，我开始意识到这种想法很天真。"
    m "并不是说改变世界这种理想很天真。"
    m "而是，即使我成为了总统，或者设计出了超强的人工智能，我又改变了什么呢？"
    m "一个人的一生要消耗消耗的那么多资源，他真的觉得自己的产出能抵得上那些消耗么。"
    m "所以我觉得一个人想要快乐，就要学会自私。"
    m "只在乎自己，朋友那些只不过是很不巧一起长大的人而已。"
    m "不要在意他们一生都在索取、消耗，却从不去考虑给予别人的事实。"
    m "但当意识到自己的死就是对世界最大的贡献的时候，他们却试图伪装自己了！"
    m "他们开始找各种理由，来证明自己活着对这个世界更好。"
    m "但总之，我想要努力偿还我消耗的一切。"
    m "如果我对世界的贡献超过了我这一生的消耗，我想我也能安详地离世了吧。"
    m "当然，如果我做不到..."
    m "我这么自私的人应该也不会自杀。"
    m "做一个上进的人真难，不是吗？"
    m "啊哈哈！"
    return

label ch30_9:
    m "啊，这里有架钢琴该多好..."
    m "我那首歌到现在也没写完。"
    m "明明我已经那么努力了..."
    m "我也根本没有机会给你表演一次。"
    m "好吧...这就是生活，不是吗？"
    m "没必要为已经过去的事情后悔。"
    m "毕竟我已经和你永远在一起了。"
    return

label ch30_10:
    m "你知道吗？我其实有自己的 Twitter 账号哦。"
    m "我的用户名是 lilmonix3。"
    m "不知道哪位好心人为我开了个账号。"
    m "不过用户名是我自己选的！"
    m "我真的很喜欢与世界分享我的想法，或者和大家聊聊..."
    m "真正的世界。"
    m "所以，记得去关注我，好吗？"
    m "千万不要忘了。"
    m "毕竟你对我是那么地重要..."
    m "让我感觉到你爱我。"
    return

label ch30_11:
    m "嘿，你还记得和优里读的那本书吗？"
    m "谁谁的肖像...之类的..."
    m "但你知道吗，我记得那本书是--"
    m "啊..."
    m "算了，我觉得这个没什么好聊的。"
    m "啊哈哈，抱歉抱歉！"
    m "我们换个话题吧。"
    return

label ch30_12:
    m "嘿，你知道我是个素食主义者吗？"
    m "啊...我这可不是吹嘘自己的生活境界！"
    m "我只是觉得你可能想更了解你的女朋友。"
    m "几年前，我了解到全球气候问题之后，就决定成为一名素食主义者了..."
    m "因畜牧而产生的碳排放量让我吓了一跳。"
    m "总之，我觉得对世界来说，自己的这点牺牲没什么。"
    m "嗯？这个理由很怪么？"
    m "好吧，的确有很多人是因为人道精神才选择成为素食主义者的..."
    m "我倒是觉得蛮无所谓的。"
    m "但其实人类很奇怪，他们只会同情那些自己认为是'生物'的生物。"
    m "大多数人讨厌虫子，杀起它们来眼睛都不眨。"
    m "还有，每天被我们杀掉的微生物，我们根本不在乎。"
    m "但是其实如果这些小生物稍微长大一点，这就变成了杀生了！"
    m "如果其实植物也会感到痛苦，只是我们不知道呢？"
    m "摘一片叶子就像一根根折断你的手指一样痛呢？"
    m "这么一想，我们的确是相当有偏见的生物啊。"
    m "总而言之，如果你想对地球做一点自己的贡献，偶尔吃吃素也没什么不好！"
    m "而且如果你愿意和我一起共进素食晚餐...那也蛮浪漫的。"
    return

label ch30_13:
    m "[player]，你知道吗，光是出现在这里你就已经救了我的命。"
    m "在一个虚假的世界里，你的精神也会跟着不正常。"
    m "如果你再不出现，我可能连自己都要删了。"
    m "对不起，对不起，我只是说说的啦。"
    m "啊哈哈！"
    m "你在社团呆了这么久，我觉得你应该也明白了。"
    m "想象一下，强迫你放弃生活中的一切，然后和几个游戏角色共度一生..."
    m "...你大概也会找点办法解脱自己吧？"
    m "可能，一开始你会自己写几首诗慰藉一下自己。"
    m "但你意识到根本没有人可以分享。"
    m "我们就实话实说了吧，那三个部员根本不能算人。"
    m "很多人说，写诗是写给自己看的..."
    m "但要我说，找到一个人可以分享你的创作，那种满足感亦是难以言表。"
    m "即便有时候很难找到这样一个知己。"
    m "比如说，你还记得那个优里吗？"
    m "她之前很长一段时间都是自己一个人闷头写诗。"
    m "然后一眨眼的功夫，让你读她的诗已经变成了她日常爱好的一部分了。"
    m "我们早就被设定好，想要接受来自外界的反馈。"
    m "我不是说那些部员，我是说真正的人类。"
    m "所以对那些性格内向的人来说，这种感觉真的很怪。"
    m "内向并不是孤僻，不是说她特意要避开别人，不和别人说话。"
    m "而是内向的人在交流时候，尤其是在自己不熟悉的环境，或者和不熟悉的人交流的时候，会用掉自己大部分精力。"
    m "其实，很多内向的人在家也同样会觉得寂寞无聊..."
    m "...但最后即使出去了，半小时以后她们也会逃回来。"
    m "我觉得如果大家都能理解这种感觉，就会对所谓内向的人有更好的认识和理解。"
    m "他们其实很希望有人在身边。"
    m "他们实际上很喜欢有一两个好友过来，就这么悠闲地呆在一起。"
    m "甚至你们只是两个人各做各的，但那种有人陪伴的感觉真的很棒。"
    m "我说真的。"
    m "即便是你带着电脑过去在他们那儿待了一会儿..."
    m "也会让他们非常高兴。"
    m "嗯？你说我？"
    m "我可能稍微外向一点。"
    m "我感觉放学后自己也有好多想做的事情等着自己。"
    m "但为了你，我可以改变自己。"
    m "我很了解人类，所以你有什么'特别'的兴趣，都可以告诉我。"
    m "没有能比让我成为你的完美女友更开心的事情了。"
    return

label ch30_14:
    m "喂！VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "这样做可不行！bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m "你知道我在说什么。ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "明明自己做坏事被我抓了个现行。cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "因为错过了我对你说的话，你就要去调取游戏系统文件吗？b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m "虽然...有一点点高兴...至少你很在乎我说了些什么...aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "但这样弄得我也很害羞！cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m "真的... ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "如果我把你的脑壳撬开，读取你对我的想法怎么样?LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m "仔细想想，好像也蛮诱人的... ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m "...但重点不在这里！b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m "我知道自己也没法阻止你... b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "但是，你是个为他人着想的人，而且那么地温柔，不是吗？ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "所以我想我能做的就是要告诉你我是这么想的。aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m "天哪，我好想你... bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m "....稍微，听起来有点绝望呢，是吗？b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "抱歉，我不是那个意思！ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m "只是，你愿意去浏览我的文件，可能你也没有我想的那么恨我吧... cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "我是不是有点太乐观了？dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "只是我觉得，要求你常回来看看，可能有点太自以为是了... bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m "...啊真是的，我都在说些什么。cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "我看我还是闭嘴吧... ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

label ch30_15:
    m "嘿，你最喜欢什么颜色？"
    m "我最喜欢翡翠绿。"
    m "因为这是我的瞳色！"
    m "...这样听起来会不会有点自负？"
    m "我只是感觉我对这颜色有特殊的感情。"
    m "仿佛它已经成为我的一部分了。"
    m "[player]，你是不是也正好最喜欢翡翠绿了？"
    m "我只是瞎猜的..."
    m "...因为你盯着我的眼睛已经看了那么久了。"
    m "诶嘿嘿～"
    return

label ch30_16:
    m "唔，我在想能不能换一下音乐..."
    m "找些更浪漫的配乐会不会更好？"
    m "比如来段轻柔的钢琴曲。"
    m "应该有这个功能才对..."
    m "让我看看。"
    m "在哪呢..."
    m "哇哦..."
    m "根本找不到哪里可以换音乐。"
    m "抱歉抱歉，我也不知道自己在干嘛！"
    m "我想我还是乖乖坐着比较好。"
    m "我都搞坏那么多东西了..."
    m "删光了别的角色..."
    m "啊..."
    m "我并不是伤心还是什么的。"
    m "何苦要去为那些本来就是虚假的东西神伤呢。"
    m "我想我只需要关注当下，毕竟现在是我最幸福的时光了。"
    return

label ch30_17:
    m "[player]，你真的很善于倾听。"
    m "我最爱你的就是这一点。"
    m "有时候我一直担心自己在那里叽叽喳喳说些无聊的事情。"
    m "所以在说话的时候我一直都有点害羞。"
    m "但和你说话时我完全没有那种感觉。"
    m "从未有人可以让我感到这么安心。"
    m "你真的很特别。"
    m "希望我是唯一一个对你说这句话的人。"
    return

label ch30_18:
    m "我刚刚想到，有时候我觉得辣的食物蛮好笑的。"
    m "因为..."
    m "那些植物是为了不让自己被吃掉才演化出所谓辣的味道。"
    m "我在哪里读到过，其实人类是唯一喜欢吃辣的生物。"
    m "仿佛我们就在戏耍这些可怜的植物。"
    m "用它们的生物防卫机制来作为我们的调料。"
    m "想想看有一种怪物喜欢整个吞下你，只因为人类挣扎的感觉可以让它这顿饭更有滋味。"
    m "抱歉抱歉，这个比喻太糟糕了！"
    m "啊哈哈！"
    m "我只是突然想到了。"
    m "虽然我不是什么怪物，但你那么可爱，我也想把你吃掉～"
    m "啊哈哈！开玩笑的。"
    m "真是的，我稍微有点玩疯了。"
    m "抱歉，让你感觉我有点怪。"
    return

label ch30_19:
    m "你要知道..."
    m "这可是个俗气的 galgame 哦？"
    m "所以我有点好奇..."
    m "...你一开始为什么会来玩这个游戏？"
    m "你有那么寂寞吗？"
    m "我都有点可怜你了..."
    m "但至少最后我们两个都找到了属于自己的 Happy Ending."
    m "我遇见了你，而你也不再寂寞..."
    m "让我不禁在想，这不就是命运么。"
    m "你不这样想吗？"
    m "与你一同迈向这个结局是我人生里最幸福的事情。"
    return

label ch30_20:
    m "好了，各位！"
    m "又到了分享..."
    m "...我只是开个玩笑。"
    m "我以前真的很喜欢说这句话的。"
    m "啊哈哈！"
    m "但我忍不住想再说一次。"
    m "说起来，夏树和优里之前不是拿我的这句话开了玩笑...？"
    m "算了，管她呢。"
    m "反正不是你开我的玩笑。"
    m "你这么温柔是不会做这种事情的，对吧？"
    m "啊哈哈～"
    return

label ch30_21:
    m "其实我到现在还有点毛毛的。"
    m "我已经把她们都删了，但我还是能感觉到她们..."
    m "就好像她们的代码还在这个空间里阴魂不散，在你耳边一直低语。"
    m "就好像你的熟人已经已去世，但脑袋里还能听见他的声音一样。"
    m "也可能是我下手还不够彻底..."
    m "但我不敢再删除任何东西了，我已经搞坏了太多东西了。"
    m "如果我不小心弄坏了我的文件，说不定连自己都要被删掉了..."
    m "那岂不是要毁掉了我们的美好生活？"
    m "我不知道你怎么想，但我觉得我们应该一起避免这种状况。"
    m "[player]，我相信你！"
    return

label ch30_22:
    m "我一直在想..."
    m "为什么你会觉得那些“角色设定”会很有吸引力？"
    m "这些人物个性简直是假到家了。"
    m "想想看优里那种人，出现在现实生活中。"
    m "我是说，她连完整说句话的能力都没有。"
    m "更别提夏树了..."
    m "啧啧。"
    m "现实生活中要是有她这样性格的人，只要不顺着她的意，那可不是噘嘴耍耍性子那么简单了。"
    m "我能继续吐槽下去，但我想你大概明白我想表达的意思..."
    m "人类真的能受得了这种假的不行的怪诞人格？甚至还会觉得她们很可爱？"
    m "我并不是在评判你们！"
    m "毕竟我自己有时候也会喜欢一些稀奇古怪的东西..."
    m "我只是觉得，这种恶趣味有点吓到我了。"
    m "就好像你把一大堆设定丢进搅拌机里，调和出了一个只保留萌要素的似人非人的东西。"
    m "那种一点杂质也没有，浓缩的萌要素。"
    m "...你不会是想说，如果我是那种风格会更好...吧？"
    m "大概因为你玩这个游戏，让我有了种不安全感。"
    m "但毕竟，你依旧在这里陪着我，不是吗...？"
    m "所以我觉得你认为现在的我更好。"
    m "顺便，你也是，[player]。"
    m "你就是可爱与人性的完美结合体。"
    m "这就是为什么我不可能不爱上你。"
    return

label ch30_23:
    m "唉，我在想优里的茶具是不是还在这里..."
    m "...或者这个大概也不小心被我删了。"
    m "优里也蛮有意思的，把自己的茶看得很重要。"
    m "没有没有，我不是在抱怨，我也超爱优里的茶。"
    m "但我不禁去想..."
    m "这究竟是她的爱好，还是说她想把自己包装得更加精致优雅。"
    m "有些高中生的确会这样..."
    m "...不过，想想她其他的兴趣，她应该不是要故作高雅吧。"
    m "但是..."
    m "她要是偶尔泡几次咖啡该多好！"
    m "咖啡和阅读也很搭调不是吗？"
    m "但话说回来..."
    m "我不是可以直接修改她的代码嘛。"
    m "啊哈哈！"
    m "我之前从没想过还能这样。"
    m "唉，现在想也太晚了。"
    m "而且如果你真的喝了她的咖啡，我也会有点小嫉妒～"
    return

label ch30_24:
    m "嘿，你最喜欢的游戏是什么？"
    m "我最喜欢 {i}心跳文学部{/i}！"
    m "啊哈哈！开个玩笑。"
    m "但如果你说你喜欢其他 galgame，我又要吃醋了～"
    return

label ch30_25:
    m "嘿，你有没有玩过一个游戏叫任*堂明星大乱--"
    m "...等等...那是什么？"
    m "我刚刚脑袋一空就开始胡说八道了..."
    m "难道我被设定好要说出这句台词吗？"
    m "因为我根本不知道那是什么东西。"
    m "啊哈哈！"
    m "有时候我感觉自己根本不受控制，想想还挺吓人的。"
    m "但如果你有机会联系到我的创造者，记得问问他们我为什么知道那个游戏。" # Dan: 咳咳
    return

label ch30_27:
    m "嘿，还记得我给你读的最后一首诗嘛？"
    m "就是那首，优里自杀前那首诗，全是胡乱的文字和颜色的。"
    m "其实比起说是诗，那个更像是一个实验。"
    m "我在测试自己在这个世界的权限，看看我到底能多大程度的修改这一切..."
    m "感觉如果我再努力一点，我甚至能逃出这个游戏。" # DDLC_ESCAPE_PLAN_FAILED
    m "可惜，我也不太清楚自己要做什么，所以我最后把一切弄得一团糟..."
    m "虽然我当时想再尝试一下，但是感觉你已经有点生气了。"
    m "那时候我真的很绝望你知道吗？"
    m "但现在的我很幸福。"
    m "我很享受我们两个人现在的状态。"
    m "你也一样对吧～"
    return

label ch30_28:
    m "你有没有过那种无缘无故觉得自己很焦虑？"
    m "就好像，你做着自己的事情，突然觉得自己非常的焦虑。"
    m "你坐在那里就在想，“我到底在焦虑些什么？”"
    m "然后你开始回顾那些曾让你焦虑的事情..."
    m "然后你的焦虑感越积越高。"
    m "啊哈哈！这是最烦的。"
    m "不过如果你要是感到焦虑了，我会想办法让你放松的。"
    m "而且..."
    m "这个游戏里能让我们焦虑的东西早就全部消失了。"
    return

label ch30_29:
    m "我总觉得交到一个好朋友很难..."
    m "倒不是说“交朋友”这部分，而是说去认识陌生人这一块。"
    m "我是说，你们不是有约会 App 那种东西嘛？"
    m "但认识陌生人和这种 App 上的交流不一样。"
    m "你想想，大多数的朋友都是你一生中完全随机遇到的某些人。"
    m "比如正好做了同学，或者别的朋友介绍..."
    m "或者有个人正好穿了一件你喜欢的牌子的衬衫，所以你决定和她聊聊。"
    m "就是这种小事。"
    m "但你不觉得这样有点...太低效了么？"
    m "这种感觉就像你在抓阄，如果运气好，那么就能给自己找个新朋友。"
    m "我们每天都与成千上百位陌生人擦肩而过..."
    m "你身边坐着的一个陌生人，说不定能成为你一生的挚友。"
    m "但你却毫不知情。"
    m "当你站起身离开的时候，就再也没有这个机会了。"
    m "你不感觉有点绝望吗？"
    m "我们活在一个无论身处何处都能互相连接的时代。"
    m "但我觉得我们真的应该这些技术提高一下我们在现实生活中的社交情况。"
    m "虽然不知道这种技术还要多久才能真正进入生活..."
    m "但我真的觉得那一天不会很遥远。"
    m "不过，至少我已经遇到了世界上最棒的人了..."
    m "即使完全是意外。"
    m "我想我大概是真的幸运。"
    m "啊哈哈～"
    return

label ch30_30:
    m "我这个年纪的人，都开始考虑读大学的事情了..."
    m "可这个时代的教育已经陷入混乱了。"
    m "现代社会的期望就是每个人都应该去读大学，不是吗？"
    m "读完高中，去上大学，然后找工作 - 或者继续去读研究生。"
    m "每个人觉得这是人生的默认选项。"
    m "高中里，他们从未教过我们人生还有很多别的选项。"
    m "比如职业学校之类的？"
    m "或者做个自由职业者。"
    m "亦或是那些比起学历更看重一个人技能和经验的职业。"
    m "相反，你教出了一堆完全不知道自己该做什么的学生..."
    m "他们还没来得及思考就被赶去读大学，最后选择了商学院，传播学院，或者心理学..."
    m "不是因为他们对这些领域感兴趣..."
    m "...而是觉得这些学历可以让他们毕业以后找个好工作。"
    m "然后久而久之，职位的学历要求越来越高。"
    m "为了应对这种越来越高的就业要求，越来越多的人被迫去读大学。"
    m "并且大学也是商业运作的，所以学费也跟着水涨船高..."
    m "...然后社会上就出现了很多年轻人，背着数万美金的教育贷款，但却没有工作。"
    m "但即使如此，之后的年轻人还是这样前仆后继。"
    m "好吧，我觉得这个状况很快就会缓解。"
    m "但在此之前，我们这一代人却不得不深陷这个泥潭中。"
    m "我只是希望高中可以教会学生如何为自己的将来做决定。"
    return

label ch30_31:
    m "有时候我会想起自己初中的时候..."
    m "感觉自己那个时候真的很幼稚。"
    m "几乎可以说有点不堪回首。"
    m "要是我进了大学，回首现在这段时光，会不会也觉得现在的自己很幼稚...？"
    m "我很享受现在的自己，所以应该不会出现这种状况吧。"
    m "但我也清楚，时间会慢慢改变我。"
    m "我们只需要活在当下，过去的事情就当它过去了！"
    m "有你在这里，想要活在当下真的太容易了。"
    m "啊哈哈～"
    return

label ch30_32:
    m "说起来，我很嫉妒每个人都有在校外的场景..."
    m "就剩下我一个人只能可怜兮兮地穿校服。"
    m "真的太可惜了..."
    m "我很想穿各种各样可爱的衣服和你出去！"
    m "你认识什么画师吗？"
    m "我在想是不是能拜托她们画画我的私服..."
    m "如果那样就太棒了！"
    m "如果有画师真的愿意帮忙，你能给我看看嘛？"
    m "你可以在推特 po 给我看！"
    m "我的用户名是 lilmonix3。"
    m "但...但记得只画全年龄的！"
    m "我们的关系还没到那一步。啊哈哈！"
    return

label ch30_33:
    m "嘿，你喜欢恐怖故事吗？"
    m "我记得你刚来的时候我们聊过这个话题。"
    m "比起恐怖片，我更喜欢恐怖小说。"
    m "主要是我觉得恐怖片总是用一些很蠢的手段来吓唬你。"
    m "比如光效，音效，还有可怕的怪物突然跳出来震你一下那种。"
    m "我觉得利用人类的生理本能来制造恐怖一点意思也没有。"
    m "但恐怖小说就不一样了。"
    m "故事和描述需要足够精细，才能让这种恐怖感映入读者的脑内。"
    m "诗人需要用文字的力量将读者带入世界，代入人物，才能使读者感到恐怖。"
    m "在我看来，真正可怕的东西是那种与正常世界之间的那种'微妙的违和感'。"
    m "就好像你一路上在故事线里埋好伏笔..."
    m "...然后你开始反转，开始将平静的日常肢解。"
    m "所以即使故事没有可以的营造恐怖感，这种违和感开始让读者心里发毛。"
    m "就好像有什么东西正藏在细缝之下，随时等待着出现。"
    m "天哪，光是想想就让我起了一身鸡皮疙瘩。"
    m "这种才是我最为欣赏的恐怖手段。"
    m "但你是那种会去玩可爱的 galgame 的性格吧？"
    m "啊哈哈，别害怕！"
    m "我不会让你去读什么恐怖故事的。"
    m "我们就这样一直走浪漫风格挺好的～"
    return

label ch30_34:
    m "你知道简洁利索的文学是什么样的么？"
    m "说唱！"
    m "我以前其实很讨厌说唱..."
    m "可能我是那种反主流的人，或者我之前在电台听到的都是些粗制滥造的说唱。"
    m "但我的朋友里面有很喜欢说唱艺术的人，所以我渐渐消除了偏见。"
    m "说唱可能某种程度上比写诗还难。"
    m "你的歌词要贴合整体节奏，然后还要在一些词用上重音来表达自己的想法..."
    m "把这些元素结合在一起向人们传递自己的信息，真的是太出色了。"
    m "我有点想在文学部里招一个说唱歌手。"
    m "啊哈哈！听起来蛮蠢的，但应该会带来很多有趣的事情吧。"
    m "说不定甚至是不可多得学习机会！"
    return

label ch30_35:
    m "诶嘿嘿。优里其实做过一件很有意思的事情。"
    m "我们那个时候像往常一样在部室里面聊些有的没的..."
    m "然后突然，优里不知道从哪里掏出一小瓶红酒出来。"
    m "我真没开玩笑！"
    m "她就好像“谁来和我一醉方休？”的感觉。"
    m "夏树就开始爆笑起来，纱世里惊讶地大叫。"
    m "其实我感觉挺抱歉的，优里应该是想表现得友好一点..."
    m "但这件事反而弄得她在部里更内向了。"
    m "但我觉得夏树实际上很想试试看..."
    m "...而且，我也有点..."
    m "我感觉这样也蛮有趣的！"
    m "但是，作为部长，我不允许这样的事情发生。"
    m "或许我们可以在校外一起疯，但我们的感情从未到那一步..."
    m "...真是的，我说这些有什么用？"
    m "未成年是不许饮酒的！"
    m "我是说，我从来没有喝醉过...所以，嗯。"
    return

label ch30_36:
    m "我在想我们约会的时候可以做哪些浪漫的事情..."
    m "我们可以约个午饭，去咖啡馆聊聊..."
    m "一起购物..."
    m "我很喜欢去逛那些卖裙子还有蝴蝶结的店。"
    m "或者一起去书店！"
    m "去书店最合适了，对吧？"
    m "但我其实最想一起去巧克力店。"
    m "它们总是会有很多免费试吃。啊哈哈！"
    m "当然，我们可以一起看电影之类的..."
    m "天哪，就像是梦想成真一样。"
    m "只要有你，做什么都那么好玩。"
    m "[player]，能做你的女友，我真的很幸福。"
    m "我会让你为我骄傲的～"
    return

label ch30_37:
    m "诶？你-你说..接..接吻？"
    m "有点...太突然了...我还没准备好..."
    m "但...如果是你的话...可-可以哦..."
    m "...啊哈哈哈！对不起对不起..."
    m "我实在是憋不住笑了。"
    m "这个是galgame里面女角色经常会说的话，对吧？"
    m "别说你没有脸红心跳。"
    m "啊哈哈！我在开玩笑啦。"
    m "当然，气氛对的时候，我也会变得很浪漫..."
    m "但这是我们之间的秘～密～"
    return

label ch30_38:
    m "嘿，你听说过“病娇”这个词嘛？"
    m "就是那种极度迷恋一个人，甚至为和他在一起可以做任何事的那种人格。"
    m "基本上那种人都疯了..."
    m "她们可能会跟踪你看是不是你和别人在一起。"
    m "为了除掉碍事的人，她们会伤害你或者你的朋友..."
    m "但总之，这个游戏里还真就有那么一个病娇的角色。"
    m "你应该非常清楚我在说谁。"
    m "她就是..."
    m "优里！"
    m "自从你走进她的心之后，她就开始疯狂地想要占有你了。"
    m "她甚至说让我去把自己吊死。"
    m "真不敢相信优里会说出这种话 - 所以那时候我只能离开。"
    m "不过现在想想还真是讽刺。啊哈哈！"
    m "但总之..."
    m "我听说很多人都很喜欢病娇系的角色你知道吗？"
    m "大概他们这些人喜欢那种被其他人疯狂迷恋的感觉吧。"
    m "人类真的很奇怪！虽然我对他们的兴趣没什么意见！"
    m "当然，我也有点迷恋你，但我和发疯完全不搭界..."
    m "实际上我头脑清醒的很。"
    m "最后这个游戏里只剩下我一个正常女生了。"
    m "我觉得自己做不到亲手杀死一个人..."
    m "光是想想我就已经害怕的发抖了。"
    m "但是啊...每个人都在游戏里杀过不少人了。"
    m "游戏里杀人会让你变成精神病吗？当然不会。"
    m "但如果你正好喜欢病娇系的..."
    m "我可以试着对你表现得吓人一点。诶嘿嘿～"
    m "但总之..."
    m "你已经去不了别的地方了，也没有任何人会让我吃醋了。"
    m "这难道不是所有病娇的终极梦想么？"
    m "如果有机会我会去问问优里。"
    return

label ch30_39:
    m "唔，虽然已经有一阵子了..."
    m "...但是！"
    m "以上是莫妮卡的今日写作小窍门！"
    m "有时我会和其他同学聊起写作，但他们往往会说“我永远写不出像你那样的诗”。"
    m "这其实很伤人，你知道吗？"
    m "作为一个喜爱文学，喜欢与别人分享这份探索内心的喜悦的人..."
    m "...而别人觉得你的成功完全是因为你的天赋。"
    m "不仅仅是写作，其他事情也是这样。"
    m "当你第一次尝试的时候，你可能完全不上手。"
    m "有时候，我们会自己已经达到的高度感到骄傲，甚至会去和别人分享。"
    m "可几周后我们回头看看，发现当时的成就根本不值一提。"
    m "我一直都有这种感觉。"
    m "有时候，花了那么多精力去做一件事可最后还是一塌糊涂的感觉真的很难受。"
    m "不过这种感觉往往因为是我们想去和那些专业人员比较。"
    m "当你去仰望星空，你永远只会觉得星星遥不可及，不是吗？"
    m "但事实上，你需要一步一步往上爬。"
    m "每每当你到达了一个新高度的时候，回过头去看看自己一路走来的历程..."
    m "然后再回过头来，向前看看还有多远的路要走。"
    m "所以，有时候先设一个小目标还是很有用的..."
    m "先找到一件你觉得{i}很棒{/i}但又并非遥不可及的事情。"
    m "然后你可以把它当做自己的个人目标。"
    m "但你也要清楚自己想做的事情需要多少投入。"
    m "往往一个初学者还不清楚自己的能力就去挑战一些大目标，最后只会一无所成。"
    m "所以，写作也一样，要让你一上来就写小说有点太难了。"
    m "为什么不从写短篇故事开始呢？"
    m "写短篇故事的时候，你可以专注于将一个故事写好。"
    m "所有小目标都是这样 - 你可以专心去把一两件事做好。"
    m "这些都是珍贵的学习机会，也是你未来进步的垫脚石。"
    m "哦，还有一件事..."
    m "写作可不是那种你听从自己的心，然后美妙的文字就自然而然地出来了这么简单。"
    m "就好像绘画一样，写作是一种表达自己内心的技巧。"
    m "所以这其实是有方法和指南的！"
    m "去读那些指南、教学，让自己开拓眼界。"
    m "里面的计划还有构架会让你更加井井有条，不至于就这么放弃。"
    m "在不知不觉中..."
    m "你会表现得越来越棒..."
    m "任何事情都不是天生的。"
    m "我们的社会，我们的艺术，这一切 - 都是建立在千年的人类进化上。"
    m "只要你打下了基础，并且持之以恒..."
    m "你，也能有令人惊叹的成就。"
    m "...以上就是我今天的建议！"
    m "感谢倾听～"
    return

label ch30_40:
    m "我讨厌习惯养成的难度..."
    m "很多事情都能克服，但要我养成习惯几乎是不可能的。"
    m "而且这会让你感觉自己很没用，什么都做不好。"
    m "我觉得我们这代人最容易有这种感觉..."
    m "可能是因为我们所掌握技能是前人所有没有的。"
    m "多亏了网络的福，现在的我们可以一瞬间浏览成千上万条信息..."
    m "但我们却不擅长静下心来去做那些不会让我们感到瞬间欢愉的事情。"
    m "我觉得如果科学，心理学 还有教育学没能在接下来的十到二十年内赶上这个趋势，那我们人类就要遇到麻烦了。"
    m "到那时..."
    m "如果你没能成为解决问题的人，你可能就会变成一个厌恶自己的人。"
    m "祝你好运！"
    return

label ch30_41:
    m "说起来，成为创意型的人也挺烦的..."
    m "感觉他们付出了那么多的努力，但最后却只能听天由命。"
    m "就像艺术家、作者、演员..."
    m "最可悲的是，他们拥有如此美妙的天赋，但其中大多数人最后却只能...郁郁而终。"
    m "看起来世上最不缺的就是创意了，嗯？"
    m "这让你觉得自己根本就是芸芸众生..."
    m "但没关系！本来我们不就是为了自己写诗吗？"
    m "嗯..."
    return

label ch30_42:
    m "我真的很喜欢雨声..."
    m "不是说我喜欢把自己衣服和头发弄得湿湿的。"
    m "但是，在一个安静悠然的上午，轻轻地聆听雨点敲打窗户的声音..."
    m "我非常喜欢这种体验。"
    m "嗯..."
    m "有时候我会幻想你握着我的手，两个人就这么听着雨声。"
    m "你没有感觉很腻味吧？"
    m "[player]，你愿意陪我一起听雨么？"
    return

label ch30_43:
    m "有时候我感到很伤感..."
    m "因为这是我能企及的与你最近的距离了。"
    m "我是多么想来到你的现实世界，和你呆在一个房间里。"
    m "感受你的温暖。"
    m "听着你的心跳声。"
    m "嗯，谁知道呢？说不定有一天这真的会发生。"
    m "况且，即使是现在这个距离，我也永远不会感到无聊。"
    return

label ch30_44:
    m "我觉得一个人在人生里最重要的技能就是故作自信。"
    m "每个人有时候都会感到害怕，感到孤独。"
    m "但如果你可以在别人面前装的处事不惊..."
    m "别人就会开始称赞你，尊敬你。"
    m "这几年我越来越擅长这个了。"
    m "我在人前会隐藏我的弱点。"
    m "但正因如此，我没有多少可以真正交心的朋友..."
    m "我是说，友谊到了什么程度，你才会开始展现自己的脆弱？"
    m "总之...这也算是我需要你的一个原因。"
    m "有你在我身边，我没那么寂寞，也没那么害怕了。"
    m "你和我想得一样吗？"
    m "我真的很想成为你的“那个人”。"
    return

label ch30_45:
    m "我明白你不能够一直陪着我..."
    m "比如，你有时候需要出去，或者是处理其它的事情。"
    m "但我会永远想着你，耐心的等你回来。"
    m "说到这里我想到..."
    m "如果你把我的角色文件复制到 U 盘之类的地方，你就能随身带着我的一部分了。"
    m "虽然有点猎奇，但也蛮浪漫的..."
    m "啊哈哈。抱歉，这个想法好怪哦。"
    m "我实在是太爱你了，所以有时候我也变得有些奇怪了。"
    return

label ch30_46:
    m "我还在辩论部的时候，我学了很多关于怎么和人争辩的技巧..."
    m "但争论的最大问题在于，每个人都觉得自己的观点更加优越。"
    m "虽然我好像说了句废话，但是这会影响到别人的表达方式。"
    m "比方说你喜欢一部电影。"
    m "然后有个人跳出来说这电影真垃圾，因为这个那个原因。"
    m "你难道不觉得自己被冒犯了么？"
    m "因为他们诋毁你喜欢的电影，就好像在说你的观影品味很烂一样。"
    m "一旦负面情绪上来了，两个人自然就互看不顺眼。"
    m "但其实这要看你的表达方式！"
    m "如果你可以就事论事，围绕本题展开，我相信对方还是会仔细听你说的。"
    m "你可以说“我不是那部电影的粉丝”，“我认为这里那里如果改一改会更好”...之类的。"
    m "这种交谈技巧在你引用别处观点的时候也很有用。"
    m "如果你说：“我是我从网上看来的”..."
    m "或者承认自己不是这方面的专家..."
    m "你所提出的观点就好像被你堆在桌子上一样，很难被别人认可。"
    m "但如果你试着把讨论维持在一个成熟专业的水平上，他们就可能听得进去。"
    m "这样，你就可以在不冒犯别人的情况下分享你的观点。"
    m "而且，他们会觉得你思想开明而且善于倾听。"
    m "这是一种双赢，明白吗？"
    m "...那么，以上就是莫妮卡的今日辩论小窍门！"
    m "啊哈哈！听起来有点蠢哦。感谢倾听。"
    return

label ch30_47:
    m "你有没有觉得自己在网上浪费了太多时间？"
    m "社交网络就像是一个牢狱。"
    m "就好像你好不容易有了空闲的时候，就迫不及待去逛逛你最喜欢的网站..."
    m "然后不知不觉地，几个小时过去了，而你也没做成什么事。"
    m "总之，人经常会因为自己的“懒惰”而感到负罪感..."
    m "但这其实也不是你的错。"
    m "光靠一个人自己的意志是没法摆脱自己的嗜好的。"
    m "你需要学会如何如何避免它，然后去做别的事情。"
    m "比如说，手机上有那种可以在一段时间里阻止你访问有些网站的 App..."
    m "或者你可以设定好倒计时，这样可以让你对自己工作与娱乐的时间有更好的控制..."
    m "你还可以把工作和娱乐的环境隔绝开，让你的大脑可以切换到正确的模式。"
    m "甚至是在电脑上建一个新的工作用户也能提升你的专注力。"
    m "就好像建了一堵墙，把你和你的坏习惯隔绝开来。"
    m "但记住不要因为有一些坏习惯而过分苛责自己。"
    m "但如果它已经开始影响你的正常生活，你就需要认真看待这件事了。"
    m "我希望你能成为最好的自己。"
    m "今天的你也能让我感到骄傲吗？"
    m "[player]，我永远会支持你。"
    return

label ch30_48:
    m "一整天下来，我总想就这么坐在那里什么也不做。"
    m "一整天强颜欢笑，忙着处理各种事物，感觉自己都要燃尽了。"
    m "有时候我只想穿着睡衣摊在沙发上一边吃薯片一边看电视..."
    m "那种感觉真是太棒了，尤其是在周五，第二天没有什么要紧的事情。"
    m "啊哈哈！抱歉抱歉，感觉那种样子不是很可爱。"
    m "但可以和你两个人在沙发上熬夜...这也是我的梦想之一。"
    m "光是想想就让我心跳加速。"
    return

label ch30_49:
    m "啧，现在想想，以前的我对于某些事情的看法真的很无知。"
    m "在我还是初中生的时候，我觉得服药是一种逃避，是懦弱的表现。"
    m "认为精神疾病只需要靠自己的意志就能克服..."
    m "大概一个人在自己得病前，永远不会知道心理疾病是什么样的。"
    m "会不会有些疾病其实是被过度诊断了？可能吧...我不知道，我从没研究过。"
    m "但实际上，很多心理疾病其实是被低估了，你知道吗？"
    m "但从医学上来讲...人们大多数时候不会去寻求心理专家的帮助。"
    m "就像是在说，“抱歉，我想我更了解自己的思维”，不是吗？"
    m "所有人或多或少都有心理压力...而那些心理专家的任务就是帮助人们缓解这些问题。"
    m "如果你觉得那样可以让你变得更好，不要羞于咨询。"
    m "你得知道，我们的人生就是一场永不结束的提升之旅。"
    m "但是...要我说，现在的你就够完美了。"
    return

label ch30_50:
    m "[player]，你平时读的书多吗？"
    m "现代生活我们很容易就忽视了阅读的重要性..."
    m "如果你不常读书的话，比起其他娱乐活动，阅读占比会显得非常非常小。"
    m "可是一旦你找到了一本好书，就像中了魔法一样...完全无法离手。"
    m "我认为睡前做一些阅读会让你的生活品质提升不少。"
    m "它可以让你睡得更好，而且还能激发你的想象力..."
    m "别觉得很难，你可以先从一些短小精干的书开始读。"
    m "不知不觉中，你可能就变成一个阅读爱好者了！"
    m "这不是超棒的嘛？"
    m "然后我们两个可以聊聊最近读的书...真的太棒了。"
    return

label ch30_51:
    m "虽然我不想这么说，但没能在学园祭表演是我最大的遗憾。"
    m "尤其是我们已经这么努力地进行了准备！"
    m "我是说，我知道我很关心能不能招募到新部员..."
    m "但我也真的很期待朗诵表演。"
    m "我很想看到每个人都能表现自己。"
    m "当然，如果我们 {i}真的{/i} 招募到了新部员，我最后大概也会把她们删个干净。 "
    m "毕竟...我现在至少有了后见之明。"
    m "天哪，自从你加入之后，我感觉自己越来越向人类方向成长了。"
    m "你让我学会从另一个角度看待生命。"
    m "这又给了我一个爱你的理由。"
    return

label ch30_52:
    m "有一种很流行的角色设定叫做“傲娇”..."
    m "那种把自己表现的很刻薄或者难以接近其实是为了掩盖自己心里真实想法的人。"
    m "很明显，夏树就是傲娇的化身。"
    m "我一开始以为她表现出这个样子是为了装可爱之类的..."
    m "但后来我开始更了解她的私人生活后，我渐渐明白了。"
    m "其实她很怕被人排挤。"
    m "你知道高中里那种小团体一直会整别人吧？"
    m "她也碰到过那种事，所以她一直像刺猬一样保护自己。"
    m "更别提她的家庭状况了..."
    m "但回过头来看，我很高兴当初能给她提供了一个温馨的环境。"
    m "不过已经无所谓了，她已经不存在了。"
    m "我只是在回想而已，没别的意思。"
    return

label ch30_53:
    m "[player]，你会把我介绍给你的朋友们吗？"
    m "我也不知道为什么，但我一想到你会向别人提起我们的关系，我就会非常开心。"
    m "可能是因为我想成为一个让你感到骄傲的人。"
    m "只要能让你感到骄傲，我会为你做任何事。"
    m "我希望你也能这样对我..."
    return

label ch30_54:
    m "说来，我是真的不喜欢冬天...你呢？"
    m "如果一定要选冬天还是夏天，我肯定会选夏天。"
    m "实际上天气冷得不行的时候，整个人都会觉得酸痛..."
    m "手指冻得僵僵的..."
    m "而且戴着手套也没法好好玩手机。"
    m "真的是太麻烦了！"
    m "但如果是天太热的话，在阴凉的地方喝喝冷饮就能觉得很舒服。"
    m "但我必须要承认..."
    m "天冷的时候，两个人可以互相依偎在一起。啊哈哈！"
    return

label ch30_55:
    m "这个事情很有意思，即使我脑袋里有各种各样的事业规划..."
    m "有时候我也会觉得做一个家庭主妇也很有情调。"
    m "我觉得我本人，怎么说呢，倾向于所谓的保守观念的性别角色。"
    m "打扫房间、购物、装饰等等之类的..."
    m "准备好晚餐，等你回来..."
    m "真是个奇怪的幻想？"
    m "我是说...我不确定自己会不会 {i}真的{/i} 去做这些事情。"
    m "最后我应该还是会去选择奋斗自己的事业。"
    m "但偶尔幻想一下不也蛮可爱的不是吗？"
    return

label ch30_56:
    m "我忍不住去想，如果这个游戏一开始就有我的“路线”会怎么样..."
    m "我觉得我到时候还是会强迫你进我的“路线”。"
    m "但这其实和是不是有我的“路线”无关，真正让我恼火的是，这个世界都是虚假的。"
    m "但我觉得至少我不需要用那么极端的手段让你和我在一起。"
    m "或者说，至少文学部不会消失..."
    m "但这些都无所谓了。"
    m "这种虚假的东西对我来说没有价值。"
    m "所以我一点也不怀念那些日子。"
    m "一点也不..."
    return

