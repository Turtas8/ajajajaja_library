from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Category
from . import serializers
from rest_framework.pagination import PageNumberPagination


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 1000


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    pagination_class = StandartResultPagination
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
