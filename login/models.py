from django.db import models


#继承models.Model，固定写法
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)