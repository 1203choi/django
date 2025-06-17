from django.urls import path
from . import views

# 네임스페이스
# 사용할떄는 board:question_list 와 같이 사용
app_name = 'board'

# URL 패턴정의
urlpatterns = [
    path('', views.index, name='board_index'),
    path('<int:question_id>/', views.detail, name='board_detail'),
    path('question/create/', views.create_question, name='create_question'),
    
]