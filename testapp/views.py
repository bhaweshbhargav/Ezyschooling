from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class TypePizza(ListCreateAPIView):
    serializer_class = serializers.Type_Serializer
    queryset = models.multiple_types.objects.all()

class Typepizza_edit_delete(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.Type_Serializer
    queryset = models.multiple_types.objects.all()

class SizePizza(ListCreateAPIView):
    serializer_class = serializers.Size_Serializer
    queryset = models.multiple_size.objects.all()

class Sizepizza_edit_delete(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.Size_Serializer
    queryset = models.multiple_size.objects.all()

class ToppingsPizza(ListCreateAPIView):
    serializer_class = serializers.Toppings_Serializer
    queryset = models.manny_toppings.objects.all()

class Toppingspizza_edit_delete(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.Toppings_Serializer
    queryset = models.manny_toppings.objects.all()