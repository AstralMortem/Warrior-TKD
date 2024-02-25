from rest_framework.routers import DefaultRouter
from .views import GymViewSet,get_gyms_by_coach,get_groups_by_gym,get_available_participants_by_coach
from django.urls import path

router = DefaultRouter()

router.register(r'',GymViewSet, basename='gym')

app_name = "gyms"
urlpatterns = [
    path('get_gyms_by_coach/<slug:user_id>/', get_gyms_by_coach,name='get_gyms_by_coach'),
    path('get_groups_by_gym/<int:gym_id>/', get_groups_by_gym,name='get_groups_by_gym'),
    path('available/<slug:coach_id>/',get_available_participants_by_coach,name="get_available_participants_by_coach"),
]



urlpatterns += router.urls