from django.shortcuts import render
from django.views.generic import DetailView, CreateView, View
from .models import UserProfile
from modules.post.models import Post, User

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = UserProfile
    context_object_name = 'profile'



class FilterView(View):

    def get(self, request, **kwargs):
        post = Post.objects.filter(user = request.user)

        if request.GET:
            queryset = Post.objects.get(
                title = request.GET.get('title'))
            reaction = queryset.reaction_set.all()
            return render(request, template_name='filter-reaction.html',
                          context={'queryset': queryset, 'post': post,
                                   'reaction': reaction})
        return render(request, template_name='filter-reaction.html',
                      context={ 'post': post})
