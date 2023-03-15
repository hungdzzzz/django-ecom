from django.contrib import admin
from.models import *
# Register your models here.
#gan cung gia tri
class Product_Images(admin.TabularInline):
    model=Product_Image

class Additional_Informations(admin.TabularInline):
     model=Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines=(Product_Images,Additional_Informations)
    list_display = ('product_name','price','Categories','color','section') # gan gia tri hien thi admin
    list_editable= ('Categories','section','color') #edit gia tri




admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Color12)

admin.site.register(Additional_Information)
admin.site.register(Review)

admin.site.site_header=" Hung-ShopAdmin"


