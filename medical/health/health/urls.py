"""health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views
# #update by naitik
# from doctor import views as doc_views
# from patient import views as pat_views

urlpatterns = [
    path('',views.home,name='home'),
    path('patient/',include('patient.urls')),
    path('doctor/',include('doctor.urls')),
    path('hospital/',include('hospital.urls')),
    path('admin/', admin.site.urls),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('seedocs', views.seedocs),
]
