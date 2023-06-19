from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question=models.CharField(max_length=300)
    author=models.CharField(max_length=50)
    create_date=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.question
    
    class Meta:
        ordering=["-id"]

class Answer(models.Model):
    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer=models.TextField(max_length=3000)
    author=models.CharField(max_length=50)
    create_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer
    
    class Meta:
        ordering=["-id"]