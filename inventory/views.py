from django.shortcuts import render
from .models import Category,Product,Product_details
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/authentication/login')  
def category(request):
    category = Category.objects.all()

    context= {
       "category":category,
    }
    return render(request, 'inventory/category.html', context)   



@login_required(login_url='/authentication/login') 
def product(request, category_code):
    product = Product.objects.filter(category_code=category_code)
    context={
    "product":product,
    }

    return render(request, 'inventory/product.html',context)   

    
@login_required(login_url='/authentication/login') 
def part(request, product_code):
    part = Product_details.objects.filter(product_code=product_code)
    context={
    "part":part,
    }

    return render(request, 'inventory/part.html',context)   