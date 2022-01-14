from rest_framework import serializers as rest_framework_serializers
from rest_framework.authtoken.models import Token as AuthToken
from rest_framework import exceptions

from django.contrib.auth import authenticate
from django.db.models import F, fields

from apps.accounts import models as accounts_models
from apps.problems import (
    models as problem_models,
    utils as problem_utils,
)


class UserSerializer(rest_framework_serializers.ModelSerializer):
    """
    Custom User Serializer class
    """
    token = rest_framework_serializers.SerializerMethodField()

    class Meta:
        model = accounts_models.User
        fields = ['email', 'name', 'password', 'username', 'token']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        user = accounts_models.User(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_token(self, user):
        """
        Creating token for already registered user
        """
        return AuthToken.objects.create(user = user).key


class LoginSerializer(rest_framework_serializers.Serializer):
    """
    Validating login credentials
    """
    email = rest_framework_serializers.EmailField()
    password = rest_framework_serializers.CharField()

    def validate(self, attrs):
        """
        Validating if user exists with given credentials
        """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise exceptions.ValidationError('Unable to log in with provided credentials.')
        attrs['user'] = user
        return attrs


class UserProfileSerializer(rest_framework_serializers.ModelSerializer):
    """
    User Profile Serializer
    """
    submissions = rest_framework_serializers.SerializerMethodField()

    class Meta:
        model = accounts_models.User
        fields = [
            'email', 'name', 'username', 'gender', 'location', 'summary', 'date_of_birth',
            'website', 'education', 'work', 'profile_pic', 'skills', 'submissions',
        ]
    
    def get_submissions(self, user):
        """
        Retrieving last 10 submissions made by the user
        """
        submissions_list = problem_models.Submission.objects.filter(user=user).order_by('-created_at').values(
            'status', 'language_used', submitted_at=F('created_at'), problem_name=F('problem__name')
        )[:10]

        for submission in submissions_list:
            submission['submitted_at'] = problem_utils.get_submission_interval(submission['submitted_at'])

        return submissions_list
