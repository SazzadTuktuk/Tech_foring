from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, ProjectMember, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']

class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']
