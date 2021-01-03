from django.urls import path
from .views import show_order
from .views import create_order
from .views import show_orders
from .views import set_is_confirmed
from .views import set_is_canceled

from .views import show_canceled
from .views import show_confirmed

urlpatterns = [
    path('<int:id>/', show_order, name='show_order'),
    path('is_confirmed/<int:id>/', set_is_confirmed, name='set_is_confirmed'),
    path('is_canceled/<int:id>/', set_is_canceled, name='set_is_canceled'),
    path('create_order/', create_order, name='create_order'),
    path('show_orders/', show_orders, name='show_orders'),
    path('show_canceled/', show_canceled, name='show_canceled'),
    path('show_confirmed/', show_confirmed, name='show_confirmed'),
    
]
