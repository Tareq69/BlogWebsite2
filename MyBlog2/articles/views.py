from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.
def articles(request):
    articles = Article.objects.all().order_by('publish_date')
    return render(request, 'articles/articles_list.html', context={'articles':articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', context={'article':article})

@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article_app:articles')
            #save form in database
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', context={'form':form})
