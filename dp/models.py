import redis
from django.db import models


# Create your models here.

# makemigrations  migrate
class DataInfo(models.Model):
    file_name = models.CharField(max_length=64)
    file = models.FileField()
    # 分数
    fraction = models.IntegerField()
    people_name = models.CharField(max_length=32)


