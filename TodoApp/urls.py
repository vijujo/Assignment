# from django.conf.urls import url
from django.urls import path
from TodoApp import views

urlpatterns = [
    # path('api/v1/boards', views.BoardsList.as_view()),
    # path('api/v1/boards/<int:pk>/', views.BoardDetail.as_view()),
    # path('api/v1/boards/<int:pk>/todos/', views.TodosList.as_view()),
    # path('api/v1/boards/<int:pk>/todos/<int:todopk>', views.TodoDetail.as_view()),
    # url(r'^api/v1/boards/(?P<board_pk>\d+)/todos$', views.TodosList.as_view(), name='todos_of_a_board'),

    path('v1/boards', views.board_list),
    path('v1/boards/<int:pk>/', views.board_detail),

    path('v1/boards/<int:pk>/todos/', views.todos_of_board),
    path('v1/todos/open', views.todos_uncompleted),
    path('v1/todos/<int:pk>', views.todo_detail)

]
