from django.utils import timezone
from datetime import timedelta

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def publish_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)





class Author(models.Model):
    name = models.CharField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_name}/{self.post.title}'







# Create your models here.
