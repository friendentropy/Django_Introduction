from django.shortcuts import render
from django.http import HttpResponse


def karibu(request):
    return HttpResponse("<h1>Karibu Django</h1>")


def home(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def gallery(request):
    return render(request, 'gallery.html')


def contactus(request):
    return render(request, 'contactus.html')
