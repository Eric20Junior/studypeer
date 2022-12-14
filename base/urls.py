from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('register/', views.registerView, name="register"),


    path('', views.home, name="home"),
    path('room/<int:pk>/', views.room, name="room"),
    path('profile/<int:pk>/', views.ProfileView, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<int:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<int:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<int:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user', views.updateUser, name="update-user"),

    path('topics', views.topicsPage, name="topics"),
    path('activity', views.activityPage, name="activity"),

]

