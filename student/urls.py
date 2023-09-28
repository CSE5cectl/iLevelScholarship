from django.urls import path
from student import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.student_login, name='student_login'),
    path("register/", views.register_student, name="register_student"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path('apply/<int:scholarship_id>/', views.apply_scholarship, name='apply_scholarship'),
    path("get_institutions/", views.get_institutions, name='get_institutions'),
    path("logout/", views.student_logout, name='student_logout'),
]
