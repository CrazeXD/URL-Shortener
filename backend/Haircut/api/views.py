from django.http import JsonResponse
from main.models import URL
from django.views.decorators.csrf import csrf_exempt
import secrets
import json

# Create your views here.
@csrf_exempt
def shorten(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=405)

    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        data = request.POST

    url = data.get('url')
    alias = data.get('alias', '')

    if not url:
        return JsonResponse({'error': 'URL is required'}, status=400)

    if alias == '':
        alias = secrets.token_urlsafe(5)
    elif URL.objects.filter(alias=alias).exists():
        return JsonResponse({'error': 'Alias already exists. Please choose another one.'}, status=400)

    new_url = URL(url=url, alias=alias)
    new_url.save()
    
    return JsonResponse({'url': url, 'alias': alias})