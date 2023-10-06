from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    # return HttpResponse("<h1>About page</h1")
    print(request.GET);
    print(request.POST);
    ddd = {'name': request.GET.get('name')};
    return render(request, 'main/about.html', ddd);

def style(request):
    return
