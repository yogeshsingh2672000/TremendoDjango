from django.db import models

# Create your models here.


class StudentRegister(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=50)
    address = models.TextField()
    batch_enrolled = models.CharField(max_length=50)


class TeacherRegister(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    address = models.TextField()
    batch_handling = models.CharField(max_length=50)
