from django_setup import *
from task_app.models import Task

task = Task.objects.create(title="Купити Spotify преміум", description = "Бо хочу", status = "postponed")

task.save()
