
from django.db import models
from django.contrib.auth.models import User
# 引入内置信号
from django.db.models.signals import post_save
# 引入信号接收器的装饰器
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=20,blank=True)
    avatar = models.ImageField(upload_to='avater/%Y%m%d/',blank=True)
    bio = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)

