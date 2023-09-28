from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import *
from state.models import State
from django.contrib.auth.models import Group
from state.models import Scholarship
from django import forms
from inst.models import InstitutionUser

class StateSelectionForm(forms.Form):
    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        label='Select Your State of Study',
        widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-white'}),
    )

class ScholarshipApplicationForm(forms.Form):
    application_text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-white', 'rows': 5}),
        label='Write Your Scholarship Application'
    )

    institution = forms.ModelChoiceField(
        queryset=InstitutionUser.objects.all(),
        label='Select Your Institution',
        widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-white'}),
    )


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')  
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'student_login.html', {'error_message': error_message})

    return render(request, 'student_login.html')

def register_student(request):
    states = State.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        address = request.POST['address']
        home_state_id = request.POST['home_state']
        password = request.POST['password']

        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            error_message = "A user with this email address already exists."
            return render(request, 'student_registration.html', {'states': states, 'error_message': error_message})

        user = User.objects.create_user(username=email, email=email, password=password, first_name = name)

        student_group, created = Group.objects.get_or_create(name='Student')
        user.groups.add(student_group)

        # Create a new Student instance and associate it with the user
        student = Student(
            user=user,
            name=name,
            username=email,
            email=email,
            contact_number=contact_number,
            address=address,
            home_state=State.objects.get(pk=home_state_id),  # Get the State object based on home_state_id
        )
        student.save()

        return redirect("student_login")

    return render(request, 'student_registration.html', {'states': states})

def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    home_state = student.home_state.user
    scholarships = Scholarship.objects.filter(state=home_state)
    notifications = ScholarshipApplicationNotification.objects.filter(
        scholarship_application__student=student.user,
    )
    context = {
        'student': student,
        'scholarships': scholarships,
        'notifications': notifications
    }

    return render(request, 'student_dashboard.html', context)


def apply_scholarship(request, scholarship_id):
    scholarship = Scholarship.objects.get(pk=scholarship_id)
    state_form = StateSelectionForm()
    
    if request.method == 'POST':
        form = ScholarshipApplicationForm(request.POST)
        
        if form.is_valid():
            selected_institution = form.cleaned_data['institution']
            application = ScholarshipApplication(
                student=request.user,
                scholarship=scholarship,
                institution=selected_institution,
                application_text=form.cleaned_data['application_text']
            )
            application.save()
            messages.success(request, 'Your scholarship application was submitted successfully.')

            notification = ScholarshipApplicationNotification(
                receiver=selected_institution.user, 
                sender=request.user,
                scholarship_application=application,
            )
            notification.save()
            return redirect('student_dashboard')
    else:
        form = ScholarshipApplicationForm() 
        
    context = {
        'scholarship': scholarship,
        'state_form': state_form,  
        'form': form, 
    }
    
    return render(request, 'student_apply.html', context)

def get_institutions(request):
    if request.method == 'GET':
        state_id = request.GET.get('state_id')
        institutions = InstitutionUser.objects.filter(state=state_id).values('id', 'institution_name')

        # Convert the queryset to a list of dictionaries
        institution_list = list(institutions)
        return JsonResponse(institution_list, safe=False)

def student_logout(request):
    logout(request)
    return render(request, 'student_login.html')