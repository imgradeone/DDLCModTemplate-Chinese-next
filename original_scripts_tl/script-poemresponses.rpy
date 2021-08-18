## script-poemresponses.rpy

# This is where the doki's respond to how good or crappy the MC's poem
# Act 2 uses script-poemresponses2 but that is used as a hub for Act 2 responses to MC's poem
label poemresponse_start:
    # default count of poems being read at the beginning of poem sharing
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        # defaults skipping the poem sharing to false (no poem is shown)
        $ skip_poem = False
        # controls the audio played in the poem sharing. change t5 to a different audio track
        # if you want to use a custom poem share track
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        # controls if the track playing is the default track but if nothing is playing
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        $ skip_poem = False
        # sends the poem response to another label
        # if it's Act 2 else Act 1 responses
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        # MC's dialogue of who to share first or next
        if poemsread == 0:
            $ menutext = "我应该先跟谁分享我的诗呢？"
        else:
            $ menutext = "接下来要跟谁分享我的诗呢？"
        # Main Menu of the Poem Responses
        # You can add more boxes here by copy and pasting the others and changing
        # their variables and text to that new character
        menu:
            "[menutext]"

            "纱世里" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "果然还是先和纱世里分享最轻松自在了。"
                    "毕竟她是我的好朋友。"
                call poemresponse_sayori
            "夏树" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "我昨天跟夏树说我对她的诗感兴趣。"
                    "可能先和她分享会比较好一些。"
                call poemresponse_natsuki
            "优里" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "优里似乎是最有经验的，所以我应该先和她分享。"
                    "我相信她的意见是公允的。"
                call poemresponse_yuri
            "莫妮卡" if not m_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "我应该先从莫妮卡开始。"
                    "她昨天似乎非常想读我的诗，而我也想让她看到我的努力。"
                call poemresponse_monika
        # Adds a new poem read point per poem share
        $ poemsread += 1
        # Asks if poems shared is less than set value for Act 2 or Act 1
        # Act 2 uses 3 while 1 uses 4. If true poem sharing loops to certain value until it's false
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # defaults to poem responses
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

# Everything below here under poemresponse_ is the script used per doki
# All comments below Sayori applies to all doki's (Monika does not have a med value. only good or bad)
label poemresponse_sayori:
    # default scene and pose
    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    # default opinion
    $ poemopinion = "med"
    # asks if the doki's appeal in the poem game was bad or -1. if true opinion is bad
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    # asks if the doki's appeal in the poem game was good or 1. if true opinion is good else med or meh
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    # sets the label for the response to the chapter with their opinion
    # If Act 2 is active it adds 2 to it (e.g Act 1 - ch2_n_bad | Act 2 - ch22_n_bad)
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    # calls nextscene which has the opinion of the doki for that chapter
    call expression nextscene
    # asks if poem was not skipped. if true it calls the ending of the poem sharing
    # if true it skips and returns to the poem response menu or to the normal game script
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene
    return

label poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse_yuri:
    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene
    return

# Monika does not use ch2_m_good. instead it's ch2_m_start or Act 2 ch22_m_start
# she does not not have a med opinion. only good or bad
label poemresponse_monika:
    scene bg club_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene
    return

# This is where the responses are said.
# call showpoem calls the poem from poems.rpy to be displayed
# img="yuri 3t" is the pose the doki should be when the scene happens hiddenly
label ch1_y_end:
    call showpoem (poem_y1_chs, img="yuri 3t")
    y 3t "..."
    y "抱...抱歉，我的字写得太丑了！"
    mc "什么？？"
    mc "我可完全没这么想..."
    y 2v "但是你花了很久才读完啊..."
    mc "啊——"
    mc "嗯，我只是不怎么读手稿..."
    mc "我其实觉得你的字挺漂亮的呢。"
    y 2t "诶？"
    y 2u "真是...松口气了..."
    mc "还有，诗本身我也很喜欢。"
    mc "虽然短，但表达得相当生动。"
    y 2t "是不是太短了？"
    y "我一般会写长一些的诗..."
    mc "不要紧的。"
    y 1m "很...很高兴你能喜欢。"
    y "说实话..."
    y 1a "毕竟这是我们第一次分享诗作，所以我想写得浅显一些。"
    y "或者说是容易消化理解。"
    mc "优里，你对幽灵很感兴趣吗？"
    y 1m "呼呼。"
    y "[player]，实际上，故事跟幽灵完全没关系哦。"
    mc "真的吗？"
    mc "我肯定完全理解错了..."
    y 1u "嗯，毕竟你只是草草浏览了一下..."
    y "不过你要记住，诗人常常会在自己的作品中表达他们的思想、情感以及经历。"
    y 1a "他们通常并不会只讲简单一个的故事，或是单纯把画面描绘出来。"
    y "在这种情况下，诗的主体只是象征意义上的幽灵。"
    y 2l "徘徊在她最后一处安身立命之所，无法对往昔释怀。"
    y "而且很快就会一无所有..."
    mc "...这样一解释，诗就严肃了很多。"
    mc "我想都没有想到过那些东西..."
    mc "真是令人印象深刻。"
    if poemopinion == "good":
        y 2f "诶？"
        y 3v "没-没什么，真的！"
        y "你的诗也非常让人印象深刻，所以..."
        mc "不..."
        mc "恰恰相反，倒是我可以从你身上学到一两点。"
        y 4a "...你是这么想的吗？"
        mc "嗯，当然啦。"
        y "啊..."
        y 2s "你知道的..."
        y "这些事情都会让我非常紧张。"
        y "不过到头来，我自己也很享受。"
        y "我会继续为你尽力的，[player]！"
        mc "啊..."
        mc "我也是。"
    else:
        y 1u "其实真的没什么..."
        y "不过...你能这么想，我很开心。"
        y 1a "不过你要记得，很快你也会领略这些东西的。"
        mc "嗯，或许你说得没错。"
        mc "看来我必须要继续努力了。"
        y "我相信你。"
    return

label ch2_y_end:
    call showpoem (poem_y2_chs)
    y 2m "唔..."
    y "比起昨天那首，我在这首诗上面更大胆了一些..."
    mc "看得出来。"
    mc "它要隐喻得多..."
    "不知道是不是我自身的问题，我无法猜想出这首诗的主题。"
    y 1a "说得没错。"
    y "它更接近于我偏爱的写作风格..."
    y "将诗词作为画布来表达生动的意象，并通过它们传递情感。"
    mc "嗯，如果只从表面意义来看的话，我都不清楚它想要表达什么..."
    y 2f "好吧..."
    y "我觉得每个人都可以用自己的方式理解。"
    y "我想表达的是我沉溺于不寻常爱好的感觉..."
    y 2v "这些东西在平时只能深藏在我的内心。"
    y "因此，我有时候会很享受写这些东西。"
    # asks if Natsuki read your poem already or if she liked Day's 1 or 2 poems
    if n_readpoem and (n_poemappeal[0] >= 0 or n_poemappeal[1] >= 0):
        mc "嗯，有意思..."
        y 2e "...？"
        mc "夏树不也写了类似的东西吗？"
        mc "有些人会因为一个奇怪的兴趣而被嘲笑。"
        y 2h "诶？"
        y "她...她也写了？"
        mc "是啊..."
        mc "她写的是只要不会伤害到别人，那么什么样的爱好都可以。"
        y 3r "她--她说得没错！"
        y 3o "啊--我是说..."
        y "她真的这么觉得吗...？"
        mc "是啊。"
        mc "看起来你们在这一点上还是一样的..."
        y 3h "很...嗯，很有趣..."
        y "对我来说，她看起来像是会取笑我的爱好的人..."
        y "不过我觉得我也不该评判她，不是吗...？"
        y 3p "啊-- 请不要跟她说我刚刚的话！"
        mc "啊哈哈。别担心，我不会那样做的。"
        y 1l "好的..."
        y 1a "嗯，谢谢你和我分享。"
    else:
        mc "为什么你要把它们藏在心里呢？"
        y 3v "因...因为..."
        y "很尴尬啊..."
        y "而且大家会取笑我的。"
        y "你没有类似的爱好吗，[player]？"
        mc "好吧..."
        mc "嗯，我觉得我也有..."
        y 2h "我觉得每个人都有那样的小爱好。"
        y "我们能做的就是，尊重彼此以及我们自己的个性。"
        y "虽然有的时候会比较难，有些事情也会让我们感到不安..."
    y 1a "但毕竟，要是我没有学会如何接纳自己的怪异，那么我也许就会讨厌自己了。"
    y 2u "我-我好像有点胡言乱语了..."
    y "...你能耐心倾听真的是太好了。"
    if y_appeal >= 2:
        y 2s "你擅长很多东西..."
        y "写作，倾听..."
        y 2u "像你这样的人已经不多了，[player]..."
        mc "这-这有些夸张了吧..."
        y 2v "这就是...我的感觉。"
        y "我从来没有想到过，我会对分享自己的文字感到如此安心..."
        y 2s "不过现在，我感觉自己变得很期待..."
        y 2m "这对我来说...真是个美好的感觉。"
        y "而你就是我为此要感谢的人。"
        mc "没...没什么的，真的..."
        "优里真诚地对我微笑着。"
        "有那么一瞬间，她的胆怯似乎消失了。"
    return
label ch3_y_end:
    # tells the game you shared with that doki 3 times
    $ y_read3 = True
    # asks if Yuri liked all 3 poems. if true it jumps to a special response label
    if y_appeal >= 3:
        jump ch3_y_end_special
    call showpoem (poem_y3_chs, img="yuri 2v")
    y "唔..."
    y "我知道写沙滩是一件很空洞的事情。"
    y "不过我已经尽力使用了隐喻的手法。"
    # asks if Natsuki read 3 times or liked all your poems
    if not n_read3 or n_appeal >= 3:
        mc "你说得就像是你不愿意写沙滩一样..."
        y 2e "哦，你没听说吗...？"
        y 2h "昨天之后，夏树和我...嗯..."
        y "当时我们两个...用了不同的手法写了相似的东西，非常有趣。"
        y "所以，夏树想要我和她再写一次相同的主题。"
        if n_readpoem:
            if not n_read3:
                mc "明白了..."
                "夏树并没有给我看她写的那首诗，所以我也不好评判。"
            else:
                mc "明白了..."
                "由此可知，夏树给我看的那首诗，并不是她打算给其他人看的那首..."
                "当然，我选择对优里进行了隐瞒。"
    else:
        mc "是的，夏树已经跟我说过了。"
        y 3t "她-她说了...？"
        y "她没说什么奇怪的东西吧，有吗？"
        y "她只是想要我们再写一次相同的主题..."
    y 2f "我觉得这样能更好地比较我们的写作风格...或者说思维过程。"
    y 2w "不管怎么说，这是她的主意...！"
    y "你知道她的，她想这么做也并不奇怪。"
    y "她可能只是想要卖弄一下。"
    y 2v "我对她的写作风格没有什么特别的兴趣..."
    y "只是按照她的要求做了。"
    y "不过..."
    y 1s "好吧，我觉得偶尔写写简单的东西也没那么糟。"
    y 1m "它可以让人耳目一新，你懂吗？"
    y "可以让我偶尔平静一下我的思绪。"
    mc "嗯...我同意。"
    mc "谢谢你的分享。"
    return
label ch3_y_end_special:
    call showpoem (poem_y3b_chs, img="yuri 4b")
    "在读完诗后，我想把它还给优里。"
    "不过她并没有接过去，而是看向了一边。"
    y "..."
    y "你是...不喜欢吗？"
    mc "啊--不，当然不是。"
    mc "我只是...不知道自己应该怎么回应。"
    "虽然优里的诗通常都有些晦涩，但是想要理解这首诗并不难。"
    if n_read3:
        "而且，这显然不是夏树说她写的内容..."
        "...也就是说，我可能是她唯一展示过那首诗的人。"
    y 2v "我-我不知道自己能不能解释清楚这首诗..."
    mc "没关系。"
    mc "我能理解这首。"
    y 4c "..."
    "优里现在说起话来比平时还要困难。"
    mc "这首诗...对你很重要吗？"
    "优里点了点头。"
    mc "我不是很擅长言辞，不过..."
    mc "很高兴你能和我分享。"
    mc "所以，谢谢你。"
    mc "希望我们还能一起共度时光。"
    show yuri 4e
    "尽管我无法进行眼神接触，但我还是看到了优里唇边浮现了淡淡的微笑。"
    "我又一次试着把诗还给她。"
    show yuri 4a
    "但是优里轻轻地抓住我的手、推回到我的身上。"
    "我不知道该对她那温暖的触碰做出怎样的回应。"
    y 1v "你可以..."
    y "唔..."
    y "这首诗..."
    "优里又一次无法完整地组织起一句话。"
    mc "你是说我可以留着它？"
    "优里点了点头。"
    mc "我很乐意。"
    show yuri 1u
    "优里又淡淡地微笑了起来，似乎不想让我注意到。"
    y "你总是.."
    y "你总是...让我感觉很好。"
    y "我知道我不擅长和人打交道，不过..."
    y "我希望...自己有些时候能回报一下。"
    mc "嗯。"
    mc "别担心。"
    mc "我觉得你做得挺好的。"
    "优里终于转过身面对着我。"
    y 1s "我想...在莫妮卡说话前，我们得进行下一步了。"
    y "不过我们之后肯定能再聊聊的..."
    mc "是的。"
    mc "一定会的。"
    "就这样，优里羞怯地对我笑了笑，而我回到了座位上，将她的诗收了起来。"
    return

label ch1_n_end:
    call showpoem (poem_n1_chs, img="natsuki 2s")
    n 2q "嗯..."
    n "我就说你不会喜欢的嘛。"
    mc "我喜欢。"
    n 2h "什么？"
    n "说实话！"
    mc "我确实喜欢。"
    mc "你怎么就这么肯定我不会喜欢呢？"
    n 5w "嗯——"
    n "因为！"
    n "高中里每个人都都觉得，写作就一定得深奥复杂什么的..."
    n 5q "所以大家都不把我的文章当回事。"
    mc "但是，诗的意义不就是要表达自己吗？"
    mc "你的写作风格并不会使主旨逊色一分。"
    n 1k "是的！就是这样！"
    n "我喜欢那些读起来容易，但是又能狠狠触动你的诗。"
    n 1c "就像这首诗一样。"
    n "看着身边的所有人都成绩斐然，会让人相当灰心气馁..."
    n "所以我就决定把这种感觉写下来。"
    mc "嗯，我能理解。"
    n 2a "不过简洁的写作还有一个好处，它可以更注重文字游戏。"
    n "比如说，我在每句话末尾设置了韵脚，但最后一句就故意押错韵。"
    n "这样就能够在最后一行点睛，引出这种因平凡而气馁的感觉。"
    mc "所以你写得..."
    mc "似乎比我意识到的还要更深奥一些。"
    n 4y "这就是专业嘛！"
    n "很高兴你能学到些东西。"
    n "你没想到会从年纪最小的人身上学到东西吧？"
    mc "是啊...确实没想到。"
    "我决定就这样迁就她一次。"
    "我其实并不在意大家的年纪，不过如果夏树对此感到自豪的话，那么我也不会说破的。"
    return

label ch2_n_end:
    call showpoem (poem_n2_chs)
    n 2a "还不错，是吧？"
    mc "比起昨天那首要长多了。"
    n 2w "昨天那首太短了..."
    n "我只是热热身而已！"
    n 2c "希望你不会误以为那是我的上限。"
    mc "不，当然不会..."
    n 2a "不管怎么说，这首诗的主旨还是相当直白的。"
    n "我都怀疑需不需要我来解释。"
    n 2c "有时候你可以用简单的类比来解释复杂的事情..."
    n "而且这样可以让大家意识到他们一直以来有多笨了。"
    n 2g "比如说，所有人都会认同这首诗的主题是一个愚昧的混蛋..."
    mc "你认识这样的人吗？"
    n 2c "当然啦。这首诗就是关于大家怎么看待我的--"
    n 5w "...这无关紧要！关于什么都行！"
    n 5h "我写它是为了容易联系起..."
    n "所有人都会有某种古怪的爱好，或者说是一种带有负罪感的快乐。"
    n 5q "某种你害怕别人发现、并且因此取笑或是看轻你的东西。"
    n 1e "...但这只会让人变得愚蠢！"
    n "只要他们没有伤害到任何人，并且从中得到了快乐，谁会在乎他们喜欢什么呢？"
    n 1q "我觉得人们真的需要学会尊重他人的古怪爱好..."
    if y_readpoem and (y_poemappeal[0] >= 0 or y_poemappeal[1] >= 0):
        mc "唔，很有意思..."   
        mc "优里今天也写了类似的东西。"
        n 1h "嗯？"
        n "你刚刚说了优里？"   
        mc "是啊..."   
        mc "她说她的诗是关于自己的一个不寻常的爱好。"  
        mc "我不是很能理解，不过她说的跟你差不多..."   
        mc "人们不应该让彼此因为这些而感到不安。"  
        n 1q "真的吗？"
        n "好吧..."
        n 1t "我是说，优里挺古怪的，所以我也毫不怀疑她会有些古怪的爱好..." 
        n "...而不是说这样有什么不对！"
        n 1u "唔..."   
        n "我并不是...评判她什么的..." 
        "夏树不知道该说什么。" 
        n 1q "我-我想我应该试试，不要那么刻薄地对她..."
        n "既然她对于自己的古怪行为感到不安的话..."
        n "我是说，我很讨厌那些让我觉得不安的人..."
        n 1w "而优里昨天就让我觉得不安了！"
        n 1s "不过从你说的话来看，她似乎已经吸取教训了..." 
        mc "是的，我也这么觉得。"  
        mc "即便她的写作风格和你大不相同，我也敢肯定地说，她会喜欢你诗里的主旨的。"
    else:
        mc "嗯，你说得没错。"  
        mc "至少我可以联想到。"
        mc "而且我相信很多人也可以。"  
    if n_appeal >= 2:
        n 4h "那个..." 
        n "我很高兴你能欣赏这类文字..."
        n 4q "我是说...我知道我昨天已经说过了。"   
        n "不过我一直...嗯，我一直都很享受和你分享我的文字，所以..."   
        n 4w "...所以你就想想自己有多幸运吧，好吗？"   
        mc "啊哈哈。"  
        mc "好啦，谢谢你的坦诚。"  
        n 1n "你这么说是什么意思？"
        n "我一直都很坦诚的！" 
        n 12b "天哪..."
        n "你也期待一下明天，可以吗？" 
        mc "好的，我会的。"
    else:
        n 4c "毕竟那是我最擅长的！"
        n "除非能从中传递出一个好的主旨，不然我都不喜欢写作。" 
        n "比如说，传递情绪很重要..."  
        n "但是我想要让人们思考，而不是单纯地感受。"   
        n 4b "记住这点！"  
        n "我也会为明天写一首好诗的，所以敬请期待。"   
    return
label ch3_n_end:
    $ n_read3 = True
    if n_appeal >= 3:
        jump ch3_n_end_special
    call showpoem (poem_n3_chs)
    n 2a "嗯..."
    n "我感觉自己一直在写消极的东西，所以我这次想要写点有积极意义的东西。"
    n 2z "况且...沙滩太棒了！"
    n 2j "很难写出关于沙滩的消极内容。"
    if not y_read3 or y_appeal >= 3:
        mc "所以你是先决定写沙滩，然后再想出主旨的？"
        n 2c "嗯，是的..."
        n "只是因为昨天发生的事情。"
        n 5q "我是说，在优里和我意识到我们写了同一件东西的时候..."
        n "她想挑一个主题，让我们俩都写它，差不多就这样。"
        if y_readpoem:
            if not y_read3:
                mc "我明白了..."
                "其实我根本没看优里写的诗，所以我也不好评判..."
            else:
                mc "我明白了..."
                "由此可知，优里给我看的那首诗，并不是她打算给其他人看的那首..."
                "当然，我选择对夏树进行了隐瞒。"
    else:
        mc "好吧，优里处理地更严肃一点。"
        n 5h "嗯，那--"
        n 42c "天哪...她最好没有说我的坏话！"
        n "毕竟是她想让我们写同一个主题的。"
    n 1s "呃...你也能看出这是她要求的吧。"
    n "让我们两个写同一个主题，然后试图用一些花哨的东西打动我。"
    n 1w "好吧，其实我并不在乎。"
    n "我只是这么做了而已。"
    n 1q "我是说，我觉得我的诗最后也有些隐喻..."
    n "...不过偶尔这么做也没什么问题啊！"
    n "至少这是也一次不错的练习。"
    return
label ch3_n_end_special:
    call showpoem (poem_n3b_chs)
    n 1q "..."
    n "...为什么你要那样看着我？"
    n "如果你不喜欢，那你就说出来。"
    n 1u "我不会...生气的。"
    mc "不，我不是不喜欢它...！"
    mc "它只是...读起来有些让人惊讶。"
    if y_read3:
        "这首诗显然不是优里告诉我的那首..."
        "...也就是说，我可能是看过这首诗的人。"
    mc "呃...我觉得我只是还不习惯从你身上听到这样的好话..."
    n 1h "别-别那么说！"
    n 1n "笨蛋..."
    n "你觉得...写作的意义是什么？"
    n 1u "表达你无法说出来的东西..."
    mc "是的...我能理解。"
    mc "很抱歉，有时候我会忽略重点。"
    mc "我的本意是好的..."
    mc "而且...我很高兴你能把它拿给我看。"
    mc "我很喜欢。"
    n 1h "好吧...嗯..."
    n 1q "我...我是专业的，所以..."
    "夏树嘟囔着，完全不像她平时自信的样子。"
    n "一定要..."
    n 12c "你给我记得...有时候我也会思考这些东西！"
    n "你知道的，当你对我好的时候，它..."
    n 12a "..."
    n "...就很有意义。"
    mc "啊...我很高兴。"
    "感觉到夏树满意了之后，我想把诗还给她。"
    "但当我这么做时，夏树抓住了我的手、推回到我的身上。"
    "她那又小又软的手坚决得让我吃惊。"
    n 12b "我不要。"
    mc "诶...？"
    mc "为什么？"
    n 12c "我就是不要！"
    n "天哪..."
    "我意识到了夏树在做什么。"
    "她做不到坦诚，所以只好用迂回的手段，试图把诗交给我。"
    mc "好吧...这样的话，那我就收下了。"
    "我没有调侃她，而是选择了照做。"
    n 1t "...很好。"
    n "如果你不这么做的话，我会..."
    n "..."
    n 1h "算了..."
    n 1q "我只是...很高兴你会收下它。"
    "夏树欲言又止地只说到了这里。"
    "尽管她已经尽力隐藏自己的表情了，但我还能看到她淡淡地微笑了起来。"
    n "就这样吧，那么..."
    n 1s "在别人看到之前把它收起来，好吗？"
    mc "啊...好的。"
    mc "我会的。"
    "就这样，我回到了自己的座位上，将夏树的诗收了起来。"
    return

label ch1_s_end:
    call showpoem (poem_s1_chs)
    mc "纱世里..."
    mc "让我大胆猜一猜..."
    mc "你是不是今早才写了这首诗？"
    s 4h "不是！"
    s 4l "只...只有一点啦！"
    mc "你不能对一个是非问题回答'只有一点'..."
    s 5b "我昨晚忘了写嘛..."
    mc "好吧，至少这让我的自我感觉好了些..."
    s 1h "不要这么过分啦！"
    s "毕竟我还是有尽力的啊..."
    mc "啊，好吧..."
    mc "我不是说这首诗不好。"
    mc "结果还不错...嗯，该怎么说好呢..."
    mc "这很纱世里。"
    s 1d "真的吗？"
    mc "嗯。"
    mc "尤其是最后一行..."
    s 4r "我做了鸡蛋和烤面包！"
    mc "即便你上学要迟到了...？"
    s 5d "不吃早饭是不好的！"
    s "我整个人都会变得暴躁..."
    mc "好吧，我觉得这也没什么好争的..."
    mc "不管怎么样，谢谢你能给我看这首诗。"
    s 1q "诶嘿嘿～"
    s "真是太有意思了。"
    s "莫妮卡是最棒的！"
    mc "啊...没错。"
    s "不过下一次，我不会忘了写的。"
    s 4x "而且我会写出最好的诗！"
    mc "好啊，我很期待。"
    return

label ch2_s_end:
    call showpoem (poem_s2_chs)
    mc "天啊..."
    mc "纱世里，这真的是你写的吗？"
    s 2j "当然是我写的！"
    s "我昨天不是告诉过你，我要写出最好的诗吗？"
    mc "说了，但是..."
    mc "我是说，我从没有预料到会从你手里拿到这样的一首诗。"
    s 4x "莫妮卡教了我很多东西！"
    s "而且我最近情感很丰富..."
    mc "我看出来了..."
    mc "简直有些吓人。"
    s 1b "吓人...？"
    mc "好吧，准确地来说并不是..."
    mc "大概是因为我太习惯于你一直以来开心的样子吧..."
    mc "...算了，别在意。"
    mc "我有些想过头了。"
    mc "关键在于，结果还挺不错的，所以应该为此感到自豪。"
    s 1y "啊，谢谢～"
    s "我觉得..."
    s "我觉得就是要用这种方式表达自己。"
    s "它甚至让我对自己的情感有了更好的理解..."
    s 1a "写作真像魔法啊！"
    mc "你已经对此相当有热情了吧，嗯？"
    mc "希望能够继续保持。"
    s 4r "是的！"
    s "写作最棒了！"
    s "我要一直写到我死的时候！"
    mc "啊哈哈...别想太远了。"
    "纱世里一直有个三分钟热度的习惯，通常不超过一个星期就会放弃。"
    "我在想这会不会也是其中之一？"
    "不过从她眼中的激情来看，这么想是不是有点悲观了。"
    return
label ch3_s_end:
    return

label ch1_m_end:
    call showpoem (poem_m1_chs)
label ch1_m_end2:
    m 1a "那么...你觉得如何？"
    mc "唔...这首诗非常...不拘一格，应该是这么说吧。"
    mc "抱歉，我真的不是征求反馈意见的合适人选..."
    m 2e "啊哈哈。没关系。"
    m 2b "嗯，这种风格现在已经相当流行了。"
    m "也就是，很多诗会注重强调词和行之间的节奏把控。"
    m 2a "大声朗读出来时，就能极具感染力。"
    mc "这首诗背后的灵感是什么？"
    m "啊..."
    m 3d "嗯，我不太确定能不能表达好..."
    m 3a "我想可以这么说，我最近有些顿悟了。"
    m "而这也稍微影响到了我的诗。"
    mc "顿悟？"
    m 1a "是的...诸如此类的东西吧。"
    m "我对于谈论这些深层次的东西有些紧张，因为这聊起来显得有点咄咄逼人..."
    m "也许是在大家的友谊更进一步之时降临的吧。"
    m 1j "总之..."
    m 3b "以下是莫妮卡的今日写作小窍门！"
    m "在写诗（或者是写故事）的时候，你的大脑会过分执着于某个特定点上..."
    m "如果过于追求完美的话，那就永远不会有任何进步。"
    m "只要强迫你自己在纸上写下一些东西，事后再整理就行了！"
    m "可以换个角度这样想："
    m "如果你把钢笔放在同一个位置太久，那么你只会得到一个很大的黑色墨点。"
    m "所以只要挥洒起来，顺其自然就行了！"
    m 3k "...以上就是我今天的建议！"
    m "感谢倾听～"
    return

label ch2_m_end:
    call showpoem (poem_m2_chs)
    mc "嗯..."
    mc "这首比你上次那首还要抽象，嗯？"
    m 5 "啊哈哈..."
    m "我想这就是我写作的方式..."
    m "如果你不喜欢的话，那我很抱歉。"
    mc "不，我没这么说。"
    mc "只不过这是我以前闻所未闻的东西而已。"
    m 2a "我喜欢在诗句的布局上做文章..."
    m "选择在何处以何种方式间隔词语，会让整首诗的氛围变得完全不同。"
    m 2b "就像是魔法一样。"
    m "我这种写很多短句的写法，让它感觉像是要盖过噪音似的。"
    mc "我明白了..."
    mc "不过我还是很难理解这首诗是关于什么的。"
    m 2k "啊哈哈。"
    m 4a "有时候，询问诗词关于什么其实并不正确。"
    m "一首诗可以像情感的物理表达一样抽象。"
    m "也可以是和读者的对话。"
    m "所以从这个角度来看，并不是所有的诗都是{i}关于{/i}某些东西的。"
    m "好了..."
    m 3b "以下是莫妮卡的今日写作小窍门！"
    m "有时候你会发现自己面对一个非常困难的抉择..."
    m "当这样的情况发生时，别忘了保存游戏！"
    m "你永远也不会知道什么时候你会改变主意...."
    m "...或者什么时候会发生意外的事情！"
    m 3d "等等...这个是关于写作的窍门吗？"
    m 3k "我到底在说什么？"
    m "啊哈哈！"
    m 3b "...以上就是我今天的建议！"
    m "感谢倾听～"
    return
label ch3_m_end:
    call showpoem (poem_m3_chs)
    m 1a "那个..."
    m "我认为学习和寻找答案是能赋予生命意义的一类事情。"
    m 1e "不是太多哲学层面上..."
    m 1a "而是在我的脑海里，所以这就是我写的东西。"
    mc "我明白了..."
    mc "我从没有深入地想过。"
    m 1d "某种意义上来说，它有些自相矛盾。"
    m "因为如果我们都去寻找答案了，那么世界不就失去它的意义了吗？"
    mc "嗯，我注意到了一件事情..."
    mc "似乎社团里的每个人更喜欢写悲伤的、而不是快乐的东西。"
    m 1k "啊哈哈，你很惊讶吗？"
    m 1a "我是说，如果一切都好的话..."
    m "那我们就没什么可写的了，不是吗？"
    m "人类不是二维生物。"
    m "我觉得你应该比所有人都要理解这一点。"
    mc "你是说一维...？"
    m 1l "啊...是的，就是那样！"
    m 1a "好了..."
    m 3b "以下是莫妮卡的今日写作小窍门！"
    m "你有没有因为害怕写得不够好，而羞于和别人分享自己的文字？"
    m "自己倾注了很多的作品，却只得到了冷淡的反应，真是令人沮丧。"
    m "但是如果你找到其他喜欢写作的人，那么分享就会变得容易很多！"
    m "因为他们不会仅仅告诉你，你写得好、一般还是糟糕..."
    m "他们会更注重一切深层次的内容，以及你可以提升的地方。"
    m "这种方式更鼓舞人，而且会让你想要继续进步。"
    m "就像是你有自己的小文学部一样，不是吗？"
    m 3k "...以上就是我今天的建议！"
    m "感谢倾听～"
    return


label ch1_n_bad:
    n "..."
    mc "...?"
    # asks if it's in Act 2 mode and if random number is 0. if true special scene happens
    if persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0:
        $ currentpos = get_pos()
        stop music
        $ pause(2.0)
        play sound "sfx/stab.ogg"
        show n_blackeyes zorder 3 at i11
        show n_eye zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        show blood zorder 3:
            pos (645,255)
        show blood as blood2 zorder 3:
            pos (575,260)
        $ pause(0.75)
        hide n_blackeyes
        hide n_eye
        hide n_eye2
        hide blood
        hide blood2
        stop sound
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    n 2b "[player]，如果你不认真对待社团的话，那么请你直接回家。"
    mc "什-什么？？"
    mc "无情..."
    n 42c "你在说什么，你以为我会相信，你真的付出了努力了吗？"
    n "你以为我是傻的？"
    mc "我不是个作家！"
    mc "可能它不太好，但是没错，我确实努力了。"
    mc "我们都有个起步过程，不是吗？"
    mc "如果你还对 {i}你{/i} 写的第一首诗非常自豪的话，那么我很想读一读。"
    n 1o "！！"
    mc "回想起来很痛苦？"
    n 1r "..."
    n 5q "好吧。"
    n "那个，对不起。"
    n 5c "反正你以后会写得好起来的。"
    n "我会告诉你需要改进什么，不过你最好还是再尝试一次。"
    mc "说得在理..."
    mc "嗯，我觉得，每个人都有选择喜好的权利。"
    n 5q "不管怎么说，我猜现在该由我来分享诗了..."
    n "以我对你的了解，你可能会觉得它很傻。"
    return

label ch1_n_med:
    n "..."
    mc "...？"
    n 2k "...好吧，符合我对你这种人的期待。"
    mc "你这话说得有些直接了..."
    n 2c "好吧，那就对不起咯。"
    n "我也没说它写得很烂啊。"
    n "只不过它并不能唤起人的任何情感。"
    mc "所以简单点说，对你的口味而言，它还不够可爱？"
    n 4f "你是想挨揍吗？"
    mc "当我没说..."
    n 42b "唉..."
    n 42c "反正无论如何，我还是得给你看看我的诗。"
    n 4q "不过，这首诗不像是你会喜欢的类型。"
    return

label ch1_n_good:
    n "..."
    mc "...？"
    n 1t "...好了，我们先从我不喜欢的地方开始！"
    n "首先，呃..."
    mc "..."
    "夏树又读了一遍我的诗。"
    n 4c "算-算了。我不想给你我的意见。"
    mc "诶？那分享又有什么意义呢？"
    mc "我在写它的时间里，本来可以做其它事情的。"
    n 4r "呜..."
    mc "实际上，你还记得我是怎么说我想要读你的诗的吗？"
    mc "这就是我在写这首诗时，脑海中想着的东西。"
    mc "我想要让你对分享你的诗感到安心。"
    mc "就像莫妮卡说的那样。"
    n 4x "呜...!"
    n 1h "嗯，要是你的诗很烂的话，我会更安心于分享我的诗！"
    n 1w "你应该给我看一首非常蠢的诗，然后我就可以说'哈，这可不太行，让我给你看看真正的文学是怎么样的吧！'"
    n 1h "但是你却毁了它！"
    n "你高兴了吧？！"
    mc "..."
    mc "...所以，换句话说，你是在说你喜欢这首诗？"
    n 1o "呃--"
    "夏树的反驳被卡在了喉咙里。"
    n 1x "呜呜呜...你真是太...！"
    n "你...你...什么都不懂，对吗？"
    n 5q "我已经跟你说了，你不需要这样对着全世界宣布，就好像你很高傲一样！"
    mc "我很确定你真的没有说过..."
    "我这句话基本是在对自己说。"
    "夏树肯定很讨厌我了吧。"
    "我不知道她喜欢我的诗，是意味着我的胜利还是失败。"
    mc "不管怎么说...你还是得给我看看你的诗，不是吗？"
    n 5s "呃...好吧。"
    n "只是因为如果我不这么做的话，莫妮卡会让我这么做的。"
    return

label ch2_n_bad:

    if n_poemappeal[0] < 0:
        n "...哼。"
        n 2k "好吧，不得不说它比上一首更好。"
        n "很高兴能看到你的努力。"
        mc "那就好..."
        n 2c "但我还是一点都不喜欢这首。"
        n "它太严肃了。"
        mc "诶？你这么说是什么意思？"

        # label if Nat hated your last poem in Day 3
        label ch2_n_bad_sharedwithch3:
            n 4c "诗词不需要全都用深刻的手法来表达。"
            n "除非你真的擅长，否则感觉起来会像是你在强行那么做。"
            n 4w "老实说...除非你到了优里那样的层次，否则不要尝试这样写诗--"
            show natsuki 4o
            "夏树突然停了一下。"
            n 1o "你-你别...告诉我..."
            mc "诶？"
            n "你不会...你不会是想要打动优里吧，是不是？！"
            mc "你-你在说什么？？还有，你小声点...！"
            n 1x "你知道优里会喜欢这种...这种恐惧感......！！"
            mc "她是一个有天赋的作者并不意味着...我-我是说..."
            n 1o "呜....！！"
            "我似乎遇到了麻烦。"
            "我不知怎么地被触动了一下神经，但是我不知道该怎么办。"
            n 1c "我受够你了。"
            "夏树把我给她的诗塞回给我。"
            n 5w "拿好你的傻逼诗。如果你是写给别人的，那么就别拿给我看！"
            mc "哎呀..."
            "这就是让一个比我小的女生接入到我的个人事务的后果。"
            "除非我能读心，不然我从一开始就注定要陷入到痛苦的世界中。"
            "至少夏树不是我当初想要打动的女孩..."
            $ skip_poem = True
            return
    else:


        n 1k "...哼。"
        n "我更喜欢你的上一首诗。"
        mc "诶？真的吗？"
        n 2c "是啊。我能看出来你在这一首上大胆了一些。"
        n "但是你做得还不够好。它没达到效果。"
        mc "你说的或许没错，不过我只是想要尝试不同的东西。"
        mc "我还在摸索过程中。"
        n 2k "我是说，我喜欢那些没有用力过头的诗。"
        n 2q "我讨厌人们试图使用恼人的复杂语句，让文字看起来很棒、又或是加入更多的含义。"
        n 4b "只要做到简单、可爱、抓住重点就行了！"
        n 4y "优里对这些晦涩的废话神魂颠倒，但是我已经看穿了这种把戏了。哈！"
        n 42a "让你的读者需要如此努力地寻找深层意义，这只不过是对于毫无意义的一个借口罢了。"
        mc "我觉得这也不失为看待它的一种方式。"
        n 2d "好吧，每个人都有自己的观点。"
        n "不过我的观点是最好的观点。我敢肯定你已经明白了。"
        mc "呃..."
        n 2a "好了，这是我的诗。也许你能从中学到什么。"
        return

label ch2_n_med:

    if n_poemappeal[0] < 0:
        n "...哼。"
        n 2k "好吧，不得不说它比上一次要好。"
        n "很高兴能看到你的努力。"
        mc "那就好..."
        label ch2_n_med_shared:
            n 2c "仔细一想的话，它让我想起了纱世里昨天的诗..."
            mc "诶？你这么觉得吗？"
            n 2j "是啊。我觉得既然你跟她做了那么久的朋友，那你们可能就是在同一个波段上。"
            n 2k "但是你不能像她那种类型那样来打动我。"
            mc "突然纱世里就有了种“类型”了...？"
            n 42c "好吧，我也不知道！但是老实说，一个人怎么可以这么...呃，无聊地...花那么长的时间和你待在一起？"
            n "就像是她在拖着一个累赘一样。"
            mc "呃...你这说得就没必要了..."
            mc "不过你再这样想想，如果不是我的话，她可能就像松手的气球一样飞走了。"
            mc "你可以说我们是用自己的方式彼此照顾。"
            n 2q "不管是什么，我都无法理解..."
            n "...哦，对了，我想是时候让你看我的诗了。"
            n "给你。"
            return


    elif n_poemappeal[0] == 0:
        n "...哼。"
        n 2k "好吧，它不比你上一首差。"
        n "但我也不能说它比上一首好。"
        mc "呼..."
        n 2c "嗯？你“呼”什么？"
        mc "啊...只要不是那么不堪，我都会当作是胜利。"
        mc "而且我觉得你大概是最挑剔的。"
        n 1p "嘿-嘿！是什么让你--"
        n 1q "{i}（等等，刚刚那句也许是表扬...？){/i}"
        n 4y "啊-啊哈！真高兴看到有人意识到了我的丰富阅历！"
        n "那么，只要你继续练习，也许有一天你也会像我一样好的！"
        mc "那...呃..."
        "我怀疑夏树完全误解了我的意思。"
        jump ch2_n_med_shared
    else:


        n "...哼。"
        n 2c "好吧，它还不算太糟。"
        n "不过在看过你的上一首诗之后，这首还是相当让人失望的。"
        n 2s "但话又说回来，如果这首诗跟你上一首一样好，那我会气疯的。"
        mc "好吧，我只是想这次尝试些稍微不同的东西。"
        n 2c "很合理。你还是新手，所以我也不会指望你一下子就找到自己的风格。"
        jump ch2_n_med_shared

label ch2_n_good:

    if n_poemappeal[0] != 1:
        n 1h "..."
        "夏树读着我的诗。"
        "她不断地看看我，然后又低头读诗。"
        "到目前为止，她肯定已经读了不止一次了。"
        n 1q "...你不应该不擅长写诗吗？"
        mc "...这是一种表扬吗？"
        n 1o "不-不！我是说...你知道的..."
        "夏树拼命想要找一个她需要的词语。"
        n 5w "我只是...在你昨天给我看那首诗后，期待值少了很多。"
        n "仅此而已。"
        mc "好吧，我只是这首诗运气比较好。"
        n 4t "是-是的！确实如此！"
        n "你只是运气好，知道吗？"
        n 4y "不要习以为常了。"
        n "你的诗不可能一直都可以写得这么可爱。我是说--！"
        n 1p "我是说写得好！不对，我是说--"
        mc "啊，原来是这样。我是诗很可爱吗？"
        n 1v "不是的！你干嘛笑啊？！我才不喜欢可爱的东西！"
        "夏树把我的诗塞回给我。"
        n 4w "哼-哼！又读了一次之后，我决定了，它一点也不好。"
        n "过于可爱和心跳了。"
        n 4t "它只可能给那些...喜欢这类东西的...那个，女孩子。"
        n "啊哈哈！"
        "不知为何，要看穿夏树真的非常容易。"
        n 1w "好了，不管怎么说...！"
        n 1h "你该读读我的诗了，不是吗？"
        n "根据你的口味判断，你应该会很喜欢它的。"
        n 2q "而且你可能也会学到点什么。别忘了谁才是 {i}真正{/i} 的专家。"
        return
    else:

        label ch2_n_good_sharedwithch3:
            n 1n "..."
            "夏树读着我的诗。"
            "她不断地看看我，然后又低头读诗。"
            "到目前为止，她肯定已经读了不止一次了。"
            n 1u "好吧..."
            mc "...？"
            mc "它有那么糟糕吗？"
            n 1r "不是！不是，完全不是！"
            n "它很棒。它真的很棒，好吗？！"
            n 5w "听到了吗，我就这么说了！"
            n "呃，但这不应该啊...！"
            n 5s "为什么你就不能不擅长于此呢？"
            n "应该是我的诗来打动 {i}你{/i}，而不是反过来像这样！"
            mc "你想要打动我？"
            n 12c "当然啊！你觉得我会让你更喜欢优里的诗吗？"
            n "我想静静。"
            mc "好吧..."
            mc "这么说的话，我试图打动你有什么问题吗？"
            n 1e "我告诉你！你--"
            n 1p "--"
            "夏树的表情凝固了，似乎刚刚才意识到了什么。"
            n "你-你-你..."
            n "你在试图...打动 {i}我？{/i}"
            show natsuki 1q
            "夏树又猛地扫了一遍我的诗。"
            "接着，诗从她手中滑落，然后飘到了地板上。"
            n 1p "我...要去趟厕所！"
            show natsuki at lhide
            hide natsuki
            "夏树红着脸，快速地走出了房间。"
            show monika 1d zorder 2 at t11
            m "嘿，[player]..."
            m "你是对夏树做了什么吗？"
            m "我刚刚看到她那样冲出去了..."
            m 2g "你没做什么可怕的事情吧？"
            mc "没-没有！"
            mc "我只是告诉她--"
            "我的话卡在了喉咙。"
            "我没办法告诉莫妮卡我想要打动夏树。"
            m 2d "嗯？"
            "莫妮卡看到了掉在地面上的诗，迅速地把它捡了起来。"
            if m_readpoem:
                "她又略读了第二遍，笑容还留在脸上。"
                m 2a "我明白了。"
                m "一开始我只是以为你喜欢她的写作风格..."
                m "但是这首诗你是 {i}写给{/i} 夏树的，对吧？"
            else:
                $ n_poemearly = True
                "她读了一遍，笑容还挂在脸上。"
                m 2a "我明白了。"
                m "这首诗你是写给夏树的，对吧？"
            mc "我-我是说..."
            mc "不完全是..."
            m 2d "实际上，那天她也不太喜欢你的诗吧？"
            m "我很惊讶你已经这么了解她的口味了。"
            m 4a "你确定你没在作弊吗，[player]？"
            mc "作弊...？"
            mc "你这是什么意思？"
            m 5a "别在意，我只是开个玩笑。啊哈哈！"
            "我一点也不能理解莫妮卡的玩笑。"
            m "无论如何..."
            m 1a "你觉得夏树对你感觉如何？"
            m "哦，你不需要回答。"
            m "这不过是你需要考虑的东西而已。"
            show monika zorder 2 at t22
            show natsuki 4e at l21
            n "嘿！"
            "夏树出现了，并且从莫妮卡手中抢过了诗。"
            "我们俩都没注意到她已经回到教室了。"
            show natsuki zorder 3 at f21
            n "你读了这首诗了吗，莫妮卡？"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1j "当然了！我很喜欢！"
            show monika 1a zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1r "呃..."
            n "你真的不该阅读这些不是写给你的东西，你知道的。"
            n "你有这样的坏习惯。"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1d "诶？"
            m "但是这首诗是 [player] 写的。"
    m 1a "而我们应该和所有人分享，不是吗？"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1x "呜--"
            "夏树语塞了。"
            "她显然忘记了，我的诗从严格意义上来说，是给所有人来读的。"
            n 42c "好吧，我想 [player] 已经和大家都分享过这首诗了。"
            n "反正也不会有人再想读这个。"
            n 4h "那么，这首诗就由我拿着了。"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 5 "如果你坚持的话～"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1i "怎么的？"
            n "你为什么那样看着我？"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m "那样是什么样？"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 12b "呃..."
            n "算了。"
            if s_readpoem and y_readpoem:
                "好吧，我想我的诗现在归夏树了。"
                "而不是我原想的那样，留在自己手里。"
            else:
                # variable that tells Natsuki who hasn't gotten to read the poem
                $ unfairto = "Sayori"
                $ unfairto_chs = "纱世里"
                # if Sayori already read it, change to Yuri
                if s_readpoem:
                    $ unfairto = "Yuri"
                    $ unfairto_chs = "优里"
                show natsuki zorder 2 at t21
                mc "啊，夏树..."
                mc "我会给你这首诗的，但是这样对[unfairto_chs]来说不是很公平..."
                mc "...她还没读过呢。"
                show natsuki zorder 3 at f21
                n 2q "那又如何？"
                show natsuki zorder 2 at t21
                show monika zorder 3 at f22
                m 2a "好啦...我觉得[player]说的没错，夏树..."
                m "如果你不让大家都读完的话，那就不公平了。"
                show monika zorder 2 at t22
                show natsuki zorder 3 at f21
                n "..."
                n 2h "...好吧。"
                "夏树把我的诗还给了我。"
                n "但是她应该不会喜欢这首诗。"
            show monika zorder 1 at thide
            show natsuki zorder 2 at t11
            hide monika
            n 2h "算了，现在来读我的诗吧。"
            n 4h "还有，我不会让你保管我的诗的。"
            n "这是我唯一的一份。"
            return

label ch3_n_bad:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        label ch3_n_bad12_shared:

            n 5x "谢谢，不用了。"
            mc "诶？你甚至都没有--"
            n 5w "{i}下一个！{/i}"
            $ skip_poem = True
            return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...搞咩啊。"
        n "我觉得你到头来，什么都没有学到。"
        n "老实说，我不知道自己为什么当初会抱有希望。"
        mc "什么？我不觉得这首诗有那么糟啊..."
        mc "我做错了什么吗？"
        jump ch2_n_bad_sharedwithch3
    else:

        n "..."
        n 2r "哦，天哪。"
        n "这真是一个大退步。"
        mc "诶？"
        n 2c "比起这首，我对你之前的两首要喜欢得多。"
        n 1k "我是说..."
        n "我觉得自己不该对你想要尝试不同东西而感到生气。"
        n 1c "只要你不是只想打动优里之类的。"
        n 5x "恶心。"
        mc "好吧，好吧。"
        mc "就像你说的，我可以尝试新的东西。"
        label ch3_n_shared:
            show natsuki 5g
            mc "话说回来，为什么你对我的诗投入那么多感情？"
            mc "难道不是对我的赞赏吗？"
            n 1o "...诶？"
            n 4x "不-不是！恶心！"
            n 4w "我不在乎！"
            n "只是在社团中的 {i}某个人{/i} 需要确保你没有松懈而已。"
            mc "真的吗？"
            mc "好吧，如果你最后把我吓跑了怎么办？"
            n 1t "那-唔..."
            n "...不像是你真的会去做的。"
            mc "是啊，你说得没错。"
            mc "在这里待着还是挺有趣的，即便我不得不需要忍受你。"
            show natsuki 1x
            mc "{i}呕--！！{/i}"
            "夏树的手肘打在了我的肚子上。"
            n 2y "哦？"
            n "或许我根本不担心会把你吓跑。"
            mc "我刚刚...只是开玩笑..."
            n 4z "哦，我知道！"
            n "别担心，我也是开玩笑。"
            n "啊哈哈哈！"
            show natsuki 4j
            mc "..."
            "你怎么能称它为玩笑？"
            "真的很痛啊。"
            "好吧，可能对她来说很有意思吧..."
            "...我猜这才是重点。"
            "在夏树边上时，我真的应该管住我的嘴。"
            n 2c "算了..."
            "夏树把她的诗递给我，就像什么都没发生一样。"
            return

label ch3_n_med:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    elif n_poemappeal[1] != 0:
        n "..."
        n 2k "...这首诗还行。"
        mc "还行？"
        n "嗯，是的。"
        n "它没有特别打动我。"
        n "但也没有我讨厌的地方。"
        n "它只不过不是我的风格罢了。我是说，还可以吧。"
        jump ch2_n_med_shared
    else:
        n "..."
        n 2k "...这首诗还行。"
        mc "还行？"
        n "嗯，是的。"
        n "差不多和昨天那首一样好。"
        n "我知道你想要什么，不过那不是我的风格。"
        n 2a "我的意思是，还可以吧。"
        n "我高兴的原因只是你有在努力。"
        mc "好吧，至少我肯定是努力了。"
        jump ch3_n_shared

label ch3_n_good:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared

    elif n_poemappeal[0] > 0 and n_poemappeal[1] > 0:
        n 1l "拭目以待，拭目以待！"
        mc "你今天看起来很热情啊。"
        n 2j "当然。"
        n "你知道我喜欢你的文字的。"
        mc "我只是有些惊讶。"
        mc "似乎之前你并不太愿意承认。"
        n 5w "好吧...好吧，没错！"
        n 5q "我只是要让你清醒点！"
        n "而不是..."
        n "我是说，不是因为我害羞或者是别的什么傻傻的原因。"
        n 5t "也不是嫉妒！"
        n "我真的没有嫉妒。"
        n "只是因为你恰好是一个好的作者？"
        n 4y "嫉妒这样的事情可太蠢了。"
        n "啊哈哈！"
        mc "夏树..."
        n 1h "什么？？"
        mc "你对自己的写作水平不是很自信，不是吗？"
        n 1n "...诶？"
        n "你-你在说什么？"
        n 1u "我的写作水平显然是最好的..."
        n "...对吧？"
        mc "..."
        "我花了一些时间才明白，不过我想我终于明白了。"
        "可能夏树行为如此夸张的原因是，她想要弥补自己的不安。"
        "如果她将自己表现得像是最好的，那么其他人没准也会这么觉得。"
        n 1m "对吧...？"
        n "[player]..."
        n "请你告诉我，你喜欢我的诗。"
        n 1u "我不在乎你是不是讨厌它们。"
        n "只要告诉我，我是最好的，就行了。"
        n "我只是..."
        n 1q "我只是真的很需要从某个人那里听到那句话。"
        n "我知道这听起来很蠢。"
        n "但是之前，我从来不跟别人分享诗是有原因的。"
        mc "夏树..."
        n "因为..."
        n 12c "因为没有人认真地看待过我！"
        n "如果大家笑着说“真可爱啊，就像你一样，夏树！”，那么分享我的诗还有什么意义呢。"
        n "有时候我不想要可爱！"
        n 12d "但是没人理解我！"
        n "我在写的时候真的很努力了。"
        n 12e "风格不是关键。"
        n "情绪在里面就行了。"
        n 1n "为什么没有人能 {i}看到{/i} 呢...？"
        n 1u "我只是想..."
        "夏树声音渐渐变小。"
        "可能是因为她的嘴唇开始颤抖了。"
        "我低头看了看。"
        "她的拳头紧紧地握了起来。"
        mc "嘿，夏树。"
        mc "如果你不小心点的话，可是会扯坏自己的诗的。"
        "我轻轻地用手抓住了她的诗，直到她松开了牢牢握住的手为止。"
        "我把诗平放在桌子上，抚平了她揉起的褶皱。"
        n 1h "别-别看！"
        "在我拿起诗之前，夏树把它从桌子上抢了过去。"
        n 5q "它一点也不好。"
        n "而且我也知道你讨厌我的诗。"
        n "所以你就不必读这首诗了，好吗？"
        mc "但是我想读。"
        n "为-为什么？"
        mc "因为。"
        mc "我喜欢你的诗。"
        mc "我真的喜欢。"
        show natsuki 5h
        mc "为什么我要评判你的风格呢？"
        mc "我的风格也没有什么出色的地方啊。"
        mc "我的意思是，虽然第一次读你的诗的时候，我确实不太喜欢它。"
        mc "但是我现在更了解你了。"
        mc "而优里认为你的风格比她的更业余这种想法，是错误的。"
        mc "还有纱世里...她的本意都很好..."
        mc "但是有时候她过于专注于简单的快乐，以至于她并不明白人们真正想要的是什么。"
        mc "是啊...我想我从来都没有考虑过你有多么艰难。"
        mc "如果我是问题的一部分的话，那我很抱歉。"
        mc "我现在理解了。"
        mc "你不仅仅是可爱而已，你还有很多其它的特点。"
        show natsuki 12d
        mc "啊--夏树，你又这样了--"
        "夏树又一次地有些用力地抓着她的诗。"
        "她低着头，不让我看到她的眼睛。"
        "我之前从未意识到，这对她有多么地艰难。"
        "不过最终，她还是强迫自己伸出了手，把她的诗放到了桌子上。"
        n 12e "你可以...读它了。"
        n "朝着那边看。"
        n "我不想让你...现在看我的脸。"
        mc "好的，我会的。"
        return


    elif n_poemappeal[0] > 0 or n_poemappeal[1] > 0:
        jump ch2_n_good_sharedwithch3
    else:

        n "..."
        n 2k "...终于！"
        mc "诶？"
        n 2l "这首诗。它很棒！"
        n "我刚刚在想你花了多少时间写它。"
        mc "好吧！"
        n 4y "嗯，认真点。"
        n "不要听其他任何人说的话。"
        n "尤其是优里。"
        n 4a "只要继续像这样写诗就行了。你要做的就是这些！"
        mc "呃..."
        mc "你确定这不是只有 {i}你{/i} 想要的吗？"
        n 2h "你说什么？"
        n "你是在跟专业人士对话，你知道的。"
        n "你不觉得你应该最信任我的观点吗？"
        mc "我觉得得分情况。"
        mc "你不是偏爱这种那些简单而又可爱的诗吗？"
        n 2w "偏爱？"
        n "当然没有啊。"
        n 4y "我的意见正好是最好的。"
        mc "..."
        "我还有一件事不是很明白。"
        "夏树到底有没有自我意识到她那被惯坏的行为？"
        "这样下去的话，我都不知道自己能不能搞清楚这点。"
        mc "...算你说得对吧。"
        mc "无论如何，我很高兴你喜欢我的诗。"
        n 4z "啊哈哈！"
        n 4j "我知道你最终会理解的。"
        n "只要继续给我看你的诗，你就会在不知不觉中变成专业的啦。"
        n "好了，这是我写的。"
        return

label ch1_s_bad:
    s 1b "..."
    s "...哇！"
    s "[player]..."
    s 4r "你的诗真的好烂啊！"
    s "啊哈哈哈！"
    mc "诶？！"
    s 4a "没关系，没关系～"
    s "这是你的第一次嘛。"
    s "至少..."
    label ch1_s_shared:
       s 1a "我真的很高兴你会写一首诗。"
        s "这提醒了我，你现在真的是文学部的一员了～"
        "(更何况我现在人就在部室里，正站在你的面前...？)"
        mc "呃...对，当然了。"
        mc "我现在还不熟练，不过这并不意味着我会违背我的承诺。"
        s 1d "对吧？"
        s "[player]，就像我之前说的那样..."
        s "在内心深处，你一点也不自私，对不？"
        s "像这样为了别人而尝试新的事物..."
        s 2q "只有非常好的人才会这么做哦！"
        mc "谢谢你...纱世里。"
        "...我不确定纱世里是不是完全明白我的动机是什么。"
        "况且..."
        "我也无法否认她是我加入社团的原因之一。"
        "我心里清楚知道，这对她意味着什么..."
        s 1x "嗯。"
        s "我保证你在这能玩得很开心的，好吗？"
        s "这就是我感谢你的方式～"
        mc "好啊，那你可要说话算数哦。"
        s 4r "耶～！"
        s "现在，轮到你读我的诗了，是吧？"
        s 1y "别担心，我真的不擅长写诗。"
        s "诶嘿嘿..."
        mc "我们拭目以待吧。"
        return

label ch1_s_med:
    s "..."
    s 2x "这真是一首好诗啊，[player]！"
    s "你确定你是第一次写吗？"
    mc "当然..."
    mc "它没那么好。"
    mc "我看起来像是那种会在闲暇时间写诗的人吗？"
    s 2q "诶嘿嘿，我觉得你说得没错～"
    s 1q "不过这也是为什么它给我留下了深刻印象！"
    s 1d "好吧，老实说..."
    s "我之前担心你不会认真写..."
    s "甚至你连写都不会写。"
    jump ch1_s_shared

label ch1_s_good:
    s 1n "..."
    s "...我的天哪！"
    s 4b "[player]，你写得太太太太太——好了！"
    mc "诶？"
    s 4r "我很喜欢～！"
    s "我以前都不知道你是这么出色的诗人！"
    mc "纱世里..."
    mc "你显然是有些反应过度了。"
    mc "我根本不是一个好诗人。"
    mc "实际上，我压根都不知道自己在干什么。"
    s 1x "好吧..."
    s "可能这就是原因！"
    s "因为我也不知道我喜欢什么！"
    s 1r "啊哈哈哈！"
    mc "真是的..."
    if y_readpoem:
        "优里的观点比这有建设性多了..."
    else:
        "我相信优里的观点肯定比你这稍微要有建设性一点 。"
    if not n_readpoem:
        "就连夏树的点评可能都比你的强呢。"
    mc "你确定你不是因为这是我写的才喜欢它吗？"
    s 1b "诶？"
    s "这个嘛，确实有一部分是这个原因。"
    s 1x "我觉得我比其他人更了解你哦~"
    s "所以你的诗在我读来..."
    s "不仅仅是一首诗..."
    s 4q "还是 [player] 写的诗！"
    s "这就让它倍显特殊了！"
    s "比如说，我可以感受到你在诗中的情感～"
    "纱世里把那张纸抱在了胸前。"
    mc "你真古怪，纱世里..."
    s "诶嘿嘿..."
    jump ch1_s_shared


label ch2_s_bad:
    s "..."
    s 1q "诶嘿嘿，我喜欢读你的诗～"
    s "就像是我永远都不会知道会读到什么！"
    mc "所以你其实就是在说它很烂。"
    s 4c "不！完全不是！"
    s 4l "...可能！"
    s 5a "只有一点点？"
    s "肯定是优里的诗有些把我养刁了..."
    s "诶嘿嘿。"
    mc "没关系，没关系。"
    mc "毕竟我还不知道你喜欢什么样的文章。"
    label ch2_s_shared:
        s 1q "嗯！"
        s "我也不知道！"
        mc "呃..."
        mc "为什么你不试着想一想呢？"
        s 2d "啊，你是想为我写点什么吗？"
        s "真贴心啊～"
        mc "嗯，是的。"
        mc "但是你总是在考虑别人。"
        mc "你应该时不时地想一想自己。"
        mc "不然的话，你最终可能会在某个时候受伤的。"
        s 1n "诶？"
        s "好吧..."
        s 1o "我不是很清楚你的意思，但是我会尽量记住的！"
        mc "好吧，随你了..."
        s 1b "那，让我想想..."
        s "唔..."
        s 4q "我猜我喜欢...开心的诗～"
        s 4i "等等，有时候我也喜欢悲伤的诗..."
        s 1i "有时候喜欢两者都有一点..."
        s "有个词是形容这个的，对吧...？"
        s "是哪个词来着..."
        s 4r "...苦乐参半！"
        s "没错！"
        s 1x "我喜欢开心的事情，也喜欢悲伤的事情。"
        mc "开心的和悲伤的？"
        mc "我不觉得你喜欢悲伤的事情，纱世里..."
        s 1c "好吧..."
        s "那我最喜欢开心的事情！"
        s 1d "不过有的时候，当你在心中有一小片乌云时..."
        s "一首悲伤的诗能给这片乌云一个小小的拥抱..."
        s 4q "...然后它就会变成一道漂亮的开心的彩虹！"
        mc "...纱世里，这段话出于意料地有诗意啊。"
        s 4n "诶？是吗？"
        s "可能我越来越善于表达自己的感受了！"
        s 2q "谢谢你，[player]！"
        s "那我现在就去把那段话写下来～"
        s 2a "你现在可以读我的诗了，好吗？"
        return

label ch2_s_med:

    if s_poemappeal[0] < 0:
        s "..."
        s 4x "哦！"
        s "我喜欢这首诗，[player]！"
        s "诗里有非常好的感情～"
        mc "啊，我很高兴。"
        mc "所以它至少比昨天的要好。"
        s 1q "嗯-嗯！"
        mc "那这么说，我正在渐入佳境。"
        label ch2_s_med_shared:
        s 1a "嗯，我不是很擅长于辨别诗的好坏..."
        s "不过这也是为什么我会用心去感受～"
        s "如果它能触动我的话，那它肯定是一首好诗！"
        "我不确定是不是就是这样..."
        "...话说回来，我觉得传递感情也是整体中相当重要的一部分。"
        mc "是吧，大概..."
        mc "老实说，我甚至都不知道你喜欢什么样的文章。"
            jump ch2_s_shared

    elif s_poemappeal[0] == 0:
        s "..."
        s 4x "哦！"
        s "我喜欢这首诗，[player]！"
        s "诗里有非常好的感情～"
        mc "啊，我很高兴。"
        mc "意思就是说，它比昨天的更好咯？"
        s 4b "唔，让我想想..."
        s 1q "我不知道！"
        s "我觉得两首我都喜欢！"
        s "诶嘿嘿～"
        mc "这话可不太有用，你知道的..."
        jump ch2_s_med_shared
    else:

        s "..."
        s 4x "哦！"
        s "我喜欢这首诗，[player]！"
        s "诗里有非常好的感情～"
        mc "啊，我很高兴。"
        mc "不过..."
        mc "从你的语气来看，你似乎更喜欢昨天的诗。"
        s 2l "诶嘿嘿，被你发现了..."
        s "对我来说，你有时候太了解我了点！"
        mc "嗯，不要只想着友好。"
        mc "如果我做得不好的话，那么我更愿意能听到意见。"
        s 1c "不，不是的！"
        s "我还是喜欢这首诗的！我保证！"
        s 1h "你知道我不会对你撒谎的，[player]...！"
        s "永远不会！"
        mc "嗯，我也觉得是这样..."
        mc "那么，是什么让昨天那首诗比今天的要好呢？"
        s 1b "唔..."
        jump ch2_s_med_shared

label ch2_s_good:

    if s_poemappeal[0] < 1:
        s 1n "..."
        s "...哦天哪！"
        s 4r "这首诗太～好了，[player]！"
        mc "诶？"
        s "我很喜欢～！"
        s "尤其是在看过昨天的诗之后！"
        mc "呃..."
        mc "有时候你太诚实了，纱世里。"
        s 4x "没有，是真的！"
        s 1x "我想把它贴到墙上～"
        s "可以吗？"
        mc "纱世里..."
        mc "你显然是有些反应过度了。"
        mc "我根本不是一个好作者。"
        mc "实际上我都不知道我在干什么。"
        s 1l "好吧..."
        s "可能这就是原因！"
        s "因为我也不知道我喜欢什么！"
        s 4r "啊哈哈哈！"
        mc "天哪..."
        "我敢说优里的观点肯定比这有建设性一些。"
        "它甚至还不如夏树的观点。"
        mc "你确定你不是因为这是我写的才喜欢它吗？"
        s 4b "诶？"
        s 1b "好吧，确实有一部分是这个原因。"
        s "我觉得我比其他人更了解你，不是吗？"
        s "所以在我读你的诗的时候..."
        s "它不仅仅是一首诗..."
        s 4q "它还是[player]的诗！"
        s "这就有了额外的特殊感！"
        s "比如说，我可以感受到你在诗中的情感～"
        "纱世里把那张纸抱在了胸前。"
        mc "你真古怪，纱世里..."
        s 4l "诶嘿嘿..."
        jump ch2_s_med_shared
    else:

        s "..."
        s 1d "[player]..."
        s "我真的超爱你的诗。"
        s "我都不敢相信你居然把它们藏起来了！"
        mc "诶？我没有藏什么啊！"
        s 1b "但是..."
        s "你的诗这～么好..."
        s "昨天的是，今天的也是！"
        s "别告诉我你以前没写过！"
        mc "我是说..."
        mc "你真的是唯一一个这么觉得的人，所以..."
        s 4h "诶？！"
        s "不可能！！"
        s "连夏树也不觉得吗...？"
        mc "嗯，我觉得夏树是最不可能承认她有多喜欢某样东西的..."
        mc "不过这次应该不是那样。"
        s 1b "什么意思？"
        mc "好吧..."
        mc "那我就老实说吧。"
        mc "当我想着你的时候，写诗就会变得容易很多。"
        s 4m "诶-诶？！"
        s "哇哇哇--！"
        mc "别想奇奇怪怪的东西啦，小笨蛋！"
        mc "我只是说你真的是一个...善于表达感情的人，我觉得。"
        mc "我怎么可能会写关于自己这种愚蠢人生的诗？"
        mc "但是你让你的人生中的一切都像是冒险一样。"
        mc "即便是很小的事情。"
        s 4o "比如说料理！！"
        mc "我们还是别提那个了！"
        s 5a "诶嘿嘿..."
        mc "所以，是的..."
        mc "我想我要说的就是，比起从我自己身上，我更能从你身上感受到更多情感。"
        mc "我们有那么一种奇怪的联系。"
        mc "老是掺和到我的事情来是你的错。"
        s 1e "诶...？"
        s "我不知道我是不是理解了..."
        mc "唉..."
        mc "每次我想要跟你解释什么的时候，你从来都没有理解过，不是吗，纱世里？"
        "我拍了拍纱世里的头。"
        s 4s "啊哈哈！喂！"
        s "我不是个小孩子，你知道的！"
        mc "你确定吗？"
        s 4l "唔，大概～"
        "纱世里开始在双手间摆弄着她的铅笔。"
        s "嘿，[player]..."
        s 2d "你会把你的诗给我吗？"
        s "我想要留着它。"
        mc "嗯？为什么？"
        s 1y "因为..."
        s "那个..."
        s "这是你第一次给我写了些东西..."
        s "诶嘿嘿..."
        mc "！！"
        mc "纱世里，你完全误解了！"
        mc "我不是写给你的！"
        s 5b "诶嘿嘿嘿嘿..."
        mc "唉..."
        mc "你还在听我说话吗？"
        mc "好吧，算了。"
        mc "我会在回家路上给你的。"
        show sayori at h11
        s 4m "真的吗？！"
        "{i}咔嚓！{/i}"
        s 4p "啊-啊！！"
        s "我弄断了我的铅笔..."
        "纱世里急忙弯下腰去捡掉落在地上的那一段。"
        "但是由于没有注意周围，她正好撞到了我身上。"
        s 4l "对-对-对不起--！！"
        mc "没关系，没关系。"
        mc "我替你捡吧。"
        "我弯下腰捡起了折断的铅笔。"
        "纱世里抓着身边的桌子来支撑自己，膝盖颤抖着。"
        s 5b "我-我今天有点笨拙..."
        s "啊哈哈哈..."
        mc "我们坐下吧，纱世里..."
        s 4y "好-好的..."
        "我抓住纱世里的手臂，帮她坐到了桌子上。"
        mc "话说回来，我还没有读你的诗..."
        s 4b "哦！"
        s "抱歉，我刚刚忘了～"
        s 1h "不过它没你的那么好！！"
        mc "天哪，你别担心。"
        mc "我敢肯定我会喜欢的。"
        return

label ch3_s_bad:
    $ currentname = "Yuri"
    $ currentname_chs = "优里"
    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"
        $ currentname_chs = "夏树"
    s "..."
    s 1k "...唔。"
    s "我觉得它还不错～"
    mc "拜托，我看出来你不喜欢它了。"
    s 1d "好吧..."
    s "你不用为我的看法担心。"
    s 2y "毕竟，你是写给另一个人的，不是吗？"
    s "大概是[currentname_chs]吧..."
    mc "诶？？"
    mc "我没有特意为了某个人写啊！"
    s "也许吧..."
    s 1d "不过，这也不是我的本意。"
    s "没关系的。"
    s "你在交新的朋友，就像我希望的那样。"
    s 1q "这就让我...非常开心了。"
    s "而且你也开心，对吧？"
    s 1a "在这个社团里？"
    mc "好吧..."
    mc "我当然开心了。"
    s 4q "很好～"
    s "这对我来说就是最重要的。"
    s 1d "谢谢你，[player]。"
    mc "纱世里..."
    mc "是不是出了什么事？"
    s 1b "嗯？"
    s 1k "没，没事。"
    s "我只是今天有点累而已。"
    s 1l "诶嘿嘿。"
    mc "好吧..."
    mc "如果你有需要的话，告诉我就行。"
    s 1a "我会的。"
    s "不要为我担心，好吗？"
    s "你可以去找别人玩了。"
    mc "如果你坚持的话..."
    s 4q "耶～"
    s 4a "我今天要稍微早点回家。"
    mc "纱世里...？"
    s 1q "请你告诉莫妮卡，我不太舒服，好吗？"
    s "明天见～"
    "我还没来得及说什么，纱世里已经哼着歌，开心地走出了教室。"
    $ skip_poem = True
    return


label ch3_s_med:
    jump ch3_s_bad

label ch3_s_good:
    if poemwinner[0] != "sayori" and poemwinner[1] != "sayori":
        jump ch3_s_bad
    s 1d "..."
    s "这是你到现在为止最好的一首。"
    s "它真的真的很棒，[player]～"
    mc "呃--谢谢。"
    s 1q "嗯哼～"
    mc "..."
    mc "纱世里，你今天有些安静。"
    mc "一切都还好吗？"
    s 4m "诶-诶？？"
    s "当然！"
    s 4l "一切都好～"
    s "我可能只是今天有些累而已。"
    s 1l "诶嘿嘿。"
    mc "你想要小睡一会儿嘛？"
    s 1h "不要，那太傻了！"
    s "不要为我担心，好吗？"
    s 1q "我只想看到你脸上的笑容～"
    mc "嗯，好吧..."
    s 1b "嘿，[player]..."
    s "我还是有些惊讶。"
    s "我真的还以为你会试着像优里那样写诗..."
    s 1y "或者甚至是夏树的..."
    s "但是最终..."
    mc "...是啊。"
    mc "我想你应该是最喜欢这首诗的人。"
    stop music fadeout 1.0
    s 1k "...为什么？"
    s "你不想和其他人更亲近一些吗？"
    play music t9
    mc "等等！"
    mc "我当然想啊！"
    mc "但是这并不意味着我需要那么努力去给她们留下深刻印象啊。"
    mc "我最了解的还是你，纱世里。"
    mc "我知道你有时候不得不迁就我。"
    mc "而我有时候也不得不迁就你。"
    mc "但是我们有着...同一个波段。"
    mc "而这就是我如何写下这首诗的。"
    mc "有时候的感觉就像是，你是我生命中唯一一个能让我激动的事物。"
    mc "所以在想你的时候，写起来会更容易。"
    mc "...纱世里？"
    s 4v "不-不..."
    s "[player]..."
    s "我...配不上这些..."
    s "你对我太好了..."
    s "为什么你要这么做...？"
    "纱世里突然之间无法保持声音的平稳。"
    s "如果你去和别人好好相处...！"
    s "这就会...容易很多！"
    mc "纱世里...！"
    "我环顾了一下房间，确保没人注意到这里。"
    mc "纱世里。"
    mc "我可能从来没说过这句话，不过，现在的我无法理解你的感受。"
    mc "告诉我什么能让你开心起来。"
    "纱世里摇摇头。"
    "她抽泣着，继续摇着头。"
    "终于，她收拾好了心情，给了我一个微笑。"
    s 1y "没事的，[player]。"
    s "只是一小片乌云而已。"
    s 4r "抱歉让你看到了。啊哈哈哈！"
    s "我保证再也不会发生了。"
    s 1a "大家都笑着，好吗？"
    s "这是最重要的。"
    s "去和其他人玩吧。"
    s "我今天要稍微早点回家～"
    mc "纱世里--"
    s 2q "请你告诉莫妮卡，我不太舒服，好吗？"
    s "明天见～"
    "我还没来得及说什么，纱世里已经哼着歌，开心地走出了教室。"
    $ skip_poem = True
    return

label ch1_y_bad:
    y 1g "..."
    y "唔..."
    y "..."
    "优里盯着那首诗。"
    "一分钟过去了，要读完诗已经绰绰有余了。"
    mc "唔..."
    y "哦！"
    y 3n "抱-抱歉...！"
    y "我忘了说话了..."
    y "唔-唔！"
    mc "没关系，别强迫自己。"
    y 2v "我没有..."
    y "我只是需要一点时间来酝酿下我的语言。"
    y "稍微等我一下..."
    y "...好了。"
    y 1f "这是你第一次写诗，对吗？"
    mc "呃，是啊..."
    mc "你为什么要这么问？"
    y "我只是确认一下。"
    y "在读完这首诗之后，我就猜到应该是了。"
    mc "啊，也就是说我写的这首诗很烂啊。"
    y 2p "不是的！！"
    y 2o "...我刚刚是不是大声了点...？"
    y 4c "呜，抱歉..."
    "优里把脸埋进了手里。"
    "我不禁注意到，已经好几分钟过去了，而我们一点进展都没有。"
    "优里可能需要一些时间来适应新人..."
    mc "没事啦，我都没注意到。"
    mc "你刚刚说了什么来着？"
    y 2u "好吧...唔..."
    label ch1_y_shared:
        y 1a "你的诗里能看到一般新手诗人特有的写作习惯。"
        y "我也是从新手过来的，所以对于这些习惯都有些熟悉。"
        y 1i "我觉得，新手诗人身上最容易察觉的一点就是，他们会把自己的风格表现得非常刻意。"
        y "换句话说，他们倾向于挑选一个脱离主题的写作风格，然后再将两者杂糅起来。"
        y 1a "结果就是风格和表现力都大为削弱。"
        "一旦优里找到了思路，她的举止就仿佛完全变了个样。"
        "她的磕磕巴巴完全消失了，说起话来就像是专家一样。"
        y 1k "当然，这也无可厚非。"
        y "即便是写一首简单的诗，也有大量不同的技巧和手法供你选用。"
        y 1a "你要做的不仅仅是找到并构建它们，还要让它们相互配合，这可能才是最有挑战性的部分。"
        y "这可能会需要你花上一些时间，不过这一切都要从实践、举一反三以及尝试新事物中得来。"
        y "我也希望，社团里的其他人都能给你宝贵的反馈意见。"
        y 1l "不过夏树可能会有些偏见..."
        mc "偏见？怎么会？"
        y 2j "唔-唔..."
        y "这个嘛..."
        y "算了..."
        y "我不应该那样谈论别人的..."
        y "抱歉..."
        mc "没关系。"
        "我不知道优里在对着谁道歉，是她自己、我、还是夏树。"
        mc "介意我现在读你的诗吗？"
        y 3c "请吧！"
        y "我很乐意分享创作这首诗的心路历程..."
        "优里如梦如醉地笑着，仿佛对她来说这是一个千载难逢得的机会。"
        "这本身倒有点好笑..."
        "...毕竟，这里不就是文学部吗？"
        return

label ch1_y_med:
    jump ch1_y_bad

label ch1_y_good:
    y 1e "..."
    "随着优里读着诗，我注意到她的眼睛亮了起来。"
    y 2f "...超乎卓越。"
    mc "诶？什么意思？"
    y "...？"
    y 2n "我-我刚刚大声说出来了吗...？"
    "优里先是掩住了嘴，但随后掩住了整张脸。"
    y 4c "我...！"
    y "呜..."
    y "{i}（他会讨厌我的...）{/i}"
    mc "唔..."
    mc "你没做错什么啊，优里..."
    y 4a "诶...？"
    y "那..."
    y 2q "我-我想你说得对..."
    y "我在紧张什么？"
    y "啊-啊哈哈..."
    show yuri 2l at t11
    "优里做了个深呼吸。"
    y "那么..."
    y 1a "你有过什么样的写作经验？"
    y "你在意象和隐喻上的运用表明，你之前写过很多诗。"
    mc "真的...？"
    mc "哇，那可是一个了不得的称赞。"
    mc "其实这是我第一次写诗，真的。"
    y 1e "嗯...？"
    "优里茫然地盯着我，然后又看了一遍我的诗。"
    y "..."
    y 2h "...好吧，其实我知道的！"
    y "我只是说...唔-唔..."
    "优里的声音小了下去，无法找到一个借口。"
    "她指读着诗里的文字，似乎想要更透彻地分解它。"
    y 2l "...嗯。"
    y "好了。"
    y "我找到原因了。"
    jump ch1_y_shared


label ch2_y_bad:

    if y_poemappeal[0] < 0:
        y "..."
        y 2h "唔..."
        y "...你还在生我气吗？"
        mc "诶？！"
        y "我昨天没有尊重夏树..."
        y "因为读这首诗..."
        y "我现在知道你为什么会对我生气了。"
        y "因为你..."
        y 3v "比起我的诗，你更喜欢她的！"
        mc "并不是那样的...！"
        y "这就意味着，当我不尊重她时..."
        y "我也在不尊重你...不是吗？"
        y 4c "哦不..."
        mc "优里..."
        mc "你有些过度解读了..."
        y "我怎么会这么笨...？"
        y "我总是让这样的事情发生..."
        y "每当我在说话前思考时，我都会表现得尴尬而又不讨喜。"
        y "但是如果我不假思索地说话，那么我想保留在心里的话又会说出来，让大家讨厌我。"
        y 2v "所以...请不要勉强你自己待在我身边。"
        y "我知道这是莫妮卡希望的。"
        y "但是你本可以在这些时间跟夏树和纱世里在一起，这对你不公平。"
        mc "优里--"
        y 4b "拜托了..."
        y "不要表现出担心，这样我会好受一些。"
        y "另外..."
        y "我还有书陪着我。"
        y 3u "有它...就够了。"
        mc "..."
        "优里悲伤地笑了，低头靠在了桌子上。"
        "我很沮丧。"
        "我不讨厌她，但是她似乎并不听我的，而是有着自己的想法。"
        "我叹了口气。"
        "我能做的，就只有接受这样的她。"
        "如果她想要独自一人，那么我也别无选择，只能遵循她的请求。"
        $ skip_poem = True
        return
    else:

        y 2a "啊，轮到我了吗？"
        y "我们来看看，它跟昨天的相比如何..."
        y "唔..."
        y "明白了..."
        y "它有了一些差别。"
        y 1a "我尊重你能尝试不同的东西，[player]。"
        y "你是被夏树的诗启发的吗？"
        y "又或者是纱世里的诗？"
        mc "好吧..."
        mc "我觉得你可以这么说..."
        y "我也这么想的。"
        y 2u "我为你感到高兴。"
        y "你不需要从我的诗里寻找灵感。"
        y "我是写给自己的..."
        y 4b "...而不是写给别人。"
        y "所以我并不...需要别人来喜欢它们。"
        mc "优里！"
        y 3t "诶-诶？"
        mc "抱歉我要直说了，你有点想多了。"
        mc "仅仅因为我们的风格不同，并不意味着我不喜欢你的诗..."
        mc "事实上，如果我尝试用你的风格来写的话，我很可能会写得很烂。"
        y 4a "我...我明白了..."
        y "抱歉..."
        y "我那愚蠢的大脑...它有时候会喜欢这么想。"
        y "不管怎么样..."
        label ch2_y_shared:
            y 2h "你尽可以大胆一些..."
            y "隐喻其实大有可为。"
            y "你不要觉得自己需要像转动齿轮那样开动大脑。"
            y 1m "可以试着让你的思维在情绪中自由游荡..."
            y "然后写下你看到和听到的东西。"
            y "这种方法能让你的读者真正地了解你的思想。"
            y 2u "也是一种非常私人化的活动..."
            mc "我明白了。"
            mc "嗯，很非常有趣的技术。"
            mc "谢谢你的分享。"
            y 2v "我有，呃..."
            y "...嗯，有一个这样的例子，如果你愿意读的话..."
            mc "当然愿意。"
            mc "是你为今天写的诗吗？"
            "优里点了点头，羞怯地把诗递给了我。"
            return

label ch2_y_med:

    if y_poemappeal[0] <= 0:
        y 1a "我们来看看你为今天写了些什么。"
        y "..."
        y "唔..."
        y 1c "写得很好，[player]。"
        y "你的技巧已经开始进步了。"
        mc "真的吗？"
        mc "谢谢你，优里。"
        mc "这句话由你说出来，有很大的意义。"
        y 3f "诶？"
        y 3v "没-没什么！"
        y "我只是乐于帮助启发作者同伴而已..."
        y "我知道你是新手，所以就算你无法让诗变得完美，你也不用太担心。"
        jump ch2_y_shared
    else:


        y 1a "我们来看看你为今天写了些什么。"
        y "..."
        y "唔..."
        y "相当不错，[player]。"
        y "在昨天看过大家的写作风格后，你因此受到影响了吗？"
        mc "我觉得你可以这么说..."
        y 1m "我也对大家的写作方式如此不同而有些惊讶。"
        y "所以我尊重你尝试新的东西。"
        jump ch2_y_shared

label ch2_y_good:

    if y_poemappeal[0] < 1:
        y 1a "我们来看看你为今天写了些什么。"
        y "..."
        y 2e "......"
        "优里面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y "...你是怎么做到这么快上手的？"
        label ch2_y_good_shared:
            y 2v "就在昨天，我还在告诉你那些值得练习的技术..."
            mc "可能原因就是这个..."
            mc "你解释得很棒。"
            mc "我也很想试着加入更多的意象。"
            show yuri 4b zorder 2 at t11
            "优里明显地吞咽了下口水。"
            "甚至她的双手也出汗了。"
            y "我不是...很习惯..."
            mc "习惯什么？"
            y 3o "我不知道...！"
            mc "没关系，慢慢来..."
            show yuri 3l at t11
            "优里做着深呼吸，整理着她的想法。"
            "我知道优里喜欢在说话前思考，所以我也给了她足够的耐心。"
            y 4a "好了..."
            y "就是...像这样被表扬...我猜。"
            y "可能听起来很傻..."
            y "但是看到有人被我的文字所激励..."
            y "这让我觉得..."
            y "真的很开心..."
            mc "你是在说，你以前从来没有分享过你的诗？"
            "优里点了点头。"
            mc "真的吗？不敢置信。"
            y "我真的只写给自己..."
            y "除此之外..."
            y 3w "...大家只会嘲笑我！"
            mc "你真的是那么想的...？"
            "优里再次点了点头。"
            mc "唔..."
            mc "即便是你的好朋友？"
            y 2v "..."
            "优里没有回应。"
            "我很疑惑是为什么..."
            mc "话说回来..."
            mc "你想跟我分享一下你今天的诗吗？"
            y "...是的。"
            y 3t "我想！"
            y "如果是分享给你的话..."
            return
    else:

        y 1a "我们来看看你为今天写了些什么。"
        y "..."
        y 2e "......"
        "优里面带惊讶地盯着那首诗。"
        mc "你...喜欢它吗？"
        y "[player]..."
        y "这首比昨天的还要好..."
        y "...你是怎么做到这么快上手的？"
        jump ch2_y_good_shared

label ch3_y_bad:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:
            y 4b "..."
            "优里似乎并不是特别想跟我待在一起..."
            "我觉得如果她改变主意的话，她会来找我的。"
            "而现在，我应该先离开她。"
            $ skip_poem = True
            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        y 1i "..."
        y "...我明白了。"
        y "我觉得你在写作方面有了整体的进步，[player]。"
        y 2i "但是我忍不住觉得自己有点傻。"
        mc "诶？为什么？"
        y "只是..."
        y "我觉得我不停地想要给你建议..."
        y "但实际情况是，你明显更喜欢另一种写作风格。"
        y 3w "我可能看上去有点自负了！"
        y "我真傻..."
        mc "优里，你这样有点--"
        y 4b "不..."
        y "你不明白。"
        y "我花了这么多时间患得患失。"
        y "不仅仅是和你在一起的时候..."
        y "还有和夏树、纱世里在一起的时候..."
        y "现在很明显了，为什么没人觉得跟我说话有意思..."
        y "而正因如此..."
        y 4c "...我以后会对你的诗三缄其口的！"
        mc "..."
        "优里把头埋到了桌上的手臂里。"
        "这并不是我第一次看到她这么做。"
        mc "我并不觉得这件事有你想的那么糟糕..."
        y "..."
        mc "我觉得，如果大家真的不喜欢跟你说话..."
        mc "那么就会明显很多。"
        mc "我知道你喜欢深入地解读事物。"
        mc "但有些东西只要看到表面就足够了。"
        y 4b "我只是..."
        y "我已经如此习惯于此..."
        y "...以至于很难让我理解其它的可能性。"
        mc "习惯于什么？"
        mc "深入地解读事物？"
        y "习惯于被讨厌。"
        mc "优里..."
        y 2v "我...我在说什么？"
        y "抱歉..."
        y "我从来没想过要提到这个..."
        "优里转过身。"
        y 4b "你该走了..."
        mc "诶...？"
        y "拜托了..."
        y "拜托你现在不要看着我。"
        y "我想要进行一些思考..."
        mc "你确定吗...？"
        "优里点点头。"
        mc "好吧..."
        "我不再打扰优里。"
        "想要安慰或是宽慰她几乎是不可能的。"
        "所以当她想要一个人待着的时候，我觉得不管我说什么，都只会让事情变得更糟。"
        "我感到很难过，但是好在她没有怪我..."
        "还是等到她感觉好点的时候再说吧。"
        $ skip_poem = True
        return
    else:
        y 1a "..."
        y "...啊。"
        y "你是决定了今天尝试不同的东西吗？"
        mc "我想是的。"
        mc "这样好吗，还是说不好？"
        y 2g "嗯，两者都不是。"
        y "我有自己的偏好。"
        y "如果让我基于此来判断某样东西好不好，那么这其实并不是很公平。"
        label ch3_y_shared:
            y 1f "而且我一直坚信，最重要的就是要自己探索和发现。"
            mc "那我就放心了。"
            mc "我有些害怕会让你失望。"
            y 2t "诶...？"
            y "为什么是我...？"
            mc "嗯，你一直在写作上非常老练，而且可以分享最多的建议。"
            y 4a "是这样吗...？"
            y "..."
            "优里想了好一会儿。"
            y 4c "...那肯定很可怕。"
            mc "诶？"
            y "我成为一个观点让人害怕的人..."
            y "我有多么不讨人喜欢啊..."
            mc "优里..."
            mc "它没有你想象中的那么糟。"
            mc "我只是想说，我尊重你的观点。"
            y 2v "我明白了..."
            y "抱歉，我经常想得太多，然后得出那样的结论..."
            y "我只是...有点太习惯于此了。"
            mc "习惯于想得太多？"
            y "习惯于被讨厌。"
            mc "优里..."
            y 3w "我...我在说什么？"
            y "抱歉，我不是有意提起来的..."
            y "我们继续吧..."
            mc "好吧..."
            mc "你想要现在分享你的诗吗？"
            y 2i "好的..."
            y "给你。"
            return


label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "..."
        y 1a "写得很好，[player]。"
        y "这几天以来，你的写作水平显然提高了。"
        y "我的建议对你有用吗？"
        mc "是的...当然有用。"
        y 2m "我很高兴..."
        y "能这样分享我们的诗..."
        y 2a "它比我预料中的要有趣和有意义地多。"
        y "我要记得谢谢莫妮卡..."
        y "我觉得在刚开始时，我们都有些尴尬。"
        y 1a "但现在似乎大家都很享受分享自己的诗，以及看看别人是怎么想的。"
        mc "我完全同意。"
        mc "我之前还害怕它会变成例行公事..."
        "这对我来说也不错，可以让我和社团里的女生一起共度一些私人时光。"
        mc "不过能逐渐了解大家、以及各自的诗，也真的很有意思。"
        mc "而且我自己还能进行写作..."
        y 2a "嗯..."
        y "你对自己有了什么了解吗，[player]？"
        mc "诶？"
        y 2i "是这样的，你知道我很喜欢说，写作是用于了解自己的一种非常私人的体验..."
        y 1a "最终，最关键的并不是你是一个好的作者，还是一个坏的作者。"
        y "而即便是我的观点，也仅仅是观点而已...你明白吗？"
        jump ch3_y_shared
    else:
        y 1e "..."
        y "...啊。"
        y "你是决定了今天尝试不同的东西吗？"
        mc "我想是的。"
        mc "这样好吗，还是说不好？"
        y 2i "嗯，两者都不是。"
        y "我有自己的偏好。"
        y "如果让我基于此来判断某样东西好不好，那么这其实并不是很公平。"
        jump ch3_y_shared

label ch3_y_good:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    if y_poemappeal[1] < 1:
        y "..."
        y 2u "[player]..."
        y "...这首诗太精彩了。"
        y "我可以感受到你倾注到里面的感情。"
        y "这是尝试了我昨天建议的结果吗？"
        mc "是的，我想是这样的..."
        mc "你解释得很棒。"
        mc "我也很想试着加入更多的感情。"
        show yuri 4b zorder 2 at t11
        "优里明显地吞咽了下口水。"
        "甚至她的双手也出汗了。"
        play music t9 fadeout 1.0
        y "我不是...很习惯..."
        mc "习惯什么？"
        y 3o "我不知道...！"
        mc "没关系，慢慢来..."
        "优里做着深呼吸，整理着她的想法。"
        "我知道优里喜欢在说话前思考，所以我也给了她足够的耐心。"
        y 4a "好了..."
        y "就是...像这样被表扬...我猜。"
        y "可能听起来很傻..."
        y "但是看到有人被我的文字所激励..."
        y "这让我觉得..."
        y "真的很开心..."
        mc "你是在说，你以前从来没有分享过你的诗？"
        "优里点了点头。"
        mc "真的吗？不敢置信。"
        y "我真的只写给自己..."
        y "除此之外..."
        y 3w "...大家只会嘲笑我！"
        mc "你真的是那么想的...？"
        "优里再次点了点头。"
        mc "唔..."
        mc "即便是你的好朋友？"
        y 2v "..."
        "不知为何，优里没有回应。"
        mc "优里...？"
        label ch3_y_good_shared:
            if not renpy.music.get_playing(channel='music') == audio.t9:
                play music t9 fadeout 1.0
            "优里悲伤地笑了。"
            y 1u "[player]，在午饭时间，我都是一个人吃的。"
            y "你知道吗？"
            y "在这段时间里，你找个安静的地方做些阅读。"
            y "实际上..."
            y 2s "我总会随身带着几本书。"
            y "你可以说我真的很喜欢阅读..."
            y "...好吧，反正这也是一种表达方式..."
            y "但是..."
            y "书里充满了令人惊喜和激发灵感的人。"
            y "你希望能够爱上的人。"
            y "抑或是你知道可以成为非常好的朋友的人。"
            y 1m "开心的人，他们总能让你的脸上带上笑容..."
            y "又或是深邃的思考者、问题的解决者，发现了生命的秘密。"
            y "所以从这个角度来看..."
            y "我每天都被朋友包围着..."
            y "...你明白吗？"
            y 2s "而且这些朋友并不会嘲笑我..."
            y "他们不会因为我整天发呆而捉弄我..."
            y "他们不会嘲笑我的体型..."
            y "还有..."
            y 3v "...还有他们也不会因为我表现得像是个自以为是的人而讨厌我！"
            mc "大家...是这么说你的吗？"
            y "我不是个自以为是的人，[player]!"
            y "恰恰相反，我什么都不知道！"
            y 4b "我不知道如何跟大家交谈。"
            y "我不知道如何让大家像平常人那样看待我。"
            y "我甚至都不知道如何让自己快乐！"
            y "我有这么多的情感..."
            y "而我能做的只有读和写..."
            y "但是直到现在..."
            y 2s "在我开始与你分享之后..."
            y "...我终于明白自己一直以来缺少的是什么了。"
            mc "但是我真的没做什么..."
            y "不是的..."
            y "你错了。"
            y "耐心和尊重..."
            y 3u "对我来说真的...很重要。"
            y "我知道我是一个难相处的人，[player]..."
            y "我说话速度太慢..."
            y "我总是自我怀疑..."
            y "我过分解读事物..."
            y "但是每一次..."
            y "你总是会像对待别人那样对待我。"
            y "跟别人交谈还能感到自在，这样的情况真的是太少见了..."
            y "而这也是为什么每次我跟你聊天..."
            y 2s "...我都会感到非常开心。"
            mc "我明白了..."
            mc "嗯，我只是以应有的方式对待你，优里。"
            mc "如果别人不是这么看的话，那你只需要无视他们。"
            mc "我的意思是，我加入社团是希望能够交到朋友。"
            mc "而现在我可以说，我至少成功交到了一个。"
            mc "你不也是吗？"
            y 4b "唔-唔..."
            y "既然你这样说..."
            y "...是的..."
            y 4e "我们现在是朋友了，不是吗？"
            "优里用手捂住了脸。"
            "但这次。她是笑着这么做的。"
            mc "你想给我看看你的诗吗？"
            y 3s "是的。"
            y "我想！"
            y "我去给你拿..."
        return
    else:
        y "..."
        y "[player]。"
        y 2s "你的诗在过去短短几天内就有了进步。"
        y "你给我看的每首诗都称得上文采斐然。"
        y "我真的可以感受到里面的情绪..."
        y 2m "我甚至都有点嫉妒了..."
        y "我都不觉得这种事情能自然而然地发生在我身上。"
        mc "优里，你这样想是错误的。"
        mc "它也没有自然而然地发生在我身上。"
        mc "我能有这么大的进步，都要归功于你。"
        mc "你是我追逐的榜样。"
        y 3u "是-是这样吗...？"
        "优里轻轻地微笑起来。"
        y "这种感觉..."
        y "我真的很高兴...能有机会分享我的诗。"
        y 4e "我从来没想过它的感觉是这样的。"
        mc "我记得你昨天提到过这点。"
        mc "我都不敢相信，你这么擅长写作，却从来没有和任何人分享过。"
        mc "真是可惜了。"
        y 2u "可能吧，但是..."
        y "我似乎并没有...什么机会。"
        mc "什么意思...？"
        y "嗯..."
        jump ch3_y_good_shared

# Monika is a bit different in this department
# As mentioned she uses _m_start to begin

label ch1_m_start:
    m 1b "嗨，[player]！"
    m "到目前为止，你在文学部过得开心吗？"
    mc "啊...还好。"
    m 1k "好！很高兴听到你这么说！"
    m 4a "顺便，由于你是新来的..."
    m "如果你对社团有什么建议，比如说新的活动，或是可以改进的地方..."
    m 4b "可以随时跟我说哦。"
    m "有事别怕提出来，好吗？"
    show monika 4a
    mc "好的...我会记住的。"
    "我不怕提出问题就怪了。"
    "在没有完全融入之前，我最好还是随波逐流吧。"
    m 1a "话说回来..."
    m "你想跟我分享一下你的诗吗？"
    mc "虽然有些尴尬，不过我想也只能这么做了。"
    m 5a "啊哈哈哈！"
    m "别担心，[player]！"
    m "我们今天都会有一点尴尬的嘛。"
    m "但我们很快就都能学会该如何克服它。"
    mc "是的，说得没错。"
    "我把我的诗递给了莫妮卡。"

    m 2a "...唔！"
    # determines the next scene by who won the poemgame and their appeal number
    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    # this plays after Monika voices on the tone of your poem to which specific doki
    mc "我相信，我最终会尝试很多不同东西的。"
    mc "可能要花上一段时间后，我才能适应写作。"
    m 1k "没关系！"
    m 1b "我很乐意看到你尝试新东西。"
    m "这个方法最能帮你找到适合自己的风格。"
    m 3e "其他人都偏爱与她们自己相近的风格..."
    m 3a "不过我会帮你找到最适合你的那种！"
    m "所以，不要强迫自己使用别人希望的方式来写作。"
    m "反正你并不需要担心能否打动她们之类的。"
    m 5 "啊哈哈！"
    mc "啊哈哈..."
    m 1a "话说回来，你想现在读一读我的诗吗？"
    m 1e "别担心，我的水平不是很好..."
    mc "你自称水平不是很好，但你的语气听起来还是自信满满的啊。"
    m 1j "好吧...是因为我的语气必须自信满满啦。"
    m 1b "这并不意味着我心里真的总是自信满满，明白吗？"
    show monika 1a
    mc "这样啊..."
    mc "好了，那我们来读你的吧。"
    return

label ch2_m_start:
    m 1b "嗨，又见面了，[player]！"
    # If Nat shared her poem and ran, Monika already read it and plays a special script
    if n_poemearly:
        $ n_poemearly = False
        m "刚才夏树是不是有点点傻里傻气的？"
        m 1j "我很欣喜，你们现在能玩得那么好。"
        mc "..."
        "这也是一种说法吧..."
        m 2a "总之，我也看过你的诗了，不过你现在可以来看看我的。"
        m 1a "我喜欢这个作品的效果，所以我希望你也喜欢~"
        return
    else:
        m "写得怎么样？"
        mc "还行吧，我觉得..."
        m 2k "我来看看。"
        m 2b "只要它不太差！"
        m 2a "我都为你的努力而开心。"
        m "也许你很快就会想出一篇杰作的！"
        mc "啊哈哈，我就不指望了..."
        m 2a "谁知道呢！"
        m "想跟我分享一下你为今天写的东西吗？"
        mc "当然...给。"
        "我把我的诗给了莫妮卡。"
        m "..."
        m "...没问题！"
        $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))
        call expression nextscene

        m 1a "不过话说回来..."
        m "你想现在读读我的诗吗？"
        m "我还挺喜欢这首诗的表现方式的，所以希望你也喜欢～"
        mc "好的，那我们来看看吧。"
        return

label ch3_m_start:
    m 2a "嗨，[player]～"
    m "你有考虑过自己想给学园祭的表演提交什么吗？"
    mc "嗯..."
    "在这个社团里是一回事，而在一堆人面前表演..."
    mc "...我要再想想。"
    m 2b "好的，不要有压力！"
    m "不管你做什么，我敢肯定最后的结果都会很棒的。"
    m "我也会很高兴看到。"
    m 2k "啊哈哈！"
    # If Nat shared her poem and ran, Monika already read it and plays a special script for chapter 3
    if n_poemearly:
        $ n_poemearly = False
        m 1a "总之，我也看过你的诗了，不过你现在可以来看看我的。"
        return
    else:
        m 1a "话说回来，我们来看看今天的诗吧！"
        mc "当然..."
        "我让莫妮卡拿走了我手中的诗。"
        m "..."
        $ nextscene = "m_" + poemwinner[2] + "_" + str(eval(poemwinner[2][0] + "_appeal"))
        call expression nextscene

        m 1a "话说回来...！"
        m "我现在把我的诗也分享给你，好吗？"
        mc "呃..."
        mc "好吧..."
        return

# All of Monika's responses to the poem per Doki and appeal level

label m_natsuki_1:
    m 2b "我喜欢这首诗，[player]！"
    mc "真的吗...？"
    m 2e "它比我想象中的要可爱多了。"
    m 2k "啊哈哈哈！"
    mc "哦天哪...."
    m 1b "不是，不是！"
    m "它只是有点让我想起了夏树写的东西。"
    m "而她也是个好的作者。"
    m 5a "所以你就当它是表扬吧！"
    mc "啊哈哈..."
    mc "既然你都这么说了。"
    m "是的！"
    m 1a "或许，你是不是读过谢尔·希尔弗斯坦写的什么东西？"
    mc "诶？"
    mc "可能在很久之前..."
    m "他以用寥寥数语讲述各种故事而闻名。"
    m "他的诗可以是好笑的、可爱的、甚至是悲伤的..."
    m 3d "而有时候它们只有几行的长度。"
    m "有些甚至感觉起来像是给孩子们写的，但是如果你去想一想它们..."
    m "它们表达的世界观适用于任何人。"
    mc "我明白了..."
    mc "所以你是在说夏树有点像那样？"
    m 2a "可以这么说。"
    m "可能她并不是专家..."
    m "但是你在她的诗里不太能找到太多的辞藻。"
    m "它们写起来可能很容易，但是要传递内涵就非常有挑战性了。"
    m 2b "所以我能理解为什么你会去探索这诗！"
    return

label m_sayori_1:
    m 2a "我喜欢这首诗！"
    m "这让我感觉像是纱世里会喜欢的东西。"
    mc "是吗？"
    m 2d "你和纱世里是非常要好的朋友，对吧？"
    m "你们有这样的共同点，我也不会感到惊讶的。"
    mc "啊，那个..."
    mc "我们是好朋友，但是纱世里和我其实还是大不相同的。"
    m "唔..."
    m "好吧，也许你说得没错。"
    m 3a "不过可能你们也有一些意想不到的相似之处。"
    m "她谈到你的方式..."
    m "听起来就像是你们两个都很在乎彼此的幸福。"
    m "即便你们是用不同的方式展现出来的，但最终比你想象中的要更相似。"
    m 1a "所以我在阅读你的诗的时候，就有这样的既视感。"
    mc "唔..."
    mc "你确定你没有过分解读吗？"
    m 5 "啊哈哈！也有可能！"
    m "天哪，我听起来就跟优里一样..."
    m 2a "...不过，无论如何，纱世里的诗里有一种轻柔的感觉。"
    m "我知道她喜欢带着情绪去探索，比如快乐和悲伤。"
    m "谁知道这么开心的一个人，也会喜欢悲伤的事情呢？"
    mc "是啊...完全出乎意料。"
    m 2j "好了，每个人都有选择喜好的权利～"
    m 2a "你也不用害怕进行一些小小的尝试。"
    return

label m_yuri_1:
    m 1a "写得很好，[player]！"
    m "我读它的时候，脑子里都是“哦”这样的声音。"
    m 1j "真的非常有隐喻性！"
    m 1a "不知道为什么，不过我没有想到你会这么深入。"
    m 3b "我想我之前低估你了！"
    mc "大家最容易对我保持一个较低的期待值。"
    mc "这样一来，一旦我努力了，它就会变得很明显。"
    m 5a "啊哈哈！这可不太公平啊！"
    m "好吧，不管怎么说，我觉得它还是起效了。"
    m 2a "你知道优里喜欢这种文字的，对吧？"
    m "那种充满意象和隐喻的文字。"
    m 2d "而不是像纱世里那样，喜欢使用简单直接的语言来描绘快乐和悲伤..."
    m "优里喜欢能让读者从中提取出自己的意义。"
    m 4d "要高效地写出那样的诗还是很有挑战性的。"
    m "能同时让人们通过感受来从中获取..."
    m "以及能深入地分析每个微妙变化。"
    m "它可能需要好几年的练习，而我觉得优里已经做到了这一点。"
    m 1e "不过我从来没有问过她..."
    mc "我敢肯定，我远远比不上她的层次。"
    m 2b "不要太担心！"
    m "你只需要做你自己的事情。"
    m "只要你继续探索，通过尝试新东西来不断学习！"
    return

label m_natsuki_2:
    m 1j "这首诗相当不错～"
    m 1a "你和夏树已经待过一段时间了，对吧？"
    m "你肯定是喜欢她的写作风格。"
    mc "啊，是的..."
    mc "我觉得这是一种讲述故事的好方法。"
    m 2a "唔。我不否认。"
    m "夏树的诗可能有些可爱，但是它们也是富有深意的。"
    m "我能理解为什么你喜欢这种风格。"
    m "那么，我觉得，这就意味着你并不是非常喜欢优里的诗？"
    mc "啊--我可不会这样说..."
    mc "我喜欢所有人的诗。"
    m 2d "这也没错，但是我敢肯定你更喜欢其中的一种，对吧？"
    m "比如说优里使用复杂的词语和象征手法..."
    m "或是纱世里用更直接的方式表现快乐和悲伤的手法。"
    m 2a "你肯定有偏好吧，不是吗？"
    m 4l "啊，并不是说要分个高下！"
    m 4a "我只是有些好奇，仅此而已。"
    return

label m_sayori_2:
    m 1j "这首诗相当不错啊～"
    m 1a "它让我想起了纱世里，就像你写的另一首一样。"
    m 4b "你们俩就像是动态的二人组！"
    mc "啊哈哈...这么说有些夸张了。"
    m 2a "好吧，大概是吧。"
    m "但是即便在社团里，你也花了很多时间和她在一起，不是吗？"
    m 2j "况且，我也不会责怪你的害羞～"
    mc "我-我不是害羞，只是..."
    m 5 "啊哈哈！我只是捉弄你一下。"
    m "我知道和大家做朋友需要一点时间。"
    m 2d "但是优里和夏树都是超有趣的人，所以别怕给她们应得的时间哦！"
    m "而且你也可以时不时地跟我聊聊..."
    m 1e "我不是那种，比如说，不易亲近的人，对吧？"
    mc "啊，不是，当然不是..."
    mc "我只是还在适应待在这里，仅此而已。"
    m 1a "好吧..."
    m 1l "如果我给你压力了，那我很抱歉！"
    m "我其实真的不是那个意思。"
    mc "不，不用担心。"
    mc "我已经明白你在说什么了。"
    m 1a "嗯，那就好～"
    return

label m_yuri_2:
    m 2b "这首诗不错啊！"
    m "它感觉起来像是，你不仅仅对自己的风格更得心应手了..."
    m "而且意象也比我上次读到的那首要好！"
    m 2a "我只是有些疑惑，你是不是从优里的写作风格那里找到了灵感？"
    mc "唔..."
    mc "我觉得是的。"
    mc "你无法否认她的天赋。"
    m 4k "是的，完全没错！"
    m 4a "我觉得她的诗是最..."
    m "...浪漫的。"
    m 1a "这是形容她的诗的最好方法。"
    m 1d "当她拿起笔时，她就像是完全变了个人一样。"
    mc "我也注意到了这一点。"
    mc "或者在她谈论到文学时，她就像是打开了内心的灯一样。"
    m 2a "嗯！"
    m "伤心的是，很难和她进行太多的私人对话..."
    m 2m "相信我，我已经尝试过了..."
    m "谁知道她心里想的是什么？"
    mc "我希望你不是那种不好的意思。"
    m 1g "不，当然不是！"
    m "我只是说，我希望她不要那么封闭..."
    m 1e "不过，你那样地维护她..."
    m 5 "你肯定相当地喜欢她..."
    mc "诶？！"
    mc "你...完全误会了！"
    m "啊哈哈！冷静，我只是开个玩笑！"
    m 2a "除此以外，我也很确定她已经有男朋友了..."
    mc "等等，真的吗？"
    m 2k "是啊。不过是个虚拟的人物。"
    "莫妮卡悄悄地对我说了最后一句。"
    m 5 "这只是一种直觉，不过..."
    mc "...好吧，其实也没有什么问题！"
    m 1n "哦，其实我知道...！"
    m "我只是说说而已～"
    return

label m_natsuki_3:
    m 2j "又一次坚持了夏树的风格，我明白了～"
    m 2d "唔..."
    m "你真的很喜欢夏树，不是吗？"
    mc "诶？这--"
    m 5 "哦，拜托，[player]。"
    m "已经相当可疑了，你知道吗？"
    m "每天在部室和她待在一起..."
    m "假装喜欢她热衷的漫画..."
    mc "你-你知道夏树是怎么样的...！"
    mc "如果我不迁就她，那她最后会讨厌我的。"
    m 2e "诶？"
    m 2a "不，我觉得你误解了，[player]。"
    m "就算有人不能迁就夏树，她也不是那种会因此而讨厌他们的人。"
    m 2d "没错，她确实很强硬，但她并没有那么自私..."
    m "实际上，我觉得你是唯一一个尽可能迁就她的人。"
    mc "是这样吗..."
    "我其实是知道的，但是我就是不想承认。"
    m "所以，我需要问你一件事..."
    m 1e "...小心回答。好吗？"
    m "夏树有些不可预料。"
    m "很多时候，她甚至都不知道她想要什么。"
    m 1i "毕竟她是这里年纪最小的一个。"
    m "她可能并不知道如何正确地控制自己的情绪。"
    m "我要说的是..."
    m 1m "如果发生了什么不好的事情，那么它最终也会伤害到社团..."
    m 5 "而你也不会这么对我的...对吧？"
    mc "这--"
    "我不知道该如何回应莫妮卡。"
    "虽然我很关心她和社团，但是要说出口似乎也不太合理。"
    m "好吧...你很聪明。"
    m "我相信你会做正确的事情。"
    "莫妮卡甜甜地微笑着。"
    return

label m_sayori_3:
    m 1k "啊哈哈。"
    m "很好玩..."
    mc "为什么呢？"
    m 1a "不，不是指诗..."
    m 2a "我的意思是说，每天看着你和纱世里的诗变得越来越像，这件事很好玩。"
    m "我对你和她能如此同步而感到惊讶。"
    m 2d "况且，你们最近也花了很多时间在一起，不是吗？"
    mc "啊，我想你可以这么说..."
    mc "虽然我们是作为最好的朋友长大的，但在过去的一年里，我并没有经常见到她。"
    mc "但自从加入社团后，我们又有很多时间在一起了。"
    m 1a "我明白了，我明白了～"
    m "这让我想起了..."
    m "纱世里今天为何会有些不在状态..."
    mc "是吗？她跟你说了什么？"
    m 1n "啊..."
    m "好吧..."
    m 2l "[player]，你没有跟她在调情吧，对吗？"
    mc "当-当然没有！"
    mc "我只是像平常那样对待她。"
    m 2a "好吧。"
    m 5 "我只是确认一下～"
    m "我知道你有多在乎她..."
    m "如果她身上发生了什么不好的事，那就太糟了，所以你要留心一下她。"
    m 2d "自从你加入社团以来，纱世里一直都表现得快乐了很多。"
    m "突然之间能发生什么呢...？"
    mc "..."
    m 1l "...好吧，别在意。"
    m "现在确实不是谈论这个的时候..."
    return

label m_yuri_3:
    m 2e "你的风格变得好精炼啊，[player]。"
    m "优里教了你很多东西吧，不是吗？"
    mc "嗯--"
    mc "我觉得是这样的。"
    m 2a "是啊...我一直都有注意到你和她花了多少时间。"
    m 2d "我想，在过去的几天里，我听到她说的话比过去一年都要多。"
    m "不知道你是怎么做到的，不过真是让人印象深刻..."
    mc "嗯，我觉得她只是需要些耐心，还有就是需要一种方法来谈论她内心的一切..."
    mc "我自己也还在掌握窍门之中。"
    m 2a "唔..."
    m "你无疑花费了很多的努力。"
    m 2e "看来你肯定真的很喜欢她。"
    mc "诶？这--"
    m 5 "啊哈哈！"
    m "这已经相当可疑了，你知道吗？"
    m "每天在部室和她待在一起..."
    m "和她一起读前卫小说..."
    mc "好吧--！"
    mc "我只是...为她的社交困难感到难过。"
    mc "这让我想要确保她并不会一直一个人待着。"
    mc "除此以外，小说也不是太差，你知道的..."
    m 1k "好啦，好啦～"
    m "我明白你的意思啦。"
    m 1a "只是...小心点，好吗？"
    m "我知道优里不习惯敞开心扉..."
    m 2d "所以如果在她脆弱的时候发生了什么不好的事情..."
    m "那么对她来说会变得很艰难的。"
    m 2i "她的书并不是完全逃离了现实。"
    m "它们只是绷带而已。"
    mc "你说的就像是我要伤害她一样..."
    m 1l "抱歉，我不是那个意思～"
    m "如果发生了什么，她可能会不小心伤到自己。"
    return
