# HTML

## HTML简介

HTML（超文本标记语言）是一种用于创建网页的标准标记语言。 HTML 不需要编译，可以直接由浏览器执行，它的解析依赖于浏览器的内核。 它不是一种编程语言，而是一种标记语言。

HTML 不区分大小写

## HTML 网页结构

```html
<!DOCTYPE html>
<html>
    <head>
        <title>HTML 简介</title>
    </head>
    <body></body>
    <!-- 注释 -->
</html>
```

- `<!DOCTYPE html>` - 文档声明头。他告诉了浏览器，本文档处理的是 HTML 文档
- `html` - 根元素标签，表示文档的开始
- `head` - 网页的头部标签，设置网页的相关信息
- `title` - 网页标题标签
- `body` - 文档主体标签，主要显示区域
- `<!-- 注释 -->` - 该标签为注释格式，浏览器中不会显示注释

## 标签通用样式

- `background-color:red` - 设置背景颜色
- `font-family:console` - 设置字体
- `color:green` - 设置颜色
- `font-size:50px` - 设置字体大小
- `text_align:center` - 文本对齐

```html
<html>
    <body>
        <p style="background-color:red;font-family:arial;color:green;font-size:50px;">HTML 样式</p>
    </body>
</html>
```

## 头标签

头标签中通常有以下几种标签

- `<title>` - 指定整个网页的标题，在浏览器最上方显示
- `<base>` - 为页面上的所有链接规定默认地址或默认目标
- `<meta>` - 提供有关页面的基本信息
- `<link>` - 定义文档与外部资源的关系
- `<style>` - 定义了HTML文档的样式文件引用地址
- `<script>` - 加载脚本文件

## Meta 标签

`<meta http-equiv="refresh" content="3;http://www.baidu.com">`

- `name`
	- `keywords` - 为搜索引擎定义关键词
	- `description` - 为网页定义描述内容
	- `author` - 定义网页作者
	- `viewport` - 定义视口，`content="width=device-width, initial-scale=1.0"` 表示视口宽度等于屏幕宽度
- `http-equiv`
	- `refresh` - 定义几秒刷新，如果时间后面有网址，则跳到该网页
	- `Content-Type` - 定义字符集

## body 标签

- `bgcolor` - 设置整个网页的背景颜色
- `background` - 设置整个网页的背景图片
- `text` - 设置网页中的文本颜色
- `leftmargin` - 网页的左边距。IE浏览器默认是8个像素
- `topmargin` - 网页的上边距
- `rightmargin` - 网页的右边距
- `bottommargin` - 网页的下边距
- `link` - 表示a标签默认显示的颜色
- `alink` - 表示鼠标点击a标签但是还没有松开时的颜色
- `vlink` - 表示点击a标签完成之后显示的颜色

## 简单标签

- `<br />` - 换行
- `<hr />` - 水平线
- `&nbsp;` - 半角的不断行的空白格
- `&ensp;` - 半角的空格
- `&emsp;` - 全角空格
- `&gt;` - 大于符号 `>`
- `&lt;` - 小于符号 `<`
- `&gte` - 大于等于
- `&lte` - 小于等于
- `&quot;` - 引号 `"`
- `&copy;` - 版权符号
&	和号	&amp;
￥	人民币	&yen;
©	版权	&copy;
®	注册商标	&reg;
°	摄氏度	&deg;
±	正负号	&plusmn;
×	乘号	&times;
÷	除号	&divide;
²	平方2（上标2）	&sup2;
³	立方3（上标3）	&sup3;
- `<h1>标题内容</h1>` - 标题标签，h1到h6
- `<strong>内容</strong>` `<b>内容</b>` - 字体加粗
- `<em>内容</em>` `<i>内容</i>` - 字体倾斜

```html
<ul>
    <li class="li">姓&emsp;&emsp;名：<input type="text" /></li>
    <li class="li">手&ensp;机&ensp;号：<input type="text" /></li>
    <li class="li">电子邮箱：<input type="text" /></li>
</ul>
```

## 图像标签

`<img />`

- `src` - 图片的链接  
- `alt` - 图片加载失败显示  
- `title` - 为鼠标悬停显示文字  
- `width` - 为宽度  
- `height` - 为高度
- `Align` - 图片的水平对齐方式，属性值可以是：left、center、right
- `border` - 给图片加边框（描边），单位是像素，边框的颜色是黑色
- `Hspace` - 图片左右的边距
- `Vspace` - 图片上下的边距

## 链接标签

`<a>内容</a>`

- `href` - 链接的地址，`#name值`为当前页面锚点跳转  
- `target` - 打开网页的位置
	- `_blank` - 空白页打开  
	- `_self` - 当前页打开
- `name` - 定义锚点

## 列表

`<ul>li标签内容</ul>` - 无序列表

- `type` - 无序列表前符号样式
	- `disc` - 实心圆，默认  
	- `square` - 实心框  
	- `circle` - 空心圆

`<ol>li标签内容</ol>` - 有序列表

- `type` - 有序列表前符号样式
	- `1` - 数字  
	- `a/A` - 字母大小写  
	- `i/I` - 罗马数字大小写

`<dl><dt></dt><dd></dd></dl>` - 自定义列表

- `dl` - 声明定义列表  
- `dt` - 声明列表项  
- `dd` - 定义列表项内容

示例:
```html
<dl>
	<dt>所属学院</dt>
	<dd>计算机学院</dd>
	<dt>专业</dt>
	<dd>计算机软件工程</dd>
</dl>
```

## 表格

- `<table></table>`
	- `border` - 设置表格边框宽度  
	- `cellspacing` - 边框宽度，html5不支持  
	- `align` - 水平对齐方式
		- `left` - 居左  
		- `center` - 居中  
		- `right` - 居右
	- `valign` - 垂直对齐
		- `top` - 顶部对齐  
		- `middle` - 中部对齐  
		- `bottom` - 底部对齐  
		- `baseline` - 基线对齐

- `<caption></caption>` - 表格标题
- `<thead></thead>` - 表格页眉
- `<tfoot></tfoot>` - 表格页脚
- `<tbody></tbody>` - 表格主题
- `<tr></tr>` - 表格行
- `<th></th>` - 表格头
- `<td></td>` - 单元格
	- `colspan` - 跨行
	- `rowspan` - 跨列

注意：如果使用 `thead`、`tbody`、`tfoot`元素，就必需使用全部元素，他们的顺序是 `thead`、`tfoot`、`tbody`

```html
<table border="1" cellspacing="5" align="center">
	<tr>
		<td>第一个单元格</td>
		<td colspan="2">第二个单元格</td>
	</tr>
	<tr>
		<td>第三个单元格</td>
		<td>第四个单元格</td>
		<td>第五个单元格</td>
	</tr>
</table>
```

## 表单

### 原始内容

- `<form></form>` - 表单
	- `name='值'` - 规定表单的名称  
	- `action='值'` - 提交表单的URL  
	- `method='get/post'` - 提交方式  
	- `enctype='值'` - 提交表单前进行编码，使用MIMO类型  
	- `target='_blank/_self/_parent/_top'` - 何处打开表单url  
	- `autocomplete='on/off'` - 是否启动表单自动完成  
	- `novalidate='novalidate'` - 不验证表单
- `<input type="text" [value="默认值"]/>` - 输入内容
	- `type` - 类型
		- `text` - 文本框
		- `password` - 密码框
		- `submit` - 提交按钮
		- `reset` - 重置按钮
		- `button` - 按钮
		- `radio` - 单选框
		- `checkbox` - 复选框
		- `file` - 上传文件框
		- `image` - 图片域
	- `placeholder` - 文本框预显示内容
	- `value` - 显示值，如果是按钮，则为按钮上显示的值，如果是输入框，则为输入框内填充值
	- `name` - 控件名称，单选框和复选框需要name一致，才能识别为一组
	- `checked="checked"` - 单选框或复选框选中状态
	- `disable="disable"` - 单选框或复选框禁用状态
	- `cols` - 多行文本框设置宽度
	- `rows` - 多行文本框设置高度


密码框: `<input type="password" [placeholder="密码"]/>`

提交按钮: `<input type="submit" value="按钮内容" />`

重置按钮: `<input type="reset" value="按钮内容" />`

单选框/单选按钮: `<input type="radio" name="xxx" [checked="checked"] />`

按钮: `<input type="button" value="按钮内容" />`

复选框: `<input type="checkbox" name="xxx" [disabled="disabled"] />`

下拉菜单: `<select name="xxx"><option>菜单内容</option></select>`

多行文本框: `<textarea name="xxx" cols="字符宽度" rows="行数"></textarea>`

上传文件框: `<input type="file" accept=".png, .jpg, .jpeg"/>`

图像域: `<input type="image" width="100" height="100" border="2" src="上传图片">`

提示信息标签: `<lable for="绑定控件id名"></label>`

表单字段集: `<fieldset></fieldset>`

字段级标题: `<legend></legend>`

### html5 新增

datalist

`datalist` 元素用于为文本框提供一个可供选择的列表

```html
<input type="text" name="myColor" id="myColor" list="mySuggestion" />
    <datalist id="mySuggestion">
      <option>black</option>
      <option>blue</option>
      <option>green</option>
      <option value="red"> </option>
      <option value="white"> </option>
      <option value="yellow"> </option>
    </datalist>
```

autocomplete

`autocomplete` 属性规定表单是否应该启用自动完成功能：自动完成允许浏览器预测对字段的输入，浏览器基于之前键入过的值，应该显示出在字段中填写的选项。可选项为`on`和`off`

autofocus

`autofocus` 属性规定在页面加载时，域自动地获得焦点。适用于所有 `<input>` 标签的类型。

form

`form` 属性规定输入域所属的一个或多个表单。`form` 属性适用于所有 `<input>` 标签的类型。`form` 属性必须引用所属表单的 id。

```html
<form action="#" method="get" id="user_form">
    First name:<input type="text" name="fname" />
</form>

Last name: <input type="text" name="lname" form="user_form" />

```

multiple

`multiple` 属性规定输入域中可选择多个值，适用于以下类型的 `<input>` 标签：`email` 和 `file`。

```html
<input type="file" name="file" multiple="multiple" />
```

novalidate

`novalidate` 属性规定在提交表单时不应该验证 `form` 或 `input` 域，适用于form和部分input类型

pattern

`pattern` 属性规定用于验证 input 域的模式（pattern）。模式（pattern） 是正则表达式。`pattern` 属性适用于以下类型的 `<input>` 标签：`text`, `search`, `url`, `telephone`, `email` 以及 `password`。

placeholder

`placeholder` 属性提供一种提示（hint），描述输入域所期待的值。适用于以下类型的 `<input>` 标签：`text`, `search`, `url`, `telephone`, `email` 以及 `password`

required

`required` 属性规定必须在提交之前填写输入域（不能为空）。适用于以下类型的 `<input>` 标签：`text`, `search`, `url`, `telephone`, `email`, `password`, `date pickers`, `number`, `checkbox`, `radio` 以及 `file`。

新增input类型

email, url, number, range

number和range属性：
- max: 最大值
- min: 最小值
- value: 默认值
- step: 数字间隔

时间日期选择器：
- date - 选取日、月、年
- month - 选取月、年
- week - 选取周和年
- time - 选取时间（小时和分钟）
- datetime - 选取时间、日、月、年（UTC 时间）注意：此类型已被弃用，目前大多数浏览器都不再支持。
- datetime-local - 选取时间、日、月、年（本地时间）

color 类型用于选择颜色

## 7. 菜单

`<select name="select"></select>`
> `size`: 表示下拉框展示的数据长度，更多数据使用滚动条
选项内容: `<option value="提交值", selected="selected">展示值</option>`

## 8. 文本域

`<textarea></textarea>`

> `clos` 表示列数
>
> `rows`: 表示行数
## 9. 框架

`<iframe></iframe>`

> `src`: 地址
>
> `width`: 宽
>
> `height`: 高
>
> `frameborder`: 边框宽度
将a标签的target设置为和iframe的name属性值一致，则可以点击a标签在iframe中加载网页

## 10. HTML5标签

### section

`<section>` 表示文档中的一个区域（或节）。比如章节、页眉、页脚或文档中的其他部分，一般来说会包含一个标题。

### article

`<article>` 标签定义独立的内容。常常使用在论坛帖子，报纸文章，博客条目，用户评论等独立的内容项目之中。`article` 可以嵌套，内层的 `article` 对外层的 `article` 标签有隶属关系。

### nav

`<nav>` 标签定义导航链接的部分：描绘一个含有多个超链接的区域，这个区域包含转到其他页面，或者页面内部其他部分的链接列表。

### header

`<header>` 标签定义文档的页眉，通常是一些引导和导航信息。它不局限于写在网页头部，也可以写在网页内容里面。

### footer

`<footer>` 标签定义 section 或 document 的页脚，包含了与页面、文章或是部分内容有关的信息，比如说文章的作者或者日期。 它和 `header` 标签使用基本一样，可以在一个页面中多次使用，如果在一个区段的后面加入了 `footer` 标签，那么它就相当于该区段的页脚了。

### aside

`<aside>` 标签表示一个和其余页面内容几乎无关的部分，被认为是独立于该内容的一部分并且可以被单独的拆分出来而不会使整体受影响。其通常表现为侧边栏或者嵌入内容。他们通常包含在工具条，例如来自词汇表的定义。也可能有其他类型的信息，例如相关的广告、笔者的传记、web 应用程序、个人资料信息，或在博客上的相关链接。

## 11. Web Storage

localStorage

`localStorage.setItem(key,value)` - 在本地客户端存储一个字符串类型的数据。

`localStorage.setItem.key=value` - 也可以像这样直接存储。

`localStorage.getItem(key)` - 读取已存储在本地的数据，获取键值。

`localStorage.key` - 也可以像这样直接获取值。

`localStorage.removeItem(key)` - 移除已存储在本地数据，通过键名作为参数删除数据。

`localStorage.clear()` - 也可以一次性清除

sessionStorage用法和localStorage用法类似

# 二. CSS

## 1. 基本信息

注释: `/* */`

## 2. 选择器

1. 标签选择器

语法: `元素名称{属性:属性值;}`

例句: `p{background:red;}`

2. id选择器

语法: `#id名称{属性:属性值;}`

例句: `#para1{text-align:center;}`

3. class选择器

语法: `.class类名{属性:属性值;}`

例句: `.top{width:200px;}`

4. *通配符（全局选择器）

语法: `*{属性:属性值;}`

例句: `*{padding:0;margin:0;}`

5. 交集选择器

语法: `选择器1选择器2{属性:属性值;}`

例句:`h1#center{color:red;}`

注意: 两个选择器中不能有空格，必须连续书写

6. 并集选择器

语法: `选择器1,选择器2{属性:属性值;}`

例句: `h1,div,#ppp{background:red;}`

7. 后代选择器

语法: `选择器1 选择器2{属性:属性值;}`

例句: `p div{color:red;}`

8. 子选择器

语法: `选择器1>选择器2{属性:属性值;}`

例句: `p>div{属性:属性值;}`

9. 伪类选择器
语法:
> `a:link{属性:属性值;}` - 超链接的初始状态
>
> `a:visited{属性:属性值;}` - 超链接被访问后的状态
>
> `a:hover{属性:属性值;}` - 鼠标悬停,即鼠标滑过超链接的状态
>
> `a:active{属性:属性值;}` - 超链接被激活的状态,即鼠标按下时超链接的状态
## 3. 显示和隐藏

`display:none;` - 隐藏元素,该方式隐藏在页面中不占位

`visibility:hidden;` - 隐藏元素,该方式隐藏的元素在页面中占位

## 4. 背景

background - 简写属性，作用是将背景属性设置在一个声明中

background-attachment - 背景图像是否固定或者随着页面的其余部分滚动
> scroll - 默认,滚动
>
> fixed - 不滚动
>
> inherit - 继承父元素设置
background-color - 设置元素的背景颜色
> 可以使用颜色的单词,也可以使用rgb来表示颜色(#000000)
background-image - 把图像设置为背景(url(floder/img.gif))
> 默认值是none,如果需要设置背景色,需要设置一个url值.
background-position - 设置背景图像的起始位置
> top/bottom/left/right/center/100px/5cm
background-repeat - 设置背景图像是否及如何重复
> no-repeat/repeat/repeat-x/repeat-y
## 5. 文本

1. 文本样式的font属性
font-size - 文本大小
> xx-small/x-small/small/medium/large/x-large/xx-large
font-family - 文本字体

font-weight - 文本粗细:(400对应默认字体)

font-style - 文本倾斜
> normal - 默认,正常字体
>
> italic - 倾斜字体
>
> oblique - 倾斜字体
>
> inherit - 继承父元素样式
color - 文本颜色

line-heigh - 文本行高
> normal - 默认值
>
> number - 设置数字,与当前字体相乘
>
> length - 固定的行间距
2. 文本样式的text属性

text-align - 水平对齐方式
> left/right/center/justify(两端对齐)
vertical-align - 垂直对齐方式
> top/buttom/middle
3. 文本样式修饰的运用规范

text-decoration - 文本修饰
> none/underline(下划线)/overline(上划线)/line-through(添加删除)/blink(删除)
text-indent - 文本缩进
> value(数值,可以取负值,缩进在左边,只对首行起作用)
letter-spacing - 字符间距
> value(英文字母之间的间距)
word-spacing - 字间距
> value(英文单词之间的间距)
white-space - 元素空白的处理方式
> normal - 空白被浏览器忽略
>
> pre - 空白会被浏览器保留
>
> nowrap - 文本不会换行
>
> pre-wrap - 保留空白符序列，但是正常地进行换行
>
> pre-line - 合并空白符序列，但是保留换行符
text-transform - 控制元素中的字母
> capitalize - 文本中的每个单词以大写字母开头
>
> uppercase - 所有字母转大写
>
> lowercase - 所有字母转小写
text-shadow - 文字添加阴影
> h-shadow - 必需,水平阴影的位置,允许负值
>
> v-shadow - 必需,垂直阴影的位置,允许负值
>
> blur - 可选,模糊的距离
>
> color - 阴影的颜色
word-wrap - 自动换行
> normal - 默认,只允许在断字典换行
>
>break-word - 在长单词或url内部进行换行
## 6. 列表

list-style - 简写属性,用于把所有用于列表的属性设置在一个声明中

list-style-image - 将图像设置为列表项标志

list-style-position - 设置列表中列表项标志的位置
> inside - 列表项目标记放置在文本以内，且环绕文本根据标记对齐
>
> outside - 默认值，保持标记位于文本的左侧
list-style-type - 设置列表项标志的类型	
> none - 无标记
>
> disc - 默认，标记是实心圆
>
> circle - 标记是空心圆
>
> square - 标记是实心方块
>
> list-style-type:url(floder/img.gif) - 图片作为列表符号
## 7. 盒子模型

overflow - 控制内容溢出元素框时在对应的元素区间内添加滚动条
> visible - 默认值。内容不会被修剪，会呈现在元素框之外。
>
> hidden - 内容会被修剪，并且其余内容是不可见的。
>
> scroll - 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
>
> auto - 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
text-overflow - 针对文本(必需和overflow:hidden;white-space:nowrap;一起使用)
> clip - 修剪文本
>
> ellipsis - 显示省略号来代表被修剪的文本
>
> string - 使用给定的字符串来代表被修剪的文本
`width:值` - 盒模型的宽

`height:值` - 盒模型的高

`background-color:值` - 盒模型的背景

`background-image:url(图片地址)` - 盒模型的背景图片

`border:线型(solid/dashed/dotted/double) 粗细(数值＋单位) 颜色;` - 盒模型的边框

`border-style` - 设置样式

`border-width` - 边框宽度

`border-color` - 设置颜色

`border-bottom` - 下边框

`border-top` - 上边框

`border-left` - 左边框

`border-right` - 右边框

# 三. JavaScript基础语法

## 1.基本介绍

js是javascript的缩写，是web标准中的行为标准，主要负责网页中内容的改变

js是编程语言，是脚本语言。主要针对脚本开发

**注意:js中严格区分大小写**

1)内联 -> js代码写在标签事件相关属性中,例如:onclick

2)内部 -> js代码写在script标签中(script标签放在html中任何位置都有效)

3)外部 -> js代码写在js文件中,然后通过script标签在html中导入（导入相当于执行）

## 2.注释(同C)

单行注释://

多行注释:`/*       */`

## 3.数据类型

### 3.1 关键字
```javascript
break else new var typeof
case finally return void
catch for switch while
default if throw delete
in try do instanceof
```
### 3.2 数据类型
Number:数字类型
String:字符串
Boolean:布尔值
Array:数组
Object:对象
Map:map对象(同python中的字典)(ES6)
Set:set对象(同python中的集合,(元素不重复))(ES6)
NaN:not a number,注意:NaN===NaN结果为false,判断是否为NaN用isNaN()
```javascript
NaN === NaN //false
isNaN(NaN) //true
```
null:表示空
undefined:表示未定义
判断数据类型的方法用typeof
```javascript
typeof 123; //number
```
### 3.3 变量
#### 3.2.1 变量名命名规范
数字 字母 _ $组成,数字不能开头
使用驼峰命名方式
#### 3.2.2 直接赋值
变量名 = 值
注意:不管声明在什么地方,都是全局的
#### 3.2.3 var 变量名
var 变量名 = 值
注意:如果声明在函数中,那么这个变量只能在函数中使用
#### 3.2.4 let 变量名
let 变量名 = 值
注意:let声明的变量的作用域是当前{}中,如果没有声明在{}中就没有约束效果
#### 3.2.5 多个变量同时赋值
ES6中新增了构析方法,可以同时对多个变量进行赋值
```javascript
var [x, y, z] = ['hello', 'JavaScript', 'ES6']
```
### 3.4 常量
声明方法:const 常量名 = 值
## 4.运算符
### 4.1 数学运算符
`+, -, *, /, %, **(幂运算) ++自增加运算`
### 4.2 比较运算符
`>, <, ==, !=, >=, <=, ===, !==`
`==\!=` -> 先自动转换类型,再进行比较
`===\!==` -> 不自动转换类型,直接比较
### 4.3 逻辑运算符
逻辑与&&    逻辑或||     逻辑非!
## 5.判断\循环结构
### 5.1 选择结构
#### 5.1.1 if语句
1)
if(条件语句){
​	代码段
}
2)
if(条件语句){
​	代码段1
}else{
​	代码段2
}
3)
if(条件语句1){
​	代码段2
}else if(条件语句2){
​	代码段2
}else if(条件语句3){
​	代码段3
}else{
​	代码段N
}
#### 5.1.2 switch语句
switch(表达式){
​	case 值1:{
​		代码段2
​	}
​	case 值2:{
​		代码段2
​	}
​	......
​	default:{
​		代码段N
​	}
}
#### 5.1.3 三目运算符
表达式?表达式1:表达式2
### 5.2 循环结构
#### 5.2.1 while循环
语法一:
while(条件语句){
​	循环体
}
语法二:
do{
​	循环体
}while(条件语句)
#### 5.2.2 for循环
语法一:
for(变量 in 序列){
​	循环体
}
注意:变量取到的不是元素,是下标或者属性名
语法二:
for(表达式1;表达式2;表达式3){
​	循环体
}
#### 5.2.3 循环中的关键字
break,continue用法同C语言和Python语言
## 6.函数
### 6.1 函数的声明
function 函数名(参数名1,参数名2,...){
​	函数体
​	return 返回值
}
说明: 无返回值其实是返回undefined
### 6.2 函数的参数 
#### 6.2.1 关键字参数无效
```javascript
function stu(name,age){
	console.log('我是'+name+',我今年'+age)
}
stu(age=18,name=’小明’) //我是18,我今年小明
```
#### 6.2.2 arguments
js中所有的函数,都可以接收不定长的参数.除了通过形参以外,可以通过函数中的arguments去获取实参
#### 6.2.3 rest
ES6中新定义了一个函数参数rest,rest主要是接受除了赋值意外多余的传入参数,以数组的形式保存,rest只能写在最后面,前面用三个点隔开
```javascript
function foo(a, b, ...rest) {
	console.log('a = ' + a);
	console.log('b = ' + b);
	console.log(rest);
}
foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]
```
### 6.2 匿名函数
变量 = function (参数名1,参数名2,...){
​	函数体
}
### 6.3 箭头函数
(参数列表)=>{函数体}
箭头函数的this始终指向外层调用这的object
```javascript
//写法一
func3 = (x, y)=>x+y
console.log(func3(10, 20))
//写法二
func3 = (x, y)=>{
	return x+y
}
```
### 6.4 迭代器
和python中一样,定义方法为function后面加`*`号
```javascript
function* fib(max) {
	a = 0,
	b = 1,
	n = 0;
	while (n < max) {
		yield a;
		[a, b] = [b, a + b];
		n ++;
	}
	return;
}
```
## 7.字符串

### 7. 1 字符串相关属性

字符串.length

### 7. 2 字符串相关方法

用`arr = new Array`方式创建后用`console.log(arr)`打印,然后在浏览器中展开就能看到全部的方法

`字符串.toUpperCase()`	-	把一个字符串全部变为大写

`字符串.toLowerCase ()`	-	把一个字符串全部变为小写

`字符串.indexOf (字符串2)`	-	搜索字符串2在字符串中出现的位置,成功返回位置下标,失败返回-1

`字符串.lastIndexOf(字符串)`	-	从右查找str中是否有括号中的字符串,有返回第一个字符的下标,没有返回-1

`字符串.substring(下标1,下标2)`	-	返回字符串下标1到下标2的字符串,不包含下标2

`字符串.substr(起始下标,截取长度)`	-	从起始下标开始,截取指定长度的字符串

`字符串.charAt(下标)`	-	获取下标对应的值

`字符串.charCodeAt(下标)`	-	获取对应下标值的ASCII码值

`字符串.localCompare(另一个字符串)`	-	如果字符串大得1,另一个字符串大得-1,相同得0

`字符串.replace(原来字符,新字符)`	-	返回一个替换后的字符串,(不是改str的内容)全部替换用正则

`字符串.split(字符)`	-	用指定字符对原字符串进行分割

`String.fromChatCode(编码)`	-	获取编码对应的字符(类方法)

### 7. 3 获取字符:字符串[下标]

**注意**:js中的下标只有正值`0~长度-1`

字符无法进行赋值操作

### 7. 4 相关运算

\+ -> js中字符串支持加运算,运算方法是只要加运算中有字符串,就把其他所有参与运算的变量都转换为字符串参与运算

### 7.5 转义字符

\n – 换行

\t – 制表

\\ - 反斜杠

\x## - 用十六进制表示ASCII

\u#### - 用十六进制表示Unicode

ES6用反引号表示多行字符串

```javascript
console.log(`多行
	字符串
测试`);
```

### 7.6 格式化字符串

用反引号可以进行格式化字符串

```javascript
name = ‘小明’
console.log(\`你好,${name}\`)   //你好,小明
```
## 8.数组
### 8.1 查 - 获取元素
1)获取单个元素:数组[下标]
2)遍历
方法一:
for(变量 in 数组) ->遍历拿到下标
方法二   
数组.forEach(function(元素,下标){
​	遍历后做的事情
})
// 同时遍历取到元素和下标
3)用属性查:
数组名.indexOf(元素) – 返回元素在字符串中的位置
数组名.indexOf(下标) – 返回字符串指定下标中的元素
数组名.lastIndexOf(值) - 从数组结尾往前寻找，返回第一个匹配的位置
数组名.slice(起始下标,终止下标) – 截取数组中从起始下标到终止下标(不包含)的字符并返回
### 8.2 增 – 增加元素
数组名.push(元素) - 在数组的最后添加一个元素
数组名.splice(开始下标, 0, 添加元素或列表) -> 将元素或列表添加到开始下标处
数组名.unshift(元素1,元素2,...) – 在数组开头添加多个元素
### 8.3 删 – 删除元素
数组名.pop() -> 删除数组的最后一个元素,并返回
数组名.shift() -> 删除数组的第一个元素,并返回
数组名.splice(开始下标,个数) -> 从开始下标开始删除指定个元素
### 8.4 改 – 修改元素
数组名[下标值] = 值
### 8.5 排序
数组名.sort(函数)  ->  会产生新的数组,也会修改原数组
直接使用数组名.sort() -> 会将元素转换为字符串进行比较
sort可以传入函数对排序进行定制化
```javascript
var arr = [10, 20, 1, 2];
arr.sort(function (x, y) {
	if (x < y) {
		return 1;
	}
	if (x > y) {
		return -1;
	}
	return 0;
});     // [20, 10, 2, 1]
```
### 8.6 数组方法
数组名.length – 返回组数的元素个数
数组名. concat(数组2) – 将数组2的元素拼接在数组1后面并返回,不改变数组1
数组名.join(字符) – 将数组元素用字符进行连接,返回一个字符串
数组名.reverse() - 将数组原数组倒置（改变原数组）
### 8.7 map和reduce
8.7.1 map
map定义在Array中,作用是将Array中每一个元素都作用于map内的函数,使数组变为一个新的数组
```javascript
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(arr.map(String));  // ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```
8.7.2 reduce
reduce接收两个参数,返回一个参数,使数组以某一种方式运算得到一个值
```javascript
var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
	return x + y;
});     // 25
```
### 8.8 filter
用于过滤数组中的元素,后两个参数可以省略,返回true则元素保留,返回false则删除
```javascript
var arr = ['A', 'B', 'C'];
var r = arr.filter(function (element, index, self) {
	console.log(element);     // 依次打印'A', 'B', 'C'
	console.log(index);   // 依次打印0, 1, 2
	console.log(self);     // self就是变量arr
	return true;
});
```
## 9.对象
### 9.1 创建对象
1)对象值:{属性名1:属性值1,属性名2:属性名2.....}
2)new创建对象
```javascript
obj2 = new Object()
obj2.name = '张三'
```
### 9.2 构造方法
用来创建对象的方法(相当于python中的类)
1)声明构造方法
function 类名(){
​	this.属性名1 = 属性值1
​	this.属性名2 = 属性值2
​	 ....
​	return this
}
2)通过构造方法创建对象
对象 = new 构造方法名()
注意:this相当于python中的self, 谁调用就指谁
### 9.3 添加对象属性
1)给一个对象添加属性:对象.属性名 / 对象[属性名]
2)给指定类的所有对象添加属性
类型名.prototype.属性名 = 值
### 9.4 判断对象中是否有某属性
属性名 in 对象名
## 10. 迭代对象(iterable)
ES6中引入的新的数据类型
Array Map Set都输入iterable
遍历iterable使用for...of...语法
```javascript
'use strict';
var a = [1, 2, 3];
for (var x of a) {
	console.log(x)
}
console.log('你的浏览器支持for ... of');
```
for...of是遍历元素本身 
## 11. 数学方法
Math.round(数据)四舍五入
Math.ceil(数据)向上取整
Math.floor(数据)向下取整
Math.max(多个数据)取最大值
Math.min(多个数据)取最小值
Math.abs(数据)取绝对值
Math.pow(x,y)x的y次方
Math.sqrt(数据)开平方
parseInt(Math.random() * (y - x + 1) + x):随机生成xy之间的的一个整数,包含xy
## 12. 时间与日期方法
`var d1 = Date()`	-	得到当前时间,括号中赋值表示得到指定时间对象，如果传入元组注意，月份从零开始数，不传表示为当前时间
`var d4 = new Date(2019,0,1,12,13,24)`	-	表示一月一日
对象方法:
`d1.getFullYear`
`d1.getMonth`
`d1.getDate`//获取日期
`d1.getDay`//获取星期
`d1.getHours`
`d1.getMinutes`
`d1.getSeconds`
`d1.getMilliseconds`//获取毫秒
`d1.getTime`//获取距离1970年的毫秒数
时间计算结果为毫秒。
## 13. base64/百分号编码
btoa('字符串')	-	将字符串转换为base64编码
atob('base64编码')	-	将64编码转换为字符串
encodeURIComponent('字符串')	-	将字符串转换为百分号编码
decodeURIComponent('百分号编码')	-	将百分号编码转换为字符串
# 四. DOM
## 1.DOM简介
DOM(document object model)    -    文档对象模型
js中默认创建了document对象,表示网页内容.整个document是一个树结构,网页中添加的标签是数结构的节点(又叫元素),如果想要在js中获取网页中的标签,都要通过document去获取
## 2.DOM获取节点
### 2.1 直接获取节点
#### 2.1.1 通过id获取标签
`document.getElementById('id值')` -> 返回当前页面中id是指定值的标签 
#### 2.1.2 通过class获取标签
`document.getElementsByClassName('class值')` -> 返回当前页面中所有class是指定值的标签,返回的是序列(类似数组)
**注意:此处不是数组,故不能用for-Each方式进行遍历**
#### 2.1.3 通过标签名获取标签
`document.getElementsByTagName('标签名')` -> 返回当前页面中所有指定类型的标签,返回的是序列(类似数组)(其实返回的是对象,对象的属性是每一个节点对象)
#### 2.1.4 通过name获取
`document.getElementsByName('name属性值')`
#### 2.1.5 通过选择器获取
`document.querySelector('CSS选择器')`	->	如果有多个，则返回第一个
`document.querySelectorAll('CSS选择器')`	->	返回所有匹配对象
### 2.2 根据节点获取父子节点
#### 2.2.1 获取父节点
节点.parentElement -> 获取指定节点的父节点
#### 2.2.2 获取子节点
节点.children -> 获取指定节点所有的子节点,返回一个序列
节点. firstElementChild -> 获取第一个子节点
节点. lastElementChild -> 获取最后一个子节点
节点.childNodes -> 除了子标签以外,会将标签中的文字信息也作为子标签
## 3 节点操作
### 3.1 创建节点
document.createElement(标签名) -> 创建指定标签(创建好的标签不在网页中)
### 3.2 添加节点
节点1.appendChild(节点2) -> 在节点1中最后添加节点2
节点1.insertBefore(节点2,节点3) -> 在节点1中的节点3前插入节点2
### 3.3 删除节点
节点1.removeChild(节点2) -> 删除节点1中的节点2
节点.remove() -> 删除指定节点
### 3.4 拷贝节点
默认浅拷贝,不拷贝子标签
`节点.cloneNode()` -> 复制指定节点产生一个新的节点,不拷贝子节点, 默认不显示
`节点.cloneNode(true)` -> 深拷贝,复制指定节点产生一个新的节点,节点中的子节点也会被拷贝
### 3.5 替换节点
替换标签要用父标签来操作
`节点1.replaceChild(节点2(new),节点3(old))` -> 将节点1中的节点3替换为节点2
## 4 DOM属性
### 4.1 文本节点
#### 4.1.1 innerText
`节点.innerText` - 获取节点内容;只获取整个节点中所有的文本信息（包括子标签内的文本）,不获取子标签信息
`节点.innerText` = 值 - 修改节点内容;如果内容中有标签语法,不会有效
#### 4.1.2 innerHTML
`节点.innerHTML` - 获取节点内容;获取整个节点中所有的文本信息和子标签信息
`节点.innerHTML` = 值 - 修改节点内容;如果内容中有标签语法,会有效
#### 4.1.3 outerText
`节点.outerText`	-	获取包含自己在内的节点内容，如果有子标签，子标签的内容也获取，但不获取标签本身。
#### 4.1.4 outerHTML
`节点.outerHTML`	-	获取包含自己在内的节点内容，包括所有的标签。
### 4.2 获取\修改属性值
#### 4.2.1 普通属性
`节点.属性名` - 获取节点属性
`节点.属性名 = 值` - 修改节点属性
`节点变量名.getAttribute('属性名')`	-	获取节点属性
`节点变量名.setAttribute('属性名', '新的属性值')`	-	修改节点属性
`节点变量名.attributes`	-	获取当前节点的所有属性节点
#### 4.2.2 特殊属性
class属性
`节点.className`
`window.getComputedStyle(节点变量名, null).属性名`	-	获取外部样式表属性
`节点变量名.style.属性名`	-	操作行间样式表
`节点变量名.style['属性名']`	-	操作行间样式表
### 4.3 删除节点属性
`节点变量名.removeAttribute('属性名')`
# 五. BOM
## 1.BOM简介
BOM(browser object model) - 浏览器对象模型
js中创建一个window对象,当前浏览器
js中声明的所有的全局变量都是绑定在window对象上的属性
`window.document`	-	html页面内容
`window.frames`	-	框架集合
`window.navigator`	-	浏览器描述信息
`window.screen`	-	屏幕信息
## 2.window基本操作
### 2.1 打开新的窗口
`window.open(url, target, 位置属性)` - 打开一个指定窗口，url为空则为空白窗口； target: `__self`为当前标签页，默认为`__black`
`window.open('','','width=?,height=?')` - 打开一个新的独立的窗口,并且设定窗口的大小,并且返回窗口对象
### 2.2 关闭新的窗口
`窗口对象.close()`
`window.close()`	-	关闭当前标签页
### 2.3 移动窗口
`窗口对象.moveTo(x坐标,y坐标)` - 将指定的**小窗口**移动到指定的位置
### 2.4 获取窗口大小
`innerWidth\innerHeight` - 获取浏览用来显示网页内容的有效部分的宽度和高度(HTML中的body标签)
`outerWidth\outerHeight` - 获取整个浏览器的宽度和高度(HTML中的html标签)
### 2.5 弹框
#### 2.5.1 alert
`alert(提示信息)`
提示信息+确定按钮
#### 2.5.2 confirm
`confirm(提示信息)`
提示信息+确定\取消按钮;返回值是布尔值,true代表确认,false代表取消
#### 2.5.3 prompt
`prompt(提示信息,输入框的默认值)`
提示信息+输入框+确定\取消按钮;点击确认,返回输入框的内容,点击取消,返回null
### 2.6 网页控制
#### 2.6.1 location
控制网页地址栏和刷新
`location.href`	-	控制浏览器地址栏内容
`location.host`	-	获取当前的域名（不带http）
`location.origin`	-	获取当前页面的域名（带http）
`location.reload()`	-	刷新页面，括号中放true表示不带缓存
`location.assign()`	-	加载新的页面
`location.repalce()`	-	加载新的页面。不会在浏览器中的历史记录表中留下信息
#### 2.6.2 history
控制网页历史记录和前进后退
`window.history.length`	-	获取历史记录的长度
`history.back()`	-	上一页
`history.forward()`	-	下一页
`history.go(num)`	-	往前(num>0)往后(num<0)跳转到第num个记录
## 3 定时器
### 3.1 setInterval()\clearInterval()
`setInterval(回调函数,定时时长)` - 每隔指定时长(单位毫秒)就调用一次回调函数;返回定时对象
`clearInterval(定时器对象)` - 停止指定的定时器
### 3.2 setTimeout()\clearTimeout()
`setTimeout(回调函数,定时时长)` - 指定时长后调用指定函数(回调函数只会调用一次)
`clearTimeout(定时器对象)`
## 4 事件绑定
### 4.1 给标签的事件属性赋值
直接给标签的onclick属性赋值
通过标签的事件属性绑定事件1,事件驱动程序中this是window
```javascript
<button onclick="action1()">按钮1</button>
```
事件清除使用`事件属性名.onclick = null`
### 4.2 给节点的对象属性赋值
用函数名给节点的事件属性赋值;函数中的this是事件源
```javascript
btnNode2 = document.getElementById('btn2')
btnNode2.onclick = action2
```
### 4.3 给节点的对象属性赋匿名函数
用匿名函数给节点的事件属性赋值;函数中的this是事件源
```javascript
document.getElementById('btn4').onclick = function(){
	alert('你还在点击按钮')
	// 此处this代表事件源
	console.log(this)
}
```
### 4.4 使用addEventListener
`事件源节点.addEventListener(事件类型名,事件驱动程序对应的函数)`
注意:事件类型名是事件名去掉on之后的值;函数中的this是事件源
这种绑定方式可以同时给同一事件源的同一事件绑定不同的事件驱动程序
### 4.5 常见的事件类型
`window.onload`: 页面完全加载后触发
`window.onunload`: 页面完全卸载时触发，只有ie支持
`window.onresize`: 窗口变动事件
`onclick`: 鼠标点击事件
`ondblclick`: 双击事件
`onmouseover`:鼠标进入事件
`onmouseout`:鼠标离开事件
`onmousedown`:鼠标按下事件
`onmouseup`:鼠标抬起事件
`onmousemove`: 鼠标移动事件
`onkeydown`:键盘按下事件
`onkeyup`:键盘抬起事件
`onfocus`: 聚焦事件
`onblur`: 离焦事件
`window.onscroll`:鼠标滑动事件(滚轮)
```javascript
// 获取滚动条的位置
var a = document.documentElement.scrollTop || document.body.scrollTop
```
```javascript
// 获取窗口宽高
var w = document.documentElement.clientWidth || document.body.clientWidth || document.Screen.width
var h = document.documentElement.clientHeight || document.body.clientHeight || document.Screen.height
console.log(w, h)
```
```javascript
inputNode.onkeydown = pressKey
function pressKey(event){
	var keynum
	// 获取按下的键盘ascii码
	keynum = event.keyCode
}
```
### 4.6 事件的冒泡和捕获
事件冒泡:当父标签和子标签都绑定同一个事件时,当点击子节点,不仅会响应子节点的事件,还会响应父节点的事件.这种现象叫做事件冒泡.
捕获: 阻住当前事件传递给父标签
`子节点事件.stopPropagation()`
## 5. fetch网络请求
语法:
```javascript
fetch('url',{
	请求参数
})
.then((res)=>res.json())
.then((res)=>{
	获取数据后的操作
})
```
说明: fetch获取到的数据为字符串数据，需要先进行格式转换才能使用，可以用`res.json()`转换，也可使用`JSON.parse(字符串)`进行转换。
get请求中中文需要以百分号方式显示，转换方法为:
`encodeURIComponent(中文)`
`decodeURIComponent(百分号参数)`
# 六. jQuery
## 1.介绍jQuery
### 1.1 什么是jQuery
jQuery就是用js封装的一个库,主要解决原生js中DOM操作复杂\麻烦的问题
js和jQuery可以混合使用
### 1.2 如何导入jQuery
1)导入本地jQuery:
```html
<script src="js/jquery.min.js" type="text/javascript"></script>
```
2)导入远程的jQuery:
```html
<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js">
```
<!-- 开发环境版本，包含了有帮助的命令行警告 -->
```html
 <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```
<!-- 生产环境版本，优化了尺寸和速度 -->
```html
 <script src="https://cdn.jsdelivr.net/npm/vue"></script>
```
### 1.3 使用jQuery
jQuery中提供了一个$,用来表示jQuery类
`$(数据)` - 可以创建jQuery对象,jQuery中提供的所有的属性和方法都是绑定在jQuery对象中的
### 1.4 ready方法
ready方法 - 页面加载完成后会自动调用和它关联的回调函数
`$(document).ready(回调函数)`
缩写方式:`$(回调函数)`
## 2.获取节点
### 2.1 常见的选择器(同css)
#### 2.1.1 id选择器
`$('#id值')`
#### 2.1.2 class选择器
`$('.class值')`
#### 2.1.3 标签选择器
`$('标签名')`
#### 2.1.4 群组选择器
`$('选择器1,选择器2,...')`
#### 2.1.5 后代选择器
`$('祖先选择器 后代选择器')`
`$('夫选择器>子选择器')`
### 2.2 其他选择器
`$('p+a')` - 选中紧跟着p标签的a标签
`$('#pa~*')` - 选中id是p1的标签后面所有的兄弟标签
`$('p:first')` - 选中第一个p标签
`$('p:last')` - 选中最后一个p标签
`$('div *:first-child')` - 选中id是div2中第一个子标签
### 2.3 节点值
jQuery中不管选择器选中了多少个标签,节点的结果都是一个容器型数据类型的数据,这个数据是jQuery对象.容器中的元素就是js的节点对象
节点jQuery对象和js对象的相互转换
js转jQuery - `$(js对象)`
jQuery转js - 单独取出jQuery对象的元素
## 3.节点的增删
### 3.1 创建节点
创建出的节点不在body中,要进行添加才能到body中
`$(html创建标签的语法)`
```html
imgNode = $('<img src="img/picture-2.jpg" />')
```
### 3.2 添加节点
1)`节点1.append(节点2)` - 将节点2添加到节点1的最后,节点1和节点2是父子关系
2)`节点1.prepend(节点2)` - 将节点2添加到节点1的开头,节点1和节点2是父子关系
3)`节点1.before(节点2)` - 将节点2插入到节点1的前面,节点1和节点2是兄弟关系
4)`节点1.after(节点2)` - 将节点2插入到节点1的后面,节点1和节点2是兄弟关系
### 3.3 删除节点
1) `节点.remove()` - 删除指定节点
2) `节点.empty()` - 删除节点中所有的子标签
## 4.节点操作属性
### 4.1 特殊属性
#### 4.1.1 标签内容
innerText(js) - text(jq)
innerHTML(js) - html(jq)
`jq对象.text()` - 获取标签内容
`jq对象.text(值)`- 给标签内容赋值
#### 4.1.2 value属性
value(js) - val(jq)
`jq对象.val()` - 获取标签value值
`jq对象.val(值)` - 给标签value赋值
#### 4.1.3 样式属性
style(js) - css(jq)
`jq对象.css(css样式属性名, 属性值)` – 给对象的一个属性赋值
`jq对象.css({js样式属性名1:属性值1,js样式属性名2:属性值2,...})` – 给对象的多个属性赋值
#### 4.1.4 class属性
`节点.addClass(class值)` - 给指定节点添加class属性值
`节点.removeClass(class值)` – 移除指定节点的指定class
### 4.2 普通属性
`节点.attr(属性名)` - 获取指定节点中指定属性的值
`节点.attr(属性名,属性值)` - 给指定节点的指定属性赋值
## 5.jQuery事件绑定
### 5.1 直接绑定事件
`jq对象.on(事件名,事件驱动程序)`
注意:此处的事件名是js中事件名去除on的名字
事件驱动程序中this表示事件源,this是js对象,$(this)才是jQuery对象
### 5.2 通过父标签去给子标签绑定事件
`父标签.on(事件名, 选择器, 事件驱动程序)` - 给指定节点中选择器选中的子标签绑定事
this代表事件源,指向所选择到的子标签
## 6.Ajax使用
### 6.1 什么是Ajax
什么是Ajax(Asynchronous Javascript And XML) - 异步js(在子线程中完成网络请求)
Ajax是jQuery封装的,专门用来解决前端HTTP请求的一个库
相当于python中的requests模块
### 6.2 post请求
`$.post(url, 参数对象, 请求成功的回调函数, 数据类型)`
post请求是将数据放在参数对象中进行传输,可传输大数据
### 6.3 get请求
`$.get(url, 参数对象, 请求成功的回调函数, 数据类型)`
Get请求是将数据拼接在url后面进行传输,最大可传输1Kb的数据
注意:调用的时候数据放在参数对象中,在传输中自动拼接
### 6.4 ajax方法
$.ajax({
​	url:请求地址,
​	data:请求参数,
​	type:请求方式(GET\POST)
​	dataType:返回的数据类型
​	success:请求成功后的回调函数,
​	error:请求失败后的回调函数
})
### 6.5 Ajax代码示例
```javascript
$.ajax({
	url:'https://www.apiopen.top/satinApi',
	data:{type:1,page:1},
	type:'GET',
	success:function(responsData){
		console.log(responsData)
		dataArray = responsData.data
		for(x=0;x<dataArray.length;x++){
			objc = dataArray[x]
			console.log(objc.text)
		}
	}
})
```
# 七. vue.js
## 1. vue.js简介
Vue是js框架,用来让标签和数据的绑定更加简单
## 2. 导入方法
开发环境版本，包含了有帮助的命令行警告
`<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`
生产环境版本，优化了尺寸和速度
`<script src="https://cdn.jsdelivr.net/npm/vue"></script>`
## 3. 使用方法
### 3.1 创建vue对象语法:
变量 = new Vue({
		el:选择器,
		data:对象
		methods:对象
		computed:对象
	})
说明: el后面为选择器，主要是用来选择标签的，语法同css选择器
data: 数据提供，所有vue的数据均保存在data对象中
methods: 方法提供，所有绑定vue方法的函数均保存在methods对象中
computed: 计算提供，提供一些计算方法
### 3.2 使用方法
标签内容: `{{Vue中data的属性名\computed方法名}}`
标签属性: `v-bind:标签属性名='Vue中的data属性名'`
### 3.3 循环判断
`v-if='Vue中data的属性名'`	-	如果属性为true,标签显示;如果为false,标签不显示
`v-for = '变量名 in 序列'`	-	通过循环用数据决定产生多个标签
### 3.4 双向绑定
`v-model='Vue对象的data属性名'`	-	只能和input中的value属性绑定
## 4. 事件绑定
`v-on:事件名='Vue中methods中的属性名'`	-	给标签绑定vue事件，事件中的this指向当前Vue对象
事件捕获:
`v-on.事件名.stop='methods中的属性名'`	-	阻止事件冒泡(捕获事件)
计算属性:
计算属性应该有一个返回值，返回值作为数据提供给标签
# 八.常用js方法
1 判断是否滑倒页面底部
```javascript
$(window).scrollTop()+$(window).height()>=$('body').height() //滑到页面底部返回true,未滑到返回false 
```
form表单中button默认会自动提交表单，设置type为button则会阻止自动提交，设置type为submit或者不设置则不会提交