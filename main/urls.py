from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings




urlpatterns = [

                  path('', views.index, name='home'),
                  path('index/', views.index, name='index'),
                  path('about/', views.about, name='about'),
                  path('general_reports/', views.general_reports, name='general_reports'),
                  path('feedback/', views.feedback, name='feedback'),
                  path('partners/', views.partners, name='partners'),
                  path('new_partner/', views.new_partner, name='new_partner'),
                  path('fund_project/', views.fund_project, name='fund_project'),
                  path('police/', views.police, name='police'),
                  path('user_cabinet/', views.user_cabinet, name='user_cabinet'),

                  path('login/', views.custom_login, name='login'),
                  path('user_registration/', views.user_registration, name='user_registration'),
                  path('add_user/', views.add_user, name='add_user'),
                  # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', views.logout, name='logout'),

                  path('login/guest/', views.login_as_guest, name='login_as_guest'),  # URL для увходу як гість
                  path('help_request_list/', views.help_request_list, name='help_request_list'),
                  path('help_request_list/<int:pk>/', views.MyCustomView.as_view(), name='HelpRequest_inf'),
                  path('help_request_list/<int:pk>/donate_financial/', views.FinancialDonateView.as_view(),name='Financial_Donate'),
                  path('help_request_list/<int:pk>/donate_material/', views.MaterialDonateView.as_view(),name='Material_Donate'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
