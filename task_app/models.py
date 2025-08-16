from django.db import models

# Create your models here.

class Task(models.Model):
    status_choice = [("in_progress", "In progress"), ("done", "Done"), ("postponed", "Postponed")]
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=status_choice, default="in_progress")

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    

