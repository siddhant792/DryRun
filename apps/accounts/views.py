from rest_framework import generics as rest_framwork_generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token as AuthToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from apps.accounts import serializers as accounts_serializers
from apps.accounts import models as accounts_models


class RegisterUserView(rest_framwork_generics.CreateAPIView):
    """
    Register API for users
    """
    serializer_class = accounts_serializers.UserSerializer
    permission_classes = [AllowAny]


class LoginUserView(rest_framwork_generics.CreateAPIView):
    """
    Login API for users
    """
    serializer_class = accounts_serializers.LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        login_serializer = self.serializer_class(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        token = AuthToken.objects.get_or_create(user = login_serializer.validated_data['user'])[0].key
        return Response(
            {
                'token': token,
                'name': login_serializer.validated_data['user'].name,
                'email': login_serializer.validated_data['user'].email,
                'username': login_serializer.validated_data['user'].username,
            }
        )


class UserProfileView(rest_framwork_generics.RetrieveAPIView):
    """
    Get User profile data 
    """
    serializer_class = accounts_serializers.UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request._user
        return_data = dict(self.serializer_class(instance=user).data)
        return_data['skills'] = eval(return_data['skills'])
        return Response(return_data)



class LogoutUserView(rest_framwork_generics.DestroyAPIView):
    """
    LogOut the current user
    """
    query_set = AuthToken.objects.all()

    def destroy(self, request, *args, **kwargs):
        token = self.query_set.filter(user=request.user)
        if token:
            token.delete()
            return Response({'message': "Logout Successful"}, status=HTTP_200_OK)
        return Response({'message': "Logout Failed"}, status=HTTP_400_BAD_REQUEST)
