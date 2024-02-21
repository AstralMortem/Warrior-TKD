from rest_framework.routers import DefaultRouter
from .views import CompetitionViewSet, AttestationViewSet, AllEventsView, AllViewSet
from django.urls import path

router = DefaultRouter()

router.register(r'competitions',CompetitionViewSet, basename='competitions')
router.register(r'attestations',AttestationViewSet, basename='attestations')
router.register(r'all-events',AllViewSet, basename='allevents')


urlpatterns = [
    path('all', AllEventsView.as_view(),name='all')
]

urlpatterns += router.urls