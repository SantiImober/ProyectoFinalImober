from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.PostListView.as_view(), name='post_list'),
    path('pages/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('pages/create/', views.PostCreateView.as_view(), name='post_create'),
    path('pages/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('pages/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('pages/<int:pk>/like/', views.like_post, name='like_post'),
]