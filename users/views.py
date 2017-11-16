from django.shortcuts import render_to_response
from .models import Profile
from django.views.generic import TemplateView

# Create your views here.


def profile_detail(request):
    return render_to_response('films/user_profile_detail.html')


class ProfileView(TemplateView):
    model = Profile
    template_name = 'films/user_profile_detail.html'


class RegistrationView(TemplateView):
    model = Profile
    template_name = 'films/registration.html'

