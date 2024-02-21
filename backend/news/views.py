from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import NewsSerializer
from .models import News

class NewsViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_archived=False)
    serializer_class = NewsSerializer