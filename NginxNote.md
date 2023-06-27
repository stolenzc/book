# Nginx 简介

## Nginx 是什么

Nginx 读音 `Engine X`, 很多工程师也喜欢读成'恩基克思'。

Nginx 是一款高性能的 HTTP 和反向代理服务器软件，第一个开源版本诞生于 2004 年，虽然诞生较晚但经过近二十年的发展，已经成为非常流行的 Web 服务器软件

Nginx 和 Apache 相同点

- 同是 HTTP 服务器软件，都采用模块化结构设计
- 支持通用语言接口，如 PHP、Python 等
- 支持正向代理和反向代理
- 支持虚拟主机及 SSL 加密传输
- 支持缓存及压缩传输
- 支持 URL 重写
- 模块多，扩展性强
- 多平台支持

## Nginx 的优势

- 轻量级：安装文件小，运行时 CPU 内存使用率低；
- 性能强：支持多核，处理静态文件效率高，内核采用的 poll 模型最大可以支持 50K 并发连接；
- 支持热部署，同时启动速度快，可以在不间断服务的情况下对软件和配置进行升级；
- 负载均衡，支持容错和健康检查；
- 代理功能强大，支持无缓存的反向代理，同时支持 IMAP/POP3/SMTP 的代理。

## Nginx 的缺点

- 相比 Apache 模块要少一些，常用模块都有，支持 LUA 语言扩展功能；
- 对动态请求支持不如 Apache；
- Windows 版本功能有限，受限于 Windows 的特性，支持最好的还是 Unix/Linux 系统

## Nginx 的工作原理

Nginx 由内核和一系列模块组成：内核提供 web 服务的基本功能，如启用网络协议、创建运行环境、接收和分配客户端请求、处理模块之间的交互。模块实现 Nginx 的各种功能和操作，Nginx 的模块从结构上分为核心模块、基础模块和第三方模块。

- 核心模块： HTTP 模块、EVENT 模块和 MAIL 模块
- 基础模块： HTTP Access 模块、HTTP FastCGI 模块、HTTP Proxy 模块和 HTTP Rewrite 模块
- 第三方模块： HTTP Upstream Request Hash 模块、Notice 模块和 HTTP Access Key 模块及用户自己开发的模块

这样的设计使 Nginx 方便开发和扩展，也正因此才使得 Nginx 功能如此强大。Nginx 的模块默认编译进 Nginx 中，如果需要增加或删除模块，需要重新编译 Nginx，这一点不如 Apache 的动态加载模块方便。如果有需要动态加载模块，可以使用由淘宝网发起的 Web 服务器 Tengine，在 Nginx 的基础上增加了很多高级特性，完全兼容 Nginx，已被国内很多网站采用。

## Nginx 架构

Web 历史上最流行最经典的环境是 LAMP（Linux + Apache + Mysql + PHP），至今仍有大量网站采用此架构，Apache 默认配置在未优化的情况下比较占用 CPU 和内存。

借助于 Nginx 的轻量和高性能，LNMP 架构只是将 LAMP 环境中的 Apache 换成 Nginx，于是另一经典 LNMP 架构就诞生了。

LNMP 在服务器硬件配置相同时，相对于 LAMP 会使用更少的 CPU 和内存，是小型网站、低配服务器和 VPS 的福音。
