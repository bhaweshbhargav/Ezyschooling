from django.contrib import admin
from testapp.models import multiple_types,multiple_size,manny_toppings

# Register your models here.
class Type_Admin(admin.ModelAdmin):
    list_display = ['id','regular','square']

class Size_Admin(admin.ModelAdmin):
    list_display = ['id','small','medium','large']


class Toppings_Admin(admin.ModelAdmin):
    list_display = ['id', 'onion', 'tomato', 'corn','capsicum','cheese','jalapeno']


admin.site.register(multiple_types,Type_Admin)
admin.site.register(multiple_size,Size_Admin)
admin.site.register(manny_toppings,Toppings_Admin)