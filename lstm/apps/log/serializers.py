from rest_framework import serializers
from .models import EventLog

class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ('id', 'url', 'name')