from .models import Purchase_requisition,Requisition_product

class PurchasesDBRouter:
       def db_for_read (self, model, **hints):
          if (model == Purchase_requisition):
             # your model name as in settings.py/DATABASES
             return 'purchases'
          if (model == Requisition_product):
            # your model name as in settings.py/DATABASES
            return 'purchases'
       
         
          return None
       
       def db_for_write (self, model, **hints):
          if (model == Purchase_requisition):
             # your model name as in settings.py/DATABASES
             return 'purchases'
          if (model == Requisition_product):
            # your model name as in settings.py/DATABASES
            return 'purchases'
          
          return None