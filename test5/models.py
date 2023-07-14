from django.db import models
from user.models import User

# Create your models here.
RATE_CHOICES = [
    (1, '1 - F'),
    (2, '2 - D'),
    (3, '3 - C'),
    (4, '4 - B'),
    (5, '5 - A'),
]

class Reviewww(models.Model):
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def  __str__(self):
        return self.user.username