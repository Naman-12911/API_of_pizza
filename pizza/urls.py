"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import pizza_choice1List,pizza_choiceDetails,pizza_choiceList,pizza_choice_addList

# changing names of the admin pannel.
admin.site.site_header = "c3"
admin.site.site_tile = "c3"
admin.site.index_title = "welcome to c3"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza_choice/', pizza_choiceList.as_view()), # this urls redirect to see pizza type
    path('pizza_choice1/', pizza_choice1List.as_view()), # this urls redirect to see pizza size toppings etc.
    path('',pizza_choice_addList.as_view()), # this urls can use by the user to order a pizza ## we can also add pizza_choice_add/ this urls
    path('api/pizza/<int:pk>',pizza_choiceDetails.as_view()) # this url redirect to edit and functions.
]
