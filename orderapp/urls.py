from django.urls import path
from .views import show_order

urlpatterns = [
    path('', show_order, name='show_order'),
]
