from django.urls import path, include
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsDeleteView, NewsUpdateView, PostListView, \
    PostDetailView
from . import views
from django.views.decorators.cache import cache_page


app_name = 'news'

urlpatterns = [
    path('news/', PostListView.as_view(), name='news_ser'),
    path('new/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/detail', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    # path('noview/', IndexTime.as_view(), name='set_time'),
    # path('translateView/', IndexLanguage.as_view(), name='set_language'),
]