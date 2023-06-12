from django.db import models
from django.utils.text import slugify


def product_image_upload_to(instance, filename):
    name = slugify(instance.name)
    return f"products/{name}/{filename}"


def company_logo_upload_to(instance, filename):
    name = instance.name.upper().replace(" ", "@")
    return f"companies/{name}/{filename}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    company_logo = models.ImageField()
    def __str__(self):
        return self.name