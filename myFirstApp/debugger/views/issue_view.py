from debugger.models import Issue
from debugger.serializers.issue_serializer import IssueSerializer,IssueUpdateSerializer
from rest_framework import viewsets, permissions
from debugger.permissions import IsCreatorOrReadOnly,IsAdmin, IsReportedByOrReadOnly,IsTeamMemberOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class IssueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdmin,IsReportedByOrReadOnly,IsTeamMemberOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return Issue.objects.filter(project_name=pk)

    def get_serializer_class(self):
        if(self.action == 'list' or self.action == 'create'):
            return IssueSerializer
        else:
            return IssueUpdateSerializer
        