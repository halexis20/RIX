from django.contrib import admin
from participant.models import Participant
# Register your models here.

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display=['id','nick','email','winner']
