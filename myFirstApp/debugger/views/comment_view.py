from debugger.models import Comment
from debugger.serializers.comment_serializer import CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from debugger.permissions import IsAdmin,IsCommentedByOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsCommentedByOrReadOnly,IsAdmin]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_queryset(self):
        """
        This view should return a list of all the comments for
        the issue as determined by the issue portion of the URL.
        """
        pk1 = self.kwargs['pk1']
        return Comment.objects.filter(issue_name=pk1)

    def perform_create(self, serializer):
        serializer.save()