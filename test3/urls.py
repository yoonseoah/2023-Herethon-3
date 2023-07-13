from test3 import views
from django.urls import path, include
app_name = 'test3'

urlpatterns = [
    # path(사용자의 요청 , 내가 연결할 view의 함수), 이름 붙여주기
    # path('', views.index, name='index' ),    # '' = localhost/test1/
    
    # crud
    path("", views.indexs),
    # path('rate/', views.rate),
    path('rate/<int:post_id>/<int:rating>/', views.rate),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)