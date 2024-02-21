from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserListSerializer, UserDetailSerializer,BeltListSerializer,BeltDetailSerializer
from .models import BaseUser,Belt



class UserViewSet(ReadOnlyModelViewSet):
    queryset = BaseUser.objects.all()
    filterset_fields = ['is_staff']
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'retrieve':
            return UserDetailSerializer
        

class BeltViewSet(ReadOnlyModelViewSet):
    queryset = Belt.objects.all()
    pagination_class = None
    def get_serializer_class(self):
        if self.action == 'list':
            return BeltListSerializer
        elif self.action == 'retrieve':
            return BeltDetailSerializer

