from datetime import date,datetime, timedelta
from django.shortcuts import redirect, render
from django.template import context
from .models import Requisition_product, Purchase_requisition
from users.models import   UsuarioCorporativo 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group, User
from decimal import Context, Decimal
from helpdesk.forms import ImageForm, ImageForms

import os
# Create your views here.

