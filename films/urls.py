from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from Films import settings
from films.views import FilmsListView, FilmDetailView, UserProfileDetailView
from django.conf.urls import url

urlpatterns = [
                  url(r'^$', FilmsListView.as_view()),
                  url(r'^(?P<pk>\d+)/$', FilmDetailView.as_view()),
                  url(r'^(?P<pk>\d+)/$', UserProfileDetailView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<pk>\w+)/$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
