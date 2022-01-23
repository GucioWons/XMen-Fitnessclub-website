from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from Products.forms import PassForm, TrainingForm, DietForm
from Products.models import Pass, Diet, Training


@login_required(login_url='/landing')
def passes_page(request):
    queryset = Pass.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, "passes_view.html", context)

def bought_page(request):
    diets = Diet.objects.filter(bought=request.user)
    trainings = Training.objects.filter(bought=request.user)
    context = {
        'diets': diets,
        'trainings': trainings
    }
    return render(request, "bought_view.html", context)

def add_pass_page(request):
    if request.user.account.type == 'STAFF':
        form = PassForm(request.POST or None)
        if form.is_valid():
            new_pass = form.save()
            form = PassForm()
    context = {
        "form": form,
    }
    return render(request, "add_pass_view.html", context)

def add_training_page(request):
    if request.user.account.type == 'STAFF' or request.user.account.type == 'TRAINER':
        form = TrainingForm(request.POST or None, request.FILES)
        if form.is_valid():
            new_training = form.save(commit=False)
            new_training.author = request.user
            new_training.save()
            form = TrainingForm()
    context = {
        "form": form,
    }
    return render(request, "add_training_view.html", context)

def add_diet_page(request):
    if request.user.account.type == 'STAFF' or request.user.account.type == 'DIETICIAN':
        form = DietForm(request.POST or None, request.FILES)
        if form.is_valid():
            new_training = form.save(commit=False)
            new_training.author = request.user
            new_training.save()
            form = DietForm()
    context = {
        "form": form,
    }
    return render(request, "add_diet_view.html", context)