from django.db import models
from state.models import State, Scholarship
from django.contrib.auth.models import User
from inst.models import InstitutionUser

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True)  
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    home_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='students')
    
    def __str__(self):
        return self.name
    
class ScholarshipApplication(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    application_text = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    institution = models.ForeignKey(InstitutionUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username}'s Application for {self.scholarship.name}"
    
class ScholarshipApplicationNotification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    scholarship_application = models.ForeignKey(ScholarshipApplication, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # New field to track approval status
    rejected = models.BooleanField(default=False)  # New field to track rejection status

    def __str__(self):
        return f"Notification for {self.scholarship_application}"
    

