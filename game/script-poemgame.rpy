#Commented to absurdity, blame Terra.
#
#Worth noting how the game gets here in the first place:
    #This script is called via "call poem" in script.rpy.
    #All of the Act 1 instances are done simply with "call poem".
    #Some of the Act 2 instances are done with "call poem (False)"
        #This is how we get the abrupt cut-in to the mini-game in Act 2.
#Images are defined after the main poem game loop.

init python: #This whole block runs when DDLC is started (as opposed to when the poem minigame is called)
    import random

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch

    # Static variables for characters' poem appeal: Dislike, Neutral, Like
    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45

    # Building the word list
    full_wordlist = []
    with renpy.file("poemwords.txt") as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()
            
            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    full_wordlist_chs = [
    PoemWord("happiness 幸福",3,2,1),
    PoemWord("sadness 难过",3,2,1),
    PoemWord("death 死",3,1,2),
    PoemWord("tragedy 悲剧",3,1,2),
    PoemWord("alone 孤独",3,1,2),
    PoemWord("love 爱",3,2,1),
    PoemWord("adventure 冒险",3,2,1),
    PoemWord("sweet 甜蜜",3,2,1),
    PoemWord("excitement 激情",3,2,1),
    PoemWord("fireworks 焰火",3,2,1),
    PoemWord("romance 浪漫",3,2,1),
    PoemWord("tears 眼泪",3,1,2),
    PoemWord("depression 抑郁",3,1,2),
    PoemWord("heart 心脏",3,2,1),
    PoemWord("marriage 婚姻",3,2,1),
    PoemWord("passion 热情",3,2,1),
    PoemWord("childhood 童年",3,2,1),
    PoemWord("fun 有趣",3,2,1),
    PoemWord("color 色彩",3,2,1),
    PoemWord("hope 希望",3,1,2),
    PoemWord("friends 朋友",3,2,1),
    PoemWord("family 家庭",3,2,1),
    PoemWord("party 派对",3,2,1),
    PoemWord("vacation 假期",3,2,1),
    PoemWord("lazy 懒",3,2,1),
    PoemWord("daydream 白日梦",3,1,2),
    PoemWord("pain 痛",3,1,2),
    PoemWord("holiday 假日",3,2,1),
    PoemWord("bed 床",3,2,1),
    PoemWord("feather 羽毛",3,2,1),
    PoemWord("shame 羞愧",3,1,2),
    PoemWord("fear 恐惧",3,1,2),
    PoemWord("warm 温暖",3,2,1),
    PoemWord("flower 花",3,2,1),
    PoemWord("comfort 安慰",3,2,1),
    PoemWord("dance 舞蹈",3,2,1),
    PoemWord("sing 歌唱",3,2,1),
    PoemWord("cry 哭泣",3,1,2),
    PoemWord("laugh 欢笑",3,2,1),
    PoemWord("dark 黑暗",3,1,2),
    PoemWord("sunny 晴朗",3,2,1),
    PoemWord("raincloud 乌云",3,2,1),
    PoemWord("calm 镇静",3,1,2),
    PoemWord("silly 愚蠢",3,2,1),
    PoemWord("flying 飞翔",3,2,1),
    PoemWord("wonderful 完美",3,2,1),
    PoemWord("unrequited 单恋",3,1,2),
    PoemWord("rose 玫瑰",3,1,2),
    PoemWord("together 一起",3,2,1),
    PoemWord("promise 承诺",3,2,1),
    PoemWord("charm 魅力",3,2,1),
    PoemWord("beauty 美丽",3,2,1),
    PoemWord("cheer 欢呼",3,2,1),
    PoemWord("smile 笑容",3,2,1),
    PoemWord("broken 破碎",3,1,2),
    PoemWord("precious 宝贵",3,2,1),
    PoemWord("prayer 祈祷",3,1,2),
    PoemWord("clumsy 笨拙",3,2,1),
    PoemWord("forgive 宽恕",3,1,2),
    PoemWord("nature 自然",3,2,1),
    PoemWord("ocean 深海",3,2,1),
    PoemWord("dazzle 炫目",3,2,1),
    PoemWord("special 特别",3,2,1),
    PoemWord("music 音乐",3,2,1),
    PoemWord("lucky 幸运",3,2,1),
    PoemWord("misfortune 不幸",3,1,2),
    PoemWord("loud 响亮",3,2,1),
    PoemWord("peaceful 平静",3,1,2),
    PoemWord("joy 愉悦",3,1,2),
    PoemWord("sunset 日落",3,2,1),
    PoemWord("fireflies 萤火虫",3,2,1),
    PoemWord("rainbow 彩虹",3,2,1),
    PoemWord("hurt 伤痛",3,1,2),
    PoemWord("play 玩耍",3,2,1),
    PoemWord("sparkle 闪耀",3,2,1),
    PoemWord("scars 伤痕",3,1,2),
    PoemWord("empty 空虚",3,1,2),
    PoemWord("amazing 惊喜",3,2,1),
    PoemWord("grief 悲伤",3,1,2),
    PoemWord("embrace 拥抱",3,1,2),
    PoemWord("extraordinary 杰出",3,2,1),
    PoemWord("awesome",3,2,1),
    PoemWord("defeat 击败",3,1,2),
    PoemWord("hopeless 无助",3,1,2),
    PoemWord("misery 痛苦",3,1,2),
    PoemWord("treasure 宝藏",3,2,1),
    PoemWord("bliss 福祉",3,2,1),
    PoemWord("memories 记忆",3,2,1),
    PoemWord("cute 可爱",2,3,1),
    PoemWord("fluffy 松软",2,3,1),
    PoemWord("pure 纯",1,3,2),
    PoemWord("candy 糖果",2,3,1),
    PoemWord("shopping 购物",2,3,1),
    PoemWord("puppy 狗狗",2,3,1),
    PoemWord("kitty 猫咪",2,3,1),
    PoemWord("clouds 云朵",2,3,1),
    PoemWord("lipstick 唇膏",1,3,2),
    PoemWord("parfait 帕菲",2,3,1),
    PoemWord("strawberry 草莓",2,3,1),
    PoemWord("pink 粉色",2,3,1),
    PoemWord("chocolate 巧克力",2,3,1),
    PoemWord("heartbeat 心跳",1,3,2),
    PoemWord("kiss 亲吻",1,3,2),
    PoemWord("melody 旋律",2,3,1),
    PoemWord("ribbon 缎带",2,3,1),
    PoemWord("jumpy 神经质",2,3,1),
    PoemWord("doki-doki 心跳",2,3,1),
    PoemWord("kawaii 卡哇伊",2,3,1),
    PoemWord("skirt 短裙",2,3,1),
    PoemWord("cheeks 脸颊",2,3,1),
    PoemWord("email 邮件",2,3,1),
    PoemWord("sticky 粘粘",2,3,1),
    PoemWord("bouncy 活力",2,3,1),
    PoemWord("shiny 闪亮",2,3,1),
    PoemWord("nibble 轻咬",2,3,1),
    PoemWord("fantasy 幻想",1,3,2),
    PoemWord("sugar 白糖",2,3,1),
    PoemWord("giggle 傻笑",2,3,1),
    PoemWord("marshmallow 棉花糖",2,3,1),
    PoemWord("hop 跃动",2,3,1),
    PoemWord("skipping 跳过",2,3,1),
    PoemWord("peace 和平",2,3,1),
    PoemWord("spinning 旋转",2,3,1),
    PoemWord("twirl 卷曲",2,3,1),
    PoemWord("lollipop 棒棒糖",2,3,1),
    PoemWord("poof 噗",2,3,1),
    PoemWord("bubbles 泡泡",2,3,1),
    PoemWord("whisper 耳语",2,3,1),
    PoemWord("summer 夏日",2,3,1),
    PoemWord("waterfall 瀑布",1,3,2),
    PoemWord("swimsuit 泳装",2,3,1),
    PoemWord("vanilla 香草",2,3,1),
    PoemWord("headphones 耳机",2,3,1),
    PoemWord("games 游戏",2,3,1),
    PoemWord("socks 袜子",2,3,1),
    PoemWord("hair 头发",2,3,1),
    PoemWord("playground 游乐场",2,3,1),
    PoemWord("nightgown 睡袍",1,3,2),
    PoemWord("blanket 毯子",1,3,2),
    PoemWord("milk 牛奶",2,3,1),
    PoemWord("pout 噘嘴",2,3,1),
    PoemWord("anger 愤怒",2,3,1),
    PoemWord("papa 爸爸",2,3,1),
    PoemWord("valentine 情人",2,3,1),
    PoemWord("mouse 老鼠",1,3,2),
    PoemWord("whistle 口哨",2,3,1),
    PoemWord("boop",2,3,1),
    PoemWord("bunny 兔子",2,3,1),
    PoemWord("anime 动画",2,3,1),
    PoemWord("jump 跳跃",2,3,1),
    PoemWord("determination 决意",1,1,3),
    PoemWord("suicide 自裁",2,1,3),
    PoemWord("imagination 想象",2,1,3),
    PoemWord("secretive 秘密",2,1,3),
    PoemWord("vitality 活力",1,1,3),
    PoemWord("existence 存在",2,1,3),
    PoemWord("effulgent 璀璨",1,1,3),
    PoemWord("crimson 绯红",1,1,3),
    PoemWord("whirlwind 飑风",1,1,3),
    PoemWord("afterimage 残影",1,1,3),
    PoemWord("vertigo 晕厥",1,1,3),
    PoemWord("disoriented 迷惘",1,1,3),
    PoemWord("essence 精髓",2,1,3),
    PoemWord("ambient 氛围",2,1,3),
    PoemWord("starscape 繁星",2,1,3),
    PoemWord("disarray 混乱",1,1,3),
    PoemWord("contamination 玷污",1,1,3),
    PoemWord("intellectual 智能",1,1,3),
    PoemWord("analysis 分析",1,1,3),
    PoemWord("entropy 熵",1,1,3),
    PoemWord("vivacious 生机",1,1,3),
    PoemWord("uncanny 诡异",2,1,3),
    PoemWord("incongruent 不相容",1,1,3),
    PoemWord("wrath 愤怒",2,1,3),
    PoemWord("heavensent 天赐",2,1,3),
    PoemWord("massacre 屠杀",2,1,3),
    PoemWord("philosophy 哲学",1,1,3),
    PoemWord("fickle 薄情",1,1,3),
    PoemWord("tenacious 执拗",1,1,3),
    PoemWord("aura 光环",2,1,3),
    PoemWord("unstable 动荡",1,1,3),
    PoemWord("inferno 炼狱",2,1,3),
    PoemWord("incapable 无能",2,1,3),
    PoemWord("destiny 宿命",2,1,3),
    PoemWord("infallible 万无一失",1,1,3),
    PoemWord("agonizing 折磨",2,1,3),
    PoemWord("variance 方差",1,1,3),
    PoemWord("uncontrollable 失控",2,1,3),
    PoemWord("extreme 极端",1,1,3),
    PoemWord("flee 逃跑",2,1,3),
    PoemWord("dream 梦想",2,2,3),
    PoemWord("disaster 灾难",2,1,3),
    PoemWord("vivid 生动",2,1,3),
    PoemWord("vibrant 震动",1,2,3),
    PoemWord("question 问题",1,2,3),
    PoemWord("fester 化脓",2,1,3),
    PoemWord("judgment 审判",1,1,3),
    PoemWord("cage 牢笼",1,2,3),
    PoemWord("explode 爆炸",1,2,3),
    PoemWord("pleasure 快感",1,2,3),
    PoemWord("lust 欲望",1,2,3),
    PoemWord("sensation 知觉",1,2,3),
    PoemWord("climax 高潮",1,2,3),
    PoemWord("electricity 电力",1,2,3),
    PoemWord("disown 否认",1,1,3),
    PoemWord("despise 蔑视",2,1,3),
    PoemWord("infinite 无尽",2,1,3),
    PoemWord("eternity 永恒",2,1,3),
    PoemWord("time 时光",2,1,3),
    PoemWord("universe 宇宙",2,1,3),
    PoemWord("unending 无尽",2,1,3),
    PoemWord("raindrops 雨滴",2,1,3),
    PoemWord("covet 觊觎",1,1,3),
    PoemWord("unrestrained 恣意",1,1,3),
    PoemWord("landscape 景观",2,1,3),
    PoemWord("portrait 肖像",2,1,3),
    PoemWord("journey 旅程",2,1,3),
    PoemWord("meager 匮乏",1,1,3),
    PoemWord("anxiety 焦虑",2,1,3),
    PoemWord("frightening 吓人",2,1,3),
    PoemWord("horror 恐怖",2,1,3),
    PoemWord("melancholy 忧郁",2,1,3),
    PoemWord("insight 洞悉",2,1,3),
    PoemWord("atone 赎罪",2,1,3),
    PoemWord("breathe 呼吸",1,2,3),
    PoemWord("captive 俘虏",2,1,3),
    PoemWord("desire 欲望",1,2,3),
    PoemWord("graveyard 墓园",2,1,3)
    ]

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1
##################################################################################
#These functions define random pause lengths for each of the stickers' movements.
#renpy.random.random() returns a random floating point number between 0 and 1
#So the -Doki-Time variable for each is a random decimal ranging from 4 to 8.
#These are used in the image definitions.

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0
##############These functions define random movements for the stickers.#######
    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0

##################################################################################


label poem(transition=True, chinese=True):
    stop music fadeout 2.0
    if persistent.playthrough == 3: #Takes us to the glitched notebook if we're in Just Monika Mode.
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu #This allows the player to pull up the save menu during the poem minigame.
    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid #Just Monika.
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left #Only show Sayori's sticker in Act 1.
        show n_sticker at sticker_mid #Natsuki's sticker
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right #Replace Yuri's sticker with the "cut arms" sticker..
        else:
            show y_sticker at sticker_right #Yuri's sticker
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch #Monika's sticker
    if transition:
        with dissolve_scene_full #Gives the dissolve transition if the minigame isn't called with False.
    if persistent.playthrough == 3:
        play music ghostmenu #Change the music in Just Monika.
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False #Not completely sure why skipping has to be explicitly disabled, but apparently it does..
    if persistent.playthrough == 0 and chapter == 0: #Shows the below dialogue the first time the minigame is played.
        call screen dialog("写诗时间到！\n请从下列词语中，挑选出你觉得部员们会喜欢的几个词，\n组成一首诗吧！要是你写的诗恰好让某位成员爱不释手，\n那么你和她之间可能会发生什么好事哦~", ok_action=Return())
    python: #Variable initialization here. Important to note, these initialize at the start of the mini-game.
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        if chinese:
            wordlist = list(full_wordlist_chs)
        else:
            wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1




        # Main loop for drawing and selecting words
        while True:
            ystart = 160
##################This block of code controls the word counter.###########################################
            if persistent.playthrough == 2 and chapter == 2:
                #This makes the counter do the "111111111" thing in Act 2.
                pstring = ""
                for i in range(progress):
                    pstring += "1" #Appends "1" to pstring each loop.
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000') #This is the word counter.
##################This block of code puts the poem words on the screen.###################################
            for j in range(2): #In python, range() is not inclusive. So j loops from 0 to 1.
                if j == 0: x = 440 #These two lines build columns out of the words. The first column is at 440px and the second at 680px.
                else: x = 680
                ui.vbox() #This is outdated UI code to create a vbox. It adds things to the vbox until it hits a ui.close()
                for i in range(5):
                    if persistent.playthrough == 3: #This sets all the words to "Monika" in Just Monika.
                        s = list("Monika")
                        for k in range(6): #This gives random corruption effects to the "Monika" words.
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, True) #This gives a chance for a random word in Act 2 to be the glitched word.
                    else: #Normal circumstances
                        word = random.choice(wordlist) #Pick a random word out the wordlist
                        wordlist.remove(word) #Remove the word from the list. This prevents a word from being on the screen twice.
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close() #Closes the vbox from above
##################This block controls what happens when words are selected.############################
            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch: #This conditional controls what happens when the glitch word is selected.
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    #The below three lines are just a scene statement in python. It's exactly the same as 'scene bg white'.
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0: #Act 1. This makes the stickers hop when words are picked.
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else: #Act 2
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop") #1/10 chance for Monika's sticker to show.
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop") #Since there's just Yuri and Natsuki in Act 2, whoever has the higher value for the word hops.
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg") #"y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop") #Yuri's cut arms sticker.
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10) #1/10 chance to hear "baa", one time.
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            #Add the word's point values to the running total
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            progress += 1
            if progress > numWords: #This stops the minigame once we've picked all the words.
                break
##################End of main loop.##################################################################

        if persistent.playthrough == 0:
            # For chapter 1, add 5 points to whomever we sided with
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            # Logic for taking point totals and assigning poem appeal, scene order, etc.
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            # Set poemwinner to the highest scorer
            poemwinner[chapter] = pointlist[2]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        stop music
        scene black with None
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes
        pause 0.5
        hide bg eyes
        show bg eyes_move
        pause 1.25
        hide bg eyes with None
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return
############ Image definitions start here. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0