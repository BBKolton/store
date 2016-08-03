from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userdir.models import Users
from userdir.serializers import UsersSerializer
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
 
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
