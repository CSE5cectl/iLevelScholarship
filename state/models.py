from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
class Scholarship(models.Model):
    state = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    application_deadline = models.DateField()
    scholarship_amount = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return self.name

