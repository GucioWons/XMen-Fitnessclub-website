from django.urls import path

from Accounts.views import dietician_page, trainer_page

app_name = "accounts"
urlpatterns = [
        path('dietician/<int:my_id>/', dietician_page, name='dietician-view'),
        path('trainer/<int:my_id>/', trainer_page, name='trainer-view'),
    ]