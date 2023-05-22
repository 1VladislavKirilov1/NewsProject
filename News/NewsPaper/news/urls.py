from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, \
    ArticleDelete

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/search/', PostSearch.as_view()),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view()),

    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pl>/edit/', ArticleUpdate.as_view(), name='article_create'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),


]