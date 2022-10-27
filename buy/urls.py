from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateOrderView.as_view()),
    path('list/', views.UserOrderList.as_view()),
]