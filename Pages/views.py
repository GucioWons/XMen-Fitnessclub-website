from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar


# Create your views here.
from Accounts.models import Account, Cart
from Pages.forms import SignUpForm


def landing_page(request):
    if request.user.is_authenticated:
        messages.error(request, "Thou art already logg'd in.")
        return redirect('pages:home-view')
    return render(request, "landing_view.html", context={})

def login_page(request):
    if request.user.is_authenticated:
        messages.error(request, "Thou art already logg'd in.")
        return redirect('pages:home-view')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, "Thee has't logg'd in successfully.")
            if user is not None:
                login(request, user)
                return redirect('pages:home-view')
        else:
            messages.error(request, "wrong username or password!")
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login_view.html", context)

def register_page(request):
    if request.user.is_authenticated:
        messages.error(request, "Thou art already logg'd in.")
        return redirect('pages:home-view')
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        Account.objects.create(user=user, type="CLIENT")
        Cart.objects.create(user=user)
        login(request, user)
        messages.success(request, "Thee has't successfully regist'r'd.")
        return redirect("pages:home-view")
    context = {
        "form": form
    }
    return render(request, "register_view.html", context)

@login_required(login_url='/landing')
def logout_view(request):
    logout(request)
    messages.success(request, "Thee has't been logg'd out successfully.")
    return redirect("pages:landing-view")

@login_required(login_url='/landing')
def home_page(request):
    delta = None
    if request.user.account.pass_expire:
        delta = request.user.account.pass_expire - datetime.date(datetime.now())
        delta = delta.days
    context = {
        'delta': delta
    }
    return render(request, "home_view.html", context)
