from django.urls import path
from . import views


urlpatterns = [
    # URL form : "/api/v1/messages/1/2"
    path('api/v1/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/v1/messages/"
    path('api/v1/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/v1/users/1"
    path('api/v1/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/v1/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
]