from django.db import models
from django.contrib.auth import get_user_model
from library.models import Book


User = get_user_model()


class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.book} -> {self.created_at}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
