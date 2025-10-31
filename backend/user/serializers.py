from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Role
from organization.models import Location
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn’t match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()

        # create UserProfile
        UserProfile.objects.create(
            user=user,
            username=validated_data['username'],
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    role_name = serializers.ReadOnlyField(source='role.name')
    location_name = serializers.ReadOnlyField(source='location.name')

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'role', 'role_name', 'location', 'location_name')
