import json

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse

from .forms import RussianUserCreationForm

## Отображает форму авторизации.
"""
def login(request):
    res_dict= {}
    res_dict.update(csrf(request))
    if request.POST:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user_name = request.POST['username']
            user_password = request.POST['password']
            user = auth.authenticate(username=user_name,
                                    password=user_password)
            if user:
                auth.login(request, user)
                return redirect('/')
        res_dict['error'] = ('Введены неверные логин или пароль, '
                             'либо такого пользователя не существует.')
         
    res_dict['form'] = AuthenticationForm
    return render_to_response('login.html', res_dict)
"""

def login(request):
    if request.POST:
        if request.is_ajax():
            print(request.POST)
            print('fsdf')
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                print('valid')
                user_name = request.POST['username']
                user_password = request.POST['password']
                user = auth.authenticate(username=user_name,
                                    password=user_password)
                if user:
                    auth.login(request, user)
                    res = {'result': 'success'}
                    print(res)
                else:
                    res = {'result': 'Неверный пользователь или пароль'}
            else:
                res = {'result': 'Заполните все поля'}
            print(res)
            return HttpResponse(json.dumps(res))
    else:
        print('here')            
        res_dict= {}
        res_dict.update(csrf(request))
        res_dict['form'] = AuthenticationForm
        return render_to_response('login.html', res_dict)


## Выходит из системы.
def logout(request):
    auth.logout(request)
    return redirect('/')

## Отображает форму регистрации.
def registrate(request):
    res_dict = {}
    if request.POST:
        form = RussianUserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user_name = request.POST['username']
            user_password = request.POST['password1']
            new_user = auth.authenticate(username=user_name,
                                        password=user_password)

            auth.login(request, new_user)
            return redirect('/')
        else:
            res_dict['error'] = 'Неверно введены поля или такой пользователь уже существует.'
    form = UserCreationForm()
    res_dict['form'] = form
    res_dict.update(csrf(request))
    return render_to_response('registration.html', res_dict)

## Выводит форму регистрации.
def registrate_ajax(request):
    ## Если нет JAVASCRIPT У ПОЛЬЗОВАТЕЛЯ, МОИ ДЕЙСТВИЯ?
    res_dict ={}
    if request.method == "POST":
        if request.is_ajax:
            form = UserCreationForm(data = request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
                user_name = request.POST['username']
                user_password = request.POST['password1']
                new_user = auth.authenticate(username=user_name,
                                            password=user_password)
                auth.login(request, new_user)
                return HttpResponse(json.dumps({'result': 'success'}))
            return HttpResponse(json.dumps({'result': 'error'}))
    form = RussianUserCreationForm()
    res_dict['form'] = form
    res_dict.update(csrf(request))
    return render_to_response('registration.html', res_dict)





                    