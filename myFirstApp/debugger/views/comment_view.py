from debugger.models import Comment
from debugger.serializers.comment_serializer import CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer