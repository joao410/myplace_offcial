from django.contrib.auth.models import User, Group, GroupManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse
from .models import  Chamado, Image , ImageLink, Chat
from users.models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Empresa, ImagePerfil, UsuarioPessoal
from django.http import HttpResponseRedirect
from django.contrib import messages
from .filters import ChamadoFilter
from datetime import date, datetime, timedelta
import json
from django.conf import settings
from .forms import ImageForm, ImageForms
from gcm.api import GCMMessage

# Create your views here.   
@login_required(login_url='/authentication/login')
def chat(request, id):
    chamado = Chamado.objects.get(pk=id)
    chat= Chat.objects.filter(idChat= id).order_by("id")
    u = chamado
    context = {
        'chat': chat,
            }
    if  Chat.objects.filter(idChat= id).exists(): 
        chamado = Chamado.objects.get(pk=id)
        u = chamado.username
        user = User.objects.get(username=u)
        n = UsuarioCorporativo.objects.get(usuario=user)
        img = ImagePerfil.objects.get(nome=n.codigo.nome) 
        if not img.image:
            img = ImagePerfil.objects.get(nome= "padrao")   
        z = chamado.name.nome
     
        images  = ImagePerfil.objects.get(nome = z)
        if not images.image:
            images = ImagePerfil.objects.get(nome= "padrao")  
        context = {

        'values': chamado,
        'img':img,
        'z':z,
        'images':images,
        'chat': chat,
            }
          
    return render(request, 'chamado/chat.html', context)             

@login_required(login_url='/authentication/login')
def atendimento(request, id):
    
    

  

    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    chamado = Chamado.objects.get(pk=id)
    ticket = chamado.ticket
    try:
        image = Image.objects.get(ticket=ticket)
    except:
        image = Image.objects.get(nome="padrao")
    if not image.image:
        image = Image.objects.get(nome="padrao")
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    chat= Chat.objects.filter(idChat= id).order_by("id")
    u = chamado
    e = usuarioC.codigo.nome
    context = {

        'values': chamado,
        'grupo' : grupo,
        'grupos':grupos,
        'usuarioC':usuarioC,
        'image' : image,
        'imageP' : imageP, 
        'chat': chat,
            }
    if  Chat.objects.filter(idChat= id).exists(): 
        chamado = Chamado.objects.get(pk=id)
        u = chamado.username
        user = User.objects.get(username=u)
        n = UsuarioCorporativo.objects.get(usuario=user)
        img = ImagePerfil.objects.get(nome=n.codigo.nome)
        if not img.image:
            img = ImagePerfil.objects.get(nome= "padrao")  
        try:       
            images  = ImagePerfil.objects.get(nome =chamado.name.nome)
        except:    
             images  = ImagePerfil.objects.get(nome ="padrao")
        context = {

        'values': chamado,
        'grupo' : grupo,
        'grupos':grupos,
        'usuarioC':usuarioC,
        'image' : image,
        'imageP' : imageP, 
        'img':img,
        'z':z,
        'images':images,
        'chat': chat,
            }
          
    if request.method == 'POST' and 'aceitar' in request.POST:
        ids = request.POST['aceitar']
        user = request.user
        atendente = UsuarioCorporativo.objects.get(usuario=user)
        at =atendente.codigo.nome    
        a = UsuarioPessoal.objects.get(nome=at) 
        chamado = Chamado.objects.get(pk=ids)
        chamado.name =   a
        chamado.status="em atendimento"
        chamado.active= False
        chamado.save()  
               
        return redirect( 'atendimento',ids)

    if request.method == 'POST' and 'salvar' in request.POST:
        chamado = Chamado.objects.get(pk=id)
        obs = request.POST['obs']
        chamado.status="resolvido"
        chamado.obs_tecnico = obs
        chamado.active = False
        chamado.save()
        return redirect( 'dash_index')
                
    if request.method == 'POST' and 'reabrir' in request.POST:
        chamado = Chamado.objects.get(pk=id)                
        chamado.status="aberto"                
        chamado.active = True
        chamado.save()
        return redirect( 'atendimento',id)                 
    if request.method == 'POST' and 'redrh' in request.POST:
        chamado = Chamado.objects.get(pk=id)                              
        chamado.active = True
        chamado.grupo ='recursos humanos'
        chamado.save()
        return redirect( 'dash_index')                     
    if request.method == 'POST' and 'redti' in request.POST:
        chamado = Chamado.objects.get(pk=id)                              
        chamado.active = True
        chamado.grupo ='atendimento ti'
        chamado.save()
        return redirect( 'dash_index')                     

    
    if request.method == 'POST' and 'encerrar' in request.POST:
        chamado = Chamado.objects.get(pk=id)                
        chamado.status="resolvido"                
        chamado.active = False
        chamado.finalizado = e
        chamado.end_datetime = datetime.now()
        chamado.save()
        return redirect( 'dash_index')                     
    if request.method == 'POST' and 'send' in request.POST:
       chamado = Chamado.objects.get(pk=id) 
       From = request.POST["atendente"]
       mensage = request.POST["mensagem"]
       name = request.POST["nome"]
       if not mensage:
           messages.error(request, "Preencha o campo de mensagem por favor! ")
           return redirect('atendimento',id)     
       Chat.objects.create(idChat=chamado, From=From,mensagem=mensage,nome=name)
    return render(request, 'chamado/atendimento.html', context)

@login_required(login_url='/authentication/login')    
def linksup(request):
    user = request.user
    admin = Chamado.objects.all().order_by("-ticket")       
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-ticket")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-ticket")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    
    
    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP, 
    'form':ImageForm
            }  
    if request.method == 'POST' and 'cadastrar' in request.POST:        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            link = request.POST['link']
            img = form.cleaned_data.get("imagem") 
            if not img:
                messages.error(request, "Por favor escolha uma imagem")
                return render(request, 'chamado/linksup.html', context)
            if not link:
                messages.error(request, "Por favor preencha o link da imagem")
                return render(request, 'chamado/linksup.html', context)
            obj =ImageLink.objects.create(link=link,img=img)
            obj.save()
            messages.success(request, 'Link adicionado')
        else:
            messages.error(request, 'Link não adicionado')
        
    return render(request, 'chamado/linksup.html', context)        
      
@login_required(login_url='/authentication/login')
def dash_index(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    codigo = usuarioC.codigo
   
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    if usuarioC.grupo.name == "Administrador":
            user = request.user
            usuarioC = UsuarioCorporativo.objects.get(usuario=user)
            grupo= usuarioC.grupo
            codigo = usuarioC.codigo
            chamados = Chamado.objects.all().order_by('-ticket')   
            grupos= usuarioC.grupo.name
            imageP = ImagePerfil.objects.get(nome= codigo.nome)
            if not imageP.image:
                imageP = ImagePerfil.objects.get(nome= "padrao")        
            filtro = ChamadoFilter()
            context = {
            'chamados': chamados,
            'grupos': grupos,
            'usuarioC':usuarioC,
          
            'user' : user, 
             
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,
            'imageP':imageP,    
                }
            if request.method == 'GET':
                myFilter = ChamadoFilter(request.GET, queryset=chamados)
                chamados = myFilter.qs
                    
                user = request.user
                usuarioC = UsuarioCorporativo.objects.get(usuario=user)
                grupo= usuarioC.grupo
               
                codigo = usuarioC.codigo
                chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-ticket")
                grupos= usuarioC.grupo.name

                context = {
                    'chamados': chamados,
                    'chamados_abertos': chamados_abertos,
                    'grupos': grupos,
                    'usuarioC':usuarioC,
                    
                    'user' : user, 
                   
                    'grupo':grupo,
                    'filtro': filtro,  
                    'imageP':imageP,                   
                        }     
        
    else:        

        user = request.user
        admin = Chamado.objects.all().order_by('ticket')       
        user = request.user
        usuarioC = UsuarioCorporativo.objects.get(usuario=user)
        grupo= usuarioC.grupo
       
        codigo = usuarioC.codigo
        chamados = Chamado.objects.filter(grupo=grupo).order_by("ticket")    
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
        grupos= usuarioC.grupo.name
        codigo = usuarioC.codigo.nome
        imageP = ImagePerfil.objects.get(nome= codigo)
        if not imageP.image:
            imageP = ImagePerfil.objects.get(nome= "padrao")  
    

        filtro = ChamadoFilter()
        context = {
        'chamados': chamados,
        'chamados_abertos': chamados_abertos,
        'grupos': grupos,
        'usuarioC':usuarioC,
        'user' : user, 
        'grupo':grupo,
        'admin':admin, 
        'filtro': filtro,
        'imageP':imageP,    
                }  
        if request.method == 'GET':
            myFilter = ChamadoFilter(request.GET, queryset=chamados)
            chamados = myFilter.qs
                
            user = request.user
            usuarioC = UsuarioCorporativo.objects.get(usuario=user)
            grupo= usuarioC.grupo
            chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
            grupos= usuarioC.grupo.name

            context = {
                'chamados': chamados,
                'chamados_abertos': chamados_abertos,
                'grupos': grupos,
                'usuarioC':usuarioC,
                'user' : user,  
                'grupo':grupo,
                'filtro': filtro,  
                'imageP':imageP,                   
                    } 
    return render(request, 'chamado/dash_index.html', context)
    

    #    myFilter = ChamadoFilter(request.GET, queryset=chamados)
     #   chamados = myFilter.qs
      #         
       # user = request.user
        #usuario = Usuarios.objects.get(usuario=user)
        #grupo= usuario.grupo
        
        #chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        #grupos= usuario.grupo.name

        #context = {
         #   'chamados': chamados,
          #  'chamados_abertos': chamados_abertos,
           # 'grupos': grupos,
            #'usuarioC':usuarioC,
            #'user' : user,  
            #'grupo':grupo,
           # 'admin':admin, 
            #'filtro': filtro,  
            #'imageP':imageP,                   
                
    #return render(request, 'chamado/dash_index.html', context)        

@login_required(login_url='/authentication/login')
def tecnico(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  

    images = ImageLink.objects.filter(active=True)

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP, 
    'images':images   
            }  

    if request.method == 'POST' and 'inativar' in request.POST:  
        ids = request.POST["inativar"]
        images = ImageLink.objects.get(id=ids)
        images.active = False
        images.save()  

    
    return render(request, 'chamado/tecnicos.html', context)

@login_required(login_url='/authentication/login')
def id_chamado(request, id):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupo= usuarioC.grupo
    grupos= usuarioC.grupo.name
    chamado = Chamado.objects.get(pk=id)
    ticket = chamado.ticket
    try:
        image = Image.objects.get(ticket=ticket)
    except:
        image = Image.objects.get(nome="padrao")
    if not image.image:
        image = Image.objects.get(nome="padrao") 
   
        
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   
    chat= Chat.objects.filter(idChat= id).order_by('id')
    u = chamado
    e = usuarioC.codigo.nome
    context = {
        'values': chamado,
        'grupo' : grupo,
        'grupos':grupos,
        'usuarioC':usuarioC,
        'image' : image,
        'imageP' : imageP, 
        'chat':chat,
            }
    if  Chat.objects.filter(idChat= id).exists():  
        chamado = Chamado.objects.get(pk=id)
        u = chamado.username
        user = User.objects.get(username=u)
        n = UsuarioCorporativo.objects.get(usuario=user)
        img = ImagePerfil.objects.get(nome=n.codigo.nome)  
        if not img.image:
            img = ImagePerfil.objects.get(nome= "padrao")  
        context = {

        'values': chamado,
        'grupo' : grupo,
        'grupos':grupos,
        'usuarioC':usuarioC,
        'image' : image,
        'imageP' : imageP, 
        'img':img,
        'chat': chat,
            }
    if request.method == 'POST' and 'send' in request.POST:
       chamado = Chamado.objects.get(pk=id) 
       From = request.POST["cliente"]
       mensage = request.POST["mensagem"]
       name = request.POST["nome"]
       Chat.objects.create(idChat=chamado, From=From,mensagem=mensage,nome=name)
       return redirect( 'id_chamado',id)  
    if request.method == 'POST' and 'salvar' in request.POST:
        chamado = Chamado.objects.get(pk=id)
        obs = request.POST['obs']
        chamado.status="resolvido"
        chamado.obs_tecnico = obs
        chamado.active = False
        chamado.save()
        return redirect( 'dash_index')
                
    if request.method == 'POST' and 'reabrir' in request.POST:
        chamado = Chamado.objects.get(pk=id)                
        chamado.status="aberto"                
        chamado.active = True
        chamado.save()
        return redirect( 'dash_index')                     

    
    if request.method == 'POST' and 'encerrar' in request.POST:
        chamado = Chamado.objects.get(pk=id)                
        chamado.status="resolvido"                
        chamado.active = False
        chamado.finalizado = e
        chamado.save()
        return redirect( 'rh_chamado')                     
   
    return render(request, 'chamado/id_chamado.html', context)
  
def fastchamado(request):
    
    if Chamado.objects.all():
            chamado_id = Chamado.objects.all().order_by('-id')[0].id
                

            ticket = chamado_id + 10001
    else:
                    ticket = 10001
    try:
         user = request.user  
         context = {
            'user':user
         }
    except:
        pass     

    if request.method == 'POST':
        nome = request.POST["requisitante"]
        nome = nome.upper()
        assunto = request.POST["assunto"]
        des = request.POST["obs"]
        status = "aberto"
        grupo = "atendimento ti"
        urgencia = ""
        if User.objects.filter(username=nome).exists(): 
            Chamado.objects.create(username=nome, problem=assunto,status=status,ticket=ticket,urgency=urgencia, grupo=grupo, des_problem=des) 
            messages.success(request, 'Chamado criado com sucesso')
        else:
            context={
                'des':des,
            }
            messages.error(request, 'Usuario invalido')
           
    return render(request,'fastchamado.html',context)

@login_required(login_url='/authentication/login')   
def add_chamado(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    g = Group.objects.all()
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo
    imageP = ImagePerfil.objects.get(nome=codigo.nome)
    if not imageP.image:
        imageP = ImagePerfil.objects.get(nome= "padrao")  
    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,
    'g':g,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,   
    'form':ImageForm,
    'forms':ImageForms,
            }  

   
    if Chamado.objects.all():
            chamado_id = Chamado.objects.all().order_by('-id')[0].id
                

            ticket = chamado_id + 10001
    else:
                    ticket = 10001
                        
   

  
    if request.method == 'POST' and 'add_rh' in request.POST:
            nome = user
            grupo = request.POST["add_rh"]
            problema = request.POST["assunto"]
            urgencia = ""
            status = "aberto"
            data = date.today() 
            des = request.POST["obs"] 
            fin = "default"
           
            if not nome:
                    messages.error(
                    request, "Por favor preencha os campos ")
                    return render(request, 'chamado/add_chamado.html', context)

            if not problema:
                        messages.error(request, "Por favor escolha um assunto para tratar")
                        return render(request, 'chamado/add_chamado.html', context)
            if not des:
                    messages.error(request, "Por favor preencha a mensagem do assunto")
                    return render(request, 'chamado/add_chamado.html', context)        
            if not grupo:
                    messages.error(request, "Por favor escolha a urgencia do assunto")
                    return render(request, 'chamado/add_chamado.html', context)        
            Chamado.objects.create(username=nome, problem=problema,status=status,ticket=ticket,data=data,finalizado= fin,urgency=urgencia, grupo=grupo, des_problem=des) 
            messages.success(request, 'Chamado criado com sucesso')
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                chamados = Chamado.objects.get(ticket=ticket)  
                ticket = ticket     
                nome = user
                img = form.cleaned_data.get("imagem") 
                if not img:
                    img = ""
                obs = ''
                Image.objects.create( ticket=ticket, nome=nome, image=img, obs=obs )
               
                messages.success(request, 'Imagem adicionada')
            else:
                messages.error(request, 'Imagem não adicionada')

       
    if request.method == 'POST' and 'add_ti' in request.POST:
            nome = user
            grupo = request.POST["add_ti"]
            problema = request.POST["assunto"]
            urgencia = ""
            status = "aberto"
            des = request.POST["obs"] 
            data = date.today() 
            datetime_start = datetime.now()

            fin = "default"
            
            if not nome:
                    messages.error(
                    request, "Por favor preencha os campos ")
                    return render(request, 'chamado/add_chamado.html', context)

            if not problema:
                        messages.error(request, "Por favor escolha um assunto para tratar")
                        return render(request, 'chamado/add_chamado.html', context)
            if not des:
                    messages.error(request, "Por favor preencha a mensagem do assunto")
                    return render(request, 'chamado/add_chamado.html', context)        
            if not grupo:
                    messages.error(request, "Por favor escolha um grupo do assunto")
                    return render(request, 'chamado/add_chamado.html', context)        
            Chamado.objects.create(username=nome, problem=problema,status=status,ticket=ticket,urgency=urgencia,finalizado= fin, data=data,grupo=grupo, des_problem=des, start_datetime=datetime_start) 
            messages.success(request, 'Chamado criado com sucesso')
            form = ImageForms(request.POST, request.FILES)
            if form.is_valid():
                chamados = Chamado.objects.get(ticket=ticket)  
                ticket = ticket     
                nome = user
                img = form.cleaned_data.get("imagens") 
                obs = ''
                Image.objects.create( ticket=ticket, nome=nome, image=img, obs=obs )
               
                messages.success(request, 'Imagem adicionada')
            else:
                messages.error(request, 'Imagem não adicionada')
    return render(request, 'chamado/add_chamado.html', context) 

@login_required(login_url='/authentication/login')  
def rh_chamado(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    codigo = usuarioC.codigo
    
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(username=user).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome= codigo.nome)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")   

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,    
            }  
    if request.method == 'GET':
        myFilter = ChamadoFilter(request.GET, queryset=chamados)
        chamados = myFilter.qs     
        user = request.user
        admin = Chamado.objects.all()        
        usuarioC = UsuarioCorporativo.objects.get(usuario=user)
        codigo = usuarioC.codigo
       
        grupo= usuarioC.grupo
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        grupos= usuarioC.grupo.name

        context = {
            'chamados': chamados,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            
            'user' : user, 
          
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }            
    
        


    return render(request, 'chamado/rh_chamado.html', context)    


