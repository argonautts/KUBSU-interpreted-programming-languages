from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .models import Order
from .forms import OrderForm
from .forms import InsertForm


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'edit.html'
    form_class = OrderForm
    success_url = './'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'insert.html'
    form_class = InsertForm
    success_url = reverse_lazy('index')


def orders_view(request, pk):
    template = loader.get_template("order.html")
    o = Order.objects.get(pk=pk)
    context = {"o": o}
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template("index.html")
    orders = Order.objects.all()
    context = {"orders": orders}
    return HttpResponse(template.render(context, request))
