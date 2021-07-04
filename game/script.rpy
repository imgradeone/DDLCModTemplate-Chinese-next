# Script.rpy
# 这里支撑着游戏的整体运行逻辑。

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

    # Start of the script
    call ch1_start

    return

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

