#!/usr/bin/env python3
"""
AI Daily Digest — 每日 AI 科技热点收集脚本
数据源：Hacker News API + RSS (ArXiv AI / MIT Tech Review / The Verge AI)
输出：在 GitHub Issues 创建一篇 Markdown 格式日报
"""

import os
import json
import time
import datetime
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.error import URLError

# ── 配置 ──────────────────────────────────────────────────────────────────────

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_REPO  = os.environ["GITHUB_REPOSITORY"]   # "owner/repo"

# 北京时间显示
BJ_OFFSET = datetime.timezone(datetime.timedelta(hours=8))
NOW_BJ    = datetime.datetime.now(BJ_OFFSET)

WEEK_START = NOW_BJ - datetime.timedelta(days=7)

HN_TOP_URL    = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL   = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HN_FETCH_NUM  = 200   # 从前 N 条里筛 AI 相关

RSS_FEEDS = [
    {
        "name": "ArXiv CS.AI",
        "url": "https://rss.arxiv.org/rss/cs.AI",
        "max": 8,
    },
    {
        "name": "MIT Technology Review",
        "url": "https://feeds.technologyreview.com/feeds/rss/all",
        "max": 6,
    },
    {
        "name": "The Verge · AI",
        "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
        "max": 6,
    },
]

AI_KEYWORDS = {
    "ai", "artificial intelligence", "machine learning", "deep learning",
    "llm", "gpt", "claude", "gemini", "openai", "anthropic", "mistral",
    "transformer", "neural", "diffusion", "chatgpt", "copilot", "model",
    "agent", "rag", "embedding", "inference", "benchmark", "multimodal",
    "generative", "hallucination", "fine-tun", "lora", "sora", "robotics",
}

# ── 工具函数 ──────────────────────────────────────────────────────────────────

def fetch_json(url: str, timeout: int = 10) -> object:
    req = Request(url, headers={"User-Agent": "github-claw-digest/1.0"})
    with urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())

def fetch_text(url: str, timeout: int = 10) -> str:
    req = Request(url, headers={"User-Agent": "github-claw-digest/1.0"})
    with urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def is_ai_related(text: str) -> bool:
    t = text.lower()
    return any(kw in t for kw in AI_KEYWORDS)

def ts_to_dt(ts: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)

# ── Hacker News ───────────────────────────────────────────────────────────────

def fetch_hn_ai_stories(limit: int = 12) -> list[dict]:
    print("Fetching Hacker News top stories…")
    try:
        ids = fetch_json(HN_TOP_URL)[:HN_FETCH_NUM]
    except URLError as e:
        print(f"  HN fetch failed: {e}")
        return []

    results = []
    for item_id in ids:
        if len(results) >= limit:
            break
        try:
            item = fetch_json(HN_ITEM_URL.format(item_id))
        except URLError:
            continue

        if item.get("dead") or item.get("deleted"):
            continue
        title = item.get("title", "")
        url   = item.get("url", f"https://news.ycombinator.com/item?id={item_id}")
        score = item.get("score", 0)
        ts    = item.get("time", 0)

        if ts and ts_to_dt(ts) < WEEK_START.astimezone(datetime.timezone.utc):
            continue  # 超过一周的跳过

        if is_ai_related(title):
            results.append({
                "title": title,
                "url":   url,
                "score": score,
                "source": "Hacker News",
            })
        time.sleep(0.05)   # 限速

    print(f"  Found {len(results)} AI stories from HN")
    return results

# ── RSS ───────────────────────────────────────────────────────────────────────

def fetch_rss(feed: dict) -> list[dict]:
    name = feed["name"]
    print(f"Fetching RSS: {name}…")
    try:
        raw = fetch_text(feed["url"])
    except URLError as e:
        print(f"  RSS fetch failed ({name}): {e}")
        return []

    results = []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        print(f"  RSS parse failed ({name}): {e}")
        return []

    ns = {}
    # Atom or RSS?
    items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")

    for item in items:
        if len(results) >= feed["max"]:
            break

        def get(tag: str, atom_tag: str = "") -> str:
            node = item.find(tag)
            if node is None and atom_tag:
                node = item.find(atom_tag, ns)
            return (node.text or "").strip() if node is not None else ""

        title   = get("title")
        link_el = item.find("link")
        if link_el is None:
            link_el = item.find("{http://www.w3.org/2005/Atom}link")
        link = ""
        if link_el is not None:
            link = link_el.get("href") or link_el.text or ""
        link = link.strip()

        if not title or not is_ai_related(title + get("description") + get("summary")):
            continue

        results.append({
            "title":  title,
            "url":    link,
            "source": name,
        })

    print(f"  Found {len(results)} AI items from {name}")
    return results

# ── 创建 Issue ────────────────────────────────────────────────────────────────

def build_body(hn_stories: list[dict], rss_items: list[dict]) -> str:
    date_str = NOW_BJ.strftime("%Y-%m-%d")
    week_str = f"{WEEK_START.strftime('%m/%d')}–{NOW_BJ.strftime('%m/%d')}"

    lines = [
        f"## 🤖 AI 科技热点日报 · {date_str}",
        f"> 数据时间范围：本周（{week_str}）· 自动生成于北京时间 {NOW_BJ.strftime('%H:%M')}",
        "",
    ]

    if hn_stories:
        lines += [
            "### 🔥 Hacker News 热议",
            "",
        ]
        for s in hn_stories:
            score_tag = f" `▲{s['score']}`" if s.get("score") else ""
            lines.append(f"- [{s['title']}]({s['url']}){score_tag}")
        lines.append("")

    for feed in RSS_FEEDS:
        items = [x for x in rss_items if x["source"] == feed["name"]]
        if not items:
            continue
        lines += [
            f"### 📰 {feed['name']}",
            "",
        ]
        for item in items:
            lines.append(f"- [{item['title']}]({item['url']})")
        lines.append("")

    total = len(hn_stories) + len(rss_items)
    lines += [
        "---",
        f"*共收录 {total} 条 · 由 [github-claw](https://github.com/{GITHUB_REPO}) 定时工作流自动生成*",
    ]
    return "\n".join(lines)

def create_issue(title: str, body: str) -> None:
    import urllib.request
    payload = json.dumps({"title": title, "body": body, "labels": ["ai-digest"]}).encode()
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    req = Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept":        "application/vnd.github+json",
            "Content-Type":  "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "github-claw-digest/1.0",
        },
        method="POST",
    )
    with urlopen(req, timeout=15) as r:
        resp = json.loads(r.read())
    print(f"Issue created: {resp['html_url']}")

# ── 主流程 ────────────────────────────────────────────────────────────────────

def main():
    hn_stories = fetch_hn_ai_stories(limit=12)
    rss_items  = []
    for feed in RSS_FEEDS:
        rss_items.extend(fetch_rss(feed))

    if not hn_stories and not rss_items:
        print("No content collected, skipping issue creation.")
        return

    date_str  = NOW_BJ.strftime("%Y-%m-%d")
    issue_title = f"🤖 AI 日报 · {date_str}"
    body = build_body(hn_stories, rss_items)
    create_issue(issue_title, body)

if __name__ == "__main__":
    main()
