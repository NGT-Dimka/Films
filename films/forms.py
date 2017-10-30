from django.forms import ModelForm
from films.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
