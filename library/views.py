from django.shortcuts import render
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from . import serializers
from .models import Book, AudioBook
from .permissions import IsAuthor
from rating.serializers import ReviewSerializer
# from comment.serializers import CommentSerializer
from rest_framework.response import Response
from .models import Like, Favorites
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookListSerializer
from .service import BookFilter, AudioBookFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'owner', 'author_name')
    # filter_fields = ('price',)
    # ordering_fields = ('price', 'author_name')
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookListSerializer
        return serializers.BookDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        elif self.action in ('create', 'add_to_liked', 'remove_from_liked', 'favorite_action', 'remove_from_favorites'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        book = self.get_object()
        if request.method == 'GET':
            reviews = book.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if book.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв!!', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, book=book)
        return response.Response(serializer.data, status=201)

    @action(['GET'], detail=True)
    def comments(self, request, pk):
        book = self.get_object()
        comments = book.comments.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        book = self.get_object()
        user = request.user
        if user.liked.filter(book=book).exists():
            return Response('This Movie is Already Liked!', status=400)
        Like.objects.create(owner=user, book=book)
        return Response('You Liked The Movie', status=201)

    @action(['DELETE'], detail=True)
    def remove_from_liked(self, request, pk):
        book = self.get_object()
        user = request.user
        if not user.liked.filter(book=book).exists():
            return Response('You Didn\'t Like This Movie!', status=400)
        user.liked.filter(book=book).delete()
        return Response('Your Like is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_likes(self, request, pk):
        book = self.get_object()
        likes = book.likes.all()
        serializer = serializers.LikeSerializer(likes, many=True)
        return Response(serializer.data)

    @action(['POST'], detail=True)
    def favorite_action(self, request, pk):
        book = self.get_object()
        user = request.user
        if user.favorites.filter(book=book).exists():
            user.favorites.filter(book=book).delete()
            return Response('Deleted From Favorites!', status=204)
        Favorites.objects.create(owner=user, book=book)
        return Response('Added to Favorites!', status=201)

    @action(['DELETE'], detail=True)
    def remove_from_favorites(self, request, pk):
        book = self.get_object()
        user = request.user
        if not user.favorites.filter(book=book).exists():
            return Response('This Movie is not in Favorites!', status=400)
        user.favorites.filter(book=book).delete()
        return Response('Your Favorite is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_favorites(self, request, pk):
        book = self.get_object()
        favorites = book.favorites.all()
        serializer = serializers.FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    @action(['DELETE'], detail=True)
    def remove_from_reviews(self, request, pk):
        book = self.get_object()
        user = request.user
        if not user.review.filter(book=book).exists():
            return Response('You are not Review This Movie!', status=400)
        user.review.filter(book=book).delete()
        return Response('Your Review is Deleted!', status=204)


class AudioBookViewSet(ModelViewSet):
    queryset = AudioBook.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_class = AudioBookFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AudioBookListSerializer
        return serializers.AudioBookDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        elif self.action in ('create', 'add_to_liked', 'remove_from_liked', 'favorite_action', 'remove_from_favorites'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        audio_book = self.get_object()
        if request.method == 'GET':
            reviews = audio_book.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if audio_book.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв!!', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, audio_book=audio_book)
        return response.Response(serializer.data, status=201)

    @action(['GET'], detail=True)
    def comments(self, request, pk):
        audio_book = self.get_object()
        comments = audio_book.comments.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        audio_book = self.get_object()
        user = request.user
        if user.liked.filter(audio_book=audio_book).exists():
            return Response('This Movie is Already Liked!', status=400)
        Like.objects.create(owner=user, audio_book=audio_book)
        return Response('You Liked The Movie', status=201)

    @action(['DELETE'], detail=True)
    def remove_from_liked(self, request, pk):
        audio_book = self.get_object()
        user = request.user
        if not user.liked.filter(audio_book=audio_book).exists():
            return Response('You Didn\'t Like This Movie!', status=400)
        user.liked.filter(audio_book=audio_book).delete()
        return Response('Your Like is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_likes(self, request, pk):
        audio_book = self.get_object()
        likes = audio_book.likes.all()
        serializer = serializers.LikeSerializer(likes, many=True)
        return Response(serializer.data)

    @action(['POST'], detail=True)
    def favorite_action(self, request, pk):
        audio_book = self.get_object()
        user = request.user
        if user.favorites.filter(audio_book=audio_book).exists():
            user.favorites.filter(audio_book=audio_book).delete()
            return Response('Deleted From Favorites!', status=204)
        Favorites.objects.create(owner=user, audio_book=audio_book)
        return Response('Added to Favorites!', status=201)

    @action(['DELETE'], detail=True)
    def remove_from_favorites(self, request, pk):
        audio_book = self.get_object()
        user = request.user
        if not user.favorites.filter(audio_book=audio_book).exists():
            return Response('This Movie is not in Favorites!', status=400)
        user.favorites.filter(audio_book=audio_book).delete()
        return Response('Your Favorite is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_favorites(self, request, pk):
        audio_book = self.get_object()
        favorites = audio_book.favorites.all()
        serializer = serializers.FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    @action(['DELETE'], detail=True)
    def remove_from_reviews(self, request, pk):
        audio_book = self.get_object()
        user = request.user
        if not user.review.filter(audio_book=audio_book).exists():
            return Response('You are not Review This Movie!', status=400)
        user.review.filter(audio_book=audio_book).delete()
        return Response('Your Review is Deleted!', status=204)


def auth(request):
    return render(request, 'oauth.html')
