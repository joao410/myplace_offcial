from django.contrib.auth.models import User, Group, GroupManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse
from .models import  Chamado , ImageLink, Chat
from users.models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Companies,UsuarioPessoal
from django.http import HttpResponseRedirect
from django.contrib import messages
from .filters import ChamadoFilter
from datetime import date, datetime, timedelta
import json
from django.conf import settings
from .forms import ImageForm, ImageForms

    


