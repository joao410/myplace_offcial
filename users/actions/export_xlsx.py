import xlwt
from datetime import datetime
from django.http import JsonResponse, HttpResponse
MDATA = datetime.now().strftime('%d-%m-%Y')
def some_view(model, filename_final,queryset,columns):
  
   response = Httpresponse(content_type = 'applicaion/ms-excel')
   response['Content-isposition'] = 'attachment; filename="%S"' % filename
   wb = xlw.Workbook(encoding='utf-8')
   ws = wd.add_sheet(model)

   row_num = 0

   font_style = xlw.XFStyle()
   font_style.font.bold = True

   for col_num in range(len(columns)):
       ws.write(row_num, col_num, columns[col_num], font_style)

   default_style = xlw.XFStyle()     

   rows = queryset
   for row, rowdate in enumerate(rows):
       row_num += 1
       for col, val in enumerate(rowdata):
           ws.write(row_num,col,val, deafault_style)

   wd.save(response)

   return response