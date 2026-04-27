# web-fetch — 网页内容抓取技能

## 功能描述

抓取指定 URL 的网页内容，将其转换为简洁的 Markdown 格式，方便 Claw 直接阅读和引用。

## 触发关键词

- "帮我看看这个网页"
- "抓取 / 获取网页"
- "fetch URL"
- "网页内容"
- "访问链接"

## 使用说明

提供目标 URL，Claw 将使用 `web_fetch` 工具进行抓取：

| 参数           | 说明                                           | 默认值  |
|--------------|----------------------------------------------|--------|
| `url`        | 目标网页地址（必填）                             | —      |
| `max_length` | 返回内容的最大字符数                              | 5000   |
| `raw`        | 是否返回原始 HTML（false 则转为 Markdown）        | false  |
| `start_index`| 分页起始位置，用于内容过长时继续读取               | 0      |

## 示例

**示例 1：读取文档页面**
```
用户：帮我看看 https://docs.github.com/en/copilot 的内容
Claw：[调用 web_fetch，返回该页面的 Markdown 摘要]
```

**示例 2：分页读取长文**
```
用户：获取 https://example.com/long-article，内容很长
Claw：[先抓取前 5000 字符，若截断则提示用户并使用 start_index 继续]
```

**示例 3：获取原始 HTML**
```
用户：fetch https://example.com/page 的原始 HTML
Claw：[调用 web_fetch，raw=true，返回 HTML 源码]
```

## 依赖

- 工具：`web_fetch`（已内置于 Claw 工具集）
- 权限：目标域名需未被沙箱屏蔽；若域名被屏蔽，Claw 应告知用户并请求解封。
