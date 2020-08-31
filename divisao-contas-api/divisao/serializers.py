from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'members',)

        def create(self, validated_data):
            group = Group.objects.create(**validated_data)
            return group
