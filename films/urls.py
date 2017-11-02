from films.views import FilmsListView, FilmDetailView, UserProfileDetailView
from django.conf.urls import url

urlpatterns = [
                  url(r'^$', FilmsListView.as_view()),
                  url(r'^(?P<pk>\d+)/$', FilmDetailView.as_view()),
                  url(r'^(?P<id>\w+)/$', UserProfileDetailView.as_view()),
              ]
