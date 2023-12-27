from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import CommentForm

from django.views.generic import ListView


def logout_view(request):
    logout(request)
    return redirect('post_list')


def main_news(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/main_news.html', {'posts': posts})


def culture_news(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/culture_news.html', {'posts': posts})


def interesting_news(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/interesting_news.html', {'posts': posts})


def politic_news(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/politic_news.html', {'posts': posts})


def economic_news(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/economic_news.html', {'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('post_list')
        else:
            # Пользователь ввел неправильные учетные данные
            messages.error(request, 'Неправильный логин или пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming you have user authentication
            comment.save()
            return redirect('post_detail', post_id=post_id)  # Redirect to post detail view
    else:
        form = CommentForm()
    return render(request, 'myapp/comment_form.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all()
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming you have user authentication
            comment.save()
            form = CommentForm()  # Clear the form after saving a comment
    else:
        form = CommentForm()

    return render(request, 'myapp/post_detail.html', {'posts': posts, 'post': post, 'comments': comments, 'form': form})