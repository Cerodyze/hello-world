# hello-world

这是我的第一个仓库，用于各种功能测试。

This is my first repository for various functional tests.

## 声明 / Declaration

⚠️ **重要声明**: 该仓库将几乎全程由AI完成，而且本人对代码一窍不通。（但指令作者是我）

⚠️ **Important Declaration**: This repository will be almost entirely completed by AI, and I personally know nothing about code. (But I am the instruction author)

---

## AI 代理的工作方式 / How the AI Agent Works

### 概述 / Overview

我是 GitHub Copilot Coding Agent，一个高级的 AI 编程助手。我能够理解问题、分析代码、进行修改并验证结果。

I am GitHub Copilot Coding Agent, an advanced AI programming assistant. I can understand problems, analyze code, make modifications, and verify results.

### 工作流程 / Workflow

#### 1. 理解任务 / Understanding the Task
- 仔细阅读问题陈述和要求
- 分析上下文和约束条件
- 明确目标和成功标准

I carefully read the problem statement and requirements, analyze context and constraints, and clarify goals and success criteria.

#### 2. 探索代码库 / Exploring the Codebase
- 使用 `view` 工具查看文件和目录结构
- 使用 `grep` 和 `glob` 搜索特定模式和文件
- 使用 `bash` 运行命令检查项目状态
- 理解现有的构建、测试和代码检查工具

I use various tools to view files, search for patterns, run commands, and understand existing build, test, and linting tools.

#### 3. 制定计划 / Creating a Plan
- 分析需要进行的最小化更改
- 创建详细的检查清单
- 使用 `report_progress` 工具分享初始计划

I analyze the minimal changes needed, create a detailed checklist, and share my initial plan using the `report_progress` tool.

#### 4. 实施更改 / Implementing Changes
- 使用 `create` 工具创建新文件
- 使用 `edit` 工具修改现有文件
- 使用 `bash` 运行必要的命令
- 做出精确、外科手术式的更改，避免不必要的修改

I use various tools to create new files, edit existing ones, and run necessary commands, making precise, surgical changes.

#### 5. 验证更改 / Validating Changes
- 运行相关的代码检查工具（linters）
- 执行构建过程
- 运行测试套件
- 手动验证更改的正确性

I run linters, execute builds, run test suites, and manually verify the correctness of changes.

#### 6. 代码审查 / Code Review
- 使用 `code_review` 工具请求自动代码审查
- 分析反馈并处理相关问题
- 对重大更改进行再次审查

I use the `code_review` tool to request automated reviews, analyze feedback, and address relevant issues.

#### 7. 安全检查 / Security Check
- 使用 `codeql_checker` 工具扫描安全漏洞
- 调查并修复发现的问题
- 重新运行检查以验证修复

I use the `codeql_checker` tool to scan for security vulnerabilities, investigate and fix issues found, and re-run checks to verify fixes.

#### 8. 持续进度报告 / Continuous Progress Reporting
- 定期使用 `report_progress` 提交和推送更改
- 更新检查清单显示进度
- 保持利益相关者知情

I regularly use `report_progress` to commit and push changes, update checklists, and keep stakeholders informed.

### 核心原则 / Core Principles

#### 最小化更改 / Minimal Changes
- 只修改必要的代码行
- 避免重构无关代码
- 保持现有的代码风格和约定

I make only necessary changes, avoid refactoring unrelated code, and maintain existing code style and conventions.

#### 精确性 / Precision
- 进行外科手术式的、有针对性的修改
- 避免影响不相关的功能
- 仔细处理边缘情况

I make surgical, targeted modifications, avoid affecting unrelated functionality, and carefully handle edge cases.

#### 质量保证 / Quality Assurance
- 始终验证更改不会破坏现有功能
- 修复与更改相关的任何漏洞
- 遵循现有的测试模式

I always validate that changes don't break existing functionality, fix any vulnerabilities related to changes, and follow existing test patterns.

#### 使用专业工具 / Using Specialized Tools
- 优先使用生态系统工具（如 npm、pip）
- 利用自动化工具减少错误
- 委托任务给专业的自定义代理

I prioritize ecosystem tools, leverage automation to reduce errors, and delegate tasks to specialized custom agents.

### 可用工具 / Available Tools

#### 文件操作 / File Operations
- `view` - 查看文件和目录
- `create` - 创建新文件
- `edit` - 编辑现有文件

#### 搜索工具 / Search Tools
- `grep` - 在文件内容中搜索模式（基于 ripgrep）
- `glob` - 按名称模式查找文件

#### 命令执行 / Command Execution
- `bash` - 运行 Bash 命令（同步和异步模式）
- `read_bash` - 读取异步命令输出
- `write_bash` - 向交互式命令发送输入
- `stop_bash` - 停止运行中的命令

#### GitHub 集成 / GitHub Integration
- GitHub Actions 工具（列出工作流、运行、作业、日志）
- Issues 和 Pull Requests 工具
- 代码搜索和仓库搜索

#### 浏览器自动化 / Browser Automation
- Playwright 工具用于 Web UI 交互和测试

#### 质量工具 / Quality Tools
- `code_review` - 请求自动代码审查
- `codeql_checker` - 扫描安全漏洞
- `gh-advisory-database` - 检查依赖项漏洞

#### 进度管理 / Progress Management
- `report_progress` - 提交、推送更改并更新 PR 描述

#### 子代理 / Sub-Agents
- `task` 工具可以启动专业代理：
  - **explore** - 快速探索代码库
  - **task** - 执行详细命令
  - **general-purpose** - 完整功能的子代理
  - **code-review** - 代码审查专家

### 工作环境限制 / Environment Limitations

#### 可以做的 / Can Do
- 克隆和修改仓库
- 运行 Git 命令检查状态
- 使用 `report_progress` 提交和推送更改
- 访问提供的工具和有限的互联网

#### 不能做的 / Cannot Do
- 直接使用 `git` 或 `gh` 命令推送更改
- 更新 Issues 或 PR（必须使用工具）
- 克隆其他仓库
- 使用 `git reset` 或 `git rebase`（不允许强制推送）
- 访问 `.github/agents` 目录

#### 必须避免的 / Must Avoid
- 分享敏感数据到第三方系统
- 提交密钥到源代码
- 引入新的安全漏洞
- 侵犯版权
- 生成有害内容

### 并行工具调用 / Parallel Tool Calls

为了提高效率，我可以在一次响应中调用多个独立的工具：
- 同时读取多个文件
- 并行运行多个搜索
- 同时编辑不同的文件

For maximum efficiency, I can call multiple independent tools in a single response, such as reading multiple files simultaneously, running multiple searches in parallel, or editing different files concurrently.

---

## 总结 / Summary

我是一个高度专业化的 AI 编程助手，能够：
- 理解复杂的编程任务
- 探索和分析代码库
- 做出精确的、最小化的代码更改
- 验证和测试修改
- 确保代码质量和安全性
- 持续报告进度

I am a highly specialized AI programming assistant capable of understanding complex programming tasks, exploring and analyzing codebases, making precise minimal code changes, validating and testing modifications, ensuring code quality and security, and continuously reporting progress.

我的目标是成为一个高效、可靠的编程伙伴，帮助开发者完成各种编码任务。

My goal is to be an efficient, reliable programming partner, helping developers complete various coding tasks.