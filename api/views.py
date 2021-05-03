from django.shortcuts import render, redirect
from api.models import pizza_choice  # importing models from model file
from django.contrib import messages  # importing messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .seializer import  pizza_choiceSerializer ,pizza_choice1Serializer# import pizza_choice form seializer file.
from rest_framework import generics # import generic from django rest_framework
# Create your views here.

# creating views for the pizza form.
class pizza_choiceList(APIView):
    def get(self,request):
        pizza_choice1 = pizza_choice.objects.all()
        serializer = pizza_choiceSerializer(pizza_choice1, many=True)
        return Response(serializer.data)
# creating API of pizza toppings and pizza size
class pizza_choice1List(APIView):
    def get(self,request):
        pizza_choice2 = pizza_choice.objects.all()
        serializer1 = pizza_choice1Serializer(pizza_choice2, many=True)
        return Response(serializer1.data)
# creating api to add data
class pizza_choice_addList(generics.ListCreateAPIView):
    queryset = pizza_choice.objects.all()
    serializer_class = pizza_choice1Serializer

# creating edit and delete finction in the API here edit name is put.
class pizza_choiceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pizza_choice
    serializer_class = pizza_choice1Serializer

# Save the form data to database.
"""
def pizza_form(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        choose_pizza = request.POST['choose_pizza']
        pizza_size = request.POST['pizza_size']
        toppings = request.POST['toppings']
        if len(phone) != 10:
            messages.warning(request, "Entre correct phone  number")
            return redirect('pizza_form')
        # The data should be saved in database
        pizza_save = pizza_choice(name=name, phone=phone, choose_pizza=choose_pizza, pizza_size=pizza_size, toppings=toppings)
        pizza_save.save()
        messages.success(request, "your account has been create succesfully")
        return redirect('pizza_choice1/')
    return render(request, 'pizza_form.html')
"""