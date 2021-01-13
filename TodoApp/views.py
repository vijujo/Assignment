from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from TodoApp.models import Board, Todo
from TodoApp.serializers import BoardSerializer, TodoSerializer


@api_view(['GET', 'POST'])
def board_list(request):
    """
    List all code boards, or create a new board.
    """
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, pk):
    """
    Retrieve, update or delete a code board.
    """
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)
