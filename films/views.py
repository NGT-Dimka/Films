# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from films.models import Film, UserProfile
from django.views.generic import ListView, DetailView


class FilmsListView(ListView):
    model = Film


class FilmDetailView(DetailView):
    model = Film


class UserProfileDetailView(DetailView):
    model = UserProfile

