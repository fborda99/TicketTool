"""TicketTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from AppTickets.views import *
from AppIT_Team.views import *
from AppEmployees.views import *
from AppMessages.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage, name='homepage'),
    path("", include("AppTickets.urls")),
    path("AppIT_Team/", include("AppIT_Team.urls")),
    path("AppEmployees/", include("AppEmployees.urls")),
    path("AppMessages/", include("AppMessages.urls")),
]

urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)