from rest_framework import serializers

from debugger.models import Project,User
from .user_serializer import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    team_member = serializers.SlugRelatedField(many=True,slug_field='name',queryset=User.objects.all(),required= False)
    creator =  serializers.SlugRelatedField(many=False,slug_field='name', read_only=True )

    class Meta:
        model = Project
        fields = ('creator', 'project_name', 'wiki', 'team_member')
        
    """def create(self, validated_data):
        team_members_data = validated_data.pop('team_member')
        user = User.objects.create(**validated_data)
        for team_member_data in team_members_data:
            User.objects.create(user=user, **team_member_data)
        return user
"""