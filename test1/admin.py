from django.contrib import admin
from .models import Review, Location
from .forms import ReviewForm, LocateForm
# from .forms import UniversityForm, StudentForm

# @admin.register(University)
# class CountryAmin(admin.ModelAdmin):
#     form = UniversityForm

# @admin.register(Student)
# class PostAmin(admin.ModelAdmin):
#     pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocateForm