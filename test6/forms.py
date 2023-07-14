from django import forms
from .models import  ReviewSub

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewSub
        fields = ['star_avg', 'star_danger', 'star_price', 'star_traffic', 'star_leisure', 'star_food']
