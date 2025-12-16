# Options.rpy
## This template version is 2.4.9. When asked to provide the template version you are using,
## give them this version number. DO NOT REMOVE OR CHANGE THIS COMMENT.
   
## 目前中文 Mod 模板的版本为 2.0.0-beta3-fix，基于原版改良模板的 2.4.9 版本改造。
## 如果你需要向别人提及模板版本，建议把这两个都放上去。
## 不要修改、删除这段注释，包括上面的英文原版。

# 这里可以为你的 Mod 命名。
# 把 "DDLC 中文 Mod 模板" 改成你的 Mod 名字（比如 "我永远喜欢 Sayori"）
## 带有 _() 的字符串表示其可被翻译。
define config.name = "DDLC 中文 Mod 模板"

# 这里可以控制是否在游戏主菜单展示 Mod 名字及版本号。
# 一般情况下可以打开以与原游戏区分，但如果 Mod 名字太长，建议改为 False
define gui.show_name = True

# 这里可以输入版本号。如果你的 Mod 版本很多，那这时版本号会很有用。
# 如果你刚刚开始，那么建议把版本号设为 "1.0"
define config.version = "2.0.0-beta3-fix"

# 这里是在“关于”页显示的 Mod 介绍文字。
# 由于我们重新启用了关于界面，你可以在这里写点介绍。
define gui.about = _("""这里是写简介的地方。在 options.rpy 里写上你的 Mod 简介吧！""")

# 这是 Ren'Py SDK 会读取的构建名。
# 构建名只能使用 ASCII 字符，因此只能使用英文字母，不能有空格、数字、下划线。
# 例：Sayori Is The Best → SayoriIsTheBest
define build.name = "DDLCModTempCNNext"

# 控制设置菜单中的音量设置显示
# 音效，建议保留为 True
define config.has_sound = True

# 背景音乐，建议保留为 True
define config.has_music = True

# 语音，如果 Mod 有语音则为 True，否则为 False
define config.has_voice = False

# 这里控制主菜单的背景音乐。
# audio.t1 是 Doki Doki Literature Club 的主菜单音乐。
# 如果你想修改，那么把 "t1" 改成其他已定义的 BGM。
define config.main_menu_music = audio.t1

# 这是进入和退出游戏菜单时使用的转场。
# Dissolve(.2) 相当于转场特效。
# config.enter_transition 控制进入游戏菜单时使用的转场。
# config.exit_transition 控制退出游戏菜单 / 返回游戏时使用的转场。
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# 这是加载存档后显示的转场。
# 默认情况下为 None，你可以自定义转场，但如果不确定，请保留为 None。
define config.after_load_transition = None

# 这是在故事结束后显示的转场。
# Dissolve(.2) sets the transition effect you see.
define config.end_game_transition = Dissolve(.5)

# This controls the textbox that the characters use to speak.
# "auto" sets the textbox to hide during scenes and show when a character speaks
# "show" sets the textbox to show at all times
# "hide" only shows dialogue when a character speaks.
define config.window = "auto"

# This controls the transition effects of the textbox.
# Dissolve(.2) sets the transition effect you see.
# config.window_show_transition controls the effect when the textbox is shown.
# config.window_hide_transition controls the effect when the textbox is hidden.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# 这里可以控制 Mod 默认的文字展示速度。
# 默认值为 50，增加即为加速，减小即为减速。
# 若设置为 0，则为直接展示文字，无打字机过渡。
default preferences.text_cps = 50

# This controls the auto-forward speed
# 15 is DDLC's default speed.
# You can change it from 0-30
default preferences.afm_time = 15

# This controls the audio level of your mod.
# Increasing this will make the music louder while decreasing will make it quieter.
# SFX controls the sound effects volume.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# Mod 的存档位置。经测试，使用中文会导致异常。
# Change "DDLCModTempCNNext" to your mod's name
# Windows Directory for Saves: %AppData%/RenPy/
# macOS Directory for Saves: $HOME/Library/RenPy/ (Un-hide the Library Folder)
# Linux Directory for Saves $HOME/.renpy/
define config.save_directory = "DDLCModTempCNNext"

# This controls the window logo of your mod.
# By default this defaults to the DDLC Icon PNG.
define config.window_icon = "gui/window_icon.png"

# This controls whether your mod allows skipping dialogue.
define config.allow_skipping = True

# This controls whether your mod saves automatically.
define config.has_autosave = False

# This controls whether you mod saves when quitting the game.
define config.autosave_on_quit = False

# This controls the number of slots auto-saving can use
define config.autosave_slots = 0

# 控制各个 GUI 元素（屏幕、图像等）的图层。
# 最好不要动这一块。
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# 最好也不要动这一块。
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

## 构建配置 #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    # Code to Package your mod to a ZIP in Ren'Py
    build.package(build.directory_name + "Mod",'zip','mod',description="Ren'Py 6 DDLC Compliant Mod")
    build.package(build.directory_name + "Renpy7Mod",'zip','windows mac linux renpy mod',description="Ren'Py 7 DDLC Compliant Mod")

    build.archive("scripts", 'mod all')
    build.archive("mod_assets", 'mod all')

    ## 不要动这里。
    ## 这里可以让 Ren'Py 添加 Linux / macOS 的执行文件。
    try:
        build.renpy_patterns.remove((u'renpy.py', [u'all']))
    except:
        pass
    build.classify_renpy("renpy.py", "renpy all")

    build.early_base_patterns.remove(('*.sh', None))
    build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
    build.classify("*.sh", None)
    
    #############################################################

    # To classify packages for both pc and android, make sure to add all to it like so
    # Example: build.classify("game/**.pdf", "scripts all")
    
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/gui/**", "mod_assets all")
    build.classify("game/images/**", "mod_assets all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.txt", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all")
    build.classify("game/tl/**", "scripts all") ## Translation Folder
    build.classify("game/tutorial_route_answer/**", None)

    build.classify('**~', None)
    build.classify('**.zip', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.md', None)
    build.classify('help.html','mod all')
    build.classify('attributions.txt','mod all')

    # Set's help.html as documentation
    build.documentation('help.html')

    build.include_old_themes = False

    # # Advanced Addons
    # # This section is for advanced build classifications to your mod that
    # # can be added to your mod. Note DDLC runs as normal and doesn't require this.
    # # This is either for compatibility issues or added features.

    # # Doki Doki Mod Manager metadata file
    # build.classify('ddmm-mod.json','mod')
    # build.classify('ddmm-bg.png','mod')
