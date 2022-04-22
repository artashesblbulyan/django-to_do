from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('profile/<int:user_id>', views.user_profile, name="user_profile"),
    path('profile/<int:profile_id>/update', views.profile_update, name="profile_update"),
]