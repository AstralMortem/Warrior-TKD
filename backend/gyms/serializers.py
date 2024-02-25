from rest_framework.serializers import ModelSerializer
from .models import Gym, Group

class GymSerializer(ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"