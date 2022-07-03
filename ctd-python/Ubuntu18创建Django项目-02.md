# Ubuntu18创建Django项目-02（2022年）

#### 1.准备工作

目前最新的Ubuntu20有些虚拟环境兼容性不是很好，安装的时候碰见各种命令找不到的问题，
所以我还是选择了ubuntu18。

**TODO:**[TMP.link](https://app.tmp.link/)

废话不多说，直接把我做好的Vmvare voa镜像附上。用Vmvare直接打开即可使用`用户名：andre  密码：123123`

其他相关学习资料我会放到我的github上定期更新。

**事先的环境准备命令大致如下(这些在我的Voa镜像中已经有了)：**

```shell
#如果不指定python版本，默认安装的是python2的虚拟环境，目前世界上大部分都是python3了所以推荐使用python3
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python
sudo apt-get install python-pip
sudo apt-get install python3
sudo apt-get install python-pip3

#安装虚拟环境的命令
sudo pip install virtualenv
sudo pip install virtualenvwrapper
#创建目录用来存放虚拟环境
mkdir  $HOME/.virtualenvs
#打开~/.bashrc文件，并添加如下：
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
#有效化上面命令
source ~/.bashrc
#在python3中，创建虚拟环境
mkvirtualenv -p python3 python_django
```

#### 2.开始搭建Django项目

**创建工程**

```shell
#退出虚拟环境的命令 : deactivate  rmvirtualenv 
#删除虚拟环境的命令 :虚拟环境名称
#进入到虚拟环境  
andre@ubuntu18:~$ workon python-django
#虚拟环境中安装django==1.11.11
(python-django) andre@ubuntu18:~$ pip install django==1.11.11
#查看虚拟环境中安装的包==1.11.11
(python-django) andre@ubuntu18:~$ pip list
Package           Version
----------------- -------
asgiref           3.4.1
Django            1.11.11
pip               21.3.1
pytz              2022.1
setuptools        59.6.0
sqlparse          0.4.2
typing_extensions 4.1.1
wheel             0.37.1
#创建工程
(python-django) andre@ubuntu18:~/Desktop$ mkdir python1
(python-django) andre@ubuntu18:~/Desktop$ cd python1/
(python-django) andre@ubuntu18:~/Desktop/python1$ 
(python-django) andre@ubuntu18:~/Desktop/python1$ django-admin startproject bookmanager
(python-django) andre@ubuntu18:~/Desktop/python1$ cd bookmanager/
#查看下已经建好的工程
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ tree
├── bookmanager #与项目同名的目录，此处为bookmanager。
│   ├── __init__.py   #python初始化加载文件
│   ├── settings.py   #settings.py是项目的整体配置文件。
│   ├── urls.py       #urls.py是项目的URL配置文件。
│   └── wsgi.py       #wsgi.py是项目与WSGI兼容的Web服务器入口。
└── manage.py         #manage.py是项目管理文件，通过它管理项目。

#manage.py就是管理脚本，Python写的脚本文件，就是去尝试导入一个import django
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ more manage.py 
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
    
#运行服务器,按ctrl+c停止服务器。
#python manage.py runserver ip:端口
#或：
#python manage.py runserver   这里的IP默认的是一个回环地址，并且端口号是8000
#127.0.0.1，通常被称为本地回环地址(Loop back address)，不属于任何一个有类别地址类。 它代表设备的本地虚拟接口，所以默认被看作是永远不会宕掉的接口。 在windows操作系统中也有相似的定义，所以通常在不安装网卡前就可以ping通这个本地回环地址。
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py runserver
April 27, 2022 - 03:48:41
Django version 1.11.11, using settings 'bookmanager.settings'
Starting development server at http://127.0.0.1:8000/
```

![huihuan](D:\var\python\ctd-python\assets\huihuan.png)

**创建子应用**

```shell
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py startapp book
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py startapp login
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ python manage.py startapp pay
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ tree
.
├── book
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── bookmanager
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3

#admin.py文件跟网站的后台管理站点配置相关。
#apps.py文件用于配置当前子应用的相关信息。
#migrations目录用于存放数据库迁移历史文件。
#models.py文件用户保存数据库模型类。
#tests.py文件用于开发测试用例，编写单元测试。
#views.py文件用于编写Web应用视图。
```

用pythcarm打开工程项目

![subpro](D:\var\python\ctd-python\assets\subpro.png)

默认情况下pycharm并不知道我们的Django在哪里需要找到file-->settings-->Project。设置我们虚拟环境的python3目录即可，
我们的虚拟环境python3路径可以在虚拟环境console中查看

```shell
(python-django) andre@ubuntu18:~/Desktop/python1/bookmanager$ type python3
python3 is /home/andre/.virtualenvs/python-django/bin/python3
```

![2](D:\var\python\ctd-python\ass\2.png)![1](D:\var\python\ctd-python\ass\1.png)

#### 注册安装子应用

> 创建出来的子应用目录文件虽然被放到了工程项目目录中，但是django工程并不能立即直接使用该子应用，需要注册安装后才能使用。在工程配置文件settings.py中，**INSTALLED_APPS**项保存了工程中已经注册安装的子应用，初始工程中的INSTALLED_APPS如下：

![3](D:\var\python\ctd-python\ass\3.png)



#### 安装Mysql

```shell
#安装Mysql
andre@ubuntu18:~$ sudo apt-get install mysql-server
andre@ubuntu18:~$ sudo service mysql status
● mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2022-04-27 14:01:28 JST; 43s ago
#安装客户端
andre@ubuntu18:~$ sudo apt-get install mysql-client
#查看版本
andre@ubuntu18:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.37, for Linux (x86_64) using  EditLine wrapper

#新版本mysql链接的时候有个坑，需要先用debian-sys-maint账户登录mysql再更改root的密码
andre@ubuntu18:~$ sudo chmod 755 /etc/mysql/debian.cnf
andre@ubuntu18:~$ cat /etc/mysql/debian.cnf
# Automatically generated for Debian scripts. DO NOT TOUCH!
[client]
host     = localhost
user     = debian-sys-maint
password = krAQ7bSDYf2NGKZf
socket   = /var/run/mysqld/mysqld.sock
[mysql_upgrade]
host     = localhost
user     = debian-sys-maint
password = krAQ7bSDYf2NGKZf
socket   = /var/run/mysqld/mysqld.sock

andre@ubuntu18:~$ mysql -udebian-sys-maint -pkrAQ7bSDYf2NGKZf
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
mysql> UPDATE mysql.user SET authentication_string=PASSWORD('123123'), PLUGIN='mysql_native_password' WHERE USER='root';
mysql> USE mysql;
mysql>  UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;
Bye
#成功登录了
andre@ubuntu18:~$ mysql -uroot -p123123
mysql> 
```
