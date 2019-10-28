from django.shortcuts import render
from .models import Sport

# Create your views here.
def index(request):
    sports = Sport.objects.all()
    context = {'sports': sports}
    return render(request, 'layout/basic.html', context)
