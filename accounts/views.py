from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from builder.models import UserTemplate, Template

from django.views.decorators.csrf import csrf_protect 



# Create your views here.
def index(request):
  return render(request,'index.html')

@csrf_protect
def signup(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else: 
    form = RegisterForm()
  return(render(request, 'registration/signup.html', {"form": form}))

def logout_view(request):
    logout(request, 'login.html')

@login_required(login_url='/login/')
def home(request):
  # return render(request, 'allTemplates.html')
  usertemplates = UserTemplate.objects.all().filter(created_by=request.user).order_by('-created_at')
  return render(request, 'myTemplates.html', {"usertemplates":usertemplates})

@login_required(login_url='/login/')
def portfolio(request):
  return render(request, 'portfolio.html')

@login_required(login_url='/login/')
def landingpages(request):
  return render(request, 'landingPage.html')

#might be removed
@login_required(login_url='/login/')
def mytemplates(request):
  return render(request, 'myTemplates.html')

@login_required(login_url='/login/')
def alltemplates(request):
  templates = Template.objects.all()
  return render(request, 'allTemplates.html', {"templates":templates})
  

@login_required(login_url='/login/')
def blogs(request):
  return render(request, 'blog.html')

def about(request):
  return render(request, 'about.html')

def support(request):
  return render(request, 'support.html')