from django.shortcuts import render
from app.models import *
# Create your views here.
def list_view(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'pages/list.html', context)