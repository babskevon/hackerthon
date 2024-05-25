"""agentant URL Configuration

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
from delivery.views import Index, PickPoint, Deliver, Available, PickUp, FirstPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", FirstPage.as_view(), name="index"),
    path("register/", Index.as_view(), name="register"),
    path("pick/", PickPoint.as_view(), name="pick"),
    path("deliver/", Deliver.as_view(), name="deliver"),
    path("all/", Available.as_view(), name="all-available"),
    path("all/<int:id>/approve", PickUp.as_view(), name="approve"),
]
