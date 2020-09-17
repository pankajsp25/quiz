from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Option(models.Model):
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.value


class Question(models.Model):
    question = models.CharField(max_length=500)
    options = models.ManyToManyField(Option)
    correct_ans = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='quizzes')
    answer = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='quizzes')
    is_correct = models.BooleanField()
    quiz_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user.first_name} - {self.question.question}'
