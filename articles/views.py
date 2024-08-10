from urllib import request

from django.shortcuts import render


# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


# response = HttpResponse("<h1>Hello, Django!</h1>")
# return response

def hello(request):
    name = "희경"
    tags = ["파이썬", "장고", "html", "css", "js"]
    books = ["한글", "영어"]
    context = {
        "name": name,
        "tags": tags,
        "books": books
    }
    return render(request, "hello.html", context)


def data_throw(request):
    return render(request, "data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "data": message,
    }
    return render(request, "data_catch.html", context)
# return render(request, "data_catch.html")
