from rest_framework import serializers
from TodoApp.models import Board, Todo


class BoardSerializer(serializers.ModelSerializer):
    todos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'todos']

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'done', 'created', 'updated', 'board']

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.done = validated_data.get('done', instance.done)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.save()
        return instance
