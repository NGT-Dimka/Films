from django import forms
from users.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'password', 'email', 'location', 'birth_date',
                  'avatar', 'is_active'}
