from django.http import JsonResponse

from .models import ContentModel
from .serializers import ContentModelSerializer

# Content API endpoint
def content_index(request):
    """Index request to display content"""
    content = ContentModel.objects.first()
    serializer = ContentModelSerializer(content)
    return JsonResponse({ 'content': serializer.data })
