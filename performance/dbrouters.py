from .models import Performance,Image,Announcement,Metas,Profile,Annou_Detail

class PerformanceDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Performance):
             # your model name as in settings.py/DATABASES
             return 'online'
          if (model == Image):
                # your model name as in settings.py/DATABASES
                return 'online'
          if (model == Announcement):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Metas):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Profile):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Annou_Detail):
            # your model name as in settings.py/DATABASES
            return 'online'
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Performance):
             # your model name as in settings.py/DATABASES
             return 'online'
          if (model == Image):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Announcement):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Metas):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Profile):
            # your model name as in settings.py/DATABASES
            return 'online'
          if (model == Annou_Detail):
            # your model name as in settings.py/DATABASES
            return 'online'
          return None