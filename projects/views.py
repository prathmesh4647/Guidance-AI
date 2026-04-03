from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ProjectScreenshot
# Create your views here.

@login_required
def my_project(request):

    if request.user.role != "student":
        return redirect("login")

    team = request.user.student_teams.first()
    project = Project.objects.filter(team=team).first()

    if request.method == "POST":

        project.tech_stack = request.POST.get("tech_stack")
        project.github_link = request.POST.get("github_link")
        project.demo_video = request.POST.get("demo_video")
        project.documentation = request.FILES.get("documentation")

        project.save()

        # Handle multiple screenshots
        images = request.FILES.getlist("screenshots")

        if images:
            # clear old screenshots (optional)
            project.screenshots_list.all().delete()
 
            for img in images[:5]:  # max 5
                ProjectScreenshot.objects.create(
                    project=project,
                    image=img
                )
        
        if project.screenshots_list.count() < 1:
            return render(request, "error.html", {
                "message": "At least one screenshot is required."
        })

        return redirect("my_project")

    return render(request, "my_project.html", {"project": project})



from django.utils.timezone import now

@login_required
def evaluate_project(request, project_id):

    if request.user.role != "faculty":
        return redirect("login")

    project = get_object_or_404(Project, id=project_id)

    # Prevent re-evaluation after approval
    if project.status == "approved":
        return render(request, "error.html", {
            "message": "Project already evaluated and approved."
        })

    if request.method == "POST":

        project.evaluation_modeling = int(request.POST.get("modeling", 0))
        project.evaluation_coding = int(request.POST.get("coding", 0))
        project.evaluation_testing = int(request.POST.get("testing", 0))
        project.evaluation_understanding = int(request.POST.get("understanding", 0))
        project.evaluation_contribution = int(request.POST.get("contribution", 0))
        project.evaluation_teamwork = int(request.POST.get("teamwork", 0))
        project.evaluation_presentation = int(request.POST.get("presentation", 0))
        project.evaluation_documentation = int(request.POST.get("documentation", 0))

        # Calculate total
        project.evaluated_marks = project.calculate_total()

        action = request.POST.get("action")

        if action == "approve":
            project.status = "approved"
            project.approved_at = now()
        else:
            project.status = "revision"

        project.save()

        return redirect("faculty_projects")

    return render(request, "evaluate_project.html", {
        "project": project
    })

@login_required
def faculty_projects(request):

    if request.user.role != "faculty":
        return redirect("login")

    projects = Project.objects.filter(
        team__guide=request.user
    ).select_related("team").prefetch_related("screenshots_list")

    return render(request, "faculty_projects.html", {"projects": projects})


def showcase(request):

    projects = Project.objects.filter(
        status="approved"
    ).select_related("team", "team__guide").prefetch_related("likes")

    return render(request, "showcase.html", {"projects": projects})


def project_detail(request, project_id):

    project = Project.objects.select_related(
        "team", "team__guide"
    ).prefetch_related(
        "team__members",
        "screenshots_list",
        "likes"
    ).get(id=project_id)

    if project.status != "approved":
        return render(request, "error.html", {
            "message": "Project not available for public view."
        })

    return render(request, "project_detail.html", {"project": project})



from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model

User = get_user_model()

def like_project(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    # HARD BLOCK
    if not request.user.is_authenticated:
        return render(request, "error.html", {
            "message": "You need to login to like a project."
        })

    # Extra safety (optional but strong)
    if not isinstance(request.user, User):
        return render(request, "error.html", {
            "message": "Invalid user."
        })

    if request.user in project.likes.all():
        project.likes.remove(request.user)
    else:
        project.likes.add(request.user)

    return redirect("project_detail", project_id=project.id)


def leaderboard(request):

    projects = Project.objects.filter(status="approved")

    # Convert to list for sorting
    projects = list(projects)

    # Sort by final score (descending)
    projects.sort(key=lambda x: x.get_final_score(), reverse=True)

    return render(request, "leaderboard.html", {
        "projects": projects
    })