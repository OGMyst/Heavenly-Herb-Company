from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('edit/<str:address_number>', views.edit_address, name='edit_address'),
    path('delete/<str:address_number>', views.delete_address,
         name='delete_address'),
]
