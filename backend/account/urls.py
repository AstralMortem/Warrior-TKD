from rest_framework.routers import DefaultRouter
from .views import UserViewSet,BeltViewSet

router = DefaultRouter()

router.register(r'users',UserViewSet, basename='user')
router.register(r'belts', BeltViewSet,basename='belt')

urlpatterns = router.urls
