from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    yearofstudy = models.CharField(max_length=10)
    usertype = models.CharField(max_length=20)
    # ... other fields and methods ...
