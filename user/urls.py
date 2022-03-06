from django.urls import path
from user import views

urlpatterns = [
    path('', views.home),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
]