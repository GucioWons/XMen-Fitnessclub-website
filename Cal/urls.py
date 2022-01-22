from django.urls import path

from Cal.views import class_page, signed_page, calendar_page, join_view, leave_view, add_class_page

app_name = "cal"
urlpatterns = [
        path('calendar/', calendar_page, name='calendar-view'),
        path('your-classes/', signed_page, name='signed-view'),
        path('class/<int:my_id>/', class_page, name='class-view'),
        path('join/<int:my_id>/', join_view, name='join-view'),
        path('leave/<int:my_id>/', leave_view, name='leave-view'),
        path('add-class/', add_class_page, name='add-class-view'),
    ]