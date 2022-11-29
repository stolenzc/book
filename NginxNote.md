# Nginx 使用笔记

## Nginx 基础命令使用

Nginx 支持的信号

|信号|命令行参数|功能|
|---|---|---|
|TERM / INT|stop|快速关闭 Nginx 服务|
|QUIT|quit|安全关闭 Nginx 服务|
|HUP|reload|热加载配置文件|
|WINCH||安全关闭工作进程|
|USR1|reopen|重新创建日志文件|
|USR2||平滑更新 Nginx 执行文件|