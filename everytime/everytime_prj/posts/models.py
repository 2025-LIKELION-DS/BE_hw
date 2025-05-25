from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=20)
    is_anonymous = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='comments')
    content=models.TextField()
    author=models.CharField(max_length=20)
    is_anonymous = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        author_display = "익명" if self.is_anonymous else self.author
        return f"[{author_display}] {self.content}"