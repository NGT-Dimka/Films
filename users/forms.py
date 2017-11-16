from django import forms
from users.models import Profile


class ProfileForm(forms.Form):
    class Meta:
        model = Profile

