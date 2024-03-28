from django.urls import path
from .views import AppointmentView
from django.views.decorators.cache import cache_page


app_name = 'appointment'

urlpatterns = [
    path('', AppointmentView.as_view(), name='make_appointment'),
]
