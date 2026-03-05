from django.urls import path
from .views import submit_idea, faculty_ideas
from .views import idea_generator


urlpatterns = [
    path("submit/", submit_idea, name="submit_idea"),
    path("faculty/", faculty_ideas, name="faculty_ideas"),
    path("generate/", idea_generator, name="idea_generator"),
]