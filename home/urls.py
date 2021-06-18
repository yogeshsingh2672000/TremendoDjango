from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.login, name='home'),
    path('login', views.login, name='login'),
    path('student_register', views.student, name='student_register'),
    path('teacher_register', views.teacher, name='teacher_register'),
    path('form_submition', views.form_submition, name='form_submition'),
]
