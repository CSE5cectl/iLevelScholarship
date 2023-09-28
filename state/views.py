from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Scholarship, State
from django.contrib.auth.models import Group
from inst.models import InstitutionUser
from django.contrib.auth.models import User


def state_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('state_dashboard')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'state_login.html') 

def dashboard(request):
    state_scholarships = Scholarship.objects.filter(state=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        eligibility = request.POST['eligibility']
        deadline = request.POST['deadline']
        amount = request.POST['amount']

        scholarship = Scholarship(state=request.user, name=name, eligibility_criteria=eligibility, application_deadline=deadline, scholarship_amount=amount)
        scholarship.save()

        return redirect('state_dashboard') 
    context = {
        'state_scholarships': state_scholarships,
    }
    return render(request, 'state_dashboard.html', context) 

def register_institution(request):
    states = State.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        institution_name = request.POST['institution_name']
        state_id = request.POST['state']  
        contact_number = request.POST['contact_number']
        address = request.POST['address']
        website = request.POST['website']

        user = User.objects.create_user(username=username, password=password)
        
        # Create a new InstitutionUser instance and associate it with the user
        institution_user = InstitutionUser(
            user=user,
            institution_name=institution_name,
            state=State.objects.get(pk=state_id), 
            contact_number=contact_number,
            address=address,
            website=website
        )
        institution_user.save()

        group, created = Group.objects.get_or_create(name='Institution')
        user.groups.add(group)

        return redirect('register_institution')

    return render(request, 'institution_registration.html', {'states': states})