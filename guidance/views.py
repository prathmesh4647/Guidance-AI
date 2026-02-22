from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def board(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'base.html')