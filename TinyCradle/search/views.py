from django.shortcuts import render
from shop.models import Product
from django.db.models import Q #used in or,and operator

# Create your views here.
def search(request):
   q="" #initialization
   product=None
   if(request.method=="POST"):
      q=request.POST['q']
      if q:
          product=Product.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))# in product table if there is q in name
   return render(request,template_name='search.html',context={'p':product,'query':q})