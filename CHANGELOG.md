# 更新日志

## 未发布版本（v2.0.0-dev）

### 开发

- refactor: 中文注释补充
- refactor: 修改 DDLC 资源缺失时提示
- refactor: 解禁 Ren'Py SDK 7.4.11
- change: 开发者模式设置为 `False`
- refactor: 将 BSOD 功能分离
- refactor: 修改部分译文
- change: 补丁更新
- change: 在关于页添加模板相关信息
- 修复了一处弹窗未汉化的问题
- `lockdown_check` 逻辑更新并屏蔽 Ren'Py 8

### 文件

- add: script-poemresponses2
- change: 修改 script-poemresponses 为汉化版本

## v2.0.0-beta3（测试版本）

### 功能

- add: 更完美的 BSoD

### 开发

- refactor: 解禁 Ren'Py SDK 7.4.9 - 7.4.10

## v2.0.0-beta2（测试版本）

### 功能
- add: 原版剧情翻译（待进一步优化，基于 Plus 和原版社区翻译）
- add: 双语选词游戏支持

### 修改 / 修复
- add: 帮助文档翻译（依旧不完全）
- refactor: 翻译更新（`跳过` -> `快进`）
- refactor: 修改默认存档位置为 `DDLCModTempCNNext`
- refactor: 更新 `original_scripts/script.rpy` 的文件逻辑
- refactor: 修改默认角色名称，匹配官方译名
- refactor: 补充未翻译部分
- patch: 跟进原模版 2.4.8 更新
- fix: 修复“历史”页标题未翻译的 bug

### 中文字体
- changed: 所有字体现已内嵌于仓库
- changed!: 部分字体重命名
- changed: Monika 字体改为悠哉字体
- changed: Yuri 字体改为霞鹜文楷

### 已知问题
- Ren'Py 7 下存档页可能不展示时间信息

## v2.0.0-beta1（测试版本）

First release.

### 功能
- add: 中文字体支持
- add: Ren'Py 7.4.6 Lockdown Check
- add: poem_en
- refactor: 将 README.html 改为 help.html
- changed: 默认不在工程中保留 `characters/*.chr` 文件

### 中文字体
- changed!: 主界面中文字体更换为 HarmonyOS Sans
- improved: Acy 字体展示效果
- add: attributions.txt
