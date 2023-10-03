from django.db import models
import uuid
# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    mileage = models.DecimalField(max_digits=4,decimal_places=2)
    avg_speed = models.IntegerField()
    date_posted = models.DateField()

    def __str__(self):
        return f"{self.name}:{self.mileage}"