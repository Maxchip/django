from django.db import models

# Create your models here.

class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_days = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"ID:{self.id} from {self.origin_country} to {self.destination_country} for {self.number_of_days} days at ${self.price}"