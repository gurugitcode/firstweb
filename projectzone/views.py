from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import View
from django.contrib.auth.models import User ,Group
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import UserCreateforms,LoginForm
from . models import ContectModel
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

# Home Class based views function
class MainView(View):
    template_name="webzone/home.html"
    def get(self, request):
        return render(request, self.template_name)

# AboutView Class based views function
class AboutView(View):
    template_name="webzone/about.html"
    def get(self, request):
        return render(request, self.template_name)

# ContectView Class based views function
class ContectView(View):
    template_name="webzone/contect.html"
    def get(self, request):
        return render(request, self.template_name)

# ServiceView Class based views function
class ServiceView(View):
    template_name="webzone/services.html"
    def get(self, request):
        return render(request, self.template_name)

# PortFolioView Class based views function
class PortFolioView(View):
    template_name="webzone/portfolio.html"
    def get(self, request):
        return render(request, self.template_name)

# BlogView Class based views function
class BlogView(View):
    template_name="webzone/blog.html"
    def get(self, request):
        return render(request, self.template_name)


# BlogView Class based views function
class DashboardView(View):
    template_name="webzone/dashboard.html"
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect('/home/home')


# CreateAccountView Class based views function
class CreateAccountView(View):
    def get(self,request):
        return JsonResponse({"status":0})
    def post(self,request):
        if request.method=='POST':
            print('after_---------------------------')
            fm=UserCreateforms(request.POST)
            if fm.is_valid():
                messages.success(request, "Congratulations Your account created")
                user=fm.save()
                group = Group.objects.get_or_create(name="Author")
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                print('succsessfully upload data')
                return JsonResponse({"status":"Save"})
        else:
            return JsonResponse({"status":"Field"})
        return JsonResponse({"status":"Field"})

# LoginFormView Class based views function
class LoginFormView(View):
    def post(self,request):
        if request.method=='POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    group = Group.objects.get(name='Author')
                    group.user_set.all()
                    return JsonResponse({"status":"Save"})
        else:
            return JsonResponse({"status":"Faield"})
        return JsonResponse({"status":"Faield"})
# Logout_User
class User_logout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

class ContectUserDataView(View):
    template_name="index.html"
    def get(self,request):
        return JsonResponse({"status":0})
    
    def post(self,request):
        # print(request.POST)
        if request.method=='POST':
            name=request.POST["name"]    
            email=request.POST["email"]    
            subject=request.POST["subject"]    
            message=request.POST["message"]    
            print('succsessfully upload data')
            reg=ContectModel(name=name,email=email,subject=subject,message=message)
            reg.save()
            return JsonResponse({"status":"Save"})
        else:
            return JsonResponse({"status":0})
       