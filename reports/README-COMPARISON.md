# 2026 春夏季与秋冬季课程 README 对比报告

核对日期：2026-09-20。对比范围为 LearningOS 四门课程的春夏季原始课堂模板、此次修改前的秋冬季 README 与学员指南，以及本次恢复后的版本。rCore 同时检查 `main` 和 `ch1` 至 `ch8`。

## 结论

春夏季原 README 确实包含教学内容。秋冬季改造时，首页更多用于领取、身份绑定、提交和计分；部分操作移到了学员指南，但模块知识点、教材导航、本地练习工具、环境和本地评测没有完整保留下来。原文曾另存为 `docs/UPSTREAM-2026s.md`，该文件后来也被删除，因此不能把所有减少的内容都解释为“换了位置”。

本次将有用教学内容与现有流程合并到四个秋冬季 README：领取仓库、准备环境、阅读教材、完成练习、本地测试、提交和查看成绩形成连续流程。春夏季保留原课程教学结构，换用自助领取入口，并修正已失效或会误导学员的操作步骤。

## 逐门对比

| 课程 | 春夏季原文包含什么 | 本次修改前的秋冬季情况 | 本次整合结果 |
| --- | --- | --- | --- |
| Rustlings | 本地与 Codespaces 使用、逐题运行和提示、全量检查、进度列表、综合练习、rust-analyzer、教材与贡献资料 | 保留领取、评分、轻量环境安装和教材顺序表；上述练习工具与学习说明缺失 | 补回 `run`、`hint`、`next`、`list`、`verify`、`lsp`，主题 README、三道综合练习、Codespaces 和扩展资料；保留 Windows MSVC 安装脚本及 `cargo run -- watch`；教材顺序表仍在最后 |
| 基础阶段 | 六个模块、24 项练习与知识点，交互工具、按键、逐题与全量测试、学习方法 | 首页主要为领取和评分表；学员指南只补充克隆、提交与看分，没有完整教学正文 | 补回六模块全部目录和知识点、Linux/RISC-V 环境、交互按键、提示与本地测试；保留现有 24 项权重和部分成绩上传说明 |
| rCore | 简明指导、详细教材、九章 API 链接、学习资源、用户程序、Docker、启动与官方本地检查器 | 保留分支、报告和评分；学员指南有简明指导和提交步骤，但缺少详细教材、API 和完整本地流程 | 补回教材和九章 API、环境、用户程序、运行、Docker 和本地检查器；测试版本与秋冬季 CI 对齐；完整保留报告、五章累计计分及排错说明 |
| ArceOS | 内核与组件目录、PPT/课程导航、依赖安装、完整测试、内存分配器挑战资料 | 首页与指南主要为领取、提交和六项评分；教学导航与本地环境缺失 | 补回课件、教材、目录用途、Rust/QEMU/musl 配置、六个单项测试与完整测试；保留挑战原理资料，说明旧活动流程的所属范围 |

## 保留、替换与整理的依据

| 原有内容 | 本次处理 | 原因 |
| --- | --- | --- |
| 教材、模块知识点、题目提示、API、PPT、挑战原理 | 保留并放回学习流程 | 学员理解与完成课程所需 |
| 现有自动领取、账号绑定、提交分支、报告要求、评分与错误处理 | 保留，并与教程衔接 | 是当前作业提交与成绩同步流程 |
| Rustlings Windows MSVC、macOS/Linux 配置脚本、教材对应表 | 保留 | 沿用本期已提供的配置方式与学习安排 |
| 学员指南中的有效步骤 | 合并到对应 README，旧指南只保留跳转链接 | 避免重复维护，同时保留原链接的可用性 |
| GitHub Classroom 领取入口 | 替换为春夏季或秋冬季 Issue 申请入口 | 新学员通过自动建仓流程领取作业 |
| Rustlings 又下载或克隆 `rust-lang/rustlings` 的安装步骤与按钮 | 从春夏季主流程移除；秋冬季在已分配仓库执行课程命令 | 原步骤会创建另一个仓库，与作业仓库及评测脱节；本地安装、Nix 配置、编辑器和贡献资料继续保留 |
| 删除整个 Rustlings 工作目录的卸载示例 | 从课程流程移除 | 对完成作业无帮助，且容易删掉学员练习 |
| 基础阶段“23 项” | 修正为 24 项 | 核对六模块实际目录和评分表均为 24 项 |
| 基础阶段不存在的上下文切换 README 链接 | 指向实际模块目录 | 两期仓库均不存在原链接目标 |
| 基础阶段全仓库单一目标 `cargo test --workspace` 示例 | 改为课程工具的全量检查 | 第 4 模块必须使用 RISC-V；工具会选择正确目标 |
| 基础阶段 Codespaces 的 `qemu-user-static` | 改为 `qemu-user` | 与仓库配置的 `qemu-riscv64` 运行命令对应 |
| rCore Docker 命令所在目录、先删除 `ci-user` 的步骤 | 明确在章节仓库根目录构建 Docker；已有检查器目录直接复用 | Docker 目标位于根 Makefile；无需先删目录 |
| rCore 第 9 章 | 保留为拓展 API 资料，课程分支说明到 `ch8` | 两期作业均只有 `ch1` 至 `ch8` |
| ArceOS 三套架构工具链全部安装的主流程 | 主流程配置六项练习需要的 RISC-V，其他架构保留上游资料入口 | 避免初学者安装当前作业不使用的工具链 |
| ArceOS `lab1` 分支、验证脚本与邮件活动规则 | 保留挑战资料，移除当前作业中不存在的分支操作 | 当前模板只有 `main`；旧活动不属于本期六项自动评测 |
| ArceOS 总脚本返回状态 | 补充查看各项结果与总分的方法 | 原脚本成功退出不等于六项测试全部通过 |

## 可核对的版本

下表链接固定到提交版本。行数只用于定位文本变化，不表示课程质量或内容保留比例。原教学源码、测试题、课件、许可证的内容未在本次教程整理中删除。

| 课程 | 春夏季原始 README | 秋冬季整理前 README | 秋冬季整合后 README | 春夏季入口调整后 README |
| --- | --- | --- | --- | --- |
| 导学阶段 · Rustlings | [206 行](https://github.com/LearningOS/rustling-classroom-2026s-rustling-2026s-rustling-classroom-template-1/blob/2f2152ac49dc56cf189dd08ffe4ef10870ccc195/README.md) | [96 行](https://github.com/LearningOS/2026a-rustling/blob/589f71c5812a948a24f1c11408c54a207bd227d8/README.md) | [130 行](https://github.com/LearningOS/2026a-rustling/blob/e067e9bbf32767f58b7173d7fdfb70ee2a9244ab/README.md) | [122 行](https://github.com/LearningOS/rustling-classroom-2026s-rustling-2026s-rustling-classroom-template-1/blob/89c279f345713ca6730d9815a2d39cf26f703256/README.md) |
| 基础阶段 · Rust 进阶与 OS 入门 | [151 行](https://github.com/LearningOS/2026s-oscamp-base-2026s-oscamp-base-exercise-oscamp-base-experiment/blob/1196ac363c2cba1dcd7f33cf584b5d746f396ffd/README.md) | [53 行](https://github.com/LearningOS/2026a-oscamp-base/blob/9710613fe39a5b3de7b57f0dac911a72abd9c0eb/README.md) | [185 行](https://github.com/LearningOS/2026a-oscamp-base/blob/afa3dcccc4abd5eb2ec09bc18b8903895930b61b/README.md) | [168 行](https://github.com/LearningOS/2026s-oscamp-base-2026s-oscamp-base-exercise-oscamp-base-experiment/blob/35122e46a44bce9c4a088a4f15bf613f0b507a63/README.md) |
| 专业阶段 · rCore-Tutorial | [80 行](https://github.com/LearningOS/2026s-oscamp-professional-2026s-rcore-rCore-Tutorial-Code/blob/6a82420303a607614293e5dd77951aafa564feec/README.md) | [46 行](https://github.com/LearningOS/2026a-rcore/blob/04e5a9b1f4be3bb6123b3940de0aae0841a0ba1f/README.md) | [150 行](https://github.com/LearningOS/2026a-rcore/blob/682979ec048d8fadea1da699e860d3fc8c172254/README.md) | [96 行](https://github.com/LearningOS/2026s-oscamp-professional-2026s-rcore-rCore-Tutorial-Code/blob/7f5a7904394ad848e6b2ce2bc15a30ab4401254b/README.md) |
| 项目先导阶段 · ArceOS | [85 行](https://github.com/LearningOS/2026s-oscamp-professional-2026s-arceos-arceos-classroom-2026s-arceos-oscamp/blob/85237911b8fb71ac94d7a7c51597ebec6b73e939/README.md) | [35 行](https://github.com/LearningOS/2026a-arceos/blob/87d0b2301022ddd9ca4ddc9cb4aabeb1078abbbd/README.md) | [138 行](https://github.com/LearningOS/2026a-arceos/blob/bb517b53a9ed19a7311c403c234fcdbe3eaa8a9b/README.md) | [91 行](https://github.com/LearningOS/2026s-oscamp-professional-2026s-arceos-arceos-classroom-2026s-arceos-oscamp/blob/80ccd4567a5d341895ffbfa8efb60cc818171b69/README.md) |

### 原文归档删除记录

这些提交确认 `docs/UPSTREAM-2026s.md` 曾被删除。旧版内容仍可通过 Git 历史查看，本次按教学用途整合，未恢复重复的整份归档文件。

- 导学阶段 · Rustlings：[删除记录](https://github.com/LearningOS/2026a-rustling/commit/ae3de0d9c6a41780631fa357d861b2bd6892d8d7)。
- 基础阶段 · Rust 进阶与 OS 入门：[删除记录](https://github.com/LearningOS/2026a-oscamp-base/commit/223a3429fdcb44f77fa8ebf78a82054d90898eab)。
- 专业阶段 · rCore-Tutorial：[删除记录](https://github.com/LearningOS/2026a-rcore/commit/765e3bdae02d67c0279c7bd72584a641fe56626a)。
- 项目先导阶段 · ArceOS：[删除记录](https://github.com/LearningOS/2026a-arceos/commit/09b905054b4a0edbf135579e1f61aa3359e43d03)。

## 春夏季入口切换与验证

新入口：[LearningOS/2026s-enroll](https://github.com/LearningOS/2026s-enroll)。新学员提交对应课程申请，系统从 Issue 作者读取 GitHub 登录名，准备仓库、检查课程配置、分配权限，最后发布正式仓库名并回复链接。

四个原始春夏季课堂模板已启用模板功能，继续作为新作业来源。课程凭证和课程配置沿用 LearningOS 原有组织 Secrets；新仓库设置固定学员身份。原 Classroom 学员仓库继续使用，领取代码能够识别对应的旧 fork 并保留代码、分支和成绩记录。配置检查只确认身份、凭证可用性及参数格式，不提交成绩。

| 课程 | 本人领取申请 | 新作业仓库 | 实际配置检查 |
| --- | --- | --- | --- |
| 导学阶段 · Rustlings | [申请 #1](https://github.com/LearningOS/2026s-enroll/issues/1) | [2026s-rustling-Alayfolk64](https://github.com/LearningOS/2026s-rustling-Alayfolk64) | [成功](https://github.com/LearningOS/2026s-rustling-Alayfolk64/actions/runs/35457947402) |
| 基础阶段 · Rust 进阶与 OS 入门 | [申请 #2](https://github.com/LearningOS/2026s-enroll/issues/2) | [2026s-oscamp-base-Alayfolk64](https://github.com/LearningOS/2026s-oscamp-base-Alayfolk64) | [成功](https://github.com/LearningOS/2026s-oscamp-base-Alayfolk64/actions/runs/35457975912) |
| 专业阶段 · rCore-Tutorial | [申请 #3](https://github.com/LearningOS/2026s-enroll/issues/3) | [2026s-rcore-Alayfolk64](https://github.com/LearningOS/2026s-rcore-Alayfolk64) | [成功](https://github.com/LearningOS/2026s-rcore-Alayfolk64/actions/runs/35458017104) |
| 项目先导阶段 · ArceOS | [申请 #4](https://github.com/LearningOS/2026s-enroll/issues/4) | [2026s-arceos-Alayfolk64](https://github.com/LearningOS/2026s-arceos-Alayfolk64) | [成功](https://github.com/LearningOS/2026s-arceos-Alayfolk64/actions/runs/35458058333) |

### 已完成的检查

- 领取代码 43 项本地测试通过；[云端代码检查](https://github.com/LearningOS/2026s-enroll/actions/runs/35457917813)通过。覆盖身份来源、异常重试、配置失败不发布、旧 Classroom 仓库复用及成绩分支保护等路径。
- 四门课程均完成真实 Issue 申请、自动建仓、实际配置检查、回复和关闭申请。核对四个仓库的固定学员身份及启用的评测工作流。
- 新 rCore 作业包含 `main` 与八个章节分支；发布前已清除从模板生成的 `gh-pages` 历史分支，正式作业仓库不含往期成绩。
- 两期共 24 个课程分支完成教程更新检查；秋冬季修改限于 README、指南跳转及基础阶段开发环境的 QEMU 包名。教学源码与评分规则没有随教程整理改写。
- 所有新 README 的本地链接、代码块与空白格式已检查；基础阶段 6 模块、24 个练习目录、Rustlings 25 项教材对应表与实际文件核对通过；开发环境脚本通过 Bash 语法检查。

### 本次验证范围

本次完成领取与配置的云端验证，没有重新完成全部练习，也没有向 OpenCamp 排行榜提交测试分数。原春夏季评分脚本继续使用；本次配置通过不等于重新验证了所有题目的评分或排行榜写入。恢复的本地 Rust/QEMU/Docker 教程依据仓库代码和工具配置核对，未逐项重新安装并运行完整实验。
