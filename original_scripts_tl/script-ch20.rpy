label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "平常的上学日，一如既往。"
    "早上可以说是最糟糕的，会被周围的现充包围着走到学校。"
    "与此同时，我却总是一个人。"
    "我经常告诉自己，差不多是时候该找一个女朋友之类的了..."
    "但我确实没什么动力去加入什么社团。"
    "可以把空余时间花在游戏和动画上，我其实已经相当满足了。"
    "学校总是会有动画部的，但是那里怎么可能会有女孩啊..."

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包，我茫然地盯着墙，完全没有半点动力。"
    mc "社团啊..."
    "真的没什么社团能让我提起兴趣。"
    "除此以外，大部分社团都会安排很多事，这我肯定受不了。"
    "我想我别无选择，除了动漫社......"

    $ m_name = "???"

    m "...[player]？"
    window hide(None)
    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "...莫妮卡？"
    $ m_name = "莫妮卡"
    m 1b "天哪，我完全没想到会在这里看见你！"
    m 5 "有一段时间没见了，对吧？"
    mc "啊..."
    mc "确实。"
    "莫妮卡冲我甜甜地笑着。"
    "我们的确互相认识 - 好吧，虽然我们基本没说过话，但在去年还是同班同学。"
    "莫妮卡可以说是班级里最受欢迎的女生 - 聪明，漂亮，又擅长运动。"
    "基本上和我是两个世界的人。"
    "所以，看到她这么真诚地对我微笑，我有点..."
    mc "话说，你怎么会来这？"
    m 1a "哦，我只是来找一点我的社团会用得上的东西。"
    m 1d "你知道这里有没有彩纸吗？"
    m "或者马克笔？"
    mc "我觉得你可以看看储藏间里有没有。"
    mc "...你在辩论部，对吧？"
    m 5 "啊哈哈，关于那个..."
    m "实际上，我退出辩论部了。"
    mc "真的？你退部了？"
    m "是的..."
    m 2e "说实话，我无法忍受大社团里的勾心斗角。"
    m "除了争论预算和宣传以及准备活动，感觉都没有别的事情..."
    m "我更愿意选择自己喜欢的东西，并做出一些有意义的事。"
    mc "这样啊，那你后来加入哪个社团了？"
    m 1b "其实，我正在组建一个新的！"
    m "是一个文学部！{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "是一个文学部！{fast}"
    window auto
    mc "文学...？"
    "听起来有点...无聊？"
    mc "那么你们现在有多少部员了呢？"
    m 5 "唔..."
    m "啊哈哈..."
    m "有点不好意思讲，不过现在我们只有三个人。"
    m "为这个听上去很无聊的社团寻找新成员真的很难..."
    mc "嗯，我能理解..."
    m 3d "但是这个社团一点也不无聊，真的！"
    m "文学可以是任何东西。阅读，写作，诗歌..."
    m 3e "我意思是，我们的一个社员甚至把她的漫画收藏拿到了部室.."
    mc "等等...真的吗？"
    m 2k "是的，有点好玩，对吧？"
    m 2e "她总是坚称漫画也是文学的一部分。"
    m "我的意思是，她说得应该也没错..."
    m "况且，成员有一个算一个，对吧？"
    "...莫妮卡刚刚是不是说了...“她”？"
    "唔..."
    m 1a "嘿，[player]..."
    m "就随便问问...你还在找要加入的社团吗？？"
    mc "啊--"
    mc "我，大概在找，不过..."
    m "这样的话..."
    m 5 "你可以帮我一个大忙吗？"
    m "我不会直接要求你加入，不过..."
    m "如果你能稍微来我的社团参观一下，我会非常开心的。"
    m "可以吗？"
    mc "唔..."
    "嗯，我想我没有拒绝的理由..."
    "况且，我怎么会拒绝像莫妮卡这样的人呢？"
    mc "行，我想我去一下没什么问题。"
    m 1k "啊哈，太棒了！"
    m 1b "你真的很温柔呢，[player]，你知道吗？"
    mc "这-这没什么的，真的..."
    m 1a "那我们走吧？"
    m "我下次再来拿材料吧 - 你更重要些。"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "就这样，今天，我把灵魂出卖给了莫妮卡和她那无人可挡的微笑。"
    "我羞怯地跟随着莫妮卡穿过校园，登上了不常来的楼层 - 这里通常是三年级学生和社团活动所使用的地方。"
    "元气满满的莫妮卡一口气拉开了教室的门。"

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "我回来啦～！"
    m "而且我还带来了一位客人！"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "诶？"
    y "一个...客人？"
    show natsuki 4c zorder 2 at t32
    n "真的假的？你带了个男生过来？"
    n "太毁气氛了吧。"
    show monika 3m zorder 3 at f31
    m "不要说得那么过啦，夏树..."
    m 3b "...不管怎样，欢迎来到文学部，[player]!"
    show monika 3a zorder 2 at t31
    mc "..."
    "看着这幅景象，我根本说不出话来。"
    "这个社团里..."
    "{i}...全都是超级可爱的女孩子啊啊啊！！{/i}"

    show natsuki zorder 3 at f32
    n 5c "那么，我来猜一猜..."
    n "你是莫妮卡的男朋友，对吧？"
    show natsuki zorder 2 at t32
    mc "什--"
    mc "不，不是！"
    show yuri zorder 3 at f33
    y 2l "夏树..."
    $ n_name = '夏树'
    "我并不认识这个看起来脾气很嚣张的女生。很明显，这个应该就叫夏树。"
    "她那娇小的身材，看上去像是一年级的学妹。"

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "总-总之，这位是夏树，和平常一样充满活力..."
    m 2b "这位是优里，文学部的副部长！"
    $ y_name = '优里'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "很-很荣幸认识你..."
    "优里，看起来更加成熟，却有点害羞，似乎不太跟得上夏树这类人的节奏。"
    show yuri zorder 2 at t33
    mc "嗯...很高兴认识你们俩。"
    show monika zorder 3 at f31
    m 1a "我正巧在教室里碰到了 [player]，然后他决定来社团看看。"
    m "还不错吧？"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "等等！莫妮卡！"
    n "难道我没和你说过，在让其他人加入之前先告诉我的么？"
    n 4q "我正要...好吧，你知道的..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "抱歉，抱歉！"
    m "我没忘，只不过我碰巧遇见他了。"
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y "这样的话，我去泡壶茶，怎样？"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "嗯，再好不过了！"
    m "你不过来坐坐吗，[player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们用几张课桌拼成了一张大桌子。"
    "优里走到了房间的角落，打开了储藏间。"
    "与此同时，莫妮卡和夏树面对面坐在了桌旁。"
    "我还是觉得有些尴尬，于是就坐在了莫妮卡的旁边。"
    show monika 1a zorder 2 at t11
    m "嗯，我知道你其实并没有打算要来这里..."
    m "但是我们会让你感到宾至如归的，好吗?"
    m 1j "作为文学部的部长，我的职责就是要让所有人都能感受到社团的有趣刺激！"
    mc "我很惊讶，这里居然只有这么些部员。"
    mc "新社团刚起步一定很难吧。"
    m 3b "可以这么说。"
    m "没有多少人会愿意把全部精力投入到全新的事物中..."
    m "尤其是像文学这样，不能第一时间吸引到足够注意力的东西。"
    m "你必须努力向大家证明，这个社团既有趣又有意义。"
    m "而这也让校园活动，比如学园祭，变得更加重要。"
    m 2k "我有自信我们能在我们毕业之前，将文学部发展壮大！"
    m "对吧，夏树？"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "好吧..."
    n "...大概吧。"
    "夏树勉勉强强同意了。"
    "这样几个迥然不同的女生，却都对同样的事物感兴趣..."
    "莫妮卡一定花了不少功夫去找这两个成员。"
    "优里这时端着一套茶具回到了桌旁。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在蛋糕托盘旁边。"
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "你居然把一整套茶具都放在部室里了？"
    y "别担心，老师已经同意了。"
    y "而且，热茶配好书，不是很好嘛？"
    mc "啊...也...也许吧..."
    show monika 4a zorder 3 at f22
    m "诶嘿嘿，别被吓到了，优里只是想给你留个好印象。"
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "诶？！不...不是的..."
    "优里红着脸，看向一边。"
    y 4b "我的意思是，那个..."
    show yuri zorder 2 at t21
    mc "我相信你。"
    mc "嗯，虽然阅读和品茶并不是我喜欢的消遣活动，但至少茶我是可以欣赏的。"
    show yuri zorder 3 at f21
    y 2u "那就好..."
    show yuri zorder 2 at t21
    "优里宽慰地微微一笑。"
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "所以说，[player]，你平时喜欢读些什么呢？"
    mc "这个...啊..."
    "考虑到我过去几年匮乏的阅读量，我真的不知道该如何回答。"
    mc "...漫画..."
    "我半开玩笑地小声嘀咕着。"
    show natsuki 1c zorder 2 at t41
    "夏树的头突然抬了起来。"
    "她似乎想说些什么，不过最后还是选择了沉默。"
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "不...不算是一个阅读爱好者呢，我猜..."
    mc "...呃，这也是可以改变的..."
    "我这是在说什么？"
    "我看着优里的苦笑，就情不自禁地说出了刚刚那句话。"
    mc "话说回来，你喜欢读些什么呢，优里？"
    y 1l "嗯，让我想想..."
    "优里的指尖描划着茶杯边缘。"
    y 1a "我最喜欢的是那种构建了深邃复杂世界的幻想小说。"
    y "它们背后的创造力和匠心水平，真是让我大开眼界。"
    y 1f "而且，能在那种陌生的世界观下叙述好一个故事，也同样令人钦佩。"
    "优里继续说着，显然对阅读充满热情。"
    "从我走进社团以来，她似乎一直很害羞和沉默，但从她亮起来的眼神可以看出，比起现实的人际关系，她更喜欢在书中寻求安慰。"
    y 2m "不过嘛，我喜欢的类型可宽泛了。"
    y "有着深层次心理要素的故事也能让我沉浸其中。"
    y 2a "诗人刻意利用你在想象力上的缺乏，完全打你一个措手不及，这不是很神奇吗？"
    y "话又说回来，最近我倒是读了不少恐怖小说呢..."
    mc "啊，我也读过一本恐怖小说..."
    "好不容易产生了一点点共鸣，我急急忙忙抓住了这个机会。"
    "不然再这样下去，优里看上去就像是在和一块石头说话了。"
    show monika 1j zorder 3 at f33
    m "啊哈哈，确实很像你呢，优里。"
    m 1a "这很符合你的性格。"
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "哦，是吗？"
    y "说真的，如果这个故事可以让我思考，或者将我带到了另一个世界，那么我真的会手不释卷的。"
    y "超现实主义的恐怖小说会改变你看待世界的方式，哪怕只有一小会。"
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "呃，我讨厌恐怖小说..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "哦？为什么？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "呃，我只是..."
    "夏树短暂地撇了我一眼。"
    n 5q "没什么。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "对了，你平常更喜欢写可爱的东西，对吧，夏树？"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "什...什么？"
    n "你从哪里冒出来的这种想法？"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "上次社团活动结束后，你在教室里掉了张小纸片。"
    m "你似乎正在写一首诗，叫——"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "不要讲得那么大声啦！！"
    n "还有，把它还给我！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "好吧，好吧～"
    show monika 1a zorder 2 at t33
    mc "夏树，你会自己写诗？"
    show natsuki zorder 3 at f31
    n 1c "诶？嗯，偶尔吧。"
    n "你问这个干嘛？"
    show natsuki zorder 2 at t31
    mc "我觉得很了不起啊。"
    mc "为什么不找个时间分享一下呢？"
    show natsuki zorder 3 at f31
    n 5q "不-不行！"
    "夏树的眼神游移着。"
    n "你们不会...喜欢的..."
    show natsuki zorder 2 at t31
    mc "啊...对自己的水平还不够自信吗？"
    show yuri zorder 3 at f32
    y "我理解夏树的感受。"
    y "分享那种水平的文字需要的可不仅仅是自信。"
    y 2k "最真挚的文字是写给自己的。"
    y "所以分享的前提是，你必须要愿意向读者敞开心扉，暴露出自己的脆弱，甚至展现心灵的最深处。"
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "优里，你也有写作的经验吗？"
    m "要是你愿意分享一下你的作品，没准就能树起榜样作用，让夏树也能放心分享。"
    show yuri at s32
    y 3o "..."
    mc "似乎优里也是这样想的..."
    "气氛短时间陷入了沉默。"
    show monika zorder 3 at f33
    m 5a "嘿，我突然有个主意！"
    m "这样如何？"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "...？"
    "夏树和优里疑惑地看向莫妮卡."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "我们每个人回家写一首的诗吧！"
    m "然后，在下次社团活动的时候，我们就可以互相分享了。"
    m "这样的话，大家就扯平了！"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "唔...唔..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "啊..."
    m "我是说，我觉得这是个好主意..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "那个..."
    y "...我觉得你说的没错，莫妮卡。"
    y 2f "我们或许应该开始找一些可以让我们全员参与的活动了。"
    y 2h "毕竟作为副部长，我也要负起责任来..."
    y "我也要尽力培养社团和社团的成员。"
    y 2a "况且，既然我们有了一个新成员..."
    y "迈出这一步似乎也不错。"
    y "你也同意吗，[player]?"
    show yuri zorder 2 at t32
    mc "等一下...还有一个问题。"
    show monika zorder 3 at f33
    m 1d "诶？还有什么问题吗？"
    "既然已经回到了拉我进社团的话题，我终于能够直截了当地说出我一直以来的心声。"
    show monika zorder 2 at t33
    mc "我从来都没说过我要入部啊！"
    mc "虽然莫妮卡说服了我来看看，但我可没下过任何决定。"
    mc "我还有别的一些社团要看看，而且...呃..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "我的思路戛然而止。"
    "三个女生都用失落的眼神看着我。"
    show monika at s33
    m 1p "但——但是..."
    show yuri at s32
    y 2v "抱歉，我以为..."
    show natsuki at s31
    n 5s "哼。"
    mc "诶...？"
    "女孩们相互交换了一下眼神，之后莫妮卡转向了我。"
    show monika zorder 3 at f33
    m 1m "我...我猜我需要告诉你真相，[player]."
    m "事实上..."
    m 1p "...我们甚至还没有达到组建一个正式社团的最低人数要求。"
    m "我们至少需要四个人..."
    m "而且我已经非常、非常尽力地去寻找新成员了。"
    m "而如果我们没能在学园祭之前再找到一个的话..."
    show monika zorder 2 at t33
    mc "..."
    "我...我对可爱的女孩子毫无抵抗力啊。"
    "这种情况下我怎么做一个头脑清醒的决定啊？"
    "在这种情况下，我还让她们失望的话，我会感到很难受的..."
    "更何况，这个社团本身看上去还挺轻松的..."
    "因此，如果只要写写诗，我就能每天和这些可爱的女生待在一起..."
    mc "...好吧。"
    mc "那我决定了。"
    mc "我要加入文学部。"
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "女生们的眼神一个接一个地泛起了光彩。"
    show monika zorder 3 at f33
    m "我的天啊，真的吗？"
    m "你真的确定吗，[player]?"
    show monika zorder 2 at t33
    mc "是的..."
    mc "应该会挺有意思的，对吧？"
    show yuri zorder 3 at f32
    y 1m "你有一瞬间真的吓到我了..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "如果你真的就直接走了，我真的会超生气的。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], 我非常高兴..."
    m 1k "我们终于可以成为正式社团了！"
    m 1e "真的非常感谢你。你很了不起。"
    m "我会尽一切努力让你在这里的时间变得有意义的，可以吗？"
    show monika zorder 2 at t33
    mc "啊...谢谢你。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "好了, 各位!"
    m "这么一来, 今天的社团活动到这里就正式圆满结束了。"
    m "各位要记得今晚的任务："
    m "每个人写一首诗，明天带过来，这样我们就可以分享了！"
    "莫妮卡再一次看向了我。"
    m 1a "[player]，期待你的表现哦。"
    show monika 5 at hop
    m "诶嘿嘿~"
    mc "好...好吧..."
    show monika zorder 1 at thide
    hide monika
    "我真的能用我那平庸的写作水平打动班级之星莫妮卡吗？"
    "焦虑已经在我的心中开始翻涌了。"
    "与此同时，优里开始整理桌子，大家继续这样有的没的闲聊着。"
    mc "那我就回家了..."
    show monika 5a zorder 2 at t11
    m "好的！"
    m "那么我们明天见。"
    m "我都等不及了！"

    scene bg residential_day
    with wipeleft_scene

    "就这样, 我离开了部室，踏上了回家的路。"
    "一路上，我的思绪都在三位女孩间游转："
    show natsuki 4a zorder 2 at t31
    "夏树，"
    show yuri 1a zorder 2 at t32
    "优里，"
    show monika 1a zorder 2 at t33
    "当然，还有莫妮卡。"
    "把每天放学后的时间花在文学部里，我真的会很开心吗？"
    "说不定我还有机会和当中的某个女生拉近距离..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "好的！"
    "我只要充分利用条件就行了，好运总有一天会来的。"
    "看来我要从今晚的写诗开始了..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("你解锁了一首特殊诗。\n是否查看？", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return

