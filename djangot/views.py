from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def story(request):
    return render(request, 'story.html')

def random(request):
    return render(request, 'random.html')

def admin(request):
    return HttpResponse('admin')