from django.shortcuts import redirect, render
from .models import Category,Product,Product_details,Log_entrance
from users.models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Empresa, ImagePerfil, UsuarioPessoal
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    product = Product.objects.all()
    

    context= {
       'category':category,
       'grupo' : grupo,
       'grupos':grupos,
       'usuarioC':usuarioC,
       'imageP' : imageP, 
       'product':product,
    }
    return render(request, 'inventory/category.html', context)   



@login_required(login_url='/authentication/login') 
def product(request, category_code):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    
    product = Product.objects.filter(category_code=category_code)
    context={
    "product":product,
    'grupo' : grupo,
    'grupos':grupos,
    'usuarioC':usuarioC,
    'imageP' : imageP, 
    }

    return render(request, 'inventory/product.html',context)   

    
@login_required(login_url='/authentication/login') 
def part(request, product_code):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    
    part = Product_details.objects.filter(product_code=product_code)
    context={
    "part":part,
    'grupo' : grupo,
    'grupos':grupos,
    'usuarioC':usuarioC,
    'imageP' : imageP, 
    }

    return render(request, 'inventory/part.html',context)   

    
@login_required(login_url='/authentication/login') 
def add_category(request):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    
    context={
    'grupo' : grupo,
    'grupos':grupos,
    'usuarioC':usuarioC,
    'imageP' : imageP, 
    }

    return render(request, 'inventory/category.html',context)   
@login_required(login_url='/authentication/login') 
def add_product(request):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  

    context={
    'grupo' : grupo,
    'grupos':grupos,
    'usuarioC':usuarioC,
    'imageP' : imageP, 
    }

    return render(request, 'inventory/category.html',context)   
@login_required(login_url='/authentication/login') 
def add_part(request):
    user = request.user   
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
      
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    if Log_entrance.objects.all():
            LOG_id = Log_entrance.objects.all().order_by('-entrance_code')[0].entrance_code
                

            cod = LOG_id + 1
    else:
                    cod = 100  
    if request.method == 'POST' and 'register' in request.POST:  
        code= request.POST['part_code']
        product = Product.objects.get(product_code=request.POST['product_code'])  
        category = Category.objects.get(category_code= product.category_code.category_code)
        details = request.POST['part_details'] 
        Product_details.objects.create(part_code=code,product_code=product,details=details)
        product.amount = product.amount + 1
        product.save()
        category.amount = category.amount + 1
        category.save()
        ########LOG#########
        part = Product_details.objects.get(part_code=code)
        Log_entrance.objects.create(entrance_code=cod,part_code=part,product_code=product,creator=user)
        
        messages.success(request, "Registrado com sucesso")
        return redirect( 'product')

        

        

    context={
    'grupo' : grupo,
    'grupos':grupos,
    'usuarioC':usuarioC,
    'imageP' : imageP, 
  
    }

    return render(request, 'inventory/part.html',context)   



