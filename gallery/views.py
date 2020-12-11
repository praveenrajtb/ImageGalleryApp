from django.shortcuts import render
from django_filters.views import FilterView
from .filtersets import GalleryFilter
from .models import Gallery
from django.views.generic.edit import CreateView


class GalleryList(FilterView):
    model = Gallery
    context_object_name = 'images'
    filterset_class = GalleryFilter
    template_name = 'gallery/index.html'
    paginate_by = 20


class GalleryCreate(CreateView):
    model = Gallery
    fields = ['image', 'category']
    template_name = 'gallery/upload.html'
