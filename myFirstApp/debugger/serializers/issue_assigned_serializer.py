from rest_framework import serializers

from debugger.models import Issue_assigned
from .user_serializer import UserSerializer


class IssueAssignedSerializer(serializers.ModelSerializer):


    class Meta:
        model = Issue_assigned
        fields = ('assigned_by','assigned_to',' issue_name')

