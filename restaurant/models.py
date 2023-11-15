from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.IntegerField(primary_key=True, max_digits=11)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(max_digits=6)
    bookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    id = models.IntegerField(primary_key=True, max_digits=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.Integer(max_digits=5)

    def __str__(self) -> str:
        return self.title
