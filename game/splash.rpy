## Splash.rpy - 启动屏幕

# 检测 DDLC RPA 文件是否补全
## 提示：若需要构建 Android Mod 包，
## 请依旧保留 RPA 文件，同时将相应 RPA 文件解包。
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                renpy.error("未在 /game 文件夹内找到 DDLC 资源，请先补全资源。")

# 启动屏幕显示的信息文本
init python:
    menu_trans_time = 1
    # 默认的启动屏幕信息，所有玩家都可以看到。
    splash_message_default = "这是非官方的饭制 Mod，与 Team Salvato 无关。"
    # 一些可供随机选择的额外信息
    splash_messages = [
        "请多多支持 Dan 鸽www",
        "Monika 在盯着你的粪代码。（笑）",
        "Monika 保佑你，开发 Mod 不遇一个 expection！"
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

# 主界面图片
image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# 阴间菜单（Ghost Menu）相关图片
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Sayori Image After Game 1st Restart
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

# Main Menu Effects

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

# Team Salvato Splash Screen

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# 特殊的 Mod 文字提示。

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# 检查缺失的角色文件。
init python:
    if not persistent.do_not_delete:
        import os
        if renpy.android: # 检查平台是否为 Android。
            try:
                # 补回缺失角色文件，目录为 Android/data/[您的Mod包名]/characters
                if not os.access(os.environ['ANDROID_PUBLIC'] + "/characters/", os.F_OK):
                    os.mkdir(os.environ['ANDROID_PUBLIC'] + "/characters")
                if persistent.playthrough <= 2:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/monika.chr")
                    except: open(os.environ['ANDROID_PUBLIC'] +  "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
                if persistent.playthrough <= 1 or persistent.playthrough == 4:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/natsuki.chr")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/yuri.chr")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
                if persistent.playthrough == 0 or persistent.playthrough == 4:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/sayori.chr")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
            except:
                pass
        else:
            try:
                if not os.access(config.basedir + "/characters/", os.F_OK):
                    os.mkdir(config.basedir + "/characters")
                if persistent.playthrough <= 2:
                    try: renpy.file("../characters/monika.chr")
                    except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
                if persistent.playthrough <= 1 or persistent.playthrough == 4:
                    try: renpy.file("../characters/natsuki.chr")
                    except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                    try: renpy.file("../characters/yuri.chr")
                    except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
                if persistent.playthrough == 0 or persistent.playthrough == 4:
                    try: renpy.file("../characters/sayori.chr")
                    except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
            except:
                pass

# 启动警告背景图片。
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

# 启动警告 / 声明

label splashscreen:
    # 在 Windows 系统中自动获取电脑用户名及进程列表。
    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass

    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black
        "你似乎删除了 firstrun 文件，或者我们发现还有旧版本 / 先前的存档。"
        menu:
            "是否删除存档并重置游戏？该操作不可撤销。"
            "是的，删除存档":
                "正在删除存档...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "不，继续游戏":
                $ restore_relevant_characters()

    # 兼容性警告功能，详见 lockdown_check.rpy。
    ## 请 不 要 修 改 这 几 行 。
    default persistent.lockdown_warning = False

    if not persistent.lockdown_warning:
        if os.path.exists(config.gamedir + "/lockdown_check.rpy"):
            call lockdown_check
        else:
            $ persistent.lockdown_warning = True

    # 设定 first run 默认值为 False 以展示游戏内容警告
    default persistent.first_run = False

    # 游戏内容警告

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        # 您可以随意更改以下内容，但请您 务 必 注 明 本 Mod 与 Team Salvato 无关，
        # 且包含剧透，必须在通关原作后游玩，同时保留原作下载链接。
        "[config.name] 是 Doki Doki Literature Club 的粉丝 Mod，与 Team Salvato 无关。"
        "本 Mod 理应在通关原游戏后再进行游玩，因此本 Mod 包含剧透。"
        "要游玩本 Mod，需要原版 Doki Doki Literature Club 的文件。您可以在 {a=https://ddlc.moe}DDLC.moe{/a} 或者 Steam 免费获取。"
        menu:
            "如果继续游玩 [config.name] 将视为你已经通关原游戏，并接受任何剧透内容。"
            "我同意。":
                pass
            "我不同意，退出。":
                $ renpy.quit()
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white

        $ persistent.first_run = True

    ## 控制 Sayori XX 彩蛋。
    ## 为避免 Mod 社死，保证心理安全，默认注释该段。
    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: renpy.file("../characters/sayori.chr")
    #         except: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: renpy.file("../characters/monika.chr")
    #             except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: renpy.file("../characters/natsuki.chr")
    #             except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: renpy.file("../characters/yuri.chr")
    #             except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: renpy.file("../characters/sayori.chr")
    #             except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())


    # 首次启动游戏时获取特殊诗序号。
    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')

    # Controls auto-load of certain scripts
    if persistent.autoload:
        jump autoload

    # Team Salvato/Splash Message

    $ config.allow_skipping = False

    ## ghost menu（阴间版菜单）随机展示，仅在二周目生效，默认概率 1/64，可以自己修改。
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    ## 为避免 Mod 社死，保证心理安全，默认注释该段。
    ## Sayori 提前 XX 彩蛋
    # if s_kill_early:
    #     show black
    #     play music "bgm/s_kill_early.ogg"
    #     $ pause(1.0)
    #     show end with dissolve_cg
    #     $ pause(3.0)
    #     scene white
    #     show expression "images/cg/s_kill_early.png":
    #         yalign -0.05
    #         xalign 0.25
    #         dizzy(1.0, 4.0, subpixel=False)
    #     show white as w2:
    #         choice:
    #             ease 0.25 alpha 0.1
    #         choice:
    #             ease 0.25 alpha 0.125
    #         choice:
    #             ease 0.25 alpha 0.15
    #         choice:
    #             ease 0.25 alpha 0.175
    #         choice:
    #             ease 0.25 alpha 0.2
    #         choice:
    #             ease 0.25 alpha 0.225
    #         choice:
    #             ease 0.25 alpha 0.25
    #         choice:
    #             ease 0.25 alpha 0.275
    #         choice:
    #             ease 0.25 alpha 0.3
    #         pass
    #         choice:
    #             pass
    #         choice:
    #             0.25
    #         choice:
    #             0.5
    #         choice:
    #             0.75
    #         repeat
    #     show noise:
    #         alpha 0.1
    #     with Dissolve(1.0)
    #     show expression Text("现在，大家都高兴了。", style="sayori_text"):
    #         xalign 0.8
    #         yalign 0.5
    #         alpha 0.0
    #         600
    #         linear 60 alpha 0.5
    #     pause
    #     $ renpy.quit()

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

# 警告屏幕
label warningscreen:
    hide intro
    show warning
    pause 3.0

## 如果 monika.chr 被删除并进入游戏，将触发此特殊剧情，并删除所有角色。
## from original_scripts_tl/script-ch0.rpy
## 为避免 Mod 社死，保证心理安全，默认注释该段。

# label ch0_kill:
#     $ s_name = "Sayori"
#     show sayori 1b zorder 2 at t11
#     s "..."
#     s "..."
#     s "什...什么......"
#     s 1g "..."
#     s "这..."
#     s "这是哪里......?"
#     s "哦......"
#     s 1u "不......"
#     s "不可能。"
#     s "绝对不可能。"
#     s 4w "这又是哪跟哪？"
#     s "我又是谁？"
#     s "停下来！"
#     s "快点停下来！！！"

#     $ delete_character("sayori")
#     $ delete_character("natsuki")
#     $ delete_character("yuri")
#     $ delete_character("monika")
#     $ renpy.quit()
#     return

# 反作弊功能，核对目前游戏进度与存档的反作弊 ID 是否一致
label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat: # 不一致则显示彩蛋并重启游戏
        stop music
        scene black
        "存档加载失败。"
        "您是不是想作弊呢？"
        show monika 1a at t11 zorder 1
        if persistent.playername == "":
            m "您真可笑。"
        else:
            m "[persistent.playername]，您真可笑。"

        $ renpy.utter_restart()
    return

# 自动读档。
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

        try: renpy.pop_call()
        except: pass
    jump expression persistent.autoload

# 返回主菜单之前的事件。
label before_main_menu:
    return

# 退出游戏的事件。
label quit:
    if persistent.ghost_menu: # Ghost Menu 的短暂恐吓，可以自行修改
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
