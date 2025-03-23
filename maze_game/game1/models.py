from django.db import models

# Create your models here.
from django.db import models

class PlayerScore(models.Model):
    name = models.CharField(max_length=100)
    moves = models.IntegerField()
    time_elapsed = models.DecimalField(max_digits=5, decimal_places=2)  # Time in seconds with two decimal places

    def __str__(self):
        return f"{self.name} - {self.moves} moves, {self.time_elapsed} seconds"
