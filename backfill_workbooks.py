import os
import django
import sys

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guidance.settings')
django.setup()

from projects.models import Project
from workbook.models import ReviewQuestion, ReviewResponse

def backfill():
    projects = Project.objects.all()
    all_questions = ReviewQuestion.objects.all()
    
    print(f"Found {projects.count()} projects and {all_questions.count()} questions. Starting backfill...")

    for project in projects:
        created_count = 0
        try:
            for q in all_questions:
                # Create a blank response linking the project to every question
            
                response, created = ReviewResponse.objects.get_or_create(
                    project=project, 
                    question=q
                )
                if created:
                    created_count += 1
                    
            print(f"✅ Project '{project.title}': Added {created_count} tracking questions.")
            
        except Exception as e:
             print(f"❌ Error on Project '{project.title}': {e}")

if __name__ == "__main__":
    backfill()
