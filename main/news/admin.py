from django.contrib import admin
from .models import Post, Category, PostCategory, Comment
from appointment.models import Appointment


# def nullfy_news(modeladmin, request, queryset):
#     queryset.update(author='', title='', text='')


# nullfy_news.short_news = 'Очистить новости'


# Создаем новый класс для представления товара в админке
# class PostAdmin(admin.ModelAdmin):
#     model = Post  # - Это необезательно, но тем не менее
#     # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
#     list_display = [
#         field.name for field in model._meta.get_fields()
#     ]  # генерируем список имён всех полей для более красивого отображения
#     # добавляем фильтры
#     list_filter = ('author', 'title')
#     # Добавляем поисковой фильтр в нашу админ панель
#     search_fields = ('author', 'title', 'category__name')
#     # очистить новости
#     actions = [nullfy_news]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'message')
    list_filter = ('client_name', 'message')
    search_fields = ('client_name', 'message')


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Appointment, AppointmentAdmin)

'''
    Разумеется, нужно убрать строчку с разрегистрацией товаров перед тем, как получить такой вывод. Здесь прошу заметить, мы использовали все поля. Однако, если вам нужны только какие-то конкретные поля, то можно оставить, например, только название, изменив код следующим образом:

from django.contrib import admin
from .models import Category, Product
 
 
# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price') # оставляем только имя и цену товара
 
# Register your models here.
 
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
'''

# filters-admin
'''
    Давайте дополним наши товары фильтрами, напоминаем, что главное действие сейчас ведётся в admin.py файле.
    list_filter = ('price', 'quantity', 'name') # добавляем примитивные фильтры в нашу админку
'''





