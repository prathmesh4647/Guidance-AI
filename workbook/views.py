from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from .models import Review, ReviewQuestion, ReviewResponse, WorkbookSection

# Create your views here.




# STUDENT + FACULTY VIEW (COMMON DASHBOARD)
@login_required
def workbook_dashboard(request):

    # 🔥 STUDENT VIEW
    if request.user.role == "student":
        project = Project.objects.filter(team__members=request.user).first()

        if not project:
            return render(request, "error.html", {
                "message": "No project assigned."
            })

        projects = [project]

    # 🔥 FACULTY VIEW (MULTIPLE PROJECTS)
    elif request.user.role == "faculty":
        projects = Project.objects.filter(team__guide=request.user)

        if not projects.exists():
            return render(request, "error.html", {
                "message": "No projects assigned."
            })

    else:
        projects = []

    return render(request, "workbook_dashboard.html", {
        "projects": projects
    })




@login_required
def student_workbook_view(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    # Ensure student belongs to this project
    if request.user not in project.team.members.all():
        return render(request, "error.html", {
            "message": "Access denied."
        })

    responses = ReviewResponse.objects.filter(
        project=project
    ).select_related("question__review")

    return render(request, "student_workbook_view.html", {
        "responses": responses,
        "project": project
    })





# FACULTY EDIT VIEW
@login_required
def faculty_review_edit(request, project_id):

    if request.user.role != "faculty":
        return redirect("login")

    project = get_object_or_404(Project, id=project_id)

    responses = ReviewResponse.objects.filter(project=project).select_related("question__review")

    if request.method == "POST":
        for r in responses:
            r.remark = request.POST.get(f"remark_{r.id}")
            r.is_completed = True if request.POST.get(f"complete_{r.id}") else False
            r.save()

        return redirect("workbook_dashboard")

    return render(request, "faculty_review_edit.html", {
        "responses": responses,
        "project": project
    })