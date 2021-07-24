from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(
        max_length=100,
    )
    mobile = models.CharField(
        max_length=10,
    )
    profile_pic = models.ImageField()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='Product photos')