from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_notice, name='create_notice'),
    path('student/', views.student_notices, name='student_notices'),
]