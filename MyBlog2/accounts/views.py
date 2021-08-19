from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def signup_view(request):

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect('article_app:articles')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', context={'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article_app:articles')
                #log in the user


    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse_lazy('article_app:articles'))
