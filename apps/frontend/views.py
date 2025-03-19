from django.http import JsonResponse

from .models import ContentModel
from .serializers import ContentModelSerializer

# Content API endpoint
def content_index(request):
    """Index request to display content"""
    content = ContentModel.objects.first()
    print(content)
    serializer = ContentModelSerializer(content)
    print(serializer.data)
    return JsonResponse({ 'content': serializer.data })
