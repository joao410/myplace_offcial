from .models import Chamado,ImageLink,Chat

class ChamadosDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Chamado):
             # your model name as in settings.py/DATABASES
             return 'tickets'
  
          if (model == ImageLink):
            # your model name as in settings.py/DATABASES
            return 'tickets'
          if (model == Chat):
            # your model name as in settings.py/DATABASES
            return 'tickets'
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Chamado):
             # your model name as in settings.py/DATABASES
             return 'tickets'

          if (model == ImageLink):
             # your model name as in settings.py/DATABASES
             return 'tickets'
          if (model == Chat):
             # your model name as in settings.py/DATABASES
             return 'tickets'
          return None