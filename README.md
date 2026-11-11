# Folio Atelier 3.42.0 · 白板画布设置精修

本预览版打磨 ThoughtSpace 的纸张和图片背景设置。纸张预设、色值输入、背景适配方式与透明度数值使用统一的层次和选中反馈，并修复滑杆被通用输入框样式绘成粗块的问题。[本轮改进与验证](BOARD-SETTINGS-3.42.0.md)。

同时包含 3.40–3.41 的累计改进，包括 14 组界面配色、卡片库适配、白板工具与搜索、对象编辑栏和整理预览。打开工具面板时自动让出编辑栏空间，关闭后恢复，工具搜索与白板搜索只保留一圈焦点指示。[此前白板界面改进](BOARD-POLISH-3.41.0.md)。

本轮原生验证使用 [ThoughtSpace 1.3.53](https://github.com/YuguangLi-lab/obsidian-thoughtspace/releases/tag/1.3.53)。主题安装包仅更新 Folio Atelier，不安装或升级 ThoughtSpace 插件二进制。

[浅色纸张设置](previews/v3.42.0/light-paper.png) · [深色图片背景](previews/v3.42.0/dark-background.png) · [画布工具](previews/v3.42.0/light-canvas-settings.png)

在 **Obsidian → 设置 → Style Settings → Folio Atelier → ThoughtSpace 界面配色** 中，为 14 组界面分别取色。每行左侧设置浅色，右侧设置深色；点击对应色块旁的重置按钮即可恢复主题原色。未选择的色块显示示例色，界面沿用原配色。

| 分区 | 取色器 |
| --- | --- |
| 工具与导航 | 插件工具栏、菜单与浮层、选中项底色、导航侧栏、空间总览与检索 |
| 阅读与创作 | 阅读台与引用、写作台、素材库与摘录、视频与媒体工作台、手写工作台 |
| 整理与设置 | 关系图、集合与卡片资料库、脑图与思维导图、插件设置与偏好 |

“分区颜色浓度”调节已选颜色与当前主题底色的混合程度。工具栏和浮层保留原有玻璃透明度与模糊；经典、Apple 简洁和液态玻璃三种风格都可使用。白板底色仍由原来的画布选项管理。配色范围是插件界面，正文、卡片自定义颜色、播放器、手写墨色、图谱连线及独立日历保持原样。开启系统强制色或高对比度时优先使用系统显示。

独立的桌面 Obsidian 1.15.0 测试库加载 ThoughtSpace 1.3.53，完成 113 项原生检查，覆盖纸张预设、色值校验、背景适配、滑杆键盘调节和取消不保存，以及既有白板、卡片库和写作交互。ThoughtSpace 1.3.50 与 1.3.53 各通过 154 项限定离线配色检查，共 308 项，覆盖深浅色和三种界面风格。[验证记录](validation/summary.json)

本轮没有新增模糊滤镜、持续动画或脚本监听器。尚未开展大型白板 FPS 基准或真机手机验收。

退出 Obsidian 后，将主题包中的 `manifest.json` 和 `theme.css` 放入库的 `.obsidian/themes/Folio Atelier/`；也可运行 `python3 scripts/install.py "/你的笔记库路径"` 自动备份旧主题并保留已有配色设置。重开 Obsidian 后在 Style Settings 调色。

完整安装包包含阅读、研究、写作三份可选 CSS 预设。安装器会将它们放入 CSS 代码片段目录，但不会自动启用；需要时在 Obsidian 外观设置中只启用其中一份。
