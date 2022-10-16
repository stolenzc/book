# PHP 语法基础

## PHP 基础介绍

### PHP简介

PHP（HyperText PreProcessor），超文本预处理器的字母缩写，是一种服务器端脚本语言，可以嵌入到HTML中

被 `<?php` 和 `?>` 包裹的就是php代码

```html
<html>
  <head>
    <title>Example</title>
  </head>

  <body>
    <p>
    <?php echo 'Hello World!';?>
    </p>
  </body>
</html>
```

将被解析为

```html
<html>
  <head>
    <title>Example</title>
  </head>

  <body>
    <p>Hello World!</p>
  </body>
</html>
```

### 功能

- 服务端脚本。需要 PHP 解析器（CGI或者服务器模块）、Web 服务器（Nginx、Apache）、浏览器
- 命令行脚本。只需要 PHP 解析器
- 桌面应用程序。通过 PHP-GTK 来开发，该模块不包括在基础 PHP 的安装中，需要额外安装

### 运行

1. 脚本运行

    `php hello.php`

    ```php
    <?php
    echo 'hello world';
    ```

    `chmod +x hello.php && ./hello.php`

    ```php
    #!/usr/bin/php
    <?php
    echo 'Hello World';
    ```

2. 命令行运行

   - `php -a` 交互模式
   - `php -r "echo 'Hello, World'";`

3. 服务器端

   - cgi，如 Nginx 的 fast-cgi
   - 模块，如 Apache 的 mod_php

4. 内置服务器

  进入项目根目录执行 `php -S localhost:8080`

## 基础语法

### PHP 标记

通常 PHP 标记为 <?php 和 ?>，输出内容可使用短格式 <? 和 ?>。所有这些标签内的部分都会被 PHP 解析器解析。

如果文件内容是纯 PHP 代码，最好在文件末尾删除 PHP 结束标记。这可以避免在 PHP 结束标记之后万一意外加入了空格或者换行符，会导致 PHP 开始输出这些空白。

```php
<?php

$a = 'Hello';
echo "$a World";
```

注意文件末尾省略了结束标签 `?>`

在 PHP5.4 以后短标签无需任何设置，都是合法标签

```php
<?="Hello Wolrd"?>
```

在 PHP7 中以下两个标记方式已经不再实用

- `<script language='php'></script>`
- `<%` 和 `%>`

### 从 HTML 中分离

通常情况下可以使用 `echo` 输出 HTML 页面

```php
<?php

$highlight = true;

echo "<html>
  <body>
    <p".($highlight ? " class='highlight'" : '').">
    This is a paragraph
    </p>
  </body>
</html>";
```

由于在一对开始和结束标记之外的内容都会被 PHP 解析器忽略，我们可以在 HTML 中需要使用 PHP 的地方在执行 PHP 程序，因此，上面例子可以写成

```php
<?php
$highlight = true;
?>
<html>
  <body>
    <p <?=$highlight ? "class='highlight'" : ''?>>
    This is a paragraph
    </p>
  </body>
</html>
```

### 指令分隔符

PHP 需要在每个语句后用分号 `;` 结束指令，如果后面还有新行，则代码段的结束标记包含了行结束。

### 注释

- 单行注释。 `//` 和 `#` 仅仅注释到行末或者当前的 PHP 代码块。
- 多行注释。注释在碰到第一个 `*/` 时结束

```php
<?php

# 单行注释
echo 'Hello World';

$a = 'abc';//单行注释

/**
 * 多行注释
 * 注释内容
 *
 */
```

## 数据类型

### 数据类型简介

php 支持 8 种数据类型

标量类型

- boolean（布尔型）
- integer（整型）
- float/double（浮点型）
- string（字符串）

复合类型

- array（数组）
- object（对象）

特殊类型

- resource（资源）
- NULL（无类型）

类型检测

- `var_dump()` 函数可以查看表达式的值和类型
- `gettype()` 函数用于检测变量类型
- `is_类型()` 判断变量是否为该类型，如 `is_int()`, `is_array()`

```php
<?php
$a = TRUE;
$b  = "foo";
$c = 0.1;
$d = 12;

if (is_string($b)) {
    echo "$b 是字符串".PHP_EOL;
}

if (is_int($c)) {
    echo "$c 是整型".PHP_EOL;
}

var_dump($a);
var_dump($b);
echo gettype($c).PHP_EOL;
echo gettype($d);

/*
foo 是字符串
bool(true)
string(3) "foo"
double
integer
*/
```

### Boolean 布尔类型

布尔类型表达了真值，可以为 `TRUE` 或 `FALSE`，不区分大小写

一下情况转化为 Boolean 类型时，为FALSE

- 布尔值 False 本身
- 整型值 0
- 浮点型值 0.0
- 空字符串，以及字符串 `"0"`
- 不包括任何元素的数组
- 特殊类型 NULL，包括未赋值的变量
- 从空标记生成的 SimpleXML 对象

```php
<?php

$a = TRUE;
$b = FALSE;
$c = 'abcde';

var_dump($a); // bool(true)
var_dump($b); // bool(false)

if ($a == 'abcde') {
    echo "hello\n";
}
// hello

$d = '';
$e = 0;
$f = false;
$g = "0";

var_dump($d == $e); // bool(true)
var_dump($e == $g); // bool(true)
var_dump($d == $f); // bool(true)
var_dump($e == $f); // bool(true)
```

### Integer 整型

整型可以使用十进制、十六进制（前加 `0x` ）、八进制（前加 `0` ）、二进制（前加 `0b` ），前面也可以加上符号（ `-` 或者 `+` ）

```php
<?php

$a = 1234; // 十进制数
$b = -123; // 负数
$c = 0123; // 八进制数 (等于十进制 83)
$d = 0x1A; // 十六进制数 (等于十进制 26)
```

整数溢出：如果一个数超出了 integer 的范围，会被解释为 float，如果执行结果超出了 integer 范围，也会返回 float。

```php
<?php

$a = 123445566;
$b = 9223372036854775807;
$c = 9223372036854775808;
$d = 50000000000000 * 1000000;

var_dump($a); // int(123445566)
var_dump($b); // int(9223372036854775807)
var_dump($c); // float(9.2233720368548E+18)
var_dump($d); // float(5.0E+19)
```

### float 浮点型

浮点型：也称为双精度 double 或实数 real

浮点数的字长和平台相关，通常最大值是 1.8e308 并具有 14 位十进制数字的精度

```php
<?php
$a = 1.234;
$b = 1.2e3;
$c = 7E-10;
```

### string 字符串类型

一个字符串就是一系列自负组成，其中每个字符等同于一个字节

- 单引号: 单引号内特殊字符和变量不会被解析
- 双引号: 双引号内的特殊字符和变量会被解析
- Heredoc: 与双引号类似，内部转义字符和变量可以被解析
- Nowdoc: 与单引号类似，无法解析转移字符和变量，语法为 Heredoc 开始标识符上加上单引号

```php
<?php

$a = 'Hello';
$b = '$a World';
$c = "$a World";

$d = <<<EOT
$a \n World
EOT;

$e = <<<'EOT'
$a \n $c
EOT;

var_dump($b);
var_dump($c);
var_dump($d);
var_dump($e);
```

### Array 数组

数组实际上是一个有序映射，映射是一种把 values 关联到 keys 的类型，由于数组元素的值也可以是另一个数组，所以也可以出现树形结构和多维数组

```php
<?php
$a = [
  "a" => "1",
  "b" => "2",
];

$b = ["a", "b"];

$c = [
  "a",
  "b",
  "c" => $a,
  "d" => $b,
];

var_dump($a); // array(a) {...}
var_dump($a[0]); // NULL 
var_dump($a["a"]); // string(1) "1"
var_dump($b); // array(2) {...}
var_dump($b[0]); // string(1) "a"
var_dump($b["a"]); // NULL
var_dump($c); // array(4) {...}
var_dump($c['c']); // array(2) {...}
var_dump($c['c']['b']); // string(1) "2"
```

注意

- 如果没有键名，则数组默认使用从 0 开始的数字键名（索引）
- 打印数组不存在的 key 的值时，直接返回NULL
- 数组可以多维嵌套，通过键名可以获取特定值

### Object 对象

使用 new 可以创建一个新的对象

```php
<?php
class foo
{
  function do()
  {
    echo "Action do";
  }
}

$f = new foo;
$f->do();
```

转换为对象

如果将一个对象转换成对象，它将不会有任何变化，如果其他任何类型的值被转换成对象，将会创建一个内置类 stdClass 的实例。如果该值为 NULL，则新的实例为空，array 转换为 object 将使键名成为属性名并具有相对应的值，除了数字键，不迭代就无法被访问。

```php
<?php

class A {}

$a = new A();
$b = (object)$a;
$c = (object)'A';
$d = (object)NULL;
$e = (object)['hello'=>'world'];
$f = (object)['a', 'b', 'c'=>'cc', 'd'=>'dd'];

var_dump($a); // object(A) {}
var_dump($b); // object(A) {}
var_dump($c); // object(stdClass) {["scalar"]=>string(1) "A"}
var_dump($c->scalar); // string(1) "A"
var_dump($d); // object(stdClass) {}
var_dump($e->hello); //string(5) "world"
var_dump($f); // object(stdClass) {}
var_dump($f->c); // string(2) "cc"
```

转换总结

- a 是对象，对象转换为对象不变化， a 和 b 相等
- 字符串 "A" 转换为对象时，自动生成 scalar 属性
- 数组转换为对象时，键名作为属性，键值作为属性值

### Resource 资源

资源 resource 是一种特殊变量，保存了外部资源的一个引用，如打开文件、数据库连接等，资源是通过专门的函数来建立和使用的

```php
<?php

$file = fopen($filename) // 打开文件
$db = mysqli_connect(); //数据库连接
```

转换为资源：由于资源类型变量保存为文件、数据库连接、图形画布区域等特殊的句柄，因此将其他类型的值转换为资源没有意义

释放资源：引用计数系统是 Zend 引擎的一部分，可以自动检测到一个资源不再被引用了（和 Java 一样）。这种情况下此资源使用的所有外部资源都会被垃圾回收系统释放。

### NULL

特殊的 NULL 值表示一个变量没有值，NULL 类型的唯一可能值就是 NULL，在下列情况下一个变量被认为是 NULL

- 被赋值为 NULL
- 未被赋值
- 被 `unset()`

NULL 类型的特点

- 不区分大小写，只有一个值，就是 NULL
- 将一个变量转换为 NULL 将不会删除该变量，只是返回 NULL 值

```php
<?php

$a = NULL;
var_dump($a); // NULL

$b = "abc";
var_dump($b); // string(3) "abc"

unset($b);
var_dump($b); // NULL
```

### 类型转换

PHP 是弱类型语言，定义变量的时候不需要指定变量类型，根据上下文自动解析为对应的变量类型

类型转换优先级：浮点型 > 整型 > 字符串

意味着类型

```php
<?php

$a = '1';
var_dump($a);

$b = $a + 2;
var_dump($b);

$c = $b + 1.2;
var_dump($c);

$d = $c + '456';
var_dump($d);

$e = $d + 'abc';
var_dump($e);
```

类型强制转换

在转换的变量前加上用括号括起来的目标类型

- (int), (integer) - 转换为整形 integer
- (bool), (boolean) - 转换为布尔类型 boolean
- (float), (double), (real) - 转换为浮点型 float
- (string) - 转换为字符串 string
- (array) - 转换为数组 array
- (object) - 转换为对象 object
- (unset) - 转换为 NULL (PHP 5)

```php
<?php
$a = 10;
$b = (boolean)$a;
var_dump($b); // bool(true)
```

## 变量

### 定义和规范

PHP 中的变量用美元符号 `$` 后面跟变量名来表示

- 变量名区分大小写
- 变量名可以由字母、数字、下划线组成
- 变量名只能以字母或者下划线开头，不能以数字开头

```php
<?php

$a = "var a"
$_b = "var _b"
$4c = "var 4c" // PHP Parse error: Syntax error
```

### 传值和引用

PHP 默认传值使用值传递，改变了原变量值，不会影响新变量的值

```php
<?php

$a = 1;
$b = $a;
$a = 2;

var_dump($a); // int(2)
var_dump($b); // int(1)
```

PHP 也可以使用 `&` 来进行引用传递，改变了原变量，新变量值也会收到影响，`&` 符号只能用在变量名前，无法使用在表达式前，如 `&(1 + 2)` 会报错

```php
<?php

$a = 1;
$b = &$a;
$a = 2;
var_dump($a); // int(2)
var_dump($b); // int(2)
```

### 预定义变量

PHP 提供了很多预定义变量。其中一些变量依赖于运行的服务器的版本和设置

- `$GLOBALS` 引用全局作用域中可用的全部变量
- `$_SERVER` 服务器和执行环境信息
- `$_GET` HTTP GET 变量
- `$_POST` HTTP POST 变量
- `$_FILES` HTTP 文件上传变量
- `$_REQUEST` HTTP Request 变量
- `$_SESSION` Session 变量
- `$_ENV` 环境变量
- `$_COOKIE` HTTP Cookies
- `$php_errormsg` 前一个错误信息
- `$HTTP_RAW_POST_DATA` 原生 POST 数据
- `http_response_header` HTTP 响应头

以下变量只在命令执行的时候生效

- `$argc` 传递给脚本的参数数目
- `$argv` 传递给脚本的参数数组

```php
<?php

var_dump($argc);
var_dump($argv);

// 执行脚本使用 php a.php 1 2 3
// int(4)
// array(4) {
//  [0] => string(8) "a.php"
//  [1] => string(1) "1"
//  [2] => string(1) "2"
//  [3] => string(1) "3"
// }
```

### 变量范围

变量范围代表变量的生效范围，大部分的 PHP 变量只有一个单独的范围，这个单独的范围跨度包含了 `include` 和 `require` 引入的文件。

```php
<?php

$a = 1;
include 'b.php';
```

函数使用外部变量可以用传参或外部变量实现

```php
<?php

$a = 'a';
$b = 'b';

function output_a(){
    echo $a;
}

function output($item){
    echo $item;
}

output_a(); // Undefined variable
output($b); // string(3) abc
```

```php
<?php

include "a.php";

var_dump($a);
var_dump($b);
```

### 全局变量

全局访问全局变量的两个方式

- 使用 `global` 声明在函数内使用全局变量
- 使用 `$GLOBALS` 数组来使用全局变量

```php
<?php

$a = 1;
$b = 2;
$c = 0;
$d = 0;

function sum1()
{
  global $a, $b, $c;
  $c = $a + $b;
  echo $c; // 3
}

function sum2()
{
  $GLOBALS['d'] = $GLOBALS['a'] + $GLOBALS['b'];
  echo $GLOBALS['d']; //3
}

sum1();
sum2();
```

### 静态变量

- 当程序离开作用域时，其值不丢失