import os
import sys
import django

# Django 환경 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 프로젝트 루트 경로 추가
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from board.models import Question  # 절대 경로로 import

def main():
    for i in range(1,101):
        Question(
            subject=f"질문 제목 {i}",
            content=f"질문 내용 {i}"
        ).save()

if __name__ == '__main__':
    main()