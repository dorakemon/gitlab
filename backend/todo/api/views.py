from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from todo.api.serializers import GroupSerializer, ContentDetailSerializer, ContentSerializer
from todo.models import Group, Todo

class GroupDetailAPIView(APIView):

    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group_list=[]

        for item in Group.objects.filter(user_in_group__username=str(request.user)).values_list('name', flat=True):
            group_list.append(item)

        if request.user.is_superuser:
            serializer = GroupSerializer(group) 
            return Response(serializer.data)

        elif group.name in group_list:
            serializer = GroupSerializer(group) 
            return Response(serializer.data)

        else: 
            raise ValidationError("You cannot access this!")

class GroupListAPIView(generics.ListCreateAPIView):

    serializer_class = GroupSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Group.objects.all()

        elif user != "AnonymousUser":
            return Group.objects.filter(user_in_group__username=str(user))

class ContentDetailAPIView(APIView):

    
    #serializer_class = ContentDetailSerializer
    #queryset = Group.objects.all()

    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group_list=[]

        for item in Group.objects.filter(user_in_group__username=str(request.user)).values_list('name', flat=True):
            group_list.append(item)

        if request.user.is_superuser:
            serializer = ContentDetailSerializer(group) 
            return Response(serializer.data)

        elif group.name in group_list:
            serializer = ContentDetailSerializer(group) 
            return Response(serializer.data)

        else: 
            raise ValidationError("You cannot access this!")

class ContentCreateAPIView(generics.CreateAPIView):
    """Todoの中身を登録するPOSTのみ許可  
        Group選択時にintのID指定"""
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_uuid = self.kwargs.get("uuid")

        # if question.answers.filter(author=request_user).exists():
        #     raise ValidationError("You have already answered this Question!")

        serializer.save(pub_user=request_user)


class ContentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Todo.objects.all()

        elif user != "AnonymousUser":
            return Todo.objects.filter(pub_user__username=str(user))

        else:
            raise ValidationError("You cannot access this!")
