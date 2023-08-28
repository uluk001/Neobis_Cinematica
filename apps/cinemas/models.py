from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from apps.movies.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    is_open = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    name = models.CharField(max_length=50)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    is_3d = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.cinema.name}'


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room.name} - {self.row}{self.number}'


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.movie.title} - {self.room.name} - {self.start_time}'


@receiver(pre_save, sender=Seat)
def validate_seat_capacity(sender, instance, **kwargs):
    if instance.room and instance.room.capacity <= instance.room.seat_set.count():
        raise ValidationError("The room is already at full capacity.")
