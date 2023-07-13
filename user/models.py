from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, nickname, user_id, email, profileImg, password=None):
        if not nickname :
            raise ValueError("닉네임을 입력해야 합니다.")
        if not user_id :
            raise ValueError("아이디를 입력해야 합니다.")
        if not email :
            raise ValueError("이메일을 입력해야 합니다.")

        user = self.model(
            nickname=nickname,
            user_id=user_id,
            email=self.normalize_email(email),
            profileImg=profileImg
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, user_id, email, profileImg, password):
        user = self.create_user(
            nickname=nickname,
            user_id=user_id,
            email=email,
            profileImg=profileImg,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=15, unique=True)
    user_id = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    profileImg = models.ImageField(upload_to='profiles/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'user_id' # username, 아이디로 사용할 필드
    REQUIRED_FIELDS = ['nickname', 'email', 'profileImg']

    objects = UserManager()

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['date_joined']
=======

# Create your models here.
>>>>>>> 713bf834585d063a0649dcd4c5599f6ec25df72c
