from django.shortcuts import render
from django.http import JsonResponse
from main.models import URL, User
import secrets
# Create your views here.

def create_api_key(request):
    if request.method == 'POST':
        if request.user.is_aunthenticated == False:
            return JsonResponse({'error': 'Not authenticated'})
        user = User.objects.get(username=request.user.username)
        user.api_key = secrets.token_urlsafe(32)
        user.save()
        return JsonResponse({'api_key': user.api_key})
    return

def create_url(request):
    if request.method != 'POST':
        return
    url = request.POST['url']
    alias = request.POST['alias']
    if alias == '':
        alias = secrets.token_urlsafe(5)
    elif URL.objects.filter(alias=alias).exists():
        return JsonResponse({'error': 'Alias already exists'})
    user = User.objects.get(api_key = request.POST['api_key'])
    new_url = URL(url=url, alias=alias, owner=user)
    new_url.save()
    return JsonResponse({'url': url, 'alias': alias})

def check_url(request):
    if request.method != 'POST':
        return
    alias = request.POST['alias']
    if URL.objects.filter(alias=alias).exists():
        return JsonResponse({'exists': True, 'url': URL.objects.get(alias=alias).url})
    return JsonResponse({'exists': False})