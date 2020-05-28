from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.creator == request.user

class IsTeamMemberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return Project.objects.filter(team_member__id=request.user.id)

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.name == request.user.name

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_admin

class IsReportedByOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the person who had reported the issue  to edit it.
    """

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.reported_by == request.user.name

class IsCommentedByOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the person who had writtened a particular comment to edit it.
    """

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.commented_by == request.user.name