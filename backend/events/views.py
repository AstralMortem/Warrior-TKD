from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CompetitionSerializer,AttestationSerializer
from .models import Competition, Attestation
from rest_framework.views import APIView
from rest_framework.response import Response

class CompetitionViewSet(ReadOnlyModelViewSet):
    queryset = Competition.objects.filter(is_archived=False)
    serializer_class = CompetitionSerializer
    filterset_fields = ["participants"]

class AttestationViewSet(ReadOnlyModelViewSet):
    queryset = Attestation.objects.filter(is_archived=False)
    serializer_class = AttestationSerializer
    filterset_fields = ["participants"]


class AllEventsView(APIView):
    def get(self, request, format=None):
        competitions = CompetitionSerializer(Competition.objects.filter(is_archived=False),many=True)
        attestation = AttestationSerializer(Attestation.objects.filter(is_archived=False),many=True)

        return Response(competitions.data+attestation.data)
    
class AllViewSet(ReadOnlyModelViewSet):

    def list(self, request, *args, **kwargs):
        competitions = CompetitionSerializer(Competition.objects.filter(is_archived=False),many=True)
        attestation = AttestationSerializer(Attestation.objects.filter(is_archived=False),many=True)

        return Response({
            'attestations': attestation.data,
            'competitions': competitions.data
        })

        
        




