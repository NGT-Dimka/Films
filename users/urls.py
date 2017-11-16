from users.views import ProfileView
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileView.as_view(), name='user_profile'),
]


