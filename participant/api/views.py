import random
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import status
from participant.models import Participant
from participant.api.serializers import ParticipantSerializer

class ParticipantApiViewSet(ModelViewSet):
    serializer_class=ParticipantSerializer
    queryset= Participant.objects.all()
    http_method_names=['get','post']

    def list(self,request):
        winners=Participant.objects.filter(winner=True)
        winnersSerializer=self.serializer_class(data=winners,many=True)
        winnersSerializer.is_valid()

        return Response(status=status.HTTP_200_OK,data=winnersSerializer.data)

class ParticipantTotalView(ViewSet):
    def list(self,request):
        participants=Participant.objects.all()
        total= len(participants)
        return Response(status=status.HTTP_200_OK,data=total)
    
class ExecuteLotteryView(ViewSet):
    def create(self,request):
        participants=Participant.objects.all()
        total_winners=int(request.data['total_winner'])
        winners=random.sample(list(participants),total_winners)

        for winner in winners:
            participant=winner
            participant.winner=True
            participant.save()
        return Response(status=status.HTTP_200_OK,data={'result':'Ganas'})