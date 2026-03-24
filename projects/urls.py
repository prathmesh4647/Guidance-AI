from django.urls import path
from .views import my_project
from .views import evaluate_project
from .views import faculty_projects
from .views import like_project
from .views import showcase
from .views import project_detail

urlpatterns = [
    path("my-project/", my_project, name="my_project"),
    path("evaluate/<int:project_id>/", evaluate_project, name="evaluate_project"),
    path("faculty-projects/", faculty_projects, name="faculty_projects"),
    path("like/<int:project_id>/", like_project, name="like_project"),
    path("showcase/", showcase, name="showcase"),
    path('showcase/<int:project_id>/', project_detail, name='project_detail'),
]