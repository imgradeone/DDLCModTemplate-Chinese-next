# Lockdown_check.rpy - 兼容性警告

# 本文件并非来源于 DDLC。
# 用于检测 Ren'Py SDK 版本兼容性，并对不兼容版本做出警告 / 拦截。
## 请 勿 修 改 该 文 件 ！ ！ ！

label lockdown_check:

    $ version = renpy.version()

    # if renpy.version_tuple >= (7, 4, 6, 1693) and renpy.version_tuple < (7, 4, 9, 2142): # 不再阻止 7.4.6 - 7.4.9，毕竟有补丁了

    #     scene black
    #     "{b}警告！{/b} Ren'Py 7.4.6 的严重 bug 会导致 DDLC 转场彻底损坏。"
    #     "该 bug 目前在 Ren'Py SDK 7.4.7 及更高版本中仍有残余。"
    #     "如果您想使用 Ren'Py 7 制作 DDLC Mod，请您暂时将 Ren'Py 降级至 {a=https://www.renpy.org/release/7.4.5}7.4.5 版本{/a}，或者更新至 {a=https://renpy.org/release/7.4.9}7.4.9{/a} 或 {a=https://renpy.org/release/7.4.10}7.4.10{/a} 版本。"
    #     "抱歉给您带来不便，希望您保持开心，快乐 Modding。"
    #     $ renpy.quit()

    if renpy.version_tuple > (7, 4, 11, 2266):
        scene black
        "{b}警告！{/b} 您目前使用的 Ren'Py SDK 未经过兼容性测试。"
        "目前为止，上游的 Mod 模板仅在 {a=https://www.renpy.org/release/7.4.11}Ren'Py SDK 7.4.11 版本{/a} 经过测试。"
        "如果您想在当前版本的 Ren'Py SDK 上开发 Mod，您可能会遇到兼容性问题与错误。"
        menu:
            "如果您同意使用该版本的 Ren'Py SDK 进行 Mod 开发，则意味着您能接受未知的兼容性 bug。"
            "我同意。":
                $ persistent.lockdown_warning = True
                return
            "我不同意。":
                "您选择了不同意，因此 DDLC 中文 Mod 模板将暂时停止在该版本 Ren'Py SDK 下工作，除非重新同意。"
                "如果您仍然希望开发 Mod，您应该暂时选择 {a=https://www.renpy.org/release/7.4.11}Ren'Py SDK 7.4.11 版本{/a}。"
                "如果您想选择重新同意该协议，那么您可以重新在该版本 SDK 下运行 Mod 模板，再次选择。"
                "抱歉给您带来不便，希望您保持开心，快乐 Modding。"
                $ renpy.quit()

    else:
        $ persistent.lockdown_warning = True
        return
