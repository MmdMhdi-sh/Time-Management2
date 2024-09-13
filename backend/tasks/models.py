from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    done = models.PositiveSmallIntegerField(blank=True)
