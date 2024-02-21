from rest_framework.routers import DefaultRouter
from .views import GymViewSet

router = DefaultRouter()

router.register(r'',GymViewSet, basename='gym')

urlpatterns = router.urls