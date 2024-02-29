from django.db import models



# create a products model
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to="core_images")
    
    

    def __str__(self):
        return self.product_name



# Create a product variant model
class Product_variant(models.Model):
    product_variant_sku = models.CharField(max_length=100, unique=True)
    product_variant_name = models.CharField(max_length=255)
    product_variant_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_variant_details = models.TextField()
     # create a many to one relationship with Product model
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
  

    def __str__(self):
        return self.product_variant_name
    
