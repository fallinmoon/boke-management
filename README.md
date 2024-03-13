Django
博客管理系统

使用的环境： 
Win 10（64位）
Python 3.7.0
Django 2.2


python manage.py makemigrations，对模型的更改创建新的迁移表

通过运行 makemigrations 命令，Django 会检测你对模型文件的修改，并且把修改的部分储存为一次迁移。

然后输入python manage.py migrate，应用迁移到数据库中：

python manage.py runserver 8000 启动服务器

python manage.py createsuperuser 创建超级管理员账号

http://127.0.0.1:8000/article/article-list/ 访问主页面

http://127.0.0.1:8000/admin 访问后台管理
