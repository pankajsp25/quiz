from django.urls import path
from rest_framework import routers

from quiz.views import QuestionVeiwSet, QuizViewSet, QuizResultView

router = routers.DefaultRouter()
router.register('question', QuestionVeiwSet, basename='question')
router.register('quiz', QuizViewSet, basename='quiz')

urlpatterns = router.urls

urlpatterns += [
    path('quizresult/<int:pk>', QuizResultView.as_view()),
]
