# UI-UX-PRO-MAX — 顶级 UI/UX 设计优化技能

## 功能描述

对网页界面进行专业级 UI/UX 全面优化，涵盖视觉设计、交互体验、动效、排版、可访问性与移动端适配，
目标是达到产品级别的设计质量，让每一个细节都符合现代设计规范。

## 触发关键词

- "UI-UX-PRO-MAX"
- "优化 UI/UX"
- "提升视觉体验"
- "设计优化"
- "界面美化"
- "前端设计升级"
- "顶级 UI 优化"

## 使用说明

调用此技能时，Claw 将按照以下 **10 条黄金准则** 对目标页面进行系统性优化：

### 1. 视觉层次（Visual Hierarchy）
- 通过字重（font-weight）、字号（font-size）、颜色对比、留白建立清晰的信息层次
- 重要元素突出，次要元素退后，引导用户视线自然流动
- 使用 `clamp()` 实现流体排版，适配各种屏幕尺寸

### 2. 色彩系统（Color System）
- 建立统一的 CSS 自定义属性色彩体系（`--primary`、`--accent`、`--surface` 等）
- 确保所有文字对比度符合 WCAG AA 标准（≥4.5:1）
- 用微妙的渐变和半透明层叠增加空间感

### 3. 动效与微交互（Motion & Micro-interaction）
- 所有过渡效果使用 `cubic-bezier` 或语义化缓动（`ease-in-out`）
- 悬停（hover）效果需要在 150–300ms 内完成，不得卡顿
- 利用 `IntersectionObserver` 实现入场动画，避免首屏闪烁
- 遵循「有意义的动效」原则：动效应服务于信息传递，而非装饰

### 4. 组件质量（Component Quality）
- 卡片、按钮、标签等组件需有完整的状态：默认 / 悬停 / 激活 / 禁用
- 按钮最小点击区域 ≥ 44×44px（移动端）
- 表单元素需有焦点样式（`focus-visible`）

### 5. 功能性 UX 增强（Functional UX）
- 为长内容页面添加**阅读进度条**（顶部固定）
- 为列表内容添加**实时搜索/过滤**功能
- 添加**回到顶部**浮动按钮，超过一屏后出现
- 关键链接添加**键盘导航**支持（Tab 顺序合理）

### 6. 性能友好（Performance-aware）
- 避免不必要的 JavaScript 阻塞，使用 `requestAnimationFrame` 处理动画
- 图片使用懒加载（`loading="lazy"`）
- CSS 动画优先使用 `transform` 和 `opacity`，避免触发 layout
- CDN 依赖使用 `defer` / `async` 加载

### 7. 响应式设计（Responsive Design）
- 移动优先（mobile-first）布局策略
- 断点设置：`480px`（手机）/ `768px`（平板）/ `1024px`（桌面）
- 导航栏移动端需折叠或简化，不可遮挡内容
- 触摸目标大小与间距适合手指操作

### 8. 排版系统（Typography）
- 正文字号 ≥ 15px，行高 1.6–1.8
- 标题使用字重 700-800，有字母间距（`letter-spacing`）调整
- 代码/技术词汇使用等宽字体（`monospace`）
- 中文字体优先：`PingFang SC`、`Microsoft YaHei`、`Noto Sans SC`

### 9. 装饰与氛围（Decoration & Atmosphere）
- 利用 `backdrop-filter: blur()` 制作毛玻璃效果
- 使用 CSS `radial-gradient` / `linear-gradient` 创造光晕/光效
- 适量添加 SVG 图标或 Emoji 增强视觉语义
- 暗色主题下使用低饱和度表面色，避免纯黑背景

### 10. 可访问性（Accessibility）
- 所有交互元素有语义化 HTML 标签（`<button>`, `<nav>`, `<main>`, `<article>`）
- 图片有 `alt` 属性，图标有 `aria-label`
- 避免仅用颜色传递信息（配合图标或文字）
- 支持系统级 `prefers-reduced-motion` 偏好

---

## 执行流程

调用 UI-UX-PRO-MAX 技能时，Claw 应按以下流程执行：

1. **分析现状**：阅读目标页面代码，识别当前设计痛点
2. **制定优化清单**：列出要改进的具体项目
3. **系统实施**：按照 10 条准则逐项优化，保持代码整洁
4. **验证**：确认所有交互功能正常，移动端样式符合预期

## 示例

**示例 1：优化导航网站**
```
用户：使用 UI-UX-PRO-MAX 技能优化我的 index.html 导航网站
Claw：[分析现有设计 → 添加进度条、搜索过滤、改进动效、优化排版 → 输出优化后的 index.html]
```

**示例 2：提升单个组件**
```
用户：用 UI-UX-PRO-MAX 优化这个卡片组件的悬停效果
Claw：[检查组件代码 → 添加 shimmer 动画、阴影层叠、transform 过渡 → 输出改进后的代码]
```

**示例 3：全站设计审查**
```
用户：UI-UX-PRO-MAX 审查我的网站设计问题
Claw：[逐条对照 10 条准则 → 输出问题列表与改进建议]
```

## 依赖

- 工具：`view`、`edit`、`create`（文件操作）
- 外部：无需额外 CDN，优先使用页面已有依赖
- 权限：需要对目标 HTML/CSS 文件有读写权限
