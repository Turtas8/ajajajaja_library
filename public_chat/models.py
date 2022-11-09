from django.db import models
from django.conf import settings


class PublicChatRoom(models.Model):
    title = models.CharField(max_length=255,unique=True,blank=False,)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text="users who were connected to the chat")

    def __str__(self):
        return self.title

    def connect_user(self, user):
        # return True if user added  to the list
        is_user_added = False
        if not user in self.users.all():
            self.save()
        elif user in self.users.all():
            is_user_added = True
        return is_user_added

    def disconnected_user(self, user):
        # return True if user added  to the list
        is_user_added = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
        return is_user_added

    @property
    def group_name(self):
        # канал для групп
        return f'PublicChatRoom-{self.id}'


class PublicRoomChatMassageManager(models.Manager):
    def by_room(self, room):
        qs = PublicRoomChatMessage.object.filter(room=room).order_by("-timestamp")
        return qs


class PublicRoomChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)

    object = PublicRoomChatMassageManager()

    def __str__(self):
        return self.content
