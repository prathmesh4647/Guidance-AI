from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Idea

# Create your views here.
@login_required
def submit_idea(request):
    if request.user.role != 'student':
        return redirect('login')
    
    idea_count = Idea.objects.filter(student=request.user).count()

    if idea_count >= 3:
        return render(request, 'idea_limit.html')
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        abstract = request.POST.get("abstract")
        ppt = request.FILES.get('ppt')

        Idea.objects.create(
            student = request.user,
            title = title,
            description=description,
            abstract=abstract,
            ppt=ppt
        )

        return redirect('student_dashboard')
    
    return render(request,"submit_idea.html")