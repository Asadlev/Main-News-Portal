from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Appointment
from django.core.mail import send_mail, mail_managers, mail_admins


# Отправка писем по электронной почте
class AppointmentView(View):
    # Обрабатываем get-запрос
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment/index.html')

    # Обрабатываем post-запрос
    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], "%Y-%m-%d"),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name}: {appointment.date.strftime("%S-%m-%d")}',
            message=appointment.message,
            from_email='imaralievasadbek@yandex.ru',
            recipient_list=['imaraliev.kg2005@gmail.com', 'ozodbekibragimov369@gmail.com', 'imyaminov04@gmail.com']

        )

        return redirect('appointment:make_appointment')

