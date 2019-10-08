from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.log.forms import SelectLogForm
from rest_framework import viewsets
from .models import EventLog
from .serializers import EventLogSerializer

def index(request):
    if request.method == 'POST':
       form = SelectLogForm(request.POST)
       if form.is_valid():
           form.save()
       return redirect('log:index')
    else:
        form = SelectLogForm()

    return render(request, 'log/index.html', {'form':form})

def about(request):
    return render(request, 'log/about.html')

def contact_us(request):
    return render(request, 'log/contact_us.html')

class EventLogView(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
