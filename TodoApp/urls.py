from django.urls import path
from TodoApp import views

urlpatterns = [
    path('api/v1/boards', views.board_list),
    path('api/v1/boards/<int:pk>/', views.board_detail),
    path('api/v1/boards/<int:pk>/todos/', views.todo_list),
    path('api/v1/boards/<int:pk>/todos/<int:todopk>', views.todo_detail),
]