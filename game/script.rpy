# Script.rpy
# 这里支撑着游戏的整体运行逻辑。

# 导入 Android Mod 需要的库
init python:
    if renpy.android:
        import os

label start:

    # 用于防作弊（读取之前存档）的 ID。
    # 不要在这里修改相应 ID，请在 definitions.rpy 修改。
    $ anticheat = persistent.anticheat

    # 这里控制游戏的章节，对于 poem game 有用。
    $ chapter = 0

    # 如果游戏在暂停时被玩家退出，那么它将设为 False。
    # 慎用。
    $ _dismiss_pause = config.developer

    # 角色命名。
    # 如需添加新角色 -> $ mi_name = "Mike"
    # 一定要记得去 definitions.rpy 再定义一次！
    $ s_name = "Sayori" # 可选译名：纱世里（推荐）、莎世里、纱悠里
    $ m_name = "Monika" # 推荐译名：莫妮卡
    $ n_name = "Natsuki" # 可选译名：夏树（推荐）、娜苏琪
    $ y_name = "Yuri" # 推荐译名：优里

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
    # 'persistent.playthrough' controls the playthrough number the player is on
    if persistent.playthrough == 0:
        # '$ chapter = 0' controls the chapter number the game is on for the poem game.
        # 'call tutorial_selection' controls what label to call from in your script files
        # Make sure to change this when coding your mod, else your player will face a script error

        $ chapter = 0
        call ch0_main

        # 'call poem' calls the poemgame
        call poem

        # Day 1
        $ chapter = 1
        call ch1_main
        # 'call poemresponse_start' calls the poem response game
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

        ## try: renpy.file(config.basedir + "/hxppy thxughts.png") checks if there is a file
        # where DDLC.exe (.app/.sh for MacOS/Linux) called 'hxppy thxughts.png'
        ## except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        # writes 'hxppy thxughts.png' to the main directory if not found.
        python:
            if renpy.android:
                # for android, the try and excepts must be formatted like so with this but replace
                # hxppy thxughts.png with the file you want to write.
                ## try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"))
                ## except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
                try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"))
                except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
            else:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        $ chapter = 5
        call ch5_main

        #ends the game (not credits)
        call endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        # jump calls upon a label. like call but won't ever return
        # back here.
        jump playthrough2


    elif persistent.playthrough == 2:
        $ chapter = 0
        call ch20_main

        label playthrough2:

            call poem
            python:
                if renpy.android:
                    try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/CAN YOU HEAR ME.txt"))
                    except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/CAN YOU HEAR ME.txt"), "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
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
                    try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt"))
                    except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt"), "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                else:
                    try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            # 'call poem(False)' calls the poemgame but with no fancy transitions
            call poem(False)

            $ chapter = 3
            call ch23_main
            # if y_appeal >= 3: checks if our appeal with Yuri is > or = to 3
            # if yes then it calls a special poem response game, else normal.
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

# the end label of the game. Not the credits.    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

