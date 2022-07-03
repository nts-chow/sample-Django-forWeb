# Django数据模型和站点管理--Ubuntu18-03（2022年）

## 模型

#### ORM框架进行数据库开发

- `MVT`设计模式中的`Model`, 专门负责和数据库交互.对应`(models.py)`
- 由于`Model`中内嵌了`ORM框架`, 所以不需要直接面向数据库编程.
- 而是定义模型类, 通过`模型类和对象`完成数据库表的`增删改查`.
- `ORM框架`就是把数据库表的行与相应的对象建立关联, 互相转换.使得数据库的操作面向对象.

#### 定义模型类

- 根据书籍表结构设计模型类:

  - 模型类：BookInfo
  - 书籍名称字段：name

- 根据人物表结构设计模型类：

  - 模型类：PeopleInfo
  - 人物姓名字段：name
  - 人物性别字段：gender
  - 外键约束：book
    - 外键要指定所属的模型类`book = models.ForeignKey(BookInfo)`

- 说明 :

  - 书籍-人物的关系为一对多. 一本书中可以有多个英雄.
  - 不需要定义主键字段, 在生成表时会自动添加, 并且值为自增长.

- 根据数据库表的设计

  - 在`models.py`中定义模型类,继承自`models.Model`

  - ```python
    from django.db import models
    
    # Create your models here.
    # 准备书籍列表信息的模型类
    class BookInfo(models.Model):
        # 创建字段，字段类型...
        name = models.CharField(max_length=10)
    
    # 准备人物列表信息的模型类
    class PeopleInfo(models.Model):
        name = models.CharField(max_length=10)
        gender = models.BooleanField()
        # 外键约束：人物属于哪本书
        book = models.ForeignKey(BookInfo)
    ```

    ![](D:\var\python\ctd-python\ass\4.png)


#### 模型迁移 （建表）

```shell
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py makemigrations
Migrations for 'book':
  book/migrations/0001_initial.py
    - Create model BookInfo
    - Create model PeopleInfo
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, book, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying book.0001_initial... OK
  Applying sessions.0001_initial... OK

```



## 站点管理

#### 创建管理员

```
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py createsuperuser
```

登陆站点 :`http://127.0.0.1:8000/admin`

在`应用`的`admin.py`文件中注册模型类

- 需要导入模型模块 :`from book.models import BookInfo,PeopleInfo`

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/book$ more admin.py 
from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)

```

![5](D:\var\python\ctd-python\ass\5.png)

![6](D:\var\python\ctd-python\ass\6.png)



