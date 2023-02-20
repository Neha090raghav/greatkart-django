from django.urls import path
from .import views

urlpatterns=[
    path('place_order/',views.place_order,name='place_order'),
    path('payments/',views.payments,name='payments'),
    path('order_complete/',views.order_complete,name='order_complete'),
     path('payments_get/',views.payments_get,name='payments_get'),
     path('orders_get/',views.orders_get,name='orders_get'),
     path('order_products_get/',views.order_products_get,name='order_products_get'),


    

]