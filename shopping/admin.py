from django.contrib import admin
from .models import Cart,CartItem,Coupon_group,Coupon

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon)
admin.site.register(Coupon_group)
