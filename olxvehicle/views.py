from django.shortcuts import render,redirect
from django.views.generic import View
from olxvehicle.forms import OlxCreateForm,OlxChangeForm,RegistrationForm,LoginForm
from olxvehicle.models import OlxVehicle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect('signin')
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # form.save()
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                print ("credentials are valid")
                return redirect("olx-list")
            else:
                print("invalid credentials")
                return render(request,"login.html",{"form":form})
            
class OlxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=OlxCreateForm()
        
        return render(request,"olx_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=OlxCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            OlxVehicle.objects.create(**form.cleaned_data)
        

            return render(request,"olx_add.html",{"form":form})
        else:
            return render(request,"olx_add.html",{"form":form})
class OlxListView(View):
    def get(self,request,*args,**kwargs):   
         qs=OlxVehicle.objects.all()
         return render(request,"olx_list.html",{"olxs":qs}) 
    
class OlxDeleteView(View):
    def get(self,request,*args,**kwargs):  
         id=kwargs.get("pk") 
         qs=OlxVehicle.objects.filter(id=id).delete()
         return redirect("olx-list")

    
class OlxDetailView(View):
    def get(self,request,*args,**kwargs):  
         id=kwargs.get("pk") 
         qs=OlxVehicle.objects.get(id=id)
         return render(request,"olx_detail.html",{"olx":qs})    

class OlxUpdateView(View):
    def get(self,request,*args,**kwargs):  
         id=kwargs.get("pk") 
         obj=OlxVehicle.objects.get(id=id)
         form=OlxChangeForm(instance=obj)
         return render(request,"olx_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
         id=kwargs.get("pk") 
         obj=OlxVehicle.objects.get(id=id)
         form=OlxChangeForm(request.POST,instance=obj,files=request.FILES)
         if form.is_valid():
            form.save()
           
        

            return redirect("olx-list")
         else:
           
         
         
             return render(request,"olx_edit.html",{"form":form})

    

    
       



# Create your views here.
