from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from quiz.models import Question, Quiz
from quiz.serializers import QuestionSerializer, QuizSerializers, QuizListSerializers


class QuestionVeiwSet(ListModelMixin, GenericViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.prefetch_related('options').all()

    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class QuizViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = QuizSerializers
    queryset = Quiz.objects.all()

    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return QuizListSerializers

        return super().get_serializer()

    def get_queryset(self):

        queryset = super().get_queryset()

        return queryset.filter(user=self.request.user)


@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
class QuizResultView(APIView):

    def get(self, request, pk):
        total_question = Quiz.objects.filter(user__pk=pk).count()

        if total_question == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'msg': 'You have not attended quiz'})

        correct_answer = Quiz.objects.filter(user__pk=pk, is_correct=True).count()
        wrong_answer = Quiz.objects.filter(user__pk=pk, is_correct=False).count()
        correct_percentage = (correct_answer / total_question) * 100

        res_data = {
            'total_question' : total_question,
            'correct_answer': correct_answer,
            'wrong_answer': wrong_answer,
            'correct_percentage': correct_percentage
        }

        return Response(status=status.HTTP_200_OK, data=res_data)
