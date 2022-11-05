from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artise_id = models.IntegerField()

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()
