from django.contrib import admin

# Register your models here.
from quiz.models import Question, Option, Quiz

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Quiz)
