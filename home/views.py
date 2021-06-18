from django.shortcuts import render, HttpResponse
from home.models import StudentRegister
from home.models import TeacherRegister

# Create your views here.


def login(request):
    return render(request, 'login.html')


def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        batch_enrolled = request.GET.get('batch')
        student = StudentRegister(
            name=name, email=email, gender=gender, address=address, batch_enrolled=batch_enrolled)

        def __str__(self):
            return self.name

    return render(request, 'student_register.html')


def teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        batch_handling = request.POST.get('batch')
        teacher = TeacherRegister(name=name, email=email, phone=phone,
                                  gender=gender, address=address, batch_handling=batch_handling)

        def __str__(self):
            return self.name

    return render(request, 'teacher_register.html')


def form_submition(request):
    return render(request, 'form_submition.html')
