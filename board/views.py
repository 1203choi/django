from django.shortcuts import render, get_object_or_404, redirect
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

def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # 질문이 없으면 404 에러 발생
    Answer(question=question, 
           content=request.POST.get('content')  # POST 요청에서 'content' 필드의 값을 가져옴, 없으면 빈 문자열
           ).save()  # 답변 생성
    return redirect('board:question_detail', question_id=question.id)

from django.shortcuts import render, redirect
from .models import Question

def create_question(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        Question.objects.create(subject=subject, content=content)
        return redirect('board:board_index')  # 질문 목록 페이지로 리디렉션
    return render(request, 'board/create_question.html')