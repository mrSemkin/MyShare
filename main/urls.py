from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('general_reports/', views.general_reports, name='general_reports'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('partners/', views.partners, name='partners'),
    path('new_partner/', views.new_partner, name='new_partner'),
    path('fund_project/', views.fund_project, name='fund_project'),
    path('police/', views.police, name='police'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_URL)

