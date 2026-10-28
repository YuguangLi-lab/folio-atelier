# 3.38.0 开源参考与边界

核验日期：2026-10-23。本轮没有引入第三方玻璃引擎、远程素材或新增运行依赖。

- [Style Settings · SettingsManager.ts](https://github.com/community-archive/obsidian-style-settings/blob/main/src/SettingsManager.ts)：核实 getSetting、setSettings 的实际实现。Folio 通过能力检测和本主题设置 ID 检查调用；使用可等待的 setSettings 保存与恢复，不直接写入其他插件 data.json。此接口来自源码，未被文档承诺为稳定扩展 API；不可用时保留设置并说明依赖。
- [Style Settings · main.ts](https://github.com/community-archive/obsidian-style-settings/blob/main/src/main.ts)：核实主题设置分组以及 settingsManager、settingsList 的实际结构。
- [MDN · addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)：按事件阶段与 passive 语义处理输入。新增捕获监听器不阻止原有操作；确认插件已经接受事件后才进入流畅模式。
- 延续 [3.37.0 参考](GITHUB-REFERENCES-3.37.0.md) 中的内容保护、短文本浮层与辅助功能降级原则。分区变量复用已有绘制层，不增加全窗口模糊。

配套插件以本地固定 1.3.38 commit `7e7d13a33d2ef584fb497fd3310fbf4c5ed8460e` 为底座，合并既有 Folio.9 界面修整，单独构建为 `1.3.38-folio.10`。旧插件目录和历史包保留。

性能证据只覆盖新增运行时路径、已有折射更新、DOM 清理与静态 CSS 预算。1000 次连续活动指针事件中的零布局读取/零映射更新不等于整款 Obsidian 的零负载，也不构成实际 FPS 测量。
