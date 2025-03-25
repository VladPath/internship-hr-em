from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import ItemDish, Orders



# Create your views here.
def index(request):
    return HttpResponse('Заказы тут!')


def add(request):
    return render(request, 'orders/add_order.html', data)