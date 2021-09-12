

label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "又是平常的一天，眨眼间已经到了社团活动的时间了。"
    "几天过去，我对文学部已经相当习惯了。"
    "走进部室，迎来的又是那熟悉的一幕。"
    show sayori 2x zorder 2 at t11
    s "嗨，[player]～"
    mc "哟，纱世里。"
    mc "看起来你今天心情不错啊。"
    s 1q "诶嘿嘿～"
    s "我只是还不太习惯你出现在社团里，仅此而已。"
    mc "了解..."
    mc "...这么小一件事都能让你这么高兴啊。"
    mc "不过似乎你也总是为这种小事开心呢。"
    s 1d "说起来..."
    s "我有点饿了..."
    s "要和我一起去买零食吗？"
    mc "不，谢了。"
    s 4h "诶？？"
    s "这-这一点也不像你！！"
    mc "我有我的理由。"
    mc "不如检查下你的钱包，纱世里？"
    s 4l "诶-诶？"
    show sayori at s11
    s "为什么...突然要这么做？"
    mc "没有为什么，真的。"
    mc "我只是想看看。"
    s 1l "啊-啊..."
    show sayori zorder 2 at t11
    "纱世里紧张地拿出了她的零钱包。"
    "她笨拙地摸索着扣子，将钱包打开。"
    "然后，她把钱包倒过来，把里面的东西倒在了桌面上。"
    "只掉出来了两个小硬币。"
    s 5a "啊-啊哈哈...."
    mc "我就知道..."
    mc "我早就看穿你了，纱世里。"
    s 5c "这不公平！"
    s "你怎么会知道的？"
    mc "很简单。"
    mc "如果你一开始就有足够的钱，来部室之前你肯定就买好零食了。"
    mc "所以，要么就是你不饿，只是想找个借口出去走走..."
    mc "要么就是，你早就花光了所有的钱，所以试图装健忘骗我借钱给你！"
    mc "不过还有一点是..."
    mc "...你没有不饿的时候！"
    mc "这样一来，就只剩下一个选项了！"
    s 4p "呜啊啊啊～！"
    s "我投降了！"
    s "不要让我觉得有罪恶感嘛！"
    mc "如果你觉得有罪恶感，那就意味着你确实应该感到有罪恶感..."
    show yuri 1c zorder 2 at t33
    y "啊哈哈。"
    "优里突然咯咯地笑了起来。"
    show sayori 4g
    mc "诶？"
    "我都没注意到她在听我们说话。"
    "她的脸埋在书里，就跟往常一样。"
    show yuri 3n at h33
    y "啊-啊！"
    y "我刚刚没有在听--！"
    y 3o "只不过是...书里的东西..."
    show sayori zorder 3 at f32
    s 1h "优里--..."
    s "快让 [player] 借我些钱..."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "这--！"
    y "别这样把我扯进来啊，纱世里..."
    y "而且..."
    y 1k "你应该根据自己的经济情况来买东西..."
    y "坦白地说，耍了个小把戏后，你也算是受到相应的报应了。"
    show sayori 1b
    mc "..."
    y 3n "啊--！"
    y "我刚刚是不是..."
    y 4c "我-我不是那个意思！！"
    y "我看这本书看得太入迷了..."
    y "唔..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1r "啊哈哈！"
    s 3x "我真喜欢你直言不讳的样子，优里..."
    s "挺少见的，不过这也是你有趣的一面！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3v "这..."
    y "你怎么会那样想..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1x "不过你说的倒也没错啦..."
    s "我做了错事，于是就得接受抱怨。"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "是报应..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1l "就那个词啦！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "难得你会这么说，纱世里..."
    y 1a "大概每个人心中都有只小恶魔，不是吗？"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1q "诶嘿嘿..."
    show sayori zorder 2 at t32
    mc "别让她给骗了啊。"
    mc "纱世里知道她在做什么。"
    mc "别忘了，她在跟我说之前，就已经告诉你们她会把我带到社团来..."
    show sayori zorder 3 at f32
    s 1h "但-但是...！"
    s "如果不是为了小蛋糕的话，你可不会来的..."
    s "所以我只好骗夏树去做蛋糕！"
    show sayori zorder 2 at t32
    mc "拜托，给我多点肯定啊，纱世里。"
    show sayori zorder 3 at f32
    s 1l "诶嘿嘿..."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}啪！{/i}"
    hide white
    s 4p "咿呀--！"
    "某个东西突然凭空冒出来，啪地打在了纱世里脸上后滚落桌上。"
    s 4j "嗷..."
    s "什么啊--"
    s 4n "诶？？"
    s "曲-曲奇！"
    "没错，一块塑料包装的巨型曲奇。"
    "纱世里环绕了四周。"
    s 4m "这-这是奇迹吗？"
    s "因为我受到了报复!"
    show sayori zorder 2 at t32
    mc "是报应..."
    show sayori 4n
    show yuri zorder 3 at f33
    y 1u "其实你这个词差不多算是用对了..."
    show yuri zorder 2 at t33
    show natsuki 3z zorder 3 at f31
    n "啊哈哈哈！"
    n "我 {i}本来{/i} 就是想给你的。"
    n 3d "但接着又听到你多嘴说起了小蛋糕的事。"
    n "不过，你的反应还挺有趣的。啊哈哈！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 4m "夏-夏树！"
    s "你人好好哦！"
    s 4s "我超开心..."
    "纱世里抱住了曲奇。"
    show sayori zorder 2 at t32
    mc "哎呀，你就吃吧..."
    "纱世里飞快地拆开包装，咬了一大口。"
    show sayori zorder 3 at f32
    s 4q "针不戳..."
    show sayori zorder 3 at hf32
    s 4o "唔——！"
    "纱世里突然把手捂到了嘴上。"
    s 4p "我咬到舌头了..."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3a "诶嘿嘿。"
    n "你吃个曲奇事儿还真多。"
    "夏树咬了一口自己的曲奇。"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1c "啊，你的看起来也很不错嘛，夏树！"
    s "我能尝尝吗？"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "真是的..."
    n "乞丐没得挑！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1h "但是你的是巧克力味的..."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4c "是啊，不然你觉得我干嘛给你那一块？"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "好吧..."
    s 1q "不过，我还是非常高兴你能把这块分享给我呢。"
    s "诶嘿嘿～"
    show sayori behind natsuki zorder 2 at t21
    "纱世里起身走到夏树身后，伸出双臂搂住了她。"
    n 12c "啊--真是的..."
    n "行啦行啦。"
    "夏树手里还拿着曲奇，于是她用手肘把纱世里推开。"
    show sayori 1n at h21
    s "...{i}啊呜。{/i}"
    "纱世里突然弯下身，咬了一口夏树的曲奇。"
    n 1p "{i}喂-喂！！{/i}"
    n "你还真就上嘴抢啊？！"
    s 1q "呜呼呼呼~！"
    show sayori at lhide
    hide sayori
    "纱世里嘴里塞得满满的，快步跑到了安全的地方。"
    show yuri 1c
    "优里和我也笑了起来。"
    show yuri 1a
    show natsuki zorder 3 at f31
    n 1w "天哪！有时候你还真像个活小孩！"
    n 1h "莫妮卡！你能不能告诉纱世里--"
    n 1c "--诶？"
    "夏树环视了一下。"
    "莫妮卡并不在部室。"
    n 4q "呃..."
    n "话说，莫妮卡去哪了？"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "好问题..."
    y "她和你们说过今天会迟到之类的吗？"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "没有..."
    show sayori zorder 2 at t32
    mc "嗯，我也不知道。"
    show yuri zorder 3 at f33
    y 2l "唔..."
    y "那可有点反常。"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "希望她没事..."
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "她肯定没事。"
    n "可能她只是今天刚好有事情要做。"
    n 3t "毕竟她还是蛮受欢迎的..."
    show natsuki zorder 2 at t31
    show sayori 4m zorder 3 at f32
    s "诶？"
    s "你该不会觉得她..."
    s "她有个...！"
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "啊哈哈，那也不奇怪嘛。"
    y "她可能比我们大家加起来都有魅力。"
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "诶嘿嘿，就是嘛..."
    show sayori zorder 2 at t32
    show natsuki 1p zorder 3 at f31
    n "哪跟哪啊喂？！"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "突然，门被猛地拉开了。"
    show monika 1g at l41
    m "抱歉！非常抱歉！"
    mc "啊，你来了..."
    m "我真不是有意迟到的..."
    m "希望你们没有担心我之类的！"
    show sayori 4n zorder 3 at f42
    s "诶？？"
    s "莫妮卡最终在社团和男朋友之间选择了社团！"
    s "你的意志力真强！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 1l "男-男朋友...？"
    m "你们到底在说什么？"
    "莫妮卡疑惑地看向我。"
    show monika zorder 2 at t41
    mc "啊，当我们没说..."
    mc "话说回来，你是被什么事情耽误了吗？"
    show monika zorder 3 at f41
    m 1e "啊..."
    m "嗯，今天的上一段时间是自习课。"
    m "说实话，我忘了注意时间..."
    m "啊哈哈..."
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "那也没道理啊。"
    n "你至少应该听到下课铃了吧。"
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "那一定是因为被我练钢琴的声音盖过去了..."
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "钢琴...？"
    y "我之前还不知道你会弹钢琴，莫妮卡。"
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "啊，其实也不算会弹...！"
    m "我最近才开始学。"
    m 1m "我一直都蛮想学钢琴的。"
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "真好啊！"
    s "给我们弹些什么吧，莫妮卡！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "这..."
    "莫妮卡看向了我。"
    m 1a "也许等到我弹得稍微好点了，再弹给大家听吧。"
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "耶～！"
    show sayori zorder 2 at t42
    mc "听起来好厉害。"
    mc "我很期待哦。"
    show monika zorder 3 at f41
    m 1b "真的吗？"
    m "这样的话..."
    m "我不会让你失望的，[player]。"
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "莫妮卡甜甜地笑着。"
    mc "啊..."
    mc "我不是想给你压力什么的！"
    m 1a "啊哈哈，别担心。"
    m "我最近练习得挺多的。"
    m "我也很乐意在我准备好之后能有机会分享。"
    mc "我明白了..."
    mc "这样的话，祝你好运。"
    m 1j "谢谢～！"
    m 1a "话说，我没有错过什么吧？"
    mc "没...没什么。"
    show monika zorder 1 at thide
    hide monika
    "我选择了略过纱世里的调皮恶作剧。"
    "不过我敢肯定，夏树最后会向她抱怨的。"
    "看起来大家都已经安定下来了。"
    "纱世里竟然已经吃完了整块曲奇。"
    "优里回到了书前，而夏树也消失在了储藏间里。"



    $ nextscene = poemwinner[1] + "_exclusive_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene



    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "好了，各位！"
    m "我们都已经读完彼此的诗了，是吧？"
    m "我们今天需要商量点事，请大家都坐到房间的前面来..."
    show natsuki 3c zorder 3 at f31
    n "是关于学园祭吗？"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "嗯，差不多～"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "呃。我们真的必须准备学园祭吗？"
    n "我们似乎没办法在短短几天内，就拼凑出什么像样的东西来啊。"
    n "可能到头来，我们只会变得很难堪，而不是吸引到新成员的加入。"
    show yuri 2g zorder 3 at f33
    show natsuki zorder 2 at t31
    y "我也有这种担心呢。"
    y "我并不擅长临时抱佛脚..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "别这么担心！"
    m "我们就简单地来，好吗？"
    m 1a "只要进行一些装饰就够了。"
    m "纱世里已经在做海报了，我也做了一些我们能在赏诗会期间用的诗册。"
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "好吧，很不错，但也就这样了..."
    n "况且你都没有说明白，在赏诗会上，我们到底要做些什么啊。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "啊，抱歉！我还以为你已经听说了。"
    m 1b "我们要进行表演！"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3h "表演？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "表..."
    y 3o "唔，莫妮卡..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1k "没错！我们要进行一次诗朗诵表演。"
    m 1b "我们每个人都要选一首赏诗会上朗诵的诗。"
    m "不过最棒的部分是，我们也会提供给访客作诗并且朗诵的空间！"
    m 1a "或许有些人会想要事先准备，所以纱世里会在海报上声明这一点。"
    show yuri zorder 2 at t44
    show monika zorder 2 at t43
    show natsuki zorder 2 at t42
    show sayori 4q at l41
    s "诶嘿嘿～"
    "纱世里一直在给一张海报上色，她把它拿起来给我们看了看。"
    show natsuki 4w zorder 3 at f42
    n "你是在开玩笑吗，莫妮卡？"
    n "你不会...你不会已经把这些海报贴出去了吧？"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1d "诶？是啊，我贴了..."
    m "你们真的觉得这个主意有那么糟吗...？"
    show monika zorder 2 at t43
    show natsuki 1s zorder 3 at f42
    n "好吧，倒也不是。"
    n "这个主意也不算糟。"
    n 1w "但是我没有报名参加过！"
    n 1x "我 {i}绝不{/i} 可能像那样在一大群人面前进行表演！"
    show natsuki zorder 2 at t42
    show yuri zorder 3 at f44
    y 3r "我...我同意夏树！"
    y 3w "我这辈子...也不会...做那样的事情..."
    "想到这里，优里害怕地摇了摇头。"
    show yuri zorder 2 at t44
    show sayori 1g zorder 3 at f41
    s "各位..."
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 1g "别了，纱世里..."
    m "我理解她们心里在想什么。"
    m "要知道几天前，夏树和优里还从来没有跟别人分享过她们的诗..."
    m "让她们当着一屋子的人大声朗诵自己的诗确实要求太高了。"
    m 1r "我想，我大概是忽略了这一点。"
    m "所以，我很抱歉。"
    show monika zorder 2 at t43
    show natsuki 5g zorder 3 at f42
    n "..."
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1i "...但是！"
    m "我还是觉得我们应该竭尽全力！"
    m 1d "这个社团的命运只能靠我们自己！"
    m "如果我们成功举办了赏诗会，并且演出效果不错的话..."
    m 3a "那么就会启发别人也这么做！"
    m "表演的人越多，我们就越能向大家展示文学是什么！"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "是的!"
    s 1x "只要表达出你们的感情..."
    s "对自己坦诚..."
    s "发现新的视界..."
    s "然后享受就行了！"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 4b "没错！"
    m "正是由于这些原因，我们今天才会在这个社团里。"
    m 4e "你不想和他人分享吗？"
    m "启发他们找到当初同样把你带到这里的感情？"
    m 1e "我知道你们想。"
    m "我知道我们都想。"
    m 1b "而如果我们要做的只是站在房间前用两分钟朗诵一首诗..."
    m "...那么我知道你们可以做到的！"
    show monika 1a zorder 2 at t43
    show natsuki 5s zorder 3 at f42
    n "..."
    show natsuki zorder 2 at t42
    show yuri 4b zorder 3 at f44
    y "..."
    show yuri zorder 2 at t44
    show sayori 1g
    "夏树和优里沉默不语。"
    "纱世里看起来有些担心。"
    "我觉得我别无选择..."
    mc "我同意..."
    mc "我并不觉得这样的要求很过分。"
    mc "纱世里和莫妮卡一直在非常努力地吸引新成员。"
    mc "我觉得我们至少应该帮她们一点。"
    show natsuki zorder 3 at f42
    n 5h "好吧...也许是吧，但是..."
    n "..."
    "似乎夏树也没有什么可以反驳的了。"
    n "唔..."
    n 1q "...好吧，好吧！"
    n "我想我会克服一下的。"
    show natsuki zorder 2 at t42
    show sayori zorder 3 at f41
    s 4r "好的～！"
    show sayori 4a zorder 2 at t41
    show monika zorder 3 at f43
    m 1e "呼..."
    m "谢谢你，夏树。"
    m "那你呢，优里...？"
    show monika zorder 2 at t43
    show yuri zorder 3 at f44
    y "..."
    "优里郁闷地看着周围其他所有人满怀期待的脸。"
    y "唉..."
    y "我-我觉得我别无选择..."
    show yuri zorder 2 at t44
    show sayori zorder 3 at f41
    s 4r "啊哈哈！那就是所有人都参加咯！"
    s "你最好了，优里～"
    show sayori 4a zorder 2 at t41
    show yuri zorder 3 at f44
    y "这个社团真的会逼死我的..."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 1l "哦天啊..."
    m 1n "没事的，优里。"
    m "不过话说回来..."
    m 1b "我们开始准备赏诗会吧！"
    m "我希望你们每个人都选一首自己的诗。"
    m "我们会在彼此面前练习朗诵。"
    show monika 1a zorder 2 at t43
    show natsuki zorder 3 at f42
    n 1p "不-不-不要！！"
    show natsuki zorder 2 at t42
    show yuri 3n zorder 3 at f44
    y "莫妮卡...！"
    y "这太突然了...！"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "嗯，如果你们连在社团成员面前都不能朗诵的话，那么在陌生人面前又怎么可能做得到呢？"
    show monika zorder 2 at t43
    show yuri 4c zorder 3 at f44
    show natsuki 1o
    y "哦不..."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "别担心。"
    m "我会第一个开始，这样能让你们感觉更放松一些。"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "我能下一个吗？？"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m "啊哈哈。当然可以。"
    m 2d "那么，我看看..."
    "莫妮卡将笔记本快速翻到她脑海中想好的那首诗上。"
    "然后她就站在了讲台后面。"
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    m 1a "这首诗的题为 {i}飞翔的方式{/i}。"
    m 1r "嗯咳..."
    show monika 1a
    "莫妮卡开始朗诵她的诗。"
    "她那清晰又自信的声音充满了整个房间。"
    "不仅如此，她的转音也非常朴素。"
    "她知道如何在朗诵的每一行中加入感情，给文字带来生气。"
    "她之前就朗诵过吗，还是说她天生如此？"
    "我朝周围看了看。"
    "所有人的视线都放在莫妮卡身上。"
    "纱世里看起来很吃惊。"
    "优里脸上带着我不能理解的紧张表情。"
    show monika 1j
    "终于，莫妮卡完成了朗诵。"
    "我们四个都鼓起了掌。"
    "莫妮卡做了个深呼吸并微笑着。"
    show monika 1a
    show sayori 4m zorder 3 at f33
    s "这...这真棒啊，莫妮卡！"
    show sayori zorder 2 at t33
    show monika zorder 3 at f32
    m 1j "啊哈哈，非常感谢。"
    m 1a "希望我树立了一个好的榜样。"
    m "准备好下一个上了吗，纱世里？"
    show monika zorder 2 at t32
    show yuri 2r at l31
    y "下...下一个让我来！！"
    show sayori at h33
    s 1n "哇！优里突然被激发了！"
    "优里手中攥着一张纸，站了起来。"
    "她低着头快速走向讲台。"
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    show yuri zorder 2 at t11
    hide monika
    hide sayori
    y 2v "这首诗的题目是--！"
    "优里紧张地看着我们。"
    s "你可以做到的，优里..."
    y "它...它叫做...{i}绯红眼眸之影{/i}。"
    "优里开始朗诵诗，声音有些颤抖。"
    "就在刚刚，她还特别抗拒这么做。"
    "为什么她突然之间变得这么努力？"
    show yuri 2l
    "优里在读过开头的几行后，声音发生了变化。"
    "就和优里沉浸到书本里的情况一样。"
    "她颤抖的话语变成了热烈而自信的女性锐利声线。"
    "诗词在结构上充满了清晰完美的跌宕起伏。"
    "这是一次难得可以窥见优里一直封存着的胸中丘壑的机会...！"
    show yuri 2t
    "她的朗诵戛然而止。"
    "每个人都呆住了。"
    "优里猛然回到了现实中，环顾四周，似乎自己也很困惑。"
    y 3o "我..."
    "...看来需要我来救场了。"
    "我带头鼓起了掌。"
    "大家都随后鼓掌起来，给了优里应得的认可。"
    "刚刚的我们并不是不想为她鼓掌。"
    "而是因为我们太措手不及，以至于都忘记了。"
    "伴随着我们的掌声，优里把诗放到胸前，跑回到自己的座位上。"
    show yuri at lhide
    hide yuri
    show monika 1a zorder 2 at t11
    m "优里，非常棒。"
    m "谢谢你的分享。"
    y "..."
    "似乎优里已经筋疲力尽了..."
    show sayori 1q zorder 2 at t31
    s "好啦～"
    s "那我想，下一个就是我了！"
    "纱世里从座位上跳了起来，兴高采烈地走向讲台。"
    show sayori zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    s 1x "这首诗叫做...{i}我的草地{/i}。"
    s "啊..."
    s 1s "...啊哈哈!"
    s 4s "不好意思，我刚刚傻笑了..."
    s 4q "诶嘿嘿..."
    mc "纱世里..."
    s 1l "比我想象中要难好多啊！"
    s "你们是怎么能那样简简单单地做到的？"
    show monika 3a zorder 2 at t31
    show sayori 1b
    m "啊..."
    m "尝试着不要想你是在给别人朗诵。"
    m "想象你在给你自己朗诵，就像站在镜子面前或者默诵一样。"
    m "这是你的诗，所以这样做的效果会最好。"
    show sayori 1i
    s "明白了，明白了..."
    s "好的，那么..."
    show monika zorder 1 at thide
    hide monika
    show sayori 1c
    "纱世里开始了朗诵。"
    "不知怎地，她温柔的声音感觉起来非常相配。"
    "诗并没有像纱世里本人那样无忧无虑地欢快。"
    "而是安宁而又苦乐参半的。"
    "如果我是在纸上读到这首诗，可能我不会想到这么多..."
    "但是听到纱世里用她的声音读出来时，它就有了全新的含义。"
    "可能这就是纱世里说她喜欢我的诗的时候，她的真实意思吧。"
    "对于这个我本以为完全了解的人，我好像有了更深入的了解。"
    "纱世里读完了，我们鼓起了掌。"
    s 3q "我做到了～！"
    mc "做得不错，纱世里！"
    s "诶嘿嘿，连 [player] 都喜欢哦。"
    s "我觉得这是一个不错的预兆～"
    mc "你在说什么呀...？"
    show monika 2b zorder 3 at f31
    m "效果非常让人满意，纱世里。"
    m "诗的基调相当适合你。"
    m "不过，如果其它诗也这么读的话，可能效果会逊色一点..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "诶？我不是很明白..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "换句话说，我看过你的另一些诗，它们不太适合这样温柔的表达方式。"
    m "取决于你读的内容，它们可能需要更多力度来支撑..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1x "哦，我懂你的意思了！"
    s "就是...嗯，我已经在这样练习了..."
    s 5 "只不过站在大家面前有些难为情而已..."
    s "诶嘿嘿..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 4a "那下一次，我可是要让你选一首更有挑战性的诗哦。"
    m "我们在学园祭之前没多少时间了，你知道的吧？"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "好...吧。"
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "那么，下一个谁来...？"
    m "夏树？"
    show natsuki 5s zorder 3 at f33
    show monika zorder 2 at t31
    n "哼。"
    n "不要把我排在 [player] 之前。"
    n "不管怎么说，我都没法跟你们相比..."
    n "在我之前，让 [player] 来降低一点大家的标准吧。"
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "夏树..."
    show sayori zorder 2 at t32
    mc "没事，没事。"
    mc "我也想尽快搞定。"
    mc "但是好像我在读什么内容上没有太多的选择..."
    mc "那我就读我为今天写的诗吧。"
    "我站起来，走到了讲台前。"
    show natsuki 2c zorder 2 at t44
    show sayori 1a zorder 2 at t43
    show monika 1a zorder 2 at t42
    show yuri 1e zorder 2 at t41
    "大家都看着我，让我感到特别地尴尬。"
    "我朗诵了我的诗。"
    "由于我对自己的作文水平不是非常有信心，以至于我很难将自己的感情融入进去。"
    "但尽管如此，在读完的时候，我还是获得了掌声。"
    mc "抱歉，我表现得没大家那么好..."
    show monika zorder 3 at f42
    m 1a "别太担心。"
    m "我觉得能力不是关键，更关键的是你对作文水平缺乏信心。"
    m "不过这是会随着时间不断进步的。"
    show monika zorder 2 at t42
    mc "嗯...也许吧。"
    show monika zorder 3 at f42
    m 1j "好了，接下来！"
    m 1a "只剩下你了，夏树。"
    show monika zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2g "好吧，好吧。"
    n "我这就来。"
    "夏树不情愿地离开座位，走向了讲台。"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at t11
    hide sayori
    hide monika
    hide yuri
    n 2c "诗的名字叫做..."
    n 2q "它叫做..."
    n 1x "你-你们都盯着我干嘛？！"
    m "因为是你在展示啊..."
    n 2x "哼..."
    n 2h "算了...诗名叫 {i}跳跃{/i}。"
    "夏树吸了口气。"
    show natsuki 2c
    "开始朗诵后，她的别扭态度稍微消散了一些。"
    "虽然她还有些不情愿，但是诗还是有韵律的。"
    "这就是夏树特有的风格，在大声朗读情况下，表现出人意料地好。"
    "词语如若在空中跃动，似乎给诗赋予了生命。"
    show natsuki 2s
    "夏树读完了，大家都鼓掌起来。"
    "她气鼓鼓地回到了座位上。"
    show monika 2a zorder 3 at f31
    m "还不错啊，是吧？"
    show monika zorder 2 at t31
    show natsuki 5w zorder 3 at f32
    n "你说起来容易..."
    n "你可别强迫我再来一次了。"
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f31
    m "啊，好啦..."
    m "那你至少对在他人面前朗诵有些心理准备了吧？"
    show monika zorder 2 at t31
    show natsuki 2c zorder 3 at f32
    n "那是，在别人面前问题倒简单多了！"
    n "对着别人我可以用随便什么样的脸色。"
    n 2q "但是在朋友面前..."
    n "真的很...难为情。"
    show natsuki zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "真意外啊，夏树..."
    s "我觉得对我来说恰恰相反。"
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    n "好吧，事实就是这样的，所以..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "嗯，这样的话我觉得..."
    m "你就不用太担心自己在学园祭的表现了。"
    m 2b "既然这样，我要感谢大家的参与。"
    m "虽然可能会有点难，不过我希望大家对现在是什么样的情况都能心里有数。"
    m 4b "保证能在学园祭之前选好一首诗并且进行足够的练习，可以吗？"
    m "我会去做诗册，所以请事先告诉我你们要朗诵的是什么。"
    show monika zorder 2 at t31
    mc "天哪..."
    mc "我大概需要找些其它的诗来朗诵。"
    show monika zorder 3 at f31
    m 1j "那也可以啊！"
    m 1a "不是自己的诗也可以。"
    m "你能为社团做出这样的努力已经很让我惊喜了。"
    m 5 "我真的很高兴。"
    show monika zorder 2 at t31
    mc "啊...好的，没问题..."
    play music t8 fadeout 1.0
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    m 4b "好了，各位！"
    m "今天就到这里。"
    m "我知道学园祭快到了，但是我们同样要试着为明天写首诗。"
    m "至今为止的效果都非常棒，所以我想将它继续下去。"
    m "而关于学园祭，我们会在明天完成规划，然后用周末的时间来进行准备。"
    m "星期一就是关键的一天了！"
    show sayori 4r zorder 2 at t31
    s "我都等不及啦～！"
    show yuri 4b zorder 2 at t33
    y "我能做到的...我能做到的..."
    mc "好吧--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "我站了起来。"
    "虽然做不到像纱世里和莫妮卡一样热忱，但是我也应该尽我所能。"
    "如果是为了社团..."
    "还有给莫妮卡留下好印象..."
    "那么我就必须要竭尽全力。"
    show sayori 1a zorder 2 at t32
    mc "准备好走了吗，纱世里？"
    show sayori at h32
    s 1x "嗯！"
    show natsuki 2d zorder 3 at f33
    n "看看你们俩，总是就这样一起回家。"
    show monika 5 zorder 3 at f31
    show natsuki zorder 2 at t33
    m "都让我有点羡慕了，不是吗？"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "诶嘿嘿～"
    show sayori zorder 2 at t32
    mc "天哪，各位..."
    mc "别太小题大作了。"
    show natsuki zorder 2 at t44
    show sayori zorder 2 at t43
    show monika zorder 2 at t42
    show yuri 1u zorder 3 at f41
    y "但感觉肯定也不错啊..."
    show yuri zorder 2 at t41
    mc "好吧..."
    mc "啊..."
    "我应该怎么回应？"
    show sayori zorder 3 at f43
    s 1d "没关系的，[player]，你不必说出来。"
    show sayori zorder 2 at t43
    mc "...算了。我们走吧。"
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori":
        $ ch2_winner = "Yuri"

    if ch2_winner == "Yuri":
        $ ch2_winner_chs = "优里"
    elif ch2_winner == "Natsuki":
        $ ch2_winner_chs = "夏树"
    
    "我又一次和纱世里走回了家。"
    "虽然只有短短的几天时间，很多事情都已经改变了。"
    "但是今天，纱世里在回家路上比往常要更安静一些。"
    mc "嘿，纱世里..."
    show sayori 1k at t11
    s "..."
    s 1n "...对不起！我走神了！"
    mc "啊，怪不得..."
    s 1d "呃..."
    s "我刚刚...在想之前的事情。"
    s "我在想我们如何变得..."
    s 1y "我-我的意思是..."
    "纱世里笨拙地组织着语言。"
    s 1a "就是...假设有一天，[ch2_winner_chs]提出要跟你一起回家..."
    mc "嗯？！"
    s "你会怎么做？"
    mc "这是个什么问题....？"
    mc "你可把我难住了..."
    s 1y "诶嘿嘿..."
    menu:
        "好吧..."
        "我会和[ch2_winner_chs]一起走回家。":
            if ch2_winner == "Natsuki":
                call ch2_end_natsuki
            else:
                call ch2_end_yuri
        "我仍然会和纱世里一起走回家。":
            call ch2_end_sayori

    "话又说回来，距离学园祭只剩下几天了..."
    "谁知道到时候会发生什么呢？"
    return
label ch2_end_sayori:
    mc "纱世里..."
    mc "你真的觉得我会抛下你而选择[ch2_winner_chs]吗？"
    s 1e "诶？！"
    s "但-但是..."
    if ch2_winner == "Natsuki":
        s "她那么可爱有趣..."
    else:
        s "她那么漂亮聪明..."
    mc "天哪..."
    mc "我已经能天天在社团看到她了。"
    mc "除此之外，你似乎也很喜欢和我一起回家..."
    mc "我不会毁了它的。"
    s 1y "你真傻，[player]..."
    s "有些时候，你太为我着想了。"
    s "如果[ch2_winner_chs]想的话，那也是她应得的，所以..."
    mc "纱世里，我已经下定决心了。"
    mc "我有时候真的不能理解你..."
    s "对不起..."
    mc "还有，假设一件永远都不会发生的事情有意义吗？"
    s 1k "唔..."
    show sayori at thide
    hide sayori
    "对话停了下来。"
    "真的很奇怪，纱世里居然会对这件事情如此在乎..."
    "但我也想尊重她并且让她开心。"
    return

label ch2_end_natsuki:
    mc "和夏树一起走回家，唔..."
    "为什么这个想法让我心跳不已...？"
    mc "我是说..."
    mc "我觉得如果我让她失望的话，我不知道会被她怎么样..."
    s 1x "不是因为她可爱有趣吗？"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "和优里一起走回家，唔..."
    "为什么这个想法让我心跳不已...？"
    mc "我是说..."
    mc "看到她在社交方面上这么努力，如果让她失望的话我会感到很内疚，所以..."
    s 1x "不是因为她漂亮聪明吗？"
    jump ch2_end_shared

label ch2_end_shared:
    mc "我可完全没有这个意思！"
    s 4s "啊哈哈！你承认了！"
    mc "天哪..."
    mc "假设一件永远都不会发生的事情根本没有任何意义。"
    s 1d "好吧，可能是吧..."
    s "但是我就是喜欢想一想。"
    s 1y "很快你就不再需要我了，对吧？"
    mc "需要你...？"
    mc "纱世里..."
    mc "我理解不了你对这些事的想法。"
    s "对不起..."
    mc "每个人都是不同的..."
    mc "社团里的人没有一个是你的替代品。"
    s 1k "唔..."
    s "也许吧..."
    show sayori at thide
    hide sayori
    "对话停了下来，我只觉得很尴尬。"
    "可是用这样一个奇怪的问题困扰我，某种程度上也是她的错..."
    "我只是不能对她撒谎。"
    "我非常不乐意从她身边夺走那些可以让她开心的事情。"
    "这就是为什么我会说，假设是没有意义的。"
    return

