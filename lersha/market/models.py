from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/categories/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    farmer = models.ForeignKey('users.Farmer', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to='images/products/')
    organic = models.BooleanField(default=False)
    delivery_available = models.BooleanField(default=False)
    quantity_unit = models.CharField(max_length=50, choices={'Item':'Item', 'KG':'KG', 'Litre':'Litre'}, default='Item')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price (Birr per unit)')
    stock = models.FloatField()
    active = models.BooleanField(default=True)
    date_listed = models.DateTimeField(auto_now_add=True)

    def in_stock(self):
        if self.stock > 0:
            return True
        return False
    
    # def save(self):
    #     if not self.in_stock():
    #         self.active = False
    #     if self.pk:
    #         previous = Product.objects.get(pk=self.pk)
    #         if not previous.in_stock() and self.in_stock():
    #             self.date_listed = models.DateTimeField(auto_now_add=True)
    #             active = True
    #     super().save()
    
    def __str__(self):
        return self.name

class Impression(models.Model):
    product = models.ForeignKey('Product', related_name='impressions', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    product = models.ForeignKey('Product', related_name='contacts', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
