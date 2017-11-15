# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

from films.models import Film, UserProfile
from films.forms import FilmComment


class FilmsListView(ListView):
    model = Film
    queryset = Film.objects.select_related('producer').all()


class UserProfileDetailView(DetailView):
    model = UserProfile
    UserProfile.objects.select_related('user_id').all()
    template_name = 'films/user_profile_detail.html'


class GenreView(ListView):
    model = Film
    Film.objects.select_related('genre').all()
    template_name = 'films/film_list.html'


class FilmDetailView(DetailView):
    model = Film

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = FilmComment(data={
            'object_id': self.kwargs['pk'],
            'user': self.request.user.id,
            'content_type': ContentType.objects.get_for_model(Film)
        })
        context['comments'] = self.get_object().comments
        return context


def post_film_comment(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    form = FilmComment(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    form.save()

    return HttpResponseRedirect(redirect_to=request.POST.get('next'))


def film_list(request):
    return render_to_response('films/film_list.html')


def film_detail(request):
    return render_to_response('films/film_detail.html')
