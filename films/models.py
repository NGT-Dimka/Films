# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse


# Create your models here.


class Film(models.Model):
    poster = models.ImageField(upload_to="films/media/films/Posters/", verbose_name="Постер фильма", blank=True)
    title_film = models.CharField(max_length=255, verbose_name='Название:')
    year_pub = models.DateField(verbose_name='Выход в прокат:')
    genre = models.CharField(max_length=255, verbose_name='Жанр:')
    producer = models.CharField(max_length=150, verbose_name='Продюсер:')
    budget = models.PositiveIntegerField(verbose_name='Бюджет:')
    fees = models.PositiveIntegerField(verbose_name='Сборы:')
    duration = models.PositiveSmallIntegerField(verbose_name='Продолжительность, мин.:')
    content = models.TextField(blank=True, max_length=10000, verbose_name='Сюжет:')

    @property
    def __unicode__(self):
        return self.title_film

    @property
    def get_absolute_url(self):
        return "/films/%i/" % self.id

    @staticmethod
    def film():
        try:
            pass
        except Film.DoesNotExist:
            raise Http404
        s = Film.title_film + "<br><br>" + Film.genre
        return HttpResponse(s)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт:')
    birth_date = models.DateField(blank=True, verbose_name='Дата рождения:')
    avatar = models.ImageField(verbose_name='Аватар:')

    def create_user_profile(self, instance, created):
        if created:
            UserProfile.objects.create(user=instance)

    @staticmethod
    def save_user_profile(instance):
        instance.UserProfile.save()
