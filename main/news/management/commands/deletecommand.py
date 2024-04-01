from news.models import Post
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Команда которая удаляет новости'

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write()
        answer = input('Вы действительно хотите удалить все новости?(yes/no): ')

        if answer == 'yes':
            news = Post.objects.all()
            news.delete()
            self.stdout.write(self.style.SUCCESS(f'{answer} - Команда применена успешно! "%s"' % str(news)))
            return

        elif answer == 'no':
            self.stdout.write(self.style.SUCCESS(f'{answer} - Операция отменена'))  # в случае неправильного подтверждения, говорим, что в доступе отказано

        elif answer not in 'no' or answer not in 'yes':
            answer_else = input('Введите - yes или no!: ')
            if answer_else == 'yes':
                news = Post.objects.all()
                news.delete()
                self.stdout.write(self.style.SUCCESS(f'{answer_else} - Команда применена успешно! "%s"' % str(news)))
                return

            elif answer_else == 'no':
                self.stdout.write(self.style.ERROR(f'{answer_else} - Операция отменена'))  # в случае неправильного подтверждения, говорим, что в доступе отказано

        # else:
        #     self.stdout.write(self.style.ERROR('Операция прервана'))  # в случае неправильного подтверждения, говорим, что в доступе отказано



