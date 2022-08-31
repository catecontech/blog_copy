from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# Create your models here.


class Comment(models.Model):
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return  self.text + " by " + str(self.user)
    