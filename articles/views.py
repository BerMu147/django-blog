from django.shortcuts import render
from .models import Article

# Create your views here.
def articles(request):
   all_articles = Article.objects.all().order_by('date')
   return render(request, 'articles/article.html', {'all_articles':all_articles})