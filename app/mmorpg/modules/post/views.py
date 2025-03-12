from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView , DetailView



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