from django.contrib import admin

from .models import*
class ProductImageAdmin(admin.StackedInline):
	model = ProductImage
	fields = ["image"]

class ProductColorAdmin(admin.StackedInline):
	model = ProductColor
	fields = ["name"]

class ProductSizeAdmin(admin.StackedInline):
	model = ProductSize
	fields = ["name"]

class ProductAdmin(admin.ModelAdmin):
	list_display = ["title", "price", "rating", "sub_category","is_active"]
	prepopulated_fields={"slug":("title",)}

	inlines = [ProductImageAdmin,ProductColorAdmin,ProductSizeAdmin]


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={"slug":("name",)}

class SubcategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={"slug":("name",)}
	

admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Product,ProductAdmin)
