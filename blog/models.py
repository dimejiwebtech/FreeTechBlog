from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category_name


# status dropdown
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)

class BlogPost(models.Model):
    post_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    description = models.TextField(max_length=300)
    post_body = models.TextField(max_length=10000)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_name