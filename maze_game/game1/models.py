from django.db import models

class PlayerScore(models.Model):
    name = models.CharField(max_length=100)
    moves = models.IntegerField()
    time_elapsed = models.CharField(max_length=20)  # Storing time as a string
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.moves} moves - {self.time_elapsed}"
