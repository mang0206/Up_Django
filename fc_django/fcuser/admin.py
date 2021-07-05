from django.contrib import admin
from .models import Fcuser

# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    # ,를 꼭 써줘야 한다. ()만 쓴다면 문자열로 인식하고 튜플로 인식 x
    list_display = ('email',)


# 사이트 등록
admin.site.register(Fcuser, FcuserAdmin)
