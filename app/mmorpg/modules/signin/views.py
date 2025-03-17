from django.shortcuts import render, redirect
from .models import OneTimeCode, User
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout , authenticate
from django.views.generic import FormView, View
from .utils import generated_code
from django.core.mail import EmailMessage
from django.http import JsonResponse
class UserLogin(FormView):
    form_class = LoginForm
    template_name = 'login.html'

class RegisterUser(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, template_name='registration-user.html',
                      context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('post')
        return render(request, template_name='registration-user.html',
                      context={'form': form})



def test_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username,
                        password=password)
    print(request.POST)
    if user is not None:
        code = generated_code()
        OneTimeCode.objects.create(code = code, user = user)
        mail = EmailMessage(subject=f'{username}',
                     body=f'Код для потверждения {code}',
                     to=[user.email])
        mail.send()
        return redirect('code')
    else:
        return redirect('login')


def login_with_code(request):
    if request.POST:
        username = request.POST['username']
        code = request.POST['code']
        if OneTimeCode.objects.filter(code = code,
                                      user__username = username).exists():

            login(request, User.objects.get(username = username))
        return redirect('post')

    return render(request, template_name='login-confirm.html')


def sing_out(request):
    logout(request)
    return redirect('post')