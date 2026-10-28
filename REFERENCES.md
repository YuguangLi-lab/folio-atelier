# GitHub 源码参考与适配记录 · 3.34.0

查阅日期：2026-10-23。以下是设计参考，主题实现独立编写；没有复制、执行或安装第三方演示代码，也未新增 React 或第三方运行时依赖。参考链接指向查阅时的主分支，后续内容可能变化。

| 项目与实际阅读文件 | 吸收的具体思路 | Folio 中的实现 |
| --- | --- | --- |
| [rdev/liquid-glass-react / src/index.tsx](https://github.com/rdev/liquid-glass-react/blob/master/src/index.tsx) | 边缘高光与中央内容分离；装饰层不截获鼠标 | 卡片使用背景渐变与内阴影，没有新遮罩 DOM；正文不使用 filter，保留选中轮廓与原有按钮命中 |
| [shuding/liquid-glass / liquid-glass.js](https://github.com/shuding/liquid-glass/blob/main/liquid-glass.js) | SVG 位移贴图属于额外运行时，不能与普通 CSS 模糊混为一谈 | 主题只提供 CSS 材质；ThoughtSpace 1.3.38 已有的 SVG 折射滤镜由插件拥有，不重复创建滤镜或鼠标追踪 |
| [stefan-imbesi/obsidian-macos-theme / theme.css](https://github.com/stefan-imbesi/obsidian-macos-theme/blob/main/theme.css) | 明暗独立的半透明材质、分层菜单、减少透明度的降级 | 独立中文卡片开关、冷雾蓝与暖砂米底色、深色低亮高光；手动实底和系统无障碍选项一起覆盖卡片 |

## 针对自己的插件重做适配

核对 ThoughtSpace 1.3.38，提交 `7e7d13a33d2ef584fb497fd3310fbf4c5ed8460e` 的 `ui-tokens.ts`、`interface-style-tokens.ts`、`liquid-glass-runtime.ts` 与实际 CSS。也检查本地 1.3.35-folio.9 的工具栏样式。

- 新版是预留列宽的左侧工具栏：列保持直边，紧凑工具组采用玻璃材质；旧版悬浮栏仍适用。
- 外观工具栏、底部视图工具栏各有一个玻璃外壳，内部行与按钮组清除重复滤镜。
- 新版动态样式有高优先级选择器；限定提高主题工具栏选择器优先级，在两种注入顺序下验证。
- 插件已经激活的 `[data-ts-glass-optics=true]` 保留原 SVG 滤镜和内容保护层。关闭插件玻璃效果或开启主题实底后，卡片与新增外壳同步降级。
- 卡片只处理普通表面。填色、自定义边框、透明、折叠、特殊纸张、媒体与行内编辑状态按原样保留。
- 卡片闲置不启用模糊，精细指针悬停或卡内聚焦时启用 6 px 磨砂；减少动态效果时不启用此增强。没有新增无限动画。

## 验证边界

离线测试包含真实插件样式、工具栏导航/溢出/滚轮助手，以及 1.3.38 的真实外观与折射运行时；整体 DOM 为根据源码构建的自有样例。没有接管 Obsidian，也没有测试原生分栏、输入法或真实使用帧率。202 张静止卡片无模糊滤镜仅说明样式开销受控，不等于性能基准。

离线预览中的图标来自 [Lucide](https://github.com/lucide-icons/lucide)，使用 ISC 许可；只作为预览资源，安装的主题没有外部图标依赖。

## 3.35.0 工具栏覆盖扩展

沿用上述参考与材质，不新增第三方代码。根据 ThoughtSpace 1.3.38 源码与已有原生 CSS，建立 111 个明确选择器的清单；不通过泛匹配 toolbar 字符串染色正文。覆盖写作、阅读、媒体、手写、关系与资料工具，以及原生工具栏。嵌套工具栏移除内部背景与滤镜，主题实底开关也覆盖手写浮层的插件折射层。新增代码在 `src/atelier-glass-toolbars.css`，来源与范围见 `validation/toolbar-inventory.json`。

## 3.36.0 背景实现参考（2026-10-23）

实际阅读 [samasante/liquid-glass/examples/GlassNotification.tsx](https://github.com/samasante/liquid-glass/blob/main/examples/GlassNotification.tsx) 中的渐变背景及材质/内容分离结构，和 [waldbach/liquid-glass-css/styles.css](https://github.com/waldbach/liquid-glass-css/blob/main/styles.css) 中的背景展示与分层滤镜。主分支链接可能随项目变化。

吸收“背景先提供色彩层次，再让玻璃覆盖其上”的思路，独立设计低饱和蓝、砂、青三组光感，提供强度与关闭选项。未照搬高饱和壁纸、多层环形滤镜或组件代码，也没有引入其图片、包或运行时。原有 macOS 主题的无障碍降级思路继续保留。

Folio 实现位于 `src/atelier-glass-backgrounds.css`：光晕属于父容器，插件的网格仍属于舞台，避免把光晕混入 24 px 网格贴图中。背景不使用伪元素遮罩、不改变堆叠与点击区域，不新增滤镜或动画。额外适配 19 类插件容器与 5 类原生导航面板，正文与媒体保留自身样式。

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


## 3.38.0

分区材质、输入阶段和可撤销设置接口依据见 [GITHUB-REFERENCES-3.38.0.md](GITHUB-REFERENCES-3.38.0.md)。


## 3.39.0

本轮材质、控件和性能取舍见 [GITHUB-REFERENCES-3.39.0.md](GITHUB-REFERENCES-3.39.0.md)。
