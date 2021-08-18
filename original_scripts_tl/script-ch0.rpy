label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    $ s_name = "???"
    s "嘿~~~！！等等我！！"
    "我看见一个吵吵闹闹的女孩不断挥着手向我跑来，仿佛要把全世界的注意力都聚焦在她身上一样。"
    "她叫纱世里，我的邻居，也是我儿时的玩伴。"
    "也许放到从前，我不一定和她交朋友，但和她在一起很久后就慢慢生出了友谊。"
    "我们以前经常这样一起上学，但上了高中以后她睡懒觉的频率就越来越高，我也就有点懒得等她了。"
    "但她这样狂追不舍，搞得我真心想一走了之。"
    "不过，我只好叹了口气，在路口等着，好让纱世里赶上我。"
    $ s_name = "纱世里"
    show sayori 4p zorder 2 at t11
    s 4p "哈...哈..."
    s "我又睡过头了！"
    s "但这次我追上你了！"
    mc "也许吧，只不过我停下来等了你。"
    show sayori at s11
    s 5c "呃......说得好像你想把我甩开似的！"
    s "讨厌死了，[player]！"
    mc "不过，如果别人都看着你这奇怪的举止，我可不想和你一起被当作什么笨蛋情侣之类的。"
    show sayori zorder 2 at t11
    s 1a "好吧。"
    s "不过你确实也等了我。"
    s "想必你即使想使坏，也还是个温柔的人吧~"
    mc "纱世里，你高兴就好..."
    s 1q "诶嘿嘿~"
    show sayori zorder 1 at thide
    hide sayori
    "穿过马路后，我们继续向学校走去。"
    "走过拐角，映入眼帘的皆是路上熙熙攘攘的学生。"
    show sayori 3a zorder 2 at t11
    s "话说回来，[player]..."
    s "你决定好加入什么社团了吗？"
    mc "社团？"
    mc "我早就说过了，我对社团活动不感兴趣。"
    mc "况且我也从来没想过加什么社团。"
    show sayori at s11
    s 4h "诶？你骗人！"
    s "你跟我说过今年想参加社团的！"
    mc "是吗......？"
    "也许我真可能说过，为了迎合她不断跳跃的话题，大概就这样随口附和了。"
    "纱世里有点太担心我了，我只不过太满足于平淡的生活，把闲暇时间合理地分配在了动画和游戏上罢了。"
    s 4j "啊哈？可是——！"
    s "我刚刚还在说呢！我担心你上大学前还搞不清怎么和人打交道，而且你也没有什么特长。"
    s "我真的担心你过得开不开心！"
    s "我知道你现在过得还行，但我一想到过几年你就会变成一个完全融入不了社会的废宅，就非常害怕！"
    s 4g "你相信我，对吧？"
    s "别让我一直担心你啦......"
    mc "行吧..."
    mc "我会去一些社团转转，这样也许能让你安心一点。"
    mc "当然，我可不一定会入社。"
    s 1h "至少答应我去看看？"
    mc "好吧，这个我可以保证。"
    show sayori zorder 2 at t11
    s 4r "好耶~！"
    "我怎么就任由自己被这么一个无忧无虑的女孩说教呢？"
    "不仅如此，在她面前，我一点也强硬不起来，只能乖乖听任她的安排。"
    "我猜是看到她这么担心，至少想让她轻松一点吧 —— 毕竟她肯定是过度紧张了。"

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包，我茫然地盯着墙，完全没有半点动力。"
    mc "社团啊..."
    "纱世里希望我能去逛逛学校里的社团。"
    "我想我别无选择，除了动漫社......"

    s "喂——？"
    show sayori 1b zorder 2 at t11
    mc "纱世里...？"
    "纱世里肯定是在我发呆的时候悄悄溜进来的。"
    "四处张望了一下，我才意识到教室里只剩下我和她。"
    s 1a "我本来想趁你出教室时跟你碰个头，但看你一直坐在这里发呆，我就进来了。"
    s "有一说一，某些时候你比我还过分......这个仇，我记下了！"
    mc "如果社团活动都快要迟到了，那也没必要等我。"
    s 1y "唔，我觉得你需要有人推你一把，所以我..."
    mc "然后呢？"
    s 1a "你就可以加入我的社团啦！"
    mc "纱世里..."
    s 4r "啊哈？？"
    mc "...加入你的社团，那是不可能的。"
    show sayori at s11
    s 5d "嗯？！为什么啦！"
    "纱世里是文学部的副部长。"
    "讲真，我压根没觉得她会对文学感兴趣。"
    "实际上, 我有 99%% 的把握，她只是觉得帮忙成立一个新社团会很好玩。"
    "由于她是第一个加入新社团的成员，所以她自然而然地接过了“副社长”的职位。"
    "话虽如此，我对文学的兴趣绝对比她还少。"
    mc "没错，我已经决定去动漫社了。"
    show sayori zorder 2 at t11
    s 1g "拜托！求你了！"
    mc "不是，你为什么这么关心啊？"
    s 5b "这个嘛..."
    s "我昨天和她们说今天一定能带来一个新成员..."
    s "夏树连纸杯蛋糕都做好了..."
    s "诶嘿嘿..."
    mc "别随便做无法兑现的许诺啊喂！"
    "我都说不清她到底是真的脑袋一片空白，还是说她已经狡猾到早有预谋。"
    "我长长地叹了口气。"
    mc "好吧...看在小蛋糕的份上，我去参观一下？"
    show sayori at h11
    s 4r "好耶！跟我来～！"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "就这样，今天，我为了区区一个纸杯蛋糕而出卖了自己的灵魂。"
    "我垂头丧气地跟着纱世里穿过校园，登上了不常来的楼层 - 这里通常是三年级学生和社团活动所使用的地方。" # “这里通常是三年级学生和社团活动所使用的地方。” is not included in DDLC Plus
    "元气满满的纱世里一口气拉开了教室的门。"

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "各位！新成员在这里～！"
    mc "我说过了，不要叫我'新成--'"
    show sayori at lhide
    hide sayori
    "诶? 我的扫视了一遍房间。"
    show yuri 1a zorder 2 at t11
    y "欢迎来到文学部。很高兴见到你。"
    y "纱世里经常跟我说你的好话。"
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "真的假的？你带了个男生过来？"
    n "太毁气氛了吧。"
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "哇，[player]! 你怎么也来了！"
    m "欢迎来到文学部！"
    show monika 1a
    mc "..."
    "看着这幅景象，我根本说不出话来。"
    "这个社团里..."
    "{i}...全都是超级可爱的女孩子啊啊啊！！{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "你在看啥子哦？"
    n "想说什么你就直说。"
    mc "对...对不起..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "夏树..."
    $ n_name = '夏树'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "哼。"
    show natsuki zorder 2 at t32

    "我并不认识这个看起来脾气很嚣张的女生。很明显，这个应该就叫夏树。"
    "她那娇小的身材，看上去像是一年级的学妹。"
    "根据纱世里说的话，今天的纸杯小蛋糕也就是她做的。"

    show sayori 2q zorder 3 at f31
    s "她心情不好的时候，你可以直接无视她呢～"
    "纱世里悄悄地在我耳旁说道，接着又转向其他女孩子。"
    s 1x "总之！这位元气满满的孩子就是夏树了。"
    s "然后这位是优里，是社团最聪明的人！"
    $ y_name = '优里'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "别——别这么说..."
    "优里，看起来更加成熟，却有点害羞，似乎不太跟得上纱世里和夏树这类人的节奏。"
    show yuri zorder 2 at t33
    mc "啊...那个，很高兴认识你们俩。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "对了，似乎你已经认识莫妮卡，是吗？"
    $ m_name = '莫妮卡'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "没错。"
    m "[player]，很高兴又和你见面啦。"
    show monika 5a at hop
    "莫妮卡冲我甜甜地笑着。"
    "我们的确互相认识 - 好吧，虽然我们基本没说过话，但在去年还是同班同学。"
    "莫妮卡可以说是班级里最受欢迎的女生 - 聪明，漂亮，又擅长运动。"
    "基本上和我是两个世界的人。"
    "所以，看到她这么真诚地对我微笑，我有点..."
    mc "我...我也很高兴见到你，莫妮卡。"
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "快坐下，[player]！我们在桌子这边给你腾了些地方，你可以坐在我或者莫妮卡的边上。"
    s "我去把蛋糕拿来～"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "慢着！我做的蛋糕，我来拿！"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "对不起，我有点太兴奋了～"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "那，我去泡壶茶，怎样？"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们把几张课桌拼成了一张大桌子。"
    "正如纱世里所说，桌子加宽了，所以莫妮卡和她旁边都留了一个空位。"
    "夏树和优里则走到房间的角落，夏树端出来一个盖好的托盘，而优里打开了储藏间。"
    "我还是觉得有些尴尬，于是就坐在了纱世里的旁边。"
    "夏树趾高气扬地走了回来，手里端着托盘。"
    show natsuki 2z zorder 2 at t32
    n "哼哼，准备好了吗？"
    n "...哒哒！"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "哇哦！"
    "夏树掀开托盘上的锡箔纸，托盘上放着十二个小猫形状的白色、松软的小蛋糕。"
    "她用糖霜画出小猫的胡须，而小片的巧克力则被用来做成耳朵。T"
    show sayori zorder 3 at f31
    s 4r "好可爱～！"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "夏树，我从来不知道你的烘焙技术这么厉害！"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "嗯哼哼，没想到吧。"
    n "快尝尝！"
    "纱世里马上拿起了一块，然后是莫妮卡，接着是我。"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "超好吃！"
    "纱世里边吃边说着，脸上沾满了糖霜。"
    "我把蛋糕放在手里转了个圈，想找一个合适的角度下口。"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "夏树默不作声。"
    "我不禁注意到了夏树偷偷瞄向我的视线。"
    "她是在等我咬下去么？"
    "我终于咬下了一口。"
    "糖霜甜度正好，风味十足——这真的是她自己做的吗？"
    mc "这个真不错。"
    mc "谢谢你，夏树。"
    n 5h "为-为什么你要谢我？我又不是...！"
    "{i}（我是不是在哪听过这个台词？）{/i}"
    show natsuki at s32
    n 5s "...为了你才做的。"
    mc "诶？我觉得其实就是啊。纱世里说过--"
    show natsuki zorder 2 at t32
    n 12c "也许是吧！"
    n "但不是为了...就...不是为 {i}你{/i} 做的！笨蛋..."
    mc "行行行..."
    show natsuki zorder 1 at thide
    hide natsuki
    "我放弃理解夏树的古怪逻辑，只能草草结束了对话。"
    "优里这时端着一套茶具回到了桌旁。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在蛋糕托盘旁边。"
    show yuri 1a zorder 2 at t21
    mc "你居然把一整套茶具都放在部室里了？"
    y "别担心，老师已经同意了。"
    y "而且，热茶配好书，不是很好嘛？"
    mc "啊...也...也许吧..."
    show monika 4a zorder 2 at t22
    m "诶嘿嘿，别被吓到了，优里只是想给你留个好印象。"
    show yuri at h21
    y 3n "诶？！不...不是的..."
    "优里红着脸，看向一边。"
    y 4b "我的意思是，那个..."
    mc "我相信你。"
    mc "嗯，虽然阅读和品茶并不是我喜欢的消遣活动，但至少茶我是可以欣赏的。"
    y 2u "那就好..."
    "优里宽慰地微微一笑。"
    "莫妮卡挑了挑眉，也微笑地看着我。"
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "所以，你为什么会考虑来文学部？"
    mc "唔..."
    "我正怕问这个问题呢。"
    "直觉告诉我，不能告诉莫妮卡我是被纱世里拖过来的。"
    mc "那个，我还没有加入过哪个社团，而纱世里似乎在这里很开心，所以我..."
    m 1j "没问题！不要害羞！"
    m 1b "我们会让你感到宾至如归的，好吗？"
    m "作为文学部的部长，我的职责就是举办好玩的活动，让大家度过一段更有趣的社团时光！"
    show monika 1a
    mc "莫妮卡，我有些惊讶。"
    mc "你是怎么想到自己成立一个社团的？"
    mc "以你的能力，大概在任何一个大社团里都能成为管理层。"
    mc "你去年不还是辩论部的部长么？"
    m 5 "啊哈哈，嗯，那个..."
    m "说实话，我无法忍受大社团里的勾心斗角。"
    m "感觉一天到晚都只是在争论预算和宣传以及准备活动，都没有别的事情..."
    m "我更愿意选择自己喜欢的东西，然后做出点名堂来。"
    m 1b "而如果可以鼓励他人接触文学，那么我就是在实现这个梦想了！"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "莫妮卡真的是个很棒的部长！"
    show yuri 1 zorder 2 at t33
    "优里也点头同意。"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "我很惊讶，这里居然只有这么些部员。"
    mc "新社团刚起步一定很难吧。"
    m 3b "可以这么说。"
    m "没有多少人会愿意把全部精力投入到全新的事物中..."
    m "尤其是像文学这样，不能第一时间吸引到足够注意力的东西。"
    m "你必须努力向大家证明，这个社团既有趣又有意义。"
    m "而这也让校园活动，比如学园祭，变得更加重要。"
    m 2k "我有自信我们能在我们毕业之前，将文学部发展壮大！"
    m "对吧，各位？"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "是的！"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "我们会竭尽全力。"
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "还用我说嘛！"
    "大家都热情地赞同着。"
    "这样几个迥然不同的女生，却都对同样的事物感兴趣..."
    "莫妮卡一定花了不少功夫去找这三个成员。"
    "可能这就是为什么在听说会有新成员加入时，她们都会这么高兴。"
    "但我不知道自己对文学的热情，能不能比得上她们那样的程度..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
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
    y 2a "作者刻意利用你在想象力上的缺乏，完全打你一个措手不及，这不是很神奇吗？"
    y "话又说回来，最近我倒是读了不少恐怖小说呢..."
    mc "啊，我也读过一本恐怖小说..."
    "好不容易产生了一点点共鸣，我急急忙忙抓住了这个机会。"
    "不然再这样下去，优里看上去就像是在和一块石头说话了。"
    show monika 1d zorder 3 at f33
    m "真的？这我倒没想到，优里。"
    m "像你这样温柔的人..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "你这么评价，我想也没错。"
    y "但如果这个故事可以让我思考，或者将我带到了另一个世界，那么我真的会手不释卷的。"
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
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "诶嘿嘿，你的小蛋糕，还有你的诗..."
    s "你做的任何事都和你本人一样可爱～"
    show sayori behind natsuki at t21
    "纱世里溜到夏树背后，把手搭在她的肩上。"
    show natsuki at h42
    n 1v "{i}我才不可爱呢！！{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "夏树，你会自己写诗？"
    n 1c "诶？嗯，偶尔吧。"
    n "你问这个干嘛？"
    mc "我觉得很了不起啊。"
    mc "为什么不找个时间分享一下呢？"
    n 5q "不-不行！"
    "夏树的眼神游移着。"
    n "你们不会...喜欢的..."
    mc "啊...对自己的水平还不够自信吗？"
    show yuri 2f zorder 2 at t31
    y "我理解夏树的感受。"
    y "分享那种水平的文字需要的可不仅仅是自信。"
    y 2k "最真挚的文字是写给自己的。"
    y "所以分享的前提是，你必须要愿意向读者敞开心扉，暴露出自己的脆弱，甚至展现心灵的最深处。"
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "优里，你也有写作的经验吗？"
    m "要是你愿意分享一下你的作品，没准就能树起榜样作用，让夏树也能放心分享。"
    show yuri at s31
    y 3o "......"
    mc "似乎优里也是这样想的..."
    show sayori 2g zorder 2 at t32
    s "啊...我倒是很想读大家的诗..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "气氛短时间陷入了沉默。"
    show monika 5a zorder 3 at f32
    m "这样吧！"
    m "各位，我有个主意～"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...？"
    "夏树和优里疑惑地看向莫妮卡."
    m 2b "我们每个人回家写一首的诗吧！"
    m "然后，在下次社团活动的时候，我们就可以互相分享了。"
    m "这样的话，大家就扯平了！"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "唔...唔..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "......"
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "好啊！就这么办！"
    show monika zorder 3 at f43
    m 1a "而且，既然我们有新成员加入，我觉得这样的活动就能让大家相处得更自在一点，还能加强社团的凝聚力。"
    m "对吧，[player]？"
    show monika zorder 2 at t43
    "莫妮卡又冲我甜甜地笑着。"
    mc "等一下...还有一个问题。"
    show monika zorder 3 at f43
    m 1d "诶？还有什么问题吗？"
    "既然已经回到了拉我进社团的话题，我终于能够直截了当地说出我一直以来的心声。"
    show monika zorder 2 at t43
    mc "我从来都没说过我要入部啊！"
    mc "虽然纱世里说服了我来看看，但我可没下过任何决定。"
    mc "我还有别的一些社团要看看，而且...呃..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "我的思路戛然而止。"
    "四个女生都用失落的眼神看着我。"
    show monika at s43
    m 1p "但——但是..."
    show yuri at s42
    y 2v "抱歉，我以为..."
    show natsuki at s44
    n 5s "哼。"
    show sayori at s41
    s 1k "[player]..."
    mc "你——你们..."
    "我...我对可爱的女孩子毫无抵抗力啊。"
    "这种情况下我怎么做一个头脑清醒的决定啊？"
    "不过，如果只要写写诗，我就能每天和这些可爱的女生待在一起..."
    mc "...好吧。"
    mc "那我决定了。"
    mc "我要加入文学部。"
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "女生们的眼神一个接一个地泛起了光彩。"
    show sayori at h41
    s 4r "太好了！我好高兴～"
    "纱世里抱着我上蹿下跳。"
    mc "喂——喂——"
    show yuri zorder 3 at f42
    y 1m "你有一瞬间真的吓到我了..."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "如果你真的只是来蹭蛋糕的，那我会超生气的。"
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "那么，正式欢迎！"
    m "欢迎来到文学部！"
    show monika zorder 2 at t43
    mc "啊...谢谢。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
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
    "与此同时，优里和夏树开始整理桌子，大家继续这样有的没的闲聊着。"
    show sayori 1a zorder 2 at t11
    s "对了, [player], 你来都来了, 咱们今天一起走回家吧？"
    "对哦 - 因为纱世里在放学后总是要参加社团活动, 所以我们就再也没有一起回过家。"
    mc "好啊, 我们走吧。"
    s 4q "好耶~"

    scene bg residential_day
    with wipeleft_scene

    "就这样, 我们俩离开了部室，踏上了回家的路。"
    "一路上，我的思绪都在四位女孩间游转："
    show sayori 1 zorder 2 at t41
    "纱世里，"
    show natsuki 4 zorder 2 at t42
    "夏树，"
    show yuri 1 zorder 2 at t43
    "优里，"
    show monika 1 zorder 2 at t44
    "当然，还有莫妮卡。"
    "把每天放学后的时间花在文学部里，我真的会很开心吗？"
    "说不定我还有机会和当中的某个女生拉近距离..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "好的！"
    "我只要充分利用条件就行了，好运总有一天会来的。"
    "看来我要从今晚的写诗开始了..."

    return

label ch0_kill:
    $ s_name = "纱世里"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "什...什么......"
    s 1g "..."
    s "这..."
    s "这是哪里......?"
    s "哦......"
    s 1u "不......"
    s "不可能。"
    s "绝对不可能。"
    s 4w "这又是哪跟哪？"
    s "我又是谁？"
    s "停下来！"
    s "快点停下来！！！"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return

