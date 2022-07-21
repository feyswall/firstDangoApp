from email.policy import default
from operator import index
from random import choices
from django.db import models
from django.forms import CharField, DateField, IntegerField

# Create your models here.
class User(models.Model):
    GENDER = [
        ('M', "male"),
        ('F', 'female')
    ]

    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    gender = models.CharField(max_length =255, choices=GENDER )
    date_of_birth = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=True)  


NORMAL_USER = 'N'
SUPER_USER = 'S'
TEACHER_USER = 'T'
STUDENT_USER = 'S'

USER_ROLES = [
    ( NORMAL_USER, 'guest'),
    ( SUPER_USER, 'super'),
    ( TEACHER_USER, 'teacher'),
    ( STUDENT_USER, 'student')
]

class role(models.Model):
    roleName = models.CharField(max_length=255, choices=USER_ROLES, default=NORMAL_USER )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    
    

    