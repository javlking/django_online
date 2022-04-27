from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse


def index(request):
    products = ProductName.objects.all()
    form = SearchForm()

    if request.method == 'POST':
        find_product = request.POST.get('search_product')
        product_find = ProductName.objects.get(name=find_product)

        return product_info(request, product_find.id)

    else:
        context = {'products': products, 'form':form}
        return render(request, 'main_page/index.html', context)


def product_info(request, pk):
    products = ProductName.objects.get(id=pk)

    context = {'products': products}
    return render(request, 'main_page/product_info.html', context)