from django.core.mail import EmailMessage

from .models import Post, Reaction, User
from .forms import PostForm, ReactionForm
from django.views.generic import (ListView, CreateView,
                                  DetailView, View, UpdateView,
                                  FormView, DeleteView)
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PostView(ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'


class CreatePost(LoginRequiredMixin, CreateView):
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
        reactions = Reaction.objects.filter(post_id=self.kwargs['pk'])
        context['reactions'] = reactions
        return context


@login_required()
def update_view(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=instance.pk)
    else:
        form = PostForm(instance=instance)
    return render(request, 'update-post.html', {'form': form,
                                                'items': instance})


@login_required()
def delete_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('post')


class CreateReaction(LoginRequiredMixin, View):
    def post(self, request):
        data = {
            'user': request.POST['user'],
            'post_id': request.POST['post_id'],
            'text': request.POST['text']
        }
        user = User.objects.get(username=data['user'])
        post = Post.objects.get(id=data['post_id'])
        reaction = Reaction.objects.create(user=user,
                                           post_id=post,
                                           text=data['text'])
        reaction.save()
        return redirect('detail', pk=data['post_id'])


@login_required()
def update_reaction(request, pk):
    instance = get_object_or_404(Reaction, pk=pk)
    form = ReactionForm(request.POST, instance=instance)
    if form.is_valid():
        if 'validate' in request.GET:
            form.validate = True
        form.save()
        return redirect('post')
    else:
        form = ReactionForm(instance=instance)
    return render(request, 'update-reaction.html', {'form': form,
                                                    'items': instance})

@login_required()
def validate_reaction(request, pk):
    if request.method == 'POST':
        instance = Reaction.objects.get(id = pk)
        instance.validate = True
        instance.save()
        message = EmailMessage(subject='Board Post Servise',
                     body=f'Ваш отклик был принят'
                          f'пользователем {request.user}.',
                     to=[f'{instance.user.email}'])
        message.send()
    return redirect('filter')


@login_required()
def delete_reaction(reuest, pk):
    if reuest.method == 'POST':
        reaction = Reaction.objects.get(id=pk)
        post = Post.objects.get(reaction=reaction)
        reaction.delete()
        return redirect('detail', pk=post.id)
