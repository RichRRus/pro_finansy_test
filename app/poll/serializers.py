from rest_framework import serializers

from poll import models


class PollOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PollOption
        exclude = [
            'poll',
        ]


class PollOptionWithPercentSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    def get_percent(self, obj) -> float:
        total_answers_count = models.PollAnswer.objects.filter(option__poll=obj.poll).count()
        return obj.answers.count() / total_answers_count * 100

    class Meta:
        model = models.PollOption
        exclude = [
            'poll',
        ]


class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)

    class Meta:
        model = models.Poll
        fields = '__all__'


class PollRetrieveSerializer(serializers.ModelSerializer):
    options = PollOptionWithPercentSerializer(many=True)

    class Meta:
        model = models.Poll
        fields = '__all__'


class PollAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PollAnswer
        fields = '__all__'
