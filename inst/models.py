from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group
from state.models import State

class InstitutionUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='institution_users')
    institution_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)  # Reference the State model
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
