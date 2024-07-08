from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import URL

@csrf_exempt
@require_http_methods(["GET"])
def site_view(request, alias):
    if request.method == 'GET':
        try:
            url = URL.objects.get(alias=alias).url
            if not url.startswith('http'):
                url = f'http://{url}'
            return JsonResponse({'url': url})
        except URL.DoesNotExist:
            return JsonResponse({'error': 'URL not found'}, status=404)
