from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse
from .models import  User
from helpdesk.models import  Chamado, Image , ImageLink, Chat
from .models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Empresa, ImagePerfil, UsuarioPessoal,Cargo
from helpdesk.forms import ImageForm, ImageForms
from django.http import HttpResponseRedirect
from django.contrib import messages
from helpdesk.filters import ChamadoFilter
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User, Group, GroupManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse


# Create your views here.

@login_required(login_url='/authentication/login')    
def add_usuarios(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    g = Group.objects.all()
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    empresa = Empresa.objects.all()
    cargos = Cargo.objects.all()
    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,
    'g':g,  
    'grupo':grupo,
    'empresa':empresa,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP, 
    'cargos':cargos,  
    'form':ImageForm,
            }  
    if UsuarioPessoal.objects.all():
            Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].id
                

            codigo = Usuario_id + 10001
    else:
                    codigo = 10001
                                
    if request.method == 'POST' and 'add_usu' in request.POST:  
        #pessoal#
        nome = request.POST["nome"]
        apelido = request.POST["apelido"]
        cpf = request.POST["cpf"]
        genero = request.POST["genero"]
        cor = request.POST["cor"]
        ecivil = request.POST["ecivil"]
        escolaridade = request.POST["escolaridade"]
        datanasci = request.POST["datanasci"]
        municipionasc = request.POST["municipionasc"]
        ufnasci = request.POST["ufnasci"]
        paisnasci = request.POST["paisnasci"]
        nasciona = request.POST["nasciona"]
        mae = request.POST["mae"]
        pai = request.POST["pai"]
        pis = request.POST["pis"]
        teleitor =  request.POST["titulo"]
        ctrabalho = request.POST["carteira"]       
        serie = request.POST["serie"]
        uf = request.POST["ufc"]
        emissao = request.POST["emissao"]
        celp = request.POST["celp"]
        #trabalho# 
        
        emp = request.POST["empresa"]
        dep = request.POST["departamento"]       
        cargo = request.POST["cargo"]
        vtrans = request.POST["vtrans"]
        admissao = request.POST["admissao"]
        demissao = None
        tipo = request.POST["tipoadmissao"]
        indica =  request.POST["indica"]
        priempr = request.POST["priempr"]
        rtrab = request.POST["rtrab"]
        rprev = request.POST["rprev"]
        rjorn = request.POST["rjorn"]
        naativ = request.POST["naativ"]
        cat = request.POST["cat"]
        codf = request.POST["codf"]
        carh = request.POST["carh"]
        unisa = request.POST["unisa"]
        salvari = request.POST["salvari"]
        #documento#
        documento = request.POST["documento"]
        ndocumento = request.POST["numero"]
        oe = request.POST["oe"]
        de = request.POST["expedicao"]
        validade = request.POST["validade"]
        #endereço#
        cep = request.POST["cep"]
        tipo = request.POST["tipo"]
        num = request.POST["num"]
        ufatual = request.POST["ufatual"]
        muniatual = request.POST["muniatual"]
        bairro = request.POST["bairro"]
        logradouro = request.POST["logradouro"]
        complemento = request.POST["complemeno"]
        pais = request.POST["pais"]
        #corporativo#
        email1 = request.POST["email1"]       
        email2 = request.POST["email2"]       
        skype = request.POST["skype"]       
        cel = request.POST["cel"]       
        tel = request.POST["tel"]       
        ramal = request.POST["ramal"]       
        usuario = request.POST["usuario"]       
        senha = request.POST["senha"]   
        repassword = request.POST["senha"]    
        grupo = request.POST["grupo"] 

        gs = Group.objects.get(name=grupo)  
        if not nome:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not cpf:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not genero:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not cor:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not ecivil:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not escolaridade:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not datanasci:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not municipionasc:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not ufnasci:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not paisnasci:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not nasciona:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not mae:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not pai:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not cep:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context) 
        if not tipo:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not logradouro:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not num:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not ufatual:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not muniatual:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not bairro:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not complemento:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not pais:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)       
        if not pis:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not teleitor:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not emp:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not dep:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not cargo:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not ctrabalho:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not serie:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not uf:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not emissao:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not vtrans:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not admissao:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not demissao:
            demissao = None 
        if not codf:
            codf = 00
        if vtrans == "SIM":
           vtrans =  "VALE TRANSPORTE"
        if vtrans == "NÃo":
           vtrans =  "AJUDA DE CUSTO"       
        if not indica:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not grupo:
            messages.error(request, "Por favor preencha todos os campos")
            return render(request, 'users/add_usuarios.html', context)  
        if not User.objects.filter(username=usuario).exists():
            if not User.objects.filter(email=email1).exists():                
                if len(senha) < 6:
                    messages.error(request, "Senha muito curta(<6)")
                    return render(request, 'users/add_usuarios.html', context)
                
                if senha != repassword:
                    messages.error(request, "As senhas nao batem")
                    return render(request, 'users/add_usuarios.html', context)
                user = User.objects.create(username=usuario,email=email1)
                user.set_password(senha)
                user.is_active = True
                user.save()
                users = User.objects.get(username=usuario)
                usu = UsuarioPessoal.objects.create(codigo=codigo,nome=nome,genero=genero, apelido=apelido,cpf=cpf,cor=cor,ecivil=ecivil,escolaridade=escolaridade,pis=pis,tituloeleitor=teleitor,carteiratrabalho=ctrabalho,serie=serie,ufcarteiratrabalho=uf,datacarteiratrabalho=emissao,datanacimento=datanasci,ufnacimento=ufnasci,municipionacimento=municipionasc,paisnacimento=paisnasci,paisnacionalidade=nasciona,nomemae=mae,nomepai=pai)
             
                u = UsuarioPessoal.objects.get(nome=nome)
                c= Cargo.objects.get(cargo=cargo)
                usua = UsuarioTrabalho.objects.create(codigo=u,departamento=dep,empresa=emp,cargo=c,valetransporte=vtrans,dataadmissao=admissao,datademissao=demissao,indicativoadmissao=indica,primeiroemprego=priempr,regimetrabalho=rtrab,regimeprevidenciario=rprev,regimejornada=rjorn,naturezaatividade=naativ,categoria=cat,codigofuncao=codf,cargahorariam=carh,unidadesalarial=unisa,salariovariavel=salvari)
                usua.save()
                
                t = UsuarioTrabalho.objects.get(codigo=u)
                do = UsuarioDocumentos.objects.create(codigo=u,documento=documento,numerodocumento=ndocumento,orgao=oe,dataexpedissao=de,validade=validade)
                do.save()
                d =  UsuarioDocumentos.objects.get(codigo=u)
                en = UsuarioEndereco.objects.create(codigo=u, cep=cep,tipo=tipo,logradouro=logradouro,numero=num,ufatual=ufatual,municipioatul=muniatual,bairroatual=bairro,complemento=complemento,pais=pais)
                en.save()
                e = UsuarioEndereco.objects.get(codigo=u)
                usuar  = UsuarioCorporativo.objects.create(codigo=u,trabalho=t,documento=d,endereco=e,email=email1,emailCorporativo=email2,skype=skype,telefone=cel,tel=tel,ramal=ramal,usuario=users,grupo=gs)
                usuar.save()
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    nome = request.POST['usuario']
                    img = form.cleaned_data.get("imagem") 
                    obs=''
                    users = User.objects.get(username=usuario)
                    usuari = UsuarioCorporativo.objects.get(usuario=users)
                    us = usuari.codigo.nome
                    obj =ImagePerfil.objects.create(image=img,obs=obs,nome=us)
                    obj.save()
                    messages.success(request, 'Imagem adicionada')
                else:
                    messages.error(request, 'Imagem não adicionada')
                messages.success(request, "Usuario criado com sucesso")
                return redirect( 'presidente')
        elif User.objects.filter(username=usuario).exists and UsuarioCorporativo.objects.filter(usuario=user).exists:
              messages.error(request, 'Usuario existente')
        else:
                users = User.objects.get(username=usuario)
                usu = Usuarios.objects.create(name=nome,empresa=emp, departamento=dep,cargo=cargo,email=email1,email_corporativo=email2,skype=skype,telefone=cel,tel=tel,ramal=ramal,usuario=users,password=senha,grupo=gs)
                usu.save()
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    nome = request.POST['usuario']
                    img = form.cleaned_data.get("imagem") 
                    obs=''
                    users = User.objects.get(username=usuario)
                    usuari = Usuarios.objects.get(usuario=users)
                    obj =ImagePerfil.objects.create(usuario=usuari,image=img,obs=obs,nome=nome)
                    obj.save()
                    messages.success(request, 'Imagem adicionada')

                
    return render(request, 'users/add_usuarios.html', context)        
    
    
@login_required(login_url='/authentication/login')    
def edit_usuarios(request,id):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    g = Group.objects.all()
    grupo= usuarioC.grupo
   
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)
    
    filtro = ChamadoFilter()
    usu = UsuarioCorporativo.objects.get(pk=id)
    cod =usu.codigo.nome
    image = ImagePerfil.objects.get(nome=cod)
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
    'usu': usu,
    'image':image,
    
            }  
    if request.method == 'POST' and 'edit_usu' in request.POST:  
        nome = request.POST["nome"]
        emp = request.POST["empresa"]
        dep = request.POST["departamento"]       
        cargo = request.POST["cargo"]       
        email1 = request.POST["email1"]       
        email2 = request.POST["email2"]       
        skype = request.POST["skype"]       
        cel = request.POST["cel"]       
        tel = request.POST["tel"]       
        ramal = request.POST["ramal"]       
        usuario = request.POST["usuario"]       
        senha = request.POST["senha"]   
        repassword = request.POST["senha"]    
        grupo = request.POST["grupo"] 
        gs = Group.objects.get(name=grupo)  
  
        if  User.objects.filter(username=usuario).exists():
            if  User.objects.filter(email=email1).exists():                
                
                user = User.objects.get(username=usuario)
                user.set_password(senha)
                user.is_active = True
                user.save()
                users = User.objects.get(username=usuario)
                usu.name = nome
                usu.empresa = emp
                usu.departamento = dep
                usu.cargo = cargo
                usu.email = email1
                usu.email_corporativo = email2
                usu.skype = skype
                usu.telefone = cel
                usu.tel = tel
                usu.ramal = ramal
                usu.usuario = users
                usu.grupo= gs
                usu.save()
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    nome = request.POST['usuario']
                    img = form.cleaned_data.get("imagem") 
                    obs=''
                    users = User.objects.get(username=usuario)
                    usuari = Usuarios.objects.get(usuario=users)
                    obj =ImagePerfil.objects.get(usuario=usuari)
                    obj.image = img
                    obj.save()
                    messages.success(request, 'Imagem salva')
                else:
                    messages.error(request, 'Imagem não adicionada')
                messages.success(request, "Usuario editado  com sucesso")
                

    if request.method == 'POST' and 'exc_usu' in request.POST: 
        id = request.POST['exc_usu']
        usuario= Usuarios.objects.get(pk=id)
        usuario.delete()
        return redirect( 'presidente')         
                
    return render(request, 'users/edit_usuarios.html', context)        
@login_required(login_url='/authentication/login')    
def perfis(request):
    ids = request.POST["perfil"]
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    usuario = UsuarioCorporativo.objects.get(pk=ids)
    grupo= usuarioC.grupo
    codigo = usuarioC.codigo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome=codigo.nome)
    img = ImagePerfil.objects.get(nome=usuario.codigo.nome)
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
    'img':img, 
    'usuario':usuario,
            }  
    return render(request, 'users/perfis.html', context)        
    
@login_required(login_url='/authentication/login')    
def perfisuser(request):
    ids = request.POST["perfil"]
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    usuario = UsuarioCorporativo.objects.get(pk=ids)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    cod =usuario.codigo.nome
    image = ImagePerfil.objects.get(nome=cod)
    imageP = ImagePerfil.objects.get(nome=codigo)
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
    'image':image, 
    'usuario':usuario,
            }  
   
        
               
    return render(request, 'users/perfisuser.html', context)      
@login_required(login_url='/authentication/login')    
def home(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    codigo = usuarioC.codigo
    usuarioT= UsuarioTrabalho.objects.get(codigo=codigo)
    usuarioP = UsuarioPessoal.objects.get(nome=codigo.nome)
    usuarioE = UsuarioEndereco.objects.get(codigo=codigo)
    usuarioD = UsuarioDocumentos.objects.get(codigo=codigo)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome= codigo.nome)

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'usuarioT':usuarioT,
    'user' : user, 
    'usuarioP':usuarioP, 
    'usuarioE':usuarioE, 
    'usuarioD':usuarioD, 
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,    
            }  

    if request.method == 'POST' and 'salvar' in request.POST:
        
        nome = request.POST["name"]
        problema = request.POST["problem"]
        urgencia = request.POST["urgency"]
        if not nome:
                messages.error(
                    request, "Por favor preencha os campos ")
                return render(request, 'home/home.html', context)

        if not problema:
                messages.error(request, "Por favor escolha um assunto para tratar")
                return render(request, 'home/home.html', context)
        if not urgencia:
                messages.error(request, "Por favor escolha a urgencia do assunto")
                return render(request, 'home/home.html', context)        
        Chamado.objects.create(username=nome, problem=problema, urgency=urgencia)
        messages.success(request, 'Chamado criado com sucesso')



    return render(request, 'users/home.html', context) 
@login_required(login_url='/authentication/login')  
def presidente(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    users = UsuarioCorporativo.objects.all()
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome=codigo)

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'users' : users,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,    
            }  
    if request.method == 'GET':
        myFilter = ChamadoFilter(request.GET, queryset=users)
        users = myFilter.qs
               
        user = request.user
        usuarioC = UsuarioCorporativo.objects.get(usuario=user)
        grupo= usuarioC.grupo
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        grupos= usuarioC.grupo.name

        context = {
            'users':users,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }            


    return render(request, 'users/presidente.html', context)     



@login_required(login_url='/authentication/login')    
def problem(request): 
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    users = UsuarioCorporativo.objects.all()
    codigo = usuarioC.codigo
    usuarioT= UsuarioTrabalho.objects.get(codigo=codigo)
    usuarioP = UsuarioPessoal.objects.get(nome=codigo.nome)
    usuarioE = UsuarioEndereco.objects.get(codigo=codigo)
    usuarioD = UsuarioDocumentos.objects.get(codigo=codigo)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome= codigo.nome)

    filtro = ChamadoFilter()
    context = {
            'chamados': chamados,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'user' : user, 
            'users' : users,
            'usuarioC':usuarioC,
            'usuarioT':usuarioT,
            'usuarioP':usuarioP, 
            'usuarioE':usuarioE, 
            'usuarioD':usuarioD,
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }       
    if request.method == 'GET':
        myFilter = ChamadoFilter(request.GET, queryset=users)
        users = myFilter.qs 
        user = request.user
        usuarioC = UsuarioCorporativo.objects.get(usuario=user)
        grupo= usuarioC.grupo
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        grupo= usuarioC.grupo.name

        context = {
            'users':users,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            'usuarioT':usuarioT,
            'usuarioP':usuarioP, 
            'usuarioE':usuarioE, 
            'usuarioD':usuarioD,
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }            
    return render(request, 'users/problem.html', context)