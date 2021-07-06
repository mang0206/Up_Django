from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    # 정보 저장에 성공하는등 정상적으로 폼이 작동했을 때
    # success_url을 사용해서 해당 주소로 이동이 가능하다.
    success_url = '/'
