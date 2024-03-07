from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def allcategories(request):
    c=Category.objects.all()#getting all record
    return render(request,template_name='category.html',context={'c':c})


def allproducts(request,p):
        c=Category.objects.get(name=p)#getting a particular record
        p=Product.objects.filter(category=c)#more than one record that satisfy condition
        return render(request,template_name='product.html',context={'c':c,'p':p})

def detail(request,p):
    product=Product.objects.get(name=p)#getting particular product
    return render(request,template_name='details.html',context={'p':product})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p =request.POST['p']
        cp =request.POST['cp']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            u.save()
            return redirect('shop:allcategories')
        else:
            return HttpResponse("Password not matching")
    return render(request,template_name='register.html')

def user_login(request):
    if (request.method == "POST"):
        name = request.POST['u']
        pass1 = request.POST['p']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect("shop:allcategories")
        else:
            message.error(request,"invalid credentails")
    return render(request,template_name='login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)


