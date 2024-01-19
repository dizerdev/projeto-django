from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=65)
    slug = models.SlugField()
    type = models.CharField(max_length=65)
    sale_price = models.IntegerField()
    product_details = models.TextField(max_length=2000)
    product_details_is_html = models.BooleanField(default =True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default =True)
    cover = models.ImageField(upload_to='product/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title