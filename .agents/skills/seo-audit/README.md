# seo-audit

## 功能描述
对网站进行全面 SEO 审计，识别并修复 meta 标签、结构化数据、可索引性、页面语义、链接结构、Core Web Vitals 等方面的问题，提供可落地的优化建议。

## 触发关键词
"SEO 审计"、"SEO 优化"、"搜索引擎优化"、"meta 标签"、"结构化数据"、"schema"、"robots.txt"、"sitemap"、"Open Graph"、"可索引性"、"页面没有被收录"、"流量下降"

## 使用说明

### 审计优先顺序
1. **可抓取性 & 可索引性** — robots.txt、sitemap、canonical、noindex
2. **技术基础** — HTTPS、速度、移动端友好、Core Web Vitals
3. **页面 On-Page 优化** — title、description、heading 结构、图片 alt
4. **结构化数据** — JSON-LD schema（WebSite、Article、BreadcrumbList 等）
5. **内容质量** — E-E-A-T 信号、关键词覆盖
6. **权威性 & 链接** — 内链结构、外链质量

### 关键检查项

**Head 区域**
- `<title>` 唯一、含主关键词、50-60 字符（中文约 25-30 字）
- `<meta name="description">` 唯一、150-160 字符、含 CTA
- `<link rel="canonical">` 指向正确 URL
- `<meta name="robots" content="index, follow">`
- `<meta name="author">`
- Open Graph: og:title、og:description、og:url、og:type、og:site_name、og:image
- Twitter Card: twitter:card、twitter:title、twitter:description
- Favicon

**结构化数据（JSON-LD）**
- WebSite + SearchAction（适合导航/内容索引类站点）
- 用 `<script type="application/ld+json">` 注入，不依赖 JS 动态渲染

**语义 HTML**
- 每页唯一 `<h1>`，层级结构 H1→H2→H3
- 日期用 `<time datetime="YYYY-MM-DD">`
- 导航用 `<nav>` + `aria-label`，主体用 `<main>`，页脚用 `<footer>`
- 图片必须有 `alt` 属性

**可索引性文件**
- `robots.txt` 位于根目录，包含 Sitemap 引用
- `sitemap.xml` 列出所有重要 URL，含 `<lastmod>`

### 注意事项
- `web_fetch` 抓取的 HTML 无法可靠检测 JS 动态注入的 JSON-LD；需用 Google Rich Results Test 验证
- 中文站点：`<html lang="zh-CN">`、og:locale = `zh_CN`

## 示例

```
用户：帮我对这个 GitHub Pages 静态站做 SEO 审计
Claw：读取 index.html → 按优先顺序逐项检查 → 给出带优先级的修复建议 → 直接落地到代码
```

## 依赖
- 读取站点 HTML（view 工具）
- 可选：Google Rich Results Test 验证结构化数据
- 可选：Google PageSpeed Insights 验证 Core Web Vitals

---

> 来源：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)，技能版本 1.2.0，本地适配版本（中文简化）。
