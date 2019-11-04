from django.shortcuts import render
from .models import Sport, Post

# Create your views here.
def index(request):
    return render(request, 'training/index.html')

def posts_page(request):
    sports = Sport.objects.all()
    posts = Post.objects.all()
    context = {'sports': sports, 'posts': posts}
    return render(request, 'training/all_posts.html', context)


def sign_in(request):
    return render(request, 'training/sign_in.html')