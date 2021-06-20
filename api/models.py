from django.db import models

# Create your models here.
class pizza_choice(models.Model):
    name = models.CharField(max_length = 130,blank = True)
    # adding pizza shape.
    choose_shape_pizza = (('regular',"Regular"),
                ('square',"square"))
    choose_shape_pizzas = models.CharField(max_length=100, default="small",choices = choose_shape_pizza)
    # adding size of pizzas
    small = models.BooleanField("small, _pizza", default=False)
    medium = models.BooleanField("Medium_pizza", default=False)
    large = models.BooleanField("Large_pizza", default=False)
    pizza_size = models.CharField(max_length=100,blank=True)

    # add toppings 
    onion = models.BooleanField("Onion_toppings", default=False)
    tomato = models.BooleanField("Tomato_Toppings", default=False)
    corn = models.BooleanField("Corn_Toppings",default=False)
    capsicum = models.BooleanField("Capsium_toppings",default=False)
    cheese = models.BooleanField("Cheese_toppings",default=False)
    jalapeno = models.BooleanField("Jalapeno_toppings",default=False)
    toppings = models.CharField("Add another toopings",max_length=150, blank = True) # add extra toppings
    # adding multiple sizes of pizzas
    
    def __str__(self):
        return self. choose_shape_pizzas