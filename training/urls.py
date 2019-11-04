from django.urls import path
from .views import index, posts_page, sign_in

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts_page, name = 'posts_page'),
    path('sign/', sign_in, name = 'sign_in_page')
]