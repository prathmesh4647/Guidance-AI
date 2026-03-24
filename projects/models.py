from django.db import models
from django.core.exceptions import ValidationError
from pgvector.django import VectorField
from django.conf import settings

class Project(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('revision', 'Needs Revision'),
        ('approved', 'Approved'),
    )

    team = models.OneToOneField(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name='project'
    )

    final_idea = models.ForeignKey(
        'ideas.Idea',
        on_delete=models.CASCADE,
        limit_choices_to={'status': 'approved'}
    )

    title = models.CharField(max_length=200)
    abstract = models.TextField()

    tech_stack = models.CharField(max_length=300)

    demo_video = models.URLField(null=True, blank=True)

    documentation = models.FileField(
        upload_to='project_docs/',
        null=True,
        blank=True
    )

    github_link = models.URLField(null=True, blank=True)

    evaluated_marks = models.FloatField(null=True, blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="liked_projects"
    )

    batch_year = models.IntegerField(default=2026)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    #Adding embeddings column having VectorField datatype  
    embedding = VectorField(dimensions=384, null=True, blank=True)
    similarity_score = models.FloatField(default=0.0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    evaluation_modeling = models.IntegerField(null=True, blank=True)
    evaluation_coding = models.IntegerField(null=True, blank=True)
    evaluation_testing = models.IntegerField(null=True, blank=True)
    evaluation_understanding = models.IntegerField(null=True, blank=True)
    evaluation_contribution = models.IntegerField(null=True, blank=True)
    evaluation_teamwork = models.IntegerField(null=True, blank=True)
    evaluation_presentation = models.IntegerField(null=True, blank=True)
    evaluation_documentation = models.IntegerField(null=True, blank=True)

    # This Function Calculates Total Marks
    def calculate_total(self):
        return sum([
            self.evaluation_modeling or 0,
            self.evaluation_coding or 0,
            self.evaluation_testing or 0,
            self.evaluation_understanding or 0,
            self.evaluation_contribution or 0,
            self.evaluation_teamwork or 0,
            self.evaluation_presentation or 0,
            self.evaluation_documentation or 0,
    ])

    def clean(self):
        # Ensure selected idea belongs to same team
        if self.final_idea.team != self.team:
            raise ValidationError("Selected idea does not belong to this team.")
        
    def save(self, *args, **kwargs):

        if self.final_idea:
           self.title = self.final_idea.title
           self.abstract = self.final_idea.abstract

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.team.name}"
    

class ProjectScreenshot(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='screenshots_list'
    )
    image = models.ImageField(upload_to='project_screenshots/')

    def __str__(self):
        return f"Screenshot for {self.project.title}"
    