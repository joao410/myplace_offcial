from django import forms



class ImageForm(forms.Form):
    imagem = forms.ImageField()


class ImportForm(forms.Form):
    file = forms.FileField(label='')

