from django.urls import path
from .views import submit_idea, faculty_ideas
from .views import idea_generator
from .views import approve_idea, reject_idea
from .views import my_ideas
from .views import edit_idea
from .views import student_ideas

urlpatterns = [
    path("submit/", submit_idea, name="submit_idea"),
    path("faculty/", faculty_ideas, name="faculty_ideas"),
    path("generate/", idea_generator, name="idea_generator"),
    path("approve/<int:idea_id>/", approve_idea, name="approve_idea"),
    path("reject/<int:idea_id>/", reject_idea, name="reject_idea"),
    path("my-ideas/", my_ideas, name="my_ideas"),
    path("edit/<int:idea_id>/", edit_idea, name="edit_idea"),
    path("my-ideas/", student_ideas, name="student_ideas"),
]