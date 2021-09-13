from .models import Inputs,Log_association,Log_defect,Log_entrance,Places,Manufacturer,Manufacturer_address,Stock_loc
class InventoryDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Inputs):
             # your model name as in settings.py/DATABASES
             return 'inventory'
          if (model == Log_association):
                # your model name as in settings.py/DATABASES
                return 'inventory'
          if (model == Places):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_association):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_defect):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_entrance):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Manufacturer):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Manufacturer_address):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Stock_loc):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Inputs):
             # your model name as in settings.py/DATABASES
             return 'inventory'
          if (model == Log_association):
                # your model name as in settings.py/DATABASES
                return 'inventory'
          if (model == Places):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_association):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_defect):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Log_entrance):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Manufacturer):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Manufacturer_address):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          if (model == Stock_loc):
            # your model name as in settings.py/DATABASES
            return 'inventory'
          
          return None