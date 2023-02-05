from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
STATE_CHOICES=(('Jharkhand','Jharkhand'),('Bihar','Bihar'),('Assam','Assam'),('UP','UP'))
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICSES=(('H','homecleaning'),('E','Electric'),('P','Plumbing'),('CS','Car Care & Service'),('C','Carpenters'),('S','Salon At Home'),('HP','Home Painting'))
class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    discription=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICSES,max_length=3)

    product_img=models.ImageField(upload_to='ProductImg')
    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    
    def _str_(self):
        return str (self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

STAUSE_CHOICES=(('Pending','Pending'),('Accepted','Accepted'),('On the way','On the way'),('Reached the destination','Reached the destination'),('Cancel','Cancel'))


class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STAUSE_CHOICES,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price



