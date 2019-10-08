from django.db import models

class Log(models.Model):
    name = models.CharField(max_length=50)
    number_of_traces = models.IntegerField()
    number_of_events = models.IntegerField()
    number_of_activities = models.IntegerField()

class EventLog(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name