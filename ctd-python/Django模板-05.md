# Python学习历程--Django模板-05（2022年）

#### 1.创建模板

- 在`应用`同级目录下创建模板文件夹`templates`. 文件夹名称固定写法.
- 在`templates`文件夹下, 创建`应用`同名文件夹. 例, `Book`
- 在`应用`同名文件夹下创建`网页模板`文件. 例 :`index.html`

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/templates/Book$ more index.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Templates</title>
</head>
<body>
    <h1>hello Django Templates!!!</h1>
    <p>{{ title }}</p>
</body>
</html>

```

![9](D:\var\python\ctd-python\ass\9.png)

#### 2.设置模板查找路径

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/bookmanager$ more settings.py 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },

```

![10](D:\var\python\ctd-python\ass\10.png)

#### 3.模板接收视图传入的数据

```python
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager/book$ more views.py 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse('hello Django!!!')
    context = {'title': 'Templates context test'}
    return render(request, 'Book/index.html', context)

```

![11](D:\var\python\ctd-python\ass\11.png)



#### 4. 查看模板处理数据成果

![12](D:\var\python\ctd-python\ass\12.png)



# View-Templates流程

![new_mvt](D:\var\python\ctd-python\assets\new_mvt.png)