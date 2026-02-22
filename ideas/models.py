from django.db import models
from django.core.exceptions import ValidationError

class Idea(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    team = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name='ideas'
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    abstract = models.TextField()
    ppt = models.FileField(upload_to='idea_ppts/', null=True, blank=True)

    plagiarism_score = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    # Restrict max 3 ideas per team
    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.pk:
            if Idea.objects.filter(team=self.team).count() >= 3:
                raise ValidationError("This Team Has Already Submitted Three Ideas.")
            
        if self.status == 'approved':
            existing_approved = Idea.objects.filter(
                team=self.team,
                status='approved'
            ).exclude(pk=self.pk)

            if existing_approved.exists():
                raise ValidationError("This team already has an approved idea.")
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)