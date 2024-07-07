from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from .models import URL
from .serializers import UserRegisterSerializer
from rest_framework import status

@csrf_exempt
@require_http_methods(["GET"])
def site_view(request, alias):
    if request.method == 'GET':
        try:
            url = URL.objects.get(alias=alias).url
            return JsonResponse({'url': url})
        except URL.DoesNotExist:
            return JsonResponse({'error': 'URL not found'}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def registration_api_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
