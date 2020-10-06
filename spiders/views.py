from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'spiders/index.html')


def pages(request):
    return render(request, 'spiders/pages.html')
