from django.urls import path, re_path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.articles, name="list"),
    re_path(r"^(?P<slug>[\w-]+)/$", views.article_detail, name="detail")
]