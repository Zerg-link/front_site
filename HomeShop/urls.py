"""HomeShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from home import views
from home.models import *

house_list = views.HouseListView.as_view(
        queryset=House.objects.order_by('price'),
        context_object_name="House_list",
        template_name="home/home.html",
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", house_list, name="Home"),
    path("Calculator", views.Calculator, name="Calculator"),
    
    path("SignUp", views.SignUp, name="SignUp"),
    path("SignIn", views.SignIn, name="SignIn"),
    path("Favourites", views.Favourites, name="Favourites"),
    path("Account", views.FollowHome, name="Account"),
    path("SignOut", views.SignOut, name="SignOut"),

    path("CreateHouse", views.NewHouse, name="CreateHouse"),
]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
