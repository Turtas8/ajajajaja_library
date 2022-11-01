from .celery import app
from account.send_email import send_confirmation_email
from django.core.mail import send_mail
from account.models import SpamContacts


@app.task
def send_email_task(user, code):
    send_confirmation_email(user, code)


@app.task
def send_spam_email():
    for user in SpamContacts.objects.all():
        send_mail(
            'Spam Spam Spam',
            'This is spam letter for you by Turat',
            'turatbek.imankulov@gmail.com',
            [user.email],
            fail_silently=False,
        )