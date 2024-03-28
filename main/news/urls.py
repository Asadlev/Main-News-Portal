from django.urls import path, include
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsDeleteView, NewsUpdateView
from . import views
from django.views.decorators.cache import cache_page


app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/detail', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
]