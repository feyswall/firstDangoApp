
from django.urls import path
from . import views

urlpatterns = [
    path('hello/<int:id>/', views.say_hello),
    path('for-my-student/', views.forMyStudent, name='about')
]
