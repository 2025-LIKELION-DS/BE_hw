from django.db import models
from users.models import User

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="posts")
    
class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name="comments")
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="comments")
    
    def __str__(self):
        return f'[{self.id}] {self.content}'

