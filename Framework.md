# 框架使用手册

# 一. Django使用

## 0. 注意事项

### 0.1 版本冲突

python3.7和django1.11.11版本冲突，解决办法，运行报错后点击报错代码路径将该行最后的逗号删除即可

django2.2和pymysql冲突，解决办法：
```python
# 项目名>init
import pymysql
pymsqy.install_as_MySQLdb()

# 进入install_as_MySQLdb()函数下添加：
global version_info
version_info = (1, 4, 2, "final", 0)

# 运行报错，用ctrl进入
# \venv\lib\site-packages\django\db\backends\mysql\operations.py
query = getattr(cursor, '_executed', None)
if query is not None:
    if type(query) == bytes:
        query = query.decode(errors='replace')
    elif type(query) == str:
        query = query.encode(errors='replace')
    else:
        query = force_text(query, errors='replace')
return query
```

## 1. 基础使用和命令

### 1.1 尚未创建项目

`python3 -m venv venv` 或 `virtualenv --python=python的安装路径 venv` - 创建虚拟环境

`pip install django==2.1.13 pymysql` - 虚拟环境下安装相关依赖项

`django-admin --version` - 查看django版本

`source venv/bin/activate` 或 `"venv/Scripts/activate"` - 激活虚拟环境

`django-admin startproject 项目名` - 创建项目

`cd 项目名` - 进入项目文件夹

`pip freeze > requirements.txt` - 将依赖项写入到requirements.txt文件中

### 1.2 已有项目和虚拟环境

`pip install django==2.1.13 pymysql` - 安装相关依赖项

`django-admin --version` - 查看django版本

`django-admin startproject 项目名 .` - 在当前路径下创建Django项目

### 1.3 从版本库创建项目

`git clone 项目地址` - 克隆项目

`cd 克隆的项目文件夹下` - 进入项目文件夹

`pip3 install virtualenv` - 安装创建虚拟环境模块

`python3 -m venv venv` `virtualenv --python=python的安装路径 venv` - 创建虚拟环境

说明：如果有多个python，需要指定python安装环境，如果只有一个则可以不写

`source venv/bin/activate` `"venv/Scripts/activate"` - 激活虚拟环境

`pip install -r requriements.txt` - 重建环境依赖项

如果安装mysqlclient报错需要先安装:`yum install mysql-devel`

### 1.4 创建应用

一个django项目中可以有多个应用

`python manage.py startapp 应用名` `django-admin startapp 应用名` - 创建应用

`python manage.py runserver` - 运行应用

默认：`ip 127.0.0.1 port:8000`

`python manage.py runserver 0.0.0.0:7999` - 指定端口和ip运行应用

### 1.5 其他命令

`python manage.py clearsessions` - 清除缓存，会删除数据库中过期session。

## 2. 配置

### 2.1 配置数据库

`项目名>settings`配置

`INSTALLED_APPS`:添加应用名

`TEMPLATES>DIRS`:添加模板地址，通常使用`[os.path.join(BASE_DIR, '模板所在文件夹'),]`，可以添加多个地址，

`DATABASES`：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hrs',
        'HOST': '121.199.42.247',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'stolen',
        'CHARSET': 'utf8',
        'TIME_ZONE': 'Asia/Chongqing',
    }
}
```

`LANGUAGE_CODE`: `zh-hans`表示汉语， `en-us`表示英语

`TIME_ZONE`: `Asia/Chongqing`表示重庆的时区，中国只有重庆和上海

`项目名>init`:

```python
import pymysql
pymsqy.install_as_MySQLdb()
```

### 2.2 数据库模型正向迁移

正向迁移（models->数据库）

`应用名>models`：编写模型类，如：

```python
class Fruit(models.Model):
    # 自增字段，主键
    fruit_id = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=15, verbose_name='名称')
    intro = models.CharField(max_length=511, verbose_name='介绍')
    counter = models.IntegerField(default=0, verbose_name='得票')
    belone = models.ForeignKey(to=Plant, on_delete=models.PROTECT, db_column='belong')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_fruit'
        # 单数形式的名字
        verbose_name = '水果'
        # 复数形式的名字
        verbose_name_plural = '水果'
```

说明：db_table为指定数据库名，verbose_name为管理员界面查看数据表名，如果需要打印类名需要重写str函数

**注意：生成迁移文件必须要有数据库存在**

`python manage.py makemigrations 应用名` - 生成迁移文件

`python manage.py migrate`	进行数据库迁移

### 2.3 数据库模型反向迁移

正向迁移（数据库->models）

`python manage.py inspectdb > 应用名/models.py`

```python
class Emp(models.Model):
    no = models.IntegerField(primary_key=True, db_column='eno')
    name = models.CharField(max_length=20, db_column='ename')
    job = models.CharField(max_length=20)
    mgr = models.ForeignKey('self', models.PROTECT, db_column='mgr', blank=True, null=True)
    sal = models.IntegerField()
    comm = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey(Dept, models.PROTECT, db_column='dno')

    class Meta:
        managed = False
        db_table = 'tb_emp'
```

说明：如果自定义变量名不是数据库的列名，需要在后面用`db_column='列名'`进行指定，

### 2.4 超级管理员配置

`应用名>admin`

```python
class FruitAdmin(admin.ModelAdmin):
    # 设置显示的列
    list_display = ('fruit_id', 'name', 'intro')
    # 设置可以搜索的项
    search_fields = ('name', )
    # 设置单页显示数量
    list_per_page = 5
    # 设置排序规则，用fruit-id列升序排列，如果需要降序用-fruit-id
    ordering = ('fruit-id', )

# 注册管理员页面
admin.site.register(Fruit, FruitAdmin)
```

`python manage.py createsuperuser` - 创建超级管理员用户

在管理员页面显示自定义应用名：

>在`应用文件夹>apps>PollsConfig`中添加：verbose_name = '自定义的名字'
>设置`init`文件：default_app_config = '应用名.apps.PollsConfig'、

对有外键关联的对象，在后台管理需要显示名称，需要在被关联的模型对象中写`__str__`魔法方法

在后台管理显示自定义的模型名称，需要在模型定义类中添加

```python
class Meta:
    db_table = 'tb_subject'
     verbose_name_plural = '学科'
```

配置后台显示应用名称

`应用名>apps.py`

```python
from django.apps import AppConfig

class VoteAppConfig(AppConfig):
    name = 'vote'
    verbose_name = '投票应用'
```

### 2.5 打开Django交互式环境

`python manage.py shell `

### 2.6 配置静态文件支持访问

项目名>setting中添加:

`STATICFILES_DIRS = [os.path.join(BASE_DIR, '静态文件路径'), ]`

## 3. 页面开发步骤

MTV MVC

1. 先把MTV每个字母什么意思，中英文说一次

2. 再解释每一层

Model模型层主要做数据层抽象，主要两个作用，一个使用面向对象的思维操作数据（ORM对象关系映射）DAO Data Access Object。另外一个作用就是隔离具体的数据库sql操作，举例来说就是如果原来用的mysql，后来要变为Orcal，不用修改大量的代码。

### 3.1 模型(models)

#### 字段类

模型字段可以用的类型：

| 字段类                | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| AutoField             | 自增ID字段                                                   |
| BigIntegerField       | 64位有符号整数                                               |
| BinaryField           | 存储二进制数据的字段，对应Python的bytes类型                  |
| BooleanField          | 存储True或False，如果后台管理需要自定义：choices=((True, '男'), (False, '女')) |
| CharField             | 长度较小的字符串                                             |
| DateField             | 存储日期，有auto_now和auto_now_add属性                       |
| DateTimeField         | 存储日期和日期，两个附加属性同上                             |
| DecimalField          | 存储固定精度小数，有max_digits（有效位数）和decimal_places（小数点后面）两个必要的参数 |
| DurationField         | 存储时间跨度                                                 |
| EmailField            | 与CharField相同，可以用EmailValidator验证                    |
| FileField             | 文件上传字段                                                 |
| FloatField            | 存储浮点数                                                   |
| ImageField            | 其他同FileFiled，要验证上传的是不是有效图像                  |
| IntegerField          | 存储32位有符号整数。                                         |
| GenericIPAddressField | 存储IPv4或IPv6地址                                           |
| NullBooleanField      | 存储True、False或null值                                      |
| PositiveIntegerField  | 存储无符号整数（只能存储正数）                               |
| SlugField             | 存储slug（简短标注）                                         |
| SmallIntegerField     | 存储16位有符号整数                                           |
| TextField             | 存储数据量较大的文本                                         |
| TimeField             | 存储时间                                                     |
| URLField              | 存储URL的CharField                                           |
| UUIDField             | 存储全局唯一标识符                                           |

#### 字段属性

通用字段属性

| 选项           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| null           | 数据库中对应的字段是否允许为NULL，默认为False                |
| blank          | 后台模型管理验证数据时，是否允许为NULL，默认为False          |
| choices        | 设定字段的选项，各元组中的第一个值是设置在模型上的值，第二值是人类可读的值 |
| db_column      | 字段对应到数据库表中的列名，未指定时直接使用字段的名称       |
| db_index       | 设置为True时将在该字段创建索引                               |
| db_tablespace  | 为有索引的字段设置使用的表空间，默认为DEFAULT_INDEX_TABLESPACE |
| default        | 字段的默认值                                                 |
| editable       | 字段在后台模型管理或ModelForm中是否显示，默认为True          |
| error_messages | 设定字段抛出异常时的默认消息的字典，其中的键包括null、blank、invalid、invalid_choice、unique和unique_for_date |
| help_text      | 表单小组件旁边显示的额外的帮助文本。                         |
| primary_key    | 将字段指定为模型的主键，未指定时会自动添加AutoField用于主键，只读。 |
| unique         | 设置为True时，表中字段的值必须是唯一的                       |
| verbose_name   | 字段在后台模型管理显示的名称，未指定时使用字段的名称         |

ForeignKey属性

1. limit_choices_to：值是一个Q对象或返回一个Q对象，用于限制后台显示哪些对象。

2. related_name：用于获取关联对象的关联管理器对象（反向查询），如果不允许反向，该属性应该被设置为`'+'`，或者以`'+'`结尾。

3. to_field：指定关联的字段，默认关联对象的主键字段。

4. db_constraint：是否为外键创建约束，默认值为True。

5. on_delete：外键关联的对象被删除时对应的动作，可取的值包括django.db.models中定义的：

> CASCADE：级联删除。（一般不这样做，一般删除前先检查关联，有关联提示用户）
>
> PROTECT：抛出ProtectedError异常，阻止删除引用的对象。
>
> SET_NULL：把外键设置为null，当null属性被设置为True时才能这么做。SET_DEFAULT：把外键设置为默认值，提供了默认值才能这么做。

ManyToManyField属性

1. symmetrical：是否建立对称的多对多关系。
2. through：指定维持多对多关系的中间表的Django模型。
3. throughfields：定义了中间模型时可以指定建立多对多关系的字段。
4. db_table：指定维持多对多关系的中间表的表名。

ImageFiled属性

upload_to：图片上传地址

#### 模型元数据选项

| 选项                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| abstract              | 设置为True时模型是抽象父类                                   |
| app_label             | 如果定义模型的应用不在INSTALLED_APPS中可以用该属性指定       |
| db_table              | 模型使用的数据表名称                                         |
| db_tablespace         | 模型使用的数据表空间                                         |
| default_related_name  | 关联对象回指这个模型时默认使用的名称，默认为`<model_name>_set` |
| get_latest_by         | 模型中可排序字段的名称。                                     |
| managed               | 设置为True时，Django在迁移中创建数据表并在执行flush管理命令时把表移除 |
| order_with_respect_to | 标记对象为可排序的                                           |
| ordering              | 对象的默认排序                                               |
| permissions           | 创建对象时写入权限表的额外权限                               |
| default_permissions   | 默认为`('add', 'change', 'delete')`                          |
| unique_together       | 设定组合在一起时必须独一无二的字段名                         |
| index_together        | 设定一起建立索引的多个字段名                                 |
| verbose_name          | 为对象设定人类可读的名称                                     |
| verbose_name_plural   | 设定对象的复数名称                                           |

### 3.2 视图(views)

```python
def index(request: HttpRequest):
    subjects = Subject.objects.all().order_by('-is_hot')
    return render(request, 'subjects.html', {
        'subjects': subjects
    })
# 查看执行是sql语句：print(subjects.query)
```

获取的参数：HttpRequest（封装了浏览器发给服务器的请求）

> 1.  request.method - 请求方法的方法(POST/GET/PUT/DELETE)
> 2.  request.path - 获取请求的链接
> 3.  request.get_full_path - 获取带查询参数的资源路径（GET参数）
> 4.  request.is_ajax() - 判断是否是ajax请求，返回值True/False
> 5.  request.META - 获取请求头
>     request.META['REMOTE_ADDR'] - 
> 6.  request.POST / GET.get('参数名', 默认值) - 获取传递的数据
> 7.  request.POST / GET['参数名'] - 获取传递的数据，没有会报错
> 8.  request.body / FILES - 获取上传的文件
> 9.  request.COOKIES - 获取本站点的Cookie信息
> 10.  request.get_signed_cookie - 获取带签名的cookie信息
> 11.  request.session.flush() - 清除session，不会删除数据库session记录

返回值：HttpResponse（封装了服务器给浏览器的响应）

> 1.  HttpResponse(字节串/字符串)
>       指定返回响应的类型用：content_type='application/json'或者使用：resp['content-type'] = 'application/pdf'
>       指定返回响应的状态码用：resp.status_code = 204
>       指定文件网页中打开：resp['content-disposition'] = 'inline'
>       指定文件下载（中文要使用百分号编码）：resp['content-disposition'] = 'attachment; filename="python入门教程"'
> 2.  render(HttpRequest对象, '模板页的名字', 渲染到页面上的数据:dict)
> 3.  redirect('重定向地址')
> 4.  JsonResponse(返回json数据)

模型的CRUD

Create：

> 1.  模型名.objects.create(字段1=值1, 字段2=值2)
>
> 2.  对象 = 模型名()
>
>  对象.save()
>
> 3.  模型名('参数1', '参数2').save()

Update:

>   1.  查询对象.update(参数1=值1)
>
>       说明：update更新方法无法使auto_now等时间约束条件生效
>
>   2.  查询对象.参数 = 值
>
>       查询对象.save()
>
>       说明：save可以使auto_now生效

Read：

查询模型中的数据：`Subject.objects.all()`

>   all()   查询所有
>   filter(查询条件)    查询满足条件的值，需要在列的后面加双下划线再加条件
>
>   ​	`name='洛昊'`             精确查找
>   ​	`name__contain='洛'`      名字中包含洛的
>   ​	`name__icontain='洛'`     名字中包含洛的，忽略大小写
>   ​	`name__startswith='洛'`   名字以洛开头的，istartswith为忽略大小写
>   ​	`name__endswith='昊'`     名字以昊结尾的，iendswith为忽略大小写 
>   ​	`exact='洛昊'`            精确匹配，iexact为忽略大小写的精确匹配
>   ​	`in`                      集合运算
>   ​	`gt/gte/lt/lte`           大于/大于等于/小于/小于等于
>   ​	`range`                   范围查询
>   ​	`year/month/day/week_day/hour/minute/second`  时间和日期
>   ​	`isnull`                  空值(True)或非空值(False)
>   ​	`search`                  基于全文的检索
>   ​	`regex/iregex`            基于正则表达式的模糊匹配

Delete：

>   查询对象.delete()

Q对象和F对象：

```python
from django.db.models import F, Q
# F对象用在数据库中不同列之间的比较
BookInfo.objects.filter(read__gt=F('commit')）#返回一个集合
# Q对象用在需要实现逻辑或和逻辑与的时候
BookInfo.objects.filter(Q(pk__lt=6)|Q(title__contains="1"))#返回符合条件的

```

模型对象的使用：

|     格式     | 模板对象名 |              子对象1               |                       子对象2                        |
| :----------: | :--------: | :--------------------------------: | :--------------------------------------------------: |
|     示例     |  Teacher   |              .objects              |                        .all()                        |
|     名称     |   Model    |            ModelManager            |                       QuerySet                       |
| 对象下的方法 |   save()   |              create()              |                  first()  /  last()                  |
|              |  delete()  | get() 查不到结果或有多个结果会报错 |                         [:]                          |
|              |            |      filter() 结果为QuerySet       |                       update()                       |
|              |            |               all()                |              only(字段)  /  defer(字段)              |
|              |            |         update_or_create()         |                      order_by()                      |
|              |            |   exclude() 查询不满足条件的数据   |       select_related()  /  prefetch_related()        |
|              |            |                                    | value(字段1,字段2)  将对象转换为字典，只包含指定字段 |
|              |            |                                    |                exists() 结果是否为空                 |
|              |            |                                    |                   count() 结果数量                   |

查询指定列的语法：`Teacher.objects.all().only('no', 'name', 'birth')`

查询除开指定列的其他列：`Teacher.objects.all().defer('name', 'birth')`

解决有关联的时候出现1+N查询问题：
`Teacher.objects.filter(subject__no).select_related('subject')`

一对一或多对一：`select_related('关联对象')`

多对多：`prefetch_related('关联对象')`

F语法(将字段值与表内其他字段比较)：`Article.objects.filter(fangwen__gt=F('zan') + 100)`

执行原生SQL语句：

> 1. `Emp.objects.raw('sql语句')`
>
> 2. `django.db.connections['数据库配置名']` --> `cursor()` --> `execute('sql语句')` --> `fetchall()/fetchone()/fetchmany()`

### 3.3 模板(templates)

for循环语法：

```
{% for teacher in teachers %}
{% endfor %}
```

if语法：

```
{% if teacher.gender %}
{% endif %}
```

说明：if支持`and or == < > != <= >= in not in is is not`

yesno语法：

```
{{ teacher.gender | yesno:"男,女" }}
```

静态文件访问语法：

```
{% load staticfiles %} //说明：添加到文件开头

<img src="{% static teacher.photo %}"> 
//说明：自动拼接静态资源路径，static为setting中的设置
```

获取列表指定下标的值：`列表名.索引下标`

加法运算：`{{ value|add:10}}` 
说明：value为5，则返回15，不改变value的值

减法运算：`{{value|add:-10}}`

乘除运算：`{%  widthratio a b c %}`
说明:返回结果为`a/b*c`，如果要将结果赋值给d，则在c后面写`as d`

切片：`{{ value|slice:"2:-1" }}`

Django模板提交表单需要加上csrf令牌，通常做法是在表单开头添加：`{% csrf_token %}`

模板挖坑：`{% block 坑名 %}` `{% endblock %}`

继承模板：`{% extends '继承的模板文件名' %}`

保留父坑内容：`{{ block.super }}`

上传文件需要在form表单中指定 enctype="multipart/form-data"

```html
<form action='' method='post' enctype="multipart/form-data"></form>
```

`{% verbatin %}{% endvarbatin %}` - django模板渲染忽略不进行渲染的部分

## 4. Form表单对象

form表单对象是专门用来验证表单数据的对象

clean()为验证所有的字段

clean_xxx()为验证xxx的字段，需要使用`raise ValidationError('错误信息')`抛出错误

```python
class LoginForm(forms.Form):
    password = forms.CharField(
        # 不剪切前后的空格
        strip=False,
        # 不允许为空格
        required=True,
        # 设置最小长度为8
        min_length=8,
        # 设置报错内容
        error_messages={
            'required': '请输入密码',
            'min_length': '密码最少为8个字符',
        }
    )
    def clean_repassword(self):
        repassword = self.cleaned_data['repassword']
        if self.cleaned_data['password'] != repassword:
            raise ValidationError('两次输入密码必须一致')
        return make_password(repassword)
   	
    def clean(self):
        password = self.cleaned_data.get('password')
        return self.cleaned_data
```

```python
# 使用模型中定义的字段进行验证
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        # 排除的字段
        exclude = ('no', 'regedister_date')
```

```python
# 使用模型的字段后，如果进行字段保存可以使用
form = RegisterForm(request.POST)
if form.is_valid():
	form.save()
```

在调用表单对象有三个重要的方法：

>   1.  is_valid - 进行表单验证
>   2.  errors - 返回验证错误产生的错误信息（字典）
>   3.  cleaned_data - 返回验证通过的数据（字典）

```python
form = LoginForm(request.POST)
form.is_valid()
errors = form.errors
cleaned_data = form.cleaned_data
```

## 5. 接入Redis缓存服务

安装三方库django-redis：`pip install django-redis`

修改django项目的setting.py配置文件

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            # redis地址加数据库名
            'redis://120.77.222.217:6379/0',
        ],
        # 设置redis中键的前缀
        'KEY_PREFIX': 'django1905:polls',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 256,
            },
            # redis密码
            'PASSWORD': '1qaz2wsx',
        }
    },
    'moblie': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            # redis地址加数据库名
            'redis://120.77.222.217:6379/1',
        ],
        # 设置redis中键的前缀
        'KEY_PREFIX': 'django1905:code',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 128,
            },
            # redis密码
            'PASSWORD': '1qaz2wsx',
        }
    },
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 设置缓存过期时间（单位：秒）
SESSION_CACHE_ALTAS = 'default'
SESSION_COOKIE_AGE = 86400
```

如果需要访问其他缓存配置：
```python
form django.core.cache import caches

caches['mobile'].set(tel, code, timeout=300)
caches['mobile'].get(tel)
```

直接操作redis数据库：
```python
from django_redis import get_redis_connection
redis_cli = get_redis_connection(alias='default')
# 该对象可以调用所有redis的方法
redis_cli.get()
```

## 6.cookie/session/token

### 6.1 用户跟踪方法：

>   1.  URL重写：`http://foo.com/bar/?sessionid=xyz`
>
>   2.  隐藏域/隐式表单域/埋点：`<input type="hidden" name="sessionid" value="xyz">`
>
>   3.  浏览器本地存储：cookie/localStorage/sessionStorage
>
>       cookie：sessionid=xyz - 每次请求自动带上
>
>       localStorage.sessionid="xyz" - 本地存储，主动清空才消失
>
>       sessionStorage.sessionid="xyz" - 本地存储，浏览器关闭自动消失

### 6.2 读写cookie

读取请求头中的cookie信息：`request.COOKIES['key']` - 返回key对应的value

通过响应将cookie写入浏览器：`response.set_cookie(key, value, 超时时间)`

删除cookie：自动过期/`response.delete_cookie(key)`

读写带签名的cookie，salt为签名内容（会进行加密链接到value后面）：

>   response.set_signed_cookie(key, value, salt, 超时时间)
>
>   request.get_signed_cookie(key, salt)

## 7. 日志和debug-toolbar

### 7.1 日志配置

`项目名>setting:`

```python
LOG_ROOT = 'C:/User/Administrator/Desktop/'
LOGGING = {
    'version': 1,
    # 是否禁用其他日志生成器
    'disable_existing_loggers': False,
    # 配置日志格式化器
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                      '%(module)s.%(funcName)s line %(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # 配置日志过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 配置日志处理器
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        'file1': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'access.log',
            # 每周天生成一个新的日志文件
            'when': 'W0',
            # 总共支持存在的日志文件
            'backupCount': 12,
            'formatter': 'simple',
            'level': 'INFO',
        },
        'file2': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'error.log',
            # 每天生成一个新的日志文件
            'when': 'D',
            # 总共支持存在日志文件的数量
            'backupCount': 31,
            'formatter': 'verbose',
            'level': 'WARNING',
        },
    },
    # 配置日志器
    'loggers': {
        'django': {
            'handlers': ['console', 'file1', 'file2'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
```

python日志级别：DEBUG<INFO<WARNING<ERROR<CRITICAL

loggers 接收日志

handlers 处理日志

formaters 设置记录格式

### 7.2 django-debug-toolbar配置

说明：不能用于前后端分离项目

使用前需要先安装`pip install django-debug-toolbar`

```python
# 项目名>setting.py>INSTALLED_APPS:
'debug_toolbar'

# 项目名>setting.py>MIDDLEWARE:
'debug_toolbar.middleware.DebugToolbarMiddleware'

# 项目名>setting.py>
DEBUG_TOOLBAR_CONFIG = {
    # 引入jQuery库
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js'
    # 工具栏是否折叠
    'SHOW_COLLAPSED': True,
    # 是否显示工具栏
    'SHOW_TOOLBAR_CALLBACK': lambda x: True,
}

# 项目名>urls.py
import debug_toolbar
urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))
```

## 8. 模型中对应关系

### 8.1 一对一

模型定义方法：

`info = models.OneToOneField(StudentInfo, on_delete=models.CASCADE)`

说明：本例定义在Student中，关联StudentInfo。

找到关联的对象：

定义数据：

>   stu = Student()
>
>   info = StudentInfo()

`stu.info` - 返回关联的对象

`stu.info = info` - 给外键列加数据

`stu.info_id` - 返回关联对象的id值

`info.student` - 返回关联的对象（后面是模型对象小写）

如果定义中加入`related_name=a`条件

`info.a` - 返回关联的对象

### 8.2 一对多

模型定义方法：

`g = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)`

说明：一对多要定义在多的一方，此例定义在Student中，关联外键为Grade

定义数据：

>   stu = Student.objects.filter().first()
>
>   grade = Grade.objects.filter().first()

`stu.g = g` - 给外键列加值

`stu.g` - 返回关联的对象

`grade.student_set.all()` - 返回所有关联的对象的列表（后面是模型对象小写加_set）

在定义模型的时候添加了`related_name = s`

`grade.s.all()` - 获取所有关联对象的列表

### 8.3 多对多

模型定义方法：

`c = models.ManyToManyField(Course)`

说明：多对多定义在任意一方即可。此例定义在Student中，关联外键为Course，多对多会自动创建一个中间表，名字分别为关联表表名小写加_id。

定义数据：

>   stu = Student.objects.get(pk=1)
>
>   cou = Course.objects.get(pk=5)

`stu.c.add(cou)` - 向中间表中添加一条数据

`cou.student_set.add(stu)` - 向中间表中添加一条数据

`stu.c.remove(cou)` - 删除一条中间表中的数据

在定义模型的时候添加了`related_name = d`

`cou.d.add(stu)` - 向中间表中添加一条数据

### 8.4 外键关联数据保护

定义模型时设置`on_delete`的值：

>   models.CASCADE: 级联删除，主键删除，外键数据也删除
>
>   models.PROTECT: 保护模式，不让删除主键信息
>
>   models.SET_NULL: 滞空模式，删除主键，外键滞空

## 9. url路由

### 9.1 路由分发

示例：`path('app/', include('app.urls'))`

说明：链接到本地址的url中如果包含app，则又链接到app.urls路由文件中去

### 9.2 路由重命名

分发路由重命名：

示例：`path('app2/', include(('app2.urls', 'app2'), namespace='ap2'))`

说明：将app2地址重命名为ap2

直接定向路由重命名：

示例：`path('login/', login, name='login')`

说明：将login地址重命名为login

路由重命名使用：

示例：`return redirect(reverse('ap2:login', kwargs={'id': 11}))`

实际结果：`return redirect('app2/login/11/')`

说明：使用reverse重新拼接url，如需传参数，使用kwargs或者args

### 9.3 路由参数

Django2.0以上版本：

语法：`<类型:参数名>`

示例：`path('params2/<str:name>/', params2)`

`path('params4/<uuid:uid>', params4)`

实际结果：`127.0.0.1:8000/app2/params2/jdkfjsld/`

说明：传递一个name参数，类型为string。uuid格式为`8-4-4-4-12`个参数，每个参数为0到9a到z的值

Django2.0一下版本：

语法：`(?P<参数名>正则表达式)`或 `(正则表达式)`

示例：`url(r'params6/(\d+)/(\d+)', params6, name='p6')` `url(r'params7/(?P<name1>\d+)/(?P<name2>\d+)/', params7)`

说明：Django2.0一下版本的`url`和2.0版本以上的`re_path`用法一样

## 10. 中间件

中间件是在执行功能代码之前执行的代码：

`process_request` - 在响应和路由解析之间执行，不能返回或者返回None

`process_view` - 在路由解析和视图函数之间执行

`process_response` - 在视图函数和返回响应之间执行，必须返回response

`process_exception` `process_template_response` - 不会自动调用执行

执行过程：

![官方执行过程](./img/django中间件官网图.png)

在process_request中使用return的执行顺序

![process_request中return了执行顺序](./img/django中间件request返回.png)

在process_view中返回执行顺序

![process_view中返回执行顺序](./img/django中间件有返回执行顺序.png)

示例：

```python
from django.utils.deprecation import MiddlewareMixin
class Test1Middleware(MiddlewareMixin):
    # 在寻找路由之前执行
    def process_request(self, request):
        print('text1 process_request ')

    def process_response(self, request, response):
        print('text1 process_response ')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs_):
        print('test1 process_view')
```

自定义中间键函数(新版本推荐)

```python
from django.shortcuts import redirect

def check_loign_middleware(func):
    """定义两个下载链接需要"""
    def wrapper(request, *args, **kwargs):
        path = request.path
        if path in ('/vote/pdf/', '/vote/excel/'):
            if 'user' not in request.session:
                return redirect('/login/')
            return func(request, *args, **kwargs)
        return warpper
```

## 11. 图片上传和图片加载

图片上传：

```python
image = models.ImageField(upload_to='imgs')
# 将文件上传到媒体文件夹下的imgs文件夹中，需要用pip安装pillow包
```

```html
<form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <p>选择图片：<input type="file" name="img"></p>
        <p><input type="submit" value="提交"></p>
</form>
```

后台获取文件：

```python
icon_img = request.FILES.get('img')
```

指定媒体文件夹（将图片保存在此文件夹下）：

`项目文件夹>setting`

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

加载文件配置：

`项目文件夹>urls`

```python
from django08.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.staticfiles.urls import static
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
```

## 12. 装饰器

`cache_page()`

页面缓存，可以设置缓存时间，以秒为单位

`method_decorator(decorator, name='')`

将函数装饰器改为类装饰器，decorator指定装饰器名称和参数，name指定要修饰的方法名称

```python
method_decorator(decorator=cache_page(cache='default', timeout=300), name='list')
```

## 13. 分页

```python
from django.core.paginator import Paginator

queryset = Article.objects.all()
p = Paginator(queryset, 5)  # 指定每页显示5条
p.count  # 总共数据条数
p.num_pages  # 总共页数
p.objects_list  # 所有的数据
page2 = p.page(2)
page2.has_previous()  # 是否有上一页
page2.has_next()  # 是否有下一页
page2.previous_page_number()  # 上一页的页码
page2.next_page_number()  # 下一页的页码
```

## 14. 前端集成富文本编辑器

使用KindEditor

> 1. 下载解压后放在static/js/ 目录下
>
> 2. 有用的文件有：/lang/， /plugins/， /themes/， /kindeditor-all-min.js/
>
> 3. 前端页面：
```html
<textarea name="intro" id="intro"></textarea>
<script src="{% static 'js/kindeditor-4.1.12/kindeditor-all-min.js' %}"></script>
<script>
    let editor = null
    KindEditor.ready(function(K){
        editor = K.create('textarea[name=intro]', {
            width: '700px',
            height: '300px',
        })
    })
</script>
```

# 二. djangorestframework框架

## 1. 介绍

前后端分离开发框架，主要用于后端数据返回

安装方法：

```python
pip install djangorestframework==3.10.3
pip install django-filter
```

## 2. 配置与结构

```python
# 项目名>setting>INSTALLED_APP中添加：
'rest_framework',
```

```python
# 应用名>urls
from rest_framework.routers import SimpleRouter
from 应用名.views import *

# 1.生成路由对象，路由对象可以用于管理路由地址
router = SimpleRouter()
# 2.注册资源，注意：此处路由后面不需要添加/，系统会自动补
router.register('地址名词', 视图类名)

urlpatterns = [
]
# 通过router.urls获取自动生成的地址
urlpatterns += router.urls
```

```python
# 项目名>urls

urlpatterns = [
	path('地址名词(最好是应用名)', include('应用名.urls'))
]
```

```python
# 应用名>views
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from 项目名.models import 模型类
from 项目名.serializers import 序列化器类
from 项目名.filters import 过滤器类

class ArticleView(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,  # POST /app/article/  创建类
                  mixins.ListModelMixin,  # GET /app/article/  查询类
                  mixins.RetrieveModelMixin,  # GET /app/article/[id]/  获取详情类（获取一个数据）
                  mixins.DestroyModelMixin,  # DELETE /app/article/[id]/  删除类
                  mixins.UpdateModelMixin): # PUT/PATCH /app/article/[id]/  更新类

    # queryset参数默认值为路由注册资源所对应的表的所有数据
    queryset = 模型类名.objects.all()
    # 序列化和字段校验功能
    serializer_class = 序列化器类名
    # 过滤类
    filter_class = 过滤器类名
```
> GenericAPIView主要作用就是定义了queryset、serializer_class等属性。
>
> viewsets.GenericViewSet 继承自 GenericAPIView
>
> CreateAPIView 继承自 CreateModelMixin 和 GenericAPIView
>
> ListAPIView 继承自 ListModelMixin 和 GenericAPIView
>
> RetrieveAPIView 继承自 RetrieveModelMixin 和 GenericAPIView
>
> DestroyAPIView 继承自 DestroyModelMixin 和 GenericAPIView
>
> UpdateAPIView 继承自 UpdateModelMixin 和 GenericAPIView
>
> ListCreateAPIView 继承自 ListModelMixin CreateModelMixin 和 GenericAPIView
>
> RetrieveUpdateAPIView 继承自 RetrieveModelMixin UpdateModelMixin 和 GenericAPIView
>
> RetrieveDestroyAPIView 继承自 RetrieveModelMixin DestroyModelMixin 和 GenericAPIView
>
> RetrieveUpdateDestroyAPIView 继承自 RetrieveModelMixin UpdateModelMixin DestroyModelMixin 和 GenericAPIView
>
> ModelViewSet 继承自所有的ModelMixin和GenericAPIView
```python
# 应用名>serializers
from rest_framework import serializers
from app.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    """
    实现序列化，序列化的字段由fields来定义
    实现字段校验，默认将model中指定的Article模型中定义的约束条件进行校验
    """
	title = serializers.CharField(required=True, max_length=10, min_length=3, error_messages={'require': 'title必填', 'max_length': '不超过10字符', 'min_length': '不短于3字符'})

    class Meta:
        model = Article
        fields = '__all__'
    # 重写序列化方法1
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['type'] = ArticleType2Serializer(instance.type).data
        return data
    # 重写序列化方法2
    password = serializers.SerializerMethodField()

    @staticmethod
    # 本处参数为序列化类的小写名。
    def get_password(user):
        return make_password(user.password)
```

```python
# 应用名>filters
import django_filters
from 应用名.models import Article

class ArticleFilter(django_filters.rest_framework.FilterSet):
    # 接口中定义的参数字段 = django_filters.CharFilter('模型中需过滤的字段')
    title = django_filters.CharFilter('title')
    
    # 模糊查询
    title = django_filters.CharFilter(lookup_expr='icontains')

    # 自定义方法查询
    is_delete = django_filters.CharFilter(method='filter_is_delete')

    class Meta:
        model = Article
        fields = []

    # 老版本djangorestframework中叫action，新版本中叫method
    def filter_is_delete(self, queryset, name, value):

        if value == 'yes':
            return queryset.filter(is_delete=True)
        else:
            return queryset.filter(is_delete=False)
```

说明：

>   1.  `title = django_filters.CharFilter()` - 如果接口中定义的参数字段和过滤的字段一样，CharFilter中可以不用写过滤字段
>   2.  `title = django_filters.CharFilter(lookup_expr='icontains')` - `lookup_expr`后接为模糊查询条件 contains、gt、gte、lt、lte
>   3.  `is_delete = django_filters.CharFilter(method='filter_is_delete')` - `method`后接自定义查询方法名

## 3. CRUD解析

### 3.1 创建

CreateModelMixin 使用POST请求，

源码解析：

>   `self.get_serializer(data=request.data)` - 表示对数据进行表单验证，如果需要自定义校验方法，就再serializers文件的对应类里面进行自定义验证：

```python
title = serializers.CharField(required=True,
                                  max_length=10,
                                  min_length=3,
                                  error_messages={'require': 'title必填',
                                                  'max_length': '不超过10字符',
                                                  'min_length': '不短于3字符'})
```

重写CreateModelMixin

> POST请求使用request.data取请求参数

```python
def create(self, request, *args, **kwargs):
    # 接收post请求传递的参数，request.data
    data = request.data
    # 将获取到的参数丢给ArticleSerializer进行字段校验
    serializer = self.get_serializer(data=data)
    # is_valid()校验成功还是失败
    result = serializer.is_valid()
    if result:
        serializer.save()
        return Response(serializer.data)
    else:
        errors = serializer.errors
        return Response(errors)
```

### 3.2 查询

ListModelMixin 使用GET请求

源码解析

>   `self.get_queryset()` - 为获取模型中所有的对象，等同于`模型名.objects.all()``
>
>   ``self.get_serializer(page, many=True)` - 为将所有传递的对象进行序列化，及将模型对象转换为字典，调用的是seralizer中相应的类方法

重写ListModelMixin

> GET请求用request.query_params获取参数
>
> eg: title = request.query_params.get('title')

```python
def list(self, request, *args, **kwargs):
    # get_queryset()方法默认返回Article.objects.all()的结果
    queryset = self.get_queryset()
    # get_serializer()方法默认返回ArticleSerializer
    # 实现将queryset中的每个对象转化为dict
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)
```

### 3.3 更新

UpdateModelMixin 使用PUT请求或者PATCH请求

PUT请求为整个字段更新，PATCH为字段局部更新（只更新某一列）

源码解析：

>   `self.get_object()` - 为获取到的对象，默认用主键筛选

重写UpdateModelMixin

```python
def update(self, request, *args, **kwargs):

    # 1.获取对象
    instance = self.get_object()
    # 2.获取修改的参数
    data = request.data
    # 3.参数校验
    serializer = self.get_serializer(instance, data=data)
    # raise_exception=True，如果is_valid校验失败，直接往外抛异常
    serializer.is_valid(raise_exception=True)
    # 4.数据保存
    serializer.save()

    return Response({'msg': '修改数据成功'})
```

### 3.4 删除

DestroyModelMixin 请求方式为DELETE

重写DestroyModelMixin：

```python
def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.is_delete = True
    instance.save()
    return Response({'msg': '删除成功'})
```

### 3.5 获取单一对象详情

RetrieveModelMixin 请求方式为GET

重写RetrieveModelMixin

```python
# 获取详情
def retrieve(self, request, *args, **kwargs):
    # 1.获取对象
    # instance = Article.objects.filter(pk=kwargs['pk']).first()
    instance = self.get_object()
    # 2.序列化
    # serializer = ArticleSerializer(instance)
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
```

### 3.6 CRUD中用到的方法

语法：`serializer = self.get_serializer(data=request.data)`

`serializer = self.get_serializer(queryset, many=True)`

说明：当传入data=request.data时，进行字段校验；当传入一个queryset时，表示将字段进行序列化，多个字段需要声明many=True。等同于写定义的serializer类名

语法：`instance = self.get_object()`

说明：表示获取传入值作为主键的那一列值，等同于`instance = User.object.filter(id=2).first()`

语法：`self.get_queryset()`

说明：用来获取所有的查询对象，等同于`User.objects.all()`

## 4. 序列化

序列化结果对象的data属性为序列化后的数据

序列化类初始内容：

```python
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # 定义序列化的字段，__all__表示所有字段
        # 需要排除字段试用exclude = ["字段名", ]
        fields = '__all__'
```

实现字段校验，默认将model中指定的Article模型中定义的约束条件进行校验，如果需要自定义校验方法，可以自定义，格式类似form表单验证：

```python
title = serializers.CharField(required=True,
                              max_length=10,
                              min_length=3,
                              error_messages={'require': 'title必填',
                                              'max_length': '不超过10字符',
                                              'min_length': '不短于3字符'})
```

如果需要定制序列化结果，可以在类中写`to_representation`函数：

```python
def to_representation(self, instance):
    data = super().to_representation(instance)
    data['type'] = ArticleType2Serializer(instance.type).data
    return data
```

## 5. 过滤

主要针对条件查询，将条件放在过滤类中，就可以进行条件查询

默认不需要进行过滤，如需要定制过滤方法，可以使用fliters

配置：`项目名>setting`末尾添加：

```python
REST_FRAMEWORK = {
    # 过滤类的配置
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}
```

在views中的类中声明表示需要进行过滤操作：

`filter_class = ArticleFilter`

```python
class ArticleFilter(django_filters.rest_framework.FilterSet):
    # 接口中传递的参数字段 = django_filters.CharFilter('模型中需过滤的字段')
    title = django_filters.CharFilter('title')
    
    # 模糊查询
    title = django_filters.CharFilter(lookup_expr='icontains')

    # 自定义方法查询
    is_delete = django_filters.CharFilter(method='filter_is_delete')

    class Meta:
        model = Article
        fields = []

    # 老版本djangorestframework中叫action，新版本中叫method
    def filter_is_delete(self, queryset, name, value):

        if value == 'yes':
            return queryset.filter(is_delete=True)
        else:
            return queryset.filter(is_delete=False)
    
    # 自定义所有的字段查询方法
    @property
    def qs(self):
        parent = super(ArticalFilter, self).qs
        q = Q()
        title = self.request.query_params.get('title')
        if title:
            q |= Q(title__icontains=title)
        is_delete = self.requset.query_params.get('is_delete')
        if is_delete:
            q |= Q(is_delete=is_delete)
        return parent.filter(q) 
```

说明：

>   1.  `title = django_filters.CharFilter()` - 如果接口中定义的参数字段和过滤的字段一样，CharFilter中可以不用写过滤字段
>   2.  `title = django_filters.CharFilter(lookup_expr='icontains')` - `lookup_expr`后接为模糊查询条件 contains、gt、gte、lt、lte
>   3.  `is_delete = django_filters.CharFilter(method='filter_is_delete')` - `method`后接自定义查询方法名

## 6. 特殊url实现

**装饰器action装饰方法，装饰器中的detail参数为False时，函数主键不能作为url中的一部分**

`@action(detail=False)` 等于 `@list_route()`

`@action(detail=True)`  等于 `@detail_route()`

`@list_route()`和 `@detail_route()`在3.10版本已被移除

```python
@action(detail=False, methods=['POST', 'GET'])
def article(self, request):
    # 请求方式 GET
    # 请求地址 /app/type/article/
    """
        返回json结构
        {
            {
                id: '',
                t_name: '',
                articles:[{}, {}]
            }
        }
        """
    queryset = self.get_queryset()
	serializer = self.get_serializer(queryset, many=True)
	return Response(serializer.data)
```

```python
@action(detail=True)
def articles(self, request, pk):
    # 请求方式 GET
    # 请求地址 /app/type/[id]/articles/
    """
        {
            id: '',
            t_name: '',
            articles: [{}, {}]
        }
        """
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
```

## 7. 请求方法装饰器

### 7.1 装饰视图函数

此方法可以更灵活的使用调用模型

通过`api_view`装饰器装饰视图函数

路由定义：`path('type_article/', type_article),`

视图函数：

```python
@api_view(['GET'])
def type_article(request):
    """
    注册资源和定义装饰器api_view的使用区别
    如果是注册资源，操作的模型固定了
    如果是定义装饰器api_view，模型没有固定。

    {
        'types': [{}, {}]
        'articles': [{}, {}]
    }
    """
    types = ArticleType.objects.all()
    articles = Article.objects.all()
    res = {
        'types': ArticleType2Serializer(types, many=True).data,
        'articles': ArticleSerializer(articles, many=True).data
    }

    return Response(res)
```

说明：一定要在装饰器后面写请求参数，没有默认请求参数

通过继承APIView来写类方法

路由定义：`path('article_msg/', ArticleMsg.as_view())`

视图类：

```python
class ArticleMsg(APIView):
    # 表示get请求
	def get(self, request, *args, **kwargs):
        types = ArticleType.objects.all()
        articles = Article.objects.all()
        res = {
            'types': ArticleType2Serializer(types, many=True).data,
            'articles': ArticleSerializer(articles, many=True).data
        }
        return Response(res)
```

说明：函数名表示请求方式

### 7.2 装饰类的装饰器

```python
# api_view只能装饰函数，不能装饰类
# 装饰类，使用method_decorator
@method_decorator(decorator=cache_page(), name='retrieve)
class SearchViewSet(CacheResponseMixin, ModelViewSet):
    queryset = Record.objects.all().order_by('-makedate')
    serializer_class = RecordSerializer
    pagination_class = CustomPagination
```

## 8. 自定义返回格式

`项目名>setting`最后添加：

```python
REST_FRAMEWORK = {
    ...
    # renderer的配置
    'DEFAULT_RENDERER_CLASSES': (
        'utils.renderer.MyJsonRenderer',
    ),
}
```

自定义格式类：继承JSONRenderer，重写render方法

```python
from rest_framework.renderers import JSONRenderer

class MyJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        需要做的操作就是将data的值添加code/msg/data
        {
            'code': 0,
            'msg': '请求成功',
            'data': data
        }
        """
        # 注意：data中有可能有code、data、msg
        try:
            msg = data.pop('msg')
        except:
            msg = '请求成功'

        try:
            code = data.pop('code')
        except:
            code = 0

        try:
            result = data['data']
        except:
            result = data

        res = {
            'code': code,
            'msg': msg,
            'data': result
        }
        return super().render(res)
```

如需对报错信息自定义：

在serializer文件的校验类中重写validate函数

```python
t_name = serializers.CharField(max_length=10, min_length=3, required=True)

def validate(self, attrs):
    t_name = attrvalidates.get('t_name')
    if ArticleType.objects.filter(t_name=t_name).exists():
        res = {'code': 1002, 'msg': '分类名称已重复'}
        raise ParamsException(res)
        return attrs
```

说明：

因为要继承一个初始异常类，所以需要自定义一个异常类：

```python
from rest_framework.exceptions import APIException

class ParamsException(APIException):

    def __init__(self, msg):
        self.detail = msg
```

## 9. 分页

指定某一个类使用分页的方法：

```python
# 应用名.views
class User(ModelViewSet):
    quseryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

# 项目名.settings
REST_FRAMEWORK = {
    'PAGE_SIZE': 3,
}
```

默认配置

`项目名>setting`最后添加：

```python
REST_FRAMEWORK = {
    # 分页配置
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	# 设置每页显示数量
    'PAGE_SIZE': 3,
}
```

说明：此方法的url中为`?page=1`

如果使用limit方式显示

url为：`http://127.0.0.1:8080/user/student/?limit=2&offset=2`

配置为：

```python
REST_FRAMEWORK = {
    # 分页配置
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
	# 设置每页显示数量
    'PAGE_SIZE': 3,
}
```
```python
# 自定义游标分类
class AgentCurcorPagination(CorsurPagination):
    page_size_query_param = 'size'
    max_page_size = 50
    # 特别注意需要排序字段
    ordering = '-agentid'
```

## 10. 登录和注销

登录的视图函数

```python
@action(detail=False, methods=['POST'], serializer_class=UserLoginSerializer)
def login(self, request):
    # 1. 获取参数
    data = request.data
    # 2. 字段校验
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    # 3. token和登录用户的关联关系的保存
    # 保存：mysql、redis、mongodb
    # redis存储类型：string
    token = uuid.uuid4().hex
    user = User.objects.get(username=data.get('username'))
    # 3.1 向redis中设置string类型的数据
    cache.set(token, user.id, timeout=1000)
    res = {
        'token': token
    }
    return Response(res)
```

注销方法：将redis中的token值删除掉

## 11. 用户验证

重写authenticate验证函数

```python
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from app.models import User
from utils.errors import ParamsException


class MyUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # TODO:将不需要做登录校验的地址屏蔽掉
        ignore_path = ['/app/user/login/', '/app/user/register/']
        if request.path in ignore_path:
            user = ''
            token = ''
            return user, token
        token = request.query_params.get('token')
        if not token:
            raise ParamsException({'code': 1007, 'msg': '无法访问'})
        user_id = cache.get(token)
        if not user_id:
            raise ParamsException({'code': 1008, 'msg': '无法访问'})
        user = User.objects.get(pk=user_id)
        return user, token
```

如果需要单独对某个视图类进行用户验证，可以在该视图类中添加

`authentication_classes = (MyUserAuthentication,)`来进行验证

如果需要对全局访问都进行用户验证，需要配置：

`项目名>setting`：

```python
REST_FRAMEWORK = {
    ...
    # 全局认证类
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 该名称的组成为：应用名.自定义的用户认证py文件.自定义的用户认证类
        'app.userauth.MyUserAuthentication',
    )
}
```

## 12. 跨域

跨域的意思为**请求方式、请求地址、请求端口**中任意有一项不一样的跨域名访问。

如使用`http://localhost:65534`访问`http://localhost:8000`就输入跨域访问

配置允许跨域需要先安装`pip install django-cors-headers`

允许跨域访问配置：

`项目名>setting`

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    ...
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
   	'django.middleware.common.CommonMiddleware',
    ...
]
...
# 跨域允许的请求方式，可以使用默认值，默认的请求方式为:
# from corsheaders.defaults import default_methods
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

# 允许跨域的请求头，可以使用默认值，默认的请求头为:
# from corsheaders.defaults import default_headers
# CORS_ALLOW_HEADERS = default_headers

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# 跨域请求时，是否运行携带cookie，默认为False
CORS_ALLOW_CREDENTIALS = True
# 允许所有主机执行跨站点请求，默认为False
# 如果没设置该参数，则必须设置白名单，运行部分白名单的主机才能执行跨站点请求
CORS_ORIGIN_ALLOW_ALL = True
```

说明：**中间键的添加位置很重要**。

## 13. 访问节流

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        # 'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        # 每分钟60次
        'anon': '60/min',
        # 'user': '1000/day'
    }
}
```

## 14. 任务异步化

使用前安装`pip install celery`

使用步骤：

```python
import celery

# 创建消息队列对象，指定模块名、消息代理（消息队列）和持久化方式
app = celery.Celery('包.模块名',
					broker="redis://username:password@ip地址:6379/数据库名",
					backend="redis://username:password@ip地址:6379/数据库名")
app.autodiscover_tasks()


# 给使用的函数上打@app.task这个装饰器
# 然后在调用这个函数的地方使用 函数名.delay()实现异步化
# 消费 celery -A 模块名 worker -l 
```

持久化任务结果

持久化到Redis

backend = "redis://username:password@ip地址:6379/数据库名"

持久化到数据库


# 三. Vue框架

## 1. 安装

安装vue框架首先需要安装node.js

`node -v` - 查看node.js版本

`npm -v` - 查看npm版本

说明：npm是node.js的包管理工具，类似于python与pip

`sudo npm install npm -g` - linux升级npm命令

`npm install npm -g` - windows升级npm命令

说明：后面加参数g表示全局安装的意思

`npm install cnpm -g` - 安装cnpm，cnpm安装速度比npm快

`cnpm -v` - 查看cnpm版本

`cnpm uninstall 包名` - 卸载模块

`cnpm update 包名` - 更新模块

`cnpm search 包名` - 搜索模块

`cnpm install vue` - 安装vue

`cnpm install --global vue-cli` - 全局安装vue-cli

创建vue项目

`vue init webpack vue项目名` - 创建一个项目名

`cd vue项目文件夹` - 进入项目文件夹

`cnpm install` - 安装相关依赖项

`cnpm run dev` - 启动vue项目

## 2. 项目结构

```
build: 项目构建(webpack)相关代码
config: 配置目录，包括端口号等。我们初学可以使用默认的。
node_modules: npm 加载的项目依赖模块
src: 开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：
	assets: 放置一些图片，如logo等。
	components: 目录里面放了一个组件文件，可以不用。
	router: 路由文件目录
		index.js: 路由设置文件
	App.vue: 项目入口文件，我们也可以直接将组件写这里，而不使用 components 目录。
	main.js: 项目的核心文件。
static: 静态资源目录，如图片、字体等。
test: 初始测试目录，可删除
.xxxx文件: 这些是一些配置文件，包括语法配置，git配置等。
index.html: 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。
package.json: 项目配置文件。
README.md: 项目的说明文档，markdown 格式
```

vue中页面都是继承自index.html；index.html的body中有个div，id为app，同App.vue中的body关联，其他页面在App.vue中注册即可生成相应完整的html。

## 3. 路由

要生成一个路由，需要进行以下配置：

`src>router>index.js`中注册路由地址：

```vue
import Home from '@/components/Home'
import About from '@/components/About'
var routes = [
  { path: '/home', component: Home },
  { path: '/about', component: About }
]
```

说明：path表示url路径地址，component表示链接组件

vue中超链接一般使用`<router-link to="/articles">文章列表</router-link>`

router-link生成的路由在`#`后面，如果使用a标签生成的路由在`#`前面

## 4. 创建组件

在conponent中创建一个组件用于定制页面中的具体内容

具体格式：

```vue
<template>
  <div id="">
    <!-- 本段用来写页面，所有内容必须被一个div包围起来 -->
  </div>
</template>
<script>
export default{
  data () {
    return {
      // 此处写数据
    }
  },
  methods: {
  	// 此处写方法
  }
}
</script>
<style>
    /* 此处写样式 */
</style>
```

## 5. vue封装的ajax

使用前需要先安装

`npm install --save axios vue-axios`

在入口函数main.js中引入

```javascript
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
```

如果需配置全局axios访问的路由前缀，可以配置如下内容:

```javascript
import axios from 'axios'

const ajax = axios.create({
  baseURL: 'http://127.0.0.1:8000'
})
Vue.config.productionTip = false
Vue.prototype.axios = ajax
```

使用方法：

```javascript
const params = {
	'username': this.username,
	'password': this.password
}
// 如果配置了全局地址前缀，url可以简写
var url = '/app/user/register/'
// 如果没有配置全局地址前缀
var url = 'http://127.0.0.1:8000/app/user/register/'
// 使用post请求，如果需要使用get请求用
// this.axios.get(url, params)
// 如果没有参数，可以不传
this.axios.post(url, params)
	.then(res => {
		console.log(res)
		if (res.data.code === 0) {
			// 网页跳转方法
			this.$router.push('/login')
		}
	})
	.catch(ers => {
		alert('失败')
	})
```

# 四. Flask

## 1. 安装配置

```
mkdir src - 创建一个源代码路径

python3 -m venv venv - 创建一个虚拟环境

source venv/bin/activate - 激活虚拟环境

pip install flash - 安装flask
```

然后开始使用吧

flask默认的模板文件夹为templates，默认静态文件夹为static，位置均为启动程序的同级目录

查找静态文件的方式

```
url_for('static', filename='/js/test.js')
```

## 2. flask项目结构

```python
from flask import Flask, request

# 实例化flask对象
app = Flask(__name__)

# route为路由
@app.route('/')
def index():
    return '你好，我要上班挣钱了'

# 传递参数并获取
@app.route('/users/<name>')
def users(name):
    return '<h1><span style="color: red;">%s</span>，吃饭没</h1>' % name

# 获取访客的信息
# 获取get参数
@app.route('/getip')
def getip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    return '你的ip地址是：%s，user-agent是：%s' % (ip, user_agent)

def main():
    # app.run(debug=True)
    # 指定访问的ip和端口
    app.run(debug=True, host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main()
```

## 3. 程序和请求上下文

current_app	    程序上下文	当前激活程序的程序实例

g				程序上下文	处理请求时用作临时存储对象

request			请求上下文	请求对象

session			请求上下文	回话对象

说明：以上四种上下文都是对象，都需要进行`from flask import `导入才能使用

`request.args.get('参数名')` - 获取get请求的参数

`request.form.get('参数名')` - 获取post请求的参数

`request.header.get('参数名')` - 获取请求头里面的参数

## 4. 路由

flask路由由视图的装饰器来决定，如果需要分模块路由转发需要用蓝图进行注册。

url尾部加/

`app.route('/projects/')` - 在访问时如果不加最后的`/`，浏览器会自动添加

`app.route('/about')` - 在访问时如果加了最后的`/`，会报错

路由参数：

```python
app.route('/index/<string:username>', methods=['GET', 'POST'])
def index(username):
    pass
```

请求方式可以通过route装饰器后的methods参数指定，默认为GET。如果有参数，需要将参数传递给视图函数，参数支持的类型：

| `类型`  | 说明                                |
| ------- | ----------------------------------- |
| `int`   | 接受正整数                          |
| `float` | 接受正浮点数                        |
| `path`  | 类似 `string` ，但可以包含斜杠      |
| `uuid`  | 接受 UUID 字符串                    |
| string  | （缺省值） 接受任何不包含斜杠的文本 |

## 5. 响应

**return响应**

通过在return后面加一个数字自定义响应值，默认响应成功为200

`return '<h2>Bad Request</h2>', 404`

通过`make_response`手动创建一个响应对象

使用前需要先导入`from flask import make_response`

**重定向**： 使用前需要先导入`from flask import redirect`

```python
# 重定向
@app.route('/jump')
def jump():
    username = 'jon'
    return redirect('/login/%s' % username)
```

**abort抛异常**，使用前需要先导入`from flask import abort`

```python
# abort抛异常的方法
@app.route('/guess/<int:number>')
def guess(number):
    if number < 8000:
        abort(404)
    return '<h1>你猜对了</h1>'
```

说明：abort括号内只能接收异常状态码

**url_for反向解析**：

url_for 用视图函数名返回对应的url

```python
url = url_for('index') # 相对链接  /
url = url_for('index', _external=True) # 绝对链接，比如放在邮件里面 http://127.0.0.1:5000/
url = url_for('login', username='carmack', v=1) # /login/carmack/?v=1
```

无参情况: url_for('蓝图中定义的第一个参数.函数名')
有参情况: url_for('蓝图中定义的第一个参数.函数名', 参数名=value)

**模板渲染**：flask默认使用template路径中的模板，如果有子目录，则从子目录开始写起

```
return render_templeate('users/login.html', form=form)
```

**自定义错误页面**：装饰器参数表示错误码，错误页面函数的形参必须传一个e

```python
# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def errorhandler(e):
    return render_template('500.html'), 500
```

## 6. Flask-Script启动参数

方便在启动flask程序的时候进行参数传递

安装flask-script包`pip install flask-script`

使用方法：

```python
from flask_script import Manager
manager = Manager(app)
# flask程序入口改为以下语句
manager.run()
```

`python hello.py runserver --help` - 查看runserver支持的参数和意义

`python hello.py runserver -h 0.0.0.0 -p 5001 -d` - -h为指定能访问的IP地址，-p为指定端口，-d为开启debug模式， --threaded为开启多线程模式

## 7. jinja2模板

Flask 默认在程序相同文件夹中的templates子文件夹中找模板

渲染模板使用`render-template`，使用前先导入`from flask import render_template`

```python
@app.route('/')
def index():
    return render_template('index.html')
```

给模板传递变量，直接在render_template中写变量名=变量值：

```python
@app.route('/usevar/<name>')
def usevar(name):
    result_list = ['苹果', '梨', '西瓜']
    result_dict = { '姓名': '吴东', '生日': '1999-10-21' }
    return render_template('usevar.html', name=name, result_list=result_list, result_dict=result_dict)
```

模板过滤器语法：

{{ 变量|过滤器|过滤器… }}
capitalize 单词首字母大写
lower 单词变为小写
upper 单词变为大写
title 每个单词首字母大写
trim 去掉字符串的前后的空格
reverse 单词反转
striptags 渲染之前，将值中标签去掉
safe 讲样式渲染到页面中
last 最后一个字母

模板控制语句

```python
{% if result_list %}
{% else %}
{% endif %}

{% for item in result_list %}
{% endfor %}
```

定义宏，类似定义函数，定义一处，多出调用

```python
{% macro f(content) %}
    <span style="color:blue;">{{ content }}</span>
{% endmacro %}

<div>{{ f('蓝色的') }}</div>
```

模板继承

挖坑语句：`{% block title %}{% endblock %}`

继承语句：`{% extends "base.html" %}`

继承父坑语句：`{{ super() }}`

## 8. 获取散列密码

使用前需要先导入包`from werkzeug.security import generate_password_hash, check_password_hash`

`generate_password_hash(password, method=pbkdf2:sha256, salt_length=8)`

说明：这个函数将 原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中。

method 和salt_length 的默认值就能满足大多数需求。

`check_password_hash(hash, password)`

说明：这个函数的参数是从数据库中取回的密码散列 值和用户输入的密码。返回值为True 表明密码正确

## 9. SQLAlchemy

使用前安装包
```
pip install flask-sqlalchemy
pip install pymysql
```

连接数据库方法
```
实例化flask对象名.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@server/db'
```

定义入口文件`manager.py`：

```python
from application import manager

def main():
    manager.run()
    # app.run(debug=True, host='0.0.0.0', port=5001)

if __name__ == '__main__':
    main()
```

定义应用包初始化类`__init__`：

```python
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置数据库连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:stolen@121.199.42.247/irest?charset=UTF8MB4'
# 不跟踪修改，不设置会有警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库连接
db = SQLAlchemy(app)

import application.models
import application.views

manager = Manager(app)
```

定义模型的方法：

```python
from application import db
import datetime

# 用户表
class Users(db.Model):
    __tablename__ = 'users'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户名 唯一索引
    username = db.Column(db.String(128), unique=True, nullable=False)
    # 密码 必填字段
    password = db.Column(db.String(512), nullable=False)
    # 姓名 创建索引，加快查询
    fullname = db.Column(db.String(128), index=True, nullable=False)
    # 状态 (1: 生效 0: 禁用)
    status = db.Column(db.SmallInteger, default=1, nullable=False)
    # 创建时间 默认当前时间
    created_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, index=True)

    def __repr__(self):
        return 'username=%s' % username   
```

### 通过模型操作数据库

通过model创建表：

```shell
$ python manage.py shell
>>> from application import db
>>> db.drop_all()
>>> db.create_all()
```

插入数据：

```shell
$ python manage.py shell
>>> user = Users(username='lisa', password='asdasdfad', fullname='李霞')
>>> db.session.add(user) # 添加到数据库会话中
>>> db.session.commit() # 提交数据
>>> db.session.rollback() # 数据库回滚
```

查询数据：

```bash
>>> Users.query.all()  # 查询全部
>>> Users.query.filter_by(username='lisa') # 返回一个新查询
>>> Users.query.filter_by(username='lisa').all() # 返回查询结果
>>> Users.query.filter(Users.username=='lisa').first_or_404()
>>> str(Users.query.filter(Users.username=='lisa3')) # 查看sql语句
>>> db.session.execute('select * from users where id = 1').first() # 原生sql语句
```

filter和filter_by的区别：

1.  filter需要通过类名.属性名的方式，类名.属性名==值。filter_by 直接使用属性名=值 
2.   filter支持> <等关系运算符，filter_by不支持 
3.   filter不直接支持组合查询，只能连续调用filter来实现，但是可以通过or_ ,and_来实现；而filter的参数是**kwargs，直接支持组合查询 

修改数据：

```python
user = Users.query.get(1)  # 获取主键为1的数据
user.password = '123412343'
db.session.add(user)
db.session.commit()
```

删除数据：

```python
db.session.delete(user)
db.session.commit()
```

### 数据库对应关系

一对多创建

```python
# 学生表
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    # 建立指向班级的外键
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))

    def __repr__(self):
        return 'student=%s' % self.name  

# 班级表
class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    # 引用学生
    students = db.relationship('Student', backref='sclass')
```

一对多关系测试：

```pyrhon
>>> from application import db
>>> db.create_all()
>>> from application.models import *
>>> student1 = Student(name='lisa')
>>> db.session.add(student1)
>>> db.session.commit()
>>> c1 = Class(name='python1904')
>>> db.session.add(c1)
>>> db.session.commit()
>>> student1.sclass = c1
```

一对一关系：

```python
student = db.relationship('Student', backref='sclass', uselist=False)
```

说明：一对一关系可以用前面介绍的一对多关系 表示，但调用db.relationship() 时要把uselist设为False 

多对多关系建模

```python
class StudentLesson(db.Model):
    __tablename__ = 'student_lesson'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
    score = db.Column(db.Integer, nullable=True)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    lessons = db.relationship('StudentLesson', foreign_keys=[StudentLesson.student_id], backref=db.backref('student', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return 'student=%s' % self.name    

class Lesson(db.Model):
    __tablename__ = 'lesson'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    students = db.relationship('StudentLesson', foreign_keys=[StudentLesson.lesson_id], backref=db.backref('lesson', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return 'lesson=%s' % self.name    
```

多对多关系测试：

```bash
>>> from application.models import *
>>> from application import db
>>> db.create_all()
>>> student1 = Student(name='carmack')
>>> student2 = Student(name='lisa')
>>> db.session.add_all([student1, student2])
>>> db.session.commit()
>>> lesson1 = Lesson(name='数学')
>>> lesson2 = Lesson(name='语文')
>>> db.session.add_all([lesson1, lesson2])
>>> db.session.commit()
>>> student_lesson = StudentLesson(student=student1, lesson=lesson1)
>>> db.session.add(student_lesson)
>>> db.session.commit()
```

常用的SQLAlchemy关系选项 

* backref 
    在关系的另一个模型中添加反向引用
* primaryjoin 
    明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
* lazy 
    指定如何加载相关记录。可选值有 select(首次访问时按需加载)、immediate(源对象加 载后就加载)、joined(加载记录，但使用联结)、subquery(立即加载，但使用子查询)， noload(永不加载)和 dynamic(不加载记录，但提供加载记录的查询) 
* uselist
    设为False，不使用列表

## 10. 使用Flask-Migrate实现数据库迁移

使用前先安装：`pip install flask-migrate`

使用前需要先配置`/应用下/__init__`：

```python
from flask_migrate import Migrate, MigrateCommand

#绑定app和数据库
migrate = Migrate(app, db)

# 传输命令行参数用
manager = Manager(app)
manager.add_command('db', MigrateCommand)
```

命令行指令说明：

python manage.py db init 初始化出migrations的文件，只调用一次

python manage.py db migrate -m ‘comment’ 生成迁移文件

python manage.py db upgrade 执行迁移文件中的升级

python manage.py db downgrade 执行迁移文件中的降级

python manage.py db —help 帮助文档

## 11. blueprint蓝图

使用前安装`pip install flask-blueprint`

蓝图是将flask程序进行模块化的一种方式，类似django中的应用，程序结构变为

> application
>
>   > users模块
>   >	> login
>   >	> register
>	>
>   > report模块

区分url通过注册蓝图进行

模块内的views.py文件为功能实现：

```
# 模块内 views.py文件
from flask import Blueprint
users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    return '注册页面'
```

application文件下的`__init__.py`文件

```
# application/__init__.py

# 放在db = SQLAlchemy(app)这条语句后面
from application.users.views import users

# 注册蓝图， url_prefix表示进入该路径的路径前缀
app.register_blueprint(users, url_prefix='/users')
```

## 12. flask-wtf表单验证

使用前先安装`pip install flask-wtf`

使用前导入

```python
from flask_wtf import FlaskForm
# 导入验证字段
from wtforms import StringField, SubmitField, ValidationError
# 导入表单验证
from wtforms.validators import DataRequired, EqualTo
# 导入模型
from user.models import User
```

表单验证：

```python
class UserForm(FlaskForm):
    """
    登录注册表单验证
    """
    username = StringField('用户名', validators=[DataRequired()])
    username = StringField('用户名', validators=[DataRequired(), length(max=6, min=3, message='密码长度不正确')])
    password = StringField('密码', validators=[DataRequired()])
    password2 = StringField('确认密码', validators=[DataRequired(),
                                                EqualTo('password', '密码不一致')]
                            )
    submit = SubmitField('提交')

    def validate_username(self, field):
        # 验证用户名是否重复
        if User.query.filter(User.username == field.data).first():
            raise ValidationError('用户名已存在')

        # 对用户名的长度进行判断
        if len(field.data) < 3:
            raise ValidationError('用户名长度不能少于3个字符')

        if len(field.data) > 6:
            raise ValidationError('用户名长度不能大于6个字符')
```

说明：validators中元素可以在括号内指定message代表验证失败的返回内容，DataRequired表示不能为空，验证字段的方法为`validate_字段名`

用form表单生成html内容

`view.py`中：

```python
def login():
    form = LoginForm()
    # 使用表单验证是否通过
    if form.validate_on_submit():
        # 从表单中取数据
        username = form.username.data
    # 将验证表单的内容传递给页面
    return render_template('users/login.html', form=form)
```

模板语法：

1.定义字段名：{{ form.字段.label }}

2.定义input输入框：{{ form.字段 }}

3.展示错误信息：{{ form.errors.字段 }}

4.跨站请求伪造：{{ form.csrf_token }}

5.跨站身份伪造：{{ form.hidden_tag() }}

解析的模板如果需要自定义样式：{{ form.字段(class='xxx'， style='color:red') }}

常见字段类型：

```
字段类型	说明
StringField	普通文本字段
PasswordField	密码文本字段
SubmitField	提交按钮
HiddenField	隐藏文本字段
TextAreaField	多行文本字段
DateField	文本字段，datetime.date格式
DateTimeField	文本字段，datetime.datetime格式
IntegerField	文本字段，整数类型
FloatField	文本字段，小数类型
BooleanField	复选框，值为True或False
RadioField	单选框
SelectField	下拉列表
FileField	文件上传字段
```

`SelectField('方法选择',coerce=int, choices=['北京', '上海', '成都'])`

>   coerce=int - 将option转为整型
>
>   choices=[] - 设置下拉框的内容，如果需要动态获取，需要在次类中写如下内容，表示从数据库中动态获取内容

```python
def __init__(self, *args, **kwargs):
        super(SelectClassForm, self).__init__(*args, **kwargs)
        result_list = [ (item.id, item.name) for item in Class.query.order_by(Class.name).all() ]
        self.select_class.choices = result_list
```

常用验证器

```python
验证器	说明
DataRequired	确保字段有值(并且if判断为真)
Email	邮箱地址
IPAddress	IPv4的IP地址
Length	规定字符长度
NumberRange	输入数值的范围
EqualTo	验证两个字段的一致性
URL	有效的URL
Regexp	正则验证
```

## 13. 使用flask-login认证用户

使用前先安装`pip install flask-login`

要使用flask-login认证方法，需要先实现四个方法：

`is_authenticated()` - 如果用户已经登录，必须返回True，否则返回False 
`is_active()` - 如果允许用户登录，必须返回 True，否则返回 False。如果要禁用账户，可以返回 False 
`is_anonymous()` - 对普通用户必须返回 False
`get_id()` - 必须返回用户的唯一标识符，使用 Unicode 编码字符串 

flask-login中有个UserMixin类提供了以上方法，要使用只需要在定义表单验证的时候继承UserMixin类即可：

```python
from flask_login import UserMixin
from application import db
import datetime

# 用户表，包含自动验证类
class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户名 唯一索引
    username = db.Column(db.String(128), unique=True, nullable=False)
```

在application的`__init__.py`中配置验证规则：

```python
from flask_login import LoginManager

# 初始化LoginManager
login_manager = LoginManager()
# 设为 'strong' 时，Flask-Login 会记录客户端 IP 地址和浏览器的用户代理信息，如果发现异动就登出用户
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面
login_manager.login_view = 'users.login'

login_manager.init_app(app)
```

在models中设置回调函数，说明查询那张表的用户：

```python
# flask-login获取用户的回调函数，会在login成功后自动执行
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
```

使用认证：

```python
from flask_login import login_required 
@app.route(‘/secret’)
@login_required
def secret():
 return '只有登录以看'
```

## 14. 分页

获取需要进行分页的信息：

```python
pagination = Users.query.order_by(Users.id.desc()).paginate(page, per_page=current_app.config['COUNT_PER_PAGE'], error_out=False)
```

`pagination.items` - 获取当前页码的所有数据

`pagination.has_prev` - 判断是否有前一页

`pagination.has_next` - 判断是否有下一页

`pagination.page` - 获取当前页码

`pagination.pages` - 获取总共的页数

`pagination.total` - 获取总共数据条数

## 15. 测试

为方便测试时使用不同的配置，如数据库，CSRF验证等。需要使用工厂模式创建原对象。

1.创建`settings.py`文件，存放相关配置：

```
SECRET_KEY = 'q234asdfad@#$AdfS*UNFs'
# 设置数据库连接字符串
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vff123456@127.0.0.1/mouse?charset=UTF8MB4'
# 不跟踪修改，不设置会有警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 每页条数
COUNT_PER_PAGE = 10

DEBUG = True
TESTING = True
WTF_CSRF_ENABLED = False
```

2.修改`application/__init__.py`文件，加入create_app方法

```python
#application/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 初始化LoginManager
login_manager = LoginManager()
# 设为 'strong' 时，Flask-Login 会记录客户端 IP 地址和浏览器的用户代理信息，如果发现异动就登出用户
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面
login_manager.login_view = 'users.login'
# 定制未授权访问提示信息
login_manager.login_message = '访问该功能需要登录'

# 创建数据库连接
db = SQLAlchemy()

def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    from application.home.views import home
    from application.users.views import users

    # 注册蓝图
    app.register_blueprint(home, url_prefix='')
    app.register_blueprint(users, url_prefix='/users')

    db.init_app(app)
    login_manager.init_app(app)

    return app
```

3.修改manager.py文件

```python
from application import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

if __name__ == '__main__':
    app = create_app('settings')

    manager = Manager(app)
    # 数据库迁移相关
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)

    manager.run()
```

**创建pytest全局文件conftest.py，和manager.py在同一级目录下**

>1.conftest.py文件名字是固定的，不可以做任何修改
>2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录
>3.conftest.py文件不能被其他文件导入
>4.所有同目录测试文件运行前都会执行conftest.py文件

内容为：

```python
# /school/conftest.py

import pytest
from application import create_app, db

@pytest.fixture
def app():
    app = create_app('test_settings')
    return app
```

所有的测试文件放在tests目录下并且需要以`test_`开头才会被自动执行

测试模块：

```
import flask

def test_app(app):
    assert isinstance(app, flask.Flask)
```

测试的相关配置文件

```
# conftest.py

# session表示该fixture作用于整个测试过程，只创建一次
@pytest.fixture(scope='session')
def db(app, request):
    database.app = app
    database.create_all()

    def teardown():
        database.drop_all()

    request.addfinalizer(teardown)
    return database

# function表示该fixture会在每个测试方法都执行
@pytest.fixture(scope='function')
def session(db, request):

    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session
```

测试模型：

```python
from application.users.models import Users, Class

def test_create_user(session):
    username = 'carmack'
    fullname = '肖世荣'
    password = 'ASDFAD@#23232'

    user = Users(username=username, fullname=fullname, password=password)
    session.add(user)
    session.commit()

    assert user.id is not None
    assert Users.query.count() == 1
    assert user.status == 1
    assert user.vote_type == 'go'
    assert user.get_vote_button() == 'stop'
    assert user.get_vote_color() == 'green' 
    
# 测试user和class关联关系
def test_user_class_relation(session):
   user1 = Users(username='jungle', fullname='林林', password='23434213sSWE')
   user2 = Users(username='ken', fullname='郑冠', password='2343asSWE')
   c1 = Class(name='python1904')
   c2 = Class(name='python1905')
   user1.uclass = c1
   user2.uclass = c1
   assert len(c1.users) == 2
   assert c1.users[0].username == 'jungle'

   session.add_all([user1, user2, c1, c2])
   session.commit()

   c1_obj = Class.query.filter_by(name='python1904').first()
   assert c1_obj is not None
   assert len(c1_obj.users) == 2
```

测试视图：

```python
from application.users.models import Users
from flask import get_flashed_messages
from werkzeug.security import check_password_hash
import pytest
import sqlalchemy

# 测试成功的注册
# client 是Werkzeug自带的测试客户端
def test_valid_register(client):
    # 测试get请求下register页面是否正确
    response = client.get('/users/register')
    assert response.status_code == 200
    assert '欢迎注册' in bytes.decode(response.data)

    # 测试post请求
    data = {'username': 'morning', 'fullname': '黎明', 'password': '123456'}
    response = client.post('/users/register', data=data)

    assert response.status_code == 302
    assert len(get_flashed_messages()) == 1
    assert '注册成功' in  get_flashed_messages()[0] 

    user = Users.query.filter_by(username=data['username']).one()
    assert user.fullname == data['fullname']
    assert user.password

    assert check_password_hash(user.password, data['password'])

# 注册失败的条件更需要测试
# 测试不满足条件的注册
def test_invalid_register(client):
    response = client.get('/users/register')

    data = {'username': '    ', 'fullname': '黎明' * 200, 'password': '123456'}
    response = client.post('/users/register', data=data)

    assert response.status_code == 200
    assert '用户名必填' in bytes.decode(response.data)
    assert '姓名不能大于128位' in bytes.decode(response.data)

    # 测试抛异常情况
    with pytest.raises(sqlalchemy.orm.exc.NoResultFound):
        Users.query.filter_by(username=data['username']).one()
```

## 16. rest接口开发

**安装flask-marshmallow，映射models到json输出**

```
pip install flask-marshmallow
pip install marshmallow-sqlalchemy
```

**创建一个序列化和反序列化的类(模型)**

```python
from datetime import datetime

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
```

**创建一个模型和json相互转换的类**

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta(ModelSchema.Meta):
    	model = User
    	# db为数据库配置 
    	sqla_session = db.session
    
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
```

**序列化**

```python
from marshmallow import pprint

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
print(result.data)
# {"name": "Monty",
#  "email": "monty@python.org",
#  "created_at": "2014-08-17T14:54:16.049594+00:00"}
```

说明：dump是实现`obj->dict`，dumps是实现`obj->string`，但是flask中jsonify可以直接将dic序列化为json，所以一般使用dump

**过滤输出**

```python
summary_schema = UserSchema(only=('name', 'email'))
summary_schema.dump(user).data
# {"name": "Monty Python", "email": "monty@python.org"}

summary_schema = UserSchema(exclude=('created_at', ))
summary_schema.dump(user).data
# {"name": "Monty Python", "email": "monty@python.org"}
```

说明：用only来选择显示哪些字段，或者使用exclude来排除不显示的字段

**反序列化**

```python
from pprint import pprint

user_data = {
    'created_at': '2014-08-11T05:26:03.869245',
    'email': u'ken@yahoo.com',
    'name': u'Ken'
}
schema = UserSchema()
result = schema.load(user_data)
pprint(result.data)
# {'name': 'Ken',
#  'email': 'ken@yahoo.com',
#  'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},
```

说明：load方法主要是实现`dict->obj`，在marshmallow中，`dict->obj`方法需要自己实现，主要方法就是在类的方法前面加一个装饰器：

```python
from marshmallow import Schema, fields, post_load

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)
```

 这样每次调用`load()`方法时，会按照`make_user`的逻辑，返回一个`User`类对象：

```python
user_data = {
    'name': 'Ronnie',
    'email': 'ronnie@stones.com'
}
schema = UserSchema()
result = schema.load(user_data)
result.data  # => <User(name='Ronnie')>
```

说明：相对于dumps，也有loads的存在，主要作用是`str->obj`

**objects->list**

当有多个对象时，转换的结果应该是个列表，每个元素为一个对象，转换方法为在对象实例化括号中写入`many=True`：

```python
user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]

# option 1:
schema = UserSchema(many=True)
result = schema.dump(users)

# Option 2:
schema = UserSchema()
result = schema.dump(users, many=True)
result.data

# [{'name': u'Mick',
#   'email': u'mick@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}
#  {'name': u'Keith',
#   'email': u'keith@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}]
```

**定义校验方法和返回值**：

在定义schema的时候，在字段中加入校验内容和错误提示信息，当校验不通过的时候，就会将错误信息返回

```python
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Email()

data, errors = UserSchema().load({'email': 'foo@bar.com'})
errors
# {'name': ['Missing data for required field.'],
#  'age': ['Age is required.'],
#  'city': {'message': 'City required', 'code': 400}}
```

>strict Mode：如果将strict=True传入Schema构造器或者class的Meta参数里，则仅会在传入无效数据是报错。
>
>Required Fields：在field中传入required=True.当Schema.load()的输入缺少某个字段时错误会记录
>
>Partial Loading：实现Partial Loadig只要在schema构造器中增加一个partial参数即可，使用该方法可以跳过数据校验。

```python
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

data, errors = UserSchema().load({'age': 42}, partial=('name',))
# OR UserSchema(partial=('name',)).load({'age': 42})
data, errors  # => ({'age': 42}, {})
```

**只校验数据，不创建对象**

```python
errors = UserSchema().validate({'name': 'Ronnie', 'email': 'invalid-email'})
errors  # {'email': ['"invalid-email" is not a valid email address.']}
```

**使用attribute自定义对应模型的字段**

```python
class UserSchema(Schema):
    name = fields.String()
    email_addr = fields.String(attribute="email")
    date_created = fields.DateTime(attribute="created_at")

user = User('Keith', email='keith@stones.com')
ser = UserSchema()
result, errors = ser.dump(user)
pprint(result)
# {'name': 'Keith',
#  'email_addr': 'keith@stones.com',
#  'date_created': '2014-08-17T14:58:57.600623+00:00'}
```

**自定义序列化传入字典和输出字典的字段名**

```python
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(load_from='emailAddress')

data = {
    'name': 'Mike',
    'emailAddress': 'foo@bar.com'
}
s = UserSchema()
result, errors = s.load(data)
#{'name': u'Mike',
# 'email': 'foo@bar.com'}  
```

**自定义fields名称，和load_from作用类似**

```python
class UserSchema(Schema):
    name = fields.String(dump_to='TheName')
    email = fields.Email(load_from='CamelCasedEmail', dump_to='CamelCasedEmail')

data = {
    'name': 'Mike',
    'email': 'foo@bar.com'
}
s = UserSchema()
result, errors = s.dump(data)
#{'TheName': u'Mike',
# 'CamelCasedEmail': 'foo@bar.com'}
```

**设定字段只能读和只能写**

```python
class UserSchema(Schema):
    name = fields.Str()
    # password is "write-only"
    password = fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)
```

**外键关联处理**

模型定义：

```python
# Use a Nested field to represent the relationship, passing in a nested schema class.
import datetime as dt

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None

class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author  # A User object
```

Schame关联：

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()

class BlogSchema(Schema):
    title = fields.String()
    # 如果集合有多个，则需要在下面括号中定义many=True 
    author = fields.Nested(UserSchema)
```

序列化blog：

```python
user = User(name="Monty", email="monty@python.org")
blog = Blog(title="Something Completely Different", author=user)
result, errors = BlogSchema().dump(blog)
pprint(result)
# {'title': u'Something Completely Different',
# {'author': {'name': u'Monty',
#             'email': u'monty@python.org',
#             'created_at': '2014-08-17T14:58:57.600623+00:00'}}
```

**自定义错误捕捉**：

当请求数据遇到错误的时候，如果该错误类型被捕捉到，就会返回相应的自定义json数据

```python
from flask import Blueprint, flash, jsonify
from marshmallow.exceptions import ValidationError
from application.common.status_code import *


error = Blueprint('error', __name__)

# 捕获验证错误
@error.app_errorhandler(ValidationError)
def valid_valid_error(e):
    return jsonify({'code':ERROR_PARAM, 'message':e.messages})
```

**访问验证**

安装包：

```
pip install flask-jwt-extended
```

配置：

```python
# application/__init__.py
from flask_jwt_extended import JWTManager
...

jwt = JWTManager()

jwt.init_app(app)
```

定义登录功能函数：

```python
# REST /users/login POST 用户登录
@users_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Users.query.filter_by(username=data['username']).first()
    
    if user and check_password_hash(user.password, data['password']):
        # 登录成功生成token令牌
        access_token = create_access_token(identity=data['username'])
        return jsonify({'status_code': 200, 'status_message': '登录成功', 'access_toten': access_token}) 
```

需要登录才能访问的视图函数前加`@jwt_required`装饰器。

前端请求需要在请求头中加入一下内容来验证令牌

```
Authorization=Bearer <jwt—token值>
```

**jwt重刷**

设置请求token过期时间（单位：秒）

```python
JWT_ACCESS_TOKEN_EXPIRES = 60
```

设置jwt refresh token 过期时间（单位：秒）

```python
JWT_REFRESH_TOKEN_EXPIRES = 2592000
```

定义一个用重刷的token生成请求token的视图函数

```python
@api_users.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    result = {
        'code':SUCCESS, 'message':'成功',
        'access_token': create_access_token(identity=current_user, fresh=False),
        'refresh_token': create_refresh_token(identity=username)
    }
    return jsonify(result)
```

**新鲜的token和不新鲜的token权限问题**

在生成token的时候，在括号后面添加fresh参数，True表示新鲜，False表示不新鲜

```python
create_access_token(identity=current_user, fresh=False)
```

设置新鲜的token才能访问的视图函数，将装饰器改为`@fresh_jwt_required`

## 17. 文件上传

在模型中添加图片字段

```python
# application_users_models.py
# 用户头像 
avatar = db.Column(db.String(128), nullable=True)
```

在Schema中加入头像字段

```python
# application_users_schemas.py
avatar = fields.String(dump_only=True)
```

属性说明：

>文件对象.filename - 获取文件的名字
>
>文件对象.content_type - 获取文件的类型，如（image/jpeg）
>
>send_from_directory(filepath, filename) - 返回文件。
>
>request.files['form表单文件控件的name值'] - 从前端请求中取出文件对象
>
>文件对象.save(本地路径) - 将收到的文件保存

# 五. scrapy

## 1. urllib.request

urllib为自带库，不需要安装，使用前先导入：`import urllib.request`

**请求**

```
纯网页请求语法：
response = urllib.request.urlopen('http://www.baidu.com', timeout=1, data=data)
```

说明：

>   data和timeout可以缺省
>
>   设置超时时间为1秒
>
>   请求数据为data，有此参数表示为post请求，没有表示为get请求

```
构建请求体请求语法：
req = urllib.request.Request(url=url, data=data, headers=headers, method="GET")
response = urllib.request.urlopen(req)
```

说明：

>   data为二进制数据，传入前需要先对数据进行编码
>
>   带请求头和请求参数的请求，data为请求参数，headers为请求头，method为请求方式

```
设置代理请求语法：
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy_handler)
request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
text = response.read().decode('utf-8')
```

说明：

>   设置代理需要重新构建一个请求对象，用新构建的请求对象来请求网页。proxies为代理ip

```
忽略未经审核的ssl认证语法：
import ssl
url = 'https://www.12306.cn/mormhweb/'
context = ssl._create_unverified_context()
res = urllib.request.urlopen(url, context=context)
```

说明：

>   ssl需要导入，在请求体中加入context来忽略ssl认证问题

**响应**

```
response.status - 响应状态码
response.getheaders() - 获取响应头信息
response.getheaders('Server') - 获取指定参数的响应头信息
response.read() - 获取响应体，为二进制数据，需要解码
```

## 2. requests

安装库：`pip install requests`

使用前先导入：`import requests`

**请求**

```
response = requests.get('https://api.github.com/events', headers=headers)
response = requests.post('http://httpbin.org/post', data = {'key':'value'}, headers=headers, files=files)
response = requests.put('http://httpbin.org/put', data = {'key':'value'}, headers=headers)
response = requests.delete('http://httpbin.org/delete', headers=headers)
response = requests.head('http://httpbin.org/get', headers=headers)
response = requests.options('http://httpbin.org/get', headers=headers)
```

说明：

>   requests允许使用params传递参数，传递的参数会以get参数的形式拼接在url后面
>
>   参数中value为None的键值对不会拼接
>
>   post可以打开文件进行上传，files = {'file': open('filename', 'rb')}
>
>   timeout=0.001可以设置超时

**响应**

```
response.text - 获取响应体，一般会自动进行解码
response.encoding - 获取编码方式
response.content - 获取响应体，返回二进制文件，如果是文本文件需要自己进行解码
response.json() - 获取json数据
response.status_code - 获取响应状态码 //requests.codes.ok来判断响应是否成功
response.headers - 以字典形式展示响应头
response.cookies['keys'] - 获取指定的cookies值

```

**错误与异常**

遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

若请求超时，则抛出一个 Timeout 异常。

若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。

## 3. 文档解析

**xpath**

```
nodename - 选取此节点的所欲子节点
/ - 从根节点选取
// - 从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置
. - 选取当前节点
.. - 选取当前节点的父节点
@ - 选取属性
text() - 获取文本内容
```

xpath一般应用：

```
from lxml import etree
from requests
html = requests.get('www.baidu.com').content.decode('utf-8')
etree_html = etree.HTML(html)
a = html.xpath('/html')
a1 = html.xpath('//ul')
# 选择属性,获取ul下的li的类定义为class1的信息
a2 = html.xpath('//ul/li[@class="class1"]')
# 获取ul节点下的第一个元素
a3= html.xpath('//ul/li[1]')
```

**beautiful soup4**

安装库：`pip install beautifulsoup4`

使用前导入：`from bs4 import BeautifulSoup`

解释器类型：

```
Python 标准库 BeautifulSoup(html, “html.parser”) 速度⼀般，容错能⼒好
lxml HTML解析器 BeautifulSoup(html, “lxml”) 速度快，容错好
lxml xml解析器 BeautifulSoup(markup, “xml”) 速度快，唯⼀⽀持xml
html5lib BeautifulSoup(markup, “html5lib”) 容错性⾼，速度慢
```

一般使用lxml

```
soup = BeautifulSoup(html, 'lxml')
```

**标准选择器**

find_all( name , attrs , recursive , text , **kwargs )

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

```
查询所有a标签的内容
soup.find_all('a')

查询所有a标签下class样式为bb的内容
soup.find_all('a', 'bb')

查询所有id样式为cc的内容
soup.find_all(id='cc')
```

**关联选择**

```
print(soup.p.contents) # 取p节点下⾯所有⼦节点列表
print(soup.p.descendants) #取p节点所有⼦孙节点
print(soup.a.parent) # 取⽗节点
print(soup.a.parents) # 取所有祖先节点
print(soup.a.next_sibling) # 同级下⼀节点
print(soup.a.previous_sibling) # 同级上⼀节点
print(soup.a.next_siblings) # 同级所有后⾯节点
print(soup.a.previous_siblings) # 同级所有前⾯节点
print(list(soup.a.parents)[0].attrs['class'])
```

**标签选择器**

```
# 取⽹⻚缩进格式化输出
print(soup.prettify())

# head标签里面title的文字内容
print(soup.title)
print(soup.title.string)
print(soup.head.title.string)

# 取整个head标签的内容
print(soup.head)
print(type(soup.head))

# 获取第一个p标签的内容	
print(soup.p)
# 获取第一个p标签的名称
print(soup.p.name)
# 获取第一个p标签下的第一个a标签的标签名称
print(soup.p.a.name)
# 获取第一个p标签中的内容
print(soup.p.contents)

# 获取第一个img标签的所有属性	
print(soup.img.attrs)
# 获取第一个img标签属性中的src属性
print(soup.img.attrs["src"])
print(soup.img['src'])
```

**类/css选择器**

```
# 获取class="news-list-b"标签中class="list"的标签下的class="item"下的p标签中的a标签内容
result = soup.select('.news-list-b .list .item p a')
for item in result:
	print(item.string)

# 获取class中定义的两个样式参数
result = soup.select('.-live-layout-row.layout_sports_350_650')
print(result)

# 获取class="title"的标签下的a标签内容
l = soup.select('.ct_t_01 a')
for item in l:
	print(item.string)
 	print(item['href'])
print(len(l))

# 获取属性
print(soup.select('#list-2 h1')[0].attrs)

# 获取内容
print(soup.select('#list-2 h1')[0].get_text())
```

## 4. selenium

安装库：`pip install selenium`

使用前导入：`from selenium import webdriver`

```
browser = webdriver.Firefox()
browser = webdriver.Ie()
browser = webdriver.Opera()
browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
```

**注意：在调用以上函数时需要要先安装浏览器驱动，windows需要将驱动放在python安装目录的Script下，linux需要配置浏览器驱动所在的环境变量**

**网页信息**

```
# 访问一个网址
browser.get('https://www.mogu.com')
# 显示网页内容
print(browser.page_source)
# 获取当前网址
print(browser.current_url)
```

**获取单个元素**

```
find_element_by_name() - 是根据Name值获取
find_element_by_id() - 是根据ID获取
find_element_by_xpath() - 是根据Xpath提取
find_element_by_css_selector('#xxx') - 是根据id=xxx来获取
```

```
from selenium.webdriver.common.by import By

find_element_by_id(id) - 等价于find_element(By.ID, id)

find_element_by_css_selector('#xxx') - 等价于find_elements(By.CSS_SELECTOR, '.service-bd li')

find_element() - 它需要传入两个参数，一个是查找的方式By，另一个就是值，实际上它就是find_element_by_id()这种方法的通用函数版本。
```

**获取多个元素**

```
find_elements_by_css_selector('#xxx li') - 是根据id=xxx来获取下面的所有li的结果
```

**隐式等待**

```
browser.implicitly_wait(10) - 查找元素未出现时先等待一会儿
```

**显式等待**

```
from selenium.webdriver.support import expected_conditions as EC
input = wait.until(EC.presence_of_element_located((By.ID, 'q'))) - 表名某个条件成立时才向下执行
```

**页面状态函数**

```
title_is - 标题是某内容
title_contains - 标题包含某内容
presence_of_element_located - 元素加载出，传入定位元组，如(By.ID, 'p')
visibility_of_element_located - 元素可见，传入定位元组
visibility_of - 可见，传入元素对象
presence_of_all_elements_located - 所有元素加载出
text_to_be_present_in_element - 某个元素文本包含某文字
text_to_be_present_in_element_value - 某个元素值包含某文字
frame_to_be_available_and_switch_to_it - frame加载并切换
invisibility_of_element_located - 元素不可见
element_to_be_clickable - 元素可点击
staleness_of - 判断一个元素是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected - 元素可选择，传元素对象
element_located_to_be_selected - 元素可选择，传入定位元组
element_selection_state_to_be - 传入元素对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be - 传入定位元组以及状态，相等返回True，否则返回False
alert_is_present - 是否出现Alert
```

**前进后退**

```
browser.back() - 后退
browser.forward() - 前进
```

**操作cookies**

```
from selenium import webdriver

chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.zhihu.com/explore')

# 获取所有cookies信息
print(browser.get_cookies())

# 添加一个Cookie信息
browser.add_cookie({'name': '王大帅', 'value': '16'})
print(browser.get_cookies())
# 删除所有的Cookies
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()
```

**切换窗口**

```
import time

from selenium import webdriver

chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
browser = webdriver.Chrome(chromedriver)

# 隐式延迟
browser.implicitly_wait(20)

browser.get('https://www.taobao.com')

# 获取主窗口
taobao_handler = browser.current_window_handle

# 点击导航栏女装按钮
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/ul/li[1]/a[1]').click()

time.sleep(3)

# 获取当前窗口
text_browser_handler_nv = browser.current_window_handle

# 切换窗口继续点击男装案例
browser.switch_to_window(taobao_handler)

# # 点击导航栏男装按钮
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/ul/li[1]/a[2]').click()

time.sleep(3)

# 后退
browser.back()

time.sleep(3)
# 前进
browser.forward()

# 关闭浏览器
browser.quit()
```

**ActionChains方法**

```
click(on_element=None) ——单击鼠标左键
click_and_hold(on_element=None) ——点击鼠标左键，不松开
context_click(on_element=None) ——点击鼠标右键
double_click(on_element=None) ——双击鼠标左键
drag_and_drop(source, target) ——拖拽到某个元素然后松开
drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
key_down(value, element=None) ——按下某个键盘上的键
key_up(value, element=None) ——松开某个键
move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
move_to_element(to_element) ——鼠标移动到某个元素
move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上⾓坐
标）多少距离的位置
perform() ——执⾏链中的所有动作
release(on_element=None) ——在某个元素位置松开鼠标左键
send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
```

## 5. scrapy框架简介

![scrapy框架结构](./img/spider_scrapy.png)

![scrapy架构](./img/scrapy_jiagou.png)

安装库`pip install Scrapy`

使用前导入`import scrapy`

```
常用命令
 Scrapy shell - 进入scrapy终端
 scrapy startproject projectName - 创建scrapy项目
 scrapy genspider 爬虫名 爬取网站地址 - 创建爬虫
 scrapy crawl 爬虫名
```

**文件解释**

```
scrapy.cfg - 项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
items.py - 设置数据存储模板，用于结构化数据，如：Django的Model
pipelines - 数据处理行为，如：一般结构化的数据持久化
settings.py - 配置文件，如：递归的层数、并发数，延迟下载等
spiders - 爬虫目录，如：创建文件，编写爬虫规则。
```

**spider程序**

爬虫名.py

```
import scrapy
from scrapy.selector import Selector

class QiDianSpider(scrapy.spiders.Spider):
    name = "qidian"
    start_urls = [
        "https://www.qidian.com/",
    ]
	
	# 有post请求则从此入口进入
	def start_requests(self):
		url = 'http://www.u17.com/'
        self.links_set.add(url)
        yield scrapy.Request(url=url, method='GET', headers=self.headers, callback=self.parse, dont_filter=False, meta={'deep': 1})
	
	# 获取第一个请求返回的内容
    def parse(self, response):
        # 爬取时请求的url
        current_url = response.url

        # 返回的html
        body = response.body

        # 返回的html unicode编码
        unicode_body = response.body_as_unicode()
        res = Selector(response)

        print(xiaoshuo_type, xiaoshuo_href)
        # 如需返回，使用yield
```

item.py

```
class WebsiteItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
```

pipelines.py

```
# mysql存储管道
class U175MysqlPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, U175Item):
            sql = 'insert into comic(comic_id, title, cover) values(%s, %s, %s)'
            self.cursor.execute(sql, (item['comic_id'], item['title'], item['cover']))
        else:
            sql = 'insert into comic_detail(comic_id, title, link) values(%s, %s, %s)'
            self.cursor.execute(sql, (item['comic_id'], item['title'], item['link']))
        self.db.commit()
        return item

    def __init__(self, host, username, password, port, database):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MYSQL_HOST'), username=crawler.settings.get('MYSQL_USERNAME'), password=crawler.settings.get('MYSQL_PASSWORD'), database=crawler.settings.get('MYSQL_DATABASE'), port=crawler.settings.get('MYSQL_PORT'))
    
    # 蜘蛛对象生成的时候调用
    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    # 蜘蛛关闭的时候调用
    def close_spider(self, spider):
        self.db.close()


# 图片保存管道
class U175ImagePipeline(ImagesPipeline):
    # 生成图片下载的请求对象
    def get_media_requests(self, item, info):
        if isinstance(item, U175Item):
            filename = item['title'] + '.jpg'
            yield scrapy.Request(item['cover'],meta={'filename': filename})
    
    # 文件名
    def file_path(self, request, response=None, info=None):
        filename = request.meta['filename']
        return filename
    
    # 判断图片是否请求成功
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
```

说明：

>   写了pipelines后需要在settings.py文件中ITEMS_PIPELINE中添加该类并设置优先级才会生效

# 补充：

生成大量测试数据：

`pip install ForgeryPy3`

```python
>>> import forgery_py
# 随机生成地址
>>> forgery_py.address.street_address()
'4358 Shopko Junction'
# 随机生成颜色的十六进制
>>> forgery_py.basic.hex_color()
'3F0A59'
# 随机生成信用卡类型
>>> forgery_py.credit_card.type()
'Visa'
# 随机生成货币描述
>>> forgery_py.currency.description()
'Slovenia Tolars'
# 随机生成日期
>>> forgery_py.date.date()
datetime.date(2012, 7, 27)
# 随机生成邮箱地址
>>> forgery_py.email.address()
'debra@tavu.edu'
# 随机生成ip地址
>>> forgery_py.internet.ip_v4()
'150.64.188.100'
# 随机生成一种乱数假文标题
>>> forgery_py.lorem_ipsum.title()
'Pretium nam rhoncus ultrices!'
# 随机生成一个金额的钱
>>> forgery_py.monetary.money()
'$4.50'
# 随机生成一个全名
>>> forgery_py.name.full_name()
'Mary Peters'
# 随机生成一种语言
>>> forgery_py.personal.language()
'Hungarian'
# 随机生成一个社保编号
>>> forgery_py.russian_tax.person_inn()
'768974545606'
# 随机生成一个时区
>>> forgery_py.time.zone()
'Melbourne'
```

# 跳到最后
