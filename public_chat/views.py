# from rest_framework import generics, permissions
# from .models import PublicChatRoom
# from . import serializers
#
# from .permissions import IsAuthor
#
#
# class ChatListView(generics.ListCreateAPIView):
#     queryset = PublicChatRoom
#     serializer_class = serializers.ChatItemSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PublicChatRoom.objects.all()
#     serializer_class = serializers.ChatItemSerializer
#
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [permissions.AllowAny()]
#         return [permissions.IsAuthenticated(), IsAuthor()]