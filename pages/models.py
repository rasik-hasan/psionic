from django.db import models

# Create your models here.


class Userdata(models.Model):
    name = models.CharField(max_length=80)
    pnumber = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)

    def __str__(self):
        return self.name
