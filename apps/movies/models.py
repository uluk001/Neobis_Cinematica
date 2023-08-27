from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    is_there_at_the_box_office = models.BooleanField(default=False)
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    trailer = models.FileField(upload_to='trailers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'