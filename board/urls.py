from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='board_index'),  # board 앱의 index 뷰를 'board_index'라는 이름으로 매핑
    path('test/abc', views.index) # board 앱의 index 뷰를 기본 URL로 설정
]