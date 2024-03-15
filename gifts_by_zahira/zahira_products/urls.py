from django.urls import path
from .import views
from .views import  product_list, customer_profile, loginview, logout_view, add_to_cart, view_cart, sign_up, home

from django.conf import settings
from django.conf.urls.static import static


app_name = 'zahira_products'

urlpatterns = [
   path('',views.home,name='home'),
   path('login/', views.loginview, name='loginview'),
   path('accounts/login/',views.loginview,name="login"),
   path('logout',views.logout_view),
   path('signup/',views.sign_up,name='signup'),
   path('product_details',views.product_list),
   path('customer_details',views.customer_profile),
   path('products.html', views.product_list, name='products'),
   path('customers.html',views.customer_profile, name='customers'),
   path('view_cart.html',views.view_cart, name='view_cart'),
   path('index.html',views.home, name='index'),
   path('products/', views.product_list, name='product_list'),
   path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('products/view_cart/', views.view_cart, name='view_cart'),

   path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
   path('place_order/', views.place_order, name='place_order'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
