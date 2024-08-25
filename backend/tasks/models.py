from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField()
    done = models.PositiveSmallIntegerField(blank=True)
