# from rest_framework import serializers
# from models import PublicChatRoom
#
#
# class ChatItemSerializer(serializers.ModelSerializer):
#     owner = serializers.CharField(write_only=True, blank=False)
#     room = serializers.CharField(write_only=True, blank=False)
#     timestamp = serializers.DateTimeField(auto_now_add=True)
#     content = serializers.CharField(write_only=True, blank=False)
#
#
# class ChatItemModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PublicChatRoom
#         fields = '__all__'