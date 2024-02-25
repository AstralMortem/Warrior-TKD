from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import GymSerializer, GroupSerializer
from account.serializers import UserListSerializer
from .models import Gym,Group
from django.contrib.auth import get_user_model

class GymViewSet(ReadOnlyModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


def get_gyms_by_coach(request,user_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = Gym.objects.filter(coach=user_id)
        return JsonResponse(GymSerializer(data,many=True).data,safe=False)
    
def get_groups_by_gym(request,gym_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = Group.objects.filter(gym=gym_id)
        return JsonResponse(GroupSerializer(data,many=True).data,safe=False)
    
def get_available_participants_by_coach(request,coach_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = get_user_model().objects.filter(is_staff=False,is_active=True,coach=coach_id,group_participants__id=None)
        print(data)
        return JsonResponse(UserListSerializer(data,many=True).data,safe=False)