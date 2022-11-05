from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    # artise_id = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.TextField()
    # song_id = models.IntegerField()
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)

