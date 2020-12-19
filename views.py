from django.shortcuts import render
from rest_framework import viewsets ,permissions, status
from .models import Note
from .serializers import NoteSerializer, UserSerializer ,NotePublicSerializer
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser


class ListNote(viewsets.ModelViewSet): 
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    #一覧取得
    def list(self,request):
        username = request.user.username

        data = NoteSerializer(Note.objects.all().select_related('user').filter(user__username=username).order_by('created_at').reverse(), many=True).data
        return Response(status=200 , data=data)

    #詳細の取得
    def retrieve(self,request,pk=None):
        note_id = pk
        data = NoteSerializer(Note.objects.filter(uuid=note_id), many=True).data
        return Response(status=200,data=data)

    def create(self, request):
        serializer = NoteSerializer(data=request.data, many=False)
        if(serializer.is_valid()):
            response = {'message': 'Note created' , 'result': serializer.data}
            note = Note.objects.create(
                title=request.data['title'],
                body=request.data['body'],
                sanmi = request.data['sanmi'],
                nigami = request.data['nigami'],
                like = request.data['like'],
                public = request.data["public"],
                user=request.user)
            return Response(response, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        note_id = pk
        username = request.user.username
        note = Note.objects.filter(uuid=note_id).filter(user__username=username).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListNote_Public(viewsets.ModelViewSet): 
    queryset = Note.objects.all()
    serializer_class = NotePublicSerializer

    #一覧取得
    def list(self,request):
        data = NotePublicSerializer(Note.objects.all().filter(public="true").order_by('created_at').reverse(), many=True).data
        if(data):
            for x in range(len(data)):
                data[x]["user"].pop("token")


        return Response(status=200 , data=data)


#
class GetUser(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self,request):
        username = request.user.username
        queryset = self.get_queryset().filter(username=username)
        serializer_class = UserSerializer
        data = UserSerializer( queryset, many=True).data
        return Response(data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminUser])
class ListUser(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)