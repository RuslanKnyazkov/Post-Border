from django.shortcuts import render, redirect
from .models import OneTimeCode, User
from .forms import LoginForm
from django.contrib.auth import login, logout , authenticate
from django.views.generic import FormView
from .utils import generated_code
from django.core.mail import EmailMessage
class UserLogin(FormView):
    form_class = LoginForm
    template_name = 'login.html'


def test_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username,
                        password=password)
    if user is not None:
        code = generated_code()
        OneTimeCode.objects.create(code = code, user = user)
        mail = EmailMessage(subject=f'{username}',
                     body=f'Код для потверждения {code}',
                     to=[user.email])
        mail.send()
    else:
        return render(request, template_name='failed-login.html')
        pass
    return redirect('code')

def login_with_code(request):
    if request.POST:
        username = request.POST['username']
        code = request.POST['code']
        if OneTimeCode.objects.filter(code = code,
                                      user__username = username).exists():

            login(request, User.objects.get(username = username))
        return redirect('post')

    return render(request, template_name='login-confirm.html')