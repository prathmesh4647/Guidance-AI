from django.db import models

# Create your models here.

class WorkbookSection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100)   # Review-I
    semester = models.IntegerField()           # 1 or 2
    description = models.TextField()

    def __str__(self):
        return self.title


class ReviewQuestion(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class ReviewResponse(models.Model):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    question = models.ForeignKey(ReviewQuestion, on_delete=models.CASCADE)

    remark = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project} - {self.question}"