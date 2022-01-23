from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from Accounts.models import Account
from Cal.models import Class
from Products.models import Diet, Training


@login_required(login_url='/landing')
def dietician_page(request, my_id):
    obj = get_object_or_404(Account, id=my_id)
    if not obj.type == 'DIETICIAN':
        return redirect("pages:home-view")
    queryset = Diet.objects.filter(author=obj.user)
    context = {
        'object': obj,
        'queryset': queryset
    }
    return render(request, "dietician_view.html", context)

@login_required(login_url='/landing')
def trainer_page(request, my_id):
    obj = get_object_or_404(Account, id=my_id)
    if not obj.type == 'TRAINER':
        return redirect("pages:home-view")
    classes = Class.objects.filter(trainer=obj.user, date__gt=timezone.now())
    trainings = Training.objects.filter(author=obj.user)
    context = {
        'object': obj,
        'classes': classes,
        'trainings': trainings
    }
    return render(request, "trainer_view.html", context)