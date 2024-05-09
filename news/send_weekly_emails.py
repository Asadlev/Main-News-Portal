# scripts/send_weekly_emails.py
import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Post, Category, Subscription

def send_weekly_emails():
    start_date = datetime.datetime.now() - datetime.timedelta(days=7)
    end_date = datetime.datetime.now()
    categories = Category.objects.all()
    for category in categories:
        new_posts = Post.objects.filter(category=category, created_at__range=(start_date, end_date))
        for subscription in Subscription.objects.filter(category=category):
            user = subscription.user
            subject = f'Weekly News Digest for {category.name}'
            html_message = render_to_string('email/weekly_email.html', {'new_posts': new_posts})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'from@example.com', [user.email], html_message=html_message)
