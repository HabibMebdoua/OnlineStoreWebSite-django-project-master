from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    img = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.img.path)
        if img.height < 10 or img.width < 10 :
            img.thumbnail((286 , 180))

class Order(models.Model):
    product = models.ForeignKey(Product , related_name='product_order' , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=250)
    nummber = models.CharField(max_length=10)
    town= models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    all_adress = models.TextField(max_length=1000)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    comment = models.TextField(max_length=250)




