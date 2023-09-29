from django import forms
from olxvehicle.models import OlxVehicle
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class OlxCreateForm(forms.ModelForm):
    class Meta:
        model=OlxVehicle
        fields="__all__"
        widgets={
           "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
           "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
           "owner_name":forms.TextInput(attrs={"class":"form-control"}),
           "vehicle_model":forms.TextInput(attrs={"class":"form-control"}),
           "kms_run":forms.NumberInput(attrs={"class":"form-control"})




        }

class OlxChangeForm(forms.ModelForm):
    class Meta:
        model=OlxVehicle
        fields="__all__"
        widgets={
           "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
           "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
           "owner_name":forms.TextInput(attrs={"class":"form-control"}),
           "vehicle_model":forms.TextInput(attrs={"class":"form-control"}),
           "kms_run":forms.NumberInput(attrs={"class":"form-control"})




        }