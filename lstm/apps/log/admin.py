from django.contrib import admin
from apps.log.models import EventLog, RunningCase

admin.site.register(EventLog)
admin.site.register(RunningCase)
