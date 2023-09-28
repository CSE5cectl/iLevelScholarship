from django.urls import path
from inst import views

urlpatterns = [
    path("", views.login_institution_user, name='login_institution_user'),
    path('institution_dashboard/', views.institution_dashboard, name='institution_dashboard'),
    
]
