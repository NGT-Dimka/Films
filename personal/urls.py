from .views import ProducerDetailView
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProducerDetailView.as_view(), name='producer-detail'),
]
