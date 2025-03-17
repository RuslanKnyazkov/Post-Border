from django.urls import path
from .views import (PostView, CreatePost,
                    SinglePost, CreateReaction, UpdatePost)

urlpatterns = [
    path('', PostView.as_view(), name = 'post'),
    path('create', CreatePost.as_view(), name = 'create-post'),
    path('<int:pk>', SinglePost.as_view(), name='detail'),
    path('reaction', CreateReaction.as_view(), name='reaction'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update')
]