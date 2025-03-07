from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from todo.models import Todo
from accounts.models import Profile


class TodoSerializer(serializers.ModelSerializer):
    "A serializer for Todo model"
    
    def create(self, validated_data):
        "A function to create tasks based on user profile"
        validated_data['user'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
    
    class Meta:
        model = Todo
        fields = ['user', 'title', 'due_time', 'complete', 'created_date', 'updated_date']
        read_only_fields = ['user']
    