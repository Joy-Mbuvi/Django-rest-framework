from django.urls import path
from . import views



urlpatterns=[
    path('blogposts/', views.BlogPostListCreate.as_view(),name='blogpost-view-create'),
    path('blogposts/<int:pk>',views.BlogPostRetrieveUpdateDestory.as_view(),name='blogpost-view-deleteupdate'),
    path('blogposts/latest/', views.latestBlog, name='latest_blog_post'),
    path('blogposts/count/', views.blog_post_count, name='number_of_blogpost'),

]
