from django.contrib import admin
from django.utils.html import format_html
from .models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self , object):
        return format_html(f'<img src="{object.car_photo.url}" width="70" style="border-radius: 40px" />')


    thumbnail.short_description = 'Car Picture'


    list_display = ('id' , 'thumbnail' , 'car_title' , 'color', 'model' , 'body_style' , 'year' , 'price' , 'is_featured')
    list_display_links = ( 'id' , 'thumbnail' , 'car_title')
    search_fields = ('car_title',)
    list_filter = ('car_title', 'model')
    list_editable = ('is_featured',)


admin.site.register(Car , CarAdmin)