from urllib import request
from django.shortcuts import render
from .models import Article


# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


# response = HttpResponse("<h1>Hello, Django!</h1>")
# return response

# def hello(request):
#     name = "희경"
#     tags = ["파이썬", "장고", "html", "css", "js"]
#     books = ["한글", "영어"]
#     context = {
#         "name": name,
#         "tags": tags,
#         "books": books
#     }
#     return render(request, "hello.html", context)
# heloo.html_ change


def data_throw(request):
    return render(request, "data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "data": message,
    }
    return render(request, "data_catch.html", context)


# return render(request, "data_catch.html")
def articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)


def new(request):
    return render(request, "new.html")


def create(request):
    # POST 방식으로 전달된 데이터를 받아서
    title = request.POST.get("title")
    content = request.POST.get("content")

    # 받은 데이터를 Article 모델을 이용해서 저장
    article = Article(title=title, content=content)
    article.save()
    context = {
        "article": article,
    }
    return render(request, "create.html", context)
