from django.shortcuts import render
from django.core.paginator import Paginator

from page_app.models import Product

def product_list(request):

    obj = request.GET.get('obj')
    print(obj)
    if obj:
        product_list = Product.objects.filter(name__icontains=obj)
    else:
        product_list = Product.objects.all()

    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})