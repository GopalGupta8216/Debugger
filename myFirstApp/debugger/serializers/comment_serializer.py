from rest_framework import serializers
from debugger.models import Comment,User,Issue
from .user_serializer import UserSerializer
from .issue_serializer import IssueSerializer 

class CommentSerializer(serializers.ModelSerializer):
    issue_name = serializers.SlugRelatedField(many=False,slug_field='id',queryset=Issue.objects.all())
    commented_by = serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all())
    mention = serializers.SlugRelatedField(many=True,slug_field='name',queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = (
                'commented_by',
                'issue_name',
                'message',
                'mention',
                'created_on'
                )

