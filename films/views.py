# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response

from films.models import Film, UserProfile
from django.views.generic import ListView, DetailView


class FilmsListView(ListView):
    model = Film


class FilmDetailView(DetailView):
    model = Film


class UserProfileDetailView(DetailView):
    model = UserProfile


def user_profile(request):
    return render_to_response('films/user_profile_detail.html')


def login(request):
    return render_to_response('films/login.html')


def logout(request):
    return render_to_response('films/logout.html')


def film_list(request):
    return render_to_response('films/film_list.html')


def film_detail(request):
    return render_to_response('films/film_detail.html')
