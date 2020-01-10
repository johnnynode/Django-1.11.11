# Django-demo 项目

### Environment 环境

- Mac
- Python 3.6
- Django 1.11.11

### 项目创建时使用的命令

- $ `django-admin startproject DjangoApp`
- 后期将最外层目录修改为了: `Django-1.11.11`

### 项目运行

- $`python manage.py runserver` 
    * 这样只能本机调试访问

- $`python manage.py runserver 8080`
    * 该runserver命令在端口8000的内部IP上启动开发服务器。当然也可以指定端口开启服务,如8080端口

- $`python3 manage.py runserver 0:8000`
    * 这样启动，通过`0`可以进行远程访问, 并且在settigns.py中ALLOWED_HOSTS添加自己的ip地址, 或支持所有 ALLOWED_HOSTS = ['*']
    * runserver只能在本机使用, 是Django自带的http服务
    * 部署时应使用uwsgi

### Add Application 添加的应用

- $`python3 manage.py startapp app`

### 可访问页面

- http://0.0.0.0:8000/app/
- http://0.0.0.0:8000/admin/

### admin登录密码

- 用户名: `johnny`
- 密码: `123456_admin`

### 数据库文件

- 详见mysql.sql