from django.db import models
from apps.cinemas.models import Showtime, Seat
from apps.users.models import CustomUser

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.user.username} - {self.showtime.movie.title} - {self.seat.row}{self.seat.number}'
