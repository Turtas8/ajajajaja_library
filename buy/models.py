from django.db import models
from django.contrib.auth import get_user_model
from library.models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.send_email import send_notification


User = get_user_model()


STATUS_CHOICES = (
    ('buy', 'Куплено'),
    ('read', 'Читать')
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ManyToManyField(Book, through=OrderItem)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} -> {self.user}'


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, *args, **kwargs):
    send_notification(instance.user, instance.id, instance.total_sum)
    products = OrderItem.objects.filter(order=instance)
    total_price = 0
    for item in products:
        price = item.quantity * item.product.price
        total_price += price

    send_notification(instance.user, instance.id, total_price)
