from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

# Create your views here.
def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)   

    # try:
    #     product = Product.objects.get(pk=0) 
    # except ObjectDoesNotExist:
    #     print("Product with given id does not exist")
    # else:
    #     print(product)

    # product = Product.objects.filter(pk=0).first()
    # exists = Product.objects.filter(pk=0).exists()
    # print(exists)

    # gt_price = Product.objects.filter(unit_price__gt=20)
    # print(gt_price)

    # range = Product.objects.filter(unit_price__range=(20, 30))
    
    # list(query_set)
    # query_set[0]
    # query_set.filter().filter().order_by().reverse()
    #Products inbetween inventory<10 and price <20
    #queryset = Product.objects.filter(unit_price__lt=20, inventory__lt=10)
    # queryset = Product.objects.filter(unit_price__lt=20).filter(inventory__lt=10)
    #Products inbetween inventory !<10 or price <20
    # queryset = Product.objects.filter(
    #     Q(unit_price__lt=20) | ~Q(inventory__lt=10)
    # )

    #Products : inventory=unit_price
    queryset = Product.objects.filter(inventory=F('unit_price'))


    return render(request, "hello.html", {'name': 'Masum', 'products': list(queryset)})
