from django.contrib import admin
<<<<<<< HEAD
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'user_id', 'email']
    search_fields = ['nickname']
    exclude = ['password']
=======

# Register your models here.
>>>>>>> 713bf834585d063a0649dcd4c5599f6ec25df72c
