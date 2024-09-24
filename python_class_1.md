# Python 培训第一课，数据类型

欢迎进入 Python 的世界！Python 是一种简洁、易读且功能强大的编程语言，广泛用于各种测试任务，从自动化测试到数据分析，都能发挥出色的效果。在本次介绍中，我将带您了解 Python 的基本概念和为什么选择 Python 作为测试工具。

## 什么是 Python？

Python 是一种高级、通用、解释性编程语言，由 Guido van Rossum 在上世纪90年代初开发。它以简洁、可读的语法著称，使得编写和维护测试代码变得更加高效和愉快。

基于 C 语言造的轮子

## 为什么选择 Python 进行测试？

- 简洁易读：Python 的简洁语法和可读性使得测试代码更易于编写、理解和维护。您可以用更少的代码实现更多的功能，节省时间和精力。
- 快速上手：Python 的学习曲线相对较低，语法简单明了，使得新手能够迅速上手并开始编写测试代码。
- 强大的第三方库和框架：Python 生态系统庞大而活跃，有许多优秀的第三方库和框架可供测试人员使用，加快测试开发速度，提高测试效率。
- 跨平台性：无论您是在 Windows、Mac 还是 Linux 环境下工作，Python 都能完美运行，保证测试代码的可移植性。
- 自动化测试支持：Python 提供了丰富的自动化测试框架和工具，如 PyTest、unittest、Selenium，可轻松实现自动化测试和持续集成。
- 数据分析能力：Python 在数据分析方面有着强大的支持，您可以使用 Pandas、NumPy 等库进行测试数据的处理和分析，生成详尽的测试报告。

## Python 在测试中的应用领域

- 自动化测试：Python 是自动化测试的首选语言，能够编写可靠且易于维护的自动化测试脚本，提高测试效率和一致性。
- API 测试：Python 提供了丰富的库和工具，如 Requests、PyTest、unittest.mock，方便进行 API 测试和接口验证。
- Web 测试：使用 Python 的测试框架（如 Selenium、Robot Framework），您可以进行 Web 自动化测试和 UI 测试，确保 Web 应用程序的质量。
- 性能测试：Python 的性能测试框架（如 Locust、PyTest-benchmark）和库（如 psutil）能够帮助您评估系统性能并发现性能瓶颈。
- 数据分析和报告生成：Python 强大的数据分析库（如 Pandas、Matplotlib）和可视化工具帮助您处理测试数据、生成清晰的测试报告和可视化图表。

## 如何开始写Python脚本

1. 安装 Python：首先，确保您的计算机上已安装 Python 解释器。您可以从 [Python 官方网站](https://www.python.org) 下载适合您操作系统的最新版本。

2. 选择文本编辑器：选择一个适合您编写代码的文本编辑器或集成开发环境（IDE）。一些常见的选择包括 Visual Studio Code、PyCharm、Sublime Text、Atom 等。选择一个您喜欢且熟悉的编辑器。

3. 创建新的 Python 文件：打开您选择的文本编辑器，创建一个新的空白文件，将其保存为以 .py 为扩展名的文件，例如 script.py。

4. 编写脚本代码：在 Python 文件中，开始编写您的脚本代码。您可以根据需要引入所需的模块或库，并编写所需的功能和逻辑。

    例如，以下是一个简单的 Python 脚本示例，打印"Hello, World!"：

    ```python
    import requests

    response = requests.get("https://test.eggrj.com/search_type?uid=77126")
    print(response_text)
    ```

5. 运行 Python 脚本：保存脚本文件后，您可以通过命令行或集成开发环境运行脚本。在命令行中，使用以下命令运行脚本：

    ```shell
    > python script.py
    {"status": 1, "msg": "\u8bf7\u6c42\u6210\u529f", "data": [{"search_type": "buyer_address", "name": "\u9879\u76ee\u5730\u5740"}, {"search_type": "order_code", "name": "\u8ba2\u5355\u7f16\u53f7"}]}
    ```

    如果一切顺利，您应该能够看到脚本输出的结果。

6. 调试和测试：编写脚本后，进行适当的调试和测试是一个好习惯。您可以使用调试器工具（如 pdb、ipdb 等）对脚本进行调试，或编写单元测试来确保脚本的功能和逻辑正确。

## Python 的数据类型

- 整数类型（int）
- 浮点数类型（float）
- 复数类型（complex）
- 布尔类型（bool）
- 字符串类型（str）
- 列表类型（list）
- 元组类型（tuple）
- 字典类型（dict）
- 集合类型（set）
- 不可变集合类型（frozenset）

### 类型的相关方法

1. `type(数据)` - 获取指定数据类型
2. `isinstance(数据, 类型)` - 判断指定的数据是否是指定的类型
3. `类型(数据)` - 将数据转换成指定类型，`int()` `float()` `bool()` `str()` 等
4. `abs(数据)` - 取该数据的绝对值

## int 类型

### int 特点

- int 是 Python 中用于表示整数的内置数据类型。
- int 类型可以表示正整数、负整数和零，没有固定大小限制，可以表示任意大的整数。
- int 类型是不可变（immutable）的，一旦创建，其值不可更改。

### int 应用场景

- 数据验证和断言：在测试过程中，我们经常需要验证计算结果或函数返回值是否符合预期。使用 int 类型，我们可以对整数结果进行断言，确保其准确性和一致性
- 循环计数器：测试中经常使用循环来执行相似的操作，比如遍历测试数据、执行重复测试步骤等。整数类型可以作为循环计数器，帮助我们跟踪循环次数，控制循环的行为和进展
- 数据边界测试：在测试中，我们通常需要测试边界条件，例如最小值、最大值、边界值、边界情况等。使用 int 类型，我们可以轻松表示和测试整数的边界条件，确保系统在边界情况下的正确性
- 随机数生成：在某些测试场景中，需要生成随机数来模拟不同的情况和输入。int 类型提供了随机整数生成的方法，可以生成随机的整数值，用于测试不同的数据情况
- 检测 http 状态码

### int 代码示例

```python
import requests

HTTP_STATUS_OK = 200

REQUEST_SUCCESS = 1
REQUEST_FAILED = 0

def test_request_success():
    response = requests.get("https://test.eggrj.com/search_type?uid=1")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json["status"] == REQUEST_SUCCESS

def test_request_failed():
    response = requests.get("https://test.eggrj.com/search_type?uid=2")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json["status"] == REQUEST_FAILED

def test_http_failed():
    response = requests.get("https://test.eggrj.com/search_type?uid=3")
    assert response.status_code != HTTP_STATUS_OK

def test_random_int():
    import random
    random_int = random.randint(1, 100)
    response = requests.get(f"https://test.eggrj.com/search_type?uid={random_int}")
    assert response.status_code == HTTP_STATUS_OK
```

## float 类型

### float 特点

- 浮点数类型（float）用于表示实数，即带有小数部分的数字。
- 浮点数类型可以表示正数、负数和零，没有固定大小限制，可以表示任意大的实数。
- 浮点数类型是不可变（immutable）的，一旦创建，其值不可更改。
- 浮点数类型的精度有限，可能会存在舍入误差。

### float 的应用场景

- float 的用法与 int 基本一致，唯一不同的就是使用float进行运算的时候，无法精确计算值

### 代码示例

```python
def test_float_calculate():
    assert 0.1 + 0.2 == 0.3 # False

def test_float_calculate2():
    assert round(0.1 + 0.2, 1) == 0.3 # True

def test_projective_area():
    height = 2.4
    width = 1.2
    area = get_area(height, width)
    assert round(area, 2) == 2.88
```

## str 类型

### str 特点

- 符串类型（str）用于表示文本数据，由一系列字符组成。
- 在 Python 中，字符串是不可变（immutable）的，一旦创建，其值不可更改。
- 字符串可以使用单引号（'）或双引号（"）括起来，例如 'hello' 或 "world"。
- Python 还提供了一些内置的字符串方法，用于处理和操作字符串数据。

### str 应用场景

- 数据验证和断言：测试中经常需要验证字符串的准确性和一致性。字符串类型可用于执行数据验证和断言操作，确保计算结果或函数返回的字符串与预期结果相匹配。
- 输入和输出测试：测试中经常涉及用户输入和系统输出的测试。字符串类型可用于模拟用户输入，检查输出结果的正确性，并与预期的字符串进行比较。
- 数据解析和处理：在某些测试场景中，需要解析和处理字符串数据。字符串类型提供了各种内置方法，如分割、拼接、替换、查找、大小写转换等，用于解析和操作字符串数据。
- 文本比较和匹配：在文本处理和分析的测试中，字符串类型可用于执行文本比较和匹配操作，如检查字符串是否包含特定的子字符串、执行模式匹配等。
- 错误消息和日志记录：测试中经常需要生成错误消息和记录日志。字符串类型可用于构建错误消息、格式化日志信息，并将其记录到日志文件或输出到控制台。

### str 相关方法

1. 字母大小写转换:
   - `字符串.upper()` - 小写字母转大写: 编码值减去32
   - `字符串.lower()` - 大写字母转小写: 编码值加上32
   - `字符串.swapcase()` - 大小写转换(大变小,小变大)
   - `字符串.capitalize()` - 字符串首字母大写
   - `字符串.title()` - 字符串每个单词首字母大写
2. 字符串对齐
   - `字符串.center(长度, 字符)` - 产生一个指定长度的字符串，原字符串居中，剩下的部分用指定的字符填充
   - `字符串.ljust(长度, 字符)` - 产生一个指定长度的字符串，原字符串放在左边，剩下的部分用指定的字符填充
   - `字符串.rjust(长度, 字符)` - 产生一个指定长度的字符串，原字符串放在右边，剩下的部分用指定的字符填充
   - `字符串.zfill(长度)` - 产生一个指定长度的字符串，原字符串放在右边，剩下的部分用字符0填充
3. 查找
   - `字符串1.find(字符串2, 开始下标, 结束下标)` - 在开始下标到结束下标前对应的范围内查找字符串2,默认从头到尾,没有返回-1
   - `rfind` - 为从右向左找
   - `字符串1.index(字符串2, 开始下标, 结束下标)` - 在开始下标到结束下标前对应的范围内查找字符串2,默认从头到尾,没有的话报错
   - `rindex` - 为从右向左找
   - `字符串1.count(字符串2,开始下标,结束下标)` - 返回字符串1中字符串2出现的次数，可以指定一个范围，默认从头到尾
4. join()
   - `字符串1.join(序列)` - 将序列中的元素用字符串1连接在一起产生一个新的字符串 (序列中的元素必须都是字符串)
5. 字符串替换
   - `字符串1.replace(old, new)` - 将字符串1中所有的old都替换成new,然后产生一个新的字符串
   - `str.maketrans(字符串1,字符串2)` - 创建字符串1和字符串2字符一一对应的映射表，
   - `字符串.translate(映射表)` - 按照映射表将字符串中的字符串1进行替换为字符串2,产生一个新的字符串
6. 字符串切割
   - `字符串1.split(字符串2)` - 将字符串1中的字符串2作为切点，切割字符串1
   - `字符串1.lstrip(字符串2)` - 截掉字符串1左侧的字符，默认为空格(去头)
   - `字符串1.rstrip(字符串2)` - 截掉字符串1右侧的字符，默认为空格(去尾)
7. 将字符串当作有效的表达式求值并返回结果

- `eval()` - 将字符串当作有效的表达式求值并返回结果，例如 `eval('1+2+3')` -> 6

### str 代码示例

```python
# 字符串拼接
first_name = "John"
last_name = "Doe"
full_name1 = first_name + " " + last_name
full_name2 = ' '.join([first_name, last_name])
print("完整姓名:", full_name)

# 字符串格式化
name = "Alice"
age = 25
message = "我的名字是{}，年龄是{}岁。".format(name, age)
print(message)

# 字符串索引
text = "Hello, World!"
print(text[0])      # 输出第一个字符 "H"
print(text[7:12])   # 输出从索引7到11的子串 "World"
print(text[-6:])    # 输出最后6个字符 "World!"

# 字符串长度和计数
text = "Hello, World!"
length = len(text)
count = text.count("l")
print("字符串长度:", length)
print("字符'l'的出现次数:", count)

# 字符串查找和替换
text = "Hello, World!"
index = text.find("World")
new_text = text.replace("Hello", "Hi")
print("子串'World'的索引位置:", index)
print("替换后的字符串:", new_text)

# 字符串大小写转换
text = "Hello, World!"
lowercase = text.lower()
uppercase = text.upper()
print("小写形式:", lowercase)
print("大写形式:", uppercase)

# 字符串分割和拼接
text = "apple,banana,orange"
fruits = text.split(",")
new_text = "-".join(fruits)
print("拆分后的列表:", fruits)
print("连接后的字符串:", new_text)

def check_message_show():
    response = requests.get("https://test.eggrj.com/customer_order?uid=abc")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json['msg'] == "uid 类型错误"
```

## list

### list 特点

- 列表类型（list）用于表示一系列有序的数据，是 Python 中最常用的数据类型之一
- 列表中的数据项可以是不同的数据类型，如整数、浮点数、字符串、布尔值等
- 列表是可变（mutable）的，可以随意添加、删除或修改其中的数据项
- 列表中的数据项是有序的，可以通过索引访问列表中的数据项
- 列表中的数据项可以是重复的，即列表中可以包含重复的数据项

### list 应用场景

任何地方都可以用到 list 类型，list 类型就是一个容器，任何任意数量的数据都可以放进去，这个就会是使用最多的一个类型

### list 相关方法

- `列表.append(元素)` - 在列表的最后中添加指定的元素。（直接影响原列表不会产生新的列表）
- `列表.insert(下标, 元素)` - 在列表指定下标前插入指定的元素
- `list.extend([元素1，元素2])` - 在list列表末端拆分增加多个元素；传入必须是数据容器
- `del 列表[下标]` - 删除列表中指定下标对应的元素 (`del 列表` - 删除列表)
- `列表.remove(元素)` - 删除列表中指定的元素(如果这个元素有多个只删第一个)
- `列表.pop()` - 取出列表最后一个元素, 返回被取出的元素
- `列表.pop(下标)` - 取出列表中指定下标对应的元素，返回被取出的元素
- `列表[下标] = 新值` - 将列表中指定下标对应的元素改成新值
- `列表1 + 列表2` - 将两个列表中的元素合并在一个产生一个新的列表
- `列表 * N` / `N * 列表` - 列表中的元素重复N次产生一个新的列表

### list 代码示例

```python
list1 = []
list2 = list()
fixture_data = ["data1", "data2", "data3", "data4", "data5"]

def test_fixture():
    for fixture in fixture_data:
        data = get_data(fixture)
        assert data is True

def test_page_outside():
    # 实际数据只有50页
    response = requests.get("https://test.eggrj.com/customer_order?uid=1&page=1&limit10")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert len(response_json['data']) == 10

    response = requests.get("https://test.eggrj.com/customer_order?uid=1&page=100")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json['data'] == []

def test_spider()
    import requests

    urls = ["https://test.eggrj.com/page/1". "https://test.eggrj.com/page/2"]
    data = []

    for url in urls:
        # 发起网页请求
        response = requests.get(url)

        # 获取网页内容
        content = response.text

        # 解析内容，提取所需信息
        # 这里以提取网页中的标题为例
        start_index = content.find("<title>") + len("<title>")
        end_index = content.find("</title>")
        title = content[start_index:end_index]

        # 将提取的标题存储在列表中
        data.append(title)
    print(data)
```

## tuple 类型

### tuple 特点

- 元组类型（tuple）用于表示一系列有序的数据，是 Python 中常用的数据类型之一。
- 元组中的数据项可以是不同的数据类型，如整数、浮点数、字符串、布尔值等。
- 元组是不可变（immutable）的，一旦创建，其值不可更改。
- 元组中的数据项是有序的，可以通过索引访问元组中的数据项。
- 元组中的数据项可以是重复的，即元组中可以包含重复的数据项。
- 元组中的值可以是任意数据类型，如整数、浮点数、字符串、布尔值、列表、元组、字典等。

### tuple 应用场景

tuple 能工作的场景都能被 list 替代，但是 tuple 有一个特殊的场景，就是在函数返回值的时候，如果返回的是多个值，那么这些值会被自动封装成一个 tuple

### tuple 相关方法

- `del 元组` - 删除元组
- `+` - 元组连接
- `*` - 元组重复
- `in`/`not in` - 判断元素是否在元组中
- `元组名[开始下标:结束下标]` - 元组的截取
- `len(元组名)` - 返回元组中元素的个数
- `min(元组名)` - 返回元组中的最小值
- `max(元组名)` - 返回元组中的最大值
- `tuple(列表)` - 将列表转换为元组(元素去重)

### tuple 示例代码

```python
set1 = (1,)
set2 = set()
int1 = (1)

fixture_data = ("data1", "data2", "data3", "data4", "data5")

def test_fixture():
    for fixture in fixture_data:
        data = get_data(fixture)
        assert data is True

def test_page_outside():
    # 实际数据只有50页
    response = requests.get("https://test.eggrj.com/customer_order?uid=1&page=1&limit10")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert len(response_json['data']) == 10

    response = requests.get("https://test.eggrj.com/customer_order?uid=1&page=100")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json['data'] == []

def test_spider()
    import requests

    urls = ("https://test.eggrj.com/page/1". "https://test.eggrj.com/page/2")
    data = []

    for url in urls:
        # 发起网页请求
        response = requests.get(url)

        # 获取网页内容
        content = response.text

        # 解析内容，提取所需信息
        # 这里以提取网页中的标题为例
        start_index = content.find("<title>") + len("<title>")
        end_index = content.find("</title>")
        title = content[start_index:end_index]

        # 将提取的标题存储在列表中
        data.append(title)
    print(data)
```

## set 类型

### set 特点

- 集合类型（set）用于表示一组互不相同的数据项，是 Python 中常用的数据类型之一。
- 集合中的数据项可以是不同的数据类型，如整数、浮点数、字符串、布尔值等。
- 集合是可变（mutable）的，可以随意添加、删除或修改其中的数据项。
- 集合中的数据项是无序的，不能通过索引访问集合中的数据项。
- 集合中的数据项是唯一的，集合中不包含重复的数据项。
- 集合中的数据项必须是可哈希（hashable）的，即不可变的数据类型，如整数、浮点数、字符串、元组等。

### set 应用场景

- 数据去重：集合中的数据项是唯一的，集合中不包含重复的数据项。因此，可以使用集合类型对数据进行去重操作，确保数据的唯一性。
- 数据交集、并集和差集：集合类型提供了交集、并集和差集等操作，可用于对数据进行比较和处理。

### set 的相关方法

- `集合.add(元素)` - 在集合中添加一个元素
- `集合.update(序列)` - 将序列中的元素添加到集合中, 打碎插入
- `集合.remove(元素)` - 删除集合中指定元素
- `集合1 | 集合2` - 将两个集合合并在一起
- `集合1 & 集合2` - 获取两个集合的公共部分
- `集合1 - 集合2` - 获取集合1中除了集合2剩下的部分
- `集合1 ^ 集合2` - 获取集合1和集合2除了公共部分以外的部分
- `集合1 > 集合2` - 判断集合1中是否包含集合2（判断集合2是否是集合1的子集）

### set 代码示例

```python
# 创建一个 set
fruits = {"apple", "banana", "cherry", "durian"}

# 添加元素到集合
fruits.add("grape") # {'apple', 'banana', 'cherry', 'durian', 'grape'}
fruits.add("apple")  # {'apple', 'banana', 'cherry', 'durian', 'grape'} 重复元素不会被添加

# 从集合中移除元素
fruits.remove("banana") # {'apple', 'cherry', 'durian', 'grape'}
fruits.discard("watermelon")  # 如果元素不存在，discard() 方法不会引发错误

# 检查元素是否存在于集合中
print("apple" in fruits)  # 输出：True
print("orange" in fruits)  # 输出：False

# 获取集合的长度
print(len(fruits))  # 输出：4

# 遍历集合元素
for fruit in fruits:
    print(fruit)

# 将两个集合进行交集、并集、差集运算
more_fruits = {"orange", "kiwi", "apple"}

# fruits = {'cherry', 'durian', 'grape', 'apple'}
intersection = fruits.intersection(more_fruits)
print(intersection)  # 输出：{'apple'}

union = fruits.union(more_fruits)
print(union)  # 输出：{'cherry', 'apple', 'durian', 'kiwi', 'grape', 'orange'}

difference = fruits.difference(more_fruits)
print(difference)  # 输出：{'cherry', 'durian', 'grape'}

# 清空集合
fruits.clear()
print(fruits)  # 输出：set()
```

## dict

### dict 特点

- 字典类型（dict）用于表示一组键值对数据，是 Python 中最常用的数据类型之一。
- 字典中的数据项可以是不同的数据类型，如整数、浮点数、字符串、布尔值等。
- 字典是可变（mutable）的，可以随意添加、删除或修改其中的数据项。
- 字典中的数据项是无序的，不能通过索引访问字典中的数据项。
- 字典中的键是唯一的，字典中不包含重复的键。
- 字典中的键必须是可哈希（hashable）的，即不可变的数据类型，如整数、浮点数、字符串、元组等。
- 字典中的值可以是任意数据类型，如整数、浮点数、字符串、布尔值、列表、元组、字典等。

### dict 的应用场景

- 数据存储：字典类型可用于存储和管理数据，如测试数据、配置数据、用户信息等。
- 数据解析：字典类型可用于解析和处理数据，如解析 JSON 数据、解析 XML 数据等。

### dict 的相关方法

- `键 in 字典` - 判断字典中是否存在指定的键
- `del 字典[key]` - 删除字典中指定key对应的键值对
- `len()` - 计算字典键值对个数，即键的总数
- `dict(数据)` - 将其他数据转换成字典;数据本身必须是序列，序列中的元素是小序列，
- `字典.pop(key)` - 取出字典中指定key对应的值, 返回值就是被取出的值
- `字典.clear()` - 删除字典中所有的键值对
- `字典.popitem()` - 随机删除字典中的一对键值对
- `字典.clear()` - 清空字典
- `字典.copy()` - 拷贝字典产生一个新的字典(浅拷贝)
- `dict.fromkeys(序列, 值)` - 创建一个字典，将序列中的元素作为key，key对应的value都是指定的值
- `字典.items()` - 将字典中所有的键值对都转换成元组作为一个序列的元素
- `字典.values()` - 获取字典中所有的值，返回一个序列
- `字典.keys()` - 获取字典中所有的键，返回一个序列
- `字典.setdefault(key, value)` - 当key不存在的时候添加键值对（不会修改）
- `字典1.update(字典2)` - 将字典2中的键值对添加到字典1中
- `zip(key, value)` - 将key和value序列中的值一一对应生成元组对元素

### dict 代码示例

```python
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# 访问字典中的值
print(student["name"])  # 输出：John
print(student["age"])  # 输出：20

# 修改字典中的值
student["major"] = "Data Science"
print(student)  # 输出：{'name': 'John', 'age': 20, 'major': 'Data Science', 'gpa': 3.8}

# 添加新的键值对到字典
student["university"] = "ABC University"
print(student)  # 输出：{'name': 'John', 'age': 20, 'major': 'Data Science', 'gpa': 3.8, 'university': 'ABC University'}

# 删除字典中的键值对
del student["gpa"]
print(student)  # 输出：{'name': 'John', 'age': 20, 'major': 'Data Science', 'university': 'ABC University'}

# 检查字典中的键是否存在
print("age" in student)  # 输出：True
print("gpa" in student)  # 输出：False

# 获取字典的键和值
keys = student.keys()
values = student.values()
print(keys)  # 输出：dict_keys(['name', 'age', 'major', 'university'])
print(values)  # 输出：dict_values(['John', 20, 'Data Science', 'ABC University'])

# 遍历字典的键值对
for key, value in student.items():
    print(key + ": " + str(value))

# 清空字典
student.clear()
print(student)  # 输出：{}
```

## bool 类型

- 布尔类型（bool）用于表示真值，即 True 或 False。
- 实际上，布尔类型是整数类型的子类型，True 表示 1，False 表示 0。

```python
def test_land_auth():
    response = requests.get("https://test.eggrj.com/check_layout_auth?uid=77126")
    assert response.status_code == HTTP_STATUS_OK
    response_json = response.json()
    assert response_json["data"]["permission_check"] == True
```

## 其他数据类型

### complex

- 复数类型（complex）用于表示复数，由实数部分和虚数部分组成。
- 复数类型可以表示正数、负数和零，没有固定大小限制，可以表示任意大的复数。
- 复数类型是不可变（immutable）的，一旦创建，其值不可更改。
- 复数类型的精度有限，可能会存在舍入误差。
- j为虚数单位,`j*j=-1`

### forzenset

- 不可变集合类型（frozenset）用于表示一组互不相同的数据项，是 Python 中不常用的数据类型之一。
- 与 set 的区别就是不可增删改元素，由于集合的特性，不可变类型不能进行数据校验，只能进行存储，所以不常用

## 最后代码

```python
# 定义一个学生信息的字典
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "is_active": True,
    "courses": ["Math", "English", "Physics"],
    "schedule": ("Mon", "Wed", "Fri"),
    "interests": {"coding", "reading", "music"},
    "grades": {
        "Math": 85,
        "English": 90,
        "Physics": 92
    }
}

# 打印学生信息
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])
print("Is Active:", student["is_active"])
print("Courses:", student["courses"])
print("Schedule:", student["schedule"])
print("Interests:", student["interests"])
print("Grades:", student["grades"])

# 修改学生信息
student["age"] = 21
student["gpa"] = 3.9
student["is_active"] = False
student["courses"].append("Chemistry")
student["schedule"] = ("Tue", "Thu", "Fri")
student["interests"].add("swimming")
student["grades"]["Chemistry"] = 88

# 打印修改后的学生信息
print("\nUpdated Student Information:")
print("Age:", student["age"])
print("GPA:", student["gpa"])
print("Is Active:", student["is_active"])
print("Courses:", student["courses"])
print("Schedule:", student["schedule"])
print("Interests:", student["interests"])
print("Grades:", student["grades"])
```
