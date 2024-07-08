from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from .models import URL, User

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

@csrf_exempt
@require_http_methods(["POST"])
def registration_api_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()
        return JsonResponse({'message': 'User created'}, status=201)
