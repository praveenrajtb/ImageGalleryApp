from django.urls import path
from . import views
from .models import Gallery

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryList.as_view(model=Gallery), name='gallery'),
    path('gallery/add/', views.GalleryCreate.as_view(), name='gallery-add'),
]
