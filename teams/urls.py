from django.urls import path
from .views import manage_teams
from .views import add_student_to_team
from .views import remove_student
from .views import delete_team
from .views import edit_team

urlpatterns = [
    path('manage/', manage_teams, name='manage_teams'),
    path('add/<int:team_id>/', add_student_to_team, name='add_student'),
    path('remove/<int:team_id>/<int:student_id>/', remove_student, name='remove_student'),
    path('delete/<int:team_id>/', delete_team, name='delete_team'),
    path('edit/<int:team_id>/', edit_team, name='edit_team'),
]
