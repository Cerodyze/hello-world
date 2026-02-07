# Linux 常用命令 / Common Linux Commands

本文档整理了日常使用中最常用的 Linux 命令。

This document summarizes the most commonly used Linux commands in daily usage.

---

## 1. 文件与目录导航 / File & Directory Navigation

```bash
# 显示当前工作目录 / Print current working directory
pwd

# 切换目录 / Change directory
cd /path/to/directory
cd ~                   # 回到家目录 / Go to home directory
cd ..                  # 回到上级目录 / Go to parent directory
cd -                   # 回到上一个目录 / Go to previous directory

# 列出文件和目录 / List files and directories
ls
ls -l                  # 详细列表 / Long listing format
ls -a                  # 显示隐藏文件 / Show hidden files
ls -la                 # 详细列表含隐藏文件 / Long listing with hidden files
ls -lh                 # 人类可读的文件大小 / Human-readable file sizes
```

## 2. 文件与目录操作 / File & Directory Operations

```bash
# 创建目录 / Create a directory
mkdir dirname
mkdir -p path/to/dirname   # 递归创建 / Create parent directories as needed

# 删除文件 / Remove a file
rm filename
rm -r dirname              # 递归删除目录 / Remove directory recursively
rm -f filename             # 强制删除 / Force remove

# 复制文件或目录 / Copy files or directories
cp source destination
cp -r source_dir dest_dir  # 递归复制目录 / Copy directory recursively

# 移动或重命名文件 / Move or rename files
mv oldname newname
mv file /path/to/destination

# 创建空文件 / Create an empty file
touch filename
```

## 3. 文件查看与编辑 / Viewing & Editing Files

```bash
# 查看文件内容 / View file contents
cat filename
less filename              # 分页查看 / View with paging
head filename              # 查看前 10 行 / View first 10 lines
head -n 20 filename        # 查看前 20 行 / View first 20 lines
tail filename              # 查看后 10 行 / View last 10 lines
tail -f filename           # 实时追踪文件变化 / Follow file changes in real time

# 使用文本编辑器 / Use text editors
nano filename
vi filename
vim filename
```

## 4. 文件搜索 / File Searching

```bash
# 搜索文件 / Find files
find /path -name "filename"
find /path -type f -name "*.txt"   # 按类型和名称搜索 / Search by type and name

# 搜索文件内容 / Search file contents
grep "pattern" filename
grep -r "pattern" /path            # 递归搜索 / Recursive search
grep -i "pattern" filename         # 忽略大小写 / Case-insensitive search
grep -n "pattern" filename         # 显示行号 / Show line numbers

# 快速定位命令 / Locate a command
which command
whereis command
```

## 5. 文件权限 / File Permissions

```bash
# 修改权限 / Change permissions
chmod 755 filename         # rwxr-xr-x
chmod +x filename          # 添加执行权限 / Add execute permission
chmod -w filename          # 移除写权限 / Remove write permission

# 修改文件所有者 / Change file owner
chown user:group filename
chown -R user:group dirname    # 递归修改 / Recursive change
```

## 6. 系统信息 / System Information

```bash
# 查看系统信息 / View system information
uname -a                   # 全部信息 / All information
hostname                   # 主机名 / Hostname

# 查看磁盘使用 / View disk usage
df -h                      # 磁盘空间 / Disk space
du -sh dirname             # 目录大小 / Directory size

# 查看内存使用 / View memory usage
free -h

# 查看系统运行时间 / View system uptime
uptime
```

## 7. 进程管理 / Process Management

```bash
# 查看进程 / View processes
ps aux                     # 所有进程 / All processes
top                        # 实时进程监控 / Real-time process monitor
htop                       # 增强版进程监控 / Enhanced process monitor (if installed)

# 终止进程 / Kill a process
kill PID
kill -9 PID                # 强制终止 / Force kill

# 后台运行 / Run in background
command &
nohup command &            # 忽略挂断信号 / Ignore hangup signal
```

## 8. 网络命令 / Network Commands

```bash
# 网络连通性测试 / Test network connectivity
ping hostname

# 查看网络接口 / View network interfaces
ip addr
ifconfig                   # 旧版命令 / Legacy command

# 下载文件 / Download files
wget URL
curl -O URL

# 查看端口监听 / View listening ports
ss -tuln
netstat -tuln              # 旧版命令 / Legacy command
```

## 9. 压缩与解压 / Compression & Extraction

```bash
# tar 压缩与解压 / tar compress and extract
tar -czf archive.tar.gz dirname    # 压缩 / Compress
tar -xzf archive.tar.gz            # 解压 / Extract
tar -tf archive.tar.gz             # 查看内容 / List contents

# zip 压缩与解压 / zip compress and extract
zip -r archive.zip dirname         # 压缩 / Compress
unzip archive.zip                  # 解压 / Extract
```

## 10. 用户与权限 / Users & Permissions

```bash
# 查看当前用户 / View current user
whoami

# 切换用户 / Switch user
su - username

# 以管理员权限执行 / Execute with admin privileges
sudo command

# 查看用户信息 / View user information
id username
```

## 11. 管道与重定向 / Pipes & Redirection

```bash
# 管道：将一个命令的输出传给另一个命令 / Pipe: pass output to another command
command1 | command2
ls -l | grep ".txt"

# 输出重定向 / Output redirection
command > file             # 覆盖写入 / Overwrite
command >> file            # 追加写入 / Append

# 输入重定向 / Input redirection
command < file
```

## 12. 常用快捷操作 / Useful Shortcuts

```bash
# 清屏 / Clear screen
clear                      # 或按 Ctrl+L / Or press Ctrl+L

# 查看命令历史 / View command history
history

# 命令别名 / Command aliases
alias ll='ls -la'
alias ..='cd ..'

# 查看命令帮助 / View command help
man command
command --help
```

---

> 💡 **提示 / Tip**: 使用 `man <command>` 可以查看任何命令的详细手册。
>
> Use `man <command>` to view the detailed manual for any command.
