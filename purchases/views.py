from datetime import date,datetime, timedelta
from django.shortcuts import redirect, render
from django.template import context
from .models import Requisition_product, Purchase_requisition,Product_image
from users.models import   UsuarioCorporativo 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group, User
from decimal import Context, Decimal
from helpdesk.forms import ImageForm, ImageForms
from users.models import ImagePerfil
import os
# Create your views here.

@login_required(login_url='/authentication/login')  
def index(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")  
    #Requisições em validação
    req_vals = Purchase_requisition.objects.filter(requester=request.user, status='Aguardando verificação do Gestor').order_by('-purchase_requisition_id')
    
    # #Requisições em Cotação
    list_status =["Aguardando cotação", "Aguardando aprovação"]
    req_cots = Purchase_requisition.objects.filter(requester=request.user, status__in= list_status).order_by('-purchase_requisition_id')
   
    # #Requisições aprovados 
  
    req_apprs = Purchase_requisition.objects.filter(requester=request.user, status= 'aprovado').order_by('-purchase_requisition_id')
   
    # #Requisições comprados
  
    req_bougths = Purchase_requisition.objects.filter(requester=request.user, status= 'comprado').order_by('-purchase_requisition_id')
    req_delivs = Purchase_requisition.objects.filter( status= 'entregue')
    req_rets = Purchase_requisition.objects.filter( status= 'Devolvida')

    
    context={
        'usuarioC':usuarioC,
        'req_vals': req_vals,
        'req_cots':req_cots,
        'req_apprs':req_apprs,
        'req_bougths':req_bougths,
        'req_delivs':req_delivs,
        'req_rets':req_rets,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
       
       
    }
    return render(request,'purchases/index.html',context)

@login_required(login_url='/authentication/login')  
def add_requisition(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    list_manager = ['gestor']
    managers = User.objects.filter(groups__name__in=list_manager)
    if Purchase_requisition.objects.all():
            purchases_id = Purchase_requisition.objects.all().order_by('-purchase_requisition_id')[0].purchase_requisition_id
                

            codigo = purchases_id + 6000
    else:
                    codigo = 6001
    if request.method == 'POST' and 'req_save' in request.POST:  
        length= int(request.POST["length"]) 
        manager = request.POST["manager"]
        sector = request.POST["sector"]
        justify= request.POST["justify"]
        deadline = request.POST["deadline"]
        forecast = request.POST["forecast"]
        Purchase_requisition.objects.create(purchase_requisition_id=codigo,requester=request.user,manager=manager,justification=justify,deadline=deadline,forecast=forecast)
        for id in range(length):
            amount = request.POST["amount" + str(id)]
            unit = request.POST["unit"+str(id)]
            product = request.POST["product"+str(id)]
            req_prod =Requisition_product.objects.create(purchase_requisition_id = codigo,amount=amount,unit=unit,requisition_product=product)
            req_prod.save()
            try:
                img = request.FILES["image"+str(id)]
            except:
                img = None
            prod_img  =Product_image.objects.create(requisition_product_id=req_prod.id,name_image=product,image=img)
            prod_img.save()
        return redirect("my_purchase_request")

    context={
        'usuarioC':usuarioC,
        'managers':managers,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
    }
    return render(request, 'purchases/add_requisition.html',context)

@login_required(login_url='/authentication/login')  
def requisition_details(request,purchase_requisition_id):
    requisition= Purchase_requisition.objects.get(purchase_requisition_id=purchase_requisition_id)
    products = Requisition_product.objects.filter(purchase_requisition_id=purchase_requisition_id)
    if request.method == 'POST' and 'edit_requisition' in request.POST:
        prod = Requisition_product.objects.get(pk=request.POST["edit_requisition"])
        prod.amount = request.POST['amount']
        prod.unit = request.POST['unit']
        prod.requisition_product = request.POST['product']
        prod.save()
    if request.method == 'POST' and 'resend_req' in request.POST:
        requisition.status='Aguardando cotação'
        requisition.save()
    context={
        'requisition':requisition,
        'products':products,
    }   
    return render(request, 'purchases/requisition_details.html',context)

@login_required(login_url='/authentication/login')  
def purchase_request(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    req_cots = Purchase_requisition.objects.filter(status="Aguardando cotação",approved=True)
    req_man_apprs = Purchase_requisition.objects.filter(status="Aguardando aprovação do(a) gestor(a) de compras", cotation= True)
    req_fin_apprs = Purchase_requisition.objects.filter(status="Aguardando aprovação financeira",purchase_manager_approval=True)
    req_apprs = Purchase_requisition.objects.filter( status= 'aprovado',purchase_manager_approval=True,cotation= True,approved=True)
    req_dens = Purchase_requisition.objects.filter( status= 'negado')
    req_bougths = Purchase_requisition.objects.filter( status= 'comprado')
    req_delivs = Purchase_requisition.objects.filter( status= 'entregue')
    req_pays = Purchase_requisition.objects.filter( status= 'Aguardando pagamento')
    req_rets = Purchase_requisition.objects.filter( status= 'Devolvida')
        
    context={
        'req_cots':req_cots,
        'req_man_apprs':req_man_apprs,
        'req_fin_apprs':req_fin_apprs,
        'req_apprs':req_apprs,
        'req_dens':req_dens,
        'req_bougths':req_bougths,
        'req_pays':req_pays,
        'req_delivs':req_delivs,
        'req_rets':req_rets,
        'usuarioC':usuarioC,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
    }
    return render(request,'purchases/purchase_request.html',context) 

@login_required(login_url='/authentication/login')    
def requisition_cotation(request,purchase_requisition_id):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    requisition= Purchase_requisition.objects.get(purchase_requisition_id=purchase_requisition_id)
    products = Requisition_product.objects.filter(purchase_requisition_id=purchase_requisition_id)
    usuarioC = UsuarioCorporativo.objects.get(usuario=request.user)
    if request.method == 'POST' and 'btn_cotation' in request.POST:
        ids = request.POST['btn_cotation']
        provider =request.POST['provider'] 
        cotation =request.POST['cotation'] 
        product =  Requisition_product.objects.get(pk=ids)
        if not product.first_cotation:
            product.first_cotation = cotation
            product.first_provider = provider
            product.cotations_length =1
            product.save()
        elif not product.second_cotation:
            product.second_cotation = cotation
            product.second_provider = provider
            product.cotations_length =2
            product.save()
        else:    
            product.third_cotation = cotation
            product.third_provider = provider
            product.cotations_length =3
            product.save()        
    if request.method =='POST' and 'cot_conclude' in request.POST:
        id = request.POST['cot_conclude']
        req= Purchase_requisition.objects.get(purchase_requisition_id=id)
        req.cotation = True
        req.buyer = str(request.user.username)
        req.cot = datetime.now()
        req.status ="Aguardando aprovação do(a) gestor(a) de compras"
        req.note = request.POST["note"]
        req.save()
        return redirect('purchase_request')
    if request.method =="POST" and  'cot_approved' in request.POST:
       requisition.purchase_manager_approval = True
       total = 0
       for product in products:
           price_product = request.POST["price_product"+ str(product.id)]
           product.price_product = price_product
           product.save()
           total = total + (Decimal(price_product.replace(',','.'))*product.amount)
       if total > 1000:
           requisition.status="Aguardando aprovação financeira"  
           requisition.total_price = total 
           requisition.save()

       else:
            requisition.financial_approval = True
            requisition.status="aprovado"   
            requisition.total_price = total 
            requisition.save()
    if request.method =='POST'  and 'cot_denied'  in request.POST:
        requisition.status = "negado"      
        requisition.save()
    if request.method =='POST'  and 'btn_boungth' in request.POST:
        for product in products:
            prod_req=Requisition_product.objects.get(pk=product.id)
            prod_req.type_of_payment = request.POST["type_product"+str(product.id)]
            try: 
                form =request.FILES["ticket"+str(product.id)]
            except:
                form = None
            prod_req.ticket = form
            prod_req.save()     
        requisition.status="Aguardando pagamento"
        requisition.boug= datetime.now()
        requisition.save()    
        return redirect('purchase_request')
    if request.method == 'POST' and 'req_paid_out' in request.POST:
        for product in products:
            try: 
                form =request.FILES["voucher"+str(product.id)]
            except:
                form = None
            product.payment_voucher = form
            product.save()
        requisition.status = "Comprado"
        requisition.save() 
        return redirect('purchase_request')
    if request.method == 'POST' and 'prod_deliv' in request.POST:
        prod = Requisition_product.objects.get(pk = request.POST["prod_deliv"])
        prod.invoice = request.FILES["invoice"+str(prod.id)]
        prod.delivered = True
        prod.delivered_at = datetime.now()
        prod.save()
    if request.method == 'POST' and 'req_deliv' in request.POST:
        requisition.status= "entregue"
        requisition.save()
    if request.method =='POST' and 'edit_cotation1' in request.POST:
        req_prod = Requisition_product.objects.get(pk=request.POST["edit_cotation1"])
        req_prod.first_cotation = request.POST["first_cotation"]   
        req_prod.first_provider = request.POST["first_provider"]   
        req_prod.save()
    if request.method =='POST' and 'edit_cotation2' in request.POST:
        req_prod = Requisition_product.objects.get(pk=request.POST["edit_cotation2"])
        req_prod.second_cotation = request.POST["second_cotation"] 
        req_prod.second_provider = request.POST["second_provider"]     
        req_prod.save()
    if request.method =='POST' and 'edit_cotation3' in request.POST:
        req_prod = Requisition_product.objects.get(pk=request.POST["edit_cotation3"])   
        req_prod.third_cotation = request.POST["third_cotation"]   
        req_prod.third_provider = request.POST["third_provider"]   
        req_prod.save()
    if request.method =='POST' and 'cot_return' in request.POST:
        requisition.return_reason  = request.POST["reason"]   
        requisition.status = "Devolvida"   
        requisition.save()   
    context={
        'usuarioC':usuarioC,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
        'requisition':requisition,
        'products':products,
        
    }
    return render(request,'purchases/requisition_cotation.html',context) 

@login_required(login_url='/authentication/login') 
def manager_requisition(request):    
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    requisitions= Purchase_requisition.objects.filter(manager = request.user,status="Aguardando verificação do Gestor")
    
    
    context={
        'requisitions':requisitions,
        'usuarioC':usuarioC,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
        
        
    }
    return render(request,'purchases/manager_requisition.html',context)

@login_required(login_url='/authentication/login') 
def manager_req_details(request,purchase_requisition_id):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao") 
    purch_req = Purchase_requisition.objects.get(purchase_requisition_id=purchase_requisition_id)
    products = Requisition_product.objects.filter(purchase_requisition_id=purchase_requisition_id)
    if request.method == 'POST' and 'req_approved' in request.POST:
        purch_req.status = "Aguardando cotação"
        purch_req.approved = True
        purch_req.save()
        return redirect('manager_requisition')
    if request.method == 'POST' and 'req_denied' in request.POST:
        purch_req.status="negado"
        purch_req.save()
        return redirect('manager_requisition')
    context={
        'purch_req':purch_req,
        'products':products,
        'usuarioC':usuarioC,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
    }
    return render(request,'purchases/manager_req_details.html',context)

@login_required(login_url='/authentication/login') 
def financial_approval(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao") 
    requisitions= Purchase_requisition.objects.filter(purchase_manager_approval=True,approved=True ,cotation=True ,status="Aguardando aprovação financeira")
    list_status=['Aguardando aprovação financeira','aprovado','negado','Comprado','entregue']
    all_requisitions= Purchase_requisition.objects.filter(status__in = list_status )

    context={
    'requisitions':requisitions,
    'all_requisitions':all_requisitions,
    'usuarioC':usuarioC,
    'grupo':grupo,
    'grupos':grupos,
    'imageP':imageP,
    } 
    return render(request,'purchases/financial_approval.html',context)

@login_required(login_url='/authentication/login') 
def financial_appr_details(request,purchase_requisition_id):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao") 
    purch_req = Purchase_requisition.objects.get(purchase_requisition_id=purchase_requisition_id)
    products = Requisition_product.objects.filter(purchase_requisition_id=purchase_requisition_id)
    if request.method == 'POST' and 'req_approved' in request.POST:
        purch_req.status = "aprovado"
        purch_req.approved = True
        purch_req.save()
        return redirect('financial_approval')
    if request.method == 'POST' and 'req_denied' in request.POST:
        purch_req.status="negado"
        purch_req.save()
        return redirect('financial_approval')
    context={
        'purch_req':purch_req,
        'products':products,
        'usuarioC':usuarioC,
        'grupo':grupo,
        'grupos':grupos,
        'imageP':imageP,
        
    }
    return render(request,'purchases/financial_appr_details.html',context)
