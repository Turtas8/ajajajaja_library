from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    product = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Review
        fields = '__all__'