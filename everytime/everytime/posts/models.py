from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="posts")
    is_anonymouse=models.BooleanField(default=False) # 익명 여부
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'[{self.id}]{self.title}'

    def anonymouse(self):
        if self.is_anonymouse: # 익명일 경우
            return "익명"
        else: # 익명 아닐 경우
            return self.author.nickname


class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name="comments")
    content=models.TextField()
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="comments")
    is_anonymouse=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.id}]{self.content}'

    def anonymouse(self):
        if self.is_anonymouse: # 익명일 경우
            return "익명"
        else: # 익명 아닐 경우
            return self.author.nickname




    
