from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import URL, User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})


def site(request, alias):
    if request.method == 'GET':
        try:
            url = URL.objects.get(alias=alias).url
            return JsonResponse({'url': url})
        except URL.DoesNotExist:
            return JsonResponse({'error': 'URL not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=405)
