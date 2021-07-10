# DDLC 中文 Mod 模板 2.0
嘿，你~~又~~想用中文写 DDLC Mod？**那你来对地方了！**

这是**新的** DDLC 中文 Mod 模板！本模板基于 GanstaKingofSA 的 DDLC Mod Template 2.0，并进行了[旧版](https://github.com/imgradeone/DDLCModTemplate-Chinese)已经进行的一系列汉化。使用本模板制作 Mod 时，请遵循 Team Salvato 的 [IP Guidelines](http://teamsalvato.com/ip-guidelines/)。

**本模板是为使用原版 DDLC 素材的饭制游戏和 Mod（而并非不使用原版素材的作品）设计的，提供源代码也并非以便将其复制粘贴到和 DDLC 没有关系的工程。此模板内大部分代码属于 Team Salvato 的知识产物，请遵循 Team Salvato 的 [IP Guidelines](http://teamsalvato.com/ip-guidelines/) 使用，否则后果自负。**

**如果你是 Mod 作者，请不要将 DDLC 游戏本体包含在你分发的 ZIP 里，这是违反 IP Guidelines 的行为。**

> 本 Mod 模板不支持 Doki Doki Literature Club Plus。

> 请注意：本模板可能尚不完善，且尚缺乏繁体中文支持。部分 GUI 元素暂未被汉化。

> 此模板自带 Android 支持，详情请看原版 DDLC Mod Template 2.0 所附带的 `guide.pdf`

## 开始制作 Mod

### 中文字体

DDLC 中文 Mod 模板使用了一些免费商用的中文字体，在此致谢。**开始 Mod 开发前，请务必下载这些字体，否则将无法启动工程。安装方式见 [中文字体包安装](#中文字体包安装) 小节。**

如有需要，您也可以自行修改配置文件，以自定义字体，**但请自主承担版权风险**。

中文字体详情请查看 [这里](./game/mod_assets/font/README.md)

#### 中文字体包安装

> 请注意：我们仍然建议您从各个字体的官网下载这些字体，即便它们都是免费商用字体。

您可以下载懒人专用字体包，下载完后将字体解压到 `game/mod_assets/font` 目录下即可。

请在 https://dokimod.cn/moddev/fontdl.html 获取字体包。

---

### 使用 Ren'Py SDK 6 进行 Mod 开发
1. 下载并运行 [Ren'Py SDK 6.99.12](https://www.renpy.org/release/6.99.12). 
    > 请注意：DDLC 不兼容新版 Ren'Py，除非游戏后续更新。
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Download DDLC on http://ddlc.moe or Steam & copy the `DDLC-1.1.1-pc` (`ddlc-mac` for MacOS/OS X or `Doki Doki Literature Club` for Steam) to the `renpy-6.99.12.4-sdk` folder. Rename the folder to your mod name.
3. Place the files withing the Mod Template's ZIP file into the DDLC folder you copied to. Accept any replaces if prompted. 
    > For MacOS/OS X, right click on DDLC.app within the `ddlc-mac` folder and click `Show Package Contents` then place the files within `Contents/Resources/autorun`. Accept any replaces if prompted. 
5. Launch the project in Ren'Py. It should compile and launch the game.
    > Sometimes this may not do anything or say a error happened. Click `Launch Project` again, and it should boot up.
6. Once you finished writing your script, navigate the Ren'Py Menu, and select `Build Distributions`. Uncheck all the options and check only `Ren'Py 6 DDLC Compliant Mod` and click `Build`. This will create a cross-platform .ZIP file with files for your mod.

### Getting Started for Advanced Users (Ren'Py 7)
1. 下载并运行 [Ren'Py SDK 7.4.5](https://www.renpy.org/release/7.4.5)。
    > 请注意：使用 Ren'Py 7 构建的 Mod 不兼容 Ren'Py 6。我们也会跟进上游的变动，以完美适配最新的 Ren'Py SDK。目前 Ren'Py SDK 7.4.6 有破坏性改动，会导致 DDLC 转场失效，请不要更新 SDK！！！
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Download DDLC on http://ddlc.moe or Steam & copy the `DDLC-1.1.1-pc` (`ddlc-mac` for MacOS/OS X or `Doki Doki Literature Club` for Steam) to the `renpy-<version>-sdk` folder. Rename the folder to your mod name.
3. Place the files withing the Mod Template's ZIP file into the DDLC folder you copied to. Accept any replaces if prompted. 
    > For MacOS/OS X, right click on DDLC.app within the `ddlc-mac` folder and click `Show Package Contents` then place the files within `Contents/Resources/autorun`. Accept any replaces if prompted. 
5. Launch the project in Ren'Py. It should compile and launch the game.
    > Sometimes this may not do anything or say a error happened. Click `Launch Project` again, and it should boot up.
6. Once you finished writing your script, navigate the Ren'Py Menu, and select `Build Distributions`. Uncheck all the options and check only `Ren'Py 7 DDLC Compliant Mod` and click `Build`. This will create a cross-platform .ZIP file with files for your mod.

### Getting Started For Android Porting/Modding
Refer to *guide.pdf* in your ZIP folder for more information, but make sure of these key points.
1. Make sure that your package name in Ren'Py Launcher is the same as the package name you will use in `options.rpy` and build name. Example: If your package name is named `com.yuri.storm` and your build name is `STORM`, your package name in Ren'Py Launcher under Android -> Configure must be `com.yuri.storm` as well. 
2. It is wise to only change the `sdc` part of the package name to your name and leave the rest as-is in `options.rpy` under `define package_name`. It will grab your mod name via `build.name` and `com` is common use in Android applications. i.e. `"com.sdc." + build.name.lower()` to `com.monika." + build.name.lower()`

More information about Android is listed in the Wiki or *guide.pdf*.

## 模板特色功能

### DDLC Mod Template 2.0
1. Build Packaging on Ren'Py 6 or 7!
2. Splash Screen when your mod is launched for the first time.
3. DDLC's exact RPY fiiles with explainations.
4. Customizable! Use this as a starting point for any ideas you wish to create.
5. MacOS/OS X and Linux `.app` and `.sh` support.
6. Full Android Support! Yes, everything DDLC (except `[currentuser]`) will work under Android.
    > Refer to *guide.pdf* for configuring your mod for Android.
7. Xcode Support! Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)
8. Terra's In-Depth Poemgame Guide!
9. NVL Support thanks to Yagamirai01!

### DDLC 中文 Mod 模板
1. 绝赞中文化（目前只支持简体中文）
2. 绝赞字体优化
3. ~~绝赞咕咕咕~~

## 特别感谢

- Team Salvato http://teamsalvato.com / https://ddlc.moe
- GanstaKingofSA
- 所有字体作者

## 开源许可

本 Mod 模板需要使用 Ren'Py。  
Ren'Py 的许可，请参照 https://www.renpy.cn/doc/license.html （简体中文）或 https://www.renpy.org/doc/html/license.html （英文）。

本模板基于 GanstaKingofSA 的 [DDLCModTemplate2.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0)。

本模板属于粉丝作品，遵循 Team Salvato IP Guidelines。

## 加入社区

[Telegram 频道](https://t.me/DDLCModCN)
