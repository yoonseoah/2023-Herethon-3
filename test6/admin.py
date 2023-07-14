from django.contrib import admin
from .models import ReviewRating, LocationSub, ReviewSub

# Register your models here.
# 리뷰
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('star_avg', 'star_danger', 'star_price', 'star_traffic', 'star_leisure', 'star_food')

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'star_avg_city')

admin.site.register(ReviewSub, ReviewsAdmin)
admin.site.register(LocationSub, LocationsAdmin)
admin.site.register(ReviewRating)