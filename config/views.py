from django.shortcuts import render

# from django.http import HttpResponse


def main(request):
    return render(request, "main.html")


def burger_list(request):
    return render(request, "burger_list.html")


# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다")


# def burger_list(requset):
#     return HttpResponse("pyburger의 햄버거 목록입니다")
