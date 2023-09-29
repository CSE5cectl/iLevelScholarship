from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import InstitutionUser
from student.models import ScholarshipApplicationNotification, ScholarshipApplication, Student

def login_institution_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check if the user belongs to the 'Institution' group
            if user.groups.filter(name='Institution').exists():
                login(request, user)
                return redirect('institution_dashboard') 
            else:
                return render(request, 'inst_login.html', {'error_message': 'Invalid login credentials.'})

    return render(request, 'inst_login.html') 


def institution_dashboard(request):
    institution = InstitutionUser.objects.get(user=request.user)
    unread_notifications = ScholarshipApplicationNotification.objects.filter(receiver=institution.user, is_read=False)
    received_scholarships = ScholarshipApplication.objects.filter(institution=institution)
    student_names = Student.objects.values_list('name', flat=True)

    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        action = request.POST.get('action')  # 'approve' or 'reject'

        if application_id and action:
            application_notification = ScholarshipApplicationNotification.objects.get(id=application_id)
            if action == 'approve':
                application_notification.approved = True
                application_notification.rejected = False 
                application_notification.is_read=True
                application_notification.message = "Insitiution approved"
                application_notification.save()
                

            elif action == 'reject':
                application_notification.rejected = True
                application_notification.approved = False  
                application_notification.is_read=True
                application_notification.message = "Insitiution rejected"
                application_notification.save()

            return redirect('institution_dashboard')

        
    context = {
        'institution': institution,
        'unread_notifications': unread_notifications,
        'received_scholarships': received_scholarships,
        'names': student_names,
    }

    return render(request, 'institution_dashboard.html', context)