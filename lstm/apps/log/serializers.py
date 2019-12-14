#------------------------------------------------------------------------------
# LSTM UI Django Project
# By japoveda10
# serializers.py
# This file has classes that represent serializers
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from rest_framework import serializers
from apps.log.models import EventLog, RunningCase

#------------------------------------------------------------------------------
# Classes that represent serializers
#------------------------------------------------------------------------------

# Event Log Serializer
class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name', 'number_of_traces', 'number_of_events', 'number_of_activities', 'avg_activities_per_trace', 'max_activities_per_trace', 'mean_duration', 'max_duration', 'sf', 'tv']

# Running Case Serializer
class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'name', 'prefix', 'suffix']