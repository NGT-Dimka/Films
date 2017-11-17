from django.contrib.auth import login
from django.shortcuts import render_to_response, render, redirect
from django.views.generic.edit import ModelFormMixin

from .models import Profile
from django.views.generic import TemplateView, CreateView
from .forms import ProfileForm

# Create your views here.


def profile_detail(request):
    return render_to_response('films/user_profile_detail.html')


class ProfileView(TemplateView):
    model = Profile
    template_name = 'films/user_profile_detail.html'


class RegistrationView(ModelFormMixin):
    model = Profile
    template_name = 'films/registration.html'


def registration(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user.authentificate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form = ProfileForm()
        return render(request, 'films/registration.html', {'form': form, 'ProfileForm': ProfileForm})

