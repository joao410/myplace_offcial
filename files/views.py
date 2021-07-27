from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.utils import report 
import os
from .models import Report_human_resources
from datetime import date, datetime, timedelta
from users.models import UsuarioCorporativo,ImagePerfil
from django.contrib import messages



# Create your views here.


@login_required(login_url='/authentication/login')  
def report_rh(request):
    today = datetime.now()
    name = 'Relat_Profissionais__' +  today.strftime("%d_%m_%Y_%H_%M") + '.xlsx'
    old_file = os.path.join(settings.MEDIA_ROOT + '\\models_rh\\' + name )
    report_hr = Report_human_resources.objects.filter(file_name = name)
    if len(report_hr) < 2:   
        try:
            os.remove(old_file) 
        except:
            pass    
        report()

        file = Report_human_resources.objects.create(file=old_file, file_name=name)
        file.save()
    else:
        messages.error(request,'Limite de relatorios por dia alcançado!! Seu limite são 2 por dia.' )

    
    return redirect('reports') 

@login_required(login_url='/authentication/login') 
def reports(request):
    usuarioC = UsuarioCorporativo.objects.get(usuario=request.user)
    grupos= usuarioC.grupo.name
    report_hr = Report_human_resources.objects.all()
    try:
        imageP = ImagePerfil.objects.get(nome= codigo.nome)
        if not imageP.image:
            imageP = ImagePerfil.objects.get(nome= "padrao")
    except:
        imageP = ImagePerfil.objects.get(nome= "padrao")       
    if  request.user == 'Administrador':
        report_hr = Report_human_resources.objects.all()
        context= {
        'report_hr':report_hr,
        } 
        return render(request,'reports/index.html',context)

    context= {
    'report_hr':report_hr,
    'usuarioC':usuarioC,
    'grupos':grupos,
    'imageP':imageP,
    }    
    return render(request,'reports/index.html',context)  