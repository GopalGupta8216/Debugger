from rest_framework import serializers

from debugger.models import Comment
from .user_serializer import UserSerializer
from .issue_serializer import IssueSerializer 
class CommentSerializer(serializers.ModelSerializer):
    issue_name = IssueSerializer(many =True, read_only=True)
    commented_by = UserSerializer(many = True,read_only=True)

    class Meta:
        model = Comment
        fields = (
                'commented_by',
                'issue_name',
                'message',
                'mentions',
                'created_on'
                )

