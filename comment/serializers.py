from comment.models import Comments
from rest_framework import serializers
from todo.models import Todo
#from comment.serializers import ThumbsupSerializers


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id','name','description','user','thumbsup','date_created']
        #thumbs = ThumbsupSerializers(many=True,read_only=True)
class TodoDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','name']

class CommentDetailSerializers(serializers.ModelSerializer):
    todo = TodoDetailsSerializers(read_only=True)
    class Meta:
        model = Comments
        fields = ['id','name','description','user','date_created','todo']

