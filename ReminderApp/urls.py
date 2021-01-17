from django.urls import path
from ReminderApp import views

urlpatterns = [
    path('v1/reminders', views.reminder_list),
    path('v1/reminders/<int:pk>/', views.reminder_detail)
]