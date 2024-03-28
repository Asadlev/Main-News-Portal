from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.core.cache import cache  # Импортируем наш кэш
from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import NewsFilter
from .forms import NewsForm
from .models import Post
# Create your views here.


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    ordering = '-id'
    paginate_by = 2

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




