# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Producer(models.Model):
    full_name = models.CharField(verbose_name='Полное имя', max_length=255)

    class Meta:
        verbose_name = 'Продюсер'
        verbose_name_plural = 'Продюсеры'

    def __str__(self):
        return self.full_name


class Genres(models.Model):
    genres = models.TextField(verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genres


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Тип содержимого')
    object_id = models.PositiveIntegerField(verbose_name='Идентификатор объекта')
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Film(models.Model):
    poster = models.ImageField(upload_to="films/media/films/Posters/", verbose_name="Постер фильма", blank=True)
    title_film = models.CharField(max_length=255, verbose_name='Название:')
    year_pub = models.DateField(verbose_name='Выход в прокат:')
    genre = models.ManyToManyField(Genres, verbose_name='Жанр:')
    producer = models.ForeignKey(Producer, verbose_name='Продюсер:')
    budget = models.PositiveIntegerField(verbose_name='Бюджет:')
    fees = models.PositiveIntegerField(verbose_name='Сборы:')
    duration = models.PositiveSmallIntegerField(verbose_name='Продолжительность, мин.:')
    content = models.TextField(blank=True, max_length=10000, verbose_name='Сюжет:')
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

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

    def __str__(self):
        return self.title_film


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь:')
    location = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт:')
    birth_date = models.DateField(blank=True, verbose_name='Дата рождения:')
    avatar = models.ImageField(verbose_name='Аватар:')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    @staticmethod
    def create_user_profile(instance, created):
        if created:
            UserProfile.objects.create(user=instance)

    @staticmethod
    def save_user_profile(instance):
        instance.UserProfile.save()

    def __str__(self):
        return self.user_id
