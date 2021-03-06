"""nhom_middle_proxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.staticfiles import views

from main.views import *

routers = DefaultRouter()
routers.register(r'persons', PersonViewSet, basename="person")
routers.register(r'managers', ManagerViewSet, basename="managers")
routers.register(r'states', StateViewSet, basename="states")
routers.register(r'passports', PassportViewSet, basename="passport")
routers.register(r'gun', GunViewSet, basename="gun")
routers.register(r'finger', FingetPrintViewSet, basename="finger")
routers.register(r'drive', DriversViewSet, basename="drive_licence")
routers.register(r'bank', BankAccountViewSet, basename="bank_account")
routers.register(r'blood', BloodViewSet, basename="bloods")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


urlpatterns += staticfiles_urlpatterns()