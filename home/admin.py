from django.contrib import admin
from home.models import StudentRegister
from home.models import TeacherRegister

# Register your models here.

admin.site.register(StudentRegister)
admin.site.register(TeacherRegister)
