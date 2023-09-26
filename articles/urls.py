from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.articles),
    re_path('(?P<slug>[\w-]+)/', views.article_detail)
]