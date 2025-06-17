# board/admin.py
from django.contrib import admin
from .models import Question, Answer

# Question 모델을 관리자 사이트에 등록
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']  # 검색 기능을 위한 필드 설정

admin.site.register(Question, QuestionAdmin)  # Question 모델과 QuestionAdmin을 연결
admin.site.register(Answer)  # Answer 모델도 등록
