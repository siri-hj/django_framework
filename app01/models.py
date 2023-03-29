from django.db import models

# Create your models here.
class userinfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    ppassword = models.CharField(max_length=60)
    depart_id = models.CharField(max_length=10)


class department(models.Model):
    depart_name=models.CharField(max_length=30)
    depart_num=models.CharField(max_length=10)