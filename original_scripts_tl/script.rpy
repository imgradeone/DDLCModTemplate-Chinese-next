# Script.rpy - 脚本文件
# 这里支撑着游戏的整体运行逻辑。

label start:

    # 用于防作弊（读取之前存档）的 ID。
    # 不要在这里修改相应 ID，请在 definitions.rpy 修改。
    $ anticheat = persistent.anticheat

    # 这里控制游戏的章节，对于 poem game 有用。
    $ chapter = 0

    # 控制是否允许玩家快速展示所有文字，默认基于开发者选项 
    # (located in definitions.rpy)
    $ _dismiss_pause = config.developer

    # 角色命名。
    # 如需添加新角色 -> $ mi_name = "Mike"
    # 一定要记得去 definitions.rpy 再定义一次角色！
    $ s_name = "???"
    $ m_name = "女孩 3"
    $ n_name = "女孩 2"
    $ y_name = "女孩 1"

    # 控制是否显示底部文字菜单和是否允许使用 Esc 显示菜单。
    $ quick_menu = True

    # 控制对话文字风格。
    # 对于“修改”类文本，请使用 'style.edited'，否则请保持 'style.normal'
    $ style.say_dialogue = style.normal

    # 控制 Sayori 此时是否 GG，但这个变量目前没什么用。
    $ in_sayori_kill = None
    
    # 控制是否允许玩家跳过 / 快进对话。
    $ allow_skipping = True
    $ config.allow_skipping = True

    # 脚本开始
    # 'persistent.playthrough' 控制玩家所在周目
    if persistent.playthrough == 0:
        # '$ chapter = 0' 这里控制游戏的章节，用于 poem game。
        # 'call ch0_main' 等都控制需要 call 的章节。
        # 请务必对这些内容进行修改，防止报错。

        $ chapter = 0
        call ch0_main

        call poem

        # Day 1
        $ chapter = 1
        call ch1_main
        # 'call poemresponse_start' 呼出特殊反应剧情
        call poemresponse_start
        call ch1_end

        call poem

        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end

        call poem

        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        $ chapter = 4
        call ch4_main

        ## try: renpy.file(config.basedir + "/hxppy thxughts.png") 检查 DDLC 启动文件所在目录下
        # 是否存在 'hxppy thxughts.png' 文件
        ## except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        # 如果不存在相应文件，则创建 'hxppy thxughts.png' 文件并写入内容
        python:
            if renpy.android:
                # 针对 Android 平台，请按照如下格式来创建文件。
                # （您可以将 'hxppy thxughts.png' 修改为你想要的其他文件。）
                ## try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
                ## except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
                except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
            else:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        $ chapter = 5
        call ch5_main

        # 显示 END 屏幕，结束游戏（但还没到 credits）
        call endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        # jump 一样呼出 label，但不会重新返回（return）至此。
        jump playthrough2


    elif persistent.playthrough == 2:
        $ chapter = 0
        call ch20_main

        label playthrough2:

            call poem
            python:
                if renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                else:
                    try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                    except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end

            call poem(False)
            python:
                if renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                else:
                    try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            # 'call poem(False)' 会呼出 poem game，但不含任何过渡转场。
            call poem(False)

            $ chapter = 3
            call ch23_main
            # if y_appeal >= 3: 检查优里好感度是否大于等于 3
            # 如果成功则进入特殊诗歌反应，否则还是正常版反应
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start
            # this is old Dan leftover code when DDLC was a demo.
            # if you wanted to you can re-use it as a demo showcase of your own mod.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main
        jump credits

# 游戏的 END 标志。（不是 Credits）
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
