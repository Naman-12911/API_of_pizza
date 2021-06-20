from rest_framework import serializers
from .models import pizza_choice
# creating API of the pizza.
class  pizza_choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  pizza_choice
        fields=['name','choose_shape_pizzas']
        
class  pizza_choice1Serializer(serializers.ModelSerializer):
    class Meta:
        model =  pizza_choice
        fields=['id','choose_shape_pizzas','small','medium','large','pizza_size',"onion","tomato",'corn','capsicum',
                 'cheese','jalapeno','toppings',]
