from django.urls import path

from Products.views import passes_page, add_pass_page, add_training_page, add_diet_page, bought_page

app_name = "products"
urlpatterns = [
        path('passes/', passes_page, name='passes-view'),
        path('bought/', bought_page, name='bought-view'),
        path('add-pass/', add_pass_page, name='add-pass-view'),
        path('add-training/', add_training_page, name='add-training-view'),
        path('add-diet/', add_diet_page, name='add-diet-view'),
    ]