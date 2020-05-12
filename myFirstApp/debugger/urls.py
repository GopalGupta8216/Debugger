from django.urls import path, include
from rest_framework.routers import DefaultRouter
from debugger.views import user_view,profile_view,comment_view,issue_view

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', user_view.UserViewSet)
router.register(r'issue', issue_view.IssueViewSet)
router.register(r'comment', comment_view.CommentViewSet)
router.register(r'project', profile_view.ProjectViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
