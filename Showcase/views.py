from django.shortcuts import render, get_object_or_404
from .models import projectInfo

# Create your views here.
def showcase(request):
    projects = projectInfo.objects.all()
    return render(request, 'showcase.html', {'projects': projects})

def viewProject(request, project_id):
    project = get_object_or_404(projectInfo, pk= project_id)
    return render(request, 'viewProject.html', {'project':project})



