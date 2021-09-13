import django_filters as df
from .models import Chamado, UsuarioPessoal
from django import forms
from users.models import UsuarioPessoal



class ChamadoFilter(df.FilterSet):
    ticket = df.CharFilter(lookup_expr='icontains', label="Ticket:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'}))
    username = df.CharFilter(lookup_expr='icontains', label="Username:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'}))
    name = df.CharFilter(lookup_expr='icontains', label="name:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'}))
    status = df.CharFilter(lookup_expr='icontains', label="status:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'}))
    problem = df.CharFilter(lookup_expr='icontains', label="problem:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'})) 
    create = df.DateFilter(lookup_expr='icontains', label="create:", widget=forms.DateInput(attrs={'id' : 'myfieldid1', 'type':'date'})) 
    grupo = df.CharFilter(lookup_expr='icontains', label="grupo:", widget=forms.TextInput(attrs={'id' : 'myfieldid1'}))
    departamento = df.CharFilter(lookup_expr='icontains', label="departamento:", widget=forms.TextInput(attrs={'id' : 'myfieldid_'}))



    start_date = df.DateFilter(field_name="data", lookup_expr='gte', label="", widget=forms.TextInput(attrs={'id' : 'myfieldid'}) )
    end_date = df.DateFilter(field_name="data", lookup_expr='lte', label="", widget=forms.TextInput(attrs={'id' : 'myfieldid'}) )
    

    class Meta:
        model = Chamado
        fields = ['ticket','username','name','status','problem','create','grupo']
    class Meta:
        model = UsuarioPessoal
        fields = ['name','departamento']






