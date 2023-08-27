from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:15]}'