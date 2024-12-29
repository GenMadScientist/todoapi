from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class RegistrationSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=100,default="")
    last_name = serializers.CharField(max_length=100,default="")
    email = serializers.EmailField(default="")
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
    confirm_password = serializers.CharField(max_length=50)

    def create(self,validated_data):
        first_name = validated_data.get("first_name","")
        last_name = validated_data.get("last_name","")
        email = validated_data.get("email","")
        username = validated_data.get("username")
        password = validated_data.get("password")
        #confirm_password = validated_data.get("confirm_password")

        user_obj = User(first_name=first_name,last_name=last_name,email=email,username=username)
        user_obj.set_password(password)
        user_obj.save()
        json_obj = {"first_name":user_obj.first_name,
                     "last_name":user_obj.last_name,
                     "email":user_obj.email,
                     "username":user_obj.username,
                     "password":user_obj.password
                    }
        return validated_data
    
    def update(self,instance,validated_data):
        instance.first_name=validated_data.get("first_name")
        instance.last_name=validated_data.get("last_name")
        instance.email=validated_data.get("email")
        instance.username=validated_data.get("username")
        instance.password=validated_data.get("password")

    def validate_confirm_password(self,confirm_password):
        data = self.get_initial()
        password = data.get("password")
        if password != confirm_password:
            raise serializers.ValidationError("Password must match")
        else:
            return confirm_password

