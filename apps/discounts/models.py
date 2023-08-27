from django.db import models

class Discount(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.user.username} - {self.percentage}'
