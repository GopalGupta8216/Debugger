from rest_framework import serializers

from debugger.models import User,Project,Issue,Issue_assigned,Comments

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name','image','contact','email')

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('creator','project_name','wiki','team_member')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('project_name',' reported_by','status',' heading','discription','media_uploads','reported_on')



class Issue_assignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue_assigned
        fields = ('assigned_by','assigned_to',' issue_name')



class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('commented_by','issue_name','msg','mentions','Created_on')



#urls.py

        from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from debugger.views import profile_view, user_view, issue_view, comment_view, issue_assigned_view

urlpatterns = [
    path('debugger/project/', profile_view.ProjectList.as_view()),
    path('debugger/project/<int:pk>/', profile_view.UpdateProjectDetail.as_view()),
    path('debugger/user/', user_view.UserList.as_view()),
    path('debugger/user/<int:pk>/', user_view.UpdateUserDetail.as_view()),
    path('debugger/issue/', issue_view.IssueList.as_view()),
    path('debugger/issue/<int:pk>/', issue_view.UpdateIssueDetail.as_view()),
    path('debugger/comment/', comment_view.CommentList.as_view()),
    path('debugger/project/<int:pk>/', comment_view.UpdateCommentDetail.as_view()),
    path('debugger/issue/assigned/', issue_assigned_view.IssueAssignedList.as_view()),
    path('debugger/issue/assigned/<int:pk>/', issue_assigned_view.UpdateIssueAssignedDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

