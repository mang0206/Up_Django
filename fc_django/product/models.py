from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    prive = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stuck = models.IntegerField(verbose_name='재고')
    register_date = models.DateField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'fastcampus_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'