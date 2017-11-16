from users.views import ProfileView, RegistrationView
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileView.as_view(), name='user_profile'),
    url('^new_user/$', RegistrationView.as_view(), name='registration'),
]
