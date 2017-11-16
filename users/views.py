from django.shortcuts import render_to_response, render
from .models import Profile
from django.views.generic import TemplateView
from .forms import ProfileForm

# Create your views here.


def profile_detail(request):
    return render_to_response('films/user_profile_detail.html')


class ProfileView(TemplateView):
    model = Profile
    template_name = 'films/user_profile_detail.html'


class RegistrationView(TemplateView):
    model = Profile
    template_name = 'films/registration.html'


def registration(self, request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.instance.created_by = self.request.ProfileForm
            return super(ProfileForm, self).form_valid(form)
        else:
            form = ProfileForm()
        return render(request, 'films/registration.html', {'form': form, 'ProfileForm': ProfileForm})

