from urllib import request
from .models import Article
from django.shortcuts import render, redirect

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
    articles = Article.objects.all().order_by("create_at")
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
    # context = {
    #     "article": article,
    # }
    # return render(request, "create.html", context)
    # return redirect("articles")
    return redirect("article_detail", article.id)


	# title = request.POST.get("title")
	# content = request.POST.get("content")
	# article = Article(title=title, content=content)
	# article.save()
  # return redirect("article_detail", article.id)

def article_detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
      "article": article,
  }
  return render(request, "article_detail.html", context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
      article.delete()
      return redirect("articles")
  return redirect("article_detail", article.pk)


def edit(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
	    "article": article,
	}
	return render(request, "edit.html", context)

def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get("title")
  article.content = request.POST.get("content")
  article.save()
  return redirect("article_detail", article.pk)