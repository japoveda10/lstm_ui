from rest_framework import serializers
from .models import EventLog, RunningCase

class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name']

class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'name', 'prefix', 'suffix']