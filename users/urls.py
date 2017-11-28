from users.views import registration, NewUserView
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewUserView.as_view(), name='user_profile'),
    url('^new_user/$', registration, name='registration'),
]
