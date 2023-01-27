from django.contrib import admin
from .models.category import categories
from.models.register import registermodel
from .models.product import products
from .models.cartmodel import cartmodel
from .models.orders import orders
from .models.testorder import testorders 
from .models.testitems import orderitems




# Register your models here.

class adminorderitems(admin.TabularInline):
    model=orderitems
class orderadmin(admin.ModelAdmin):
    inlines=[adminorderitems]
admin.site.register(testorders,orderadmin)
admin.site.register(orderitems)
@admin.register(orders)
class ordertable(admin.ModelAdmin):
    list_display=['customer','order_items','total_price','order_id','razorpay_payment_id','razorpay_signature','payment_status']

@admin.register(cartmodel)
class cartregister(admin.ModelAdmin):
    list_display=['customer','product','quantity','price','address1','address2','phonenumber','date']
@admin.register(registermodel)
class customerregister(admin.ModelAdmin):
    list_display=['email','password','address1','address2','city']
@admin.register(categories)
class catadmin(admin.ModelAdmin):
    list_display=['p_categ']

@admin.register(products)
class catadmin(admin.ModelAdmin):
    list_display=['p_name','p_description','p_category','p_price','p_image']