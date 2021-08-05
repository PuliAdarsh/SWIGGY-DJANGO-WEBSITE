from django.contrib import admin
from . models import user,product,login,order
admin.site.register(user)
admin.site.register(product)
admin.site.register(login)
admin.site.register(order)
# Register your models here.