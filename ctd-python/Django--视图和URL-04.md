# Django--视图和URL--Ubuntu18-04（2022年）

#### 定义视图

- 视图就是一个`Python`函数，被定义在`应用`的`views.py`中.
- 视图的第一个参数是`HttpRequest`类型的对象`reqeust`，包含了所有`请求信息`.
- 视图必须返回`HttpResponse对象`，包含返回给请求者的`响应信息`.
- 需要导入`HttpResponse`模块 :`from django.http import HttpResponse`
- 定义视图函数 : 响应字符串`OK!`给客户端

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/book$ more views.py 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello Django!!!')

```

**接下定义找到视图URL**

查找视图的过程 :

- 1.请求者在浏览器地址栏中输入URL, 请求到网站.
- 2.网站获取URL信息.
- 3.然后与编写好的URLconf逐条匹配.
- 4.如果匹配成功则调用对应的视图.
- 5.如果所有的URLconf都没有匹配成功.则返回404错误.

基本步骤：

- 需要两步完成`URLconf`配置
  - 1.在`项目`中定义`URLconf`
  - 2.在`应用`中定义`URLconf`

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/bookmanager$ more urls.py 
"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),    #只要不是admin开头的都匹配下一个
    url(r'^', include('book.urls')),
]
#新建一个urls.py
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/book$ more urls.py 
from django.conf.urls import url
from book.views import index


urlpatterns = [
    url(r'^$', index),
]

```

**admin匹配不变化**
![8](D:\var\python\ctd-python\ass\8.png)

**显示hello Django!!!**

![7](D:\var\python\ctd-python\ass\7.png)

**View和URL匹配流程**

![img](/assets/view_url.png)







