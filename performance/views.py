from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Announcement, Annou_Detail, Image, Profile, Performance
from django.contrib.auth.decorators import login_required
from .forms import ImageForm , ImportForm
import xlrd
from django.contrib import messages
import datetime
import os
from users.models import UsuarioCorporativo


@login_required(login_url='/authentication/login')
def index(request):
    user = request.user
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    grupos= usuarioC.grupo.name
    
    
    today = datetime.date.today()

    image_profile = Profile.objects.get(user=request.user).image_profile

    announcements = Announcement.objects.filter(active=False)

    size_complete_month = len(Announcement.objects.filter(complete=True, date_complete__month = today.month))
    test_erro = "False"
   
    performance = Performance.objects.filter(month=today.month, year=today.year)
    try:
        def complete_anuncio():
            announcements = Announcement.objects.filter(description_active=True, images_active=True)
            for announcement in announcements:
                announcement.complete = True
                announcement.active = True
                announcement.date_complete = datetime.datetime.now()
                announcement.save()
        
        complete_anuncio()
    except:
        pass
    try:
        def update_page():
            usuarios = User.objects.filter(groups__name='Online')


            for usuario in usuarios:
                profile_meta = Profile.objects.get(user=usuario)
                try:
                    meta = profile_meta.metas.all()[0]
                except:
                    pass 

                try:
                    update_perf = Performance.objects.get(month=today.month, year=today.year, user=usuario, meta=meta)
                    if usuario.username == 'carolina':
                        meta_carol = len(Announcement.objects.filter(user=usuario,description_active=True, description_complete__month=today.month))
                        update_perf.conclude = int(meta_carol)
                        update_perf.porcentagem = int((meta_carol*100)/meta.meta)
                        update_perf.save()
                    else:
                        a = len(Announcement.objects.filter(user_image=usuario.username ,image_complete__month=today.month))
                        b = len(Image.objects.filter(user=usuario.username ,create__month=today.month))
                        update_perf.conclude = int(a+b)
                        update_perf.porcentagem = int((a+b)*100/meta.meta)
                        update_perf.save()

                except:
                    Performance.objects.create(month=today.month, year=today.year, user=usuario, meta=meta)


            performance = Performance.objects.filter(month=today.month, year=today.year)
            context = {
                'announcements': announcements,
                'form':ImportForm(),
                'user':request.user,
                'form_image':ImageForm,
                'size_complete_month':size_complete_month,
                'performance':performance,
                'image_profile':image_profile,
                
            }


            return render(request, 'performance/index.html', context)
        update_page()
    except:
        pass

    if request.method == 'GET':
       
        context = {
            'announcements': announcements,
            'form':ImportForm(),
            'user':request.user,
            'test_erro':test_erro,
            'size_complete_month':size_complete_month,
            'form_image':ImageForm,
            'performance':performance,
            'image_profile':image_profile,
            'grupos':grupos,
        }
        return render(request, 'performance/index.html', context)


    if request.method == 'POST' and 'add_produto' in request.POST:
        sku = request.POST['sku_add']
        name = request.POST['nome_add']
       
        try :
            anuncio = Announcement.objects.get(sku=sku)
            messages.error(request, f'O SKU "{sku}" já está cadastrado')

               
        except:
            announcement = Announcement.objects.create(name=str(name), sku=int(sku))
            messages.success(request, f'{sku} - {name} adicionado com sucesso!')
            
        announcements = Announcement.objects.filter(active=False)

        context = {
            'announcements': announcements,
            'form':ImportForm(),
            'user':request.user,
            'test_erro':test_erro,
            'size_complete_month':size_complete_month,
            'form_image':ImageForm,
            'performance':performance,
            'image_profile':image_profile,

        }


        return render(request, 'performance/index.html', context)


    if request.method == 'POST' and 'btn_desc' in request.POST:
        sku = request.POST['btn_desc']
        announcement = Announcement.objects.get(sku=sku)
        announcement.editable = False
        announcement.user = request.user
        announcement.save()
        return redirect('anuncio' , sku)


    if request.method == 'POST' and 'btn_import' in request.POST:
        input_excel = request.FILES['file']
        workbook = xlrd.open_workbook(file_contents=input_excel.read())
        sheet = workbook.sheets()[0]
        names = sheet.col_values(0,1)
        skus = sheet.col_values(1,1)
        
        erro_list = list()

        for name, sku in zip (names, skus):

            try :
                anuncio = Announcement.objects.values().get(sku=sku)
                erro_list.append(anuncio)
                test_erro = True
                           
            except:
                announcement = Announcement.objects.create(name=str(name), sku=int(sku))

        announcements = Announcement.objects.filter(active=False)
        
        context = {
            'announcements': announcements,
            'form':ImportForm(),
            'user':request.user,
            'test_erro':test_erro,
            'erro_list':erro_list,
            'size_complete_month':size_complete_month,
            'form_image':ImageForm,
            'performance':performance,
            'image_profile':image_profile,
        }

        return render(request, 'performance/index.html', context)    

    
    if request.method == 'POST' and 'update_db' in request.POST:
        usuarios = User.objects.filter(groups__name='Online')


        for usuario in usuarios:
            profile_meta = Profile.objects.get(user=usuario)
            meta = profile_meta.metas.all()[0]

            try:
                update_perf = Performance.objects.get(month=today.month, year=today.year, user=usuario, meta=meta)
                if usuario.username == 'carolina':
                    meta_carol = len(Announcement.objects.filter(user=usuario,description_active=True, description_complete__month=today.month))
                    update_perf.conclude = int(meta_carol)
                    update_perf.porcentagem = int((meta_carol*100)/meta.meta)
                    update_perf.save()
                else:
                    a = len(Announcement.objects.filter(user_image=usuario.username ,image_complete__month=today.month))
                    b = len(Image.objects.filter(user=usuario.username ,create__month=today.month))
                    update_perf.conclude = int(a+b)
                    update_perf.porcentagem = int((a+b)*100/meta.meta)
                    update_perf.save()

            except:
                Performance.objects.create(month=today.month, year=today.year, user=usuario, meta=meta)


        performance = Performance.objects.filter(month=today.month, year=today.year)
        context = {
            'announcements': announcements,
            'form':ImportForm(),
            'user':request.user,
            'form_image':ImageForm,
            'size_complete_month':size_complete_month,
            'performance':performance,
            'image_profile':image_profile,
            
        }


        return render(request, 'performance/index.html', context)


@login_required(login_url='/authentication/login')
def announcement(request, sku):

    image_profile = Profile.objects.get(user=request.user).image_profile
    announcement = Announcement.objects.get(sku=sku)
    images = Image.objects.filter(announcement=announcement)
    details = Annou_Detail.objects.filter(anuncio=announcement)

    if request.method=='GET':

        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                'details':details,
                'image_profile':image_profile,
            }

        return render(request, 'performance/announcement.html', context)


    if request.method == 'POST' and 'btn_image' in request.POST:
       
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            #nome = form.cleaned_data.get("nome")
            nome = request.POST['name_img']
            img = form.cleaned_data.get("imagem")




            if not announcement.image_zero:
                announcement.image_zero = img
                announcement.user_image = request.user.username
                announcement.image_complete = datetime.datetime.now()
                announcement.number_images = 1 +  len(Image.objects.filter(announcement=announcement))
                
            else:
                Image.objects.create(announcement=announcement, name=nome, user=request.user, image=img, )
                announcement.number_images = 1 + len(Image.objects.filter(announcement=announcement))
                
    
            
            if announcement.number_images >= 3:
                announcement.images_active = True
            
            announcement.save()


            context = {
                    'announcement': announcement,
                    'images': images,
                    'form': ImageForm,
                    'user':request.user,
                    'details':details,
                    'image_profile':image_profile,
                   
                }

            return render(request, 'performance/announcement.html', context)


    if request.method == 'POST' and 'btn_save' in request.POST:
        announcement.description = request.POST['descricao']
        announcement.description_active = True
        announcement.description_complete = datetime.datetime.now()
        announcement.save()

        announcement = Announcement.objects.get(sku=sku)


        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                 'details':details,
                 'image_profile':image_profile,
                # 'n_tasks':n_tasks,
            }

        return redirect('index')


    if request.method == 'POST' and 'btn_edit' in request.POST:
        announcement.description_active = False
        announcement.complete = False
        announcement.save()

        announcement = Announcement.objects.get(sku=sku)


        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                 'details':details,
                 'image_profile':image_profile,
                # 'n_tasks':n_tasks,
            }

        return render(request, 'performance/announcement.html', context)


    if request.method == 'POST' and 'btn_desc' in request.POST:
        announcement = Announcement.objects.get(sku=sku)
        announcement.editable = False
        announcement.user = request.user
        announcement.save()



        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                'details':details,
                'image_profile':image_profile,

                # 'n_tasks':n_tasks,
            }


        return render(request, 'performance/announcement.html', context)


    if request.method == 'POST' and 'add_detail_annou' in request.POST:
        detail = request.POST['detail_add']
        Annou_Detail.objects.create(anuncio=announcement, detail=detail)
        details = Annou_Detail.objects.filter(anuncio=announcement)

        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                'details':details,
                'image_profile':image_profile,

               
            }


        return render(request, 'performance/announcement.html', context)

    
    if request.method == 'POST' and 'btn_del_detail' in request.POST:
        id = request.POST['btn_del_detail']
        try:
            detail = Annou_Detail.objects.get(id=id)
            detail.delete()
        except:
            pass    

        context = {
                'announcement': announcement,
                'images': images,
                'form': ImageForm,
                'user':request.user,
                'details':details,
                'image_profile':image_profile,

               
            }


        return render(request, 'performance/announcement.html', context)




# View Modulo
def del_image_zero(request, sku):
    announcement = Announcement.objects.get(sku=sku)
    announcement.number_images = len(Image.objects.filter(announcement=announcement))
    announcement.image_zero.delete(save=True)
    return redirect('anuncio', sku)


def del_image_anno(request,id):
    image = Image.objects.get(id=id)
    sku = image.announcement.sku
    image.image.delete(save=True)
    image.delete()
    announcement = Announcement.objects.get(sku=sku)
    


    try :
        if announcement.image_zero:
            announcement.number_images = 1 + len(Image.objects.filter(announcement=announcement))
            announcement.save()
    except:
        announcement.number_images = len(Image.objects.filter(announcement=announcement))
        announcement.save()
    if announcement.number_images < 3:   
        announcement.images_active = False
        announcement.save()
    return redirect('anuncio', sku)


# EndView Modulo

@login_required(login_url='/authentication/login')
def complete_anno(request):
    image_profile = Profile.objects.get(user=request.user).image_profile
    announcements = Announcement.objects.filter(complete=True)

    context = {
        'announcements':announcements,
        'image_profile':image_profile,
    }
    return render(request, 'performance/complete_anno.html', context)


@login_required(login_url='/authentication/login')
def search_page(request):
    return render(request, 'performance/search.html')


@login_required(login_url='/authentication/login')
def tasksView(request):
    image_profile = Profile.objects.get(user=request.user).image_profile
    tasks = Announcement.objects.filter(user__isnull=False, description_active=False, complete=False)
    description_tasks = Announcement.objects.filter(description_active=True, complete=False)
    initial_tasks = Announcement.objects.filter(editable=True, number_images=0) 
      


    
    images_tasks = Announcement.objects.filter(images_active=True, complete=False)
    

    # n_tasks = len(Task.objects.filter(user=request.user, complete=False , active=True))
    
    if request.method == 'GET':
        image_profile = Profile.objects.get(user=request.user).image_profile
        tasks = Announcement.objects.filter(user__isnull=False, description_active=False, complete=False)


        context = {
            'tasks':tasks,
            'descri_tasks':description_tasks,
            'image_tasks':images_tasks,
            'user':request.user,
            'image_profile':image_profile,
            'initial_tasks':initial_tasks,
            

            # 'n_tasks':n_tasks,
        }
        return render(request, 'performance/tasks.html', context)
    

    if request.method == 'POST' and 'btn_cancel' in request.POST:
        id = request.POST['btn_cancel']
        announcement = Announcement.objects.get(pk=id)
      
        announcement.editable = True
        announcement.description_active = False
        announcement.user = None
        announcement.save()


        context = {
            'tasks':tasks,
            'descri_tasks':description_tasks,
            'image_tasks':images_tasks,
            'user':request.user,
            'image_profile':image_profile,
            # 'n_tasks':n_tasks,
        }

        return render(request, 'performance/tasks.html', context)
  

