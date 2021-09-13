
from django import template
from purchases.models import Requisition_product


register = template.Library()

@register.simple_tag
def reqprod(req_val):
    return Requisition_product.objects.filter(purchase_requisition_id = req_val)

@register.simple_tag
def reqcot(req_cot):
    return Requisition_product.objects.filter(purchase_requisition_id = req_cot)    


@register.simple_tag
def reqappr(req_appr):
    return Requisition_product.objects.filter(purchase_requisition_id = req_appr)    


@register.simple_tag
def reqbougth(req_bougth):
    return Requisition_product.objects.filter(purchase_requisition_id = req_bougth)    

#buyers 

@register.simple_tag
def reqmanappr(req_man_appr):
    return Requisition_product.objects.filter(purchase_requisition_id = req_man_appr)

@register.simple_tag
def reqfinappr(req_fin_appr):
    return Requisition_product.objects.filter(purchase_requisition_id = req_fin_appr)

@register.simple_tag
def reqden(req_den):
    return Requisition_product.objects.filter(purchase_requisition_id = req_den)

@register.simple_tag
def reqdeliv(req_deliv):
    return Requisition_product.objects.filter(purchase_requisition_id = req_deliv)

@register.simple_tag
def reqpay(req_pay):
    return Requisition_product.objects.filter(purchase_requisition_id = req_pay)


@register.simple_tag
def reqret(req_ret):
    return Requisition_product.objects.filter(purchase_requisition_id = req_ret)