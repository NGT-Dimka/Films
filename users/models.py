from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь:')
    location = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт:')
    birth_date = models.DateField(blank=True, verbose_name='Дата рождения:')
    avatar = models.ImageField(verbose_name='Аватар:')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    @staticmethod
    def create_profile(instance, created):
        if created:
            Profile.objects.create(user=instance)

    @staticmethod
    def save_profile(instance):
        instance.Profile.save()

    @property
    def __str__(self):
        return self.user.username
