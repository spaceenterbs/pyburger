from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, "main.html") # HttpResponse 대신 render 함수 사용
    # HttpResponse("안녕하세요, pyburger입니다")
    # View 함수가 문자열을 리턴하고 싶다면, 언제나 HttpResponse 객체 안에 담아서 돌려준다!

def burger_list(request):
    return render(request, "burger_list.html") # HttpResponse 대신 render 함수 사용
    # HttpResponse("pyburger의 햄버거 목록입니다")