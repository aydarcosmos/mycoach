from django.urls import path
from .views import index, posts_page

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts_page, name = 'posts_page'), 
]