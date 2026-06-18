from django.db import models
from django.utils import timezone
from account.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    title = models.CharField(max_length=128, verbose_name=_('Заголовок поста'))
    content = models.TextField(verbose_name=_('Контент поста'))
    time_stamp = models.DateTimeField(default=timezone.now(), verbose_name=_('Дата создания поста'))
    edited = models.BooleanField(default=False, verbose_name=_('Редактирован ли?'))

    def __str__(self):
        return f'{self.title} - {self.time_stamp}'
    
    class Meta:
        verbose_name = _('Пост') #Псевдоним модели в единственном числе
        verbose_name_plural = _('Посты') #Псевдоним модели в множественном числе

class PostAttachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Пост'))
    name = models.CharField(blank=True, null=True, verbose_name=_('Название картинки'))
    file = models.FileField(upload_to='images/', verbose_name=_('Файл'))

    class Meta:
        verbose_name = _('Картинка поста')
        verbose_name_plural = _('Картинки постов')

    def save(self, *args, **kwargs):
        file_name = self.file.name.split('.')[0].capitalize()
        self.name = file_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.post.title} : {self.name}'