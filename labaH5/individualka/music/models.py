from django.db import models


class Song(models.Model):
    song_id = models.IntegerField(null=False, primary_key=True, verbose_name="song_id")
    song_title = models.CharField(null=False, max_length=100, verbose_name="song_title")
    author_name = models.CharField(null=False, max_length=100, verbose_name="author_name")
    release_date = models.DateField(null=False, verbose_name="release_date")

    def __str__(self):
        return self.author_name + " - " + self.song_title

    class Meta:
        verbose_name_plural = "Songs"
        verbose_name = "Song"
        ordering = ["-song_id"]


class Album(models.Model):
    album_id = models.IntegerField(null=False, primary_key=True, verbose_name="album_id")
    album_title = models.CharField(null=False, max_length=100, verbose_name="album_title")
    song_id = models.ForeignKey(Song, null=False, on_delete=models.PROTECT, verbose_name="song_id")
    author_name = models.CharField(null=False, max_length=100, verbose_name="author_name")
    release_date = models.DateField(null=False, verbose_name="release_name")

    def __str__(self):
        return self.album_title

    class Meta:
        verbose_name_plural = "Albums"
        verbose_name = "Album"
        ordering = ["-album_id"]


class Order(models.Model):
    order_id = models.IntegerField(null=False, primary_key=True, verbose_name="order_id")
    album_id = models.ForeignKey(Album, null=False, on_delete=models.PROTECT, verbose_name="album_id")
    customer_name = models.CharField(null=False, max_length=100, verbose_name="customer_name")
    date = models.DateField(null=False, verbose_name="date")

    def __str__(self):
        return "Order №" + str(self.order_id)

    class Meta:
        verbose_name_plural = "Orders"
        verbose_name = "Order"
        ordering = ["-order_id"]
