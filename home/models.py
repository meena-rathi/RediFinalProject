from django.contrib.auth.models import User

# Create your models here.
from django.db import models



class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # Example default value 'default_photo.jpg'
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class CartItem(models.Model):
    product = models.ForeignKey(Image, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Contact(models.Model):
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.EmailField(null=True)
    describtion = models.TextField(null=True)
    