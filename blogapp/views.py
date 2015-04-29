from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
  blogs = BlogArticle.objects.all()
  if request.user and request.user.is_authenticated():
    user = request.user
  else:
    user = None
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
  return render(request, "index.html", dict(blogs=blogs, user=user))


def createBlog(request):
  newBlog = BlogArticle()
  newBlog.title = request.POST['title']
  newBlog.author = request.user
  newBlog.blog_content = request.POST['blog_content']
  newBlog.save()
  blogs = BlogArticle.objects.all()
  return render(request, "index.html", dict(blogs=blogs, user=request.user))
