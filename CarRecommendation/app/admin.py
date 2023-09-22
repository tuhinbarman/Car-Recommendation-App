from django.contrib import admin
from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','type','mileage','fuel_type','price')
    list_display_links = ('id','name',)
    list_editable = ('type','fuel_type','description')
    list_per_page = 10

admin.site.register(Car,CarAdmin)


