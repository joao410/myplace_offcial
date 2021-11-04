from django.contrib.auth.models import Group
import fdb
import pandas as pd
from datetime import datetime 
import pandas as pd
from users.models import Contabancaria, Office, UsuarioCorporativo, UsuarioDocumentos, UsuarioEndereco, UsuarioPessoal, UsuarioTrabalho 
from users.dic import mydic
def update():
    con = fdb.connect(dsn='arena/3050:C:\CICOM\MECAUTO\DB\CICOM-JF.CDB', user='SYSDBA', password='masterkey')
    cur = con.cursor()
    all= UsuarioPessoal.objects.all()
    for current_user in all:
        try:
                SELECT = "SELECT * FROM  TAB_CAD_FUN where CM_CPF_FUN  = '" +  current_user.cpf + "'"
                cur.execute(SELECT)
                rows = cur.fetchall()
                colab = pd.DataFrame(rows)
                headers = [i[0] for i in cur.description]
                colab.columns = headers
                print( colab.loc[0][45])     
        except:
            try:
                work_user = UsuarioTrabalho.objects.get(code=current_user)
                print(work_user.code)
                if work_user.company.company_name == "ARENA VIDROS": 
                    LAST =  "SELECT max(CM_COD_FUN) FROM TAB_CAD_FUN  "
                    cur.execute(LAST)
                    rows = cur.fetchall()
                    last = pd.DataFrame(rows)
                    headers = [i[0] for i in cur.description]
                    last.columns = headers
                    id = last.iloc[0][0] + 1
                    print(id)
                    print(current_user.cpf )
                    INSERT = f"""INSERT INTO TAB_CAD_FUN (CM_COD_FUN,CM_CPF_FUN,CM_NUM_PIS) VALUES ( '{id}','{current_user.cpf}','{current_user.pis}')"""
                    cur.execute(INSERT)
                    con.commit()
                    print('success')
                  
                else:
                    print(work_user.company.company_name)    
                   
            except:
                print('error')
                
    All =  "SELECT * FROM  TAB_CAD_FUN  "
    SELECT = "SELECT * FROM  TAB_CAD_FUN where CM_CPF_FUN = '13532135133'"
    cur.execute(All)
    rows = cur.fetchall()
    prof = pd.DataFrame(rows)
    headers = [i[0] for i in cur.description]
    prof.columns = headers
    list = []
    for row in range(len(prof)):
            try:
                object =UsuarioPessoal.objects.get(cpf=prof.loc[row][27]) 
                user = UsuarioCorporativo.objects.get(code=object)
              
                for key,valor in zip(mydic.keys(),mydic.values()):
                    print( key , valor)
                   
                    try:
                            UPDATE2 =  "Update TAB_CAD_FUN set " + valor + " ='" + key + "' where CM_NUM_PIS  = '" + prof.loc[row][45] + "'"       
                            cur.execute(UPDATE2) 
                            con.commit()
                            print("deu certo")
                
                            list.append( [object.name,  str(key) , str(valor),"deu certo"])
                        
                    except:
                            list.append( [object.name,   str(key) , str(valor),"deu ruim"])
                            print('deu ruim') 

            except:
                pass
    excel = pd.DataFrame(list)  
    now = datetime.now()      
    excel.to_excel('Log_mypalce_' +  now.strftime("%d_%m_%Y_%H_%M") + '.xlsx' )   
def update_myplace():
        con = fdb.connect(dsn='arena/3050:C:\CICOM\MECAUTO\DB\CICOM-JF.CDB', user='SYSDBA', password='masterkey')
        cur = con.cursor()
        CARGO = "SELECT * FROM TAB_CAD_CARGO"
        NEW_SELECT = "SELECT * FROM  TAB_CAD_FUN where CM_NOM_FUN is not null and CM_CPF_FUN   is not null and CM_DAT_DEM is null"
        SELECT_FOTO = "SELECT * FROM  TAB_CAD_FUN where  CM_DAT_DEM is null"
        SELECT = "SELECT * FROM  TAB_CAD_FUN where CM_CPF_FUN = '46259391862'"
        All =  "SELECT * FROM  TAB_CAD_FUN  "
        cur.execute(NEW_SELECT)
        rows = cur.fetchall()
        prof = pd.DataFrame(rows)
        headers = [i[0] for i in cur.description]
        prof.columns = headers
        for row in range(len(prof)):
            try:
                if UsuarioPessoal.objects.filter(cpf=prof.loc[row][27]).exists():
                    object =UsuarioPessoal.objects.get(cpf=prof.loc[row][27]) 
                    object.schooling = prof.loc[row][14]
                    object.mother = prof.loc[row][69]
                    object.father = prof.loc[row][70]
                    object.birthdate_uf = prof.loc[row][66]
                    object.city_birth = prof.loc[row][65]
                    object.country_birth = prof.loc[row][67]
                    object.voter_title = prof.loc[row][43]
                    object.pis = prof.loc[row][45]
                    object.surname = prof.loc[row][5]
                    object.name = prof.loc[row][4]
                    object.gender = prof.loc[row][61]
                    object.color = prof.loc[row][62]
                    object.marital_status = prof.loc[row][14]
                    # object.personal_cell = prof.loc[row][12]
                    object.birthdate = prof.loc[row][1]
                    object.profile_image = "users\images\\" + prof.loc[row][101]
                    object.cod_mec = prof.loc[row][0]
                    object.save()
                
                    print("sucess person")
                else:
                    if UsuarioPessoal.objects.all():
                        Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].id

                        codigo = Usuario_id + 10001
                    else:
                        codigo = 10001
                    object=UsuarioPessoal.objects.create(code=codigo,name=prof.loc[row][4],cpf=prof.loc[row][27],birthdate=prof.loc[row][1])    
                    print('new person')
                try:
                    office =Office.objects.filter(office=prof.loc[row][16])
                except:
                    office = None    
                print(office)  
                if  UsuarioTrabalho.objects.filter(code=object).exists():
                    user = UsuarioTrabalho.objects.get(code=object)
                    user.note = prof.loc[row][41]
                    # user.office = office
                    user.admission_date =prof.loc[row][2]
                    user.admission_type = prof.loc[row][75]
                    user.admission_indicative = prof.loc[row][76]
                    user.first_job = prof.loc[row][77]
                    user.work_regime =prof.loc[row][80]
                    user.day_regime = prof.loc[row][82]
                    user.nature_activity = prof.loc[row][83]
                    user.pension_scheme =prof.loc[row][81]
                    user.category = prof.loc[row][84]
                    user.function_code = prof.loc[row][85]
                    user.workload =prof.loc[row][60]
                    user.wage_unit = prof.loc[row][88]
                    user.variable_salary =prof.loc[row][87]
                    user.save()
                    print("sucess work")
                else:    
                    user = UsuarioTrabalho.objects.create(code=object)
                    print('new work')
              
                    
                if UsuarioEndereco.objects.filter(code=object).exists():
                    end =UsuarioEndereco.objects.get(code=object)
                    end.zip_code=prof.loc[row][10]
                    end.type = prof.loc[row][71]
                    end.public_place= prof.loc[row][78]
                    end.number = prof.loc[row][48]
                    end.uf = prof.loc[row][9]
                    end.city=prof.loc[row][8]
                    end.district=prof.loc[row][7]
                    end.complement=prof.loc[row][49]
                    end.country=prof.loc[row][79]
                    end.save()
                    print("sucess adress")
                else:    
                    end =UsuarioEndereco.objects.create(code=object)   
                    print('new end')
                    
                if UsuarioDocumentos.objects.filter(code=object).exists():
                    second_object = UsuarioDocumentos.objects.get(code=object)
                    second_object.document ="RG"
                    second_object.document_number = prof.loc[row][28]
                    second_object.organ= prof.loc[row][54]
                    second_object.dispatch_date =  prof.loc[row][55]
                    second_object.save()
                    print("sucess doc")
                else:
                       UsuarioDocumentos.objects.create(code=object)
                       print('new doc')
                if  Contabancaria.objects.filter(code=object).exists(): 
                    third_object = Contabancaria.objects.get(code=object)
                    third_object.bank=prof.loc[row][34]
                    third_object.agency=prof.loc[row][35]
                    third_object.account=prof.loc[row][36]
                    third_object.save()
                    print("sucess banck")
                else:
                    Contabancaria.objects.create(code=object)    
                    print('new bank')
                if UsuarioCorporativo.objects.filter(code=object).exists():
                    corp_user = UsuarioCorporativo.objects.get(code=object)
                    corp_user.work=user
                    corp_user.bank =third_object
                    corp_user.address = end
                    corp_user.documents = second_object
                    if corp_user.group ==None:
                        corp_user.group = Group.objects.get(name="Colaborador")
                    corp_user.save()
                  
                        
                    print("sucess corp")
                else:
                    UsuarioCorporativo.objects.create(code=object)
                    print('new corp')


                


    
                # if UsuarioPessoal.objects.filter(name=prof.loc[row][4]).exists():
                
                #     object =UsuarioPessoal.objects.get(name=prof.loc[row][4])
                #     object.birthdate = prof.loc[row][1]
                #     object.surname = prof.loc[row][5]
                #     object.save()             
                #     try:  
                #         second = UsuarioTrabalho.objects.get(code=object)
                #         office = Office.objects.filter(office =prof.loc[row][16])[0]
                #         second.office = office
                #         second.save()
                #     except:
                #         pass    

                # print(prof.loc[row][1],prof.loc[row][4])


                # for row in range(len(prof)):
                #     if not  Office.objects.filter(office=prof.loc[row][16]).exists():
                #             Office.objects.create(office=prof.loc[row][16])
                #     elif Office.objects.filter(office=prof.loc[row][1]).exists():
                #         Office.objects.create(office=prof.loc[row][1]).delete()
                #     else:
                #         pass
            except:
                print("fail")      
                    