from django.contrib import messages
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
        messages.error(request, "Thee cannot access this page!")
        return redirect("pages:home-view")
    form = PassForm(request.POST or None)
    if form.is_valid():
        new_pass = form.save()
        form = PassForm()
        messages.success(request, "Thee has't successfully did add passeth!")
    context = {
        "form": form,
    }
    return render(request, "add_pass_view.html", context)


def add_training_page(request):
    if not request.user.account.type == 'STAFF' or not request.user.account.type == 'TRAINER':
        messages.error(request, "Thee cannot access this page!")
        return redirect("pages:home-view")
    form = TrainingForm(request.POST or None, request.FILES)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.author = request.user
        new_training.save()
        form = TrainingForm()
        messages.success(request, "Thee has't successfully did add training!")
    context = {
        "form": form,
    }
    return render(request, "add_training_view.html", context)


def add_diet_page(request):
    if not request.user.account.type == 'STAFF' or not request.user.account.type == 'DIETICIAN':
        messages.error(request, "Thee cannot access this page!")
        return redirect("pages:home-view")
    form = DietForm(request.POST or None, request.FILES)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.author = request.user
        new_training.save()
        form = DietForm()
        messages.success(request, "Thee has't successfully did add diet!")
    context = {
        "form": form,
    }
    return render(request, "add_diet_view.html", context)


@login_required(login_url='/landing')
def add_pass_to_cart_view(request, my_id):
    cart = request.user.cart
    passs = get_object_or_404(Pass, id=my_id)
    if not request.user.account.type == 'STAFF' and not request.user.account.type == 'TRAINER' and not request.user.account.type == 'DIETICIAN':
        if not cart.passs == passs:
            cart.passs = passs
            cart.save()
            messages.success(request, "Thee has't successfully did add passeth to cart.")
        else:
            messages.error(request, "Thee has't already did add this passeth to thy cart!")
    else:
        messages.error(request, "Thou art an employee, thee needeth not a passeth!")
    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_pass_from_cart_view(request, my_id):
    cart = request.user.cart
    passs = get_object_or_404(Pass, id=my_id)
    if cart.passs:
        cart.passs = None
        cart.save()
        messages.success(request, "Thee has't successfully did remove this passeth from cart.")
    else:
        messages.error(request, "Thee has't nay passeth in thy cart!")
    return redirect("accounts:cart-view")

@login_required(login_url='/landing')
def add_training_to_cart_view(request, my_id):
    cart = request.user.cart
    training = get_object_or_404(Training, id=my_id)
    if not training.author == request.user:
        if not request.user in training.bought.all():
            if not training in cart.trainings.all():
                cart.trainings.add(training)
                messages.success(request, "Thee has't successfully did add training to cart.")
            else:
                messages.error(request, "Thee has't already did add this training to thy cart!")
        else:
            messages.error(request, "Thee has't already hath bought this training!")
    else:
        messages.error(request, "Thee can't buyeth thy owneth training!")
    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_training_from_cart_view(request, my_id):
    cart = request.user.cart
    training = get_object_or_404(Training, id=my_id)
    if training in cart.trainings.all():
        cart.trainings.remove(training)
        messages.success(request, "Thee has't successfully did remove this training from cart.")
    else:
        messages.error(request, "Thee has't not this training in thy cart")
    return redirect("accounts:cart-view")

@login_required(login_url='/landing')
def add_diet_to_cart_view(request, my_id):
    cart = request.user.cart
    diet = get_object_or_404(Diet, id=my_id)
    if not diet.author == request.user:
        if not request.user in diet.bought.all():
            if not diet in cart.diets.all():
                cart.diets.add(diet)
                messages.success(request, "Thee has't successfully did add diet to cart.")
            else:
                messages.error(request, "Thee has't already did add this diet to thy cart!")
        else:
            messages.error(request, "Thee has't already hath bought this diet!")
    else:
        messages.error(request, "Thee can't buyeth thy owneth diet!")

    return redirect("accounts:cart-view")


@login_required(login_url='/landing')
def remove_diet_from_cart_view(request, my_id):
    cart = request.user.cart
    diet = get_object_or_404(Diet, id=my_id)
    if diet in cart.diets.all():
        cart.diets.remove(diet)
        messages.success(request, "Thee has't successfully did remove this diet from cart.")
    else:
        messages.error(request, "Thee has't not this diet in thy cart")
    return redirect("accounts:cart-view")
