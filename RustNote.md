# Rust Note

## 1. Rust 基础

### 1.1 Rust 简介

Rust 诞生于 2006 年，Mozilla 于 2009 年开始赞助该项目，于 2010 年开源。Rust 是一门系统编程语言，它的设计目标是提供一种安全、并发、实用的编程语言。

### 1.2 Rust 版本历史

1. 早期阶段(2006 - 2010) Mozilla研究院的格雷顿·霍尔（Graydon Hoare）在 2006 年首次开发。
2. 0.1 版本 (2012) 第一个官方预览版
3. 1.0 版本 (2015) 第一个稳定版本
4. 1.79 版本 (2024) 最新版本

### 1.3 工具介绍

1. `rustc` 编译器 - Rust 语言的编译器
2. `cargo` 包管理工具 - Rust 语言的包管理工具
3. `rustup` 工具链管理器 - Rust 语言的工具链管理器

### 1.4 环境

参考官方文档 [安装 Rust](https://www.rust-lang.org/zh-CN/tools/install)。

- 安装: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- 配置: `export PATH="$HOME/.cargo/bin:$PATH"`
- 校验: `rustc --version`
- 升级: `rustup update`
- 卸载: `rustup self uninstall`

### 1.5 Hello World

```rust
// hello.rs
fn main() {
    println!("Hello, world!");
}
```

运行：

1. rustc 编译运行

    - 编译: `rustc hello.rs`
    - 运行: `./hello`

2. cargo 管理运行

    - 创建项目: `cargo new hello`
    - 运行: `cargo run`
    - 编译: `cargo build`

### 1.6 cargo 命令

- `cargo new project_name` - 创建一个新的 Rust 项目
- `cargo build` - 编译项目
- `cargo run` - 运行项目
- `cargo check` - 检查项目
- `cargo test` - 测试项目
- `cargo doc` - 生成项目文档
- `cargo publish` - 发布项目项目到 crates.io
- `cargo clean` - 清理项目
- `cargo update` - 更新项目依赖

cargo 默认会创建一个如下的项目结构：

```shell
.
├── Cargo.toml
└── src
    └── main.rs
```

- `Cargo.toml` - 项目配置文件
- `src` - 项目源码目录

使用 `cargo new project_name --lib` 可以创建一个库项目。

使用 `cargo build` 后会在项目目录下生成一个 `target` 目录，其中包含编译生成的二进制文件。

```shell
.
├── Cargo.toml
├── src
│   └── main.rs
└── target
    └── debug
        ├── project_name
```

`cargo run` 会自动编译并运行项目。

使用 `cargo build --release` 可以生成一个优化后的二进制文件。

## 2. Rust 变量与数据类型

### 2.1 变量和可变性

#### 2.1.1 变量声明

Rust 中使用 `let` 关键字声明变量。变量后面可以跟一个冒号 `:` 和类型名，但是不是必须的，Rust 可以根据变量的值推断出类型。还可以将类型放在变量值的后面

```rust
fn main() {
    let a: i32 = 5; // 显式指定类型
    let b = 5; // 根据值推断类型
    let c: i32; // 未初始化变量
    let d = 5i32; // 后缀指定类型
}
```



#### 2.1.1 不可变变量

Rust 中的变量默认是不可变的，使用 `let` 关键字声明。定义后不可再次赋值。但是可以被再次定义来遮蔽。

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);   // 5

    // x = 6; // error: cannot assign twice to immutable variable

    let x = 7;  // 正常工作
    println!("The value of x is: {}", x);   // 7
}
```


