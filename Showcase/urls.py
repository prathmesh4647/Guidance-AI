from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showcase),
    path('<int:project_id>/', views.viewProject, name='project_detail'),
]