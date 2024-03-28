from news.models import Post
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Команда которая очищает атрибуты новостей'
    
    def handle(self, *args, **options):
        for new in Post.objects.all():
            new.user = ''
            new.title = ''
            new.text = ''
            new.save()
            
            self.stdout.write(self.style.SUCCESS('Команда применена успешно! "%s"' % str(new)))


