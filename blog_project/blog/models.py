from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title