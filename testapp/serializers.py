from .models import multiple_types,multiple_size,manny_toppings
from rest_framework import serializers

class Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = multiple_types
        fields = ['regular','square']

class Size_Serializer(serializers.ModelSerializer):
    class Meta:
        model = multiple_size
        fields = ['small','medium','large']

class Toppings_Serializer(serializers.ModelSerializer):
    class Meta:
        model = manny_toppings
        fields = [ 'onion', 'tomato', 'corn','capsicum','cheese','jalapeno']


