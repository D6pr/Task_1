from django_setup import *
from main_app.models import User, Role

user_role = Role.objects.create(name = "user")

user = User.objects.create(name = "Толя",
                           email = "tolya@gmail.com",
                           role = user_role)

user.save()