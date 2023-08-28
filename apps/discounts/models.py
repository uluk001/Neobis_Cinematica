from django.db import models
from apps.users.models import CustomUser

class Discount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.user.username} - {self.percentage}'
