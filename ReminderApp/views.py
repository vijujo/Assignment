from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ReminderApp.models import Reminder
from ReminderApp.serializers import ReminderSerializer


@api_view(['GET', 'POST'])
def reminder_list(request):
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def reminder_detail(request, pk):
    try:
        reminder = Reminder.objects.get(id=pk)
    except Reminder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)