from rest_framework import viewsets, mixins
from rest_framework import filters
import django_filters.rest_framework
from .models import Group
from .serializers import GroupSerializer
from .filters import MembersFilter


class GroupViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filterset_class = MembersFilter
