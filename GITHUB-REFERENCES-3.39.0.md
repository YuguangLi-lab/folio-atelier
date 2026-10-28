# 3.39.0 设计依据与实现范围

日期：2026-10-28。本次沿用现有插件与 CSS 实现，无新增运行依赖。

- [Apple · Materials](https://developer.apple.com/design/human-interface-guidelines/materials)：材质用于表达控件与内容层次，并优先保证文字可读。Folio 按工具栏、浮层、卡片分配不同边缘和阴影；保留用户要求的卡片玻璃及原有保护条件。这是 CSS 材质近似实现。
- [Apple · Layout](https://developer.apple.com/design/human-interface-guidelines/layout)：控件对齐和分组帮助快速浏览。本次用字段标签、数值、模式组与交互状态的视觉层次精修已有布局。
- [MDN · CSS performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/CSS)：避免动画触发布局或昂贵效果。本次新增反馈仅过渡 background-color、color、border-color；没有新增模糊、阴影或尺寸过渡，没有持续背景动画。
- [MDN · prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)：减少动效偏好下停用新增反馈；减少透明度、增强对比、强制颜色以及插件已接受的画布拖动也使用即时状态。

120 ms 是本主题的反馈时长选择，不是 Apple 提供的数值标准。浮层和控件继续使用 ThoughtSpace 自己的 DOM、定位、关闭、焦点和键盘行为。工作区柔光以用户设置强度为基础，阅读 0.32、导航 0.2、媒体/手写 0.45、组织工作区 0.6，白板与脑图保留原强度。

配套插件继续使用已验收的 ThoughtSpace 1.3.38-folio.10；运行文件与 3.38.0 配套包核对 SHA256 一致。本轮测试重点是完整主题与插件实际组件运行时的交互、显示和性能约束；离线 DOM 不是原生 Obsidian 窗口，不能据此宣称整体 FPS。
