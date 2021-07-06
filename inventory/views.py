from django.shortcuts import render
from .models import Category,Product,Product_details
from users.models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Empresa, ImagePerfil, UsuarioPessoal
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/authentication/login')  
def category(request):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    
    category = Category.objects.all()

    context= {
       'category':category,
       'grupo' : grupo,
       'grupos':grupos,
       'usuarioC':usuarioC,
       'imageP' : imageP, 
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