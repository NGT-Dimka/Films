from django import forms
from films.models import Comment


class FilmComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = []
        widgets = {
            'user': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }
