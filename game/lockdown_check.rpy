# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users and such about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher than the
# one the mod template was tested for.
## DO NOT MODIFY THIS FILE!

label lockdown_check:
    if renpy.version_tuple == (7, 4, 6, 1693):
        scene black
        "{b}警告！{/b} 近期 Ren'Py 7.4.6 的严重 bug 会导致 DDLC 转场彻底损坏。"
        "目前，这个 bug 尚且没有任何修复补丁，因此，DDLC 中文 Mod 模板 Next 已经禁止在该版本 SDK 中制作 Mod，直到问题改善。"
        "如需了解该 bug 的信息，请访问 {a=https://github.com/renpy/renpy/issues/2860}GitHub 的该 Issue 页面{/a}。"
        "目前，如果您想制作 DDLC Mod，请您暂时将 Ren'Py 降级至 {a=https://www.renpy.org/release/7.4.5}7.4.5 版本{/a}，并等待上游的 GanstaKingofSA 完成测试。"
        "抱歉给您带来不便，希望您保持开心，快乐 Modding。"
        $ renpy.quit()
    elif renpy.version_tuple >= (7, 4, 5, 1621) and renpy.version_tuple != (7, 4, 6, 1693) and not persistent.lockdown_warning:
        scene black
        "{b}警告！{/b} DDLC 中文 Mod 模板 Next 检测到您目前使用的 Ren'Py SDK 未经过测试。"
        "目前为止，上游的 Mod 模板仅在 {a=https://www.renpy.org/release/7.4.5}Ren'Py SDK 7.4.5 版本{/a} 经过测试。"
        "如果您想在当前版本的 Ren'Py SDK 上开发 Mod，您可能会遇到兼容性问题与错误。"
        menu:
            "如果您同意使用该版本的 Ren'Py SDK 进行 Mod 开发，则意味着您能接受未知的兼容性 bug。"
            "我同意。":
                $ persistent.lockdown_warning = True
                "您现在已经同意，可以继续 Mod 开发了。You have agreed to this disclaimer. You may now proceed to mod DDLC under this version of Ren'Py. Happy modding!"
                return
            "我不同意。":
                "您选择了不同意，因此 DDLC 中文 Mod 模板将暂时停止在该版本 Ren'Py SDK 下工作，除非重新同意。"
                "如果您仍然希望开发 Mod，您应该暂时选择 {a=https://www.renpy.org/release/7.4.5}Ren'Py SDK 7.4.5 版本{/a}。"
                "如果您想选择重新同意该协议，那么您可以重新在该版本 SDK 下运行 Mod 模板，再次选择。"
                "抱歉给您带来不便，希望您保持开心，快乐 Modding。"
                $ renpy.quit()
    else:
        $ persistent.lockdown_warning = True
        return