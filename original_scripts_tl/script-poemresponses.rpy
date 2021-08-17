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
        n 2c "嗯？'呼'什么？"
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
        s "Your poems are sooo good..."
        s "Yesterday's, and this one too!"
        s "You can't tell me you haven't done this before!"
        mc "I mean..."
        mc "You're really the only one who feels that way, so..."
        s 4h "Eh?!"
        s "No way!!"
        s "Not even Natsuki...?"
        mc "Well, I guess Natsuki is the least likely to admit how much she likes something..."
        mc "But I don't think it's that."
        s 1b "What do you mean?"
        mc "Well..."
        mc "I guess I'll be honest about it."
        mc "It's a lot easier to write poems when I'm thinking about you."
        s 4m "E-Eh?!"
        s "Wawawa--!"
        mc "Stop thinking weird things, idiot!"
        mc "I just mean that you're a really...expressive person, I guess."
        mc "How am I supposed to write poems about my own stupid life?"
        mc "But you somehow make everything in your life an adventure."
        mc "Even the little things."
        s 4o "Like cooking!!"
        mc "Let's not talk about that!"
        s 5a "Ehehe..."
        mc "So, yeah..."
        mc "I guess what I'm saying is that I can feel more feelings through you than I can through myself."
        mc "We have that kind of weird connection."
        mc "It's your fault for getting in my business all the time."
        s 1e "Ehh...?"
        s "I don't know if I understand..."
        mc "Sigh..."
        mc "You never understand when I try to explain things to you, do you, Sayori?"
        "I pat Sayori's head."
        s 4s "Ahaha! Heyyy!"
        s "I'm not a kid, you know!"
        mc "Are you sure about that?"
        s 4l "Mmmm, maybe~"
        "Sayori starts fiddling with her pencil between her hands."
        s "Hey, [player]..."
        s 2d "Will you give me your poem?"
        s "I kinda want to keep it."
        mc "Huh? Why?"
        s 1y "Because..."
        s "Well..."
        s "It's the first time you've written something for me..."
        s "Ehehe..."
        mc "!!"
        mc "Sayori, you completely misunderstood!"
        mc "I didn't write this for you!"
        s 5b "Ehehehehe..."
        mc "Sigh..."
        mc "Are you even listening anymore?"
        mc "Well, whatever."
        mc "I'll give it to you when we go home."
        show sayori at h11
        s 4m "Really?!"
        "{i}Snap!{/i}"
        s 4p "A-Ah!!"
        s "I broke my pencil..."
        "Sayori hastily bends down to pick up the piece she dropped."
        "But being inattentive of her surroundings, she bumps right into me."
        s 4l "S-S-Sorry--!!"
        mc "It's fine, it's fine."
        mc "I'll get it for you."
        "I bend down and pick up the broken pencil."
        "Sayori clutches the desk beside her to support herself, knees shaking."
        s 5b "I-I'm a little clumsy today..."
        s "Ahahaha..."
        mc "Let's sit down, Sayori..."
        s 4y "Y-Yeah..."
        "I grab Sayori's arm and help her sit at the desk."
        mc "Anyway, I still haven't read your poem..."
        s 4b "Oh!"
        s "Sorry, I forgot about that~"
        s 1h "But it's not as good as yours!!"
        mc "Jeez, don't worry."
        mc "I'm sure I'll like it."
        return

label ch3_s_bad:
    $ currentname = "Yuri"
    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"
    s "..."
    s 1k "...Hm."
    s "It's nice, I guess~"
    mc "Come on, I can already tell you don't like it."
    s 1d "Well..."
    s "You don't need to worry about what I think."
    s 2y "After all, you wrote this for someone else, didn't you?"
    s "Probably [currentname]..."
    mc "Eh??"
    mc "I didn't write this for anyone specifically!"
    s "Maybe..."
    s 1d "That's not really what I meant, though."
    s "But it's okay."
    s "You're making new friends, just like I was hoping."
    s 1q "That makes me...really happy."
    s "And you're happy too, right?"
    s 1a "In this club?"
    mc "Well..."
    mc "Of course I am."
    s 4q "Good~"
    s "That's all that matters to me."
    s 1d "Thank you, [player]."
    mc "Sayori..."
    mc "Is there something wrong?"
    s 1b "Huh?"
    s 1k "No, nothing."
    s "I'm just a little tired today."
    s 1l "Ehehe."
    mc "Alright..."
    mc "Just tell me if you need anything."
    s 1a "I will."
    s "Don't worry about me, okay?"
    s "You can go play with everyone else now."
    mc "If you insist..."
    s 4q "Yaay~"
    s 4a "I'm gonna go home a little bit early today."
    mc "Sayori...?"
    s 1q "Tell Monika I wasn't feeling well, okay?"
    s "I'll see you tomorrow~"
    "Before I can say anything else, Sayori cheerfully walks out of the classroom, humming to herself."
    $ skip_poem = True
    return


label ch3_s_med:
    jump ch3_s_bad

label ch3_s_good:
    if poemwinner[0] != "sayori" and poemwinner[1] != "sayori":
        jump ch3_s_bad
    s 1d "..."
    s "This is your best one so far."
    s "It's really really nice, [player]~"
    mc "Er-- Thanks."
    s 1q "Mhm~"
    mc "..."
    mc "Sayori, you've been a little quiet today."
    mc "Is everything alright?"
    s 4m "E-Eh??"
    s "Of course!"
    s 4l "Everything is fine~"
    s "Maybe I'm just a little tired today."
    s 1l "Ehehe."
    mc "Do you want to nap or something?"
    s 1h "No, that's silly!"
    s "Don't worry about me, okay?"
    s 1q "I only want to see smiles on your face~"
    mc "Well, alright..."
    s 1b "Hey, [player]..."
    s "I'm still a little surprised."
    s "I really thought that you would try writing your poems like the way Yuri does..."
    s 1y "Or even Natsuki..."
    s "But in the end..."
    mc "...Yeah."
    mc "I guess you're the one who likes this one the most."
    stop music fadeout 1.0
    s 1k "...Why?"
    s "You don't want to get closer with everyone else?"
    play music t9
    mc "Wait!"
    mc "Of course I do!"
    mc "But that doesn't mean I need to try so hard to impress them."
    mc "I still understand you the most, Sayori."
    mc "I know you have to sometimes put up with me."
    mc "And I have to sometimes put up with you."
    mc "But we have...a wavelength or something."
    mc "And this is how the poem came out."
    mc "Sometimes it feels like you're the only exciting thing in my life."
    mc "So sometimes it's just easier to write when thinking about you."
    mc "...Sayori?"
    s 4v "N-No..."
    s "[player]..."
    s "I don't...deserve this..."
    s "You're too nice to me..."
    s "Why are you doing this...?"
    "Sayori has trouble keeping her voice steady, all of a sudden."
    s "If you had fun with everyone else instead..."
    s "This would be...so much easier!"
    mc "Sayori...!"
    "I glance around the room to make sure nobody has noticed this."
    mc "Sayori."
    mc "I've probably never said this before, but I don't understand what you're feeling right now."
    mc "Tell me what will cheer you up."
    "Sayori shakes her head."
    "She sniffles and keeps shaking her head."
    "Finally, she gathers herself and puts on a smile."
    s 1y "It's nothing, [player]."
    s "It's just a little raincloud."
    s 4r "I'm sorry you had to see that. Ahahaha!"
    s "I promise it won't happen again."
    s 1a "Just smiles from everyone, okay?"
    s "That's all that matters."
    s "Go play with everyone else."
    s "I'm gonna go home a little bit early today~"
    mc "Sayori--"
    s 2q "Tell Monika I wasn't feeling well, okay?"
    s "I'll see you tomorrow~"
    "Before I can say anything else, Sayori cheerfully walks out of the classroom, humming to herself."
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
    "As Yuri reads the poem, I notice her eyes lighten."
    y 2f "...Exceptional."
    mc "Eh? What was that?"
    y "...?"
    y 2n "D-Did I say that out loud...?"
    "Yuri first covers her mouth, but then ends up covering her whole face."
    y 4c "I...!"
    y "Uu..."
    y "{i}(He's going to hate me...){/i}"
    mc "Um..."
    mc "You really didn't do anything wrong, Yuri..."
    y 4a "Eh...?"
    y "That's..."
    y 2q "I-I guess you're right..."
    y "What am I getting so nervous for?"
    y "A-Ahaha..."
    show yuri 2l at t11
    "Yuri takes a breath."
    y "So..."
    y 1a "What kind of writing experience do you have?"
    y "Your use of imagery and metaphors indicates you've written a lot of poetry before."
    mc "Really...?"
    mc "Wow, that's a huge compliment coming from you."
    mc "This is actually my first time, really."
    y 1e "Huh...?"
    "Yuri stares at me blankly, then looks at my poem again."
    y "..."
    y 2h "...Well, I know that!"
    y "I just meant...u-um..."
    "Yuri trails off, unable to find an excuse."
    "She traces her finger along the words in the poem, as if breaking it down more thoroughly."
    y 2l "...Yeah."
    y "Okay."
    y "This is the reason I was able to tell."
    jump ch1_y_shared


label ch2_y_bad:

    if y_poemappeal[0] < 0:
        y "..."
        y 2h "Um..."
        y "...Are you still mad at me?"
        mc "Eh?!"
        y "For disrespecting Natsuki yesterday..."
        y "Because reading this poem..."
        y "Now I know why you got mad at me."
        y "Because you..."
        y 3v "You prefer her writing over mine!"
        mc "That's not really true...!"
        y "Meaning when I disrespected her..."
        y "I disrespected you too...didn't I?"
        y 4c "Oh no..."
        mc "Yuri..."
        mc "You might be reading into this a little too much..."
        y "How could I be so stupid...?"
        y "I always let these things happen..."
        y "Whenever I think before I speak, I just come off as awkward and unlikable."
        y "But if I speak without thinking, the things I want to keep inside come out and make people hate me."
        y 2v "So...please don't force yourself to be around me."
        y "I know this is what Monika wants."
        y "But it's not fair to you when you could be enjoying your time with Natsuki and Sayori."
        mc "Yuri--"
        y 4b "Please..."
        y "It makes it easier for me if you don't express any concern."
        y "Besides..."
        y "I have my books with me."
        y 3u "That's...all I need."
        mc "..."
        "Yuri smiles sadly and puts her head down on her desk."
        "I'm frustrated."
        "I don't hate her, but it's as if she's not capable of listening to me over her own thoughts."
        "I sigh to myself."
        "All I can do is accept that that's how she is."
        "If she wants to be left alone, then I have no choice but to abide to that request."
        $ skip_poem = True
        return
    else:

        y 2a "Ah, is it my turn?"
        y "Let's see how it compares to yesterday's..."
        y "Mm..."
        y "I see..."
        y "It's a bit different."
        y 1a "I respect you for trying different things, [player]."
        y "Were you inspired by Natsuki's poem?"
        y "Or Sayori's, perhaps?"
        mc "Well..."
        mc "I guess you could say that..."
        y "I thought so."
        y 2u "I'm happy for you."
        y "You don't need to find inspiration in my poems."
        y "I write them for myself..."
        y 4b "...Not for anyone else."
        y "So I don't really...need for people to like them or anything."
        mc "Yuri!"
        y 3t "E-Eh?"
        mc "I'm sorry for being blunt, but you're overthinking this a little."
        mc "Just because our styles are different doesn't mean I dislike your poems..."
        mc "In fact, if I tried to do something in your style, I would probably just do a terrible job."
        y 4a "I...I see..."
        y "I'm sorry..."
        y "My stupid mind...it likes to do that sometimes."
        y "Anyway..."
        label ch2_y_shared:
            y 2h "You don't need to be afraid to be a little more daring..."
            y "Metaphors can go a long way."
            y "Don't feel like you need to work your brain like turning a bunch of gears."
            y 1m "Try letting your mind wander through your feelings..."
            y "And write down the things you see and hear."
            y "That's one way to truly enable your reader to see into your mind."
            y 2u "It's a very intimate exercise..."
            mc "I see."
            mc "That's a certainly interesting technique."
            mc "Thanks for sharing."
            y 2v "I have, um..."
            y "...Well, an example of that, if you'd like to read it..."
            mc "Of course."
            mc "Is this the poem you wrote for today?"
            "Yuri nods, and timidly hands me her poem."
            return

label ch2_y_med:

    if y_poemappeal[0] <= 0:
        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y 1c "Well done, [player]."
        y "Your skills are already improving."
        mc "Really?"
        mc "Thanks, Yuri."
        mc "Coming from you, that means a lot."
        y 3f "Eh?"
        y 3v "I-It's nothing!"
        y "I'm just happy to help inspire fellow writers..."
        y "I know you're new to this, so don't worry so much if it seems like you can't get your poem to feel perfect."
        jump ch2_y_shared
    else:


        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y "This is pretty good, [player]."
        y "Were you influenced by seeing everyone's writing styles yesterday?"
        mc "I guess you could say that..."
        y 1m "I was also a bit surprised by how differently everyone writes."
        y "So I respect you for trying new things."
        jump ch2_y_shared

label ch2_y_good:

    if y_poemappeal[0] < 1:
        y 1a "Let's see what you've written for today."
        y "..."
        y 2e "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "...How did you pick up on this so quickly?"
        label ch2_y_good_shared:
            y 2v "Just yesterday, I was telling you the kind of techniques worth practicing..."
            mc "Maybe that's why..."
            mc "You did a good job explaining."
            mc "I really wanted to try giving it more imagery."
            show yuri 4b zorder 2 at t11
            "Yuri visibly swallows."
            "Even her hands appear sweaty."
            y "I'm not...used to this..."
            mc "Used to what?"
            y 3o "I don't know...!"
            mc "It's fine, take your time..."
            show yuri 3l at t11
            "Yuri breathes and collects her thoughts."
            "I know that Yuri likes to think before she speaks, so I offer that patience to her."
            y 4a "Yeah..."
            y "Just...being appreciated like this...I guess."
            y "It probably sounds really stupid..."
            y "But seeing someone motivated by my writing..."
            y "It just makes me..."
            y "Really happy..."
            mc "Are you saying you've never shared your writing before?"
            "Yuri nods."
            mc "Really? I don't believe it."
            y "I really only write for myself..."
            y "And besides..."
            y 3w "...People would just laugh at me!"
            mc "Do you really think that...?"
            "Again, Yuri nods."
            mc "Huh..."
            mc "Even your close friends?"
            y 2v "..."
            "Yuri doesn't respond to that."
            "I wonder why..."
            mc "Anyway..."
            mc "Do you want to share the poem you wrote today?"
            y "...Yeah."
            y 3t "I do!"
            y "If it's with you..."
            return
    else:

        y 1a "Let's see what you've written for today."
        y "..."
        y 2e "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "This one might even be better than yesterday's..."
        y "...How did you even pick up on this so quickly?"
        jump ch2_y_good_shared

label ch3_y_bad:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:
            y 4b "..."
            "Yuri doesn't look too enthusiastic about spending time with me..."
            "I guess if she changes her mind, she'll come to me."
            "But I should leave her be for now."
            $ skip_poem = True
            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        y 1i "..."
        y "...I see."
        y "I think you're improving at writing in general, [player]."
        y 2i "But I can't help but feel a little bit foolish."
        mc "Eh? What for?"
        y "Just..."
        y "I feel like I kept trying to offer advice..."
        y "When it should have been clear to me that you prefer a different writing style."
        y 3w "I probably just sounded arrogant!"
        y "I'm so stupid..."
        mc "Yuri, that's a little--"
        y 4b "No..."
        y "You don't understand."
        y "I spent so much time worrying about what's better and what's worse."
        y "Not just with you..."
        y "With Natsuki, and Sayori..."
        y "It's obvious now why nobody has fun when talking to me..."
        y "And because of that..."
        y 4c "...I'll just keep my mouth shut about your poem!"
        mc "..."
        "Yuri buries her head into her arms on her desk."
        "That's not the first time I've seen her do that."
        mc "I don't think it's ever as bad as you make it sound in your head..."
        y "..."
        mc "I think if people really didn't like talking to you..."
        mc "Then it would be a lot more obvious."
        mc "I know that you like to read deeply into things."
        mc "But some things are just worth taking at face value."
        y 4b "I just..."
        y "I've gotten so used to it..."
        y "...That it's hard for me to comprehend any other possibility."
        mc "Gotten used to what?"
        mc "Reading deeply into things?"
        y "Being disliked."
        mc "Yuri..."
        y 2v "What...what am I saying?"
        y "I'm sorry..."
        y "I never meant to bring this up..."
        "Yuri turns away from me."
        y 4b "You should go..."
        mc "Eh...?"
        y "Please..."
        y "Please don't look at me right now."
        y "I want to do some thinking..."
        mc "Are you sure...?"
        "Yuri nods."
        mc "Alright..."
        "I leave Yuri be."
        "Comforting or reassuring her is nearly impossible as it is."
        "So when she wants to be alone, I think anything I say could only make things worse."
        "I feel bad, but thankfully she doesn't take it out on me..."
        "I'll wait until she's feeling a little bit better."
        $ skip_poem = True
        return
    else:
        y 1a "..."
        y "...Ah."
        y "Decided to try something different today?"
        mc "I guess so."
        mc "Is that good, or bad?"
        y 2g "Well, neither."
        y "I have my preferences."
        y "But it would be unfair of me to call something good or bad based on that."
        label ch3_y_shared:
            y 1f "As always, I believe what's most important is exploring and discovering yourself."
            mc "That's comforting."
            mc "I'm kind of afraid of disappointing you in some way or another."
            y 2t "Eh...?"
            y "Why me...?"
            mc "Well, you're always sophisticated with your writing and have the most advice to share."
            y 4a "Is that so...?"
            y "..."
            "Yuri thinks for a good minute."
            y 4c "...That must be terrible."
            mc "Eh?"
            y "For me to have become someone whose opinion is fearsome..."
            y "How unlikable of me..."
            mc "Yuri..."
            mc "It's not as bad as you're making it sound in your head."
            mc "I just meant that I respect your opinion."
            y 2v "I see..."
            y "I'm sorry that I always overthink and come to those sorts of conclusions..."
            y "I'm just...a little too used to it."
            mc "Overthinking?"
            y "Being disliked."
            mc "Yuri..."
            y 3w "What...what am I saying?"
            y "I'm sorry, I didn't mean to bring that up..."
            y "Let's move on..."
            mc "Alright..."
            mc "Do you want to share your poem now?"
            y 2i "Okay..."
            y "Here."
            return


label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "..."
        y 1a "Well done, [player]."
        y "You've definitely improved your writing over the course of these few days."
        y "Has my advice been helpful to you?"
        mc "Yeah... Definitely."
        y 2m "I'm glad..."
        y "Sharing our writing like this..."
        y 2a "It's a lot more fun and rewarding than I anticipated."
        y "I need to remember to thank Monika..."
        y "I think we all felt a little awkward at first."
        y 1a "But now it seems like everyone is enjoying sharing their writing and seeing what others think."
        mc "I guess I can't really disagree."
        mc "I was afraid this whole thing would be a chore..."
        "But it's a great way for me to spend some personal time with all the girls in the club."
        mc "But it's been fun getting to know everyone and their writing."
        mc "And I guess doing some writing myself..."
        y 2a "Well..."
        y "Have you learned anything about yourself, [player]?"
        mc "Eh?"
        y 2i "Well, you know how I like to say that writing is a very personal way to get in touch with yourself..."
        y 1a "In the end, it doesn't matter if you're a good writer, or a bad writer."
        y "And even my opinions are just opinions...you know?"
        jump ch3_y_shared
    else:
        y 1e "..."
        y "...Ah."
        y "Decided to try something different today?"
        mc "I guess so."
        mc "Is that good, or bad?"
        y 2i "Well, neither."
        y "I have my preferences."
        y "But it would be unfair of me to call something good or bad based on that."
        jump ch3_y_shared

label ch3_y_good:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    if y_poemappeal[1] < 1:
        y "..."
        y 2u "[player]..."
        y "...This is wonderful."
        y "I can feel the emotion that you poured into it."
        y "Is this the result of trying what I suggested yesterday?"
        mc "Yeah, I guess so..."
        mc "You did a good job explaining."
        mc "I really wanted to try giving it more feeling."
        show yuri 4b zorder 2 at t11
        "Yuri visibly swallows."
        "Even her hands appear sweaty."
        play music t9 fadeout 1.0
        y "I'm not...used to this..."
        mc "Used to what?"
        y 3o "I don't know...!"
        mc "It's fine, take your time..."
        "Yuri breathes and collects her thoughts."
        "I know that Yuri likes to think before she speaks, so I offer that patience to her."
        y 4a "Yeah..."
        y "Just...being appreciated like this...I guess."
        y "It probably sounds really stupid..."
        y "But seeing someone motivated by my writing..."
        y "It just makes me..."
        y "Really happy..."
        mc "Are you saying you've never shared your writing before?"
        "Yuri nods."
        mc "Really? I don't believe it."
        y "I really only write for myself..."
        y "And besides..."
        y 3w "...People would just laugh at me!"
        mc "Do you really think that...?"
        "Again, Yuri nods."
        mc "Huh..."
        mc "Even your close friends?"
        y 2v "..."
        "For some reason, Yuri doesn't respond."
        mc "Yuri...?"
        label ch3_y_good_shared:
            if not renpy.music.get_playing(channel='music') == audio.t9:
                play music t9 fadeout 1.0
            "Yuri smiles sadly."
            y 1u "[player], during lunchtime, I eat by myself."
            y "Did you know that?"
            y "It's a great time to find a quiet spot and do some reading."
            y "In fact..."
            y 2s "I always have some books with me."
            y "You could say I really enjoy reading..."
            y "...Well, that's one way to put it, anyway..."
            y "But..."
            y "Books are so full of amazing and inspiring people."
            y "People you want to fall in love with."
            y "Or people you just know would make a really good friend."
            y 1m "Cheerful people, who always put a smile on your face..."
            y "Or deep thinkers, and problem solvers, who discover the mysteries of life."
            y "So when you look at it that way..."
            y "I'm surrounded by friends every day..."
            y "...You know?"
            y 2s "And those friends don't laugh at me..."
            y "They don't tease me for spacing out all the time..."
            y "They don't make fun of my body type..."
            y "And..."
            y 3v "...And they don't hate me for acting like a know-it-all!"
            mc "People...say that about you?"
            y "I'm not a know-it-all, [player]!"
            y "It's the opposite. I don't know anything!"
            y 4b "I don't know how to talk to people."
            y "I don't know how to make people see me as normal."
            y "I don't even know how to make myself happy!"
            y "I have all these feelings..."
            y "And all I can do with them is read, and write..."
            y "But it wasn't until now..."
            y 2s "That I started sharing it with you..."
            y "...That I really understood what was missing all this time."
            mc "But I haven't really done anything..."
            y "No..."
            y "That's wrong."
            y "Just being patient and respectful..."
            y 3u "That's really...important to me."
            y "I know I'm a difficult person, [player]..."
            y "I speak too slowly..."
            y "I second-guess myself all the time..."
            y "I read too deeply into things..."
            y "But every time..."
            y "You've always treated me just like anyone else."
            y "It's so rare that I feel comfortable with myself when I talk to others..."
            y "But that's why every time I talk to you..."
            y 2s "...I just feel really happy."
            mc "I see..."
            mc "Well, I treat you how you deserve to be treated, Yuri."
            mc "And if other people don't see it that way, then screw them."
            mc "I mean, I joined this club hoping I would make friends."
            mc "And I would say I've had at least one success."
            mc "Wouldn't you?"
            y 4b "U-Um..."
            y "If you put it that way..."
            y "...Yeah..."
            y 4e "We really are friends now, aren't we?"
            "Yuri puts her head in her hands."
            "But this time, she's smiling as she does it."
            mc "Do you want to show me your poem?"
            y 3s "Yeah."
            y "I do!"
            y "Let me get it for you..."
        return
    else:
        y "..."
        y "[player]."
        y 2s "Your writing has only improved in these last few days."
        y "Every poem you've shown me has been nothing short of spectacular."
        y "I can really feel the emotions..."
        y 2m "I'm a little envious, even..."
        y "I don't think it ever came to me this naturally."
        mc "Yuri, that's the wrong way to put it."
        mc "This never did come naturally to me."
        mc "But I've been able to improve so much thanks to you."
        mc "You're really the example I was chasing after."
        y 3u "I-Is that so...?"
        "Yuri gently smiles to herself."
        y "This feeling..."
        y "I'm so glad...I got the chance to share my writing."
        y 4e "I never thought it would feel like this."
        mc "I remember you mentioning that yesterday."
        mc "I can't believe that you're so good at something and you've never even shared it with anyone."
        mc "It's kind of a shame."
        y 2u "Maybe, but..."
        y "It's not like I really...had a choice."
        mc "What do you mean...?"
        y "Well..."
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
    m 1b "Hi again, [player]!"
    # If Nat shared her poem and ran, Monika already read it and plays a special script
    if n_poemearly:
        $ n_poemearly = False
        m "That was kind of silly with Natsuki earlier, wasn't it?"
        m 1j "I'm glad the two of you have been getting along so well."
        mc "..."
        "That's one way of putting it..."
        m 2a "Anyway, I already read your poem, but you can go ahead and read mine now."
        m 1a "I like the way this one turned out, so I hope you do too~"
        return
    else:
        m "How's the writing going?"
        mc "Alright, I guess..."
        m 2k "I'll take that."
        m 2b "As long as it's not going bad!"
        m 2a "I'm happy that you're applying yourself."
        m "Maybe soon you'll come up with a masterpiece!"
        mc "Ahaha, I wouldn't count on that..."
        m 2a "You never know!"
        m "Want to share what you wrote for today?"
        mc "Sure... Here you go."
        "I give my poem to Monika."
        m "..."
        m "...Alright!"
        $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))
        call expression nextscene

        m 1a "But anyway..."
        m "You want to read my poem now?"
        m "I like the way this one turned out, so I hope you do too~"
        mc "Alright, let's take a look."
        return

label ch3_m_start:
    m 2a "Hi [player]~"
    m "Have you thought about what you want to submit to perform at the festival?"
    mc "Well..."
    "Being in this club is one thing, but performing in front of a bunch of people..."
    mc "...I'll have to give it some more thought."
    m 2b "Okay, no pressure!"
    m "But whatever you do, I'm sure it'll turn out great."
    m "It would also make me happy to see."
    m 2k "Ahaha!"
    # If Nat shared her poem and ran, Monika already read it and plays a special script for chapter 3
    if n_poemearly:
        $ n_poemearly = False
        m 1a "Anyway, I already read your poem, but you can go ahead and read mine now."
        return
    else:
        m 1a "Anyway, let's take a look at today's poem!"
        mc "Sure..."
        "I let Monika take the poem I'm holding in my hands."
        m "..."
        $ nextscene = "m_" + poemwinner[2] + "_" + str(eval(poemwinner[2][0] + "_appeal"))
        call expression nextscene

        m 1a "Anyway...!"
        m "I'll share my poem with you now, alright?"
        mc "Er..."
        mc "Alright..."
        return

# All of Monika's responses to the poem per Doki and appeal level

label m_natsuki_1:
    m 2b "I like it, [player]!"
    mc "Really...?"
    m 2e "It's a lot cuter than I expected."
    m 2k "Ahahaha!"
    mc "Oh jeez..."
    m 1b "No, no!"
    m "It kind of makes me think of something Natsuki would write."
    m "And she's a good writer, too."
    m 5a "So take that as a compliment!"
    mc "Ahaha..."
    mc "If you say so."
    m "Yep!"
    m 1a "By any chance have you read anything by Shel Silverstein?"
    mc "Eh?"
    mc "Maybe a long time ago..."
    m "He's famous for telling all kinds of stories in just a few simple words."
    m "His poems can be funny, endearing, or even sad..."
    m 3d "And sometimes they're only a few lines long."
    m "They might even feel like they're written for kids, but if you think about them..."
    m "They can express views of the world that would apply to anybody."
    mc "I see..."
    mc "So you're saying that Natsuki is kind of like that?"
    m 2a "Sort of."
    m "Maybe she's not an expert..."
    m "But you probably won't find much filler in her poems."
    m "They might be easy to write, but they're super challenging to get the meaning through."
    m 2b "So I can see why it would be your kind of poem to explore!"
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
    m 1a "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m 1j "It's really metaphorical!"
    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."
    m 3b "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low."
    mc "That way, it always counts when I put in some effort."
    m 5a "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m 2a "You know that Yuri likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m 2d "Unlike Sayori, who likes using simple and direct words to describe happiness and sadness..."
    m "Yuri likes it when readers are left to derive their own meaning out of it."
    m 4d "It's very challenging to write like that effectively."
    m "Both allowing people to get something out of it just by feel..."
    m "Or letting them deeply analyze all of the nuances."
    m "It can take years of practice, which I'm assuming Yuri has at this point."
    m 1e "I never really asked, though..."
    mc "I'm sure I'm nowhere near her level yet."
    m 2b "Don't worry so much about that!"
    m "You do your own thing."
    m "Just keep exploring, and learn by trying new things!"
    return

label m_natsuki_2:
    m 1j "It's pretty good~"
    m 1a "You've been spending some time with Natsuki, haven't you?"
    m "You must like her writing style."
    mc "Ah, yeah..."
    mc "I think it's a neat way to tell a story."
    m 2a "Mhm. I don't disagree."
    m "Natsuki's poems may be cute, but they're also meaningful."
    m "I can see why you'd be into the style."
    m "I guess that means you're not as much a fan of Yuri's poems, then?"
    mc "Ah-- I wouldn't say that..."
    mc "I kind of like everyone's poems."
    m 2d "That's true, but I'm sure you like some more than others, right?"
    m "Like Yuri's use of complex words and symbolism..."
    m "Or Sayori's way of expressing happiness or sadness in a more direct way."
    m 2a "You must have some kind of preference, don't you?"
    m 4l "Ah, not that it's a contest or anything!"
    m 4a "I was just curious, that's all."
    return

label m_sayori_2:
    m 1j "It's pretty good~"
    m 1a "It makes me think of Sayori, like the other one that you wrote."
    m 4b "You two are like the dynamic duo!"
    mc "Ahaha... That's kind of exaggerating it."
    m 2a "Yeah, probably."
    m "But you do spend a lot of time with her even in this club, don't you?"
    m 2j "Then again, I don't blame you for being a little shy~"
    mc "I-I'm not shy, it's just..."
    m 5 "Ahaha! I'm just teasing."
    m "I know it takes a bit of time to make friends with everyone."
    m 2d "But Yuri and Natsuki are super interesting people, so don't be afraid to give them their share of time!"
    m "And you can talk to me every now and then too..."
    m 1e "I'm not, like, unapproachable or anything, am I?"
    mc "Ah, no, it's nothing like that..."
    mc "I'm just still getting used to being here, that's all."
    m 1a "Yeah..."
    m 1l "I'm sorry if I was putting pressure on you or something!"
    m "I really didn't mean it like that."
    mc "No, don't worry."
    mc "I get what you're saying."
    m 1a "Well, alright~"
    return

label m_yuri_2:
    m 2b "This one's good!"
    m "It feels like you're not only getting more comfortable with your style..."
    m "But the imagery is better than the last one I read!"
    m 2a "Just wondering, but have you been finding inspiration in Yuri's writing style?"
    mc "Hmm..."
    mc "I guess so."
    mc "You can't deny that she's talented."
    m 4k "Yeah, totally!"
    m 4a "I think her poems are the most..."
    m "...Romantic."
    m 1a "That's the best way to describe it."
    m 1d "She's like a totally different person when she picks up a pen..."
    mc "I noticed that, too."
    mc "Or when she's talking about literature, it's like a light turns on inside her."
    m 2a "Mhm!"
    m "Sadly, it's hard to get much personal conversation out of her..."
    m 2m "Trust me, I've tried..."
    m "Who knows what goes on in that head of hers?"
    mc "I hope you don't mean that in a bad way."
    m 1g "No, of course not!"
    m "I just meant that I wish she didn't keep so much to herself..."
    m 1e "But still, defending her like that..."
    m 5 "You must be pretty into her..."
    mc "Eh?!"
    mc "You...completely misunderstood!"
    m "Ahaha! Calm down, I'm kidding!"
    m 2a "Besides, I'm pretty sure she's already got a boyfriend..."
    mc "Wait, really?"
    m 2k "Yeah. A fictional one, anyway."
    "Monika kind of whispers that last part to me."
    m 5 "It's just a hunch, but..."
    mc "...Well, there's not really anything wrong with that!"
    m 1n "Oh, well I know...!"
    m "I was just saying~"
    return

label m_natsuki_3:
    m 2j "Sticking with the Natsuki style once more, I see~"
    m 2d "Hmm..."
    m "You really like Natsuki, don't you?"
    mc "Eh? That's--"
    m 5 "Oh, come on, [player]."
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Pretending to like the manga that she's into..."
    mc "Y-You know how Natsuki is...!"
    mc "If I don't indulge her, she'll end up hating me."
    m 2e "Eh?"
    m 2a "No, I think you're misunderstanding, [player]."
    m "It's not like Natsuki just hates anyone who doesn't give her what she wants."
    m 2d "Yeah, she's assertive, but she's not that selfish..."
    m "In fact, I think you're the only one who's indulged her as much as you have."
    mc "Is that so..."
    "I kind of knew that, but I just didn't want to admit it."
    m "So, I just need to ask one thing of you..."
    m 1e "...Be careful. Please?"
    m "Natsuki is kind of unpredictable."
    m "A lot of times, she doesn't even know what she wants."
    m 1i "After all, she's the youngest one here."
    m "She might not know how to handle her own feelings properly."
    m "What I'm saying is..."
    m 1m "If something bad happens, then it could end up damaging the club, too..."
    m 5 "And you wouldn't do that to me...right?"
    mc "That's--"
    "I'm not sure how to respond to Monika."
    "While I care about her and the club, it's also kind of unfair to bring that up."
    m "Well...you're smart."
    m "I'm sure you'll do the right thing."
    "Monika smiles sweetly."
    return

label m_sayori_3:
    m 1k "Ahaha."
    m "It's kind of funny..."
    mc "How so?"
    m 1a "No, not the poem..."
    m 2a "I mean, it's funny how your poems and Sayori's poems have been getting more and more similar to each other every day."
    m "I'm surprised you're so in sync with her."
    m 2d "Then again, you've been spending a lot of time together lately, haven't you?"
    mc "Ah, I guess you could say that..."
    mc "Although we kind of grew up as best friends, I haven't been seeing as much of her this past year..."
    mc "But since I joined the club, we've been spending a lot of time together again."
    m 1a "I see, I see~"
    m "That reminds me..."
    m "About how Sayori's been a little bit off today..."
    mc "Yeah? Did she tell you something?"
    m 1n "Ah..."
    m "Well..."
    m 2l "[player], you haven't been flirting with her, have you?"
    mc "O-Of course not!"
    mc "I've been treating her like I always do."
    m 2a "Alright."
    m 5 "Just making sure~"
    m "I know how much you care about her..."
    m "It would be terrible if something bad happened to her, so keep an eye on her."
    m 2d "Sayori's been acting so much happier ever since you joined the club."
    m "What could have happened all of a sudden...?"
    mc "..."
    m 1l "...Well, never mind."
    m "This really isn't the time to be talking about this..."
    return

label m_yuri_3:
    m 2e "Your style's gotten so refined, [player]."
    m "Yuri's been teaching you a lot of things, hasn't she?"
    mc "Well--"
    mc "I guess so."
    m 2a "Yeah... I've been noticing how much time you spend with her."
    m 2d "I think I've heard her say more words these past couple days than she's talked in the whole year."
    m "Not sure how you did it, but that's pretty impressive..."
    mc "Well, she just needs some patience and a way to talk about all the things in her head, I guess..."
    mc "I'm still getting the hang of it, myself."
    m 2a "Hm..."
    m "You're certainly putting in a lot of effort."
    m 2e "You must really like her."
    mc "Eh? That's--"
    m 5 "Ahaha!"
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Reading that edgy novel with her..."
    mc "Well--!"
    mc "I just...feel bad that she has a hard time socializing."
    mc "It makes me want to make sure she doesn't spend all her time alone."
    mc "Besides, the novel isn't too bad either, you know..."
    m 1k "Alright, alright~"
    m "I get you."
    m 1a "Just...be careful, alright?"
    m "I know that Yuri isn't used to opening herself up..."
    m 2d "So if something bad happens while she's vulnerable..."
    m "Then it could be really hard for her."
    m 2i "Her books aren't a total escape from reality."
    m "They're just a bandage."
    mc "You say that like I'm going to hurt her..."
    m 1l "Sorry, I didn't really mean that~"
    m "If anything, she might accidentally hurt herself."
    return
