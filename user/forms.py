from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        User = get_user_model()
        model = User
        fields = ['nickname', 'user_id', 'email']

class ChangeInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nickname', 'user_id', 'email', 'profileImg']