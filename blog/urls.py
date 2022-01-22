# blog/urls.py
from django.urls import path
from blog.views import BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]