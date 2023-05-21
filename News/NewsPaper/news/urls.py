from django.urls import path
from .views import PostList, PostDetail, PostSearch


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('', PostSearch.as_view()),
]