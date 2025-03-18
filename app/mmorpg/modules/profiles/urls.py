from django.urls import path
from .views import ProfileView, FilterView

urlpatterns = [
    path('<int:pk>', ProfileView.as_view(), name= 'profile'),
    path('filter', FilterView.as_view(), name = 'filter')
]