from django.contrib import admin
from account.models import CustomUser, SpamContacts


admin.site.register(CustomUser)
admin.site.register(SpamContacts)
