from django.contrib import admin
from django.contrib.admin.decorators import register
from django.utils.safestring import mark_safe

from .models import Departments, AllCaregories, Category, Product, ProductImage



class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    prepopulated_fields = {"slug":("name",)}



@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',) 
    inlines = [
        CategoryInline
    ]
    prepopulated_fields = {"slug":("name",)}


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', "price", "quantiy", "discount", "weight", "type_product", "category", "get_image")
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {"slug":("name",)}


    def get_image(self, product):
        images = product.productimage_set.all()
        print(images)
        if images:
            return mark_safe(f'<img src="{images.first().image.url}" width="100">')
        return ''
    get_image.short_description = 'Image'



admin.site.register(AllCaregories)
