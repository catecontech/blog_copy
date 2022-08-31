from django.db import models
from post.models import Post
from django.contrib.auth.models import User
# Create your models here.


class Like(models.Model):
    number_of_likes = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    liked_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Liked By {self.user}" + str(self.post)