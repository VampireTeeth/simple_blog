from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
  blogs = BlogArticle.objects.all()
  user = None
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)

  return render(request, "index.html", 
      dict(testvar="Hello, Django template!",
        blogs=blogs,
        user=user))



