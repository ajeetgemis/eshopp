from django.contrib import admin
from django.urls import path,include
from shop import views
from django.conf.urls.static import static
from django.conf import settings
from shop.views import showcart
from shop.views import checkoutcart
from shop.views import orders_status



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index1),
    path('signup',views.registe_customer,name='signup'),
    path('login',views.login_customer,name='login'),
    path('logout',views.logout,name='logout'),
    path('orders',orders_status.as_view(),name='orders'),
    path('showcart',showcart.as_view(),name='showcart'),
    path('checkoutcart',checkoutcart.as_view(),name='checkoutcart'),
    path('addtocart',views.addto_cart,name='addtocart'),
    path('/addtocart',views.addto_cart,name='addtocart'),
    path('rozerpayment',views.rozerpayment,name='rozerpayment'),

     path('handelrequestpaytm/',views.handelrequestpaytm,name='handelrequestpaytm'),
    path('<int:id>',views.index1,name='filter')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
