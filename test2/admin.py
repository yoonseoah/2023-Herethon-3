from django.contrib import admin
from .models import Student
from .forms import StudentForm

# 생략

@admin.register(Student)
class StudentAmin(admin.ModelAdmin):
    form = StudentForm