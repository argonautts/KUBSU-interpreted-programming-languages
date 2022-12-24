from django.urls import path

from .views import index
from .views import orders_view
from .views import OrderUpdateView
from .views import OrderCreateView

urlpatterns = [
    path('<int:pk>/', orders_view, name='order_detail'),
    path('add', OrderCreateView.as_view(), name='add_order'),
    path('<int:pk>/edit', OrderUpdateView.as_view(), name='edit_form'),
    path('', index, name='index')
]
