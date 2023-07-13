from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


# 글자 수 실시간 뜨기 (별점 수 실시간 뜨기로 바꿔야 함)
# class University(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name

# review 별점 모델
class Review(models.Model):
    # 자동으로 생성되는 pk값이 있다.
    #user p.k. =           # 사용자 primary key
    #city p.k =            # 도시 primary key
    star_avg = models.DecimalField(max_digits=4, decimal_places=2)              # 총 평점 별점 소수점 이하 2자리수 까지 저장
    star_danger =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                                          # 치안 별점
    star_price =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                                           # 물가 별점
    star_traffic =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                                         # 교통 편의성 별점
    star_leisure =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                                         # 즐길 거리 별점
    star_food =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                                            # 먹거리 별점
    
    def __str__(self):
        return str(self.pk)

# 국가 및 도시 모델
class Location(models.Model):
    country = models.CharField(max_length=10)              # 국가
    city = models.CharField(max_length=20)                # 도시
    # locate_city = models.CharField        # 도시 위치(위도 경도)
    star_avg_city = models.DecimalField(max_digits=4, decimal_places=2)              # 특정 도시의 총 평점 = 총 평점 별점 소수점 이하 2자리수 까지 저장
    # 자공으로 생성되는 pk값이 있다.
    
#* crud 기능
class Index(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    date = models.DateTimeField(auto_now=True)
    
    
def __str__(self):
    # return self.titles
    return self.star_avg


# 방법 2 python models (사례 따라하기)
class Rate(models.Model):
# class Rate(AbstractBaseRating):
    name = models.CharField(max_length = 140)
    ratings =  GenericRelation(Rating, related_query_name= 'object_list')

    def __str__(self):
        return self.name