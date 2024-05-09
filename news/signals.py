# signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to News Portal!'
        html_message = render_to_string('email/welcome_email.html', {'username': instance.username})
        send_mail(subject, 'Welcome to News Portal!', 'from@example.com', [instance.email], html_message=html_message)
