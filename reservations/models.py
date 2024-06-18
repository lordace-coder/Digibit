from typing import Iterable
from django.db import models

# Create your models here.
class Reservation(models.Model):
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_created=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs) -> None:
        if Reservation.objects.filter(email= self.email).exists():
            raise Exception('email already exists')
        return super().save(*args, **kwargs)