from django import forms
from .models import Post, Reaction
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

        widgets = {
            'content' : CKEditorUploadingWidget()
        }

class ReactionForm(forms.ModelForm):
    text = forms.CharField(label='Комментарий', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    class Meta:
        model = Reaction
        fields = ['text']
