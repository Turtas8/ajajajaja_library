from django.urls import path
from comment import views


urlpatterns = [
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]