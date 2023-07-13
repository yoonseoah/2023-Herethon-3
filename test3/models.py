from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.conf import settings
from user.models import User


class Post(models.Model):
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    
    # user = models.ForeignKey(user, on_delete=models.CASCADE)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"
    

# Create your models here.
    
class User_modle(models.Model):
    user_mo = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_mo.subject)
    