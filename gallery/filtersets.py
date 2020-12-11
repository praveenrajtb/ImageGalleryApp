import django_filters
from gallery.models import Gallery


class GalleryFilter(django_filters.FilterSet):
    class Meta:
        model = Gallery
        fields = ['category']
