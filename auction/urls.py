from django.conf.urls import url
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('category/<str:pk>/', views.category_list, name = 'category_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)