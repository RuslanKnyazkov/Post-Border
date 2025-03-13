from django.urls import path
from .views import UserLogin, test_login, login_with_code

urlpatterns = [
    path('login', UserLogin.as_view(), name = 'login'),
    path('login/confirm', test_login, name='get_info'),
    path('login/confirm/code', login_with_code, name='code')
]