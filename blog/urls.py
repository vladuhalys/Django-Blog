# blog/urls.py
from django.urls import path
from blog.views import BlogDetailView, BlogListView, BlogCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]