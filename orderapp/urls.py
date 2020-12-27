from django.urls import path
from .views import show_order
from .views import create_order
from .views import show_orders
from .views import set_is_sale

urlpatterns = [
    path('<int:id>/', show_order, name='show_order'),
    path('is_sale/<int:id>/', set_is_sale, name='set_is_sale'),
    path('create_order/', create_order, name='create_order'),
    path('show_orders/', show_orders, name='show_orders'),
    
]
