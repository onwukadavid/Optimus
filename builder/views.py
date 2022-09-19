from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Template, UserTemplate, User
from django.core.serializers import serialize
import json

#DISPLAY ALL TEMPLATES IN THE DATABASE
def templates(request):
    templates = Template.objects.all()
    return render(request, 'allTemplates.html', {"templates":templates})


#CREATE USER TEMPLATE FROM PRE-EXISTING ALL TEMPLATES
def editTemplate(request, id):
    template = Template.objects.get(pk=id)
    return render(request, 'newtemplate.html', {"template":template})

def editTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST.get('html')
        css = request.POST.get('css')
        name = request.POST.get('name')
        thumbnails = request.FILES.get('thumbnails')
        usertemplate = UserTemplate.objects.create(
            name=name, 
            html=html, 
            css=css,
            thumbnails=thumbnails,
            created_by = request.user
        )
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})
    

def saveTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        name = request.POST.get('name')
        thumbnails = request.FILES.get('thumbnails')
        usertemplate = UserTemplate.objects.create(
            name=name, 
            html=html, 
            css=css,
            thumbnails=thumbnails,
            created_by = request.user
        )
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})


#USER TEMPLATE
#addnewtemplate in url.py
def addusertemplate(request):
    return render(request, 'new_user_template.html')


def edit_userTemplates(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'new_user_template.html', {"usertemplate":usertemplate})


def edit_userTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST.get('html')
        css = request.POST.get('css')
        usertemplate = UserTemplate.objects.get(pk=id)
        usertemplate.html = html
        usertemplate.css = css
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})

def saveUserTemplate(request):
    if request.POST.get('action') == 'create-user-template':
        html = request.POST.get('html')
        css = request.POST.get('css')
        name = request.POST.get('name')
        thumbnails = request.FILES.get('thumbnails')
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.create(
            name=name, 
            html=html, 
            css=css,
            thumbnails=thumbnails,
            created_by = request.user
        )
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})


#ALL TEMPLATES
def add_allTemplate(request):
    return render(request, 'new_all_template.html',)


def save_allTemplate(request):
    if request.POST.get('action') == 'create-alltemplate':
        html = request.POST.get('html')
        css = request.POST.get('css')
        name = request.POST.get('name')
        thumbnails = request.FILES.get('thumbnails')
        template = Template.objects.create(
            name=name, 
            html=html, 
            css=css,
            thumbnails = thumbnails
        )
        template.save()
        
        return JsonResponse({ "result" : (json.loads(serialize('json', [template])))[0]})


#PREVIEW TEMPLATE IN WEB BROWSER
def previewTemplate(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'preview.html', {"usertemplate":usertemplate})