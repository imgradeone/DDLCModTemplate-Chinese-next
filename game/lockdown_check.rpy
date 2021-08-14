# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users and such about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher than the
# one the mod template was tested for.
## 请 勿 修 改 该 文 件 ！ ！ ！

label lockdown_check:
    if renpy.version_tuple >= (7, 4, 6, 1693):
        scene black
        "{b}警告！{/b} 近期 Ren'Py 7.4.6 的严重 bug 会导致 DDLC 转场彻底损坏。"
        "该 bug 目前在 Ren'Py SDK 7.4.7 及更高版本中仍有残余。"
        "目前，这个 bug 尚且没有完全修复，因此，DDLC 中文 Mod 模板 Next 已经禁止在任何高于 7.4.6 版本的 SDK 中制作 Mod，直到问题改善。"
        "如需了解该 bug 的信息，请访问 {a=https://github.com/renpy/renpy/issues/2860}GitHub 的该 Issue 页面{/a}。"
        "目前，如果您想制作 DDLC Mod，请您暂时将 Ren'Py 降级至 {a=https://www.renpy.org/release/7.4.5}7.4.5 版本{/a}，并等待上游的 GanstaKingofSA 完成测试。"
        "抱歉给您带来不便，希望您保持开心，快乐 Modding。"
        $ renpy.quit()
    else:
        $ persistent.lockdown_warning = True
        return