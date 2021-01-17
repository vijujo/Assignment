from rest_framework import serializers
from ReminderApp.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['text', 'callback_url', 'delay']

    def create(self, validated_data):
        return Reminder.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.callback_url = validated_data.get('callback_url', instance.callback_url)
        instance.delay = validated_data.get('delay', instance.delay)
        instance.save()
        return instance
