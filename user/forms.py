from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nickname', 'user_id', 'email']

class ChangeInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nickname', 'user_id', 'email', 'profileImg']