from django import forms
from .models import Review, Location
from .widgets import starWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'star_danger': starWidget,          # 치안 별점
            'star_danger_': starWidget,          # 치안 별점
            'star_price': starWidget,           # 물가 별점
            'star_traffic': starWidget,         # 교통 편의성 별점
            'star_leisure': starWidget,         # 즐길 거리 별점
            'star_food': starWidget,            # 먹거리 별점 
        }
        
        
class LocateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        
