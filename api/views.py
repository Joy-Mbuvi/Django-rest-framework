from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer

class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    lookup_field='pk'

def latestBlog(request):
    latest_post=BlogPost.objects.order_by('published_date').first()

    if latest_post:
        serializer=BlogPostSerializer(latest_post)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'message': 'No latest blogpost'},status=404)

def blog_post_count(request):
    number_of_post=BlogPost.objects.count()

    if number_of_post > 0:
        return JsonResponse({'total_blog_posts': number_of_post})
    else:
        return JsonResponse({'message': 'No blogposts Found'},status=404)
