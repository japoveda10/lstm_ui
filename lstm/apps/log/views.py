from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apps.log.forms import SelectLogForm
from apps.log.forms import SelectTrainedModelForm
from apps.log.forms import SelectPostProcessingTechniqueForm
from apps.log.forms import SelectRunningCaseForm
from rest_framework import viewsets
from .models import EventLog, RunningCase
from apps.log.serializers import EventLogSerializer, RunningCaseSerializer
import json

json_data = open('./static/prefixes.json')   
data1 = json.load(json_data) # deserialize
data2 = json.dumps(data1)
json_items = data1['collection']['items']
json_data.close()

def index(request):
    if request.GET.get('Execute All'):
        return render(request, 'log/results.html')
    elif request.GET.get('Predict'):
        selectedLog = request.GET['log']
        trainedModelForm = SelectTrainedModelForm()
        postProcessingTechniqueForm = SelectPostProcessingTechniqueForm()
        runningCasesForm = SelectRunningCaseForm()
        return render(request, 'log/predict.html', { "selectedLog": selectedLog, "trained_models_form": trainedModelForm, "postprocessing_technique_form": postProcessingTechniqueForm, "data": json_items, "running_cases_form": runningCasesForm })
    
    elif request.GET.get('Show Results'):
        return render(request, 'log/results.html')
    form = SelectLogForm()
    return render(request, 'log/index.html', {'form':form})

def about(request):
    return render(request, 'log/about.html')

def contact_us(request):
    return render(request, 'log/contact_us.html')

def results(request):
    return render(request, 'log/results.html')

def get_data(request):
    data = {
        'log_data': [41, 26, 57, 47, 49, 40, 67, 68, 24, 26],
        'label_data': ['2', '3', '4', '5', '6', '7'],
    }

    return JsonResponse(data)

class EventLogViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows event logs to be viewed or edited
    '''
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer

class RunningCaseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows running cases to be viewed or edited
    '''
    queryset =RunningCase.objects.all()
    serializer_class = RunningCaseSerializer
