from django.urls import path
from state import views

urlpatterns = [
    path("", views.state_login, name='state_login'),
    path("dashboard", views.dashboard, name="state_dashboard"),
    path('register_institution/', views.register_institution, name='register_institution'),

]
