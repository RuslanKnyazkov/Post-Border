from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.shortcuts import  reverse
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='Пользователь')
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 blank=False)
    title = models.CharField(max_length=100,
                             blank=False)
    content = RichTextUploadingField()

    data_created = models.DateTimeField(verbose_name='Время создания',
                                        auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})


class Category(models.Model):
    NAME_CATEGOIES = [
        ('Tanks', _('Танки')),
        ('Heals', _('Хилы')),
        ('DD', _('ДД')),
        ('Merchants', _('Торговцы')),
        ('Guild Masters', _('Гилдмастеры')),
        ('Quest Givers', _('Квестгиверы')),
        ('Blacksmiths', _('Кузнецы')),
        ('Tanners', _('Кожевники')),
        ('Potion Makers', _('Зельевары')),
        ('Spellmasters', _('Мастера заклинаний')),
    ]
    name = models.CharField(max_length=20,
                            choices=NAME_CATEGOIES)

    def __str__(self):
        return self.name


class Reaction(models.Model):
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.post_id}\n {self.text}'