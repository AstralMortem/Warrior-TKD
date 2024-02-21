from rest_framework.serializers import ModelSerializer
from .models import Gym

class GymSerializer(ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"
