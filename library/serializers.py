from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import Book, AudioBook, Like, Favorites


class BookListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Book
        fields = ('owner', 'title', 'price', 'image')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr


class BookDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        return repr


class AudioBookListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = AudioBook
        fields = ('owner', 'title', 'price', 'image')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr


class AudioBookDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = AudioBook
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        return repr


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ('owner', 'book', 'audio_book')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('book', 'audio_book')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['books'] = BookListSerializer(instance.post).data
        repr['audio_books'] = AudioBookListSerializer(instance.post).data
        return repr