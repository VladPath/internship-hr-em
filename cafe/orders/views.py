from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import DroneModels



# Create your views here.
def index(request):
    return HttpResponse('Заказы тут!')

