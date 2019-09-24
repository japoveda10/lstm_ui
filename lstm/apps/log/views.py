from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.log.forms import SelectLogForm

def index(request):
    return render(request, 'log/index.html')

def step1(request):
    if request.method == 'POST':
       form = SelectLogForm(request.POST)
       if form.is_valid():
           form.save()
       return redirect('log:index')
    else:
        form = SelectLogForm()

    return render(request, 'log/step1.html', {'form':form})

def about(request):
    return render(request, 'log/about.html')

def contact_us(request):
    return render(request, 'log/contact_us.html')
