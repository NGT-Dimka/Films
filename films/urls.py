from films.views import FilmsListView, FilmDetailView, post_film_comment, UserProfileDetailView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', FilmsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', FilmDetailView.as_view(), name='detail'),
    url(r'^post_comment/$', post_film_comment, name='post-comment'),
    url(r'^user_id=(?P<pk>\d+)/$', UserProfileDetailView.as_view(), name='user_profile'),
]
