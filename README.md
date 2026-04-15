<p align="center">
  <h1 align="center">🛒 电商视觉文案设计 Skill</h1>
  <p align="center">E-commerce Visual Copywriting SOP — AI 驱动的主图+详情页文案设计工作流</p>
  <p align="center">
    <a href="#快速开始">快速开始</a> •
    <a href="#安装方式">安装</a> •
    <a href="#使用方式">使用方式</a> •
    <a href="#合规规则库">合规规则</a> •
    <a href="#自审机制">自审机制</a> •
    <a href="#license">License</a>
  </p>
</p>

---

## ✨ 这是什么

一个 **AI Agent Skill**，让 AI 按照标准化 SOP 输出**电商主图 + 详情页的图文案执行方案**。

**你给产品信息 → AI 输出每张图的：画面内容 + 图内文案 + 设计场景说明**

设计师拿到就能直接开工。

### 核心特性

| 特性 | 说明 |
|------|------|
| 📋 **6步SOP工作流** | 收集信息 → 必卖理由 → 主图5张 → 详情页模块 → 自审评分 → 输出 |
| ⚖️ **4层合规规则库** | 覆盖通用/蓝帽子保健食品/运动器材/普通食品，含禁用词替换表 |
| 🔍 **强制自审≥80分** | 文案精简度/可放性/合规性/结构/实用性 五维打分，不达标自动重写 |
| 📱 **手机端优化** | 主图≤5行、详情页≤6行，确保一屏扫完不留残念 |
| 🛡️ **平台全覆盖** | 淘宝/天猫/京东/拼多多/抖音小店 审核要点内置 |

### 效果对比

```
❌ 普通AI输出：
"这款产品采用独家专利技术，能够有效改善您的身体状况，
帮助您恢复到最佳状态……"

（啰嗦、放不下图、有违规风险、设计师看不懂怎么画）

✅ 本Skill输出：
┌─────────────────────────────┐
│ 画面：产品居中 + 红金背景     │
│                             │
│ 图内文案：                    │
│   标题：20秒速溶 松花粉玉竹   │
│   副标题：独立小条 随时来一条  │
│   卖点：全水溶 · 无渣 · 不卡喉 │
│   兜底：本品为普通食品        │
│                             │
│ 设计说明：深绿底色+金色文字…   │
└─────────────────────────────┘

（精简、能放图、合规、设计师直接开工）
```

---

## 🚀 快速开始

### 最简使用（3步）

```bash
# 1. 克隆或下载本仓库
git clone https://github.com/feichanggege/ecommerce-visual-copywriting-skill.git

# 2. 把 SKILL.md 放到你的 AI 工具 skill 目录（见下方「安装方式」）

# 3. 在对话中触发：
#   "帮我的松花粉饮料写一套主图文案"
#   "帮我做详情页执行方案"
#   "审查一下这个电商文案合不合规"
```

---

## 📦 安装方式

### 方式一：OpenClaw / WorkBuddy 用户（推荐）

将 `SKILL.md` 和 `references/` 目录放到用户级 Skill 目录：

```bash
# Linux/macOS
cp -r SKILL.md references/ ~/.workbuddy/skills/ecommerce-visual-copywriting/

# Windows PowerShell
Copy-Item -Recurse SKILL.md, references $env:USERPROFILE\.workbuddy\skills\ecommerce-visual-copywriting\
```

安装完成后，OpenClaw 会自动识别并加载此 Skill。

### 方式二：Claude Code 用户

将 Skill 内容注册为 CLAUDE.md 的自定义指令：

**方法 A — 直接引用（推荐）：**

```bash
# 将 SKILL.md 放到项目根目录的 .claude/skills/ 下
mkdir -p .claude/skills/ecommerce-visual-copywriting
cp SKILL.md references/ .claude/skills/ecommerce-visual-copywriting/
```

然后在 `.claude/CLAUDE.md` 中添加：

```markdown
## 自定义 Skills

当用户请求电商文案设计时，读取并遵循 `.claude/skills/ecommerce-visual-copywriting/SKILL.md` 中的完整工作流。
合规规则参考 `.claude/skills/ecommerce-visual-copywriting/references/compliance-rules.md`。
```

**方法 B — 内嵌到 CLAUDE.md：**

如果不想用文件引用，可以直接把 `SKILL.md` 的核心规则复制到项目的 `.claude/CLAUDE.md` 中：

```markdown
# .claude/CLAUDE.md（追加以下内容）

## 电商文案设计 SOP

当涉及主图文案、详情页文案、电商商品文案时：

1. 收集产品信息（类型/品牌/SKU/人群）
2. 提炼3-5条必卖理由（基于可验证事实）
3. 输出主图5张 + 详情页模块（每张图只写：画面 / 图内文案 / 设计说明）
4. 文案量控制：主图≤5行，详情页≤6行
5. 自审评分≥80分才输出（精简度20 + 可放性20 + 合规25 + 结构15 + 实用20）
6. 合规规则按产品类型匹配（通用/蓝帽子/运动器材/普通食品）
```

### 方式三：其他 AI 工具（Cursor / Windsurf / Continue 等）

几乎所有支持自定义指令的 AI 工具都可以使用此 Skill：

| 工具 | 配置文件位置 | 操作 |
|------|-------------|------|
| **Cursor** | `.cursorrules` 或项目根目录 | 追加 SKILL.md 核心规则 |
| **Windsurf** | `.windsurfrules` | 同上 |
| **Continue** | `~/.continue/config.yaml` | 引用 SKILL.md 路径 |
| **Cline** (VS Code) | `.cline/` 目录 | 参考 Claude Code 方式 |
| **Aider** | `/instructions` 文件 | 复制 SKILL.md 内容 |
| **通用** | System Prompt / Custom Instructions | 直接嵌入核心规则 |

> 💡 **核心思路**：把 `SKILL.md` 当作一份「电商文案设计的 System Prompt 片段」注入到任何 AI 工具中即可。

### 方式四：直接当 Prompt 模板用

不想配置？直接复制粘贴也行：

1. 打开 [`SKILL.md`](./SKILL.md)
2. 复制「核心工作流」Step 1-6 全部内容
3. 粘贴到任何 AI 对话框最前面
4. 在后面附上你的产品信息
5. 发送

---

## 🎯 使用方式

### 触发关键词

提到以下任一关键词即触发此 Skill：

- 中文：主图文案 / 详情页文案 / 电商文案 / 商品文案 / 合规审查 / 广告法
- 英文：listing copy / product detail page / CTR optimization
- 平台名：淘宝 / 天猫 / 京东 / 拼多多 / 抖音小店 文案

### 输入要求

向 AI 提供以下信息（**必须有** = 必填，建议有 = 选填）：

| # | 信息 | 必要性 | 说明示例 |
|---|------|--------|---------|
| 1 | 产品类型判定 | ✅ 必须有 | 保健食品(蓝帽子) / 普通食品 / 运动器材 / 其他 |
| 2 | 品牌名 + 公司全称 | ✅ 必须有 | 用于品牌信任模块和法律声明 |
| 3 | SKU列表+价格 | ✅ 必须有 | 规格参数表的基础 |
| 4 | 主图文案初稿/想法 | ✅ 必须有 | 可以是口述或已有草稿 |
| 5 | 目标人群画像 | ⭐ 建议有 | 决定必卖理由提炼方向 |
| 6 | 竞品链接/截图 | ⭐ 建议有 | 差异化定位依据 |
| 7 | 产品实拍素材 | ⭐ 建议有 | 让场景规划更具体 |

### 输出格式

每个输出单元只包含三项：

```
┌── 【图X / M模块名称】────────────────┐
│                                      │
│  📷 画面内容                          │
│  （描述这张图放什么画面）              │
│                                      │
│  ✏️ 图内文案                          │
│  （实际写在图片上的文字，≤N行）         │
│                                      │
│  🎨 设计场景说明                      │
│  （构图/配色/字号/风格指引）           │
│                                      │
└──────────────────────────────────────┘
```

### 使用示例

#### 示例对话

> **你**：帮我做一款松花粉固体饮料的主图和详情页方案
> 
> **产品信息**：
> - 类型：普通食品（非蓝帽子）
> - 品牌：雄花木末
> - 配料：松花粉、麦芽糊精、玉竹、山楂、薄荷
> - SKU：60g/盒 ¥169
> - 目标人群：31-40岁久坐职场人
>
> ---
>
> **AI（调用本 Skill 后输出）**：
> 
> （按照 SOP 输出完整执行方案，含主图5张 + 详情页M1-M7 + 合规自查）

---

## ⚖️ 合规规则库

本 Skill 内置 **4层合规规则**，根据产品类型自动匹配：

```
┌─────────────────────────────────────────┐
│          合规规则分层架构                │
├─────────────────────────────────────────┤
│                                         │
│  L3 普通食品  ← 最严！什么功能都不能说   │
│  ─────────────────────────────────────  │
│  L2 运动器材  ← 去医疗化，禁治疗动词     │
│  ─────────────────────────────────────  │
│  L1 蓝帽子    ← 只能说批准功能           │
│  ─────────────────────────────────────  │
│  L0 通用规则  ← 绝对化用语清零            │
│                                         │
│  （所有产品都必须过L0，然后按类型加层）    │
└─────────────────────────────────────────┘
```

详细规则（含禁用词替换表、免责声明模板、平台审核重点）请查看：
📖 [`references/compliance-rules.md`](./references/compliance-rules.md)

---

## 🔍 内置自审机制

这是本 Skill 最大的特色——**写完自动打分，不到80分不让输出**。

### 评分卡（满分100）

| # | 维度 | 分值 | 扣分标准 |
|---|------|------|---------|
| 1 | **文案精简度** | 20 | 有多余解释/教学式文字，每处 -2 |
| 2 | **图内可放性** | 20 | 超出行数限制，每超1行 -3 |
| 3 | **合规性** | 25 | 绝对化用语/功效暗示/缺免责，每处 -5 |
| 4 | **结构清晰度** | 15 | 多余板块超出三件套，每个 -3 |
| 5 | **实用性** | 20 | 缺关键执行信息，每处 -4 |

### 流程

```
写初稿 → 逐项打分 → 总分 ≥ 80？
                         ├─ ✅ 是 → 输出给用户
                         └─ ❌ 否 → 自己重写，不打扰用户
                                              ↓
                                          循环直到合格
```

---

## 📂 文件结构

```
ecommerce-visual-copywriting-skill/
├── README.md                              ← 你在这里 👈
├── LICENSE                                ← MIT 开源协议
├── SKILL.md                               ← ★ 核心：完整SOP工作流定义
└── references/
    └── compliance-rules.md                ← 4层合规规则库（详细版）
```

| 文件 | 大小 | 用途 |
|------|------|------|
| `SKILL.md` | ~5KB | Skill 入口文件，含完整6步SOP + 触发词 + 文案量标准 |
| `compliance-rules.md` | ~4KB | 合规规则详细版，含所有替换表、声明模板、检查清单 |

---

## 🔄 版本历史

### v1.0.0 (2025-04-15)

- ✅ 初始版本发布
- ✅ 6步SOP工作流（收集→理由→主图→详情→自审→输出）
- ✅ 4层合规规则库（通用/蓝帽子/运动器材/普通食品）
- ✅ 强制自审评分机制（≥80分门槛）
- ✅ 文案量标准（手机端一屏可读）
- ✅ 覆盖淘宝/天猫/京东/拼多多/抖音小店

---

## 🤝 贡献

欢迎提 Issue 和 PR！

- 🐛 发现 Bug？ → [提 Issue](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/issues)
- 💡 想加新功能？ → [提 Feature Request](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/issues)
- ✏️ 想改文档？ → Fork → 改 → 提 PR

---

## 📄 License

本项目采用 [MIT License](./LICENSE) 开源。

```
MIT License

Copyright (c) 2025 feichanggege

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<p align="center">
  Made with ☕ by <a href="https://github.com/feichanggege">feichanggege</a>
  <br>
  <sub>Powered by real e-commerce combat experience across Taobao, JD, Douyin & more.</sub>
</p>
