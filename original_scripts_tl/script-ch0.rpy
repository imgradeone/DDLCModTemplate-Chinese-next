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
    "实际上, 我有 99% 的把握，她只是觉得帮忙成立一个新社团会很好玩。"
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
    "优里，看起来更加成熟，却有点害羞，似乎不太跟得上纱世里和夏树这样的人的节奏。"
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
    "The girls have a few desks arranged to form a table."
    "As Sayori mentioned, it's been widened so that there is one space next to Monika and one space next to Sayori."
    "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    "Still feeling awkward, I take a seat next to Sayori."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z zorder 2 at t32
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "Uwooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show sayori zorder 3 at f31
    s 4r "So cuuuute~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "I had no idea you were so good at baking, Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Monika. I follow."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "Natsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    mc "Eh? I thought you technically did. Sayori said--"
    show natsuki zorder 2 at t32
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show natsuki zorder 1 at thide
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a zorder 2 at t21
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show monika 4a zorder 2 at t22
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show yuri at h21
    y 3n "Eh?! T-That's not..."
    "Insulted, Yuri looks away."
    y 4b "I meant that, you know..."
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    y 2u "I'm glad..."
    "Yuri faintly smiles to herself in relief."
    "Monika raises an eyebrow, then smiles at me."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "So, what made you consider the Literature Club?"
    mc "Um..."
    "I was afraid of this question."
    "Something tells me I shouldn't tell Monika that I was practically dragged here by Sayori."
    mc "Well, I haven't joined any clubs yet, and Sayori seemed really happy here, so..."
    m 1j "That's okay! Don't be embarrassed!"
    m 1b "We'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    show monika 1a
    mc "Monika, I'm surprised."
    mc "How come you decided to start your own club?"
    mc "You could probably be a board member for any of the major clubs."
    mc "Weren't you a leader of the debate club last year?"
    m 5 "Ahaha, well, you know..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m 1b "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "Monika really is a great leader!"
    show yuri 1 zorder 2 at t33
    "Yuri also nods in agreement."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "Then I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "Yeah!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "We'll do our best."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "You know it!"
    "Everyone enthusiastically agrees."
    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't really know if I can keep up with their level of enthusiasm about literature..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c zorder 2 at t41
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1d zorder 3 at f33
    m "Really? I wouldn't have expected that, Yuri."
    m "For someone as gentle as you..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "I guess you could say that."
    y "But if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Ugh, I hate horror..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "Oh? Why's that?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "W-What?"
    n "What gives you that idea?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Fine, fine~"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"
    show sayori behind natsuki at t21
    "Sayori sidles up behind Natsuki and puts her hands on her shoulders."
    show natsuki at h42
    n 1v "{i}I'm not cute!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    show yuri 2f zorder 2 at t31
    y "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s31
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    show sayori 2g zorder 2 at t32
    s "Aww... I wanted to read everyone's poems..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "We all sit in silence for a moment."
    show monika 5a zorder 3 at f32
    m "Okay!"
    m "I have an idea, everyone~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "U-Um..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..."
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "Yeaaah! Let's do it!"
    show monika zorder 3 at f43
    m 1a "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, [player]?"
    show monika zorder 2 at t43
    "Monika smiles warmly at me once again."
    mc "Hold on...there's still one problem."
    show monika zorder 3 at f43
    m 1d "Eh? What's that?"
    "Now that we're back to the original topic of me joining the club, I bluntly come forth with what's been on my mind the entire time."
    show monika zorder 2 at t43
    mc "I never said I would join this club!"
    mc "Sayori may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "I lose my train of thought."
    "All four girls stare back at me with dejected eyes."
    show monika at s43
    m 1p "B-But..."
    show yuri at s42
    y 2v "I'm sorry, I thought..."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "Y-You all..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "That is, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "One by one, the girls' eyes light up."
    show sayori at h41
    s 4r "Yesss! I'm so happyyy~"
    "Sayori wraps her arms around me, jumping up and down."
    mc "H-Hey--"
    show yuri zorder 3 at f42
    y 1m "You really did scare me for a moment..."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "If you really just came for the cupcakes, I would be super pissed."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show monika zorder 2 at t43
    mc "Ah...thanks, I guess."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika zorder 1 at thide
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri and Natsuki clean up their food."
    show sayori 1a zorder 2 at t11
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s 4q "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    show sayori 1 zorder 2 at t41
    "Sayori,"
    show natsuki 4 zorder 2 at t42
    "Natsuki,"
    show yuri 1 zorder 2 at t43
    "Yuri,"
    show monika 1 zorder 2 at t44
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    return

label ch0_kill:
    $ s_name = "Sayori"
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

