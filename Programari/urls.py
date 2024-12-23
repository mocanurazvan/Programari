"""
URL configuration for Programari project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from planificator.views import IndexPlanificatorView
from serviciu.views import IndexServiciiView
from .views import pagina_acasa, pagina_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", pagina_acasa, name="home"),
    path("servicii", IndexServiciiView.as_view(), name="services"),
    path("planificator", IndexPlanificatorView.as_view(), name="planificator"),
    path("contact", pagina_contact, name="contact"),

]
