from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.log.forms import SelectLogForm
from apps.log.forms import SelectTrainedModelForm
from apps.log.forms import SelectPostProcessingTechniqueForm
from rest_framework import viewsets
from .models import EventLog
from .serializers import EventLogSerializer

def index(request):
    if request.GET.get('Execute All'):
        return render(request, 'log/results.html')
    elif request.GET.get('Predict'):
        selectedLog = request.GET['log']
        trainedModelForm = SelectTrainedModelForm()
        postProcessingTechniqueForm = SelectPostProcessingTechniqueForm()
        return render(request, 'log/predict.html', { "selectedLog": selectedLog, "trained_models_form": trainedModelForm, "postprocessing_technique_form": postProcessingTechniqueForm })
    form = SelectLogForm()
    return render(request, 'log/index.html', {'form':form})

def about(request):
    return render(request, 'log/about.html')

def contact_us(request):
    return render(request, 'log/contact_us.html')

class EventLogView(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
