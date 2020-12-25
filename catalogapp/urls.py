from django.urls import path
from .views import show_list
from .views import show_item

urlpatterns = [
    path('category/<str:slug>/', show_list, name='show_list'),
    path('<str:slug>/', show_item, name='show_item'),
]
