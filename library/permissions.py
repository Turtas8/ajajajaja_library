from rest_framework.permissions import BasePermission
from .models import Book
from django.shortcuts import get_object_or_404


# class IsAuthor(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user == obj.owner


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            book_id = int(request.data['book'])
            owner = get_object_or_404(Book, id=book_id).owner
            return request.user == owner
        except:
            return False