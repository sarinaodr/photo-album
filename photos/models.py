from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False)
    
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    image = models.ImageField(null=False , blank=False)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , blank=True)
    description = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    
    def __str__(self):
        return self.description
    
    class Meta:
        order_with_respect_to = 'user'