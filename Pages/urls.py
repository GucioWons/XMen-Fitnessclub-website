from django.urls import path

from Pages.views import landing_page, home_page, login_page, register_page

app_name = "pages"
urlpatterns = [
        path('', home_page, name='home-view'),
        path('login/', login_page, name='login-view'),
        path('register/', register_page, name='register-view'),
        path('landing/', landing_page, name='landing-view'),
        #path('logout/', logout_view, name='logout-view'),
        #path('settings/', settings_page, name='settings-page'),
    ]