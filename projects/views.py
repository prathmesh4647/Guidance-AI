from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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