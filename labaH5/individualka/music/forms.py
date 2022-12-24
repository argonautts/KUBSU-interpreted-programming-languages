from django.forms import ModelForm
from django.forms import DateField
from django.forms import SelectDateWidget

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('album_id', 'customer_name', 'date')


class InsertForm(ModelForm):
    date = DateField(label='Date', widget=SelectDateWidget)

    class Meta:
        model = Order
        fields = ('order_id', 'album_id', 'customer_name', 'date')
