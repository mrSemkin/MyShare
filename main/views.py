from django.views.generic.base import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django import forms
from django.shortcuts import render
from .forms import UserLoginForm
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import HelpRequest, Beneficiary, User
from django.views.generic import DetailView, TemplateView


def index(request):
    msg = {'url': 'main/index.html',
           'msg': 'WELCOME'}
    return render(request, msg['url'], msg)


def about(request):
    msg = {'url': 'main/about.html',
           'msg': 'xx',
           'new_user': 'DDDDDDD'}

    return render(request, msg['url'], msg)


def general_reports(request):
    msg = {'url': 'main/general_reports.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def feedback(request):
    msg = {'url': 'main/feedback.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def login(request):
    msg = {'url': 'main/login.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def user_registration(request):
    msg = {'url': 'main/user_registration.html',
           'new_user': 'ddd',
           'msg': ''}
    return render(request, msg['url'], msg)


def partners(request):
    msg = {'url': 'main/partners.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def new_partner(request):
    msg = {'url': 'main/new_partner.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def fund_project(request):
    msg = {'url': 'main/fund_project.html',
           'msg': ''}
    return render(request, msg['url'], msg)


def police(request):
    msg = {'url': 'main/police.html',
           'msg': 'po po po '}
    return render(request, msg['url'], msg)


from django.contrib.auth import update_session_auth_hash


def user_cabinet(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return render(request, 'main/index.html')

        user = User.objects.get(id=request.user.id)
        # Оновлення полів користувача з POST-запиту
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        new_password = request.POST.get('password1')
        if new_password:
            user.set_password(new_password)

        user.save()

        update_session_auth_hash(request, user)  # Оновлення ключа сеансу
        login(request, user)
        return render(request, 'main/index.html', {})  # Відобразити якусь сторінку після редагування профілю

    else:  # Якщо це GET-запит (відобразити форму з поточними даними)
        user = User.objects.get(id=request.user.id)  # Отримання поточного користувача для відображення даних у формі
        msg = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        update_session_auth_hash(request, user)  # Оновлення ключа сеансу
        login(request, user)
        # return render(request, 'edit_profile.html', {'user': user})
        return render(request, 'main/user_cabinet.html', msg)
    # return render(request, 'main/user_cabinet.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)  # Ensure login is the one imported from django.contrib.auth
                    # After successful login, redirect as needed
                    return redirect('index')
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'main/login.html', {'form': form})


# Реєстрація шляху у файлі маршрутизації:

# def login_form(request):
#     form = UserLoginForm()  # Створення екземпляру форми
#
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # Тут виконайте перевірку користувача, як я показував раніше
#
#     return render(request, 'main/login.html', {'form': form})


from django.contrib.auth import get_user


def logout(request):
    request.session.flush()
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def login_as_guest(request):
    if request.user.is_authenticated:
        return redirect('index')

    guest = User.objects.create_user(username='guest', password='guest_password')
    guest.is_guest = True
    guest.save()

    # Аутентифікація новоствореного користувача
    user = authenticate(username='guest', password='guest_password')
    login(request, user)

    return redirect('about')  # Замість 'home' вкажіть вашу домашню сторінку


def add_user(request):
    if request.method == 'POST':
        uname = request.POST.get('username')  # Отримуємо значення з поля username форми
        email = request.POST.get('email')  # Отримуємо значення з поля email форми
        password = request.POST.get('password')  # Отримуємо значення з поля password форми
        # Отримуємо значення з поля password2 форми (якщо ви плануєте використовувати його для підтвердження)

        # Перевірка та збереження в БД
        if uname and email and password:  # Перевірка на пусті значення (можна додати інші перевірки)
            user = User.objects.create_user(username=uname, password=password, email=email)
            user.is_guest = False
            user.save()

    return render(request, 'main/login.html', {})  # Змініть 'шаблон_після_реєстрації.html' на свій шаблон


def help_request_list(request):
    help_requests = HelpRequest.objects.filter(status=HelpRequest.ACTUAL, beneficiary__isnull=False)
    return render(request, 'main/help_request_list.html', {'help_requests': help_requests})


class MyCustomView(DetailView):
    model = HelpRequest
    template_name = 'main/help_request_inf.html'
    context_object_name = 'help_request'


