from rest_framework.serializers import ModelSerializer
from participant.models import Participant


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model=Participant
        fields=['id','nick','email']
        read_only_fields=['winner']


