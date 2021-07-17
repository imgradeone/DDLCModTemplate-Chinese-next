# DDLC 中文 Mod 模板 2.0
嘿，你~~又~~想用中文写 DDLC Mod？**那你来对地方了！**

这是**新的** DDLC 中文 Mod 模板！本模板基于 GanstaKingofSA 的 DDLC Mod Template 2.0，并进行了 [旧版](https://github.com/imgradeone/DDLCModTemplate-Chinese) 已经进行的一系列汉化。使用本模板制作 Mod 时，请遵循 Team Salvato 的 [IP Guidelines](https://revolution.dokimod.cn/ipguidelines.html)。

当前版本的模板支持 Ren'Py SDK 6.99.12 及 7.4.5。

**本模板是为使用原版 DDLC 素材的饭制游戏和 Mod（而并非不使用原版素材的作品）设计的，提供源代码也并非以便将其复制粘贴到和 DDLC 没有关系的工程。此模板内大部分代码属于 Team Salvato 的知识产物，请遵循 Team Salvato 的 [IP Guidelines](https://revolution.dokimod.cn/ipguidelines.html) 使用，否则后果自负。**

**如果你是 Mod 作者，请不要将 DDLC 游戏本体包含在你分发的 ZIP 里，这是违反 IP Guidelines 的行为。**

> 本 Mod 模板不支持 Doki Doki Literature Club Plus。

> 请注意：本模板可能尚不完善，且尚缺乏繁体中文支持。部分 GUI 元素暂未被汉化。

> 此模板自带 Android 支持，详情请看原版 DDLC Mod Template 2.0 所附带的 `guide.pdf`，或在稍晚时候访问 [DokiMod 开发文档](https://docs.dokimod.cn) 了解 Android Mod 制作方式。

您可以查看 [更新日志](CHANGELOG.md)。

## 开始制作 Mod

### 中文字体

DDLC 中文 Mod 模板使用了一些免费商用的中文字体，在此致谢。**开始 Mod 开发前，请务必下载这些字体，否则将无法启动工程。安装方式见 [中文字体包安装](#中文字体包安装) 小节。**

如有需要，您也可以自行修改配置文件，以自定义字体，**但请自主承担版权风险**。

中文字体详情请查看 [这里](./game/mod_assets/font/README.md)

#### 中文字体包安装

> 请注意：我们仍然建议您从各个字体的官网下载这些字体，即便它们都是免费商用字体。

您可以下载懒人专用字体包，下载完后将字体解压到 `game/mod_assets/font` 目录下即可。

请在 https://revolution.dokimod.cn/modtemplate/chinesefonts/ 获取字体包。

---

### 使用 Ren'Py SDK 6 进行 Mod 开发
1. 下载并运行 [Ren'Py SDK 6.99.12](https://www.renpy.org/release/6.99.12)。  
    > 请注意：DDLC 不兼容新版 Ren'Py，除非游戏后续更新，当然这不意味着您不能使用 Ren'Py SDK 7 进行 Mod 制作。
1. 前往 Releases 页面获取 [模板的最新版本](https://github.com/imgradeone/DDLCModTemplate-Chinese-next/releases)。（目前 Mod 模板暂无稳定版本，您可以使用 GitHub 的 `Use this template` 创建新工程）
1. 从 [DDLC.moe](https://ddlc.moe) 或者 [Steam](https://store.steampowered.com/app/698780/) 下载 DDLC 游戏，然后将 `DDLC-1.1.1-pc` 文件夹（对于 macOS 用户则为 `ddlc-mac`，对于 Steam 版本则为 `Doki Doki Literature Club`）复制到 Ren'Py SDK（`renpy-6.99.12.4-sdk`）文件夹（或者您在 Ren'Py SDK 中自定义的文件夹）。将文件夹重命名为您的 Mod 名称。
1. 将 Mod 模板 ZIP 包内的内容复制到您刚刚粘贴的 DDLC 文件夹内。如有提示，请允许替换所有文件。  
    > 对于 macOS，请右键单击 `ddlc-mac` 文件夹内的 DDLC.app，点击 `显示包内容`，然后将 `Contents/Resources/autorun` 文件夹内的文件复制过去。如有提示，请允许替换所有文件。  
1. 下载 [中文字体包](https://revolution.dokimod.cn/modtemplate/chinesefonts/)，将下载的 ZIP 文件的内容解压并复制到 `<Mod 工程文件夹>/game/mod_assets/fonts` 文件夹。
1. 在 Ren'Py SDK 里启动项目。它应正常编译并启动游戏。
    > 有时候，启动项目可能不会发生任何事情，或者报错。您可以再次单击 `Launch Project` / `运行工程` ，此时工程应该可以正常启动。
1. 当你完成脚本编写后，转到 Ren'Py SDK 主界面，选择 `Build Distributions` / `生成分发版`。将 `Build Packages` / `生成分发包` 中的其他选项全部取消，仅选中 `Ren'Py 6 DDLC Compliant Mod`，然后点击 `Build` / `生成`。这个操作会生成跨平台的 ZIP 文件，这就是你的 Mod 文件。

### 使用 Ren'Py SDK 6 进行 Mod 开发
1. 下载并运行 [Ren'Py SDK 7.4.5](https://www.renpy.org/release/7.4.5)。
    > 请注意：使用 Ren'Py 7 构建的 Mod 不兼容 Ren'Py 6。我们也会跟进上游的变动，以完美适配最新的 Ren'Py SDK。目前 Ren'Py SDK 7.4.6 有破坏性改动，会导致 DDLC 转场失效，请暂时不要更新 SDK！！！
1. 前往 Releases 页面获取 [模板的最新版本](https://github.com/imgradeone/DDLCModTemplate-Chinese-next/releases)。（目前 Mod 模板暂无稳定版本，您可以使用 GitHub 的 `Use this template` 创建新工程）
1. 从 [DDLC.moe](https://ddlc.moe) 或者 [Steam](https://store.steampowered.com/app/698780/) 下载 DDLC 游戏，然后将 `DDLC-1.1.1-pc` 文件夹（对于 macOS 用户则为 `ddlc-mac`，对于 Steam 版本则为 `Doki Doki Literature Club`）复制到 Ren'Py SDK（`renpy-<version>-sdk`）文件夹（或者您在 Ren'Py SDK 中自定义的文件夹）。将文件夹重命名为你的 Mod 名称。
1. 将 Mod 模板 ZIP 包内的内容复制到您刚刚粘贴的 DDLC 文件夹内。如有提示，请允许替换所有文件。  
    > 对于 macOS，请右键单击 `ddlc-mac` 文件夹内的 DDLC.app，点击 `显示包内容`，然后将 `Contents/Resources/autorun` 文件夹内的文件复制过去。如有提示，请允许替换所有文件。  
    > 在 Ren'Py SDK 7 中，如果遇到意外启动失败，可能是因为 `game/scripts.rpa` 的冲突，您可以尝试删除该文件。
1. 下载 [中文字体包](https://revolution.dokimod.cn/modtemplate/chinesefonts/)，将下载的 ZIP 文件的内容解压并复制到 `<Mod 工程文件夹>/game/mod_assets/fonts` 文件夹。
1. 在 Ren'Py SDK 里启动项目。它应正常编译并启动游戏。
    > 有时候，启动项目可能不会发生任何事情，或者报错。您可以再次单击 `Launch Project` / `运行工程` ，此时工程应该可以正常启动。
1. 当你完成脚本编写后，转到 Ren'Py SDK 主界面，选择 `Build Distributions` / `生成分发版`。将 `Build Packages` / `生成分发包` 中的其他选项全部取消，仅选中 `Ren'Py 7 DDLC Compliant Mod`，然后点击 `Build` / `生成`。这个操作会生成跨平台的 ZIP 文件，这就是你的 Mod 文件。

### 使用 GitHub 生成新工程
您可能偏好使用 GitHub 托管 Mod 代码，或者希望更快创建工程，接下来您可以借助 GitHub 模板功能来创建您的 Mod 工程。

1. 下载并运行前序您希望使用的 Ren'Py SDK。([6.99.12](https://www.renpy.org/release/6.99.12) | [7.4.5](https://www.renpy.org/release/7.4.5)）
1. 转到 [模板的 GitHub 仓库](https://github.com/imgradeone/DDLCModTemplate-Chinese-next)，点击页面上的 `Use this template`（或者使用 [此链接](https://github.com/imgradeone/DDLCModTemplate-Chinese-next/generate)），按照指引命名 Mod 仓库，选择公开 / 私密仓库，点击 `Create repository from template`。
  > 包含所有分支（Include all branches）为可选项。
1. 借助您的 Git 客户端，克隆刚刚创建的仓库到电脑的相应文件夹（`renpy-<version>-sdk` 文件夹，或者您在 Ren'Py SDK 中自定义的文件夹）。
1. 从 [DDLC.moe](https://ddlc.moe) 或者 [Steam](https://store.steampowered.com/app/698780/) 下载 DDLC 游戏，然后将 `DDLC-1.1.1-pc` 文件夹（对于 macOS 用户则为 `ddlc-mac`，对于 Steam 版本则为 `Doki Doki Literature Club`）中的 3 个文件（`game/images.rpa`，`game/fonts.rpa`，`game/audio.rpa`）复制到 `<Mod 工程文件夹>/game` 文件夹。
    > 对于 macOS，请右键单击 `ddlc-mac` 文件夹内的 DDLC.app，点击 `显示包内容`，然后将 `Contents/Resources/autorun` 文件夹内的文件复制过去。如有提示，请允许替换所有文件。  
    > 在 Ren'Py SDK 7 中，如果遇到意外启动失败，可能是因为 `game/scripts.rpa` 的冲突，您可以尝试删除该文件。
1. 下载 [中文字体包](https://revolution.dokimod.cn/modtemplate/chinesefonts/)，将下载的 ZIP 文件的内容解压并复制到 `<Mod 工程文件夹>/game/mod_assets/fonts` 文件夹。
1. 在 Ren'Py SDK 里启动项目。它应正常编译并启动游戏。
    > 有时候，启动项目可能不会发生任何事情，或者报错。您可以再次单击 `Launch Project` / `运行工程` ，此时工程应该可以正常启动。
1. 当你完成脚本编写后，转到 Ren'Py SDK 主界面，选择 `Build Distributions` / `生成分发版`。将 `Build Packages` / `生成分发包` 中的其他选项全部取消，仅选中 `Ren'Py 7 DDLC Compliant Mod`，然后点击 `Build` / `生成`。这个操作会生成跨平台的 ZIP 文件，这就是你的 Mod 文件。

### 开始 Android Mod 移植 / 开发
您可以查阅[原版 DDLC Mod Template 2.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/blob/master/guide.pdf) 所附带的 `guide.pdf`，或在稍晚时候访问 [DokiMod 开发文档](https://docs.dokimod.cn) 了解 Android Mod 制作方式，但请遵循以下几点：

1. 对于 Ren'Py SDK 启动器内的包名，您应该以 `com.<作者>.<项目名>` 的格式命名并遵循 Android 包名规范。
  > 例如：如果您的昵称为 Yuri，项目名（`build.name`）为 Storm，那么您在 Ren'Py SDK 启动器的 `Android` -> `Configure` / `配置` 内的包名应该为 `com.yuri.storm`。

更多内容请前往 [原版 DDLC Mod Template 2.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/blob/master/guide.pdf) 所附带的 `guide.pdf` 了解。

## 模板特色功能

### DDLC Mod Template 2.0
1. 同时支持 Ren'Py SDK 6 和 7 的 Mod 构建
1. DDLC 的原版 RPY 文件，内含注释
1. 高度可定制！这个模板只是起点，借助你的创意，做你想做
1. macOS `.app` 及 Linux `.sh` 启动文件制作支持
1. 完整的 Android 支持！DDLC 的一切（除了 `[currentuser]` 变量）可在 Android 平台正常运行。
    > 请前往 [原版 DDLC Mod Template 2.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/blob/master/guide.pdf) 所附带的 `guide.pdf` 了解 Android Mod 移植 / 开发。
1. Xcode 支持！Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > 提示：您需要更改 `RENPY_TOOL` 变量，将其定位到您的 Ren'Py SDK 应用程序位置。[了解更多 &rsaquo;](XCODE.md)
1. Terra 的深度诗词游戏教程（WIP）
1. NVL 模式支持 - 特别感谢 Yagamirai01

### DDLC 中文 Mod 模板
1. 绝赞中文化（目前只支持简体中文）
2. 绝赞字体优化
3. ~~绝赞咕咕咕~~

## 特别感谢

- Team Salvato http://teamsalvato.com / https://ddlc.moe
- [GanstaKingofSA](https://github.com/GanstaKingofSA)
- 所有字体作者

## 开源许可

本 Mod 模板需要使用 Ren'Py。  
Ren'Py 的许可，请参照 https://www.renpy.cn/doc/license.html （简体中文）或 https://www.renpy.org/doc/html/license.html （英文）。

本模板基于 GanstaKingofSA 的 [DDLCModTemplate2.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0)。

本模板属于粉丝作品，遵循 Team Salvato IP Guidelines。

## 加入社区

[Telegram 频道](https://t.me/DDLCModCN)

Copyright © 2019-2021 GanstaKingofSA. All rights reserved. Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.