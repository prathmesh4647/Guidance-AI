from django.urls import path
from .views import submit_idea, faculty_ideas

urlpatterns = [
    path("submit/", submit_idea, name="submit_idea"),
    path("faculty/", faculty_ideas, name="faculty_ideas"),
]