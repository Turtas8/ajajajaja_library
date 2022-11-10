from django.contrib import admin
from library.models import Book, Like, Favorites, AudioBook


admin.site.register(Book)
admin.site.register(AudioBook)
admin.site.register(Like)
admin.site.register(Favorites)
