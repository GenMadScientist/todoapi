from django.urls import path
from comment.views import CommentList,CommentDetail,CommentView,ThumbsUp,ThumbsDown


urlpatterns = [
    path('',CommentList.as_view()),
    path('<int:todo_id>',CommentView.as_view()),
    path('comment-details/<int:comment_id>',CommentDetail.as_view()),
    #path('comment-details/<int:comment_id>/thumbsup/',ThumbsUp.as_view())
    path('comment-details/<int:comment_id>/thumbsup',ThumbsUp.as_view()),
    path('comment-details/<int:comment_id>/thumbsdown',ThumbsDown.as_view())
]