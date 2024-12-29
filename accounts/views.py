from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer,RegistrationSerializers
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class Register(APIView):
    def get(self, request):
        return JsonResponse({"message":"This is the register endpiont"})
    def post(self,request):
        firstname = request.data.get("firstname", "")
        lastname = request.data.get("lastname", "")
        email = request.data.get("email", "")
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        confirm_password = request.data.get("confirm_password", "")
        print(password)
        print(confirm_password)
        if password != confirm_password:
            return Response({"message":"The password does not match"},status=status.HTTP_400_BAD_REQUEST)
        else:
            user_obj = User(first_name=firstname,last_name=lastname,username=username,email=email)
            user_obj.set_password(password)
            user_obj.save()
            serializer = UserSerializer(user_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogIn(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        return JsonResponse({"mesaage":"This is the login endpiont"})
    
    def post(self,request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username,password=password)
        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            print (created)
            return Response({"token":token.key})
        elif user is None: 
            return Response({"message":"Account not found, click the link below to register your account"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"key":"Invalid Credentials"})

class LogOut(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[AllowAny]
    def get(self,request):
        try:
            token = request.auth
            token_obj = Token.objects.get(key=token)
            token_obj.delete()
            return Response({"message":"You have been logged out"},status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response({"message":"you can not log out when you are not logged in"},status=400)
        
class RegisterUser(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        json_data = request.data
        serializer = RegistrationSerializers(data=json_data)
        if serializer.is_valid():
            serializer.save()
            username = serializer.data.get("username")
            #print(username)
            #username = user.username
            user_obj = User.objects.get(username=username)
            json_obj = {"first_name":user_obj.first_name,
                     "last_name":user_obj.last_name,
                     "email":user_obj.email,
                     "username":user_obj.username,
                     "password":user_obj.password
                    }
            print(user_obj)
            #return Response(json_obj,status=status.HTTP_201_CREATED)
            return Response({"Message":"Registration Successful"}, status=200)
        else:
            return Response(serializer.errors,status=400)
        