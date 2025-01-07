from django.urls import path
from todo import views
from todo.views import UsersList,CreateComment,Like
urlpatterns = [
    path('', views.index),
    path('todo_details/<int:id>', views.todo_details,name="todo_details"),
    path('todo_details/<int:todo_id>/likes',Like.as_view()),
    path('todo_create',views.todo_create),
    path('delete_todo/<int:id>', views.delete_todo),
    path('update_todo/<int:id>',views.update_todo),
    path('search', views.search),
    path('users',UsersList.as_view()),
    path('<int:todo_id>/create_comment',CreateComment.as_view()),
]