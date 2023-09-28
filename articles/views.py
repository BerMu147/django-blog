from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# View for listing all articles.
def articles(request):
   all_articles = Article.objects.all().order_by('date')
   return render(request, 'articles/article.html', {'all_articles':all_articles})

# View for article preview - article details
def article_detail(request, slug):
   article = Article.objects.get(slug=slug)
   return render(request,'articles/article_detail.html', {'article':article})

# View for article creation - adding new article
# @login_required(login_url="/accounts/login/")
def article_create(request):
   if request.method == 'POST':
      form = forms.CreateArticle(request.POST, request.FILES)
      if form.is_valid():
         return redirect('articles:list')
   else:
      form = forms.CreateArticle()
   return render(request,'articles/article_create.html', {'article_new':form})