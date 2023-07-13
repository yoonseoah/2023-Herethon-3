
from django import forms
from .models import Student
from .widgets import starWidget

# 생략

class StudentForm(forms.ModelForm):
    class Meta:
        meodel = Student
        fields = '__all__'
        widgets = {
            'grade': starWidget,
        }