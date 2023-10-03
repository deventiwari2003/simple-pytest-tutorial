from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=300)
    date_posted = models.DateField()

    def __str__(self):
        return self.name + "_" + self.email
