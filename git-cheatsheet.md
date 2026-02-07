# Git 常用操作 / Common Git Operations

本文档整理了日常开发中最常用的 Git 命令。

This document summarizes the most commonly used Git commands in daily development.

---

## 1. 配置 / Configuration

```bash
# 设置用户名 / Set username
git config --global user.name "Your Name"

# 设置邮箱 / Set email
git config --global user.email "your.email@example.com"

# 查看配置 / View configuration
git config --list
```

## 2. 仓库初始化与克隆 / Repository Init & Clone

```bash
# 初始化新仓库 / Initialize a new repository
git init

# 克隆远程仓库 / Clone a remote repository
git clone https://github.com/user/repo.git
```

## 3. 基本工作流 / Basic Workflow

```bash
# 查看状态 / Check status
git status

# 添加文件到暂存区 / Stage files
git add <file>
git add .          # 添加所有更改 / Stage all changes

# 提交更改 / Commit changes
git commit -m "描述信息 / commit message"

# 查看提交历史 / View commit history
git log
git log --oneline  # 简洁模式 / Compact mode
```

## 4. 分支操作 / Branch Operations

```bash
# 查看分支 / List branches
git branch

# 创建新分支 / Create a new branch
git branch <branch-name>

# 切换分支 / Switch branch
git checkout <branch-name>
git switch <branch-name>       # Git 2.23+ 推荐 / Recommended since Git 2.23+

# 创建并切换分支 / Create and switch to a new branch
git checkout -b <branch-name>
git switch -c <branch-name>    # Git 2.23+ 推荐 / Recommended since Git 2.23+

# 合并分支 / Merge a branch
git merge <branch-name>

# 删除分支 / Delete a branch
git branch -d <branch-name>
```

## 5. 远程操作 / Remote Operations

```bash
# 查看远程仓库 / List remote repositories
git remote -v

# 添加远程仓库 / Add a remote repository
git remote add origin https://github.com/user/repo.git

# 推送到远程 / Push to remote
git push origin <branch-name>

# 拉取远程更改 / Pull remote changes
git pull origin <branch-name>

# 获取远程更新（不合并）/ Fetch remote updates (without merging)
git fetch origin
```

## 6. 撤销与回退 / Undo & Reset

```bash
# 撤销工作区修改 / Discard changes in working directory
git checkout -- <file>
git restore <file>             # Git 2.23+ 推荐 / Recommended since Git 2.23+

# 取消暂存 / Unstage a file
git reset HEAD <file>
git restore --staged <file>    # Git 2.23+ 推荐 / Recommended since Git 2.23+

# 回退到上一个提交 / Reset to the previous commit
git reset --soft HEAD~1        # 保留更改 / Keep changes staged
git reset --hard HEAD~1        # 丢弃更改 / Discard changes
```

## 7. 暂存工作 / Stashing

```bash
# 暂存当前修改 / Stash current changes
git stash

# 查看暂存列表 / List stashes
git stash list

# 恢复暂存 / Apply stash
git stash pop                  # 恢复并删除暂存 / Apply and drop
git stash apply                # 恢复但保留暂存 / Apply but keep
```

## 8. 查看差异 / Viewing Differences

```bash
# 查看工作区与暂存区差异 / Diff between working directory and staging area
git diff

# 查看暂存区与最新提交的差异 / Diff between staging area and last commit
git diff --staged

# 比较两个分支 / Compare two branches
git diff <branch-1> <branch-2>
```

## 9. 标签 / Tags

```bash
# 创建标签 / Create a tag
git tag v1.0.0

# 创建带注释的标签 / Create an annotated tag
git tag -a v1.0.0 -m "版本 1.0.0 / Version 1.0.0"

# 推送标签到远程 / Push tags to remote
git push origin --tags
```

---

> 💡 **提示 / Tip**: 使用 `git help <command>` 可以查看任何命令的详细文档。
>
> Use `git help <command>` to view detailed documentation for any command.
