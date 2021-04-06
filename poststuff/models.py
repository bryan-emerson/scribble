from django.db import models

# Create your models here.

#Post Model
class Post(models.Model):
  author = models.CharField(max_length=240)
  title = models.CharField(max_length=240)
  body = models.CharField(max_length=240)

  def __str__(self):
    return self.author

#Comment Model
class Comment(models.Model):
  author = models.CharField(max_length=240)
  body = models.CharField(max_length=240)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

  def __str__(self):
    return self.author