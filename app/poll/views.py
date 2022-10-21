from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from poll import models, serializers, services


@extend_schema_view(
    submit_answer=extend_schema(
        responses={200: None}
    )
)
class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    http_method_names = ('get', 'post')
    serializer_class = serializers.PollSerializer

    def get_serializer_class(self):
        match self.action:
            case 'retrieve':
                return serializers.PollRetrieveSerializer
            case _:
                return self.serializer_class

    def perform_create(self, serializer):
        poll = services.PollService.create(**serializer.data.copy())
        return poll

    @action(
        methods=('post',),
        detail=False,
        serializer_class=serializers.PollAnswerSerializer,
    )
    def submit_answer(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.PollAnswer.objects.create(option_id=serializer.data.get('option'))
        return Response(status=status.HTTP_200_OK)
