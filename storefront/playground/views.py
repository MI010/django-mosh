from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()
    for product in query_set:
        print(product)   

    try:
        product = Product.objects.get(pk=0) 
    except ObjectDoesNotExist:
        print("Product with given id does not exist")
    else:
        print(product)

    product = Product.objects.filter(pk=0).first()
    exists = Product.objects.filter(pk=0).exists()
    print(exists)

    gt_price = Product.objects.filter(unit_price__gt=20)
    print(gt_price)

    range = Product.objects.filter(unit_price__range=(20, 30))
    
    # list(query_set)
    # query_set[0]
    # query_set.filter().filter().order_by().reverse()
    return render(request, "hello.html", {'name': 'Masum', 'products': list(range)})
