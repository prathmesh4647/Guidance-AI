from django.db import models
from django.core.exceptions import ValidationError
from pgvector.django import VectorField

class Project(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
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

    screenshots = models.ImageField(
        upload_to='project_screenshots/',
        null=True,
        blank=True
    )

    documentation = models.FileField(
        upload_to='project_docs/',
        null=True,
        blank=True
    )

    evaluated_marks = models.FloatField(null=True, blank=True)

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

    def clean(self):
        # Ensure selected idea belongs to same team
        if self.final_idea.team != self.team:
            raise ValidationError("Selected idea does not belong to this team.")

    def __str__(self):
        return f"{self.title} - {self.team.name}"