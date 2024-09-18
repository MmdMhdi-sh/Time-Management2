from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=False)
    done = models.PositiveSmallIntegerField(blank=True, null=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.title}"