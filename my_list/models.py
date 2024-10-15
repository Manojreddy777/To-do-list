# models.py
from django.db import models

class Task(models.Model):
    taskname = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField()
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    status = models.BooleanField(default=False)  # Add this field for task status

    def __str__(self):
        return self.taskname
