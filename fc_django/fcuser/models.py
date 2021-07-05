from django.db import models

# Create your models here.


class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='이메일')
    register_date = models.DateField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'