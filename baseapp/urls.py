from django.urls import path
from .views import show_index
from .views import show_contacts

urlpatterns = [
    path('', show_index, name='show_index'),
    path('contacts/', show_contacts, name='show_contacts'),
]
