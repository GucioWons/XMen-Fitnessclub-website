import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar


# Create your views here.
from Pages.forms import SignUpForm


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('pages:home-view')
    return render(request, "landing_view.html", context={})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('pages:home-view')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home-view')
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login_view.html", context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('pages:home-view')
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("pages:home-view")
    context = {
        "form": form
    }
    return render(request, "register_view.html", context)

@login_required(login_url='/landing')
def logout_view(request):
    logout(request)
    return redirect("pages:landing-view")

@login_required(login_url='/landing')
def home_page(request):
    return render(request, "home_view.html", context={})
