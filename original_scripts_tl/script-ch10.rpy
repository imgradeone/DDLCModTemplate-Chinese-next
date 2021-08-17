label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "我看见一个吵吵闹闹的女孩不断挥着手向我跑来，仿佛要把全世界的注意力都聚焦在她身上一样。"
    "她叫[s_name]，我的邻居，也是我儿时的玩伴。"
    "也许放到从前，我不一定和她交朋友，但和她在一起很久后就慢慢生出了友谊。"
    "我们以前经常这样一起上学，但上了高中以后她睡懒觉的频率就越来越高，我也就有点懒得等她了。"
    "但她这样狂追不舍，搞得我真心想一走了之。"
    "不过，我只好叹了口气，在路口等着，好让[s_name]赶上我。"

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat
    $ renpy.save_persistent()

    jump ch20_from_ch10

