# Git 基础

## `.git` 目录结构

`watch -n 1 -c tree -a` - 监控目录结构变化命令

```bash
.
└── .git
    ├── HEAD
    ├── config
    ├── description
    ├── hooks
    ├── info
    │   └── exclude
    ├── objects
    │   ├── info
    │   └── pack
    └── refs
        ├── heads
        └── tags
```

## 目录结构介绍

- `HEAD` - 记录当前分支
- `config` - 配置文件
- `description` - 项目描述
- `hooks` - 钩子目录
- `info` - 信息目录
- `info/exclude` - 忽略文件
- `objects` - Git 对象存储目录
- `objects/info` - 信息目录
- `objects/pack` - 压缩包目录
- `refs` - 分支和标签目录
- `refs/heads` - 分支目录
- `refs/tags` - 标签目录

# config 配置

## 配置文件

Git配置主要存在三个位置

- `/etc/gitconfig` - 系统级配置，针对所有使用这个系统的用户，使用配置命令需要携带 `--system` 指令
- `~/.gitconfig` / `~/.config/git/config` - 用户级配置，针对当前使用系统的用户，使用配置命令需要携带 `--global` 指令
- `.git/config` - 只针对该仓库，可以使用 `--local` 来使用，默认也是操作该仓库

三个文件优先级为， `仓库>用户>系统`

## 配置命令

`git config` 配置相关命令

基础选项

- `--list` / `-l` - 列出配置
- `--show-origin` - 列出配置的值是从哪个文件中获取的
- `--global` / `--system` / `--local` - 设置配置生效范围

基础配置选项

- `user.name` - 用户名配置
- `user.email` - 用户邮箱配置
- `core.editor` - 设置编辑器
  - `vim` - vim
  - `notepad` - Windows记事本
  - `code --wait` - VSCode
- `alias.快捷键 原始指令` - 设置快捷键别名
  - `git config --global alias.co commit` - 设置别名
  - `git co` - 使用

日常使用配置项

- `init.defaultbranch` - 设置默认分支
  - `git config --global init.defaultbranch main` - 设置默认分支为 `main`
- `pull.rebase true` - 将 `—rebase` 设置为 `git pull` 默认选项

不常使用项

- `credential.helper` - 设定密码存储方式
  - `cache --timeout 900` - 将密码存储在缓存中，默认15分钟内不需要重复输入密码
  - `store --file <path>` - 将密码存储在指定位置
  - 默认不会进行缓存密码每次都要重新输入密码
- `commit.template <file_path>` - 设置提交模板
- `core.pager <pager>` - 设置分页器，默认为 `less`
  - `git config --global core.pager ''` - 取消分页器
- `core.excludesfile <ignore_file_path>` - 设置读取指定文件中的忽略项
  - `git config --global core.excludesfile ~/.gitignore_global` - 指定忽略 `~/.gitignore_global` 文件中的忽略项
- `help.autocorrect <num>` - 命令输入错误后等待时长执行匹配到的命令
  - `help.autocorrect 50` - 输入命令错误5秒后执行匹配到的命令
- `user.signingkey` - 设置GPG签署密钥

# object 存储对象

## `.git/objects` 目录结构

```bash
.git/objects
├── b2
│   └── 204a3d4efe86db540fb6e0d6a9c08d2dc42190
├── info
└── pack
```

## Git 如何存储代码

- Git 是一个内容寻址文件系统
- Git 的核心部分是一个简单的键值对数据库 (key-value data store)
- 所有的对象都是通过 SHA-1 哈希值来索引，而不是通过文件名
- 文件的内容作为 Git 对象存储在 `.git/objects` 目录中

## Git 对象

`git cat-file <sub_command> <sha-1>` - 查看 object 文件内容

- `-t` - 查看 object 类型
- `-p` - 查看 object 所存储内容
- `-s` - 查看 object 所存储文件的大小

`<file object> <file size>\0<file content>` - object 存储的原始内容

- `<file object>` - object 类型，可选为 blob、tree、commit
- `<file size>` - 内容长度，需要将文件结束符包括在内
- `<file content>` - 文件内容

### blob

数据，该文件只记录文件内容

### tree

一个指向数据对象或其他tree的指针，类似于一个目录对象，该文件会记录当前目录下所有的文件或目录的id，格式如下

```text
100644 blob b2204a3d4efe86db540fb6e0d6a9c08d2dc42190	hello.py
```

文件类型，Git只会使用以下三种

- 100644表示普通文件
- 100755表示可执行文件
- 120000表示符号链接

### commit

一个记录作者、上一个commit对象、当前 Git 管理的根目录 tree 对象的一个指针

```text
tree 19196323cc78928c5ab3a9440b3743e2cd70384e
author zhouc <1022590068@qq.com> 1691542143 +0800
committer zhouc <1022590068@qq.com> 1691542143 +0800
```

# index 暂存区

`git ls-files`  - 查看暂存区的文件名

- -s - 查看文件的详细内容

index 文件中存储了所有纳入版本控制的文件 blob object 的 id、文件类型、文件路径

```text
100644 b2204a3d4efe86db540fb6e0d6a9c08d2dc42190 0	hello.py
```

`<file_type> <blob_object_id> <file_version> <file_name>`

- `<file_type>` - 文件类型，同 blob 的文件类型
- `<blob_object_id>` - blob 的文件 sha1
- `<file_version>` - 文件的版本，默认为 0，当出现冲突时，会出现同一个文件的多个版本
- `<file_name>` - 文件的名称，包含所处的工作目录相对路径，如 `statistic/index.html`

# Git Refs 目录

记录分支和tag的目录

heads 目录下记录了所有分支的最新指向

tags 目录下记录了所有 tag 所指向的 commit 对象

# Git 合并

## Fast-Forward 合并

# Git 垃圾回收

