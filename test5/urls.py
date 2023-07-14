from test5.views import Rateeee
from django.urls import path


app_name = 'test5'

urlpatterns = [
    path('', Rateeee, name='rate-movie'),

]