from django.shortcuts import render_to_response, render, redirect
from django.http.response import HttpResponseNotAllowed
from .models import User
from django.views.generic import TemplateView
from .forms import UserForm


# Create your views here.

class NewUserView(TemplateView):
    model = User
    template_name = 'films/user_profile_detail.html'


def profile_detail(request):
    return render_to_response('films/user_profile_detail.html')


def registration(request):
    if request.method not in ["POST", "GET"]:
        return HttpResponseNotAllowed(permitted_methods=["POST", "GET"])

    if request.method == "POST":

        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return redirect('index')

        return render(request, 'films/registration.html', {'user_form': user_form})

    else:
        user_form = UserForm()
        return render(request, 'films/registration.html', {'user_form': user_form})
