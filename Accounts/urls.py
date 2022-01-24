from django.urls import path

from Accounts.views import dietician_page, trainer_page, cart_page, order_view, trainers_page, dieticians_page

app_name = "accounts"
urlpatterns = [
        path('dietician/<int:my_id>/', dietician_page, name='dietician-view'),
        path('trainer/<int:my_id>/', trainer_page, name='trainer-view'),
        path('cart/', cart_page, name='cart-view'),
        path('order/', order_view, name='order-view'),
        path('trainers/', trainers_page, name='trainers-view'),
        path('dieticians/', dieticians_page, name='dieticians-view'),
    ]