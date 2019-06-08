from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #기본 인적 사항
    sex = models.CharField(max_length=10,default="male")
    smoke = models.CharField(max_length=10,default="no")

    # 청결
    shoes = models.IntegerField(default=1)
    toilet = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=1)
    room = models.IntegerField(default=1)

    #생활패턴
    room_in = models.IntegerField(default=1)
    sleep = models.IntegerField(default=1)
    roomate = models.IntegerField(default=1)

    #인성
    one = models.IntegerField(default=1)
    two = models.IntegerField(default=1)
    thr = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user)
