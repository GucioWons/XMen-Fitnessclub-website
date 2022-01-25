from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from Accounts.models import Account, Order
from Cal.models import Class
from Products.models import Diet, Training


@login_required(login_url='/landing')
def dietician_page(request, my_id):
    obj = get_object_or_404(User, account__id=my_id)
    if not obj.account.type == 'DIETICIAN':
        messages.error(request, "There is no dietician with that id!")
        return redirect("pages:home-view")
    queryset = Diet.objects.filter(author=obj)
    context = {
        'object': obj,
        'queryset': queryset
    }
    return render(request, "dietician_view.html", context)

@login_required(login_url='/landing')
def trainer_page(request, my_id):
    obj = get_object_or_404(User, account__id=my_id)
    if not obj.account.type == 'TRAINER':
        messages.error(request, "There is no trainer with that id!")
        return redirect("pages:home-view")
    classes = Class.objects.filter(trainer=obj, date__gt=timezone.now())
    trainings = Training.objects.filter(author=obj)
    context = {
        'object': obj,
        'classes': classes,
        'trainings': trainings
    }
    return render(request, "trainer_view.html", context)

def trainers_page(request):
    queryset = User.objects.filter(account__type='TRAINER')
    context = {
        'queryset': queryset
    }
    return render(request, "trainers_view.html", context)

def dieticians_page(request):
    queryset = User.objects.filter(account__type='DIETICIAN')
    context = {
        'queryset': queryset
    }
    return render(request, "dieticians_view.html", context)

@login_required(login_url='/landing')
def cart_page(request):
    cart = request.user.cart
    cost = 0
    passs = None
    diets = None
    trainings = None
    if cart.passs:
        passs = cart.passs
        cost = cost + passs.cost
    if cart.diets:
        diets = cart.diets.all()
        for diet in diets:
            cost = cost + diet.cost
    if cart.trainings:
        trainings = cart.trainings.all()
        for training in trainings:
            cost = cost + training.cost
    context = {
        'pass': passs,
        'diets': diets,
        'trainings': trainings,
        'cost': cost
    }
    return render(request, "cart_view.html", context)

def order_view(request):
    cart = request.user.cart
    cost = 0
    if cart.passs:
        passs = cart.passs
        cost = cost + passs.cost
    if cart.diets:
        for diet in cart.diets.all():
            cost = cost + diet.cost
            diet.bought.add(request.user)
    if cart.trainings:
        for training in cart.trainings.all():
            cost = cost + training.cost
            training.bought.add(request.user)
    if not cost == 0:
        order = Order.objects.create(username=request.user.username, cost=cost)
        order.trainings.set(cart.trainings.all())
        order.diets.set(cart.diets.all())
        order.passs = cart.passs
        order.save()
        cart.trainings.clear()
        cart.diets.clear()
        cart.passs = None
        cart.save()
        messages.success(request, "Your order has been placed!")
        return redirect("pages:home-view")
    else:
        messages.error(request, "Your cart is empty!")
        return redirect("accounts:cart-view")