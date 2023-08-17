from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id=models.AutoField
    Product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default=0)
    price=models.IntegerField(default=0) 
    dsc=models.CharField(max_length=1000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")


    def __str__(self):
        return self.Product_name
    

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    number=models.CharField(max_length=50,default=0)
    desc=models.CharField(max_length=50,default=0) 


    def __str__(self):
        return self.name    

