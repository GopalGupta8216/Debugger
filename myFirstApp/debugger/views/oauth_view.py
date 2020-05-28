from debugger.models import User
from debugger.serializers.user_serializer import UserSerializer
from rest_framework import viewsets, status, permissions
from debugger.permissions import IsAdmin,IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

class OauthViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
    }
   
    def create(self, request, **kwargs):
        CLIENT_SECRET="oY3vRQevRbFdsO6O02IfWVIGIqzU1XNmq5fVan1w2gXyFuMoIjBpeO8iK22dmFL4jf7n0vlL6mLnjX8TM63MTdYnJndFq25LcNF6nwLnVSKLYqTyDSBlBCZKL0FgJAVg"
        REDIRECT_URL= "https://127.0.0.1:8000/debugger/users/"
        CLIENT_ID = "zrkRVm7TY9xaNOQmdRlVzgTI4DS4R2tNqpgfNxB2"
        Access_Token_Endpoint="https://internet.channeli.in/open_auth/token/"

        try:
            auth_code = request.data["code"]
        except KeyError:
            return Response("Authentication code not provided",status=status.HTTP_400_BAD_REQUEST)

        data={
            "client_id":CLIENT_ID,
            "client_secret":CLIENT_SECRET,
            "grant_type" : "authorization_code",
            "redirect_url":REDIRECT_URL,
            "code" : auth_code
        }

        r=requests.post(Access_Token_Endpoint,data=data).json()
        if(r.get("error",None)):
            return Response(r,status=status.HTTP_400_BAD_REQUEST)
        headers={
            "Authorization":'Bearer ' + r["access_token"],
        }
        user_data=requests.get(
            url="https://internet.channeli.in/open_auth/get_user_data/",headers=headers).json()
        
        #return Response(user_data)
        roles = user_data["person"]["roles"]
        is_maintainer = False
        for role in roles:
            if(role["role"] == "Maintainer" ):
                is_maintainer = True

        if(not is_maintainer):
            return Response("oops U can't access this Feature",status=status.HTTP_403_FORBIDDEN)
        try:
            User.objects.get(
            enrollment = user_data["student"]["enrolmentNumber"]
        )
        except User.DoesNotExist:
            #username = f'{user_data["person"]["fullName"].split()[0]}_{user_data["userId"]}'
            try:
                user = User.objects.create(
                    name = user_data["person"]["fullName"],
                    enrollment = user_data["student"]["enrolmentNumber"],
                    email = user_data["contactInformation"]["instituteWebmailAddress"],
                    image = user_data["displayPicture"],
                    is_admin = False
                )
            except KeyError:
                    return Response("You don't have a profile picture, Upload One and Try Again", status=status.HTTP_403_FORBIDDEN )    
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_201_CREATED)