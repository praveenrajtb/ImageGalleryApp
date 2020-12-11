from django.db import models
from django.utils import timezone
from django.urls import reverse


def gallery_directory_path(instance, filename):
    return 'gallery/'.format(instance.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to=gallery_directory_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    upload_date = models.DateTimeField(
          default=timezone.now)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('gallery:gallery')
