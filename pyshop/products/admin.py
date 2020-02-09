from django.contrib import admin
from .models import product,offers


class productadmin(admin.ModelAdmin):
    list_display=('name','price','stock')

class offersadmin(admin.ModelAdmin):
    list_display=("code","discount")



# Register your models here.
admin.site.register(product,productadmin)
admin.site.register(offers,offersadmin)