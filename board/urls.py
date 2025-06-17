from django.urls import path
from . import views

# 네임스페이스
# 사용할떄는 board:question_list 와 같이 사용
app_name = 'board'

# URL 패턴정의
urlpatterns = [
    path('', views.index, name='board_index'),  # board 앱의 index 뷰를 'board_index'라는 이름으로 매핑
    # path('test/abc', views.index), # board 앱의 index 뷰를 기본 URL로 설정
    path('<int:question_id>/', views.detail, name='board_detail'),  # 특정 질문의 상세 페이지를 'board_detail'이라는 이름으로 매핑
]