from django.contrib import admin
from apps.log.models import Log
from apps.log.models import EventLog

admin.site.register(Log)
admin.site.register(EventLog)
