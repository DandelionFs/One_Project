from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length=200)
    #生产日期
    date = models.CharField(max_length=200)
    deadline = models.CharField(max_length=200,null=True)
    #剩余时间
    time = models.CharField(max_length=200,null=True)
    #提醒时间
    remind = models.CharField(max_length=200, null=True)
    #分类标签
    tag = models.CharField(max_length=200)
    #备注
    note = models.CharField(max_length=200, null=True)

