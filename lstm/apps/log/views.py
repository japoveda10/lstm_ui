from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'log/index.html')

def step1(request):
    return render(request, 'log/step1.html')
