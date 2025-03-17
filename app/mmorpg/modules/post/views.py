from .models import Post, Reaction, User
from .forms import PostForm, ReactionForm
from django.views.generic import (ListView, CreateView ,
                                  DetailView, View, UpdateView,
                                  FormView)
from django.shortcuts import redirect



class PostView(ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SinglePost(DetailView):
    model = Post
    template_name = 'detail-post.html'
    context_object_name = 'single'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = ReactionForm()
        context['form'] = form
        reactions = Reaction.objects.filter(post_id = self.kwargs['pk'])
        context['reactions'] = reactions
        return context

class UpdatePost(UpdateView):
    template_name = 'update-post.html'
    model = Post
    form_class = PostForm
    context_object_name = 'items'

    def get_success_url(self):
        return redirect('update', pk = self.kwargs['pk'])







class CreateReaction(View):
    def post(self, request):
        data = {
            'user' : request.POST['user'],
            'post_id' : request.POST['post_id'],
            'text' : request.POST['text']
        }
        user = User.objects.get(username = data['user'])
        post = Post.objects.get(id = data['post_id'])
        reaction = Reaction.objects.create(user=user,
                                           post_id = post,
                                           text = data['text'])
        reaction.save()
        return redirect('detail', pk = data['post_id'])