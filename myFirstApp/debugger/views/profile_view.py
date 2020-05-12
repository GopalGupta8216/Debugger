from debugger.models import Project
from debugger.serializers.project_serializer import ProjectSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer