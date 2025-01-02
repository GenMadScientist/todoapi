from rest_framework import serializers
from todo.models import Todo,Profile,Like
from django.contrib.auth.models import User
from comment.serializers import CommentSerializers

class TodoUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username',]

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class TodoListSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True,read_only=True)
    #comments = serializers.StringRelatedField(many=True)
    #comments = serializers.SlugRelatedField(many=True,slug_field="description",read_only=True)
    #detail = serializers.SerializerMethodField()
    #comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    likes = LikeSerializers(many=True,read_only=True)
    user = TodoUserSerializers(read_only=True)
    class Meta:
        model = Todo
        fields = ['id','user','todo_list','title','image','description','comments','likes']
    
    def get_detail(self,obj):
        return [obj.title,obj.description]
    
    def validate_todo_list(self,value):
        if len(value) <= 5:
            raise serializers.ValidationError('The todo_list should not be less than 5 letters')
        not_allowed = ['+','=','#','@']
        for i in not_allowed:
            if i in value:
                raise serializers.ValidationError(f'{i} is not allowed in the todo_list')
            return value
    '''
    def validate(self,data):
        title = data["title"]
        if len(title) <= 5:
            raise serializers.ValidationError('The usermust not be less than 5 words')
        return data
    def validate_description(self,info):
        if len(info) <= 10:
            raise serializers.ValidationError("The description should be more than 10 characters")
        offensive_words = ['rape','murder','money laundering']
        for bad in offensive_words:
            if bad in info:
                raise serializers.ValidationError(f'{info} is a word not allowed in the description')
            return info
'''
class TodoDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class SearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['todo_list','title','description']

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['marital_status','age','occupation']

class UserSerializers(serializers.ModelSerializer):
    profile = ProfileUserSerializers(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','password','last_name','first_name','email','profile']
        #This is a serializer