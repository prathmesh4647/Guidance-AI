from django.urls import path
from .views import my_project

urlpatterns = [
    path("my-project/", my_project, name="my_project"),
]