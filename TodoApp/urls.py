from django.urls import path
from TodoApp import views

urlpatterns = [
    path('api/v1/boards', views.BoardsList.as_view()),
    path('api/v1/boards/<int:pk>/', views.BoardDetail.as_view()),
    path('api/v1/boards/<int:pk>/todos/', views.TodosList.as_view()),
    path('api/v1/boards/<int:pk>/todos/<int:todopk>', views.TodoDetail.as_view()),
]