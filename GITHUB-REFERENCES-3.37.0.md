# 3.37.0 开源参考与实现取舍

核验日期：2026-10-23。下列主分支链接可能随上游变化；本轮阅读源码并独立编写主题 CSS，没有复制第三方组件、加载远程素材或引入新运行时。

- [rdev/liquid-glass-react · src/index.tsx](https://github.com/rdev/liquid-glass-react/blob/master/src/index.tsx)：边缘折射与内容区域分离，装饰层不拦截点击。Folio 保留 ThoughtSpace 自有的 SVG 光学处理；新增浮层使用 CSS 材质及更实的底色，不叠加第二套折射。
- [stefan-imbesi/obsidian-macos-theme · theme.css](https://github.com/stefan-imbesi/obsidian-macos-theme/blob/main/theme.css)：菜单等短文本界面统一材质，并支持减少透明度。Folio 复用现有 8–24 px 模糊设置，新增浮层采用基础玻璃与实体色 75:25 的混合，避免直接采用上游 50 px 菜单模糊。
- [xcyberpunkx0/liquid-glass · tiers.ts](https://github.com/xcyberpunkx0/liquid-glass/blob/main/src/core/tiers.ts) 与 [styles.css](https://github.com/xcyberpunkx0/liquid-glass/blob/main/src/styles.css)：优先处理辅助功能偏好，并响应运行期间的变化。本轮新增动态减少透明度、增强对比度及强制颜色的切换/恢复检查。沿用主题统一降级变量，没有移植其设备分级或观察器。

## 插件对照

以固定的 ThoughtSpace 1.3.38 源码（commit `7e7d13a33d2ef584fb497fd3310fbf4c5ed8460e`）核对真实类名和结构：

- 画布设置面板在 `main.ts` 中为视图控制条的兄弟节点，玻璃应在外层；内层控制条去掉重复材质。
- 插件右键菜单由 `themePluginMenu()` 标记；动态样式的优先级可能盖过原生 `.menu` 规则。本轮为插件所有的菜单增加精确选择器，保留 SVG 光学表面的所有权。
- 脑图搜索结果是独立浮层；摘录来源浮层挂载在 `body`。都保留插件的位置、滚动、隐藏与关闭逻辑。
- 关系图节点选择、筛选、更多工具三类浮层采用同一材质；筛选控制组和更多工具的内部条移除重复模糊。
- 对原生 Canvas 子菜单增加嵌套透明化的例外。此项依据本地原生 CSS 与重建父子结构验证，未在原生 Obsidian 中确认实际 DOM。

所有更改仅在液态玻璃模式的屏幕媒体中启用。纸张/图片背景、用户指定的卡片表面、经典/Apple 模式与打印仍由原有规则负责。
