from rest_framework import serializers

from quiz.models import Question, Option, Quiz


class OptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializers(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'options')


class QuizListSerializers(serializers.ModelSerializer):
    question = QuestionSerializer()
    answer = OptionsSerializers()

    class Meta:
        model = Quiz
        fields = ('question', 'answer', 'is_correct')


class QuizSerializers(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('question', 'answer')

    def create(self, validated_data):
        print('validated_data', validated_data)
        question = Question.objects.get(pk=validated_data.get('question').pk)
        is_correct = True if question.correct_ans == validated_data.get('answer') else False

        quiz = Quiz.objects.create(
            user=self.context['request'].user,
            question=validated_data.get('question'),
            answer=validated_data.get('answer'),
            is_correct=is_correct,
        )

        return quiz

