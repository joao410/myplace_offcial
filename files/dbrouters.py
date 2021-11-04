from .models import Report_human_resources,Dashbaners,Calendar
class  FileDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Report_human_resources):
             # your model name as in settings.py/DATABASES
             return 'tickets'
          if (model == Dashbaners):
                # your model name as in settings.py/DATABASES
                return 'tickets'
          if (model == Calendar):
                # your model name as in settings.py/DATABASES
                return 'tickets'
        
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Report_human_resources):
             # your model name as in settings.py/DATABASES
             return 'tickets'
          if (model == Dashbaners):
                # your model name as in settings.py/DATABASES
                return 'tickets'
          if (model == Calendar):
                # your model name as in settings.py/DATABASES
                return 'tickets'      
          return None