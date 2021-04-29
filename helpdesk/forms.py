from django import forms



class ImageForm(forms.Form):
    imagem = forms.ImageField( required= False , widget=forms.FileInput(attrs={'onchange':'loadFile(event)','multiple':'multiple' }))
class ImageForms(forms.Form):    
    imagens = forms.ImageField(required= False ,   widget=forms.FileInput(attrs={'onchange':'loadFiles(event)','value':'{{image.image.url}}' }))   
    
