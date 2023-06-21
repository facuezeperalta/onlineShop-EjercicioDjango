from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta: #cambio la forma en plural del nombre en el admin site
        ordering =('name',)
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField( blank=True, null=True)
    price = models.FloatField() #precio en float
    image = models.ImageField(upload_to='item_images',blank=True,null= True)
    created_by = models.ForeignKey(User,related_name='items', on_delete=models.CASCADE)
    is_sold= models.BooleanField(default=False) #veo si el articulo tiene o no stock
    created_at = models.DateTimeField(auto_now_add=True) #aca se pone automaticamente la fecha de creación lo maneja Django

    def __str__(self):
        return self.name
    

 
    

