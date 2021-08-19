from django.conf.urls import url
from . import views

app_name = 'article_app'

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^create/$', views.create_article, name='article_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
]
