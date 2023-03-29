from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapForm
from app01.utils.md5 import md5_password
# Create your views here.

class UserLogin(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5_password(pwd)

class UserRegister(BootStrapForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput
    )
    ppassword = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput
    )
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5_password(pwd)
        ppwd = self.cleaned_data.get('ppassword')
        return md5_password(ppwd)

def one(request):
    return render(request, 'one.html')

def index(request):
    return render(request, 'index.html')

def impression(request):
    return render(request, 'impression.html')

def login(request):

    if request.method == 'GET':
        form = UserLogin()
        return render(request, 'login.html', {"form": form})
    form = UserLogin(data=request.POST)
    if form.is_valid():

        user_object = models.userinfo.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password", '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session["infor"] = {'id': user_object.id, 'name': user_object.username}
        return redirect('/one/impression')

def register(request):
    if request.method =='GET':
        form = UserRegister()
        return render(request, 'register.html', {'form': form})
    form = UserRegister(data=request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        object = models.userinfo.objects.filter(username=form.cleaned_data['username']).first()
        if object:
            form.add_error('username', '用户已存在')
            return render(request, 'register.html', {'form': form})
    # print(user_object.username, u)ser_object.password
        return HttpResponse('驻车成功')



