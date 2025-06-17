from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer

def index(request): 
    # 모든 질문 조회
    questions = Question.objects.order_by('-created_at')  
    # 템플릿 렌더링
    return render(request, 'board/index.html', {'questions': questions})

# Create your views here.

def detail(request, question_id):
    # 특정 질문 조회
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)  # 질문이 없으면 404 에러 발생
    
    # 템플릿 렌더링
    return render(request, 'board/detail.html', {'question': question})