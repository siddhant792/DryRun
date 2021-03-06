# from rest_framework import serializers as rest_framework_serializers
# from rest_framework.authtoken.models import Token as AuthToken
# from rest_framework import exceptions

# from django.contrib.auth import authenticate

# from apps.accounts import models as accounts_models


# class UserSerializer(rest_framework_serializers.ModelSerializer):
#     """
#     Custom User Serializer class
#     """
#     token = rest_framework_serializers.SerializerMethodField()

#     class Meta:
#         model = accounts_models.User
#         fields = ['id', 'email', 'name', 'password', 'username', 'token']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
    
#     def create(self, validated_data):
#         user = accounts_models.User(
#             name = validated_data['name'],
#             email = validated_data['email'],
#             password = validated_data['password'],
#             username = validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

#     def get_token(self, user):
#         """
#         Creating token for already registered user
#         """
#         return AuthToken.objects.create(user = user).key


# class LoginSerializer(rest_framework_serializers.Serializer):
#     """
#     Validating login credentials
#     """
#     email = rest_framework_serializers.EmailField()
#     password = rest_framework_serializers.CharField()

#     def validate(self, attrs):
#         """
#         Validating if user exists with given credentials
#         """
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = authenticate(email=email, password=password)
#         if not user:
#             raise exceptions.ValidationError('Unable to log in with provided credentials.')
#         attrs['user'] = user
#         return attrs
