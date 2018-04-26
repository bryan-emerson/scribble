from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default = '')
    author = models.CharField(max_length = 25, default = '')
    body = models.TextField(default='')

    def __str__(self):
        return self.title
    
    def num_comments(self):
        return len(list(self.comments.all()))

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length = 25, default = '')
    body = models.TextField(default = '')

    def __str__(self):
        return f'{self.author} replies to {self.post.author} in {self.post.title}'
