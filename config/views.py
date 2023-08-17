from django.shortcuts import render
from burgers.models import Burger

# from django.http import HttpResponse


def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)
    # return render(request, "burger_list.html")

    # Template로 전달해줄 dict 객체
    context = {
        "burgers": burgers,  # burgers 키에 burgers 변수(QuerySet)를 전달한다.
    }
    return render(request, "burger_list.html", context)


def main(request):
    return render(request, "main.html")


# def burger_list(request):
#     return render(request, "burger_list.html")

""""""

# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다")


# def burger_list(requset):
#     return HttpResponse("pyburger의 햄버거 목록입니다")
