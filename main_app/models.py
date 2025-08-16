from django.db import models

# Create your models here.

class Role(models.Model):
    role_choices = [("admin", "Admin"), ("user", "User")]
    name = models.CharField(max_length=50, choices=role_choices, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.name} ({self.role})"