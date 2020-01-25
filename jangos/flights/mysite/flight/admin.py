from django.contrib import admin
from .models import airport,flights


# Register your models here.

admin.site.register(airport)
admin.site.register(flights)