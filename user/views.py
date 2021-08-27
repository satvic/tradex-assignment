from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm
from .models import Post


@login_required
def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form = PostForm()
            messages.success(request, "Successfully created")
            return redirect('view_all')
    return render(request, 'user/post-form.html', {'form': form})


def view_all(request):
    posts = Post.objects.all()
    return render(request, 'user/all-posts.html', {'posts': posts})


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})
