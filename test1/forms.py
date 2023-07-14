from django import forms
from .models import Review, Location
from .widgets import starWidget
from django.forms.widgets import Widget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            #'star_danger': starWidget,          # 치안 별점
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
        



# widgets.py 에서 인식 못해서 추가
class starWidget_2(Widget):
    input_type = 'rating'
    # template_name =  "widgets/star_rate.html"
    template_name =  "star_rate.html"

    class Media:
        css = {
            'all': [
                'widgets/rateit/rateit.css',
            ],
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            'widgets/rateit/jquery.rateit.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': 0,       # 최소 별 개수
            'max': 5,       # 최대 별 개수
            'step': 0,      # 0으로 하면 0.5단위, 1로 하면 1 단위
        })
        return attrs
    
    
    # html 파일로 위젯 불러오기 
    def render(self, name, value, attrs=None, renderer=None):
        # 위젯의 HTML 코드를 작성하여 반환
        # <div> 태그로 감싼 커스텀 위젯을 생성
        html = f'<div class="custom-widget">{value}</div>'
        return html