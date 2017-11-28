from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import UserManager
from django.utils.translation import gettext as _

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=200, unique=True, db_index=True)
    first_name = models.CharField(_('first_name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('last_name'), max_length=150, blank=True, null=True)
    password = models.CharField(_('password'), max_length=200)
    email = models.EmailField(_('email'), max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт:')
    birth_date = models.DateField(blank=True, verbose_name='Дата рождения:', null=True)
    avatar = models.ImageField(blank=True, verbose_name='Аватар:', null=True)
    is_active = models.BooleanField(_('is_active'), blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.username

    @staticmethod
    def create_profile(instance, created):
        if created:
            User.objects.create(user=instance)

    @staticmethod
    def save_profile(instance):
        instance.User.save()
