from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='music_image/')
    audio = models.FileField(upload_to='music_audio/')

    def __str__(self):
        return self.title