from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
# Create your views here.

def login_user(request):
    if request.method == 'POST':  # when user submits
        username = request.POST["username"] # grab
        password = request.POST["password"] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # remembers user
            redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html',{})
    

def register_user(request):
    if request.method == 'POST': # when user post
        form = UserCreationForm(request.POST) # use this inbuild django form with data received
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')
    
@login_required
def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'posts':post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
        
    
@login_required
def update_post(request, pk):
    post = Post.object.get(id=pk)
    form = PostForm(request.POST or None,request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_post.html', {'form':form, 'post': post})

@login_required
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'delete_post.html', {'post':post})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post': post})