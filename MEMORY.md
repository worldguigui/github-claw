# MEMORY.md — 长期记忆

> 存放跨会话稳定不变的事实、偏好与决策。  
> 每次重大变更时更新，保持精简。最后更新：2026-04-27

---

## 用户偏好

- 语言：中文为主，代码和命令用英文
- 风格：务实、简洁，不过度设计，优先把事做完
- 提交风格：消息要说明做了什么以及原因

## 仓库定位

- 这是一个个人 AI 工作空间，使用 GitHub Copilot 网页版作为主要 AI 接口
- 仓库本身是持久化记忆与文件空间，不只是代码仓库
- 核心规范见 `AGENTS.md`

## 技术约定

- 项目级技能保存在 `.agents/skills/`，每个技能独立目录，内含 `README.md` 说明；详见 `.agents/skills/README.md`

## 重要决策

- 2026-04-27：初始化仓库，建立 AGENTS.md / MEMORY.md / memory/ 三层结构
- 2026-04-27：建立 `.agents/skills/` 技能目录体系，约定技能发现/安装/使用机制；新增示例技能 `web-fetch`
- 2026-04-27：安装 `ui-ux-pro-max` 技能（10 条黄金准则），并用其对 CodeNote 导航官网（index.html）进行深度 UI/UX 优化
- 2026-04-28：为 CodeNote 导航官网生成高质量 README.md（替换原根 README）；创建 3 张 Chiikawa 风格 SVG 插图（banner / topics / journey）保存于 docs/images/；安装 ai-image-generation 技能

## 持续跟踪目标

_（暂无，随使用积累补充）_
