from rest_framework import serializers # import restframework
from core.models import Product, Product_variant # import models from core app


# create productVariant serializer to serialize and deserialize instance of Product_variant model
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_variant
        # select the fields that are to be displayed
        fields = ['id','product_variant_sku', 'product_variant_name', 'product_variant_price', 'product_variant_details']
        

# create productSerializer to serialize and deserialize instance of Product model
class ProductSerializer(serializers.ModelSerializer):
    product_image = serializers.CharField(allow_null=True, required=False) # allow null value for image fields
    product_variant = ProductVariantSerializer() # Nesting Product_variant serializer in Product serializer

    def create(self, validated_data):   #create method extracts and processes only validated data
        product_variant_data = validated_data.pop('product_variant')  #  reomove product_variant data from validated data
        product = Product.objects.create(**validated_data)  # create a new instance of Product model
        product_variant = Product_variant.objects.create(product=product, **product_variant_data)  #create new instance of Product_variant using the extracted product_variant_data, associating it with newly created Product instance
        product.product_variant = product_variant  # 
        product.save() #saves the Product instance with the associated Product_variant 
        return product  # returns product instance
    
    class Meta:
        model = Product # model to be used
        #select fields to be displayed
        fields = ['id','product_name', 'product_image', 'product_variant']
        


