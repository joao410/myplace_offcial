from django.conf import settings
import pandas as pd
import fdb
from datetime import date,datetime, timedelta
import datetime as dt
import time
import os
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from shutil import copyfile


# def teste_excel():
    
#         today = date.today() + timedelta(days=1)
#         template_file = 'media\\excel_RH\\TEMPLATE_PROFISSIONAIS.xlsx'
#         name = 'Relat_Profissionais__' +  today.strftime("%d_%m_%Y") + '.xlsx' 
#         output_file = 'media\\excel_RH\\' + name
#         copyfile(template_file, output_file)
#         return output_file



def report():
        today = datetime.today()
        con = fdb.connect(dsn='arena/3050:C:\CICOM\MECAUTO\DB\CICOM.CDB', user='SYSDBA', password='masterkey')


        cur = con.cursor()

        #Tabela Vendas - Lembrar de abrir via Excel para checar os dados de dentro.
        SELECT = "SELECT * FROM TAB_CAD_FUN"
        cur.execute(SELECT)
        rows = cur.fetchall()
        prof = pd.DataFrame(rows)
        headers = [i[0] for i in cur.description]
        prof.columns = headers

        prof_2 = prof[['CM_COD_FUN','CM_NOM_FUN','CM_GENERO','CM_GRAU_INSTRU','CM_NAS_FUN','CM_CEP_FUN','CM_END_FUN','CM_NUM_END','CM_CID_FUN','CM_MAIL_FUN','CM_DAT_ADM','CM_REGIME_TRAB','CM_REGIME_PREV','CM_REGIME_JORN','CM_COD_CARGO','CM_COD_DEPTO','CM_DAT_DEM']]


        prof_2['CM_REGIME_TRAB'].replace({"1":"CLT","2":"RJU","3":"RJP"}, inplace=True)
        prof_2['CM_REGIME_PREV'].replace({"1":"RGPS","2":"RPPS","3":"RPPE"}, inplace=True)
        prof_2['CM_REGIME_JORN'].replace({"1":"Submetidos a Horário de Trabalho","2":"Atividade Externa Especificada","3":"Funções específicas"}, inplace=True)




        today = datetime.now()
        con = fdb.connect(dsn='arena/3050:C:\CICOM\MECAUTO\DB\CICOM.CDB', user='SYSDBA', password='masterkey')


        cur = con.cursor()

        #Tabela Vendas - Lembrar de abrir via Excel para checar os dados de dentro.
        SELECT = "SELECT * FROM TAB_CAD_CARGO"


        cur.execute(SELECT)
        rows = cur.fetchall()
        cargo = pd.DataFrame(rows)
        headers = [i[0] for i in cur.description]
        cargo.columns = headers




        lista_cargo=[]
        for item in prof_2['CM_COD_CARGO']:
            try:
                lista_cargo.append(cargo[cargo['CM_COD_CARGO']==int(item)]['CM_DESCRICAO'].item())
            except:
                lista_cargo.append('CARGO NAO DEFINIDO')
                
        prof_2['CARGO']=lista_cargo


        today = datetime.today()
        con = fdb.connect(dsn='arena/3050:C:\CICOM\MECAUTO\DB\CICOM.CDB', user='SYSDBA', password='masterkey')


        cur = con.cursor()

        #Tabela Vendas - Lembrar de abrir via Excel para checar os dados de dentro.
        SELECT = "SELECT * FROM TAB_CAD_DEPTO"


        cur.execute(SELECT)
        rows = cur.fetchall()
        depto = pd.DataFrame(rows)
        headers = [i[0] for i in cur.description]
        depto.columns = headers






        lista_dep=[]
        for item in prof_2['CM_COD_DEPTO']:
            try:
                lista_dep.append(depto[depto['CM_COD_DEPTO']==int(item)]['CM_DESCRICAO'].item())
            except:
                lista_dep.append('DEPT NAO DEFINIDO')
                
        prof_2['DEPT']=lista_dep




        prof_2.drop('CM_COD_CARGO',  axis='columns', inplace=True)
        prof_2.drop('CM_COD_DEPTO',  axis='columns', inplace=True)


        template_file = 'media\\excel_RH\\TEMPLATE_PROFISSIONAIS.xlsx'
        name = 'Relat_Profissionais__' +  today.strftime("%d_%m_%Y_%H_%M") + '.xlsx' 
        output_file =  settings.MEDIA_ROOT +  '\\models_rh\\' + name
      

        copyfile(template_file, output_file)
        wb = load_workbook(output_file)

        ws = wb['Profissionais']
        ws['D2'] =today.strftime("%d/%m/%Y-%H:%M:%S.%f")



        col_preco = ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']


        for i, r in zip(range(len(prof_2)),dataframe_to_rows(prof_2, index=False, header=False)):
                for col, item in zip(col_preco,r):
                    ws[col+str(i+8)] =item



            
                    
        wb.save(output_file)
       

        
      
  
