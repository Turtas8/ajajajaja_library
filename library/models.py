from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='books')
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images')
    text = models.URLField(max_length=1000)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class AudioBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='audio_books')
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='audio_books', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images')
    audio = models.FileField(upload_to='audio_books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')
    # audio_book = models.ForeignKey(AudioBook, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['owner', 'book']


class Favorites(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorites')
    # audio_book = models.ForeignKey(AudioBook, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['owner', 'book']