from django.shortcuts import render, redirect
from .models import URL, User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password)
        return redirect('/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            return redirect('/')
    return render(request, 'login.html')

def site(request, alias):
    if request.method == 'GET':
        url = URL.objects.get(alias=alias).url
        return redirect(url)
    return redirect('/')
