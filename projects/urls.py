from django.urls import path
from .views import my_project
from .views import evaluate_project
from .views import faculty_projects

urlpatterns = [
    path("my-project/", my_project, name="my_project"),
    path("evaluate/<int:project_id>/", evaluate_project, name="evaluate_project"),
    path("faculty-projects/", faculty_projects, name="faculty_projects"),
]