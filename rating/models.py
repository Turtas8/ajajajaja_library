from django.db import models
from library.models import Book
from django.contrib.auth import get_user_model


User = get_user_model()


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    marks = ((one, 'Too bad!'), (two, 'Too Bad!'), (three, 'Bad!'), (four, 'Not Good!'), (five, 'Normal!'),
             (six, 'Better than Normal!'), (seven, 'Good!'), (eight, 'Very Good!'), (nine, 'Very Very Good!'), (ten, 'Excellent'))


class Review(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
