from django.db import models

# Create your models here.


class PostQueryset(models.QuerySet):
    def all(self):
        return self.filter()
 
 
class PostManage(models.Manager):
    def get_queryset(self):
        return PostQueryset(self.model, using=self._db)


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True
        
    