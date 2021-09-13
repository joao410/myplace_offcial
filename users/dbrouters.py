from .models import Office,Payslip,UsuarioCorporativo,UsuarioPessoal,UsuarioDocumentos,UsuarioEndereco,UsuarioTrabalho,Companies,Contabancaria,Department,Area,Dashbaners

class UsersDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Office):
             # your model name as in settings.py/DATABASES
             return 'users'
          if (model == Payslip):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioCorporativo):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioPessoal):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioDocumentos):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioEndereco):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Companies):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioTrabalho):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Contabancaria):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Department):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Area):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Dashbaners):
            # your model name as in settings.py/DATABASES
            return 'users'
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Office):
             # your model name as in settings.py/DATABASES
             return 'users'
          if (model == Payslip):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioCorporativo):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioPessoal):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioDocumentos):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioEndereco):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Companies):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == UsuarioTrabalho):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Contabancaria):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Department):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Area):
            # your model name as in settings.py/DATABASES
            return 'users'
          if (model == Dashbaners):
            # your model name as in settings.py/DATABASES
            return 'users'  
          return None