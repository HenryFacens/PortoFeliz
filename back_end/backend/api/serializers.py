from rest_framework import serializers
from .models import User, Sector, Interaction, Feedback, AdminUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token
    
class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        SuperUser = self.Meta.model.objects.create_user(**validated_data)
        return SuperUser
    
class UserSerializer(serializers.ModelSerializer):

    group_names = serializers.ListField(
        child=serializers.CharField(max_length=80), 
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'join_date', 'groups', 'group_names']

    def create(self, validated_data):
        group_names = validated_data.pop('group_names', [])
        user = User.objects.create_user(**validated_data)
        
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        
        return user
    
    def update(self, instance, validated_data):
        group_names = validated_data.pop('group_names', [])

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.join_date = validated_data.get('join_date', instance.join_date)

        instance.groups.clear()
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            instance.groups.add(group)

        instance.save()
        return instance

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
