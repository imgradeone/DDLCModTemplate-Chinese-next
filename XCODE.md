# Using DDLCModTemplate with Xcode

![DDLC Mod in Xcode](https://marquiskurt.net/images/covers/2019-06-09-cover.png)

> 请注意！DDLC 中文 Mod 模板开发者目前无法测试模板在 Xcode 的发挥表现。

本模板内置了 Xcode 构建 / 运行支持，您可以在这篇教程（英文）中了解更多：https://marquiskurt.net/2019/06/09/post.html.

However, before running the project, there are a few things that *must* be configured to ensure that it runs properly.

## Change `RENPY_TOOL`

In **Config.xcconfig**, change the `RENPY_TOOL` line to where Ren'Py is installed. For example:

```xcconfig
// Change the line below to reflect where your Ren'Py install is!
//RENPY_TOOL=/some/renpy/location/renpy.sh
RENPY_TOOL=/Applications/renpy-6.99.12.4-sdk/renpy.sh
```

## Change Executable in the Schemes

1. In the Xcode toolbar, click where it says "DDLCModTemplate > My Mac" and click "Edit Scheme".
2. In the Info pane under the 'Run' section, click on the **Executable** field and select "Other". 
3. A file dialog should pop up; navigate to where Ren'Py is installed and select `renpy.app`.

## Test changes

When you have made these changes and added the appropriate DDLC files needed to run the template normally, click the Play button or press Command+R on your keyboard to test the build/run procedure.

If you are still receiving problems, follow [the tutorial](https://marquiskurt.net/2019/06/09/post.html) and check to make sure the project's settings are in the correct places.
