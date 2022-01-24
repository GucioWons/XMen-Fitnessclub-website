from django.urls import path

from Products.views import passes_page, add_pass_page, add_training_page, add_diet_page, bought_page, \
        add_pass_to_cart_view, remove_pass_from_cart_view, remove_training_from_cart_view, add_training_to_cart_view, \
        add_diet_to_cart_view, remove_diet_from_cart_view

app_name = "products"
urlpatterns = [
        path('passes/', passes_page, name='passes-view'),
        path('bought/', bought_page, name='bought-view'),
        path('add-pass/', add_pass_page, name='add-pass-view'),
        path('add-training/', add_training_page, name='add-training-view'),
        path('add-diet/', add_diet_page, name='add-diet-view'),
        path('add-pass-to-cart/<int:my_id>/', add_pass_to_cart_view, name='add-pass-to-cart-view'),
        path('remove-pass-from-cart/<int:my_id>/', remove_pass_from_cart_view, name='remove-pass-from-cart-view'),
        path('add-training-to-cart/<int:my_id>/', add_training_to_cart_view, name='add-training-to-cart-view'),
        path('remove-training-from-cart/<int:my_id>/', remove_training_from_cart_view, name='remove-training-from-cart-view'),
        path('add-diet-to-cart/<int:my_id>/', add_diet_to_cart_view, name='add-diet-to-cart-view'),
        path('remove-diet-from-cart/<int:my_id>/', remove_diet_from_cart_view, name='remove-diet-from-cart-view'),
    ]