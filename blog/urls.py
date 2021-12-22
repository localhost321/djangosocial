from django.urls import path

from blog.models import Comment
from . import views
from .views import (PostCreateView, PostListView,
                   
                    PostUpdateView,
                    PostDeleteView,
                    )

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    # editted
    
    # path('like/<int:pk>',LikeView,name='like_post'),
    path('post/<int:pk>/like/', views.like, name='post-like'),
]
