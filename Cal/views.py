from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import datetime
import calendar

# Create your views here.
from django.utils import timezone

from Cal.forms import ClassForm
from Cal.models import Class


@login_required(login_url='/landing')
def calendar_page(request):
    day = datetime.date.today()
    day = day.replace(day=1)
    cal = []
    for n in range(len(calendar.monthcalendar(day.year, day.month))):
        week = []
        for n in range(7):
            if n == day.weekday():
                week.append(day.day)
                if day.day != calendar.monthrange(day.year, day.month)[1]:
                    day = day.replace(day=day.day + 1)
            else:
                week.append(0)
        cal.append(week)
    print(cal)
    context = {
        'cal': cal,
        'today': datetime.date.today().day
    }
    return render(request, "calendar_view.html", context)


@login_required(login_url='/landing')
def class_page(request, my_id):
    obj = get_object_or_404(Class, id=my_id)
    is_signed = False
    if request.user in obj.signed.all():
        print("dupa")
        is_signed = True
    context = {
        'object': obj,
        'is_signed': is_signed
    }
    return render(request, "class_view.html", context)


@login_required(login_url='/landing')
def add_class_page(request):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        new_class = form.save(commit=False)
        new_class.trainer = request.user
        new_class.save()
        form = ClassForm()
    context = {
        "form": form,
    }
    return render(request, "add_class_view.html", context)


@login_required(login_url='/landing')
def join_view(request, my_id):
    obj = get_object_or_404(Class, id=my_id)
    if not request.user in obj.signed.all():
        obj.signed.add(request.user)
    return redirect("cal:class-view", my_id)


@login_required(login_url='/landing')
def leave_view(request, my_id):
    obj = get_object_or_404(Class, id=my_id)
    if request.user in obj.signed.all():
        obj.signed.remove(request.user)
    return redirect("cal:class-view", my_id)


@login_required(login_url='/landing')
def signed_page(request):
    past = Class.objects.filter(signed=request.user, date__lte=timezone.now())
    future = Class.objects.filter(signed=request.user, date__gt=timezone.now())
    context = {
        'past': past,
        'future': future
    }
    return render(request, "signed_view.html", context)
