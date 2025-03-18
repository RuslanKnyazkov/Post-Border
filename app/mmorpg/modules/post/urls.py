from django.urls import path
from .views import (PostView, CreatePost,
                    SinglePost, CreateReaction,
                     delete_reaction, update_reaction,
                    delete_post, update_view)

urlpatterns = [
    path('', PostView.as_view(), name = 'post'),
    path('create', CreatePost.as_view(), name = 'create-post'),
    path('<int:pk>', SinglePost.as_view(), name='detail'),
    path('reaction', CreateReaction.as_view(), name='reaction'),
    path('update/<int:pk>', update_view, name='update'),
    path('reaction/delete/<int:pk>', delete_reaction, name='reaction-delete'),
    path('reaction/update/<int:pk>', update_reaction, name='update-reaction'),
    path('post/delete/<int:pk>', delete_post, name = 'post-delete')

]