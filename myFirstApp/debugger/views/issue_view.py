from debugger.models import Issue
from debugger.serializers.issue_serializer import IssueSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class IssueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer