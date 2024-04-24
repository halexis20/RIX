from django.urls import path
from rest_framework.routers import DefaultRouter
from participant.api.views import ParticipantApiViewSet,ParticipantTotalView,ExecuteLotteryView

router_participant=DefaultRouter()
router_participant.register(prefix='lottery/participant',basename='lottery/participant',viewset=ParticipantApiViewSet)
router_participant.register(prefix='lottery/total_participants',basename='lottery/total_participants',viewset=ParticipantTotalView)
router_participant.register(prefix='lottery/execute',basename='lottery/execute',viewset=ExecuteLotteryView)