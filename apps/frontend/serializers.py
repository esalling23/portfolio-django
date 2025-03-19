from rest_framework import serializers
from portfolio.lib.parse_url import get_base_url

from .models import ContentModel

class ContentModelSerializer(serializers.ModelSerializer):
    about_img_safe = serializers.SerializerMethodField()
    def get_about_img_safe(self, obj):
        return get_base_url(obj.about_img.url)

    class Meta: 
        model = ContentModel
        fields = (
          'home_title', 
          'about_description',
          'about_img_safe',
          'typewriter_texts',
          'resume'
        )
