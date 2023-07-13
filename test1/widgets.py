from django import forms
from django.forms.widgets import Widget

#class CounterTextInput(forms.TextInput):
    #template_name = "widgets/counter_text.html"
    
class starWidget(forms.TextInput):
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
    
    
    
    
    # 새로운 시도.. html 형식으로 반환하기
    # {% load starWidget_2 %} 인식 못함
class starWidgetTest(Widget):
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