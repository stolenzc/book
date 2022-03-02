# GIT 基础命令

## GIT 帮助与配置

`man git <command>` / `git help <command>` - 查询git命令手册

`git config [--global] user.name <username>` - 配置git用户名

`git config [--global] user.email <email>` - 配置git用户邮箱

`git config [--global] core.editor <editor>` - 配置git编辑器



## GIT 常用命令

`git status [opt]` - opt 常用的有以下几个，常结合使用：

- `-s`：表示 short 模式显示，即只显示最精简内容
- `-b`：表示显示分支（branch），也是 git status 的参数默认之一