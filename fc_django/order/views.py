from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order

# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('product/' + str(form.product))

    # 폼을 생성할때 어떤 인자 값을 전달해서 만들것인지를 결정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        querySet = Order.objects.filter(
            fcuser__email=self.request.session.get('user'))
        return querySet
