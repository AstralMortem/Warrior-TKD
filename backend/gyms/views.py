from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import GymSerializer
from .models import Gym

class GymViewSet(ReadOnlyModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer