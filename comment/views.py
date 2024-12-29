from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from comment.models import Comments
from todo.models import Todo
import json
from comment.serializers import CommentSerializers,CommentDetailSerializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
class CommentList(APIView):
    # = [SessionAuthentication]
   # permission_classes = [AllowAny]
    def get(self, request):
        #return HttpResponse('This is the comment endpiont')
        comment = Comments.objects.all()
        serializer = CommentSerializers(comment,many=True)

        return Response (serializer.data, status=status.HTTP_200_OK)
    def post(self,request,todo_id):
        json_data = request.data
        serializer = CommentSerializers(data=json_data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CommentDetail(APIView):
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request,comment_id):
        try:
            single_comment = Comments.objects.get(id=comment_id)
            serializer = CommentSerializers(single_comment)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,comment_id):
        try:
            single_comment = Comments.objects.get(id=comment_id)
        except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        jsondata = request.data
        serializer = CommentSerializers(single_comment, data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,comment_id):
        try:
            single_comment = Comments.objects.get(id=comment_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializers(single_comment)
        single_comment.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
class CommentView(APIView):
    def get(self,request,todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
        except:
            return Response(status=404)
        comment = todo.commnts.get()
        def post(self,request,blog_id):
            try:
                todo = Todo.objects.get(id=todo_id)
            except:
                return Response(status=404)
            json_data = request.data
            serializer = CommentSerializers(data=json_data)   
            if serializer.is_valid():
                serializer.save(todo=todo)    
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=400) 

class ThumbsUp(APIView):
    def post(self,request,comment_id):
        #current_user = request.user
        try:
            comment = Comments.objects.get(id=comment_id)
        except:
            return Response({"Message":"The id does not exist."})
        comment.thumbsup = comment.thumbsup+1 
        comment.thumbsup
        comment.save() 
        serializer = CommentSerializers(comment)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ThumbsDown(APIView):
    def post(self,request,comment_id):
        comment = Comments.objects.get(id=comment_id)
        try:
            comment.thumbsup = comment.thumbsup-1 
            comment.save() 
            serializer = CommentSerializers(comment)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"Thumbsup should not be less than zero"},status=status.HTTP_400_BAD_REQUEST)
'''            
class ThumbsUp(APIView):
    def get(self,request,comment_id):
        try:
            thumb = ThumbsUp.objects.get(id=comment_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ThumbsupSerializers(thumb)
        return Response(serializer.data,status=status.HTTP_200_OK)
        '''