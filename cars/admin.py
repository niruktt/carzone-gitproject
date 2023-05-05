from django.contrib import admin
from .models import car
from django.utils.html import format_html

# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:25px;"/>'.format(object.car_photo.url))
    
    thumbnail.shot_description = 'Car Image'
    list_display = ('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links= ('id','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','city','condition','model')
    list_filter = ('fuel_type','city','body_style','color','model')
admin.site.register(car,carAdmin)