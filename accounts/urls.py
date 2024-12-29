from django.urls import path
from accounts.views import Register, LogIn,LogOut,RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('register',RegisterUser.as_view()),
    path('login', LogIn.as_view()),
    path('logout', LogOut.as_view()),   
    path('jwt_login',TokenObtainPairView.as_view()),
    path('jwt_refresh',TokenRefreshView.as_view())
]