# 鲁班打磨报告

目标仓库：`feichanggege/ecommerce-visual-copywriting-skill`
打磨日期：2026-06-13
基线提交：`f237dc3 Add usage examples`

## 1. 验料结果

挑战 1 - 真实问题：成立。电商视觉文案经常卡在“能写但不能落图”“卖点强但有合规风险”“设计师拿到仍要二次翻译”。

挑战 2 - 独特角度：唯一性来自工作流和合规规则库。它不是泛 copywriting，而是把主图、详情页、品类合规和设计执行说明合成一条 SOP。

挑战 3 - 安装理由：成立。用户安装它，是为了让 Agent 在电商图文案任务里稳定遵守确认门、行数限制、免责声明和分品类红线，而不是每次临时解释规则。

挑战 4 - 公共传播性：原仓库有 312 stars，说明题材已有传播信号；短板是首屏展示、安装路径、验证门和 marketplace 元数据不足。

验料结论：好料，继续打磨。优先补“公共 Skill 出生证”：首屏钩子、可见产物、一行安装、验证脚本、安全边界和发布元数据。

## 2. 访行记录

| 同类项目 | 链接 | 类型 | 一句话定位 | 可学的手艺 | 不能照搬的点 |
|---|---|---|---|---|---|
| dtc-copywriting-skills | https://github.com/coleschaffer/dtc-copywriting-skills | 直接/间接 | DTC marketing copywriting skills collection | 把营销任务拆成多个可安装技能 | 它偏 DTC 文案框架，不解决中国电商平台合规 |
| claude-copy | https://github.com/igoroliveirg/claude-copy | 间接 | Direct-response copywriting skills for Claude Code | 强调具体文案场景和技能包组合 | 偏英文直效营销，不适合作为合规规则来源 |
| copywriting-mastery-skill | https://github.com/Zzzeen2552/copywriting-mastery-skill | 手艺 | Master-level copywriting skill | 用“方法论来源”增强记忆点 | 大师背书型叙事不适合硬套到电商合规 |
| Sales-Page-Copywriting-Skill | https://github.com/yashaiguy-dev/Sales-Page-Copywriting-Skill | 间接 | Sales page copy generation with validation | 强调验证和反脆弱审稿 | 销售页结构不同于主图和详情页 |
| claude-code-copywriting-skills | https://github.com/robpalmer99/claude-code-copywriting-skills | 手艺 | Free Claude Code copywriting skills | README 直接说明安装后能做什么 | 不覆盖中文电商平台审核语境 |
| agent-skills-marketing | https://github.com/whyashthakker/agent-skills-marketing | 手艺 | Marketing skills collection for agents | 用技能合集定位降低理解成本 | 合集型仓库，不适合作为单一 Skill 首屏结构 |

## 3. 生态位判断

纵向结论：这个 Skill 从“私用的电商图文案 SOP”走向“公开可安装的电商视觉文案与合规工作流”。下一阶段方向不是堆更多平台口号，而是补可验证、可安装、可展示的公共资产。

横向结论：同类项目多强调 copywriting 框架、营销模板或英文直效文案；缺少“设计师可落图 + 中国电商平台合规 + 用户确认门”的组合。

交叉洞察：真正该抢的生态位不是泛营销文案，而是“电商视觉稿交付前的合规文案导演”。

一句话新定位：把产品资料和资质边界，转成设计师能直接上图的平台安全版主图和详情页文案。

## 4. 过尺结果

| 维度 | 权重 | 基线得分 | 打磨后目标 | 主要证据 | 优先级 |
|---|---:|---:|---:|---|---|
| Frontmatter 与触发条件 | 7 | 5 | 7 | 原描述有用途，但缺负触发和发布属性 | P1 |
| 工作流清晰度 | 12 | 10 | 12 | 已有 6 步 SOP 和确认门 | P1 |
| 失败模式编码 | 12 | 7 | 11 | 原有合规红线，缺关键失败模式清单 | P1 |
| 检查点设计 | 6 | 5 | 6 | 自审评分存在，发布验证缺失 | P1 |
| 可执行具体性 | 17 | 14 | 16 | 图 1-5 和模块清晰，安装说明可更短 | P1 |
| 资源整合度 | 4 | 3 | 4 | references/examples 存在，缺首页展示卡 | P2 |
| 整体架构 | 12 | 9 | 11 | 文件少而清楚，缺 marketplace 元数据 | P1 |
| 实测表现 | 23 | 12 | 20 | 缺自动验证脚本，示例可手动对账 | P0 |
| 反例与黑名单 | 7 | 5 | 7 | 合规词表已有，Skill 内需编码不要用于哪些场景 | P1 |
| 总分 | 100 | 70 | 94 | 以本次新增验证脚本和 README/SKILL 改写为目标 | P0 |

## 5. 慢刨改动

- 重写 `README.md`：首屏钩子、徽章、展示卡、效果示例、一行安装、触发方式、交付物、安全边界、验证说明。
- 重写 `SKILL.md`：强化 frontmatter、负触发、资质边界、用户确认门、失败模式和输出格式。
- 新增 `assets/showcase-output.svg`：GitHub 首屏可直接展示的输出卡。
- 新增 `tools/verify-skill.py`：零依赖发布检查和泄露扫描。
- 新增 `.claude-plugin/marketplace.json`：补 Claude plugin marketplace 元数据。

## 6. 回炉清单

- 发布后用 GitHub 页面检查 README 渲染，重点看 SVG、徽章、相对链接和代码块。
- 两周后查看 GitHub traffic，如果有浏览但 clone 少，优先补 demo GIF 或真实运行录屏。
- 下一轮可补 `README.en.md`，扩大英文 Agent Skill 生态传播面。
