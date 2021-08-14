# pronoun_example.rpy

# This file serves as a example to the pronoun feature.
# Use this as a example on how to use the pronoun feature.

label pronoun_example:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    $ renpy.jump('pronoun_menu')

label pronoun_menu:
    menu:
        "您的人称为？"
        "他":
            $ he = "he"
            $ him = "him"
            $ are = "is"
            $ hes = "he's"
            $ he_chs = "他"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()

            "已设定人称为“他”。"
            $ renpy.jump('pronoun_menu')
        "她":
            $ he = "she"
            $ him = "her"
            $ are = "is"
            $ hes = "she's"
            $ he_chs = "她"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()
            python:
                finishPronouns()

            "已设定人称为“她”。"
            $ renpy.jump('pronoun_menu')
        "他们":
            $ he = "they"
            $ him = "them"
            $ are = "are"
            $ hes = "they're"
            $ he_chs = "他们"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()
            python:
                finishPronouns()

            "已设定人称为“他们”。"
            $ renpy.jump('pronoun_menu')
        "目前的人称":
            if not he:
                "You have yet set a pronoun."
            else:
                "Your current pronoun is [heC]/[himC]."
            $ renpy.jump('pronoun_menu')
        "Play a sample.":
            if not he:
                "You have yet set a pronoun. Set one up before proceeding."
                $ renpy.jump('pronoun_menu')
            mc "My pronouns are [he]/[him]."
            m "[hesC] here to learn about how dense [he] really [are]."
            s "Don't say mean things to [him]!"
            n "I don't like the looks of [him]."
            y "[areC[0]]-[areC] [he] going to be okay?"
            $ renpy.jump('pronoun_menu')
        "清除人称":
            $ he = ""
            $ him = ""
            $ are = ""
            $ hes = ""
            python:
                finishPronouns()

            "已清除人称。"
            $ renpy.jump('pronoun_menu')
        "退出":
            return
    return