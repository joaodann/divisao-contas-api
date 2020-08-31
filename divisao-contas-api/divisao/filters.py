import django_filters.rest_framework
from .models import Group

class MembersFilter(django_filters.FilterSet):
    members = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Group
        fields = ('members', 'name')
