from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json
from django.db.models import Q
from todo.models import Todo,Like
from todo.serializers import TodoListSerializers,TodoDetailsSerializers,SearchSerializers,ProfileSerializers, UserSerializers,LikeSerializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from comment.serializers import CommentSerializers
from comment.models import Comments
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from todo.permissions import IsTodoOwnerorIsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from todo.paginations import CursorPagePagination


# Create your views here.
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication,JWTAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
   print(request.user)
   print(request.user.is_superuser)
   list_todo = Todo.objects.all()
   paginator = CursorPagePagination()
   paginator_qs = paginator.paginate_queryset(list_todo,request)
   serializer = TodoListSerializers(paginator_qs,many=True)
   return paginator.get_paginated_response(serializer.data)
   
   #serializer = TodoListSerializers(list_todo, many=True)
   #return Response(serializer.data,status=status.HTTP_200_OK)

   #return HttpResponse('This is the todo list endpiont')

@api_view(['GET'])
def todo_details(request,id):
   try: 
      todo_detail = Todo.objects.get(id=id)
   except:
      return Response(status=404)
   serializer = TodoDetailsSerializers(todo_detail)
   return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def todo_create(request):
   if request.method == 'GET':
      return Response(status=status.HTTP_200_OK)
   if request.method == 'POST':
      current_user = request.user
      json_data = request.data
      serializer = TodoListSerializers(data=json_data)
      if serializer.is_valid():
         serializer.save(user=current_user)
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_todo(request,id):
   if request.method == "GET":
      return Response(status=status.HTTP_200_OK)
   try:
      todo_to_update = Todo.objects.get(id=id)
      if todo_to_update.user.id == request.user.id or request.user.is_superuser:
         jsondata = request.data
         serializer = TodoDetailsSerializers(todo_to_update, data=jsondata)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors,status=400)
      else:
         return Response({"message":"you can not update a post that is not your own"},status=status.HTTP_401_UNAUTHORIZED)
   except:
      error = {"Message":"The todo is not in the database."}
      jsondata = json.dumps(error)
      return Response(jsondata,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','DELETE'])
#@permission_classes([IsTodoOwnerorIsAdmin])
def delete_todo(request,id):
   if request.method =='GET':
      return Response(status=status.HTTP_200_OK)
   try:
      todo_to_delete = Todo.objects.get(id=id)
      if todo_to_delete.user.id == request.user.id or request.user.is_superuser:
         serializer = TodoDetailsSerializers(todo_to_delete)
         todo_to_delete.delete()
         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
      else:
         return Response({"message":"Not authorized to delete the todo"},status=400)
   except:
      error = {"Message":"This todo list is not in the database."}
      json_data = json.dumps(error)
      return Response(json_data,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search(request):
   search_todo = request.GET["q"]
   search_list = Todo.objects.filter(Q(todo_list__contains=search_todo)|Q(title__contains=search_todo))
   serializer = SearchSerializers(search_list, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)

class UsersList(APIView):
   def get(self,request):
         users_list = User.objects.all()
         serializer = UserSerializers(users_list, many=True)
         return Response(serializer.data, status=200)
   def post(self,request):
      json_data = request.data
      serializer = UserSerializers(data=json_data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class CreateComment(APIView):
   def get(self,request,todo_id):
      comment = Comments.objects.all()
      serializer = CommentSerializers(comment, many=True)
      return Response(serializer.data, status=200)
   def post(self,request,todo_id):
      try:
         todo = Todo.objects.get(id=todo_id)
      except:
         return Response(status=404)
      serializer = CommentSerializers(data=request.data)
      if serializer.is_valid():
         serializer.save(todo=todo)
         return Response(serializer.data, status=201)
      else:
         return Response(serializer.errors,status=401)

class Like(APIView):
   def get(self,request):
      like = Like.objects.all()
      serializer = LikeSerializers(like,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def post(self,request,todo_id):
      json_data = request.data
      try:
         like = Like.objects.get(id=todo_id)
      except:
         return Response({"message":"No todo linked to this id"}, status=404)
      serializer = LikeSerializers(data=json_data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
