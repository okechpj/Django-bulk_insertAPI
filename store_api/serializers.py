from rest_framework import serializers # import restframework
from core.models import Product, Product_variant # import models from core app



# create productSerializer to serialize and deserialize instance of Product model
class ProductSerializer(serializers.ModelSerializer):
    product_image = serializers.CharField(allow_null=True, required=False) # allow null value for image fields
    class Meta:
        model = Product # model to be used
        #select fields to be displayed
        fields = ['id','product_name', 'product_image']

# create productVariant serializer to serialize and deserialize instance of Product_variant model
class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer() # Nesting Product serializer in Product_variant serializer

    def create(self, validated_data):   #create method extracts and processes only validated data
        product_data = validated_data.pop('product')  #  reomove product_variant data from validated data
        product_variant = Product_variant.objects.create(**validated_data)  # create a new instance of Product_variant model
        product = Product.objects.create(product_variant=product_variant, **product_data)  #create new instance of Product using the extracted product_data, associating it with newly created Product_variant instance
        product_variant.product = product  # 
        product_variant.save() #saves the Product_variant instance with the associated Product
        return product_variant  # returns product_variant instance
    
      
    class Meta:
        model = Product_variant
        # select the fields that are to be displayed
        fields = ['id','product_variant_sku', 'product_variant_name', 'product_variant_price', 'product_variant_details', 'product']
        

        


