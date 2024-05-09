from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.core.cache import cache  # Импортируем наш кэш
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .filters import NewsFilter
from .forms import NewsForm
from .is_authefication_file import IsAuthenticatedOrReadOnly
from .models import Post
from django.http.response import HttpResponse  # импортируем респонс для проверки текста
from django.utils.translation import gettext  # импортируем функцию для перевода
from django.utils.translation import activate, get_supported_language_variant
from main.settings import LANGUAGE_SESSION_KEY
import pytz  #  импортируем стандартный модуль для работы с часовыми поясами
from django.utils import timezone
from rest_framework import generics, permissions
from .serializers import PostSerializer
# Create your views here.


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    ordering = '-id'
    paginate_by = 4

    # Функция для фильтра
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит обьект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Вывод даты и времени
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    context_object_name = 'new'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'title-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

         # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'title-{self.kwargs["pk"]}', obj)

        return obj


    """ '''
        И вроде бы всё готово. Если объекта нет в кэше, то мы берём его из БД и кэшируем, а если есть, то сразу берём из кэша и возвращаем. Но! Давайте узнаем, что же будет происходить сейчас (не забудьте убрать кэширование из urls.py, иначе получится очень грязно!).

        Зайдите на кэшируемую страницу и попробуйте через админ-панель что-либо в ней поменять, а потом обновите страницу.

        И тут-то вас ждёт сюрприз! Весь нюанс в том, что теперь ничего не поменяется вообще… Никогда... Ведь мы не установили реакцию на редактирование объекта. Когда объект меняется его надо удалять из кэша, чтобы ключ сбрасывался и больше не находился.

        Давайте этим и займёмся, переопределим метод save в sample_app/models.py.

        from django.core.cache import cache
        
        
        class Product(models.Model):
            name = models.CharField(max_length=200)
            price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])
            quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
            category = models.ForeignKey('Category', on_delete=models.CASCADE)
        
            def __str__(self):
                return f'{self.name} {self.quantity}'
        
            def get_absolute_url(self): # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
                return f'/products/{self.id}'
        
            def save(self, *args, **kwargs):
                super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
                cache.delete(f'product-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его
        '''
"""


class NewsCreateView(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'
    success_url = reverse_lazy('news:news_list')


class NewsUpdateView(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_update.html'
    success_url = reverse_lazy('news:news_list')


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news:news_list')


class IndexTime(View):
    def get(self, request):
        curent_time = timezone.now()

        # .  Translators: This message appears on the home page only
        models = Post.objects.all()

        context = {
            'models': models,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }

        return HttpResponse(render(request, 'index.html', context))

    #  по пост-запросу будем добавлять в сессию часовой пояс, который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('news:set_time')


# class IndexLanguage(View):
#     def get(self, request):
#         string = gettext('Hello, World')
#         return HttpResponse(string)

''' Пишем сериализатор для модели Post '''


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

# def articles_and_news_list(request):
#     # Получаем как статьи, так и новости
#     articles_and_news = Post.objects.all()
#
#     # Преобразуем QuerySet в список словарей
#     data = {
#         'articles_and_news': list(articles_and_news.values())
#     }
#
#     return JsonResponse(data)

