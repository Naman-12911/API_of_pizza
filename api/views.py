from django.shortcuts import render, redirect
from api.models import pizza_choice  # importing models from model file

from .seializer import  pizza_choiceSerializer ,pizza_choice1Serializer# import pizza_choice form seializer file.
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# creating views for the pizza form.
@csrf_exempt
def pizza_regular_square(request):
    if request.method == "GET": # get request to fetch the data only regular or square
        pizza_api_regular_square = pizza_choice.objects.all()
        serializer = pizza_choiceSerializer(pizza_api_regular_square, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST': # post request to post the data regular or square
        data = JSONParser().parse(request)
        serializer = pizza_choiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)#
@csrf_exempt
def pizza_api(request): # craeting api for the all feilds
    if request.method == "GET": # get request to fetch all the data

        pizza_api_get = pizza_choice.objects.filter()
        serializer = pizza_choice1Serializer(pizza_api_get, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST': # post  request post the data
        data = JSONParser().parse(request)
        serializer = pizza_choice1Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)# when wrong data is send server return 400 insead of 500


@csrf_exempt
def pizza_detail(request, pk):
    try:
        pizza_choice_id = pizza_choice.objects.get(pk=pk)
    except pizza_choice_id.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': # get request to fetch all the data according to the id
        serializer = pizza_choice1Serializer(pizza_choice_id)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT': # put request to updat the partical data
        data = JSONParser().parse(request)
        serializer = pizza_choice1Serializer(pizza_choice_id, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': # delete request to delete accoriding to id.
        pizza_choice_id.delete()
        return HttpResponse(status=204)
