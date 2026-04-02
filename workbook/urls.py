from django.urls import path
from . import views

urlpatterns = [
    path("", views.workbook_dashboard, name="workbook_dashboard"),
    path("faculty/<int:project_id>/", views.faculty_review_edit, name="faculty_review_edit"),
    path("student/<int:project_id>/", views.student_workbook_view, name="student_workbook_view"),
]