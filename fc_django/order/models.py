from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.
#


class Order(models.Model):
    # 주문 같은 경우에는 어떤 사용자가 어떤 물건을 주문하는것이기 때문에 외래키가 많이 필요
    # 어떤 앱 안에 있는 이 모델을 사용하겠다라는 뜻
    # foreinkey 사용시에는 on_delete 속성 값을 꼭 써줘야 한다.
    # on_delete는 연결된 사용자가 삭제될 시 어떻게 할지를 뜻한다.
    fcuser = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
