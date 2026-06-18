from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=128, verbose_name=_('Псевдоним'))
    first_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Имя пользователя'))
    last_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Фамилия пользователя'))
    email = models.EmailField(unique=True, verbose_name=_('Почта'))
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Номер телефона'))
    password = models.CharField(max_length=125, verbose_name=_('Пароль'))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    #karim@gmail.com -> ['karim', 'gmail.com']
    #karim@mail.ru

    def save(self, *args, **kwargs):
        email_prefix = self.email.split('@')[0]
        self.username = f'{self.first_name.lower()} - {email_prefix.lower()}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.first_name} : {self.email}'
