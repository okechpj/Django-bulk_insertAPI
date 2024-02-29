from django.db import models



# Create a product variant model
class Product_variant(models.Model):
    product_variant_sku = models.CharField(max_length=100, unique=True)
    product_variant_name = models.CharField(max_length=255)
    product_variant_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_variant_details = models.TextField()
   
  

    def __str__(self):
        return self.product_variant_name
    

# create a products model
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to="core_images")
     # create a many to one relationship with Product_variant model
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_name

