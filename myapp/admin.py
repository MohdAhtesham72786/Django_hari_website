from django.contrib import admin
from .models import Coupon
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','description','amount','amount_type']
    
admin.site.register(Coupon, CouponAdmin)





