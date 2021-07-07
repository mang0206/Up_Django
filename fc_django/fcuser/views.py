from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from .forms import LoginForm, RegisterForm

# Create your views here.


def index(request):
    # request.session.get('user') -> session 안에있는 user를 가지고 온다
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    # 정보 저장에 성공하는등 정상적으로 폼이 작동했을 때
    # success_url을 사용해서 해당 주소로 이동이 가능하다.
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 로그인이 정상적으로 되었을때 실행 되는 함수
    def form_valid(self, form):
        # 로그인 한 이메일 정보를 사용자 세션에 저장
        self.request.session['user'] = form.email
        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')
