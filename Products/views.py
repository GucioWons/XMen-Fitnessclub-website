from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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
    if not request.user.account.type == 'STAFF':
        return redirect("pages:home-view")
    form = PassForm(request.POST or None)
    if form.is_valid():
        new_pass = form.save()
        form = PassForm()
    context = {
        "form": form,
    }
    return render(request, "add_pass_view.html", context)


def add_training_page(request):
    if not request.user.account.type == 'STAFF' or request.user.account.type == 'TRAINER':
        return redirect("pages:home-view")
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
    if not request.user.account.type == 'STAFF' or request.user.account.type == 'DIETICIAN':
        return redirect("pages:home-view")
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


@login_required(login_url='/landing')
def add_pass_to_cart_view(request, my_id):
    cart = request.user.cart
    passs = get_object_or_404(Pass, id=my_id)
    if not cart.passs == passs:
        if not cart.passs:
            cart.passs = passs
            cart.save()
        else:
            cart.passs = passs
            cart.save()
    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_pass_from_cart_view(request, my_id):
    cart = request.user.cart
    passs = get_object_or_404(Pass, id=my_id)
    if cart.passs:
        cart.passs = None
        cart.save()
    return redirect("accounts:cart-view")

@login_required(login_url='/landing')
def add_training_to_cart_view(request, my_id):
    cart = request.user.cart
    training = get_object_or_404(Training, id=my_id)
    if not request.user in training.bought.all():
        if not training in cart.trainings.all():
            cart.trainings.add(training)

    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_training_from_cart_view(request, my_id):
    cart = request.user.cart
    training = get_object_or_404(Training, id=my_id)
    if training in cart.trainings.all():
        cart.trainings.remove(training)
    return redirect("accounts:cart-view")

@login_required(login_url='/landing')
def add_diet_to_cart_view(request, my_id):
    cart = request.user.cart
    diet = get_object_or_404(Diet, id=my_id)
    if not request.user in diet.bought.all():
        if not diet in cart.diets.all():
            cart.diets.add(diet)

    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_diet_from_cart_view(request, my_id):
    cart = request.user.cart
    diet = get_object_or_404(Diet, id=my_id)
    if diet in cart.diets.all():
        cart.diets.remove(diet)
    return redirect("accounts:cart-view")
