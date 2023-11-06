from django.shortcuts import render
from .models import Beneficiary

from django.http import HttpResponse


def index(request):
    msg = {'url': 'main/index.html',
           'msg': 'WELCOME'}
    return render(request, msg['url'],  msg)


def about(request):
    msg = {'url': 'main/about.html',
           'msg': 'xx'}
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


def want_to_help(request):
    beneficiaries = Beneficiary.objects.all()
    return render(request, 'main/want_to_help.html', {'beneficiaries': beneficiaries})


def beneficiary_detail(request, beneficiary_id):
    beneficiary = Beneficiary.objects.get(pk=beneficiary_id)
    return render(request, 'beneficiary_detail.html', {'beneficiary': beneficiary})


def user_cabinet(request):

    return render(request, 'user_cabinet.html')


def style(request):
    return
