from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class Post(models.Model):
    OPTONS = (
        ("d", "Draft"),
        ("p", "Published"),
    )
    title = models.Charfield(max_length =100)
    content = models.TextField()
    image = models.ImageField()  
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField (auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.Charfield (max_length=10, choices=OPTIONS, default="D")
    slug = models.SlugField(blank=True, unique=True)