from django.urls import path
from .views import PostView, CreatePost, SinglePost

urlpatterns = [
    path('', PostView.as_view(), name = 'post'),
    path('create', CreatePost.as_view(), name = 'create-post'),
    path('<int:pk>', SinglePost.as_view(), name='detail')
]