from django import forms
from users.models import Profile


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
