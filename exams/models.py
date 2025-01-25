from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions",default=1)
    text = models.TextField(default="question")
