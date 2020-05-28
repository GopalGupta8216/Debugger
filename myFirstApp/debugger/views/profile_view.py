from debugger.models import Project
from debugger.serializers.project_serializer import ProjectSerializer
from rest_framework import viewsets, permissions
from debugger.permissions import IsAdmin,IsCreatorOrReadOnly,IsTeamMemberOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsCreatorOrReadOnly,IsAdmin,IsTeamMemberOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
