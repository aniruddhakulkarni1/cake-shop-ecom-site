from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(shippingaddress)
admin.site.register(Orderitem)