from rest_framework import serializers
from portfolio.lib.parse_url import get_base_url

from .models import Project, Category, Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tool
        fields = ('name', 'group')

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    main_img_safe = serializers.SerializerMethodField()
    def get_main_img_safe(self, obj):
        return get_base_url(obj.main_img.url)
    
    thumbnail_img_safe = serializers.SerializerMethodField()
    def get_thumbnail_img_safe(self, obj):
        return get_base_url(obj.thumbnail_img.url)

    class Meta:
        model = Project
        fields = [
						'id',
            'main_img_safe', 
            'thumbnail_img_safe', 
            'title', 
            'subtitle', 
            'date_started', 
            'date_ended', 
            'description', 
            'more_link', 
            'git_link',
            'categories',
            'is_hidden'
        ]