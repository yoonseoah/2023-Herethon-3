from django.urls import path
from . import views

app_name = 'test6'

urlpatterns = [
    path('review_star/', views.star_review, name='star_review'),
    path('submit_review/<int:location_id>/', views.submit_review, name='submit_review'),
]