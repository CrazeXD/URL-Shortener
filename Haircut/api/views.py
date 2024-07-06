from django.shortcuts import render
from django.http import JsonResponse
from main.models import URL, User
import secrets
# Create your views here.

def create_api_key(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.api_key = secrets.token_urlsafe(32)
        user.save()
        return render(request, 'api_key.html', {'api_key': user.api_key})
    return

def create_url(request):
    if request.method == 'POST':
        url = request.POST['url']
        alias = request.POST['alias']
        user = User.objects.get(api_key = request.POST['api_key'])
        new_url = URL(url=url, alias=alias, owner=user)
        new_url.save()
        return JsonResponse({'url': url, 'alias': alias})
    return
