from rest_framework import serializers
from .models import User, Sector, Interaction, Feedback, AdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'join_date', 'groups', 'user_permissions']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name', 'lat', 'lgn', 'description', 'created_at', 'updated_at']

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'like_dislike', 'created_at', 'updated_at']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'sector', 'interaction', 'full_name', 'phone', 'comment', 'created_at', 'updated_at']

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id', 'user', 'first_name', 'last_name', 'password', 'permissions', 'active', 'description', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        admin_user = AdminUser(**validated_data)
        admin_user.set_password(validated_data['password'])
        admin_user.save()
        return admin_user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.permissions = validated_data.get('permissions', instance.permissions)
        instance.active = validated_data.get('active', instance.active)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
