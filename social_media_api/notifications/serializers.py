from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source="actor.username")
    #to make this field read only

    class Meta:
        model = Notification
        fields = ["id", "actor", "verb", "timestamp", "read"]
