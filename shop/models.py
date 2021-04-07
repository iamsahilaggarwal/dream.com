from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    pro_img=models.ImageField(upload_to="shop/image",default="")

# To show product name in admin page 
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msgid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    problem=models.CharField(max_length=500)
    contact_ingo= models.CharField(max_length=50, default="")
   

# To show product name in admin page 
    def __str__(self):
        return self.name