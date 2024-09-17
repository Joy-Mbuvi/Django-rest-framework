#specify a class that will take the model and turn it into json data

from rest_framework import serializers
from.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id','title','content','published_date']