
from django.contrib.auth import models
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from helpdesk.models import  Chamado,Chat,ImageLink
from users.models import UsuarioCorporativo,UsuarioDocumentos,UsuarioPessoal,UsuarioEndereco,UsuarioTrabalho,Office,Companies,Department,Area
from performance.models  import Announcement,Performance,Profile,Annou_Detail,Metas
from files.models import  Report_human_resources
from purchases.models import  Requisition_product,Purchase_requisition
from django.contrib.auth.models import User,Permission

 ###### DJANGO USER #####
class Permissionserializer(serializers.ModelSerializer):
      class Meta:
        model= Permission
        fields = '__all__'
class Userserializer(serializers.ModelSerializer):
    user_permissions= Permissionserializer(many=True)
    class Meta:
        model= User
        fields = ("username",
                "groups",
                "user_permissions",
                )

      ###### APP PERFORMANCE #####

class Announcementserializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields= '__all__'

class Performanceserializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self,obj):
        return obj.user.username

    class Meta:
        model = Performance
        fields= ("year",
                "month",
                "user",
                "porcentagem")
# class Profileserializer(serializers,serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields= '__all__'

# class AnnouDetailserializer(serializers,serializers.ModelSerializer):
#     class Meta:
#         model = Annou_Detail
#         fields= '__all__'

# class Metasserializer(serializers,serializers.ModelSerializer):
#     class Meta:
#         model = Metas
#         fields= '__all__'

 



#         ####### APP HELPDESK ######




class  Calledserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chamado
        fields= '__all__'

 
# class Chatserializer(serializers,serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#         fields= '__all__'
 
# class ImageLinkserializer(serializers,serializers.ModelSerializer):
#     class Meta:
#         model = ImageLink
#         fields= '__all__'






    

#             ######### APP FILES ########



# class  ReportHumanResopcesserializer(serializers,serializers.ModelSerializer):
#     class Meta :
#         model = Report_human_resources
#         fields = '__all__'
        


 
#             ####### APP PURCHASES #######


        
class PurchaseRequisitionserializer(serializers.ModelSerializer):
    class Meta :
        model = Purchase_requisition
        fields = '__all__'

class ProductRequisitionserializer(serializers.ModelSerializer):
    class Meta :
        model = Requisition_product
        fields = '__all__'

        

       


