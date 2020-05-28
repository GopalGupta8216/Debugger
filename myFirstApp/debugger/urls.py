from django.urls import path, include
from rest_framework.routers import DefaultRouter
from debugger.views import user_view,profile_view,comment_view,issue_view
from debugger.views import oauth_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register our viewsets with it.

router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', user_view.UserViewSet)
router.register(r'project', profile_view.ProjectViewSet)
router.register(r'oauth', oauth_view.OauthViewSet)

#router.register(r'comment', comment_view.CommentViewSet)
#router.register(r'project', profile_view.ProjectViewSet)
router2 = DefaultRouter()
router2.register(r'issue', issue_view.IssueViewSet)
router3 = DefaultRouter()
router3.register(r'comment', comment_view.CommentViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('project/<int:pk>/', include(router2.urls)),
    path('project/<int:pk>/issue/<int:pk1>/', include(router3.urls)),
  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
