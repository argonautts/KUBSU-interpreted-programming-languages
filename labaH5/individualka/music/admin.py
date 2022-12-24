from django.contrib import admin

from .models import Song
from .models import Album
from .models import Order


class SongAdmin(admin.ModelAdmin):
    list_display = ("song_id", "song_title", "author_name", "release_date")
    list_display_links = ("song_id", "song_title")
    search_fields = ("song_id", "song_title", "author_name", "release_date")


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_id", "album_title", "author_name", "song_id", "release_date")
    list_display_links = ("album_id", "album_title", "song_id")
    search_fields = ("album_id", "album_title", "song_id", "author_name", "release_date")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "album_id", "customer_name", "date")
    list_display_links = ("order_id", "album_id")
    search_fields = ("order_id", "album_id", "customer_name", "date")


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Order, OrderAdmin)
