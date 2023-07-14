from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User

# Create your models here.
class LocationSub(models.Model):
    country = models.CharField(max_length=10)              # 국가
    city = models.CharField(max_length=20)                # 도시
    # locate_city = models.CharField        # 도시 위치(위도 경도)
    star_avg_city = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.country

class ReviewSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    location = models.ForeignKey(LocationSub, on_delete=models.CASCADE, default='')
    star_avg = models.DecimalField(max_digits=4, decimal_places=2)  # 총 평점 별점 소수점 이하 2자리수 까지 저장
    star_danger = models.IntegerField()  # 치안 별점
    star_price = models.IntegerField()  # 물가 별점
    star_traffic = models.IntegerField()  # 교통 편의성 별점
    star_leisure = models.IntegerField()  # 즐길 거리 별점
    star_food = models.IntegerField()  # 먹거리 별점

    def __str__(self):
        return str(self.user.nickname)



class ReviewRating(models.Model):
    review = models.ForeignKey(ReviewSub, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(LocationSub, on_delete=models.CASCADE)
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location