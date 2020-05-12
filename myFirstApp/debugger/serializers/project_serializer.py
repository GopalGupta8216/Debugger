from rest_framework import serializers

from debugger.models import Project
from .user_serializer import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    team_member = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
                'creator',
                'project_name',
                'wiki',
                'team_member'
                )


